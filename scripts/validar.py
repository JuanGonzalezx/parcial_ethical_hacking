#!/usr/bin/env python3
"""Valida estructura documental; no ejecuta pruebas de red ni altera evidencia."""
import csv
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
    books = sorted((ROOT / 'cherrytree/individuales').glob('*.ctd'))
    expected = {'JDOG_38402.ctd', 'JACD_40549.ctd', 'DQH_31429.ctd', 'EJVA_37831.ctd'}
    if {p.name for p in books} != expected:
        error('Se esperan los cuatro cuadernos individuales .ctd documentados')
    for book in books:
        try:
            root = ET.parse(book).getroot()
            nodes = list(root.iter('node'))
            ids = [n.get('unique_id') for n in nodes]
            if root.tag != 'cherrytree' or not nodes:
                error(f'{book.name}: estructura CherryTree vacía o incorrecta')
            if any(not value or not value.isdigit() for value in ids) or len(set(ids)) != len(ids):
                error(f'{book.name}: IDs de nodo inválidos o duplicados')
            for n in nodes:
                if not n.get('name') or n.get('prog_lang') != 'custom-colors':
                    error(f'{book.name}: nodo sin nombre o formato inesperado')
        except (ET.ParseError, OSError) as exc:
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
        try:
            if datetime.fromisoformat(row['fecha']).utcoffset() is None:
                raise ValueError('sin zona horaria')
        except ValueError:
            error(f'{key}: fecha ISO 8601 con zona requerida')
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
    print(f'{len(books)} cuadernos XML · {len(ev)} evidencias · {len(pt)} hallazgos · {len(ERRORS)} errores')
    print('Control estructural solamente: no certifica CherryTree UI, CVSS ni PDF final.')
    return 1 if ERRORS else 0


if __name__ == '__main__':
    sys.exit(main())
