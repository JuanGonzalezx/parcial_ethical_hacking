# TEST-JDOG-002 · Enumeración HTTP inicial

Estado: propuesta, sin ejecución recibida. Autor: JDOG. Instancia: LAB-JDOG, 192.168.128.4.
Origen: EV-JDOG-002 identifica HTTP/Apache y Drupal 7, y robots.txt anuncia CHANGELOG.txt.
Objetivo: documentar respuesta web y corroborar tecnología/versión, sin confundir indicios con vulnerabilidades.
Precondiciones: vincular IP/MAC a DC-1 y confirmar aislamiento UTM. Sin estas verificaciones, no continuar prueba activa.
Procedimiento y archivos esperados: docs/guia-JDOG-proxima-sesion.md; navegador y tres GET HTTP con cabeceras/cuerpos separados.
Aceptación: respuestas y estados guardados, interpretación del contenido y límites; si no hay versión exacta, registrar desconocida. No considerar 403/404 o un HTML de error como versión.
Parada: identidad/alcance incierto, redirección fuera del objetivo, degradación o efectos no previstos. Cada petición limita espera a 20 segundos; guardar fallos.
Resultado: PENDIENTE. Próximo EV libre al crear esta prueba: EV-JDOG-003.
