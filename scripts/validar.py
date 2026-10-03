#!/usr/bin/env python3
"""Valida estructura documental; no ejecuta pruebas de red ni altera evidencia."""
import csv
import json
import sqlite3
import hashlib
import re
import sys
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
AUTHORS = {'JDOG', 'JACD', 'DQH', 'EJVA'}
ERRORS = []
WARNINGS = []


def error(message):
    ERRORS.append(message)


def safe_file(value):
    """Solo archivos dentro del repositorio, incluso al resolver symlinks."""
    path = (ROOT / value).resolve()
    if not value or Path(value).is_absolute() or ROOT not in path.parents:
        raise ValueError(f'ruta no relativa al repositorio: {value!r}')
    if not path.is_file():
        raise ValueError(f'archivo inexistente: {value}')
    return path


def read_index(name, columns, pattern):
    rows = {}
    try:
        with (ROOT / name).open(encoding='utf-8', newline='') as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != columns:
                error(f'{name}: cabecera inesperada')
                return rows
            for line, row in enumerate(reader, 2):
                if None in row or any(v is None for v in row.values()):
                    error(f'{name}:{line}: número incorrecto de columnas')
                    continue
                row = {k: v.strip() for k, v in row.items()}
                key = row['id']
                if not re.fullmatch(pattern, key) or key in rows:
                    error(f'{name}:{line}: ID inválido o repetido: {key}')
                    continue
                rows[key] = row
    except OSError as exc:
        error(str(exc))
    return rows


def refs(value):
    return {item.strip() for item in value.split(';') if item.strip()}


