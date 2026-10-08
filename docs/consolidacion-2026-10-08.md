# Consolidación por estrategias - 8 de octubre de 2026

Se revisaron nodos e imágenes de los cuadernos activos completos, sin depender de que los autores siguieran las plantillas. Los cuatro archivos CTB/CTD quedaron byte a byte iguales a HEAD. Eduardo contiene 22 ocurrencias de imagen correspondientes a las 11 evidencias originales duplicadas en la reorganización; sus notas posteriores de acceso/root siguen como reportadas. Jaime contiene 34 imágenes, todas vinculadas a evidencia. Se incluyeron también todas las capturas image*.png de Daniel, aunque su CTD no las contiene.

Se incorporaron 27 evidencias: 14 de Jaime y 13 de Daniel. El índice tiene 74 EV. El inventario con nodo/offset y hash está en evidencias/procedencia-2026-10-08.json. La inclusión no transforma investigación o configuración en explotación confirmada.

Hallazgos documentales corregidos: existe captura del final de ssh_enumusers, pero no identificación de usuarios válidos; flag4 ya figura como candidato. Versiones de Metasploit visibles: Jaime 6.5.3-dev y Daniel 6.5.4-dev. Se recuperaron estabilización TTY, error de sudo, inventario SUID y lectura de shadow. El hash de shadow no sustituye la evidencia pendiente del origen del hash Drupal.

El informe v0.4 usa cuatro estrategias: reconocimiento; acceso web; autenticación SSH; escalamiento/impacto/cierre. No contiene etiquetas LAB. Se conservaron IP, MAC, autores y EV para no mezclar pruebas. Se eliminaron marcadores EV-DQH-XXX y referencias a transcripciones externas como requisito de lectura. PT-006 ya no asigna impacto bajo sin demostración.

Validación: PDF de 100 páginas, 25 marcadores de apartado y 74 figuras con página, ID e imagen verificados; hashes originales correctos. Guía de 12 páginas. Se renderizaron ambas salidas y se revisaron todas sus páginas en vistas de conjunto. Persisten las limitaciones de precisión de fechas, datos de aislamiento, revisión cruzada, severidades y limpieza; no se ejecutaron nuevas pruebas ni se fabricaron resultados.

## Edición grupal v0.5

Por solicitud del equipo, el informe usa autoría MnzHack en relato y figuras, conservando los cuatro nombres en portada. Los autores originales permanecen en índices, fichas y cuadernos para trazabilidad. Se añadió en Enumeración un bloque que integra las once evidencias de Eduardo por pasos y decisiones, con límites explícitos para los accesos solo reportados. PDF: 101 páginas, 74 figuras. La guía interna conserva el reparto sugerido de exposición.
