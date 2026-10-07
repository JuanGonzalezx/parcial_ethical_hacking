# Informe de pentest · MnzHack · DC-1

BORRADOR DE TRABAJO. Acceso inicial y privilegio efectivo root respaldados por capturas; revisión cruzada y cierre editorial pendientes. Esta fuente no es el PDF de entrega.

## 01. Portada

**MnzHack · DC-1 · Seguridad Informática**

Juan David Ocampo Gonzalez — 38402

Jaime Andres Cardona Diaz — 40549

Daniel Quintero Hurtado — 31429

Eduardo Jose Villamil Arce — 37831

Periodo: 3–8 octubre 2026. PENDIENTE: institución/docente, nombre de equipo aclarado y fecha final.

## 02. Control documental

Versión de trabajo 0.2 · revisión documental 2026-10-07. Evidencias originales conservadas; referencias corregidas. Autores de pruebas: JACD, DQH, EJVA y JDOG según cada figura. PENDIENTE: revisión cruzada, versión final, nombre de equipo aclarado y fecha de entrega.

## 03. Tabla de contenido

PENDIENTE: generar al maquetar; verificar títulos y páginas contra el PDF final.

## 04. Resumen ejecutivo

Las evidencias revisadas muestran que un atacante en la red del laboratorio puede obtener acceso al sistema y elevar su privilegio efectivo a root. Jaime documentó acceso como usuario web mediante Drupalgeddon y escalamiento por SUID find; Daniel documentó acceso SSH con una credencial débil y la misma causa de escalamiento en otra instancia. No se mezclan las sesiones ni se cuenta SUID dos veces como causa independiente.

Las prioridades de remediación son actualizar la aplicación a una plataforma soportada, corregir permisos SUID y fortalecer credenciales y privilegios administrativos. La activación de PHP Filter durante la prueba se trata como escenario condicionado a una modificación del evaluador.

PENDIENTE: revisión humana de las fichas, cierre de severidades y evidencia de restauración del laboratorio. Los avances posteriores de Eduardo continúan reportados sin capturas nuevas.

## 05. Objetivos

Determinar si un atacante con acceso a la misma red puede comprometer DC-1 y alcanzar privilegios administrativos, documentando descubrimiento, validación, impacto y remediación.

## 06. Alcance

PENDIENTE: datos reales de docs/02-alcance-roe.md, modalidad y justificación.

## 07. Exclusiones

Excluidos otros grupos, equipos personales, redes institucionales e Internet público.

## 08. Rules of Engagement

Pruebas controladas solo en DC-1 aislada; sin DoS, borrado, persistencia permanente ni pivoteo. PENDIENTE: reglas operativas, parada y manejo de evidencia acordados.

## 09. Metodología PTES

PTES: Pre-Engagement, Intelligence Gathering, Threat Modeling, Vulnerability Analysis, Exploitation, Post-Exploitation y Reporting. PENDIENTE: explicar cómo se aplicó cada fase y sus límites.

## 10. Arquitectura del laboratorio

Se registraron inicialmente dos instancias documentales: LAB-JACD (atacante 192.168.18.129, ens36; objetivo 192.168.18.130) y LAB-EJVA (atacante 192.168.81.129/24, ens36; objetivo 192.168.81.130). Eduardo muestra además ens33 192.168.80.128/24. Jaime declara Host-Only VMnet11; falta captura de configuración para verificar aislamiento.

PENDIENTE: diagrama del laboratorio, snapshots, identidad de las copias y verificación del modo de red. No presentar ambas IP como el mismo host en una única sesión.

LAB-JDOG añade una tercera instancia: UTM/Parrot reportados, objetivo candidato 192.168.128.4. Identidad y aislamiento pendientes de corroborar.

## 11. Reconocimiento e Intelligence Gathering

Jaime documentó descubrimiento ARP y ping, con tres respuestas y 0% de pérdida hacia 192.168.18.130 (EV-JACD-001/002). TTL 64 no confirma por sí solo Linux. Eduardo documentó interfaces y descubrimiento de 192.168.81.130, MAC 00:0c:29:79:c1:61 (EV-EJVA-002).

Nmap 7.98 mostró 22, 80, 111 y 57249/tcp abiertos en LAB-EJVA; 65531 puertos TCP cerrados (EV-EJVA-003/004). El escaneo de servicios identifica SSH, HTTP, rpcbind y status RPC (EV-EJVA-005). No se acredita escaneo UDP independiente. Jaime acredita 22/80/111/59236 con EV-JACD-015/016/017; la advertencia de fingerprinting limita la inferencia de sistema operativo.

Las capturas se incluyen en el anexo de esta fuente; numeración final y legibilidad del PDF pendientes.

Juan documenta ping 3/3 sin pérdida a 192.168.128.4 y Nmap 7.95 en curso (EV-JDOG-001), seguido de salida final EV-JDOG-002 con 22/80/111/47118 TCP abiertos. No se traslada el inventario de otras instancias a LAB-JDOG.

## 12. Enumeración

En LAB-EJVA, Nmap reporta OpenSSH 6.0p1 Debian 4+deb7u7, Apache 2.2.22 Debian, Drupal 7, rpcbind 2–4 y status 1 en 57249/tcp. WhatWeb coincide en Apache/Drupal y reporta PHP 5.4.45-0+deb7u14. Estos banners requieren validación antes de asociar vulnerabilidades.

Gobuster v3.6 encontró respuestas 200, 301 y 403; las consultas HTTP muestran robots.txt, README, web.config y una respuesta de xmlrpc.php que acepta POST. Las rutas no demuestran por sí mismas exposición sensible ni ejecución remota. El fragmento README no acredita versión menor de Drupal. La línea de WordPress/WPScan no tiene resultado y no coincide con el CMS observado.

PENDIENTE: recuperar salidas originales, caracterizar cada servicio y formular hipótesis verificables. Conservar errores visibles: URL como comando de shell y head con argumento 30~.

## 13. Threat Modeling

Modelo preliminar basado en LAB-EJVA; no equivale a hallazgos confirmados.

| Superficie | Evidencia | Hipótesis a investigar | Prioridad propuesta |
|---|---|---|---|
| HTTP / aplicación identificada como Drupal | EV-EJVA-005 a 011 | Comportamientos o versiones que requieran validación técnica | Alta por amplitud de superficie observada |
| SSH | EV-EJVA-005 | Configuración y autenticación que ameriten pruebas dentro del alcance | Media |
| RPC | EV-EJVA-005 | Programas expuestos y necesidad de exposición | Media |

PENDIENTE: activos/impacto del escenario, precondiciones, TEST y criterios de aceptación. No asignar CVE o exploit antes de investigación y validación propias.

## 14. Análisis de vulnerabilidades

Hay resultados de explotación respaldados por capturas y ocho fichas registradas. PT-001/002/003/004/007/008 fueron reportadas confirmadas por sus autores; su estado editorial es en-validacion hasta revisión cruzada. Las fichas distinguen qué se observa y qué interpretación falta cerrar. PT-005 sigue como hipótesis y PT-006 como exposición observada sin impacto demostrado.

No se confirma CVE-2018-7600 a partir del módulo utilizado para CVE-2014-3704. No se atribuye debilidad del algoritmo de hash solo por recuperar una contraseña. Los vectores CVSS propuestos requieren justificación por métrica y alcance; las cifras no representan una nota de madurez del sistema.

## 15. Resumen de hallazgos

