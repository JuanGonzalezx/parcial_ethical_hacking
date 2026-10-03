# EV-EJVA-008 · Consultas HTTP y error de head

- Autor atribuido por el equipo: EJVA.
- Instancia documental: LAB-EJVA; no implica que las dos VMs sean la misma sesión.
- Fecha de prueba: no-registrada. La fecha de integración 2026-10-03 no sustituye la de ejecución.
- Origen: `cherrytree/respaldos/2026-10-03-antes-integracion/WriteUp_Basic_Pentesting1--parcial1EDuardo.ctb`, nodo 3, offset 1100.
- Original extraído: `evidencias/originales/EJVA/EV-EJVA-008.png`. SHA-256: `7c792f582f325bd7a309ce963bfa4e2b47e85da01be16c389369eba4773659e0`.
- Comando/acción visible: curl -s a /xmlrpc.php, /web.config, /robots.txt y /README; README se canaliza a head -n 30 tras un intento con 30~.

## Resultado observado

Se ve error por argumento 30~; luego se repite. xmlrpc.php responde que acepta POST; web.config devuelve XML.

## Interpretación y límites

Conservar el error y su corrección. GET a xmlrpc.php no demuestra ejecución remota. Un web.config servido por Apache no demuestra IIS ni exposición de secretos.

![EV-EJVA-008 — Consultas HTTP y error de head](../originales/EJVA/EV-EJVA-008.png)

Figura y página del PDF final: pendientes. Validación técnica por otro integrante: pendiente. La revisión visual documental no equivale a repetición de la prueba.
