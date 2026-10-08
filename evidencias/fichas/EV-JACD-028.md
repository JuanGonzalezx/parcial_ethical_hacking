# EV-JACD-028 | Inventario SUID desde sesión privilegiada

Instancia: LAB-JACD. Autor: JACD. Fecha exacta de captura: no-registrada.

**Acción y resultado observado:** find / -perm -4000 -type f enumera ejecutables, incluidos /usr/bin/find y /tmp/rootbash. El prompt ya es rootbash: esta captura no acredita inventario previo al escalamiento.

**Relevancia:** Complementa PT-002 sin reemplazar su validación ni revisión cruzada.

Fuente: cherrytree/individuales/PARCIAL_PENTEST_JAIME_DC1.ctb. SHA-256: 3fe111c83124edc6434032367a59b53d114cc931121e0261d46e84b0f1443276.

La fecha de integración es 2026-10-08, no la fecha de ejecución. Original conservado sin recodificar.
