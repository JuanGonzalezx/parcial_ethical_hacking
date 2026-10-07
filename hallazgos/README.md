# Hallazgos

Hay ocho fichas incorporadas; consultar `indice.csv` y la revisión del 2026-10-07. Los resultados demostrados se distinguen de la revisión cruzada todavía pendiente. Reservar `PT-001`, `PT-002`, etc. en `indice.csv` coordinando con el integrador; crear la ficha desde `plantillas/HALLAZGO.md`.

Estados: `posible` (indicio), `en-validacion` (prueba en curso), `confirmado` (validación suficiente), `descartado` (indicio refutado con razón). Conservar descartados y errores útiles. Reabrir una ficha si cambia la evidencia.

Antes de confirmar: evidencia propia registrada, reproducción y precondiciones, causa, impacto, clasificación justificada y revisor diferente del autor. Antes del informe: completar recomendaciones y referencias. Varios pasos de una cadena pueden pertenecer a un mismo hallazgo; evitar duplicación artificial.

PT-002 y PT-008 comparten causa SUID en distintas instancias: no duplicar conteo. PHP Filter (PT-004) es una modificación administrativa durante la prueba; decidir su tratamiento como escenario posterior al compromiso. Las etiquetas de estado no sustituyen leer evidencia y límites de cada ficha.
