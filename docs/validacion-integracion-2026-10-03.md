# Validación de integración · 2026-10-03

PARCIAL_PENTEST_JAIME_DC1.ctb: 4 textos no vacíos y 2 imágenes originales preservados; 32 nodos actuales.

WriteUp_Basic_Pentesting1--parcial1EDuardo.ctb: 1 textos no vacíos y 11 imágenes originales preservados; 40 nodos actuales.

Se verificaron los hashes de los seis respaldos y la preservación exacta de los textos originales no vacíos y de todas las filas de imagen originales, incluidos BLOB y offset. El validador acepta la estructura final y los 13 hashes de evidencia. En copias temporales, rechazó una evidencia alterada y un ciclo de jerarquía SQLite. No se modificaron los registros reales para esas pruebas.

Pendiente: apertura/guardado en la aplicación CherryTree del equipo. La validación estructural no comprueba visualmente el renderizado ni reproduce pruebas de red.
