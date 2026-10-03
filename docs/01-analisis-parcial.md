# Análisis del parcial y criterio de éxito

Fuente normativa: `Docs_Base/DocsParcial/Parcial_Global_Ethical_Hacking_PTES_CTF_Azul_Neon.pdf`, 10 páginas. Los otros dos PDF son modelos de comunicación; no añaden requisitos ni autorizan sus técnicas contra DC-1.

## Qué debemos demostrar

Responder con evidencia si un atacante en la misma red puede comprometer el servidor y alcanzar privilegios administrativos. Obtener root por sí solo no asegura una buena nota. Se debe reconstruir descubrimiento, razonamiento, validación, acceso, impacto, escalamiento y remediación. Si no se alcanza una fase, explicar intentos, límites y máximo acceso demostrado.

## Matriz de evaluación (p. 9)

| ID | Componente | Puntos | Evidencia y criterio de cierre | Destino PDF |
|---|---|---:|---|---|
| R01 | Pre-Engagement, alcance y RoE | 5 | Identificación de VM/red, tipo de prueba justificado, límites y parada | 5–10 |
| R02 | Intelligence Gathering y enumeración | 10 | Descubrimiento, puertos, servicios y versiones; interpretación y siguiente decisión | 11–12 |
| R03 | Threat Modeling | 5 | Activos → superficie → hipótesis → prioridad justificada | 13 |
| R04 | Vulnerability Analysis | 15 | Posibles vs confirmadas, validación, CVE/CWE/CVSS cuando apliquen, falsos positivos | 14–15, 20 |
| R05 | Explotación y demostración técnica | 20 | Por qué funciona, técnica, parámetros, PoC propia, identidad y privilegio inicial | 16, 20 |
| R06 | Post-Exploitation y escalamiento | 10 | Enumeración local, mecanismo de escalamiento, privilegio final probado | 17–19, 21 |
| R07 | Calidad profesional del informe | 25 | 25 apartados y evidencia legible integrada; revisión editorial | Todo |
| R08 | Defensa técnica | 10 | Cualquier integrante explica el proceso completo | Guía interna de defensa |
| | **Total** | **100** | Nota máxima 5.0; no se presume fórmula adicional | |

### Desglose de R07 (no se suma nuevamente a los 100)

| Criterio | Puntos | Revisión |
|---|---:|---|
| Resumen ejecutivo | 3 | Riesgo y resultado comprensibles sin jerga innecesaria |
| Alcance y metodología | 2 | Límites y PTES coherentes con pruebas reales |
| Organización y presentación | 3 | Índice, numeración, legibilidad y control de versión |
| Documentación de vulnerabilidades | 5 | Fichas completas, reproducibles y trazables |
| Calidad y trazabilidad de evidencias | 5 | Figura, título, ejecución, demostración, relevancia y conclusión |
| Evaluación del impacto | 2 | Impacto técnico probado y organizacional razonado |
| Recomendaciones técnicas | 3 | Acción concreta y forma de verificar corrección |
| Cadena de ataque y conclusiones | 1 | Diagrama propio con los pasos realmente logrados |
| Referencias técnicas | 1 | Fuentes confiables aplicables a cada afirmación |
| **Total** | **25** | |

## Requisitos que condicionan el trabajo

- Pp. 3–4: aislamiento Host-Only/Internal, IP descubierta por el grupo; alcance y tipo de prueba justificado. No Bridge institucional.
- P. 5: cada hallazgo requiere ID, activo/IP/puerto/servicio, descripción, evidencia, severidad, CVSS/vector cuando corresponda, CVE/CWE aplicables, reproducción, impactos, remediación y referencias.
- P. 5: mostrar identidad del objetivo en la shell: `whoami`, `id`, `hostname`, `ip addr`, `pwd`, `uname -a` cuando estén disponibles. Registrar alternativas y límites cuando no lo estén.
- P. 6: proof of compromise final con usuario, privilegios y hostname; cadena de ataque propia basada en hechos.
- Pp. 6–8: único PDF; capturas externas o enlaces a carpetas no cuentan como evidencia entregada. Cada figura debe estar interpretada.
- P. 7: conservar los 25 apartados que ya están en `informe/INFORME.md`.
- P. 8 §16: prohibidos walkthroughs, writeups, videos o tutoriales que resuelvan específicamente DC-1. Todos deben poder defender todo el trabajo.

## Lectura de los informes profesionales

**Cure53, Project 11 (14 páginas):** pp. 1–5 presentan índice, contexto, modalidad y alcance delimitado por paquetes de trabajo. Pp. 6–11 usan identificadores estables, severidad, detalle, pruebas, recomendaciones y notas de verificación de correcciones; distinguen vulnerabilidades de observaciones. Pp. 12–14 cierran con una evaluación contextual. Adoptar fichas concisas y trazabilidad, sin copiar sus hallazgos, alcance white-box ni conclusiones favorables.

**Bishop Fox, Winston Privacy (26 páginas):** pp. 3–4 separan objetivos, alcance, fechas, conteos de severidad y recomendaciones ejecutivas. Pp. 5–25 desarrollan definición, detalle, figuras, ubicaciones afectadas y recomendaciones. P. 26 explica la escala de severidad. Adoptar dos niveles de lectura, figuras interpretadas y criterios explícitos de riesgo. Sus severidades no equivalen automáticamente a un puntaje CVSS de nuestro laboratorio.

La plantilla MnzHack combina estas prácticas manteniendo el orden obligatorio del docente. No copiar textos, capturas ni resultados de esos informes.

## Material de clase

Hay tres `.ctb`, exportaciones XML con imágenes y tres apuntes `.txt` de enumeración y estabilización de shell. Son referencia pedagógica, no evidencias del parcial. Los ejemplos usan otras IP y servicios: no trasladarlos a DC-1. Una tabla de Nmap explica `--min-rate` aunque el comando visible no lo incluye; documentar solo parámetros realmente ejecutados. Los apuntes de shell incluyen modificación de `authorized_keys`: no convertirla en un paso automático, dado el límite sobre persistencia. Revisar comillas tipográficas antes de reutilizar cualquier ejemplo.

## Decisiones abiertas

El equipo indica MnzHack; la asignación dice Mzlhack. Conservar el nombre del equipo y confirmar la discrepancia antes de portada final. Fechas 3–8 de octubre aportadas por Juan; hora/canal no figuran en el material revisado. El tipo de prueba y la identificación del laboratorio requieren datos reales, no inferencias de Internet.
