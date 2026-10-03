# EV-EJVA-006 · Gobuster y error al invocar URL

- Autor atribuido por el equipo: EJVA.
- Instancia documental: LAB-EJVA; no implica que las dos VMs sean la misma sesión.
- Fecha de prueba: no-registrada. La fecha de integración 2026-10-03 no sustituye la de ejecución.
- Origen: `cherrytree/respaldos/2026-10-03-antes-integracion/WriteUp_Basic_Pentesting1--parcial1EDuardo.ctb`, nodo 3, offset 796.
- Original extraído: `evidencias/originales/EJVA/EV-EJVA-006.png`. SHA-256: `da564cbf5b82c304361d8da03f7854ec060bf5895179fde33f01346be0b78ce0`.
- Comando/acción visible: gobuster dir -u http://192.168.81.130 -w /usr/share/wordlists/dirb/common.txt

## Resultado observado

Gobuster v3.6 inicia y devuelve varias rutas con 403. También aparece error de Bash por introducir una URL directamente en terminal. Hay una línea de WPScan sin resultado visible.

## Interpretación y límites

La URL debe abrirse en navegador o cliente HTTP; el error no es del servicio. No afirmar que WPScan se completó ni que hay WordPress. 403 no demuestra archivo accesible ni existencia inequívoca.

![EV-EJVA-006 — Gobuster y error al invocar URL](../originales/EJVA/EV-EJVA-006.png)

Figura y página del PDF final: pendientes. Validación técnica por otro integrante: pendiente. La revisión visual documental no equivale a repetición de la prueba.
