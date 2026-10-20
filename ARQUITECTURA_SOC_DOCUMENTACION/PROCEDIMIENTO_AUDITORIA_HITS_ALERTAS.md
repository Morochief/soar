# 🛡️ PROCEDIMIENTO ESTÁNDAR: AUDITORÍA DE HITS DE ALERTAS (STELLAR CYBER)

> **Script Oficial:** [`g:\Hermes + Antigravity\soar\stellar_alerts_checker.py`](file:///g:/Hermes%20+%20Antigravity/soar/stellar_alerts_checker.py)  
> **Objetivo:** Auditar todos los *Hits* individuales registrados en Stellar Cyber (incluso aquellos que no alcanzan umbral para abrir un caso), verificar comportamientos de endpoint y determinar si requieren creación manual de caso o descarte fundado.  
> **Capa RAG:** `PROCEDIMIENTO_ARQ` / `MEMORIA_SOC`

---

## 📌 1. ¿Por qué existe este procedimiento?
En la consola de Stellar Cyber (`https://technoma.stellarcyber.cloud/alerts?view=hits`), se registran cientos de alertas individuales (*Hits*). 
Muchas de estas alertas (como firmas informativas de IDS o anomalías aisladas de Machine Learning) **no generan un Caso automáticamente** porque el motor de correlación exige un umbral de score acumulado o múltiples vectores.

Sin embargo, ciertas alertas críticas (por ejemplo, ejecuciones de BIOC en Palo Alto Cortex XDR, comandos PowerShell o herramientas de reconocimiento como `arp.exe`) pueden quedar como un **hit aislado** y requieren que el analista las audite para decidir si amerita crear un caso.

---

## ⚡ 2. Comandos Operativos del Checker

El script [`stellar_alerts_checker.py`](file:///g:/Hermes%20+%20Antigravity/soar/stellar_alerts_checker.py) replica exactamente la vista web de Alertas / Hits con consultas directas al Data Lake:

```powershell
# 1. Resumen tabular de hits en las últimas 12 horas (con conteo, score máximo y severidades)
python stellar_alerts_checker.py --hours 12

# 2. Resumen de todos los hits generados desde las 00:00 de hoy
python stellar_alerts_checker.py --today

# 3. Filtrar únicamente hits con severidad Crítica/Alta o Score >= 70
python stellar_alerts_checker.py --hours 12 --critical

# 4. Inspeccionar en detalle los hits de endpoint y procesos sospechosos (muestra equipos, usuarios y comandos)
python stellar_alerts_checker.py --hours 12 --inspect

# 5. Caza y extracción forense profunda por palabra clave o tipo de alerta
python stellar_alerts_checker.py --hours 12 --type "arp.exe"
python stellar_alerts_checker.py --hours 12 --type "powershell"
python stellar_alerts_checker.py --hours 12 --type "Cortex XDR"
```

---

## 🔍 3. Criterio de Decisión: ¿Cuándo crear un Caso?

| Tipo de Hit | Comportamiento Típico | Decisión / Acción del Analista |
| :--- | :--- | :--- |
| **`Uncommon ARP cache listing via arp.exe`** | `arp -a` ejecutado en el host. Verificar si el usuario es de soporte/NOC haciendo troubleshooting o si es un usuario estándar sin motivo técnico. | Si es soporte/NOC: **Descartar**. Si es host no técnico en horario no laboral: **Crear Caso**. |
| **`Suspicious PowerShell Command Line`** | PowerShell con wrappers de herramientas de desarrollo (ej. VS Code Copilot, scripts locales de backup, Claude Desktop). | Inspeccionar el campo `action_process_image_command_line`. Si apunta a `.copilot/session-state`, npm o scripts corporativos: **Falso Positivo**. Si contiene `-enc` con descargas web externas (IEX, curl a IPs públicas): **Crear Caso Inmediato**. |
| **`Exploited C&C Connection`** | Peticiones DNS a `*.anydesk.com` o `remotedesktop.google.com`. | Verificar payload en `ids.payload_details.payload_printable`. Si es consulta estándar tipo A: **Descartar (Falso Positivo de firma IDS)**. |
| **`Login Failure / Kerberos Anomaly`** | Errores 4768 / 4771 por HealthMailbox o contraseñas expiradas. | Ya cubierto por casos automáticos de triaje: **Descartar**. |

---

## 📋 4. Evidencia Auditada de las Últimas 12 Horas (Caso Práctico)

1. **`arp.exe` en `NB-MGILLETTE` (`10.234.46.11`)**:
   * *Comando ejecutado*: `arp -a`.
   * *Diagnóstico*: Reconocimiento de red puntual por el usuario (5 invocaciones en los últimos 30 días). Actividad técnica benigna.
2. **`Suspicious PowerShell` en `NB-MANUELALM` (`192.168.100.239`)**:
   * *Comando ejecutado*: Wrapper de ejecución de **GitHub Copilot CLI** copiando una imagen local (`c:\Users\manuelalmada\.copilot\session-state\...\curl-mancuernas.webp`).
   * *Diagnóstico*: Falso positivo evidente generado por la extensión de IA del desarrollador. No hay payload malicioso.

---

## 🎯 5. Diagnóstico y Triaje del Widget "Top Risky Assets"

> **Script Oficial:** [`auditoria_cuota_stellar/20_auditoria_top_risky_assets.py`](file:///g:/Hermes%20+%20Antigravity/soar/auditoria_cuota_stellar/20_auditoria_top_risky_assets.py)  
> **Comandos:**  
> `python auditoria_cuota_stellar/20_auditoria_top_risky_assets.py --hours 48`  
> `python auditoria_cuota_stellar/20_auditoria_top_risky_assets.py --asset "forestdnszones"`  
> `python auditoria_cuota_stellar/20_auditoria_top_risky_assets.py --ip "192.168.15.23"`

### 🧠 Mecánica de Cálculo del Risk Score en Stellar Cyber:
El panel **Top Risky Assets** agrega y acumula el score de riesgo de las alertas (`aella-ser-*`) asociadas a cada objeto de activo (`stellar-index-v1-assets-*`). Existen dos trampas analíticas comunes que el analista debe discernir:

1. **Efecto Encadenamiento C&C sobre Controladores de Dominio (Falso Positivo Común):**
   * Cuando un DC (ej. `10.11.1.1` o `10.11.1.2`) recibe una alerta previa por volumen de paquetes DNS (*Private to Private Exploit Anomaly*), el motor de Stellar lo etiqueta como *"activo explotado"*.
   * Cualquier conexión subsiguiente interna que inicie o reciba el DC (por ejemplo, respuestas **LDAP TCP/389** a notebooks o tráfico de sincronización **FSSO UDP/8002** entre DCs) es clasificada automáticamente como `Exploited C&C Connection`, disparando el Risk Score a niveles de 50.0 - 95.0 a pesar de ser tráfico 100% administrativo interno de Technoma.
2. **Rotación DHCP y Asignación de Nombres Históricos:**
   * Stellar Cyber asocia un conjunto de IPs a una tarjeta de activo según su historial DHCP. Si un usuario (ej. `NB-NOC1` / `192.168.169.2`) intenta acceder a un puerto restringido (`3000/TCP`) en un servidor interno (`192.168.15.23`) y es bloqueado por la política `0` del FortiGate (`Internal Firewall Denial Anomaly`), el Risk Score puede subir a nombre de un hostname histórico de ese lease DHCP (ej. `nb-cgauto.technoma.local`).
3. **Duplicación por MAC Address:**
   * Un nombre DNS de zona compartida (como `forestdnszones.technoma.local`) puede aparecer repetido en la lista si los dos Domain Controllers físicos/virtuales (`10.11.1.1` y `10.11.1.2`) poseen direcciones MAC independientes registradas en VMware.

