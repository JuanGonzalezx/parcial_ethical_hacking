# Cuadernos de trabajo · Estructura de Jaime

Usar únicamente estos cuatro archivos activos. `cuadernos.json` es el inventario que lee el validador.

| Autor | Código | Archivo activo |
|---|---|---|
| Juan David | 38402 | individuales/JDOG_38402.ctd |
| Jaime | 40549 | individuales/PARCIAL_PENTEST_JAIME_DC1.ctb |
| Daniel | 31429 | individuales/DQH_31429.ctd |
| Eduardo | 37831 | individuales/WriteUp_Basic_Pentesting1--parcial1EDuardo.ctb |

Jaime y Eduardo continúan en los **mismos .ctb que compartieron**, ahora organizados y ampliados. Sus plantillas .ctd vacías se retiraron de individuales para evitar dos archivos activos por persona; se conservan en `respaldos/2026-10-03-antes-integracion/`. También se respaldaron los .ctb recibidos y los otros dos .ctd antes de editar, con `SHA256.json`.

## Árbol común

```text
00 Control documental
01 Pre-Engagement
   Alcance / Rules of Engagement / Clasificación
02 Intelligence Gathering
   Descubrimiento / Puertos / Servicios
03 Enumeración
   Resultados por servicio o evidencia
04 Threat Modeling
05 Vulnerability Analysis
06 Exploitation
07 Post-Exploitation
08 Escalamiento
09 Proof of Compromise
10 Evidencias (capturas sueltas)
11 Reporting y defensa
12 Plantillas de trabajo
```

Se conserva la organización 01–10 de Jaime, con control, reporting y plantillas complementarios. Es una descomposición de trabajo de PTES: Enumeración amplía Intelligence Gathering; Escalamiento y Proof of Compromise se relacionan con Post-Exploitation. No son doce fases oficiales nuevas. El informe mantiene los 25 apartados exigidos.

En Jaime, `Alcance` se movió a Pre-Engagement. Sus dos capturas permanecen en el nodo de descubrimiento; las correcciones se agregaron en un nodo de revisión sin alterar su texto original. En Eduardo, `90 Registro recibido sin modificar` conserva el nodo original íntegro. Las once capturas se repiten bajo las fases correspondientes, con ID EV e interpretación. Esa duplicación es intencional: el registro de origen se conserva y las copias organizadas facilitan continuar.

## Continuar trabajando

1. Abrir el archivo activo después de sincronizar esta actualización. Si hay una copia anterior abierta, cerrarla sin sobrescribir el archivo actualizado; conservar aparte cualquier nota nueva aún no sincronizada.
2. Completar control y alcance de la instancia propia: LAB-JACD usa .18.130; LAB-EJVA usa .81.130. No mezclar IP, puertos dinámicos ni capturas.
3. Duplicar una plantilla en su fase, registrar fecha real y el comando exacto. No usar la fecha de modificación del nodo como fecha de prueba.
4. Conservar originales y actualizar `evidencias/indice.csv`; usar EV-ALIAS-NNN. Reservar PT-NNN solo para una ficha específica; puertos abiertos no son vulnerabilidades por sí solos.
5. Cerrar el cuaderno antes de sincronizar. Cada autor edita su archivo; evitar cambios simultáneos.
6. Revisar los pendientes del nodo Control y `docs/revision-cherrytree-2026-10-03.md`.

SQLite y XML fueron validados estructuralmente y las imágenes comparadas con los BLOB originales. Sigue pendiente una comprobación de apertura/guardado en la aplicación CherryTree del equipo. Ambos formatos son sin cifrar.

## Consolidación

Al cierre, respaldar las cuatro versiones. Crear desde CherryTree `consolidado/MnzHack_DC-1.ctd` o `.ctb` e importar cada documento usando la función de importación de CherryTree instalada. Mantener una raíz por autor, verificar imágenes, tablas, enlaces y cajas de código y conservar EV/PT visibles aunque la aplicación reasigne IDs. No combinar SQLite/XML por concatenación ni resolver conflictos binarios eligiendo una copia a ciegas.

Consolidar hallazgos según causa e instancia sin perder autoría; trasladar el contenido revisado al informe. La entrega académica sigue siendo **un único PDF con toda la evidencia integrada**.
