# Revisión de hallazgos y plan de cierre

Revisión del 7 de octubre de 2026, para entrega el jueves 8. Hay evidencia de dos recorridos hasta privilegio efectivo root. El trabajo prioritario es corregir trazabilidad, cerrar interpretaciones, documentar cambios en las VMs y preparar el PDF; no aumentar el número de exploits.

## Git resuelto

El pull quedó en rebase al reaplicar `5eb9734 doc JD v0.1` sobre `9b43ac4`. Se combinaron docs/estado.md, evidencias/indice.csv e informe/INFORME.md conservando los aportes de Juan y Daniel. El commit reaplicado es `242a840`; main quedó un commit por delante de origin/main. No se hizo push. Al iniciar no había stash/autostash ni cambios sin commit adicionales fuera de los archivos en conflicto. Los cambios posteriores de esta revisión quedan sin commit para revisión del equipo.

## Resultados respaldados

| Frente | Evidencia observada | Cierre necesario |
|---|---|---|
| Jaime, Drupalgeddon SQLi | EV-JACD-003 muestra sesión www-data; 014 configuración y 009 identidad | Revisión cruzada y versión del módulo; separar de Drupalgeddon2 |
| Jaime, SUID find | EV-JACD-007/008/004 muestran permisos, preparación y EUID root | Cronología y limpieza de /tmp/rootbash |
| Jaime, contraseña admin | EV-JACD-005 recuperación; 013 sesión admin | Evidencia del origen del hash y construcción de wordlist |
| Jaime, PHP Filter | EV-JACD-011/012/006 activación, contenido y ejecución PHP | Presentar como escenario posterior a modificación administrativa, no RCE anónima preexistente |
| Daniel, SSH | EV-DQH-006/008/009/010: método password, Hydra, login y flag | No afirmar que ssh_enumusers confirmó flag4: 007 no muestra resultado final |
| Daniel, SUID find | EV-DQH-011/012: UID real flag4, EUID root y bandera | Captura final única con hostname explícito, revisión y limpieza |
| Eduardo, avances 5 octubre | Nodos 140–146 reportan pruebas posteriores sin nuevos EV | Obtener capturas originales o mantener como reportado |
| Juan | EV-JDOG-001/002: inventario TCP en UTM | Completar arquitectura; aportar revisión cruzada e integración final |

## Correcciones aplicadas

1. **Evidencias Daniel mal vinculadas.** EV-DQH-001 a 005 eran ARP, Nmap, web y WhatWeb, pero estaban etiquetadas como explotación/root. Se preservan los PNG y sus IDs; descripciones corregidas. Las capturas correctas que estaban como image copy se copiaron sin alterar a EV-DQH-006 a 014, con hashes y procedencia.
2. **Fichas ausentes.** PT-001 a 004 estaban solo en el nodo 108 del CTB de Jaime. Se crearon fichas Markdown y se extrajeron 18 capturas clave, EV-JACD-003 a 020. La transcripción de las fichas recibidas queda en fuente-PT-*.txt. El CTB original no fue modificado.
3. **Revisión real pendiente.** Seis fichas antes marcadas confirmado pasan editorialmente a en-validacion porque ningún compañero figura como revisor. Su resultado demostrado queda escrito expresamente. No se inventó firma de revisión; no se degradó la evidencia técnica. El índice recibido se conserva en indices-recibidos.json.
4. **SUID duplicado.** PT-002 y PT-008 describen la misma causa en instancias distintas. Conservar ambos IDs históricos y consolidar el conteo por causa; no reportar ocho vulnerabilidades únicas confirmadas.
5. **CVSS incoherente.** PT-007 decía 8.1 pero su vector AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N produce 9.1; las métricas de impacto aún requieren justificación para la cuenta flag4. PT-008 usa 7.8, categoría Alta, aunque decía Crítica. El índice deja severidad pendiente hasta cerrar revisión, y las propuestas se conservan en las fichas. PT-003 requiere revisar precondiciones; PT-004 requiere justificar Scope antes de aceptar su puntuación.
6. **Hash y palabra recuperada.** PT-003 demuestra recuperación de una contraseña y login, no debilidad intrínseca del algoritmo. El diccionario personalizado ya incluye la respuesta: aclarar su origen con el autor, sin presumir irregularidad ni conocimiento previo independiente.
7. **Cambios causados por el evaluador.** PHP Filter fue habilitado durante la prueba; /tmp/rootbash fue creado durante escalamiento. No presentarlos como configuraciones iniciales. Documentar retirada de artefactos/contenido y restauración del estado anterior.
8. **Enumeración no concluyente.** La captura de ssh_enumusers termina comprobando falsos positivos. Hydra tardó 2 min 35 s según sus marcas, no unos segundos. Agotar una wordlist sin éxito tampoco demostraría que la contraseña es fuerte.
9. **Misma IP no implica misma VM.** Jaime y Daniel usan .18.130, pero MAC observada de Jaime es 00:0c:29:55:ea:9d y de Daniel 00:0c:29:45:c1:6e. Sus cadenas se mantienen separadas.
10. **Fallos y cronología.** Dirty COW tiene relato de fallo, pero la captura revisada solo acredita descarga de dirty.c. No confirma ni descarta vulnerabilidad del kernel. Algunas capturas SUID de Jaime ya tienen prompt rootbash: ordenar por sesiones reales, no por número de figura. NFS no se descarta globalmente por un rpcinfo sin programas NFS en esa sesión.

