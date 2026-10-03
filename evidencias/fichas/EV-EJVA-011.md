# EV-EJVA-011 · Fingerprinting WhatWeb

- Autor atribuido por el equipo: EJVA.
- Instancia documental: LAB-EJVA; no implica que las dos VMs sean la misma sesión.
- Fecha de prueba: no-registrada. La fecha de integración 2026-10-03 no sustituye la de ejecución.
- Origen: `cherrytree/respaldos/2026-10-03-antes-integracion/WriteUp_Basic_Pentesting1--parcial1EDuardo.ctb`, nodo 3, offset 1141.
- Original extraído: `evidencias/originales/EJVA/EV-EJVA-011.png`. SHA-256: `fce9e3f66ea6dcbe524248b28fcbe42e4a79e53bba295da9f071213b9a39706d`.
- Comando/acción visible: whatweb http://192.168.81.130

## Resultado observado

WhatWeb devuelve HTTP 200, Apache 2.2.22, Drupal 7 y PHP 5.4.45-0+deb7u14 entre sus identificadores.

## Interpretación y límites

Fingerprinting consistente con Nmap para HTTP. Versiones reportadas, no validación de CVE; registrar versión de WhatWeb y obtener respuesta original si se conserva.

![EV-EJVA-011 — Fingerprinting WhatWeb](../originales/EJVA/EV-EJVA-011.png)

Figura y página del PDF final: pendientes. Validación técnica por otro integrante: pendiente. La revisión visual documental no equivale a repetición de la prueba.
