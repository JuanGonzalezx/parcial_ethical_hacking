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
| `cherrytree/` | Cuatro cuadernos activos, originales respaldados y área de consolidación |
| `plantillas/` | Sesión, hallazgo, evidencia y especificación de prueba |
| `evidencias/` | Capturas, salidas e índice con SHA-256 |
| `hallazgos/` | Fichas revisadas e índice de estados |
| `informe/` | Fuente editorial con los 25 apartados obligatorios |
| `entregables/` | Único PDF final, cuando esté verificado |
| `scripts/` | Controles documentales locales, sin escaneos |
| `private/` | Material sensible local, excluido de Git; no es respaldo |

## Estado actual al 8 de octubre

Rebase resuelto. **74 evidencias registradas y ocho fichas de hallazgo**. Jaime y Daniel aportan capturas de acceso inicial y privilegio efectivo root en instancias distintas. PDF v0.5 generado; faltan revisión cruzada, cierre de clasificaciones y datos de laboratorio. PT-002/PT-008 comparten causa; no equivalen a ocho vulnerabilidades únicas confirmadas.

Comenzar por [revisión y plan de cierre](docs/revision-2026-10-07/REVISION.md) y [estado actual](docs/estado.md). Se conservaron los cuadernos y las imágenes originales.

La tabla del docente dice **Mzlhack → DC-1**; se usa **MnzHack** según el equipo y se registra la discrepancia. Los walkthroughs específicos de DC-1 están prohibidos por el enunciado (§16); usar documentación general y fuentes técnicas primarias.

**Entrega académica:** `PARCIAL_PENTEST_MnzHack_DC-1.pdf`. El repositorio y CherryTree son herramientas internas: toda evidencia necesaria debe estar integrada y explicada dentro del único PDF.

Juan: [guía para continuar en UTM](docs/guia-JDOG-proxima-sesion.md). LAB-JDOG usa 192.168.128.4 como objetivo candidato; falta verificación de identidad/aislamiento; Nmap ya finalizó y la enumeración web está propuesta.

## Informe y preparación de defensa

- [Informe PDF v0.5](output/pdf/PARCIAL_PENTEST_MnzHack_DC-1.pdf): 101 páginas, 25 apartados y 74 evidencias integradas.
- [Guía interna de sustentación](output/pdf/GUIA_SUSTENTACION_MnzHack_DC-1.pdf): 12 páginas con evaluación, reparto, recorrido explicado y preguntas.
- [Fuente de la guía](docs/GUIA_SUSTENTACION.md). Los pendientes se declaran: no se garantiza nota ni aprobación final.
