# TEST-DQH-001 · Enumeración y fuerza bruta de SSH

Estado: ejecutada

- Autor / fecha / fase PTES: DQH / 2026-10-04 / Exploitation
- Instancia, IP y verificación del alcance: LAB-DQH, 192.168.18.130. Host dentro del alcance.
- Observación que origina la hipótesis y EV de respaldo: Puerto 22 abierto (SSH). Existen paneles web pero requieren mayor investigación, por lo que paralelamente se intenta un vector de fuerza bruta tras identificar posibles usuarios.
- Hipótesis y alternativa que podría refutarla: Es posible que algún usuario del sistema posea contraseñas débiles o por defecto. Agotar un diccionario solo descarta sus candidatos en esa ejecución; no demuestra que la contraseña sea fuerte.
- Objetivo / precondiciones / herramienta: Identificar usuarios SSH válidos y obtener una credencial. Herramientas: nmap, msfconsole, hydra.
- Procedimiento propuesto y límites: 
  1. Identificar métodos de autenticación soportados en SSH (`nmap --script ssh-auth-methods`).
  2. Enumerar usuarios existentes mediante `scanner/ssh/ssh_enumusers` en Metasploit.
  3. Ejecutar Hydra contra SSH usando un diccionario básico (rockyou.txt). Límite: Solo atacar a los usuarios descubiertos.
- Condición de parada / recuperación de snapshot si necesaria: Bloqueo de IP (fail2ban) o lentitud en el servidor.
- Evidencias que se capturarán: EV-DQH-006 (Enumeración), EV-DQH-008 (Hydra).
- Criterio de aceptación y de descarte: Aceptación: Obtención de contraseña. Resultado negativo limitado: diccionario agotado sin éxito; no descarta debilidad general.

## Después de la ejecución

Se verificó con Nmap que SSH acepta contraseñas. Mediante `ssh_enumusers` y un diccionario de usuarios probables (`root, admin, user, flag4, test, www-data`) se identificó actividad. Hydra logró encontrar la credencial `flag4:orange` en 2 min 35 s según las marcas visibles de Hydra. Se registra el hallazgo PT-007 y se procede a la conexión.

Revisión 2026-10-07: EV-DQH-007 conserva el inicio de ssh_enumusers sin resultado final; no confirma por sí solo existencia del usuario. Acceso efectivo respaldado por EV-DQH-009/010.
