# TEST-DQH-001 · Enumeración y fuerza bruta de SSH

Estado: ejecutada

- Autor / fecha / fase PTES: DQH / 2026-10-04 / Exploitation
- Instancia, IP y verificación del alcance: LAB-DQH, 192.168.18.130. Host dentro del alcance.
- Observación que origina la hipótesis y EV de respaldo: Puerto 22 abierto (SSH). Existen paneles web pero requieren mayor investigación, por lo que paralelamente se intenta un vector de fuerza bruta tras identificar posibles usuarios.
- Hipótesis y alternativa que podría refutarla: Es posible que algún usuario del sistema posea contraseñas débiles o por defecto. Se refutaría si falla el ataque de diccionario.
- Objetivo / precondiciones / herramienta: Identificar usuarios SSH válidos y obtener una credencial. Herramientas: nmap, msfconsole, hydra.
- Procedimiento propuesto y límites: 
  1. Identificar métodos de autenticación soportados en SSH (`nmap --script ssh-auth-methods`).
  2. Enumerar usuarios existentes mediante `scanner/ssh/ssh_enumusers` en Metasploit.
  3. Ejecutar Hydra contra SSH usando un diccionario básico (rockyou.txt). Límite: Solo atacar a los usuarios descubiertos.
- Condición de parada / recuperación de snapshot si necesaria: Bloqueo de IP (fail2ban) o lentitud en el servidor.
- Evidencias que se capturarán: EV-DQH-001 (Enumeración), EV-DQH-002 (Hydra).
- Criterio de aceptación y de descarte: Aceptación: Obtención de contraseña. Descarte: Diccionario agotado sin éxito.

## Después de la ejecución

Se verificó con Nmap que SSH acepta contraseñas. Mediante `ssh_enumusers` y un diccionario de usuarios probables (`root, admin, user, flag4, test, www-data`) se identificó actividad. Hydra logró encontrar la credencial `flag4:orange` en pocos segundos. Se registra el hallazgo PT-007 y se procede a la conexión.
