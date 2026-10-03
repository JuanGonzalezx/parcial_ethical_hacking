# MnzHack · Pentest DC-1

Seguridad Informática · Parcial Global Ethical Hacking y Penetration Testing PTES.
Trabajo: **3–8 de octubre de 2026**, zona America/Bogota. Entrega: jueves 8; hora y canal pendientes de confirmar.

| Integrante | Código | Alias documental |
|---|---|---|
| Juan David Ocampo Gonzalez | 38402 | JDOG |
| Jaime Andres Cardona Diaz | 40549 | JACD |
| Daniel Quintero Hurtado | 31429 | DQH |
| Eduardo Jose Villamil Arce | 37831 | EJVA |

## Empezar aquí

1. Leer [análisis del parcial](docs/01-analisis-parcial.md) y [alcance y reglas](docs/02-alcance-roe.md).
2. Consultar [estado y tareas](docs/estado.md). Antes de continuar pruebas, completar identificación y aislamiento del laboratorio.
3. Abrir el archivo propio en [cherrytree/individuales](cherrytree/individuales); seguir [su guía](cherrytree/README.md).
4. Documentar cada sesión y conservar salidas originales. Registrar evidencias en [el índice](evidencias/indice.csv).
5. Revisar y promover resultados a [hallazgos](hallazgos/README.md), fases [PTES](docs/ptes) e [informe](informe/INFORME.md).
6. Ejecutar `python3 scripts/validar.py`. Es un control estructural; no certifica resultados ni sustituye revisión visual del PDF.

## Mapa del repositorio

| Ruta | Función |
|---|---|
| `Docs_Base/` | Fuentes del docente y material de clase; conservar originales |
| `AGENTS.md`, `CLAUDE.md` | Instrucciones comunes para asistentes |
| `specs/` | Especificación, plan y tareas SDD |
| `docs/` | Rúbrica, alcance, arquitectura, decisiones y seguimiento |
| `cherrytree/` | Cuatro cuadernos individuales y área de consolidación |
| `plantillas/` | Sesión, hallazgo, evidencia y especificación de prueba |
| `evidencias/` | Capturas, salidas e índice con SHA-256 |
| `hallazgos/` | Fichas revisadas e índice de estados |
| `informe/` | Fuente editorial con los 25 apartados obligatorios |
| `entregables/` | Único PDF final, cuando esté verificado |
| `scripts/` | Controles documentales locales, sin escaneos |
| `private/` | Material sensible local, excluido de Git; no es respaldo |

## Estado inicial

No hay resultados técnicos de DC-1 incorporados ni vulnerabilidades confirmadas. Jaime y Eduardo comenzaron reconocimiento, según lo reportado por Juan; faltan sus evidencias. No se inventan IP, puertos, versiones, CVE, flags ni acceso root.

La tabla del docente dice **Mzlhack → DC-1**; se usa **MnzHack** según el equipo y se registra la discrepancia. Los walkthroughs específicos de DC-1 están prohibidos por el enunciado (§16); usar documentación general y fuentes técnicas primarias.

**Entrega académica:** `PARCIAL_PENTEST_MnzHack_DC-1.pdf`. El repositorio y CherryTree son herramientas internas: toda evidencia necesaria debe estar integrada y explicada dentro del único PDF.
