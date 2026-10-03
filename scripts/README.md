# Validación documental

Desde la raíz: `python3 scripts/validar.py`. Requiere Python 3.9+ y solo biblioteca estándar. No escribe datos ni hace conexiones de red.

Salida 0: estructura revisada sin errores. Salida 1: corregir errores antes de integrar. Los avisos PENDIENTE no significan aprobación de entrega. Durante el arranque los índices están vacíos deliberadamente.

Autor/revisor en CSV: usar JDOG, JACD, DQH o EJVA. Las relaciones EV ↔ PT deben estar en ambos índices, separadas por punto y coma cuando hay varias. Cada archivo registrado tiene ID propio. Un hallazgo confirmado necesita evidencia, severidad y otro integrante como revisor. Los detalles se revisan en la ficha, no se certifican automáticamente.

El control se comprobó con una copia temporal: registro coherente aceptado y cambio del archivo de evidencia detectado por hash. No se guardaron esos datos ficticios en los registros reales.
