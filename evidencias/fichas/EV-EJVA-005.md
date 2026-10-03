# EV-EJVA-005 · Servicios y versiones Nmap

- Autor atribuido por el equipo: EJVA.
- Instancia documental: LAB-EJVA; no implica que las dos VMs sean la misma sesión.
- Fecha de prueba: no-registrada. La fecha de integración 2026-10-03 no sustituye la de ejecución.
- Origen: `cherrytree/respaldos/2026-10-03-antes-integracion/WriteUp_Basic_Pentesting1--parcial1EDuardo.ctb`, nodo 3, offset 501.
- Original extraído: `evidencias/originales/EJVA/EV-EJVA-005.png`. SHA-256: `fd47f0ac375aae9c92316922414be03af97d48d13bba48b4abb8088f8e2f1194`.
- Comando/acción visible: sudo nmap -sV -sC -p22,80,111,57249 -oN nmap_services.txt 192.168.81.130

## Resultado observado

Nmap 7.98: 22/tcp OpenSSH 6.0p1 Debian 4+deb7u7; 80/tcp Apache httpd 2.2.22 Debian, generador Drupal 7; 111/tcp rpcbind 2-4; 57249/tcp status 1, RPC #100024. Inicio visible 2026-10-03 11:25 -0500 sin segundos.

## Interpretación y límites

Versiones reportadas por fingerprinting; no demuestran exploit ni parche ausente. rpcinfo enumera puertos UDP, pero esto no sustituye escaneo UDP. El comando no incluye -O.

![EV-EJVA-005 — Servicios y versiones Nmap](../originales/EJVA/EV-EJVA-005.png)

Figura y página del PDF final: pendientes. Validación técnica por otro integrante: pendiente. La revisión visual documental no equivale a repetición de la prueba.
