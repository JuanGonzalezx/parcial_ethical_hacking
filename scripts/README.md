# Validación documental

Desde la raíz: `python3 scripts/validar.py`. Requiere Python 3.9+ y solo biblioteca estándar. No escribe datos ni hace conexiones de red.

Salida 0: estructura revisada sin errores. Salida 1: corregir errores antes de integrar. Los avisos PENDIENTE no significan aprobación de entrega. El índice de evidencias ya contiene 13 registros; el índice de hallazgos sigue vacío al no haber fichas validadas.

Autor/revisor en CSV: usar JDOG, JACD, DQH o EJVA. Las relaciones EV ↔ PT deben estar en ambos índices, separadas por punto y coma cuando hay varias. Cada archivo registrado tiene ID propio. Un hallazgo confirmado necesita evidencia, severidad y otro integrante como revisor. Los detalles se revisan en la ficha, no se certifican automáticamente.

El control se comprobó con una copia temporal: registro coherente aceptado y cambio del archivo de evidencia detectado por hash. No se guardaron esos datos ficticios en los registros reales.

El inventario `cherrytree/cuadernos.json` identifica los cuatro archivos activos (CTB/CTD). Para CTB se comprueba integridad SQLite, XML interno, jerarquía, referencias de objetos y banderas de imágenes. La validación se hace en lectura solamente. `no-registrada` es una fecha desconocida explícita y produce aviso, nunca una fecha inventada.

## Generación del PDF

`generar_pdf.py` usa ReportLab, Pillow y pypdf; requiere Arial del sistema macOS en esta versión. Ejecutarlo con un Python que tenga esas dependencias. Lee informe/INFORME.md y docs/GUIA_SUSTENTACION.md y produce los dos PDF en output/pdf. Actualiza únicamente figura/pagina_pdf del índice de evidencias; no modifica PNG ni CherryTree. Tras regenerar, revisar el PDF, recalcular su manifiesto y verificar enlaces, figuras y páginas antes de compartir. El script no ejecuta pruebas de red.
