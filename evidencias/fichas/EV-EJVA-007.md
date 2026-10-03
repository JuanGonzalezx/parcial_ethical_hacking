# EV-EJVA-007 · Resultados de enumeración de rutas

- Autor atribuido por el equipo: EJVA.
- Instancia documental: LAB-EJVA; no implica que las dos VMs sean la misma sesión.
- Fecha de prueba: no-registrada. La fecha de integración 2026-10-03 no sustituye la de ejecución.
- Origen: `cherrytree/respaldos/2026-10-03-antes-integracion/WriteUp_Basic_Pentesting1--parcial1EDuardo.ctb`, nodo 3, offset 798.
- Original extraído: `evidencias/originales/EJVA/EV-EJVA-007.png`. SHA-256: `3476c2bfd78539327c0d9ac130b386b6b276be1a0fae48da016548780f76a956`.
- Comando/acción visible: Continuación del mismo Gobuster de EV-EJVA-006.

## Resultado observado

Se observan 200 en /README, /robots.txt, /web.config, /xmlrpc.php, /LICENSE y /user; 301 en varios directorios; 403 en /admin y otras rutas.

## Interpretación y límites

Los códigos son observaciones de enumeración. No prueban por sí solos divulgación sensible, listado de directorios o acceso administrativo. Comprobar contenido y controles antes de asignar hallazgo.

![EV-EJVA-007 — Resultados de enumeración de rutas](../originales/EJVA/EV-EJVA-007.png)

Figura y página del PDF final: pendientes. Validación técnica por otro integrante: pendiente. La revisión visual documental no equivale a repetición de la prueba.
