# Juan · Continuación tras Nmap final

EV-JDOG-002 completa el escaneo que estaba en curso en EV-JDOG-001. No es necesario repetir todo el escaneo para avanzar: conservar primero la salida de terminal. Repetir con -oA solo si se requiere salida estructurada, registrando una nueva ejecución.

## Estado e interpretación

| Puerto TCP | Resultado reportado | Siguiente pregunta |
|---|---|---|
| 22 | OpenSSH 6.0p1 Debian 4+deb7u7 | ¿Qué configuración/autenticación se expone? Pendiente |
| 80 | Apache 2.2.22 Debian; Drupal 7 | ¿Qué versión y contenido responde realmente? Prioridad inicial |
| 111 | rpcbind 2–4 | ¿Qué programas anuncia? Tabla ya disponible |
| 47118 | status 1, RPC #100024 | Caracterizar exposición; no presuponer explotación |

Estos son servicios observados, no cuatro vulnerabilidades. La antigüedad de un banner no prueba explotabilidad ni ausencia de parches.

## Primero: evidencia del laboratorio y del escaneo

Documentar UTM, sus adaptadores, IP/interfaz de Parrot y asociación de MAC CE:E9:EA:43:88:05 con DC-1. No asumir que .2 es atacante ni que un rango privado demuestra aislamiento. Si identidad o aislamiento no están claros, resolverlos antes de continuar pruebas activas.

Guardar el texto completo de Nmap desde la terminal y una captura compacta con IP, tabla y Nmap done. Si se copia manualmente a TXT, indicarlo. No afirmar que se generó con -oA: ese parámetro no figura en el comando inicial.

## Después: enumeración web dirigida

Una vez confirmado el laboratorio, abrir http://192.168.128.4 en el navegador de Parrot; capturar URL, título y contenido visible. Para conservar respuestas en archivos, ejecutar en Parrot (propuesta, no ejecutada por el asistente):

```bash
mkdir -p ~/MnzHack/LAB-JDOG
SESION_WEB=$(mktemp -d ~/MnzHack/LAB-JDOG/web-XXXXXX)
cd "$SESION_WEB"
date -Is | tee fecha.txt
ip -br addr | tee interfaces.txt
ip route | tee rutas.txt
curl --version > curl-version.txt
curl --max-time 20 -sS -D inicio-headers.txt -o inicio.html http://192.168.128.4/
curl --max-time 20 -sS -D robots-headers.txt -o robots.txt http://192.168.128.4/robots.txt
curl --max-time 20 -sS -D changelog-headers.txt -o changelog.txt http://192.168.128.4/CHANGELOG.txt
head -n 30 changelog.txt
```

La petición a CHANGELOG.txt se justifica porque aparece en robots.txt según el resultado de Nmap recibido; no procede de un walkthrough. Leer el estado HTTP antes de interpretar el archivo: un 403/404 o una página HTML de error no es una versión válida. Si devuelve contenido de versión, registrarlo como evidencia reportada y corroborarlo; no asignar automáticamente un CVE. Conservar errores/timeouts y revisar la URL de cualquier redirección antes de seguirla.

No es necesario lanzar todas las herramientas a la vez. Tras estas respuestas, escoger la siguiente prueba con una hipótesis concreta. Evitar repetir el trabajo de otros sin objetivo: tu aporte inmediato es una línea propia reproducible y revisión cruzada de las interpretaciones del equipo.

## Registro en CherryTree

- 01 Pre-Engagement: configuración UTM, identidad y aislamiento pendientes.
- 02 Intelligence Gathering: EV-JDOG-001 y 002 ya integradas, con comando, resultados y límites.
- 03 Enumeración → Web: una nota por respuesta relevante; comando exacto, fecha/zona, URL, código HTTP, evidencia y significado.
- 04 Threat Modeling: priorizar HTTP por la superficie observada; escribir qué hipótesis se quiere comprobar.
- 05 Vulnerability Analysis: crear PT solo con indicio específico y validación documentada; sin CVE/CVSS inventados.

Siguiente ID disponible: EV-JDOG-003. Por cada prueba: objetivo → comando → resultado → interpretación → siguiente decisión. Preservar cada archivo original con hash, y relacionar los archivos de una misma ejecución en la sesión.

Fuentes técnicas generales consultadas 2026-10-03: https://nmap.org/book/man-output.html (-oA) y https://nmap.org/book/man-nse.html (-sC). El trabajo presente interpreta capturas propias; no usa soluciones de DC-1.
