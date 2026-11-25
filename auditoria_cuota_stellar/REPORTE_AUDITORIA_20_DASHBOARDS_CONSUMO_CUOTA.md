# 📊 REPORTE EJECUTIVO DE AUDITORÍA: LOS 20 DASHBOARDS DE THREAT HUNTING
## Diagnóstico Forense de Ingesta, Volumetría y Causas Raíz del Consumo de Cuota en Stellar Cyber

**Fecha de Auditoría**: 30 de Octubre de 2026 (Tiempo Real)  
**Tenant Evaluado**: `technoma` (CustID: `e511c3fc54cd4d668bb67612c2ef4b04`)  
**Índices Auditados**: Data Lake completo de la jornada (`*2026.10.30*`)  
**Total de Eventos Analizados**: **27,737,039 eventos agregados**

---

## 1. Matriz General de los 20 Dashboards de Threat Hunting

Mediante script nativo en Go ejecutado contra el Data Lake de Stellar Cyber con conteo exacto (`track_total_hits: true`), se obtuvo la radiografía matemática de los 20 dashboards:

| Posición | Dashboard / Módulo | Eventos Reales Hoy | % del Total | Nivel de Impacto en Cuota |
| :---: | :--- | :---: | :---: | :--- |
| 🥇 **1** | **Firewall** | **11,784,513** | **42.49%** | 🚨 **DEVORADOR #1 (Crítico)** |
| 🥈 **2** | **Network Applications** | **7,311,714** | **26.36%** | 🚨 **DEVORADOR #2 (Crítico)** |
| 🥉 **3** | **DNS Analysis** | **6,491,552** | **23.40%** | 🚨 **DEVORADOR #3 (Crítico)** |
| 4 | **Google Workspace** | 1,049,786 | 3.78% | 🔹 Moderado (API Connectors) |
| 5 | **Plain Text Passwords** | 473,927 | 1.71% | 🟢 Bajo (Consultas LDAP 389) |
| 6 | **Windows Logins** | 355,480 | 1.28% | 🟢 Bajo (Event ID 4624) |
| 7 | **Windows Privilege Escalations** | 106,818 | 0.39% | 🟢 Residual (Event ID 4672) |
| 8 | **Windows New Processes** | 51,901 | 0.19% | 🟢 Residual (Event ID 4688) |
| 9 | **External File Storage Access** | 32,792 | 0.12% | 🟢 Mínimo |
| 10 | **Cloud Email Provider Access** | 21,993 | 0.08% | 🟢 Mínimo |
| 11 | **Non-Standard Port Usage** | 21,306 | 0.08% | 🟢 Mínimo |
| 12 | **Sophos Endpoint** | 18,340 | 0.07% | 🟢 Mínimo |
| 13 | **All Login Failures** | 16,545 | 0.06% | 🟢 Mínimo |
| 14 | **Windows PowerShell Startups** | 358 | 0.00% | 🟢 Mínimo |
| 15 | **Windows Account Lockouts** | 12 | 0.00% | 🟢 Mínimo |
| 16 | **Windows Login Failures** | 2 | 0.00% | 🟢 Mínimo |
| 17 | **Windows Account Changes** | 0 | 0.00% | ⚪ Sin eventos |
| 18 | **Windows Software Installed** | 0 | 0.00% | ⚪ Sin eventos |
| 19 | **Windows Command Line** | 0 | 0.00% | ⚪ Sin eventos |
| 20 | **Tunneled Traffic** | 0 | 0.00% | ⚪ Sin eventos |
| **TOTAL**| **20 Dashboards Agregados** | **27,737,039** | **100.00%** | **Consumo Proyectado: ~8.5 a 9.2 GB/día** |

---

## 2. Diagnóstico de Causa Raíz: ¿Qué está comiendo el 92.25% del tráfico?

Los primeros **3 dashboards consumen el 92.25% de toda la licencia**:
$$\text{Firewall (42.5\%)} + \text{Network Apps (26.4\%)} + \text{DNS (23.4\%)} = \mathbf{92.25\%}$$

A continuación se desglosa exactamente qué protocolos, aplicaciones y máquinas generan este volumen:

### A. Devorador #1: Dashboard de Firewall (11.78M eventos / 42.5%)
* **Acciones más ruidosas**:
  * `accept`: **2,262,393 eventos** (Tráfico permitido regular).
  * `deny`: **1,321,774 eventos** (Bloqueos de firewall perimetrales).
  * `close`: **1,055,461 eventos** (Cierres normales de sesión TCP).
  * `server-rst` / `client-rst`: **1,204,187 eventos** (Resets de conexión web).
* **Aplicaciones y Protocolos que más pesan**:
  * **SSL / HTTPS**: **3,268,996 eventos** combinados (Navegación general cifrada).
  * **Puerto tcp/1280**: **620,943 eventos** (Conexiones hacia el agente de monitoreo / SolarWinds / N-able).
  * **Windows AD**: **474,704 eventos** (Tráfico de autenticación interna FSSO / RPC).

### B. Devorador #2: Dashboard de Network Applications (7.31M eventos / 26.4%)
* **Origen**: Corresponde al índice `interflow_traffic` generado por la inspección profunda (DPI) del **Sensor Modular Technoma**.
* **Causa**: El sensor inspecciona cada flujo TCP/UDP en el switch central (puerto mirror/SPAN). Aunque un Log Filter descarte el log de syslog de FortiGate, **el sensor NDR sigue capturando el flujo de red L4/L7**, duplicando la visibilidad analítica pero duplicando el volumen en el Data Lake.

### C. Devorador #3: Dashboard de DNS Analysis (6.49M eventos / 23.4%)
* **Top 3 Dominios más consultados**:
  1. **`ad.technoma.local`**: **4,528,044 consultas** (Representa el **69.7% de todo el DNS** de la empresa).
  2. **`dns.google`**: **1,438,769 consultas** (Consultas externas a `8.8.8.8` / `8.8.4.4`).
  3. **`technoma.local`**: **346,948 consultas**.
* **Top Máquinas que generan la tormenta DNS**:
  * **`10.11.1.1` (Controlador de Dominio AD1)**: **1,235,481 consultas directas**.
  * Resto de servidores y estaciones: Generan ráfagas continuas de sondeo cada pocos segundos contra `ad.technoma.local`.

---

## 3. Plan de Acción y Recomendaciones para Aplanar la Cuota

Para evitar que la ingesta diaria toque el techo de los **10.0 GB** (ayer cerró en `8.51 GB`):

1. **Optimización de DNS Interno en Log Filters (Ahorro estimado: ~1.5 GB/día)**:
   * Aplicar un filtro de ingesta sobre consultas recursivas internas repetitivas dirigidas a `ad.technoma.local` hacia el DC (`10.11.1.1`), ya que no representan riesgo de túnel C2 ni DGA.
2. **Supresión de Syslog para tcp/1280 (Ahorro estimado: ~500 MB/día)**:
   * El tráfico administrativo de telemetría interna en el puerto 1280 genera más de 620,000 eventos diarios de ruido sin valor de seguridad.
3. **Revisión de Google Workspace (Ahorro estimado: ~300 MB/día)**:
   * La integración de Google Workspace genera más de 1M de logs diarios por sincronizaciones de tokens de OAuth de usuarios corporativos.