def main():
    ERRORS.clear()
    WARNINGS.clear()
    for required in ['README.md', 'AGENTS.md', 'CLAUDE.md',
                     'docs/01-analisis-parcial.md', 'docs/02-alcance-roe.md',
                     'docs/estado.md', 'specs/001-documentacion/spec.md',
                     'plantillas/HALLAZGO.md', 'informe/INFORME.md']:
        if not (ROOT / required).is_file():
            error(f'Falta {required}')
    report = ROOT / 'informe/INFORME.md'
    if report.exists():
        text = report.read_text(encoding='utf-8')
        headings = re.findall(r'^## (\d{2})\. ', text, re.M)
        if headings != [f'{n:02d}' for n in range(1, 26)]:
            error('Informe: se esperan 25 apartados numerados en orden')
        if 'PENDIENTE' in text:
            WARNINGS.append('Informe todavía contiene pendientes; no está listo para entregar.')
    books = []
    try:
        inventory = json.loads((ROOT / 'cherrytree/cuadernos.json').read_text())
        if len(inventory) != 4 or {r['autor'] for r in inventory} != AUTHORS:
            error('Inventario: se esperan cuatro autores únicos')
        if len({r['ruta'] for r in inventory}) != len(inventory):
            error('Inventario: rutas de cuadernos repetidas')
        books = [safe_file(r['ruta']) for r in inventory]
        active = set((ROOT / 'cherrytree/individuales').glob('*.ct[bd]'))
        if active != set(books):
            error('Hay cuadernos activos fuera del inventario o falta alguno')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        error(f'Inventario de cuadernos: {exc}')
    for book in books:
        try:
            if book.suffix == '.ctd':
                root = ET.parse(book).getroot()
                nodes = list(root.iter('node'))
                ids = [n.get('unique_id') for n in nodes]
                if root.tag != 'cherrytree' or not nodes:
                    error(f'{book.name}: estructura CherryTree vacía o incorrecta')
                if any(not value or not value.isdigit() for value in ids) or len(set(ids)) != len(ids):
                    error(f'{book.name}: IDs de nodo inválidos o duplicados')
                for n in nodes:
                    if not n.get('name') or not n.get('prog_lang'):
                        error(f'{book.name}: nodo sin nombre o formato')
            elif book.suffix == '.ctb':
                connection = sqlite3.connect(book.as_uri() + '?mode=ro', uri=True)
                try:
                    if connection.execute('pragma integrity_check').fetchall() != [('ok',)]:
                        error(f'{book.name}: integridad SQLite fallida')
                    nodes = connection.execute('select node_id,name,txt,has_image from node').fetchall()
                    ids = {n[0] for n in nodes}
                    edges = connection.execute('select node_id,father_id,sequence from children').fetchall()
                    if {e[0] for e in edges} != ids or len(edges) != len(ids):
                        error(f'{book.name}: nodos ausentes o duplicados en jerarquía')
                    parents = {n: parent for n, parent, _ in edges}
                    if sum(parent == 0 for parent in parents.values()) != 1:
                        error(f'{book.name}: debe haber una raíz activa')
                    positions = [(parent, seq) for _, parent, seq in edges]
                    if len(set(positions)) != len(positions):
                        error(f'{book.name}: orden de hermanos duplicado')
                    for node_id in ids:
                        seen = set()
                        current = node_id
                        while current != 0:
                            if current in seen or current not in parents:
                                error(f'{book.name}: ciclo o padre ausente desde {node_id}')
                                break
                            seen.add(current)
                            current = parents[current]
                    for node_id, name, txt, has_image in nodes:
                        if not name:
                            error(f'{book.name}: nodo sin nombre {node_id}')
                        if txt:
                            ET.fromstring(txt)
                        count = connection.execute('select count(*) from image where node_id=?', (node_id,)).fetchone()[0]
                        if bool(count) != bool(has_image):
                            error(f'{book.name}: bandera de imagen incoherente en {node_id}')
                    for table in ['image', 'codebox', 'grid', 'bookmark']:
                        for (node_id,) in connection.execute(f'select node_id from {table}'):
                            if node_id not in ids:
                                error(f'{book.name}: {table} referencia nodo ausente {node_id}')
                finally:
                    connection.close()
            else:
                error(f'{book.name}: formato no soportado')
        except (ET.ParseError, sqlite3.Error, OSError) as exc:
            error(f'{book.name}: {exc}')
    ev = read_index('evidencias/indice.csv',
                    ['id', 'fecha', 'autor', 'instancia', 'fase', 'ruta', 'sha256',
                     'descripcion', 'interpretacion', 'hallazgo_ids', 'figura', 'pagina_pdf'],
                    r'EV-(JDOG|JACD|DQH|EJVA)-\d{3,}')
    pt = read_index('hallazgos/indice.csv',
                    ['id', 'titulo', 'estado', 'autor', 'revisor', 'archivo',
                     'evidencia_ids', 'severidad'], r'PT-\d{3,}')
    for key, row in ev.items():
        for field in ['fecha', 'autor', 'instancia', 'fase', 'descripcion', 'interpretacion']:
            if not row[field]:
                error(f'{key}: falta {field}')
        if row['autor'] not in AUTHORS or not key.startswith(f"EV-{row['autor']}-"):
            error(f'{key}: autor incoherente con ID')
        if row['fecha'] == 'no-registrada':
            WARNINGS.append(f'{key}: fecha exacta no registrada; revisar precisión en ficha.')
        else:
            try:
                if datetime.fromisoformat(row['fecha']).utcoffset() is None:
                    raise ValueError('sin zona horaria')
            except ValueError:
                error(f'{key}: fecha ISO 8601 con zona o no-registrada requerida')
        try:
            path = safe_file(row['ruta'])
            digest = hashlib.sha256()
            with path.open('rb') as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b''):
                    digest.update(block)
            if digest.hexdigest() != row['sha256'].lower():
                error(f'{key}: SHA-256 ausente o no coincide')
        except (ValueError, OSError) as exc:
            error(f'{key}: {exc}')
        for ref in refs(row['hallazgo_ids']):
            if ref not in pt:
                error(f'{key}: hallazgo inexistente {ref}')
            elif key not in refs(pt[ref]['evidencia_ids']):
                error(f'{key}: relación con {ref} no es recíproca')
    for key, row in pt.items():
        if row['estado'] not in {'posible', 'en-validacion', 'confirmado', 'descartado'}:
            error(f'{key}: estado inválido')
        if not row['titulo'] or row['autor'] not in AUTHORS:
            error(f'{key}: título o autor inválido')
        try:
            safe_file(row['archivo'])
        except (ValueError, OSError) as exc:
            error(f'{key}: {exc}')
        evidence = refs(row['evidencia_ids'])
        for ref in evidence:
            if ref not in ev:
                error(f'{key}: evidencia inexistente {ref}')
            elif key not in refs(ev[ref]['hallazgo_ids']):
                error(f'{key}: relación con {ref} no es recíproca')
        if row['estado'] == 'confirmado':
            if not evidence or not row['severidad']:
                error(f'{key}: confirmado sin evidencia o severidad')
            if row['revisor'] not in AUTHORS or row['revisor'] == row['autor']:
                error(f'{key}: confirmado sin revisión de otro integrante')
    if not ev:
        WARNINGS.append('Sin evidencias incorporadas; índices vacíos válidos solo para arranque.')
    if not pt:
        WARNINGS.append('Sin hallazgos incorporados; no equivale a ausencia de vulnerabilidades.')
    for message in WARNINGS:
        print('PENDIENTE:', message)
    for message in ERRORS:
        print('ERROR:', message)
    print(f'{len(books)} cuadernos XML/SQLite · {len(ev)} evidencias · {len(pt)} hallazgos · {len(ERRORS)} errores')
    print('Control estructural solamente: no certifica CherryTree UI, CVSS ni PDF final.')
    return 1 if ERRORS else 0


if __name__ == '__main__':
    sys.exit(main())