| ID | Objeto | Estado editorial | Resultado / límite |
|---|---|---|---|
| PT-001 | Drupalgeddon SQLi | en-validacion | Shell www-data observada; revisión cruzada pendiente |
| PT-002 | SUID find, Jaime | en-validacion | EUID root observado |
| PT-003 | Contraseña Drupal | en-validacion | Recuperación y login observados; origen del hash pendiente |
| PT-004 | PHP Filter activado por evaluador | en-validacion | PHP ejecutado; clasificar como escenario condicionado |
| PT-005 | Drupalgeddon2 | posible | Sin PoC propia registrada |
| PT-006 | web.config | en-validacion | Archivo accesible; impacto sin justificar |
| PT-007 | Credencial SSH flag4 | en-validacion | Hydra y login observados |
| PT-008 | SUID find, Daniel | en-validacion | EUID root observado; misma causa que PT-002 |

Puntajes definitivos y aprobación de otro integrante: PENDIENTE. No son ocho vulnerabilidades únicas confirmadas.

## 16. Explotación

LAB-JACD: EV-JACD-014 muestra opciones de drupal_drupageddon y EV-JACD-003 la sesión abierta como www-data; EV-JACD-009 muestra identidad DC-1. La referencia del módulo relaciona la prueba con CVE-2014-3704.

LAB-DQH: EV-DQH-006 muestra autenticación password; EV-DQH-007 solo el inicio de enumeración, sin usuarios confirmados. EV-DQH-008 muestra Hydra con credencial para flag4; EV-DQH-009/010 muestran login y lectura de flag. La duración visible de Hydra es 2 min 35 s.

Las antiguas referencias EV-DQH-001 a 005 correspondían a reconocimiento y se corrigieron manteniendo los originales.

## 17. Post-Exploitation

LAB-JACD: se corroboró identidad de usuario web y hostname (EV-JACD-009). El autor reporta extracción de credenciales DB y hashes en la ficha PT-003; faltan capturas del origen. Hashcat y acceso admin sí aparecen en EV-JACD-005/013.

El relato de intento Dirty COW no se da por demostrado en todas sus fases: EV-JACD-019 muestra únicamente transferencia de dirty.c. Registrar error real y cambios; no deducir vulnerabilidad ni parche por un intento fallido.

PENDIENTE: completar cobertura de usuarios, permisos, tareas y procesos, explicar qué no se evaluó, y documentar retirada de artefactos/restauración.

## 18. Escalamiento de privilegios

LAB-JACD: permisos SUID de find (EV-JACD-007), preparación de /tmp/rootbash (008) y ejecución con uid=33(www-data), euid=0(root) (004). La primera copia falló en su objetivo porque conservaba propietario www-data; la segunda fue creada mediante find con propietario root. Algunas capturas del inventario se tomaron ya con prompt privilegiado; falta ordenar cronología exacta.

LAB-DQH: EV-DQH-011/012 muestran ejecución mediante find y bash -p con uid=1001(flag4), euid=0(root). El UID real no se convirtió en cero.

PT-002/PT-008 describen la misma causa en dos instancias y se consolidarán por causa sin perder autoría. Limpieza de los artefactos: pendiente.

## 19. Cadena de ataque

Dos recorridos separados respaldados por las capturas, sujetos a revisión de continuidad temporal. No se unen hosts solo por compartir IP.

```mermaid
flowchart LR
 subgraph J[LAB-JACD]
  J1[HTTP Drupal · EV-JACD-016] --> J2[SQLi y shell www-data · 003]
  J2 --> J3[find SUID · 007 y 008]
  J3 --> J4[EUID root · 004]
  J4 --> J5[Bandera final · 010]
 end
 subgraph D[LAB-DQH]
  D1[SSH password · EV-DQH-006] --> D2[Credencial obtenida · 008]
  D2 --> D3[Login flag4 · 009]
  D3 --> D4[find y EUID root · 011]
  D4 --> D5[Bandera final · 012]
 end
```

PENDIENTE: renderizar este diagrama como figura propia dentro del PDF y corroborar cronología con autores.

## 20. Hallazgos técnicos detallados

Las fichas siguientes conservan resultados y límites; revisión cruzada pendiente.

### PT-001 · SQL Injection Drupal Core asociada a CVE-2014-3704

- Estado: en-validacion
- Autor: JACD. Estado editorial: en-validacion. El autor lo reportó confirmado; hay capturas del resultado, pero falta revisión cruzada de otro integrante conforme a AGENTS.md. Esta etiqueta no niega el resultado observado. Revisor: pendiente. Fecha de revisión documental: 2026-10-07.
- Activo: LAB-JACD, 192.168.18.130:80, Drupal 7 / Apache 2.2.22. Versión menor no determinada únicamente por WhatWeb.
- Evidencias: EV-JACD-003;EV-JACD-009;EV-JACD-014;EV-JACD-018

#### Descripción y validación

La captura del módulo exploit/multi/http/drupal_drupageddon muestra apertura de sesión y comandos id/whoami con www-data (EV-JACD-003). Opciones en EV-JACD-014 e identidad DC-1 en EV-JACD-009. La configuración del módulo por sí sola no confirma la falla; el resultado de sesión sí respalda ejecución remota.

#### Procedimiento documentado

El procedimiento recibido configura RHOSTS=.18.130, LHOST=.18.129, LPORT=4444, payload php/reverse_php y TARGETURI=/; ejecuta el módulo y comprueba identidad. Conservar versiones de Metasploit y fuente exacta del módulo. La asociación CVE-2014-3704 procede del módulo utilizado y de la ficha del autor; no atribuirla a Drupalgeddon2.

#### Impacto

Ejecución como usuario web observada. La escalada a EUID root pertenece a PT-002, no es privilegio inicial. El impacto potencial afecta contenido y datos accesibles al proceso web.

#### Severidad CVSS y clasificación

CVE-2014-3704; CWE-89. Vector propuesto del autor: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, 9.8. Mantener como propuesta hasta justificar C/I/A respecto al componente afectado, sin trasladar automáticamente privilegio root de otra falla.

#### Remediación y comprobación

Migrar el CMS a una rama soportada y aplicar corrección de SQLi. Drupal 7.32 es el umbral histórico citado, no una recomendación suficiente para producción en 2026. En una copia corregida verificar que la solicitud vulnerable ya no abre sesión y que la aplicación conserva funcionamiento.

#### Referencias y cierre

Conservar referencia de versión/hash del módulo y evidencia de continuidad de la sesión. Referencia técnica aportada: https://www.drupal.org/SA-CORE-2014-005 (no accesible durante esta revisión). Ciclo de soporte consultado: https://www.drupal.org/about/core/policies/core-release-cycles/schedule .
La ficha transcrita del autor se conserva en `docs/revision-2026-10-07/fuente-PT-001.txt`; el CherryTree original permanece intacto. La revisión no ejecutó pruebas ni aplicó remediación.

### PT-002 · Permisos SUID indebidos en /usr/bin/find

- Estado: en-validacion
- Autor: JACD. Estado editorial: en-validacion. El autor lo reportó confirmado; hay capturas del resultado, pero falta revisión cruzada de otro integrante conforme a AGENTS.md. Esta etiqueta no niega el resultado observado. Revisor: pendiente. Fecha de revisión documental: 2026-10-07.
- Activo: LAB-JACD, 192.168.18.130, sistema local; sesión inicial www-data.
- Evidencias: EV-JACD-004;EV-JACD-007;EV-JACD-008;EV-JACD-010

#### Descripción y validación

