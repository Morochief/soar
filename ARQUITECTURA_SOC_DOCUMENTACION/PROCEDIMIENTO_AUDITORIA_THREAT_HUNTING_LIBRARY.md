# 🔍 Procedimiento Operativo: Reconciliación y Auditoría 1:1 de Threat Hunting Library

**Código de Procedimiento:** `SOP-THN-HUNT-01`  
**Plataforma SIEM/XDR:** Stellar Cyber OpenXDR v7.0.0s  
**Analista:** Kevin Moraes  
**Herramienta Oficial:** [`threat_hunting_exact_auditor.py`](file:///g:/Hermes%20+%20Antigravity/soar/threat_hunting_exact_auditor.py)  
**Propósito:** Proporcionar una metodología formal y reproducible para auditar y reconciliar con precisión matemática el 100% de los números, agregaciones y tarjetas visuales de la vista **Threat Hunting Library / Interflow Search** de Stellar Cyber contra los índices crudos del Data Lake.

---

## 📌 1. Fundamento Técnico y Arquitectura de Índices

En la vista web de Stellar Cyber (`/investigate/hunting`), las tarjetas interactivas superiores (*Threat Hunting Library Cards*) consolidan telemetría de diferentes orígenes. Cada tarjeta consulta un índice específico y aplica filtros Lucene propios que muchas veces no son evidentes a simple vista:

| Tarjeta en UI | Índice Nativo en Data Lake | Sintaxis Lucene / Query de Agregación | Origen de Telemetría |
| :--- | :--- | :--- | :--- |
| **Firewall** | `stellar-index-*-adr-*` | `msg_class.keyword:firewall` | Syslog perimetral de Fortinet FortiGate (inicios `accept`, cierres `close` y bloqueos `deny`). |
| **Network Applications** | `stellar-index-*-adr-*` | `msg_class.keyword:interflow_traffic` | Sensor Modular NDR (Inspección DPI L7 de aplicaciones, tráfico web y protocolos). |
| **DNS Analysis** | `stellar-index-*-adr-*` | `msg_class.keyword:interflow_traffic AND (dstport:53 OR appid_name:DNS)` | Consultas DNS decodificadas y resueltas por el sensor modular en el SPAN Port. |
| **Google Workspace** | `stellar-index-*-audit-*` | `msg_class.keyword:gsuite OR engid_name:gsuite_Workspace-THN` | Conector Cloud de Google Workspace (Drive, logins de cuentas, administración de consola). |
| **All Login Failures** | `stellar-index-*-wineventlog-*` | `login_result.keyword:fail OR event_id:4768` | Fallos de autenticación Kerberos y Active Directory (ej. pre-autenticación y HealthMailboxes). |
| **Windows Logins** | `stellar-index-*-wineventlog-*` | `event_id:4624` | Inicios de sesión exitosos en controladores de dominio y servidores Windows auditados. |
| **Windows Privilege Escalations** | `stellar-index-*-wineventlog-*` | `event_id:4672` | Asignación de privilegios especiales / inicios de sesión de administradores (Event 4672). |
| **Windows New Processes** | `stellar-index-*-wineventlog-*` | `event_id:4688` | Creación y ejecución de ejecutables en servidores Windows con Sysmon/Auditoría activa. |
| **Windows Command Line** | `stellar-index-*-wineventlog-*` | `event_id:4688` *(con CommandLine)* | Líneas de comando completas ejecutadas en terminales PowerShell y CMD. |
| **Windows Login Failures** | `stellar-index-*-wineventlog-*` | `event_id:4625` | Fallos de inicio de sesión directo o interactivo (bad password, cuenta bloqueada). |
| **Windows Account Changes** | `stellar-index-*-wineventlog-*` | `event_id:(4720 OR 4722 OR 4724 OR 4738)` | Cuentas de usuario creadas, habilitadas o modificadas en Active Directory. |
| **Sophos Endpoint** | `stellar-index-*-syslog-*,audit`| `msg_class.keyword:*sophos* OR engid_name:*sophos*` | Alertas y telemetría de antivirus y EDR Sophos Central. |
| **Non-Standard Port Usage** | `stellar-index-*-adr-*` | `tags:*non_standard* OR xdr_event.display_name:*Non-Standard*` | Protocolos conocidos cursados a través de puertos no habituales. |

---

## ⚡ 2. Ejecución de la Auditoría Automatizada

El analista no necesita realizar cálculos manuales en la web. El script oficial ejecuta consultas agregadas con `track_total_hits: true` contra la API REST de Stellar Cyber:

```powershell
python threat_hunting_exact_auditor.py
```

### Opciones de Ejecución Avanzadas:
- **Auditoría de 24 horas (Predeterminado):** `python threat_hunting_exact_auditor.py`
- **Auditoría con desglose forense y comprobación de exclusiones:**  
  `python threat_hunting_auditor.py --hours 24`

---

## 🔍 3. Protocolo de Verificación ante Discrepancias o Alzas de Tráfico

Cuando una de las tarjetas muestre un número inusualmente alto (ej. `Firewall > 2.0M` o `DNS Analysis > 700k`), el analista debe aplicar el siguiente árbol de decisión:

```
¿Qué tarjeta presenta un valor anómalo?
 ├── Firewall (> 1.5M eventos/día)
 │    ├── 1. Consultar top acciones: `action.keyword` (accept, close, deny).
 │    ├── 2. Si predominan 'deny' en DMZ: Verificar ataque perimetral con ATH THN FW Ataque Recurrente.
 │    └── 3. Si predominan 'close': Evaluar filtro quirúrgico (ej. TCP 7001 hacia servidores internos).
 │
 ├── Network Applications (> 2.5M eventos/día)
 │    ├── 1. Consultar top 'appid_name': Verificar si Grafana, Zabbix o proxies saturan flujos.
 │    └── 2. Si son flujos benignos de monitoreo interno: Aplicar BPF en el Sensor Modular.
 │
 └── All Login Failures (> 50k eventos/día)
      ├── 1. Consultar top usuarios en `stellar-index-*-wineventlog-*`: `TargetUserName`.
      ├── 2. Si son cuentas `HealthMailbox*`: Confirmar ruido de sondas sintéticas de Exchange.
      └── 3. Si son cuentas reales: Activar Playbook de Fuerza Bruta / Credential Stuffing.
```

---

## 📋 4. Registro y Mantenimiento
Toda alteración en las tarjetas derivada de la creación de Log Filters (Drop de telemetría benigna o passthrough) debe quedar registrada en la [Bitacora_Personal_Casos_SOC.md](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/Bitacora_Personal_Casos_SOC.md) vinculando el ID de regla, el veredicto forense y la confirmación de **0% ceguera de seguridad**.
