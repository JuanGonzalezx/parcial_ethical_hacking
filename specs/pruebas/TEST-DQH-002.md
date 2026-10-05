# TEST-DQH-002 · Escalada de privilegios local mediante SUID (find)

Estado: ejecutada

- Autor / fecha / fase PTES: DQH / 2026-10-04 / Privilege Escalation
- Instancia, IP y verificación del alcance: LAB-DQH, 192.168.18.130. Sesión activa como `flag4`.
- Observación que origina la hipótesis y EV de respaldo: Acceso de bajo privilegio (flag4) en la máquina. EV-DQH-003.
- Hipótesis y alternativa que podría refutarla: Pueden existir binarios SUID mal configurados que permitan ejecución de comandos como root.
- Objetivo / precondiciones / herramienta: Conseguir una shell interactiva de root. Herramientas: comandos nativos de Linux (`find`).
- Procedimiento propuesto y límites: 
  1. Buscar binarios con el bit SUID activo: `find / -perm -4000 -type f 2>/dev/null`.
  2. Si se encuentra alguno explotable (ej. `find`), usarlo para escalar privilegios.
  3. Ejecutar comando `/usr/bin/find . -exec /bin/sh -p \;` (o bash) para spawnear la shell.
- Condición de parada / recuperación de snapshot si necesaria: Ninguna acción destructiva, no requiere recuperación a menos que se dañe el sistema de archivos.
- Evidencias que se capturarán: EV-DQH-004 (SUID find), EV-DQH-005 (Acceso root).
- Criterio de aceptación y de descarte: Aceptación: Shell como UID 0 (root).

## Después de la ejecución

Al ejecutar la búsqueda de binarios SUID se halló `/usr/bin/find`. Utilizando la funcionalidad `-exec` de find (`/usr/bin/find /etc/passwd -exec /bin/bash -p \;`), se logró lanzar una shell Bash manteniendo los privilegios del SUID (root). Al confirmar con `whoami` e `id`, se demostró acceso total al sistema (UID 0). Se capturó `thefinalflag.txt`. Se registra el hallazgo PT-008.