EV-JACD-007 acredita dueño root y SUID; EV-JACD-008 conserva intento inicial y corrección al preparar shell temporal; EV-JACD-004 acredita uid=33 y euid=0; EV-JACD-010 muestra banderas. Algunas capturas de inventario se tomaron ya desde rootbash: no presentarlas como anteriores al acceso sin reconstruir cronología.

#### Procedimiento documentado

El cuaderno registra copiar bash mediante find, activar SUID y ejecutar /tmp/rootbash -p; luego id. La secuencia exacta está en EV-JACD-008 y la fuente histórica extraída. No se reejecutó en esta revisión.

#### Impacto

Escalamiento de www-data a privilegio efectivo root demostrado. El daño a disponibilidad o persistencia son consecuencias potenciales, no acciones que se hayan probado.

#### Severidad CVSS y clasificación

CVE N/A: configuración local. CWE-732. Propuesta CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H = 7.8 (Alta): acceso local y privilegios bajos previos. Misma causa que PT-008 en otra instancia; consolidar sin doble conteo.

#### Remediación y comprobación

Retirar SUID de find según necesidad legítima, auditar permisos privilegiados y verificar en copia corregida que el usuario bajo ya no obtiene euid=0. Retirar /tmp/rootbash y los artefactos propios o restaurar snapshot; no marcar limpieza realizada sin evidencia.

#### Referencias y cierre

Captura final única con whoami, id y hostname; cronología y limpieza pendientes. Referencia recibida: https://cwe.mitre.org/data/definitions/732.html .
La ficha transcrita del autor se conserva en `docs/revision-2026-10-07/fuente-PT-002.txt`; el CherryTree original permanece intacto. La revisión no ejecutó pruebas ni aplicó remediación.

### PT-003 · Contraseña administrativa Drupal recuperada por diccionario

- Estado: en-validacion
- Autor: JACD. Estado editorial: en-validacion. El autor lo reportó confirmado; hay capturas del resultado, pero falta revisión cruzada de otro integrante conforme a AGENTS.md. Esta etiqueta no niega el resultado observado. Revisor: pendiente. Fecha de revisión documental: 2026-10-07.
- Activo: LAB-JACD, Drupal /user/login y hashes de tabla users según notas.
- Evidencias: EV-JACD-005;EV-JACD-013

#### Descripción y validación

EV-JACD-005 muestra Hashcat 6.2.6 modo 7900 y una contraseña recuperada; EV-JACD-013 muestra Hello admin. La extracción de settings.php y consulta MySQL están descritas en el cuaderno, pero faltan capturas de ese origen. La lista de 20 candidatos incluye la respuesta recuperada: aclarar cómo se construyó, sin asumir una procedencia no demostrada.

#### Procedimiento documentado

El autor reporta acceso previo como www-data, lectura de configuración DB, consulta de hashes, Hashcat con lista personalizada y login administrativo. Conservar pasos como reportados donde falta evidencia. Referencia íntegra en docs/revision-2026-10-07/fuente-PT-003.txt.

#### Impacto

Recuperación de un secreto y acceso administrativo observados. Eso no demuestra por sí solo que el algoritmo de hash sea débil, que todos los usuarios estén afectados ni acceso remoto anónimo a hashes.

#### Severidad CVSS y clasificación

CVE N/A. CWE-521 como clasificación candidata de credencial débil; retirar CWE-916 como afirmación confirmada sin evaluar algoritmo/costo. Puntaje 7.5 y vector remoto anónimo recibidos requieren recalcular precondiciones de extracción; CVSS definitivo pendiente.

#### Remediación y comprobación

Cambiar la credencial comprometida, usar secretos largos no previsibles, MFA donde sea viable, limitar privilegios y proteger acceso a hashes. Verificar en copia corregida rechazo del secreto anterior y controles de acceso; no modificar el algoritmo a ciegas sin compatibilidad de la plataforma.

#### Referencias y cierre

Obtener evidencia de extracción, procedencia de wordlist y revisión humana. Fuente general consultada: https://cwe.mitre.org/data/definitions/521.html .
La ficha transcrita del autor se conserva en `docs/revision-2026-10-07/fuente-PT-003.txt`; el CherryTree original permanece intacto. La revisión no ejecutó pruebas ni aplicó remediación.

### PT-004 · Ejecución PHP tras activación administrativa de PHP Filter

- Estado: en-validacion
- Autor: JACD. Estado editorial: en-validacion. El autor lo reportó confirmado; hay capturas del resultado, pero falta revisión cruzada de otro integrante conforme a AGENTS.md. Esta etiqueta no niega el resultado observado. Revisor: pendiente. Fecha de revisión documental: 2026-10-07.
- Activo: LAB-JACD, 192.168.18.130:80, /admin/modules y /node/3; requiere administrador del CMS.
- Evidencias: EV-JACD-006;EV-JACD-011;EV-JACD-012;EV-JACD-013

#### Descripción y validación

EV-JACD-011 muestra activación/guardado de configuración, EV-JACD-012 creación de página PHP y EV-JACD-006 ejecución de id/hostname/uname como www-data. El propio evaluador habilitó la función; la prueba no acredita que estuviera habilitada al inicio.

#### Procedimiento documentado

Con sesión admin se activa PHP Filter, se crea Basic Page con PHP y se observa el resultado. Es una ampliación del impacto de control administrativo, condicionada a esa modificación. No es un segundo acceso anónimo independiente.

#### Impacto

Un administrador capaz de activar y usar el formato ejecuta PHP como usuario web. Decidir si se presenta como escenario posterior al compromiso o hallazgo de privilegios/configuración; evitar contar como falla preexistente sin justificar el modelo de permisos.

#### Severidad CVSS y clasificación

CVE N/A. CWE-94 propuesto originalmente, pertinencia pendiente porque se utiliza funcionalidad explícita. Vector propuesto del autor CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H y puntaje 9.1 recibidos necesitan recalcular y justificar Scope; no publicar esa pareja como validada.

#### Remediación y comprobación

Restringir activación de módulos y ejecución de PHP desde contenido; retirar contenido de prueba y revertir módulo activado por el evaluador. Comprobar separación de roles y ausencia de páginas PHP residuales en copia corregida.

#### Referencias y cierre

Confirmar estado previo, decisión de clasificación y limpieza. Fuente de origen preservada en docs/revision-2026-10-07/fuente-PT-004.txt; referencia Drupal PHP Filter del autor no accesible durante revisión.
La ficha transcrita del autor se conserva en `docs/revision-2026-10-07/fuente-PT-004.txt`; el CherryTree original permanece intacto. La revisión no ejecutó pruebas ni aplicó remediación.

### PT-005 · Posible ejecución remota de código en Drupal 7 (Drupalgeddon 2)

- Estado: posible
- Autor / revisor / fechas: DQH / pendiente / 2026-10-04
- Activo / instancia / snapshot / IP / puerto / servicio / versión: 192.168.18.130 / 80 / Apache / Drupal 7
- Hipótesis / sesión de origen: Identificación de Drupal 7 mediante escaneo web y whatweb. Posible vulnerabilidad a CVE-2018-7600 (Drupalgeddon 2) según resultados de searchsploit.
- Severidad: pendiente; 9.8 es el valor propuesto en la ficha recibida, no evaluación validada de esta instancia.
- CVSS: N/A (Pendiente de validación)
- CVE / CWE: CVE-2018-7600 / CWE-20

#### Descripción técnica y causa

