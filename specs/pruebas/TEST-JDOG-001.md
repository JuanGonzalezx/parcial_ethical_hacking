# TEST-JDOG-001 · Cerrar reconocimiento e inventario propio

Estado: en curso reportado; resultados finales pendientes. Registro retrospectivo inicial a partir de EV-JDOG-001, no se afirma que existió antes del escaneo.
Autor: JDOG. Instancia: LAB-JDOG. Objetivo candidato: 192.168.128.4.

Observación de origen: conectividad ICMP y Nmap 7.95 en Script Scan. Hipótesis operativa: el host identificado por Juan como DC-1 presenta servicios que se pueden enumerar; falta corroborar identidad contra UTM.

Precondiciones de continuación: MAC/VM verificadas, red aislada documentada y objetivo dentro del alcance. Procedimiento: preservar salida de ejecución actual; repetición con -oA solo si se necesita salida estructurada, como nueva sesión. Ver docs/guia-JDOG-proxima-sesion.md.

Parada: dudas de identidad/aislamiento, afectación fuera del alcance o inestabilidad del servicio. No hay razón para afirmar bloqueo por 19 segundos de progreso.

Evidencia esperada: configuración del laboratorio, interfaces/rutas, comando y salida final, tabla de servicios y explicación de próxima prueba. Aceptación: identidad respaldada, resultados completos y reproducibles, sin trasladar observaciones de otras instancias. Si no termina, registrar limitación y diagnóstico en vez de inventar puertos.

Resultado actual: ping 3/3, pérdida 0%, TTL 64; sin tabla de puertos recibida. No se ha ejecutado nada desde el asistente.

## Actualización con EV-JDOG-002

La salida final de Nmap sobre 192.168.128.4 muestra cuatro puertos TCP abiertos: 22/ssh (OpenSSH 6.0p1 Debian 4+deb7u7), 80/http (Apache httpd 2.2.22 Debian), 111/rpcbind 2-4 (RPC #100000) y 47118/status 1 (RPC #100024). Se reportan 65531 puertos TCP cerrados (conn-refused). Finaliza con 1 host activo en 29.18 segundos.

HTTP: título Welcome to Drupal Site | Drupal Site; generador Drupal 7; robots.txt con 36 entradas disallow, de las cuales Nmap muestra 15, incluyendo /CHANGELOG.txt. La tabla rpcinfo muestra registros TCP/UDP/TCP6/UDP6; no acredita un escaneo UDP independiente. Service Info indica Linux a partir del reconocimiento; no se usó -O en el comando visible previo.

La captura anterior EV-JDOG-001 contiene el comando nmap -sV -sC -p- 192.168.128.4 y Nmap 7.95 iniciado a las 17:41 UTC del 2026-10-03 (12:41 Colombia, precisión de minuto). La segunda captura fue enviada como continuación; la fecha exacta de captura no se registra. El puerto 47118 pertenece a esta observación de LAB-JDOG; no sustituirlo por 57249 de Eduardo ni 59236 declarado por Jaime.

Inventario TCP observado; sin vulnerabilidad, CVE ni CVSS confirmados. La familia Drupal 7 está reportada, pero no su versión menor. Falta corroborar identidad DC-1 y aislamiento mediante configuración UTM, y conservar salida original en texto. No hay prueba de shell ni escalamiento.

La salida final resuelve el pendiente del escaneo; no resuelve identidad ni aislamiento. Continúa TEST-JDOG-002 como propuesta.
