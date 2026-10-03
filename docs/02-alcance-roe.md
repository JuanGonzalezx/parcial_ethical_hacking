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
