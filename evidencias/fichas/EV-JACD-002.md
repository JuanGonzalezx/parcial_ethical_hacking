# EV-JACD-002 · Conectividad ICMP

- Autor atribuido por el equipo: JACD.
- Instancia documental: LAB-JACD; no implica que las dos VMs sean la misma sesión.
- Fecha de prueba: no-registrada. La fecha de integración 2026-10-03 no sustituye la de ejecución.
- Origen: `cherrytree/respaldos/2026-10-03-antes-integracion/PARCIAL_PENTEST_JAIME_DC1.ctb`, nodo 8, offset 614.
- Original extraído: `evidencias/originales/JACD/EV-JACD-002.png`. SHA-256: `c2846070dfbafbb4153a371687268633637513ae57a38f40429c2b05411819ec`.
- Comando/acción visible: ping -c 3 $IP | tee enum/ping.txt

## Resultado observado

La variable IP se resuelve a 192.168.18.130: 3 paquetes recibidos, 0% de pérdida y TTL 64.

## Interpretación y límites

Conectividad observada en esta sesión. TTL 64 es un indicio, no confirmación del sistema operativo; falta evidencia de consola mencionada en las notas.

![EV-JACD-002 — Conectividad ICMP](../originales/JACD/EV-JACD-002.png)

Figura y página del PDF final: pendientes. Validación técnica por otro integrante: pendiente. La revisión visual documental no equivale a repetición de la prueba.
