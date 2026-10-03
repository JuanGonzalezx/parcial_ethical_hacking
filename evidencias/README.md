# Gestión de evidencias

Rutas sugeridas: `originales/ALIAS/EV-ALIAS-NNN-descripcion.ext`. IDs estables por autor: JDOG, JACD, DQH, EJVA; no reutilizar un ID. Registrar archivos separados con IDs distintos y relacionarlos en la sesión. Preservar TXT/XML de herramientas y capturas originales cuando existan.

En `indice.csv`, separar varios IDs de hallazgo con `;`. Dejar `hallazgo_ids` vacío para evidencia de alcance o reconocimiento sin hallazgo. `figura` y `pagina_pdf` se completan al maquetar. `interpretacion` es obligatoria: una captura aislada no es análisis. `instancia` impide mezclar resultados de laboratorios distintos.

Calcular SHA-256 con `shasum -a 256 ruta/al/archivo` (macOS) o `sha256sum ruta/al/archivo` (Linux) y copiar únicamente el hash al índice. Si cambia el original, conservar la versión anterior y crear un archivo/registro nuevo; no actualizar el hash para ocultar un cambio.

Las copias recortadas o con datos ocultos van en `redactadas/`, se registran con otro EV y explican su relación con el original. No fabricar ni alterar el resultado visible. Cada figura del informe debe tener número, título y explicación: qué se ejecutó, qué demuestra, relevancia y conclusión.

Nunca usar las capturas de `Docs_Base/` como evidencia propia. El repositorio interno no sustituye la integración dentro del PDF.
