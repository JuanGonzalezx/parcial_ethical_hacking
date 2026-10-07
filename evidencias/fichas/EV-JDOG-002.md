# EV-JDOG-002 · Resultado final de Nmap

Autor: JDOG, Juan David Ocampo Gonzalez, 38402. Instancia: LAB-JDOG.
Fecha exacta: no-registrada. Inicio con precisión de minuto correlacionado con EV-JDOG-001; no inventar hora de finalización.
Procedencia: imagen adjunta por Juan; copia byte a byte. SHA-256: `c84dbe567436012c1fcdc93e3c129b3e60f1ef1f30e5946d1ae42457f83c2f28`.

## Resultado observado

La salida final de Nmap sobre 192.168.128.4 muestra cuatro puertos TCP abiertos: 22/ssh (OpenSSH 6.0p1 Debian 4+deb7u7), 80/http (Apache httpd 2.2.22 Debian), 111/rpcbind 2-4 (RPC #100000) y 47118/status 1 (RPC #100024). Se reportan 65531 puertos TCP cerrados (conn-refused). Finaliza con 1 host activo en 29.18 segundos.

HTTP: título Welcome to Drupal Site | Drupal Site; generador Drupal 7; robots.txt con 36 entradas disallow, de las cuales Nmap muestra 15, incluyendo /CHANGELOG.txt. La tabla rpcinfo muestra registros TCP/UDP/TCP6/UDP6; no acredita un escaneo UDP independiente. Service Info indica Linux a partir del reconocimiento; no se usó -O en el comando visible previo.

La captura anterior EV-JDOG-001 contiene el comando nmap -sV -sC -p- 192.168.128.4 y Nmap 7.95 iniciado a las 17:41 UTC del 2026-10-03 (12:41 Colombia, precisión de minuto). La segunda captura fue enviada como continuación; la fecha exacta de captura no se registra. El puerto 47118 pertenece a esta observación de LAB-JDOG; no sustituirlo por 57249 de Eduardo ni 59236 declarado por Jaime.

## Interpretación

Inventario TCP observado; sin vulnerabilidad, CVE ni CVSS confirmados. La familia Drupal 7 está reportada, pero no su versión menor. Falta corroborar identidad DC-1 y aislamiento mediante configuración UTM, y conservar salida original en texto. No hay prueba de shell ni escalamiento.

Decisión propuesta: priorizar enumeración HTTP y corroborar tecnología/versión; mantener SSH/RPC en inventario. Revisar configuración UTM antes de continuar pruebas si no se confirmó el aislamiento.

![EV-JDOG-002](../originales/JDOG/EV-JDOG-002.png)

Figura/página final y revisión cruzada: pendientes. Conservar el original; obtener captura compacta de la tabla para legibilidad del PDF.
