# 🔍 PROCEDIMIENTO ESTÁNDAR DE INSPECCIÓN DE QUERIES, LOG FILTERS Y ATH (STELLAR CYBER)
> **Directiva Operativa para la IA (Antigravity)**: Cuando el usuario pregunte por sus queries guardadas, filtros de logs, reglas ATH o exclusiones de alertas (como `HealthMailbox` o `Passthrough`), **NUNCA** adivines endpoints ni hagas barridos manuales. Ejecutá directamente [**`stellar_query_inspector.py`**](file:///g:/Hermes%20+%20Antigravity/soar/stellar_query_inspector.py).

---

## ⚡ 1. COMANDOS RÁPIDOS DE EJECUCIÓN (`stellar_query_inspector.py`)

| Solicitud del Analista / Usuario | Comando Exacto | Qué devuelve |
| :--- | :--- | :--- |
| **"¿Qué queries tengo guardadas?"** | `python stellar_query_inspector.py --queries` | Lista las 72+ queries guardadas con su creador, tenant y dónde están en uso (`ATH`, `Corr`, `Chart`, `Rep`). |
| **"¿Qué queries están en uso activo?"** | `python stellar_query_inspector.py --queries --in-use` | Filtra exclusivamente las queries vinculadas a reglas ATH, Correlación o gráficos de Dashboards. |
| **"Mostrame qué hace la query X"** | `python stellar_query_inspector.py --query-detail "Healthmailbox"` | Extrae el JSON completo, las condiciones estructuradas y el Query DSL exacto en Elasticsearch. |
| **"¿Qué filtros de logs tenemos y qué filtran?"** | `python stellar_query_inspector.py --filters` | Desglosa el campo `content` (JSON interno) de los 51+ Log Filters mostrando `dev_type`, `op` y valores reales. |
| **"Revisá el filtro de passthrough / telemetría"** | `python stellar_query_inspector.py --filter-detail "passthrough"` | Filtra por nombre o contenido JSON dentro de `/connect/api/v1/log_filters`. |
| **"¿Qué dominios / categorías están generando más logs hoy?"** | `python stellar_query_inspector.py --top-domains --date 2026.10.16` | Extrae del Data Lake el ranking de los 40 dominios más ruidosos (`fortinet.hostname`), categorías FortiGuard y ASNs. |
| **"Auditá qué porcentaje cubre un filtro y qué deja pasar"** | `python stellar_query_inspector.py --audit-filter "Drop_FW_Passthrough_Benign_Telemetry"` | Cruza el Log Filter contra el Data Lake y muestra el % exacto de cobertura y el Top 15 de dominios que siguen entrando. |
| **"Agregá un dominio benigno a un filtro existente"** | `python stellar_query_inspector.py --add-domain "Drop_FW_Passthrough_Benign_Telemetry" "dominio.com"` | Suma uno o varios dominios (separados por comas) al campo `url contains` del filtro por API (`PUT`). |
| **"¿Qué reglas ATH / Playbooks están activos?"** | `python stellar_query_inspector.py --ath` | Consulta `/connect/api/v1/alert_watchers` y extrae triggers y acciones automáticas. |
| **"Limpiá las queries de prueba huérfanas"** | `python stellar_query_inspector.py --cleanup-orphans` *(agregar `--confirm` para borrar)* | Detecta queries temporales (`Gui_Hunt_*`, `AdHoc_Hunt_*`, `SOC_CLI_Hunt_*`) con `Uso = 0`. |
| **"Revisar los dominios consultados ayer, puertos pesados y syslog"** | `python auditoria_cuota_stellar/17_auditoria_dominios_y_syslog_diario.py` | Audita las últimas 24h (o `--date YYYY-MM-DD`): Top Acciones, Top 35 URLs UTM, Top 30 Dominios DNS en NDR, Syslog No-Firewall y muestras de puertos pesados (`--ports`). |
| **"Auditar cada Log Filter y verificar si es peligroso o si está funcionando (FW vs NDR)"** | `python auditoria_cuota_stellar/18_auditoria_seguridad_y_efectividad_log_filters.py --verify-effectiveness` | Lista los 54+ Log Filters, marca cuáles carecen de `action` o están sin perfil, y cruza empíricamente Firewall (`msg_class: firewall`) contra NDR (`msg_class: interflow_traffic`) en 48h. |
| **"Actualizar un Log Filter en caliente en el Modular Sensor sin usar la GUI"** | `python auditoria_cuota_stellar/19_actualizar_log_filters_en_caliente.py --status` *(o `--apply-baseline`)* | Aplica `PUT /connect/api/v1/log_filters/{id}` sobre filtros ya vinculados a `profile-modular-sensor-technoma` o `Profile-CajaAnde`, logrando Hot-Reload inmediato en el sensor. |

---

## 🧠 2. ARQUITECTURA DE FILTROS Y EXCLUSIONES EN STELLAR CYBER 7.0.0s

Es fundamental distinguir las **4 capas de filtrado** en Stellar Cyber para no confundir reducción de cuota con supresión de falsos positivos:

1. **Log Filters (`/connect/api/v1/log_filters`) — Nivel Colector / Sensor (Ahorro de Cuota):**
   - **Propósito:** Descartar logs crudos (`Drop`) antes de que se indexen en el Data Lake.
   - **Estructura:** La condición real vive serializada como string JSON dentro de la clave `content` (ej: `{"dev_type": "fw_fortigate", "rules": {"action": {"op": "==", "value": ["passthrough"]}}}`).
   - **Limitación:** Solo acepta los campos listados en [`campos de log filter.txt`](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/02_Base_de_Conocimiento/campos%20de%20log%20filter.txt) (no soporta `event_id` de Windows ni `fortinet.catdesc`).
   - **Procedimiento de Asociación en Caliente (Hot-Reload vía API `PUT`):**
     - El endpoint `/connect/api/v1/data_sensors/sensor_profiles` solo expone `GET` en la API pública (no admite `PUT`/`POST`).
     - Por lo tanto, cualquier filtro nuevo creado con `POST /connect/api/v1/log_filters` nace con `in_use: {}` hasta asociarlo manualmente en la interfaz web (`System -> Sensor Profiles -> Edit -> Log Filters`).
     - **Solución Operativa para Aplicar Filtros 100% por API:** Modificar mediante `PUT /connect/api/v1/log_filters/{id}` un filtro existente que **ya tenga `in_use: {"sensor_profile": ["profile-modular-sensor-technoma"]}`** (expandiendo sus puertos, subredes o valores con `op: "matches"` o `op: "=="`). El Modular Sensor recarga la nueva definición automáticamente en caliente sin perder el vínculo con el perfil.
   - **Regla de Oro Pre-Cambio (Verificación Empírica Firewall vs NDR):**
     - Antes de agregar `action == deny` o modificar un filtro histórico, **siempre** cruzar los conteos de las últimas 48h entre `msg_class: firewall` y `msg_class: interflow_traffic` usando [`18_auditoria_seguridad_y_efectividad_log_filters.py`](file:///g:/Hermes%20+%20Antigravity/soar/auditoria_cuota_stellar/18_auditoria_seguridad_y_efectividad_log_filters.py).
     - **Ejemplo crítico (`[28] Filter AD DNS out`):** Tiene `0 hits` en Firewall pero **390.633 flujos** en NDR (`10.11.1.1 -> 8.8.8.8:53`). No produce ceguera porque la tabla *NDR / DNS Analysis* ya inspecciona el 100% de las consultas DNS del Domain Controller, mientras el filtro ahorra ~195.000 logs diarios duplicados del FortiGate.

2. **Saved Queries (`/connect/api/v1/queries`) — Nivel Búsqueda, Dashboards y ATH:**
   - **Propósito:** Consultas guardadas reutilizables en Threat Hunting, gráficos (`in_use_chart`), reglas de correlación (`in_use_correlation`) y playbooks ATH (`in_use_ath`).
   - **Importante:** Guardar una query en la pestaña *Queries* **NO suprime alertas por sí sola** a menos que se cree como *Alert Filter* o *Case Filter*.

3. **Alert Filters & Case Filters (`System | Saved Objects | Queries and Filters` en GUI):**
   - **Propósito:** Suprimir la generación de alertas (`Alert Filters`) o casos (`Case Filters`) para falsos positivos recurrentes sin perder el log crudo en el Data Lake.
   - **Aplicación en GUI:**
     - Desde una alerta dentro de un caso: clic en ícono **`i` (More info)** $\rightarrow$ **`Actions` $\rightarrow$ `Add Alert Customization`**.
     - Desde el gestor central: **`System` $\rightarrow$ `Saved Objects` $\rightarrow$ `Queries and Filters` $\rightarrow$ pestaña `Alert Filters` $\rightarrow$ `Create`**.

4. **Caso Conocido: Ruido de Microsoft Exchange `HealthMailbox` (`CAJAANDE` / `technoma`):**
   - **Causa Raíz:** El servicio `MSExchangeHM` (Managed Availability) ejecuta sondas de salud cada 5 minutos desde `172.16.201.4` hacia `VMBASE8` (`172.16.201.8`).
   - **Dos Variantes del Evento:**
     - **Kerberos (`Event ID 4768`, Status `0x6`):** Usa el sufijo primario `@cajaande.gov.py` contra cuentas cuyo UPN local es `@cajaande.local`. Dispara `Internal Account Login Failure Anomaly` (por cuenta `HealthMailbox*`) e `Internal User Login Failure Anomaly` (agrupado por IP `172.16.201.4`).
     - **NTLM (`Event ID 4776`, Status `0xc0000072`):** Intenta autenticar contra 18 cuentas `HealthMailbox*` deshabilitadas en AD.
   - **Regla de Supresión Recomendada en Alert Filters:**
     - `msg_class == "Microsoft-Windows-Security-Auditing"` **AND** (`srcip_username starts with "HealthMailbox"` **OR** (`srcip == "172.16.201.4"` **AND** `event_id == 4768`)).


5. **Workflow Diario del Analista SOC Élite (21_chequeo_diario_analista_soc_elite.py):**
   - **Propósito:** Automatizar al inicio de cada turno la revisión completa del ecosistema según los cursos F00, J00 y M00 de Stellar Cyber Academy.
   - **Fases del Workflow Automatizado:**
     1. **Auditoría de Ingestión y Cuota Diaria (M02):** Verifica que el consumo cerrado del día anterior y el acumulado mensual se mantengan estrictamente bajo el límite (<8.0 GB alert / 10.0 GB cap).
     2. **Health Check de Sensores e Interflow (F02/M03):** Comprueba que los sensores (Modular Sensor, Server Sensors, Connectors) estén transmitiendo y normalizando tráfico sin retenciones por buffering.
     3. **Gestión y Triage de Casos (J03):** Consulta incidentes New, In Progress y Escalated en la cola central de Case Management.
     4. **Alineación XDR Kill Chain (J01/J02):** Desglosa los eventos en las 5 etapas del ataque (*Initial Attempts*, *Persistent Foothold*, *Exploration*, *Propagation*, *Exfiltration & Impact*), alertando ante indicios multietapa.
     5. **Auditoría Forense de Alertas & Detección Heurística de FP (J03/J04):** Cruza las alertas con alta fidelidad para discernir tráfico administrativo benigno (ej: replicación DNS de DCs, consultas LDAP 389, sincronización FSSO UDP 8002) de incidentes reales.
     6. **Top Risky Assets & Análisis de Identidades (J04):** Mapea los activos con 
isk_score > 10.0 y diagnostica su causa raíz (rotación DHCP, políticas de FW 0, anomalías analíticas).
   - **Comando de Ejecución:**
     `ash
     python auditoria_cuota_stellar/21_chequeo_diario_analista_soc_elite.py
     python auditoria_cuota_stellar/21_chequeo_diario_analista_soc_elite.py --hours 48
     `