Drupal 7 anterior a versiones parcheadas es vulnerable a una falla en el motor de renderizado de formularios (Form API), que permite la inyección de código a través de parámetros no sanitizados, resultando en Ejecución Remota de Código (RCE). La enumeración con `whatweb` y Wappalyzer confirmó el uso de Drupal 7, y `searchsploit` indicó múltiples exploits.

#### Descubrimiento y validación

Se identificó el CMS Drupal 7 durante la fase de reconocimiento (Nmap, Whatweb, navegación web). Se requiere ejecutar un exploit o PoC de Drupalgeddon 2 para confirmar si el sistema está parcheado o es vulnerable.

#### Reproducción

Pendiente de validación técnica con un exploit específico.

#### Evidencias

Pendiente de extracción de capturas y asignación de IDs EV-DQH-XXX. Se identificó en la sesión inicial de reconocimiento de DQH.

#### Impacto

De confirmarse, un atacante externo podría tomar control total de la aplicación web y ejecutar comandos en el sistema operativo subyacente con los privilegios del servidor web (`www-data`).

#### Remediación y comprobación

Actualizar Drupal a la versión más reciente que incluye los parches de seguridad para esta vulnerabilidad.

#### Referencias

- NVD - CVE-2018-7600: https://nvd.nist.gov/vuln/detail/CVE-2018-7600

#### Revisión

Pendiente.

#### Revisión documental del 2026-10-07

Drupageddon usado por Jaime corresponde al CVE de 2014; no confirma CVE-2018-7600 en LAB-DQH. Mantener como hipótesis sin obligación de explotar una segunda ruta antes de cerrar la entrega. Advisory consultado: https://www.drupal.org/sa-core-2018-002 . Drupal 7 terminó soporte comunitario: para producción recomendar migración a rama soportada, no solo el parche histórico 7.58.

### PT-006 · Exposición de archivo de configuración (web.config)

- Estado: en-validacion
- Autor / revisor / fechas: DQH / pendiente / 2026-10-04
- Activo / instancia / snapshot / IP / puerto / servicio / versión: 192.168.18.130 / 80 / Apache / IIS Rules
- Hipótesis / sesión de origen: Durante la enumeración de directorios con gobuster se detectó y descargó el archivo `web.config`.
- Severidad: pendiente de demostrar impacto. La descarga de reglas genéricas sin secretos no basta para justificar 3.7.
- CVSS: N/A
- CVE / CWE: N/A / CWE-200

#### Descripción técnica y causa

El servidor web aloja en su raíz el archivo `web.config` (habitualmente usado en IIS, aunque aquí se expone en Apache 2.2.22). Este archivo puede ser leído por cualquier usuario sin autenticación.

#### Descubrimiento y validación

Gobuster identificó `/web.config` con estado 200 OK. La posterior revisión del archivo a través de un navegador demostró que contenía reglas de `system.webServer` sobre reescritura de URLs y ocultación de directorios.

#### Reproducción

Navegar a `http://192.168.18.130/web.config` y observar el contenido XML expuesto.

#### Evidencias

EV-DQH-013: contenido web.config en navegador. Revisar si difiere del archivo público distribuido con el CMS antes de concluir exposición sensible.

#### Impacto

Bajo. Revela reglas de reescritura, condiciones de rutas y medidas de seguridad del servidor, pero no se observaron credenciales, contraseñas ni rutas altamente críticas explotables directamente. Sin embargo, facilita el reconocimiento interno.

#### Remediación y comprobación

Configurar el servidor web Apache o el archivo `.htaccess` para denegar explícitamente el acceso a archivos de configuración como `web.config` y `.htaccess`.

#### Referencias

- Enumeración de archivos sensibles.

#### Revisión

Pendiente.

### PT-007 · Credenciales débiles de SSH para el usuario flag4

- Estado: en-validacion
- Resultado: demostrado en capturas; revisión cruzada pendiente (antes marcado confirmado por el autor).
- Autor / revisor / fechas: DQH / pendiente / 2026-10-04
- Activo / instancia / snapshot / IP / puerto / servicio / versión: LAB-DQH / 192.168.18.130 / puerto 22 / SSH
- Hipótesis / sesión de origen: TEST-DQH-001
- Severidad y razonamiento: Alta. Permite acceso directo e interactivo al servidor a nivel del sistema operativo.
- CVSS: 3.1, 9.1 (Crítica para este vector; propuesta pendiente de justificar impactos), CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N (C:H e I:H significan impacto alto; justificar su alcance en la cuenta no privilegiada).
- CVE / CWE: CWE-521: Weak Password Requirements. CWE-258 no aplica: la contraseña no está vacía.

#### Descripción técnica y causa

El servicio SSH expuesto en el puerto 22 permite la autenticación mediante contraseña (password). Un usuario del sistema, denominado `flag4`, posee una contraseña extremadamente débil (`orange`), la cual se encuentra en diccionarios comunes de contraseñas.

#### Descubrimiento y validación

Se identificó la autenticación por contraseña habilitada con un script de nmap. Posteriormente, se usó un diccionario corto de usuarios candidatos a través del módulo auxiliar `scanner/ssh/ssh_enumusers` en Metasploit. La captura de Metasploit no muestra el resultado final de usuarios válidos. Después se lanzó Hydra contra el usuario candidato flag4 con `rockyou.txt`; la captura muestra inicio 14:05:17 y final 14:07:52 (2 min 35 s) (EV-DQH-008).

#### Reproducción

1. Confirmar que el puerto 22 responde: `nmap -p 22 192.168.18.130`
2. Lanzar Hydra: `hydra -l flag4 -P /usr/share/wordlists/rockyou.txt ssh://192.168.18.130 -t 4`
3. Resultado esperado: Hydra informa `login: flag4   password: orange`.
4. Conectar: `ssh flag4@192.168.18.130` (Aceptar fingerprint, introducir `orange`).

#### Evidencias

- EV-DQH-006: métodos publickey/password.
- EV-DQH-007: intento de enumeración; no demuestra usuario válido.
- EV-DQH-008: Ejecución exitosa de Hydra que revela la contraseña 'orange'.
- EV-DQH-009: acceso SSH como flag4.
- EV-DQH-010: lectura de flag4.txt.

#### Impacto

Impacto técnico: Compromiso parcial del servidor con permisos de un usuario no privilegiado (`flag4`). Permite la ejecución de comandos locales, la lectura de archivos sensibles (ej. `flag4.txt`) y provee un punto de apoyo esencial para lanzar ataques de escalada de privilegios (Local Privilege Escalation).

#### Remediación y comprobación

Se recomienda deshabilitar la autenticación por contraseña en SSH modificando `/etc/ssh/sshd_config` (`PasswordAuthentication no`) y utilizar únicamente claves públicas (Ed25519 o RSA fuerte). Adicionalmente, las contraseñas de todos los usuarios locales deben someterse a una política de complejidad fuerte.
Comprobación: Intentar login SSH solo con contraseña, debe ser rechazado por el servidor.

#### Referencias

- MITRE CWE-521: https://cwe.mitre.org/data/definitions/521.html

#### Revisión

Revisor: pendiente.

#### Revisión documental del 2026-10-07

Corregidas referencias a imágenes: EV-DQH-001 a 005 eran reconocimiento, no estas pruebas. No se reemplazaron sus PNG. Puntaje, métricas y revisión de otro integrante siguen pendientes de cierre.

### PT-008 · Escalada de privilegios local mediante binario SUID (find)

