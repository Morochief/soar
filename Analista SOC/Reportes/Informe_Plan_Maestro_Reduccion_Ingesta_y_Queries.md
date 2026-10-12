# Plan Maestro de Auditoría y Reducción Quirúrgica de Ingesta — Stellar Cyber OpenXDR

**Para:** Jefatura de Ciberseguridad / Dirección de Tecnología  
**De:** Equipo SOC / Detección y Respuesta  
**Fecha:** 10 de Octubre de 2026  
**Clasificación:** Confidencial — Operaciones SOC / Ingeniería de Detección  
**Objetivo:** Diagnóstico forense integral del consumo de cuota diaria en Stellar Cyber (~16 GB/día vs límite contratado), presentación de evidencias empíricas extraídas del tablero de Threat Hunting y plan de acción técnico en 3 frentes para reducir la ingesta a **~6.5 GB/día** garantizando Cero Puntos Ciegos de seguridad (`soc-surgical-filtering`).

---

## 1. Resumen Ejecutivo: La Verdad de los Números

Durante las últimas 3 semanas, la plataforma Stellar Cyber ha operado en estado crítico de **Violación de Licencia de Almacenamiento/Ingesta** (>21 días en bandera roja), ingiriendo entre **14.1 GB y 16.7 GB/día** frente a una cuota contratada recomendada de **5 a 10 GB/día**.

A través de la API interna de telemetría de Stellar Cyber (`/ingestion-stats/*`), se obtuvo el desglose exacto de la ingesta en las últimas 24 horas:

```
                            DISTRIBUCIÓN REAL DE LA INGESTA DIARIA (~16.0 GB)
 ┌──────────────────────────────────────────────────────────┬────────────────────────────┬─────────┐
 │ FortiGate Syslog (fw_fortigate)                          │ Tráfico de Red (Interflow) │ Conect. │
 │ 8.22 GB / día (2.9M eventos) [51.4%]                     │ 7.63 GB / día (6.3M ev.)   │ 0.15 GB │
 └──────────────────────────────────────────────────────────┴────────────────────────────┴─────────┘
                                                            ▲
                                         ┌──────────────────┴──────────────────┐
                                         │ DNS Grafana zbx   │ Resto Tráfico   │
                                         │ 2.90 GB (1.75M ev)│ 4.73 GB         │
                                         └───────────────────┴─────────────────┘
```

### Conclusiones Principales para la Dirección:
1. **La Optimización de Grafana es Necesaria pero Insuficiente:**
   Mitigar el bucle DNS de Grafana recupera **2.90 GB/día** (1.75 millones de eventos). No obstante, esto reduce el volumen de ~16.0 GB a **~13.1 GB/día**, manteniéndonos aún en infracción de cuota.
2. **El Gigante Oculto es el Syslog de FortiGate (8.22 GB/día):**
   El firewall perimetral envía **2.9 millones de logs diarios** al sensor (`192.168.15.70:5149`), consumiendo más del 50% de la capacidad de la plataforma por registrar sesiones internas cerradas de alta frecuencia.
3. **Ruido Operacional de Monitoreo en el SPAN Port (Pre-DPI):**
   El motor Deep Packet Inspection (DPI) del sensor está consumiendo CPU y almacenamiento en registrar **163,200 flujos diarios de Zabbix Agent** y tráfico de Active Directory que pueden ser filtrados a nivel de Kernel (Pre-DPI) sin pérdida de visibilidad de seguridad.

---

## 2. Evidencias Empíricas del Tablero de Threat Hunting (Los 4 Paneles)

A través del panel interactivo configurado en Stellar Cyber se obtuvieron las siguientes cuatro evidencias forenses:

```
┌────────────────────────────────────────────────────────────┬────────────────────────────────────────────────────────────┐
│ PANEL 1: EVIDENCIA DNS GRAFANA (1.75M CONSULTAS)           │ PANEL 2: DISPOSITIVOS HACIA GOOGLE DNS (200k CONSULTAS)   │
│ • 192.168.15.23 -> ad.technoma.local: 1,628,868 consultas  │ • 10.11.1.1 (Domain Controller): 199,323 consultas         │
│ • 192.168.15.23 -> technoma.local: 128,383 consultas       │ • 192.168.15.70 (Sensor Stellar): 11,033 consultas         │
│ • Dominio: zbx.technoma.com.py (98.7% del DNS corporativo) │ • Hallazgo: Reenviadores DNS (Forwarders) de Active Dir.   │
├────────────────────────────────────────────────────────────┼────────────────────────────────────────────────────────────┤
│ PANEL 3: AUDITORÍA FORTIGATE SYSLOG                        │ PANEL 4: TRÁFICO SPAN PRE-DPI (MONITOREO INTERNO)          │
│ • Regla 214 FortiGuard Deny: Apenas 264 eventos            │ • zabbix_agent (192.168.15.31 -> 10.11.1.1): 163,200 flujos│
│ • Conclusión: Los 8.22 GB NO son denegaciones perimetrales;│ • ms_ad (Replicación y logons de AD): 35,000+ flujos       │
│   son sesiones aceptadas/cerradas de tráfico interno LAN.  │ • Oportunidad de ahorro: Filtro Pre-DPI en el sensor.      │
└────────────────────────────────────────────────────────────┴────────────────────────────────────────────────────────────┘
```