## Hasta dónde explorar ahora

**Prioridad alta, hoy 7:** reconstruir y cerrar la cadena ya lograda; capturar en una sesión autorizada usuario/ID efectivo/hostname, identificar instancia y snapshot, recuperar salidas originales y documentar limpieza. Registrar lo que falta sin repetir ataques innecesarios. Si root ya está logrado, seguir la condición de parada acordada por Jaime y limitarse a prueba de compromiso/cierre.

**Validación dirigida si queda tiempo:** corroborar versión/configuración que sustenta PT-001; evidencia del origen de hashes y permisos para PT-003; comparar web.config con configuración pública para decidir si PT-006 queda como observación. Completar justificación de impactos y retest propuesto; no afirmar retest realizado.

**No priorizar antes de entregar:** una segunda RCE por Drupalgeddon2, nuevos exploits de kernel, fuerza bruta más extensa, DoS o persistencia. No aportan por sí solos más puntos y pueden romper la instancia o dejar cambios. PT-005 puede quedar honestamente como hipótesis no validada y PT-006 como observación sin impacto demostrado.

## Reparto concreto para el cierre

| Responsable propuesto | Entrega interna de hoy | Revisor propuesto |
|---|---|---|
| Juan | Integrar informe y corregir referencias/figuras; verificar arquitectura y estados | Jaime |
| Jaime | Revisar PT-001 a 004, procedencia de hash/wordlist, cronología y limpieza | Juan |
| Daniel | Revisar PT-007/008, CVSS, captura final de identidad y explicación de SSH | Eduardo |
| Eduardo | Aportar capturas de su sesión reportada o declarar límites; revisar cadena Daniel | Daniel |

Los revisores son propuestas, no aprobaciones realizadas. Mañana 8: revisión visual completa del PDF, índice/páginas, defensa por los cuatro y entrega a la hora que confirme el docente.

## Fuentes técnicas consultadas el 7 de octubre

- Rapid7, fuente del módulo drupal_drupageddon: https://raw.githubusercontent.com/rapid7/metasploit-framework/master/modules/exploits/multi/http/drupal_drupageddon.rb — relaciona el módulo con CVE-2014-3704 y corrección histórica 7.32; no acredita la versión instalada del módulo del alumno.
- Drupal, SA-CORE-2018-002: https://www.drupal.org/sa-core-2018-002 — vulnerabilidad diferente, CVE-2018-7600. No validada por usar el módulo de 2014.
- FIRST CVSS 3.1: https://www.first.org/cvss/v3.1/specification-document — vector, cálculo y categorías; no sustituye justificación del impacto observado.
- MITRE CWE-258: https://cwe.mitre.org/data/definitions/258.html — contraseña vacía; no corresponde a la credencial no vacía del caso SSH.
- MITRE CWE-521: https://cwe.mitre.org/data/definitions/521.html — requisitos de contraseña.
- Drupal ciclo de soporte: https://www.drupal.org/about/core/policies/core-release-cycles/schedule — Drupal 7 terminó soporte comunitario el 5 de enero de 2025; recomendar migración soportada, no solo una versión histórica parchada.

No se consultaron walkthroughs ni se ejecutaron pruebas contra las VMs. El validador estructural no comprueba veracidad, calidad visual del PDF ni aprobación humana.