- Estado: en-validacion
- Resultado: demostrado en capturas; revisión cruzada pendiente (antes marcado confirmado por el autor).
- Autor / revisor / fechas: DQH / pendiente / 2026-10-04
- Activo / instancia / snapshot / IP / puerto / servicio / versión: LAB-DQH / 192.168.18.130 / /usr/bin/find
- Hipótesis / sesión de origen: TEST-DQH-002
- Severidad y razonamiento: Alta (propuesta CVSS 7.8). Permite a cualquier usuario local obtener privilegios de superusuario (root).
- CVSS: 3.1, 7.8 (Alta), CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H.
- CVE / CWE: CWE-732: Incorrect Permission Assignment for Critical Resource.

#### Descripción técnica y causa

El binario `/usr/bin/find` en el sistema posee el bit SUID (Set Owner User ID) activado, y su propietario es el usuario `root`. Esto significa que al ejecutar `find`, el proceso adquiere los privilegios de root temporalmente. Dado que `find` cuenta con el argumento `-exec`, el cual permite la ejecución arbitraria de comandos, es posible utilizarlo para spawnear un intérprete de comandos (`/bin/bash`) heredando los privilegios de root.

#### Descubrimiento y validación

Tras acceder al sistema como un usuario de bajos privilegios (`flag4`), se realizó una enumeración estándar de binarios SUID mediante el comando `find / -perm -4000 -type f 2>/dev/null`. El resultado incluyó `/usr/bin/find`, que es bien conocido por permitir la ejecución arbitraria en esta configuración (EV-DQH-011).

#### Reproducción

1. Desde una sesión no privilegiada, verificar los permisos de `find`: `ls -la /usr/bin/find` (debería mostrar `-rws...`).
2. Ejecutar el comando para instanciar bash preservando el ID efectivo (`-p`):
   `/usr/bin/find /etc/passwd -exec /bin/bash -p \;`
3. Resultado esperado: el prompt cambiará a `bash-4.2#` (o similar). Al ejecutar `whoami`, debe devolver `root`.

#### Evidencias

- EV-DQH-011: Comando `find` detectando binarios SUID y ejecución de `/bin/bash -p` mediante `-exec`.
- EV-DQH-012: Comandos `id` demostrando `euid=0(root)` y lectura del archivo `thefinalflag.txt` en `/root`.

#### Impacto

Se demuestra privilegio efectivo root y lectura de la bandera final. La alteración de archivos y afectación de disponibilidad son impactos potenciales; no se probaron persistencia ni pivoteo y están fuera de alcance. UID real=1001(flag4), EUID=0(root). Misma causa que PT-002 en otra instancia; consolidar sin doble conteo.

#### Remediación y comprobación

Retirar el bit SUID del binario `/usr/bin/find`.
Comando sugerido: `chmod -s /usr/bin/find`.
Para comprobar la corrección, ejecutar `find / -perm -4000 -type f 2>/dev/null` y verificar que `/usr/bin/find` ya no aparezca en la lista.

#### Referencias

- GTFOBins - find: https://gtfobins.github.io/gtfobins/find/#suid

#### Revisión

Revisor: pendiente.

#### Revisión documental del 2026-10-07

Corregidas referencias a imágenes: EV-DQH-001 a 005 eran reconocimiento, no estas pruebas. No se reemplazaron sus PNG. Puntaje, métricas y revisión de otro integrante siguen pendientes de cierre.

## 21. Proof of Compromise

Jaime: EV-JACD-004 acredita EUID root; EV-JACD-010 lectura de bandera final; EV-JACD-009 acredita hostname DC-1 en sesión previa. Daniel: EV-DQH-011/012 acreditan whoami root, EUID=0 y bandera final, con DC-1 visible en el prompt previo.

Para una prueba final más sólida, completar una captura de la misma sesión que incluya explícitamente whoami, id y hostname, y su relación con IP/instancia. No sustituirla por la bandera sola ni afirmar que esa nueva captura ya existe.

## 22. Recomendaciones

| Objeto | Acción | Cómo verificar en copia corregida |
|---|---|---|
| Drupal | Migrar a rama soportada y corregir SQLi | La reproducción autorizada deja de abrir sesión y funciona la aplicación |
| SUID find | Retirar SUID innecesario y auditar permisos | Usuario bajo no obtiene EUID root por ese mecanismo |
| Credenciales | Cambiar secretos comprometidos, evitar candidatos previsibles y limitar roles | Secreto anterior rechazado; controles de autenticación verificados |
| PHP Filter | Revertir activación y contenido de prueba; restringir roles | Contenido y formato ejecutable no disponibles a roles no autorizados |
| Cierre | Retirar artefactos propios o restaurar snapshot | Inventario y estado final documentados |

Son recomendaciones y retests propuestos, no correcciones ejecutadas. Prioridad técnica propuesta: acceso anónimo y escalamiento primero; clasificación final pendiente.

## 23. Conclusiones

El objetivo de demostrar acceso y privilegio efectivo root cuenta con evidencia en las instancias de Jaime y Daniel. La solidez de la entrega depende ahora de relacionar cada afirmación con la imagen correcta, separar instancias y distinguir configuraciones iniciales de cambios hechos durante las pruebas.

No se concluye que toda hipótesis esté validada ni que root pruebe todas las vulnerabilidades enumeradas. Quedan pendientes revisión cruzada, severidades, arquitectura y limpieza documentadas, y revisión visual del PDF.

## 24. Referencias

Fuentes técnicas consultadas el 2026-10-07:

- Rapid7, código fuente de drupal_drupageddon: https://raw.githubusercontent.com/rapid7/metasploit-framework/master/modules/exploits/multi/http/drupal_drupageddon.rb — asociación del módulo con CVE-2014-3704; registrar también versión local usada por el equipo.
- Drupal, SA-CORE-2018-002: https://www.drupal.org/sa-core-2018-002 — distinguir la hipótesis CVE-2018-7600.
- FIRST, CVSS 3.1: https://www.first.org/cvss/v3.1/specification-document — reglas de métricas y severidad.
- MITRE, CWE-521: https://cwe.mitre.org/data/definitions/521.html — debilidad de contraseñas.
- MITRE, CWE-258: https://cwe.mitre.org/data/definitions/258.html — descartar mapeo de contraseña vacía para una contraseña no vacía.
- Drupal, ciclo de soporte: https://www.drupal.org/about/core/policies/core-release-cycles/schedule — migración desde Drupal 7 sin soporte comunitario.

PENDIENTE: completar versiones y fuentes exactas de herramientas/exploits ejecutados, y revisar referencias adicionales de cada ficha.

## 25. Anexos técnicos

Evidencias recibidas: copias PNG extraídas sin modificar de los cuadernos. Los identificadores EV se conservan; PENDIENTE numeración de figuras y páginas finales. Fechas exactas no sustentadas se mantienen como no registradas. No se recibieron salidas TXT originales.

### EV-JACD-001 · Descubrimiento ARP

Instancia: LAB-JACD. Autor: JACD. Fecha: no-registrada.

![EV-JACD-001 — Descubrimiento ARP](../evidencias/originales/JACD/EV-JACD-001.png)

**Acción:** sudo arp-scan -l --interface=ens36 | tee enum/arp_scan.txt

**Observado:** Se observa ens36 con IP atacante 192.168.18.129; responden 192.168.18.1, .130 y .254. La MAC de .130 es 00:0c:29:55:ea:9d.

**Interpretación y límites:** La captura acredita respuestas ARP. La asignación de .130 a DC-1 y los roles de .1/.254 proceden de las notas de Jaime; la captura sola no acredita esos roles ni el modo Host-Only.

### EV-JACD-002 · Conectividad ICMP

