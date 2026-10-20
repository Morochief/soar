# Suite de Auditoría de Cuota y Telemetría Stellar Cyber (SOC Technoma)

Esta carpeta contiene las herramientas oficiales en Python para auditar en tiempo real la ingesta de datos, consumo de cuota de licencia y telemetría de red / firewall (FortiGate) a través de la API oficial de Stellar Cyber y Elasticsearch Data Lake.

---

## 🛠️ Herramientas Incluidas

| Script | Propósito | Endpoint Consultado |
| :--- | :--- | :--- |
| `01_consultar_consumo_licencia.py` | Muestra el consumo acumulado mensual (GB) y el historial diario de los últimos 14 días comparado contra la cuota (8.0 GB/día). | `/connect/api/v1/storage-usages/daily_and_monthly` |
| `02_resumen_diario_indices.py` | Resume el total de eventos del día por índice de Elasticsearch, clase de mensaje (`msg_class`) y tipo de dispositivo (`dev_type`). Permite pasar fecha como parámetro. | `/connect/api/data/*{fecha}*e511c3fc54cd4d668bb67612c2ef4b04*/_search` |
| `03_auditoria_fortigate_deep_dive.py` | Auditoría forense completa de FortiGate: desglose de subtipos (`forward`, `webfilter`), acciones (`accept`, `deny`, `passthrough`), top de reglas (`fw_policy_id`), interfaces y puertos. | Elasticsearch Data Lake (`aella-adr-*` / `aella-ser-*`) |
| `04_inspeccionar_politica_especifica.py` | Inspecciona muestras raw y campos parseados de una política específica de firewall (ej: `FG-Technoma_91`). | Elasticsearch Data Lake por `fw_policy_id` |
| `05_auditar_log_filters_existentes.py` | Audita los Log Filters activos en Stellar Cyber para verificar qué reglas de descarte están aplicadas a FortiGate. | `/connect/api/v1/log-filters` |
| `06_auditoria_historica_total.py` | Auditoría consolidada de todo el Data Lake (106.3M de logs): Top 15 políticas, Top 15 orígenes, Top 15 destinos. Correlación 1-a-1 con la vista "Threat Hunting Library -> Firewall". | Elasticsearch Data Lake (`dev_type: fw_fortigate`) |
| `07_investigar_activo_o_ip.py` | Permite auditar en detalle cualquier IP, hostname o activo anómalo (`192.168.169.102`, `10.11.4.2`, `192.168.16.6`, `BB09C2DPAG00002`). | Elasticsearch Data Lake por término / IP / Host |
| `10_analisis_filtrado_healthmailbox.py` | Audita factibilidad de supresión para eventos de autenticación de buzones de salud de Exchange (`Event ID 4776`). | Stellar Cyber API |
| `17_auditoria_dominios_y_syslog_diario.py` | Auditoría integral de las últimas 24h (o `--date YYYY-MM-DD`): Top Acciones, Top 35 URLs/Dominios UTM, Top 30 Dominios DNS en NDR, Syslog No-Firewall e inspección de puertos pesados (`--ports`). | Elasticsearch Data Lake (`*adr*`) |
| `18_auditoria_seguridad_y_efectividad_log_filters.py` | Audita los 54+ Log Filters detectando reglas sin `action` o huérfanas, y con `--verify-effectiveness` compara empíricamente Firewall (`msg_class: firewall`) vs NDR (`msg_class: interflow_traffic`) en 48h. | `/connect/api/v1/log_filters` + Data Lake |
| `19_actualizar_log_filters_en_caliente.py` | Actualiza en caliente (`PUT /connect/api/v1/log_filters/{id}`) los Log Filters ya vinculados a perfiles de sensor (`in_use.sensor_profile`) sin perder su asociación en el Modular Sensor. | `/connect/api/v1/log_filters/{id}` |
| `20_auditoria_top_risky_assets.py` | Audita los activos con mayor puntaje en **Top Risky Assets** cruzando el índice de activos (`*assets*`) contra las alertas analíticas (`*ser*`) para diagnosticar la causa raíz del Risk Score (falsos positivos, rotación DHCP, LDAP, SMB, o bloqueos por firewall). | Data Lake (`*assets*` y `*ser*`) |
| `21_chequeo_diario_analista_soc_elite.py` | **Workflow Integral Diario de Analista SOC Élite**: Ejecuta en un solo comando la auditoría de 6 fases (Cuota/Licencia, Salud de Sensores/Interflow, Triage de Casos, Matriz XDR Kill Chain, Diagnóstico de Alertas/Falsos Positivos y Top Risky Assets). | APIs y Data Lake Stellar Cyber |
| **Documentación** | **[GUIA_FILTROS_Y_ALERT_CUSTOMIZATIONS.md](GUIA_FILTROS_Y_ALERT_CUSTOMIZATIONS.md)** | Guía maestra de operadores: Log Filters vs Alert Customizations (`starts with`, `contains`, `is in watchlist`). |


---

## 🚀 Ejemplos de Uso

### 1. Ver consumo diario y mensual de la cuota:
```bash
python 01_consultar_consumo_licencia.py
```

### 2. Ver resumen general de eventos de hoy o de ayer:
```bash
python 02_resumen_diario_indices.py
# O para una fecha específica:
python 02_resumen_diario_indices.py 2026.10.14
```

### 3. Ejecutar Deep Dive de FortiGate (últimas 24h o fecha):
```bash
python 03_auditoria_fortigate_deep_dive.py
python 03_auditoria_fortigate_deep_dive.py 2026.10.14
```

### 4. Inspeccionar la Política 91 (WebFilter) o 74 (DNS):
```bash
python 04_inspeccionar_politica_especifica.py FG-Technoma_91
python 04_inspeccionar_politica_especifica.py FG-Technoma_74 2026.10.14
```

### 5. Verificar filtros de descarte activos:
```bash
python 05_auditar_log_filters_existentes.py
```

### 6. Ejecutar Auditoría Histórica Total (106.3M logs):
```bash
python 06_auditoria_historica_total.py
```

### 7. Investigar un IP o Hostname Anómalo:
```bash
python 07_investigar_activo_o_ip.py 192.168.169.102
python 07_investigar_activo_o_ip.py 10.11.4.2
python 07_investigar_activo_o_ip.py BB09C2DPAG00002
```

---

## 🔐 Requisitos y Variables de Entorno
Los scripts leen automáticamente las variables del entorno del sistema:
* `STELLAR_HOST`: Host de Stellar Cyber (por defecto: `technoma.stellarcyber.cloud`)
* `STELLAR_EMAIL`: Usuario analista SOC (`kevinmoraes@technoma.com.py`)
* `STELLAR_TOKEN`: Token o API Key de Stellar Cyber
