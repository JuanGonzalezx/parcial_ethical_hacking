# EV-JACD-001 · Descubrimiento ARP

- Autor atribuido por el equipo: JACD.
- Instancia documental: LAB-JACD; no implica que las dos VMs sean la misma sesión.
- Fecha de prueba: no-registrada. La fecha de integración 2026-10-03 no sustituye la de ejecución.
- Origen: `cherrytree/respaldos/2026-10-03-antes-integracion/PARCIAL_PENTEST_JAIME_DC1.ctb`, nodo 8, offset 111.
- Original extraído: `evidencias/originales/JACD/EV-JACD-001.png`. SHA-256: `f37a4e7324f5a51492e6143aac2e072504cd8c3563f45797f23b8f90a6694d51`.
- Comando/acción visible: sudo arp-scan -l --interface=ens36 | tee enum/arp_scan.txt

## Resultado observado

Se observa ens36 con IP atacante 192.168.18.129; responden 192.168.18.1, .130 y .254. La MAC de .130 es 00:0c:29:55:ea:9d.

## Interpretación y límites

La captura acredita respuestas ARP. La asignación de .130 a DC-1 y los roles de .1/.254 proceden de las notas de Jaime; la captura sola no acredita esos roles ni el modo Host-Only.

![EV-JACD-001 — Descubrimiento ARP](../originales/JACD/EV-JACD-001.png)

Figura y página del PDF final: pendientes. Validación técnica por otro integrante: pendiente. La revisión visual documental no equivale a repetición de la prueba.