Instancia: LAB-JACD. Autor: JACD. Fecha: no-registrada.

![EV-JACD-002 — Conectividad ICMP](../evidencias/originales/JACD/EV-JACD-002.png)

**Acción:** ping -c 3 $IP | tee enum/ping.txt

**Observado:** La variable IP se resuelve a 192.168.18.130: 3 paquetes recibidos, 0% de pérdida y TTL 64.

**Interpretación y límites:** Conectividad observada en esta sesión. TTL 64 es un indicio, no confirmación del sistema operativo; falta evidencia de consola mencionada en las notas.

### EV-EJVA-001 · Pantalla de arranque

Instancia: LAB-EJVA. Autor: EJVA. Fecha: no-registrada.

![EV-EJVA-001 — Pantalla de arranque](../evidencias/originales/EJVA/EV-EJVA-001.png)

**Acción:** Observación de consola de la VM; no hay comando de terminal en esta captura.

**Observado:** Menú GNU GRUB con entrada Debian GNU/Linux y Linux 3.2.0-4-486.

**Interpretación y límites:** Indicio del sistema configurado para arrancar. No prueba la versión efectivamente ejecutada ni vincula por sí sola esta consola a 192.168.81.130.

### EV-EJVA-002 · Interfaces y descubrimiento ARP

Instancia: LAB-EJVA. Autor: EJVA. Fecha: no-registrada.

![EV-EJVA-002 — Interfaces y descubrimiento ARP](../evidencias/originales/EJVA/EV-EJVA-002.png)

**Acción:** ip a; sudo arp-scan -l --interface=ens36 (acciones visibles, ejecutadas por separado)

**Observado:** Atacante ens33 192.168.80.128/24 y ens36 192.168.81.129/24. Responden .1, .130 y .254 en 192.168.81.0/24; .130 tiene MAC 00:0c:29:79:c1:61. Hay advertencias de permisos sobre archivos de fabricantes.

**Interpretación y límites:** La advertencia no impidió recibir respuestas. Falta captura del hipervisor que confirme aislamiento; dos interfaces no prueban Bridge ni Host-Only.

### EV-EJVA-003 · Descubrimiento y escaneo TCP completo

Instancia: LAB-EJVA. Autor: EJVA. Fecha: no-registrada.

![EV-EJVA-003 — Descubrimiento y escaneo TCP completo](../evidencias/originales/EJVA/EV-EJVA-003.png)

**Acción:** sudo nmap -sn 192.168.81.130; sudo nmap -p- --min-rate 5000 -T4 -v -oN nmap_fullscan.txt 192.168.81.130 (dos ejecuciones)

**Observado:** Nmap 7.98 muestra host activo y puertos TCP 22, 80, 111 y 57249 abiertos; 65531 cerrados. Hora visible de inicio: 2026-10-03 11:16 -0500, sin segundos en esta captura.

**Interpretación y límites:** Superficie TCP observada, no vulnerabilidades. 57249 aparece todavía unknown en este escaneo; el escaneo de servicios posterior lo identifica. No demuestra cobertura UDP.

### EV-EJVA-004 · Salida guardada del escaneo TCP

Instancia: LAB-EJVA. Autor: EJVA. Fecha: 2026-10-03T11:16:35-05:00.

![EV-EJVA-004 — Salida guardada del escaneo TCP](../evidencias/originales/EJVA/EV-EJVA-004.png)

**Acción:** Vista de nmap_fullscan.txt en Kate; el encabezado conserva la invocación de Nmap.

**Observado:** Mismo objetivo y cuatro puertos. Encabezado: Sat Oct 3 11:16:35 2026; finaliza 11:16:43.

**Interpretación y límites:** Respalda la captura anterior. Se extrajo la imagen, no el archivo nmap_fullscan.txt original. Zona -05:00 tomada del escaneo relacionado; reloj del laboratorio no verificado.

### EV-EJVA-005 · Servicios y versiones Nmap

Instancia: LAB-EJVA. Autor: EJVA. Fecha: no-registrada.

![EV-EJVA-005 — Servicios y versiones Nmap](../evidencias/originales/EJVA/EV-EJVA-005.png)

**Acción:** sudo nmap -sV -sC -p22,80,111,57249 -oN nmap_services.txt 192.168.81.130

**Observado:** Nmap 7.98: 22/tcp OpenSSH 6.0p1 Debian 4+deb7u7; 80/tcp Apache httpd 2.2.22 Debian, generador Drupal 7; 111/tcp rpcbind 2-4; 57249/tcp status 1, RPC #100024. Inicio visible 2026-10-03 11:25 -0500 sin segundos.

**Interpretación y límites:** Versiones reportadas por fingerprinting; no demuestran exploit ni parche ausente. rpcinfo enumera puertos UDP, pero esto no sustituye escaneo UDP. El comando no incluye -O.

### EV-EJVA-006 · Gobuster y error al invocar URL

Instancia: LAB-EJVA. Autor: EJVA. Fecha: no-registrada.

![EV-EJVA-006 — Gobuster y error al invocar URL](../evidencias/originales/EJVA/EV-EJVA-006.png)

**Acción:** gobuster dir -u http://192.168.81.130 -w /usr/share/wordlists/dirb/common.txt

**Observado:** Gobuster v3.6 inicia y devuelve varias rutas con 403. También aparece error de Bash por introducir una URL directamente en terminal. Hay una línea de WPScan sin resultado visible.

**Interpretación y límites:** La URL debe abrirse en navegador o cliente HTTP; el error no es del servicio. No afirmar que WPScan se completó ni que hay WordPress. 403 no demuestra archivo accesible ni existencia inequívoca.

### EV-EJVA-007 · Resultados de enumeración de rutas

Instancia: LAB-EJVA. Autor: EJVA. Fecha: no-registrada.

![EV-EJVA-007 — Resultados de enumeración de rutas](../evidencias/originales/EJVA/EV-EJVA-007.png)

**Acción:** Continuación del mismo Gobuster de EV-EJVA-006.

**Observado:** Se observan 200 en /README, /robots.txt, /web.config, /xmlrpc.php, /LICENSE y /user; 301 en varios directorios; 403 en /admin y otras rutas.

**Interpretación y límites:** Los códigos son observaciones de enumeración. No prueban por sí solos divulgación sensible, listado de directorios o acceso administrativo. Comprobar contenido y controles antes de asignar hallazgo.

### EV-EJVA-008 · Consultas HTTP y error de head

Instancia: LAB-EJVA. Autor: EJVA. Fecha: no-registrada.

![EV-EJVA-008 — Consultas HTTP y error de head](../evidencias/originales/EJVA/EV-EJVA-008.png)

**Acción:** curl -s a /xmlrpc.php, /web.config, /robots.txt y /README; README se canaliza a head -n 30 tras un intento con 30~.

**Observado:** Se ve error por argumento 30~; luego se repite. xmlrpc.php responde que acepta POST; web.config devuelve XML.

**Interpretación y límites:** Conservar el error y su corrección. GET a xmlrpc.php no demuestra ejecución remota. Un web.config servido por Apache no demuestra IIS ni exposición de secretos.

### EV-EJVA-009 · Contenido de robots.txt

Instancia: LAB-EJVA. Autor: EJVA. Fecha: no-registrada.

![EV-EJVA-009 — Contenido de robots.txt](../evidencias/originales/EJVA/EV-EJVA-009.png)

**Acción:** Continuación de las consultas curl de EV-EJVA-008.