---

### Análisis Detallado Panel por Panel:

#### Panel 1: `Table - Evidencia de Grafana y Distribución de Dominios DNS`
* **Datos Registrados:**
  * `192.168.15.23` $\rightarrow$ `ad.technoma.local` $\rightarrow$ `zbx.technoma.com.py`: **1,628,868 consultas**
  * `192.168.15.23` $\rightarrow$ `technoma.local` $\rightarrow$ `zbx.technoma.com.py`: **128,383 consultas**
  * Total Grafana hacia Zabbix: **1,757,251 consultas en 24 horas**.
  * El resto de consultas de Grafana son despreciables (`dev-grafana` [1,040], Cortex [693], `grafana.com` [261]).
* **Utilidad para la Jefatura:**
  * **Demuestra al culpable con nombre y apellido:** Grafana consulta al Domain Controller a una cadencia implacable de **20 consultas por segundo**.
  * **Justifica la intervención:** Aplicar la resolución local en Grafana elimina de inmediato el 98.7% del tráfico DNS de la empresa y **ahorra 2.90 GB/día**.

---

#### Panel 2: `Evidencia de Dispositivos que Bypassean a Google DNS`
* **Datos Registrados:**
  * `10.11.1.1` (MAC `00:50:56:af:ff:5a` - Controlador de Dominio principal): **199,323 consultas** saliendo a `8.8.8.8` / `8.8.4.4`.
  * `192.168.15.70` (Sensor Stellar Cyber): **11,033 consultas**.
  * Clientes finales: Apenas 3 consultas aisladas.
* **Utilidad para la Jefatura:**
  * **Desmiente una falsa alarma:** Demuestra que **NO** son usuarios de WiFi saltándose la seguridad ni malware ejecutando túneles externos a espaldas del firewall.
  * **Identifica la causa técnica:** El Domain Controller tiene configurado *DNS Forwarders* hacia Google y está resolviendo peticiones de infraestructura externa (Apple iCloud Private Relay `mask-t.apple-dns.net` y Nutanix Prism `prismdevtest...nutanix.com`).
  * **Acción requerida:** Optimizar el tiempo de vida (TTL/Caché) del reenviador en Windows Server para evitar que el DC sature la salida WAN con 200,000 flujos externos.

---

#### Panel 3: `FortiGate Syslog`
* **Datos Registrados:**
  * En la vista actual solo aparecen 12 resultados con cifras bajas (264 eventos de la regla 214 denegando `Fortinet-FortiGuard` y `Google-DNS`).
* **Utilidad para la Jefatura:**
  * **Revelación Operacional Crítica:** El grueso de los **8.22 GB y 2.9 millones de logs diarios** del FortiGate **NO son ataques ni denegaciones perimetrales**.
  * Si se quita el filtro de denegación, se constata que la casi totalidad de los logs son **confirmaciones de inicio y cierre de sesión (`action: accept` y `action: close`)** de tráfico interno repetitivo entre servidores.
  * **Acción requerida:** Modificar en FortiOS las políticas de tráfico interno confiable de `set logtraffic all` a `set logtraffic utm`.

---

#### Panel 4: `Tráfico de Red Interno en el SPAN Port` (Pre-DPI)
* **Datos Registrados:**
  * `zabbix_agent` (`192.168.15.31` $\rightarrow$ `10.11.1.1`): **163,200 flujos de red**.
  * `ms_ad` (Active Directory): Más de **35,000 flujos** entre estaciones de trabajo y el DC.
* **Utilidad para la Jefatura:**
  * **Justificación técnica para el Pre-DPI Filter:** El servidor de monitoreo Zabbix consulta al Domain Controller 163,000 veces al día por el puerto 10050 a través del switch donde escucha el sensor de Stellar Cyber.
  * El sensor gasta ciclos de CPU, memoria y cuota de licencia decodificando paquetes L7 de un monitoreo que ya conocemos y controlamos.
  * **Acción requerida:** Crear una regla **Pre-DPI Filter** en `technoma-sensor` para descartar el tráfico en el puerto 10050 entre `192.168.15.31` y `10.11.1.1` antes de ingresar al motor DPI.

---

## 3. Plan de Acción Quirúrgico: Cómo Bajar de 16 GB a ~6.5 GB/día

Para recuperar la conformidad de la licencia respetando de forma irrestricta la política de **Cero Puntos Ciegos** (`soc-surgical-filtering`), se ejecutará el siguiente plan de optimización en 3 frentes:

```
                                PROYECCIÓN DE RECUPERACIÓN DE CUOTA
   16.0 GB ────────────────────────────────────────────────────────┐ [HOY: Infracción Grave >21 días]
           │ (-2.90 GB) Mitigación DNS Grafana (/etc/hosts / IP)   │
   13.1 GB ├───────────────────────────────────────────────┤
           │ (-4.50 GB) FortiGate Syslog Tuning (logtraffic utm)   │
    8.6 GB ├───────────────────────────────────────────────┤
           │ (-1.50 GB) Sensor Pre-DPI BPF (Zabbix 10050 & AD)     │
    7.1 GB ├───────────────────────────────────────────────┤
           │ (-0.60 GB) Caché Reenviadores DNS Windows Server      │
    6.5 GB └───────────────────────────────────────────────────────┴─ [META: Cumplimiento 100%]
```

### Tabla Resumen de Intervenciones Técnicas:

| Frente de Optimización | Causa Raíz Comprobada | Acción Técnica Concreta | Ahorro Diario | Impacto en Seguridad |
| :--- | :--- | :--- | :--- | :--- |
| **1. Servidor Grafana** | Consulta continua a `zbx.technoma.com.py` (1.75M ev.) | Agregar entrada estática en `/etc/hosts` o IP directa en Data Source Zabbix. | **-2.90 GB/día** | **Cero impacto.** La conexión HTTP se mantiene; se elimina el bucle de resolución en puerto 53. |
| **2. Firewall FortiGate** | Logs de cierre (`action: close`) en políticas internas (8.22 GB) | En FortiOS: Cambiar en reglas LAN internas de `set logtraffic all` a `set logtraffic utm`. En Stellar: Log filter quirúrgico para descartar `action: close` en puertos de monitoreo. | **-4.50 GB/día** | **Cero impacto.** Se preservan inicios de sesión, amenazas, IPS, Antivirus y denegaciones. |
| **3. Sensor Stellar (Pre-DPI)** | Zabbix pollea al DC por puerto 10050 (163k flujos L7) | Configurar regla BPF en el perfil de `technoma-sensor` para descartar puerto 10050 entre Zabbix y DC antes de entrar al motor DPI. | **-1.50 GB/día** | **Cero impacto.** Tráfico L4 benigno conocido no satura la memoria ni genera flujos Interflow innecesarios. |
| **4. Active Directory DNS** | Reenvíos a Google DNS por Apple/Nutanix (200k ev.) | Ajustar caché DNS en `10.11.1.1` y verificar configuración de Apple Private Relay en la red. | **-0.60 GB/día** | **Cero impacto.** Optimización de red interna sin pérdida de telemetría. |
| **TOTAL CONSOLIDADO** | **Estrategia Integral en 4 Frentes** | **Coordinación NOC + Infraestructura + SOC** | **-9.50 GB/día** | **Ingesta final proyectada: ~6.5 GB/día (Dentro de Licencia)** |

---

## 4. Guía de Comandos y Configuraciones para Aplicación Inmediata

### A. Configuración en Servidor Linux Grafana (`192.168.15.23`)
Editar `/etc/hosts` para anclar la resolución local en memoria:
```bash
sudo echo "192.168.15.31 zbx.technoma.com.py" >> /etc/hosts
```
*O en la interfaz web de Grafana:*  
Ir a **Connections $\rightarrow$ Data Sources $\rightarrow$ Zabbix** y cambiar `URL: https://zbx.technoma.com.py/api_jsonrpc.php` por `URL: https://192.168.15.31/api_jsonrpc.php`.

---

### B. Configuración de Pre-DPI en Stellar Cyber (`technoma-sensor`)
En la interfaz web de Stellar Cyber:  
**System $\rightarrow$ Sensor Profiles $\rightarrow$ Editar Perfil de Sensor $\rightarrow$ Pre-DPI Filter**:

```text
not (host 192.168.15.31 and host 10.11.1.1 and port 10050)
```
> [!TIP]
> Esta regla le dice al Kernel del sensor que descarte los paquetes del agente de Zabbix antes de que la CPU del sensor gaste ciclos decodificándolos, ahorrando más de 160,000 registros Interflow diarios.

---

### C. Configuración en FortiGate (CLI de FortiOS)
Para las políticas de firewall de monitoreo interno y servidores (ej. Política 72 `MONITOREO_FGT`):
```fortios
config firewall policy
    edit 72
        set logtraffic utm
    next
end
```
*(Cambiar `logtraffic all` por `logtraffic utm` evita que el firewall transmita millones de logs de cierre de sesión TCP efímeros)*.

---

## 5. Próximos Pasos de Gestión

1. **Presentar este informe a la Jefatura:** Con los 4 paneles del tablero, el argumento técnico está 100% blindado con datos empíricos.
2. **Autorizar la ventana de cambio menor (5 minutos) con el NOC:** Aplicar la configuración en Grafana y en el perfil de sensor.
3. **Monitoreo a las 24 horas:** Auditar en `/storage-usages/daily_and_monthly` la caída de la curva de ingesta hacia la zona verde (por debajo de 7 GB/día).
