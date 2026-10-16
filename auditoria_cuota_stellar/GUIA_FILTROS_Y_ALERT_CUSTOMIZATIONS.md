# Guía Maestra de Filtros y Supresión en Stellar Cyber OpenXDR

Documentación técnica y operativa para la construcción de filtros en Stellar Cyber: **Log Filters (Pre-Ingesta / Cuota)** vs **Alert Customizations (Post-Ingesta / Detección y Tuning)**.

---

## 🧭 Los Dos Mundos de Filtrado en Stellar Cyber

| Dimensión | 1. Log Filters (Sensor / Pre-DPI) | 2. Alert Customizations (Post-Ingesta) |
| :--- | :--- | :--- |
| **Ubicación en UI** | `System → Data Filters → Log Filters` | `Detections → Alerts → View Alert → Add Alert Customization` |
| **Punto de Ejecución** | En el Sensor / Forwarder (Borde de red) | En el Data Processor / Motor de Alertas (Cloud) |
| **Impacto en Cuota** | **100% de ahorro** (Los logs descartados nunca entran al Data Lake ni suman GBs). | **No ahorra cuota** (Los logs crudos ya ingresaron; solo evita que se dispare la alerta o caso). |
| **Propósito Principal** | Matar ruido volumétrico de telemetría, DNS, heartbeats y denegaciones masivas de firewall. | Tuning fino de falsos positivos, supresión de cuentas de servicio (`HealthMailbox*`), ajuste de scores. |

---

## ⚡ 1. Alert Customizations (Tuning de Detecciones y Alertas)

Se utiliza para suprimir alertas falsas positivas generadas por Machine Learning o reglas IDS sin perder el log de auditoría crudo.

### 🎯 Acciones Disponibles (Action Trigger)
* **`Filter Out`**: Descarta la alerta por completo. No se registra en la vista de Alertas ni genera tickets.
* **`Adjust Score`**: Modifica la severidad/score numérico de la alerta para que no supere el umbral de apertura de caso (ej. bajar de 70 a 15).
* **`Ignore in Case Score`**: Permite que la alerta exista de forma informativa pero que no sume puntaje al caso consolidado del incidente.
* **`Add Custom Tag`**: Inyecta una etiqueta analítica (ej. `autorizado-ti`, `buzon-salud`) para clasificación.

### 🎛️ Operadores Oficiales Disponibles en Alert Customizations

| Operador | Comportamiento Técnico | Ejemplo de Uso |
| :--- | :--- | :--- |
| **`is`** | Coincidencia exacta estricta del valor. | `event_id is 4776` |
| **`is not`** | Exclusión exacta. | `srcip_host is not "DC-SRV01"` |
| **`contains`** | Subcadena contenida en cualquier parte del campo. | `srcip_username contains "HealthMailbox"` |
| **`does not contain`** | Descarta si la subcadena está presente. | `process_name does not contain "chrome"` |
| **`starts with`** | Coincidencia por prefijo inicial (ideal para comodines de cuentas y hashes). | `srcip_username starts with "HealthMailbox"` |
| **`ends with`** | Coincidencia por sufijo final (ideal para dominios y extensiones). | `dstip_host ends with ".googleapis.com"` |
| **`field exists`** | Evalúa si el campo fue parseado y tiene contenido en el JSON. | `unauthuser field exists` |
| **`field does not exist`**| Evalúa si el evento carece por completo de ese campo. | `threat_name field does not exist` |
| **`is in watchlist`** | Cruza el valor del campo contra una Watchlist corporativa de Stellar Cyber (IPs confiables, VIPs, etc.). | `srcip is in watchlist "Servidores_NOC"` |
| **`is not in watchlist`** | Alerta únicamente si el activo NO pertenece a la lista aprobada. | `srcip is not in watchlist "Gateways_Conocidos"` |

### 💡 Ejemplo Práctico: Silenciar Ruido de Exchange HealthMailbox
* **Scope:** Tenant `technoma` (o `All Tenants`).
* **Condiciones (Criterio ALL):**
  1. `msg_class` **`is`** `Microsoft-Windows-Security-Auditing`
  2. `event_id` **`is`** `4776`
  3. `srcip_username` **`starts with`** `HealthMailbox`
* **Acción:** `Filter Out`
* **Guardado del Filtro (Save alert filter as):**
  - **Name (Máx 100 caracteres):** `FilterOut_WinAudit_Exchange_HealthMailbox_4776`
  - **Notes (Máx 500 caracteres):** `"Supresión quirúrgica (Filter Out) de alertas de Login Failure / Brute Force generadas por eventos de auditoría de Windows 4776 sobre cuentas sintéticas HealthMailbox de Microsoft Exchange (VM-MARANDU / VMBASE8). Las cuentas presentan estado deshabilitado legítimo (0xc0000072) correspondiente a pruebas automatizadas de Managed Availability de Exchange, descartando fuerza bruta real."`
* **Resultado:** El motor de ML deja de emitir falsos positivos de *Brute Force / Login Failure* sobre las cuentas rotativas de salud de Exchange.

---

## 🛡️ 2. Log Filters (Control de Cuota y Pre-Ingesta en Sensor)

Se despliegan a través del sensor modular (`profile-modular-sensor-technoma`) para triturar los paquetes y logs antes de que consuman ancho de banda o almacenamiento.

### 📋 Operadores en Log Filters
* **`is` / `==`**: Coincidencia exacta de texto o número.
* **`matches`**: Evaluación contra múltiples valores o bloques CIDR (ej: `10.0.0.0/8`, `192.168.0.0/16`).
* **`contains`**: Búsqueda de subtexto en el payload del log.

### 💡 Ejemplos Desplegados en Producción:
1. **Descarte de Passthrough Benigno:**  
   `dev_type == fw_fortigate` AND `action == passthrough` AND `dstip matches [CDNs, Azure, Google, Webex]` ➔ **DROP**.
2. **Descarte de Heartbeats Palo Alto Traps:**  
   `dstip matches [34.98.77.231, 34.39.195.104]` AND `dstport == 443` ➔ **DROP**.
3. **Descarte de Denegaciones Wi-Fi DNS 53:**  
   `fw_policy_id == FG-Technoma_214` AND `dstport == 53` AND `action == deny` ➔ **DROP**.