**Observado:** robots.txt enumera rutas y reglas Disallow; aparece el comienzo del contenido README.

**Interpretación y límites:** Las reglas orientan enumeración; no equivalen a controles de acceso ni garantizan exposición de cada ruta.

### EV-EJVA-010 · Contenido de README

Instancia: LAB-EJVA. Autor: EJVA. Fecha: no-registrada.

![EV-EJVA-010 — Contenido de README](../evidencias/originales/EJVA/EV-EJVA-010.png)

**Acción:** Continuación de curl -s http://192.168.81.130/README | head -n 30.

**Observado:** El README describe Drupal y configuración; el fragmento no contiene una versión menor exacta.

**Interpretación y límites:** Corrobora familia tecnológica sin confirmar versión menor ni vulnerabilidad. No tratar drupal-x.y.z.tar.gz como una versión real.

### EV-EJVA-011 · Fingerprinting WhatWeb

Instancia: LAB-EJVA. Autor: EJVA. Fecha: no-registrada.

![EV-EJVA-011 — Fingerprinting WhatWeb](../evidencias/originales/EJVA/EV-EJVA-011.png)

**Acción:** whatweb http://192.168.81.130

**Observado:** WhatWeb devuelve HTTP 200, Apache 2.2.22, Drupal 7 y PHP 5.4.45-0+deb7u14 entre sus identificadores.

**Interpretación y límites:** Fingerprinting consistente con Nmap para HTTP. Versiones reportadas, no validación de CVE; registrar versión de WhatWeb y obtener respuesta original si se conserva.

### EV-JDOG-001 · Conectividad y escaneo en curso

![EV-JDOG-001](../evidencias/originales/JDOG/EV-JDOG-001.png)

Juan indica que configuró la VM en UTM y prueba desde Parrot. La captura muestra un descubrimiento previo de 256 direcciones con 3 hosts activos, pero el comando y la IP de uno de ellos no se ven completos. Se ve 192.168.128.4 con MAC CE:E9:EA:43:88:05 y también 192.168.128.2, cuyo rol no está identificado. No se deduce la IP atacante de esta imagen.

El comando ping -c 3 192.168.128.4 recibió 3 respuestas, 0% de pérdida, TTL 64 y RTT promedio 2.480 ms. Esto acredita conectividad; no confirma sistema operativo ni identidad DC-1.

Se ve nmap -sV -sC -p- 192.168.128.4. Nmap 7.95 inicia el 2026-10-03 a las 17:41 UTC (12:41 en Colombia), con precisión de minuto. La captura termina durante Script Scan, aproximadamente 98.05%, a los 19 segundos. No muestra el resultado final ni la tabla de puertos. El progreso varía; no hay evidencia de bloqueo en este fragmento. No se ve opción de salida a archivo.

Estado: conectividad observada y escaneo en curso al capturar. Objetivo candidato 192.168.128.4; falta vincular su MAC con el adaptador de DC-1 en UTM, evidenciar aislamiento y obtener la salida final. UTM/Parrot son información aportada por Juan, no configuración comprobada por esta imagen. No trasladar puertos ni versiones de LAB-JACD o LAB-EJVA a LAB-JDOG. Sin vulnerabilidades confirmadas.

PENDIENTE: numeración de figura, página y revisión de legibilidad en PDF.

### EV-JDOG-002 · Resultado final de Nmap

![EV-JDOG-002](../evidencias/originales/JDOG/EV-JDOG-002.png)

La salida final de Nmap sobre 192.168.128.4 muestra cuatro puertos TCP abiertos: 22/ssh (OpenSSH 6.0p1 Debian 4+deb7u7), 80/http (Apache httpd 2.2.22 Debian), 111/rpcbind 2-4 (RPC #100000) y 47118/status 1 (RPC #100024). Se reportan 65531 puertos TCP cerrados (conn-refused). Finaliza con 1 host activo en 29.18 segundos.

HTTP: título Welcome to Drupal Site | Drupal Site; generador Drupal 7; robots.txt con 36 entradas disallow, de las cuales Nmap muestra 15, incluyendo /CHANGELOG.txt. La tabla rpcinfo muestra registros TCP/UDP/TCP6/UDP6; no acredita un escaneo UDP independiente. Service Info indica Linux a partir del reconocimiento; no se usó -O en el comando visible previo.

La captura anterior EV-JDOG-001 contiene el comando nmap -sV -sC -p- 192.168.128.4 y Nmap 7.95 iniciado a las 17:41 UTC del 2026-10-03 (12:41 Colombia, precisión de minuto). La segunda captura fue enviada como continuación; la fecha exacta de captura no se registra. El puerto 47118 pertenece a esta observación de LAB-JDOG; no sustituirlo por 57249 de Eduardo ni 59236 declarado por Jaime.

Inventario TCP observado; sin vulnerabilidad, CVE ni CVSS confirmados. La familia Drupal 7 está reportada, pero no su versión menor. Falta corroborar identidad DC-1 y aislamiento mediante configuración UTM, y conservar salida original en texto. No hay prueba de shell ni escalamiento.

### EV-DQH-001 · Descubrimiento ARP de Daniel

Instancia: LAB-DQH. Autor: DQH. Fecha exacta: no-registrada.

![EV-DQH-001](../evidencias/originales/DQH/EV-DQH-001.png)

Respuestas ARP; .18.130 tiene MAC 00:0c:29:45:c1:6e. No muestra enumeración de usuarios SSH.

### EV-DQH-002 · Nmap de Daniel primera parte

Instancia: LAB-DQH. Autor: DQH. Fecha exacta: no-registrada.

![EV-DQH-002](../evidencias/originales/DQH/EV-DQH-002.png)

Escaneo iniciado 2026-10-03 14:57 -0500; muestra SSH, HTTP y RPC. No es Hydra.

### EV-DQH-003 · Nmap de Daniel segunda parte

Instancia: LAB-DQH. Autor: DQH. Fecha exacta: no-registrada.

![EV-DQH-003](../evidencias/originales/DQH/EV-DQH-003.png)

53497/tcp status y cierre Nmap; MAC 00:0c:29:45:c1:6e. No muestra login SSH.

### EV-DQH-004 · Página inicial Drupal de Daniel

Instancia: LAB-DQH. Autor: DQH. Fecha exacta: no-registrada.

![EV-DQH-004](../evidencias/originales/DQH/EV-DQH-004.png)

Página pública en .18.130. No muestra SUID ni escalamiento.

### EV-DQH-005 · WhatWeb de Daniel

Instancia: LAB-DQH. Autor: DQH. Fecha exacta: no-registrada.

![EV-DQH-005](../evidencias/originales/DQH/EV-DQH-005.png)

Fingerprinting Apache/Drupal/PHP. No muestra root ni bandera final.

### EV-JACD-003 · Shell inicial Drupalgeddon

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-003](../evidencias/originales/JACD/EV-JACD-003.png)

Sesión del módulo drupal_drupageddon hacia .18.130; id y whoami muestran www-data. Fecha visible: 2026-10-03 15:42:07 -0500, apertura de sesión, no hora de captura.

### EV-JACD-004 · Shell con EUID root

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-004](../evidencias/originales/JACD/EV-JACD-004.png)

/tmp/rootbash -p seguido de id: uid=33(www-data), euid=0(root). Prueba privilegio efectivo; falta hostname en la misma captura.

### EV-JACD-005 · Recuperación de contraseña mediante Hashcat

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-005](../evidencias/originales/JACD/EV-JACD-005.png)

