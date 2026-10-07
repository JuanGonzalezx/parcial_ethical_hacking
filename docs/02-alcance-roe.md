# Alcance y Rules of Engagement

Estado: borrador operativo; faltan datos del laboratorio. Base autorizada: enunciado del docente, pp. 2–3. Fechas indicadas por el equipo: 2026-10-03 a 2026-10-08, America/Bogota.

**Objetivo:** determinar hasta qué privilegios puede llegar un atacante en la misma red sobre la VM DC-1 asignada, y justificar impacto y remediación.

| Campo | Valor |
|---|---|
| Equipo | MnzHack; discrepancia Mzlhack pendiente de aclarar |
| Objetivo | DC-1, exclusivamente |
| Instancia y propietario | PENDIENTE; asignar LAB-JDOG/JACD/DQH/EJVA si hay copias separadas |
| Hipervisor / versión de imagen / procedencia / hash si disponible | PENDIENTE |
| Máquina atacante / versión / IP / interfaz | PENDIENTE |
| Red / CIDR / adaptador | PENDIENTE; solo Host-Only o Internal Network |
| IP / MAC / hostname objetivo | PENDIENTE de descubrimiento verificable |
| Snapshot de referencia | PENDIENTE |
| Tipo de prueba | PENDIENTE de justificar según información entregada y conocida |
| Horario, coordinación y responsable de detener pruebas | PENDIENTE de acordar |

Conocer el nombre de la VM no establece por sí solo Black/Gray/White Box. Registrar conocimiento previo real y cualquier limitación; no declarar desconocimiento total si se conocían detalles de antemano.

## Permitido dentro del laboratorio

Descubrimiento, TCP/UDP pertinente, fingerprinting, enumeración de servicios/usuarios/recursos, análisis web, investigación y validación técnica, explotación controlada, shell, cracking dentro del alcance y escalamiento. Seleccionar técnicas según hipótesis, no por cantidad de herramientas.

## Exclusiones y parada

Fuera de alcance: infraestructura institucional, Internet público, otras VMs de grupos y computadores personales. Prohibidos DoS, borrado deliberado, ransomware/wipers, persistencia permanente y pivoteo a otros sistemas. La VM no se expone a Internet ni Bridge institucional.

Detener si cambia la IP o identidad sin verificar, hay dudas sobre el adaptador, aparecen activos ajenos, inestabilidad significativa o efectos no previstos. Registrar hora, comando, efecto y responsable; corregir aislamiento/identidad antes de continuar. Preparar snapshot y documentar restauraciones, pues pueden invalidar evidencias posteriores o cambiar el estado del objetivo.

## Evidencia y cierre

Registrar fecha ISO 8601 con `-05:00`, autor e instancia de cada ejecución. Originales conservados; copias redactadas para compartir cuando proceda. Revisar secretos antes de Git. Evidencias sensibles locales en `private/`, con respaldo privado gestionado por el equipo; no confundir .gitignore con cifrado. No incorporar credenciales ajenas al laboratorio.

Al cerrar: detener listeners/procesos del ejercicio, registrar cambios y retirar artefactos temporales propios cuando corresponda; documentar restauración de snapshot. No afirmar limpieza ni remediación sin comprobarla.

## Inventario recibido el 2026-10-03

| Instancia documental | Atacante | Objetivo | Red e identidad | Estado |
|---|---|---|---|---|
| LAB-JACD | 192.168.18.129, ens36 | 192.168.18.130; MAC 00:0c:29:55:ea:9d | Host-Only VMnet11 declarado por Jaime | ARP/ping observados; falta captura del hipervisor, snapshot y salida Nmap |
| LAB-EJVA | 192.168.81.129/24, ens36; ens33 192.168.80.128/24 | 192.168.81.130; MAC 00:0c:29:79:c1:61 | Aislamiento por comprobar | ARP, Nmap y web observados; falta configuración de red y snapshot |

Black Box es la modalidad declarada por Jaime, pendiente revisión con el conocimiento previo real. La ventana 2026-10-03 11:28 consta en sus RoE; no sustituye fecha de cada EV. No se ejecutaron nuevas pruebas durante esta integración documental.

## Avance LAB-JDOG

Estado: conectividad observada y escaneo en curso al capturar. Objetivo candidato 192.168.128.4; falta vincular su MAC con el adaptador de DC-1 en UTM, evidenciar aislamiento y obtener la salida final. UTM/Parrot son información aportada por Juan, no configuración comprobada por esta imagen. No trasladar puertos ni versiones de LAB-JACD o LAB-EJVA a LAB-JDOG. Sin vulnerabilidades confirmadas.

Juan indica que configuró la VM en UTM y prueba desde Parrot. La captura muestra un descubrimiento previo de 256 direcciones con 3 hosts activos, pero el comando y la IP de uno de ellos no se ven completos. Se ve 192.168.128.4 con MAC CE:E9:EA:43:88:05 y también 192.168.128.2, cuyo rol no está identificado. No se deduce la IP atacante de esta imagen.

El comando ping -c 3 192.168.128.4 recibió 3 respuestas, 0% de pérdida, TTL 64 y RTT promedio 2.480 ms. Esto acredita conectividad; no confirma sistema operativo ni identidad DC-1.

Se ve nmap -sV -sC -p- 192.168.128.4. Nmap 7.95 inicia el 2026-10-03 a las 17:41 UTC (12:41 en Colombia), con precisión de minuto. La captura termina durante Script Scan, aproximadamente 98.05%, a los 19 segundos. No muestra el resultado final ni la tabla de puertos. El progreso varía; no hay evidencia de bloqueo en este fragmento. No se ve opción de salida a archivo.

## Actualización con EV-JDOG-002

La salida final de Nmap sobre 192.168.128.4 muestra cuatro puertos TCP abiertos: 22/ssh (OpenSSH 6.0p1 Debian 4+deb7u7), 80/http (Apache httpd 2.2.22 Debian), 111/rpcbind 2-4 (RPC #100000) y 47118/status 1 (RPC #100024). Se reportan 65531 puertos TCP cerrados (conn-refused). Finaliza con 1 host activo en 29.18 segundos.

HTTP: título Welcome to Drupal Site | Drupal Site; generador Drupal 7; robots.txt con 36 entradas disallow, de las cuales Nmap muestra 15, incluyendo /CHANGELOG.txt. La tabla rpcinfo muestra registros TCP/UDP/TCP6/UDP6; no acredita un escaneo UDP independiente. Service Info indica Linux a partir del reconocimiento; no se usó -O en el comando visible previo.

La captura anterior EV-JDOG-001 contiene el comando nmap -sV -sC -p- 192.168.128.4 y Nmap 7.95 iniciado a las 17:41 UTC del 2026-10-03 (12:41 Colombia, precisión de minuto). La segunda captura fue enviada como continuación; la fecha exacta de captura no se registra. El puerto 47118 pertenece a esta observación de LAB-JDOG; no sustituirlo por 57249 de Eduardo ni 59236 declarado por Jaime.

Inventario TCP observado; sin vulnerabilidad, CVE ni CVSS confirmados. La familia Drupal 7 está reportada, pero no su versión menor. Falta corroborar identidad DC-1 y aislamiento mediante configuración UTM, y conservar salida original en texto. No hay prueba de shell ni escalamiento.

La salida final resuelve el pendiente del escaneo; no resuelve identidad ni aislamiento. Continúa TEST-JDOG-002 como propuesta.
