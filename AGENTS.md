# Instrucciones del repositorio MnzHack

## Contexto y lectura inicial

Trabajo académico autorizado sobre la VM DC-1 aislada. Leer en orden `README.md`, `docs/estado.md`, `docs/02-alcance-roe.md`, `specs/001-documentacion/spec.md` y `docs/01-analisis-parcial.md`. Consultar la fase PTES y ficha de hallazgo relevantes antes de editar. La fuente académica es `Docs_Base/DocsParcial/Parcial_Global_Ethical_Hacking_PTES_CTF_Azul_Neon.pdf`.

## Integridad de la documentación

- Escribir en español. Diferenciar reportado por una persona, observado en evidencia, inferido y pendiente.
- No fabricar comandos ejecutados, resultados, fechas de pruebas, IP, versiones, CVE, CVSS, capturas ni acceso. Una plantilla no es una prueba realizada.
- Un banner o scanner no confirma una vulnerabilidad. Usar estados `posible`, `en-validacion`, `confirmado`, `descartado`; explicar falsos positivos.
- No consultar ni incorporar soluciones de walkthroughs de DC-1, conforme al §16. Usar documentación general y fuentes primarias; registrar URL, consulta y propósito.
- Preservar `Docs_Base/` y evidencias originales. No reemplazar salidas fallidas por resultados exitosos ni ocultar limitaciones.
- Toda afirmación del informe debe enlazar internamente con evidencia propia o referencia técnica. La entrega debe poder entenderse sin abrir archivos externos.

## Alcance de operación

La solicitud inicial es organizar y documentar; no ejecutar pruebas activas automáticamente. Para una futura ejecución, comprobar objetivo, instancia, red y condiciones de `docs/02-alcance-roe.md`. Solo DC-1 en Host-Only/Internal Network. Nada de redes institucionales, otras máquinas, DoS, borrado, persistencia permanente ni pivoteo. Los ejemplos de clase no amplían este alcance.

## Flujo SDD

1. Leer el estado y seleccionar tarea. Para una nueva prueba, copiar `plantillas/PRUEBA.md` a `specs/pruebas/` y definir objetivo, evidencia, límites y criterio de cierre.
2. Registrar hipótesis y procedimiento antes de ejecutarlo. Se permite evolución iterativa; documentar decisiones en `docs/decisiones.md`.
3. Documentar la sesión en el CherryTree del autor. Consultar `cherrytree/cuadernos.json`: dos CTB y dos CTD con el árbol de Jaime. No modificar simultáneamente cuadernos ni fusionar XML/SQLite a ciegas. Una reorganización solicitada por el usuario requiere respaldo, comprobación de integridad y preservación de textos e imágenes originales.
4. Registrar evidencia en `evidencias/indice.csv`, con ruta relativa, autor, instancia, fecha, descripción, interpretación y SHA-256. Si la fecha exacta no está sustentada, usar `no-registrada` y explicar la precisión disponible en su ficha; nunca inventar una hora. Los artefactos originales son inmutables; las versiones redactadas son archivos distintos.
5. Crear ficha desde plantilla y reservar PT-NNN en `hallazgos/indice.csv`. Revisar con otro integrante antes de incorporarla al informe.
6. Actualizar fase PTES, informe, tareas y estado sin declarar completa una fase que carece de evidencia.
7. Ejecutar `python3 scripts/validar.py`; comunicar sus límites y pendientes. No considerar su salida aprobación del PDF final.

## Cambios y cierre

Mantener `CLAUDE.md` como puente a este archivo para evitar reglas divergentes. No regenerar cuadernos con notas, sobrescribir originales ni crear resultados de ejemplo dentro de registros reales. No instalar un stack de aplicación para este repositorio documental. No publicar el repositorio, subir evidencias ni crear commits sin una solicitud que lo incluya. Al terminar, informar archivos, validación y pendientes concretos.