Hashcat modo 7900 muestra candidato recuperado; lista personalizada incluye esa misma contraseña. No demuestra debilidad intrínseca del algoritmo ni origen independiente de la lista.

### EV-JACD-006 · Ejecución PHP desde página administrativa

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-006](../evidencias/originales/JACD/EV-JACD-006.png)

/node/3 muestra uid=33(www-data), hostname DC-1 y uname. Requiere sesión admin y activación previa de PHP Filter por el evaluador.

### EV-JACD-007 · Permisos de find

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-007](../evidencias/originales/JACD/EV-JACD-007.png)

ls -la muestra propietario root y bit SUID en /usr/bin/find. Capturado ya desde prompt privilegiado: no asumir orden cronológico del descubrimiento.

### EV-JACD-008 · Preparación de shell temporal

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-008](../evidencias/originales/JACD/EV-JACD-008.png)

Secuencia desde www-data: primer archivo conserva dueño www-data; segundo creado mediante find queda root y se habilita SUID. Artefacto /tmp/rootbash debe retirarse al cerrar.

### EV-JACD-009 · Identidad de sesión inicial

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-009](../evidencias/originales/JACD/EV-JACD-009.png)

id, whoami, uname -a y hostname muestran www-data y DC-1. Vincular a sesión de EV-JACD-003 sin deducir continuidad solo por orden editorial.

### EV-JACD-010 · Lectura de banderas

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-010](../evidencias/originales/JACD/EV-JACD-010.png)

Lectura de banderas incluida la final desde rootbash. La evidencia de EUID está en EV-JACD-004; lectura de flag sola no reemplaza identidad.

### EV-JACD-011 · Activación de PHP Filter

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-011](../evidencias/originales/JACD/EV-JACD-011.png)

Mensaje de creación de formato PHP y guardado de configuración. Documenta modificación por el evaluador; no prueba que el módulo estuviera activo de origen.

### EV-JACD-012 · Creación de contenido PHP

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-012](../evidencias/originales/JACD/EV-JACD-012.png)

Formulario de página con código y formato PHP. Es precondición de EV-JACD-006, no explotación anónima.

### EV-JACD-013 · Sesión admin Drupal

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-013](../evidencias/originales/JACD/EV-JACD-013.png)

Interfaz Hello admin tras login reportado. Apoya acceso al CMS; la procedencia de hashes queda en notas sin captura de extracción.

### EV-JACD-014 · Opciones de Drupalgeddon

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-014](../evidencias/originales/JACD/EV-JACD-014.png)

Opciones del módulo y payload visibles. Configuración no equivale a explotación; resultado en EV-JACD-003.

### EV-JACD-015 · Escaneo TCP completo Jaime

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-015](../evidencias/originales/JACD/EV-JACD-015.png)

Nmap muestra 22/80/111/59236 TCP y MAC 00:0c:29:55:ea:9d; fecha visible 2026-10-03 11:28:13 sin zona en este archivo.

### EV-JACD-016 · Servicios Jaime primera parte

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-016](../evidencias/originales/JACD/EV-JACD-016.png)

Nmap SSH/HTTP/rpcbind y Drupal 7; salida en archivo mostrada. Fecha 2026-10-03 12:15:04 sin zona visible.

### EV-JACD-017 · Servicios Jaime segunda parte

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-017](../evidencias/originales/JACD/EV-JACD-017.png)

59236/tcp status; advierte condiciones poco fiables para fingerprinting de OS. No equiparar predicción con sistema corroborado.

### EV-JACD-018 · WhatWeb Jaime

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-018](../evidencias/originales/JACD/EV-JACD-018.png)

WhatWeb propone Drupal 7.22–7.26 como candidatos, no una versión exacta.

### EV-JACD-019 · Transferencia del archivo dirty.c

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-019](../evidencias/originales/JACD/EV-JACD-019.png)

Solo muestra descarga HTTP de dirty.c. No acredita ejecución de Dirty COW, el fallo reportado ni ausencia de cambios posteriores.

### EV-JACD-020 · Inventario RPC Jaime

Instancia: LAB-JACD. Autor: JACD. Fecha exacta: no-registrada.

![EV-JACD-020](../evidencias/originales/JACD/EV-JACD-020.png)

rpcinfo anuncia portmapper y status, aquí 55564/tcp. No se ve showmount ni salida que confirme ausencia universal de NFS.

### EV-DQH-006 · Métodos de autenticación SSH

Instancia: LAB-DQH. Autor: DQH. Fecha exacta: no-registrada.

![EV-DQH-006](../evidencias/originales/DQH/EV-DQH-006.png)

Nmap anuncia publickey y password; inicio 2026-10-04 13:50 -0500, precisión de minuto. No muestra usuario válido por enumeración.

### EV-DQH-007 · Enumeración SSH iniciada

Instancia: LAB-DQH. Autor: DQH. Fecha exacta: no-registrada.

![EV-DQH-007](../evidencias/originales/DQH/EV-DQH-007.png)

Metasploit muestra Checking for false positives. No hay resultado final que confirme usuarios.

### EV-DQH-008 · Hydra encuentra credencial

Instancia: LAB-DQH. Autor: DQH. Fecha exacta: no-registrada.

![EV-DQH-008](../evidencias/originales/DQH/EV-DQH-008.png)

Hydra muestra login flag4 y contraseña encontrada. Inicio 2026-10-04 14:05:17, final 14:07:52 sin zona visible: 2 min 35 s, no segundos.

### EV-DQH-009 · Acceso SSH como flag4

Instancia: LAB-DQH. Autor: DQH. Fecha exacta: no-registrada.

![EV-DQH-009](../evidencias/originales/DQH/EV-DQH-009.png)

ssh flag4@192.168.18.130 y prompt flag4@DC-1. La advertencia de fingerprint precede al login; no prueba ausencia de verificación fuera de captura.

### EV-DQH-010 · Lectura de flag4

Instancia: LAB-DQH. Autor: DQH. Fecha exacta: no-registrada.

![EV-DQH-010](../evidencias/originales/DQH/EV-DQH-010.png)

Sesión flag4@DC-1, listado de home y lectura de flag4.txt.

### EV-DQH-011 · SUID find y EUID root

Instancia: LAB-DQH. Autor: DQH. Fecha exacta: no-registrada.

![EV-DQH-011](../evidencias/originales/DQH/EV-DQH-011.png)

find SUID seguido de bash -p, whoami root e id uid=1001(flag4), euid=0(root). UID real no cambia a cero.

### EV-DQH-012 · EUID root y bandera final

Instancia: LAB-DQH. Autor: DQH. Fecha exacta: no-registrada.

![EV-DQH-012](../evidencias/originales/DQH/EV-DQH-012.png)

Misma secuencia visible con id y lectura /root/thefinalflag.txt. Hostname solo en prompt inicial: conviene captura final explícita de hostname.

### EV-DQH-013 · Contenido web.config

Instancia: LAB-DQH. Autor: DQH. Fecha exacta: no-registrada.

![EV-DQH-013](../evidencias/originales/DQH/EV-DQH-013.png)

Navegador muestra reglas XML de configuración. No se observan secretos ni se demuestra impacto de seguridad específico.

### EV-DQH-014 · Interfaces de Daniel

Instancia: LAB-DQH. Autor: DQH. Fecha exacta: no-registrada.

![EV-DQH-014](../evidencias/originales/DQH/EV-DQH-014.png)

ens36 192.168.18.129/24 y ens33 192.168.112.128/24. MAC objetivo .18.130 difiere de Jaime: no confundir instancias por IP repetida.
