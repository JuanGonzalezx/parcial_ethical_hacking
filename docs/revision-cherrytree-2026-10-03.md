# Revisión de avances CherryTree · 2026-10-03

Solicitud: incorporar los dos cuadernos recibidos y adoptar la estructura de Jaime para los cuatro integrantes. No se ejecutaron comandos contra las VMs; esta revisión lee notas y capturas existentes. La fecha de integración no es la fecha de todas las pruebas.

## Origen y preservación

- Jaime: `PARCIAL_PENTEST_JAIME_DC1.ctb`, 20 nodos y 2 imágenes recibidas.
- Eduardo: `WriteUp_Basic_Pentesting1--parcial1EDuardo.ctb`, 1 nodo y 11 imágenes recibidas.
- Respaldo exacto de los seis archivos preexistentes en `cherrytree/respaldos/2026-10-03-antes-integracion/`, con hashes.
- Todos los textos originales no vacíos y filas de imagen originales se compararon sin cambios después de actualizar los .ctb. Solo se reorganizó la jerarquía y se añadieron contenidos de revisión/plantillas; los nodos vacíos recibieron guías.
- 13 PNG extraídos directamente sin recodificación; su procedencia, nodo y offset están en `evidencias/procedencia-2026-10-03.json`. Cada uno tiene ficha de interpretación e índice con SHA-256.
- No se recibieron los TXT de Nmap, el registro `report/sesion_parcial.txt` ni salidas HTTP originales. Las capturas de esos archivos no equivalen a disponer de los originales.

## Instancias diferenciadas

| Dato | LAB-JACD (Jaime) | LAB-EJVA (Eduardo) |
|---|---|---|
| IP objetivo | 192.168.18.130 | 192.168.81.130 |
| MAC observada | 00:0c:29:55:ea:9d | 00:0c:29:79:c1:61 |
| Atacante / interfaz | 192.168.18.129 / ens36 | 192.168.81.129/24 / ens36 |
| Otra interfaz | No documentada en las capturas | ens33 192.168.80.128/24 |
| Aislamiento | Host-Only VMnet11 declarado, sin captura del hipervisor | Pendiente de identificar modo de adaptador |
| Puertos TCP | 22, 80, 111, 59236 declarados en Alcance; falta salida | 22, 80, 111, 57249 observados en Nmap |
| Evidencia | EV-JACD-001/002 | EV-EJVA-001 a 011 |

Los nombres LAB-JACD/LAB-EJVA son identificadores documentales, no hostnames. No se presupone que sean una única VM compartida. Confirmar imagen, snapshot e identidad de ambas copias. No trasladar resultados de Eduardo a la instancia de Jaime.

## Qué respaldan las capturas

Jaime: arp-scan descubre .130 y ping recibe tres respuestas sin pérdida, TTL 64. La clasificación Black Box y la ventana de inicio 11:28 son declaraciones de sus notas, no metadatos de cada captura. La identidad de .1 como host físico y .254 como DHCP no se demuestra únicamente por ARP.

Eduardo: Nmap 7.98 completa un escaneo TCP de 65535 puertos y muestra 4 abiertos. El escaneo de servicios reporta OpenSSH 6.0p1 Debian 4+deb7u7, Apache 2.2.22 Debian, Drupal 7, rpcbind 2-4 y status 1 (RPC #100024) en 57249/tcp. WhatWeb reporta además PHP 5.4.45-0+deb7u14. Son resultados de identificación, no pruebas de explotabilidad ni verificación del estado de parches.

Gobuster v3.6 y las consultas HTTP documentan rutas y contenido. Hay respuestas 200, 301 y 403, lectura de README/robots.txt/web.config y respuesta de xmlrpc.php a GET. Las imágenes no prueban acceso administrativo, ejecución de código ni una vulnerabilidad específica. No hay shell, escalamiento, root, flag ni CVE validado en estos dos archivos.

## Correcciones para la próxima sesión

1. **TTL:** reemplazar en la conclusión revisada “se confirma Linux” por “compatible con Linux; requiere corroboración”. Conservar el apunte original para trazabilidad.
2. **CMS:** el material observado identifica Drupal 7. La línea sobre WordPress/WPScan es una sugerencia no sustentada y no tiene resultado de WPScan; no presentarla como prueba concluida.
3. **HTTP:** 403 no prueba archivo accesible; robots.txt no es control de acceso; un web.config servido no demuestra IIS ni secretos expuestos; GET a xmlrpc.php no demuestra un exploit.
4. **Errores útiles:** documentar URL introducida como comando de shell y `head -n 30~` fallido, seguido del intento corregido. No borrar esas capturas.
5. **Nmap:** Eduardo ejecutó `-sV -sC`, sin `-O`; no afirmar detección activa de OS por ese comando. La tabla rpcinfo no sustituye un escaneo UDP.
6. **Fechas:** salvo el registro con fecha precisa de EV-EJVA-004, dejar `no-registrada` cuando no hay hora exacta sustentada. EV-EJVA-003 y 005 muestran hora con precisión de minuto, anotada en sus fichas. No inventar segundos ni usar fecha de guardado del .ctb.
7. **Capturas:** varias tienen fondo de terminal transparente que dificulta lectura. Preservarlas y, al repetir pruebas, capturar con fondo opaco; no retocar resultados ni borrar errores de las originales.
8. **Fuentes y modalidad:** aclarar el conocimiento previo real del equipo antes de cerrar la clasificación Black Box. No usar soluciones específicas de DC-1.

## Próximos pasos por autor

- Jaime: adjuntar los escaneos que respaldan 22/80/111/59236 y completar versiones, interpretación y evidencia de red.
- Eduardo: incorporar TXT originales, evidenciar aislamiento, documentar herramienta/versión faltante y convertir observaciones en hipótesis específicas con criterios de validación.
- Juan y Daniel: usar la misma estructura; revisar evidencias ajenas como revisión cruzada sin atribuirse ejecuciones.
- Todos: mantener actualizadas specs, EV/PT e informe. Validación documental no equivale a reproducción técnica.
