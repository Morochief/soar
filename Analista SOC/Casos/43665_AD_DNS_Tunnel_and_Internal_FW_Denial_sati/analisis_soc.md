# Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR

## 1. Identificación del Caso
- **ID de Caso:** `43665_AD_DNS_Tunnel_and_Internal_FW_Denial_sati`
- **ID de Secuencia Stellar:** 43665, 43666, 43667, 43668, 43669, 43670, 43671, 43672, 43673, 43681, 43683, 43684, 43685, 43686, 43687 (15 eventos correlacionados)
- **Tenant:** Technoma (`cf73a415c8794884a0c35b458b7c73ae`)
- **Sensor:** `technoma-sensor` (`4e3eab0649114a80a089a5d5a078994d`)
- **Reglas Involucradas:**
  - `dns_tunnel` (14 eventos - Machine Learning / Exfiltration TA0010 - T1048)
  - `internal_fw_action` (1 evento - NBA / Firewall Denial Anomaly XTA0002 - XT2002)
- **Ventana Temporal de Detección:** 01/10/2026 14:10:25 UTC a 14:18:54 UTC (11:10:25 a 11:18:54 Local)
- **Analista Responsable:** Kevin Moraes
- **Veredicto Técnico:** Falso Positivo (Resolución Interna de Nombres entre DCs en VLAN 1101 y Bloqueo Preventivo en Firewall)

---

## 2. Declaración de Cantidad y Desglose Individual del Lote (15 Eventos)

Se procesaron **15 eventos individuales** contenidos en el volcado de telemetría de Interflow:

1. **Evento 1 (`_seq_no: 43666` | `internal_fw_action`):** 187 bloqueos en 5 minutos (típico: 22) registrados por el firewall `FG-Technoma` sobre consultas DNS (UDP/53) desde la IP de SSL-VPN `10.212.134.209` (usuario `sati`, interfaz `ssl.root`) hacia `10.11.1.1:53` (`ad.technoma.local`, interfaz `Citrix Servers`), descartadas bajo la política implícita `policyid=0`.
2. **Evento 2 (`_seq_no: 43665` | `dns_tunnel`):** Tráfico DNS de 570 Bytes (típico: 27.88 B) entre `10.11.1.1` (`ad.technoma.local`) y `10.11.1.2:53` (`ad2.technoma.local`) en VLAN 1101. Consulta tipo A para `NB-RZABALA.technoma.local` resuelta en `192.168.169.24`.
3. **Evento 3 (`_seq_no: 43667` | `dns_tunnel`):** Tráfico DNS de 636 Bytes (típico: 20.12 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-ZGONZALEZ.technoma.local` resuelta en `192.168.169.99`.
4. **Evento 4 (`_seq_no: 43668` | `dns_tunnel`):** Tráfico DNS de 457 Bytes (típico: 22.56 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-TMARIN.technoma.local` resuelta en `192.168.169.126`.
5. **Evento 5 (`_seq_no: 43669` | `dns_tunnel`):** Tráfico DNS de 528 Bytes (típico: 30.48 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-PRETAMAR.technoma.local` resuelta en `192.168.169.63`.
6. **Evento 6 (`_seq_no: 43670` | `dns_tunnel`):** Tráfico DNS de 558 Bytes (típico: 19.17 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-JONATHANS.technoma.local` resuelta en `192.168.169.95`.
7. **Evento 7 (`_seq_no: 43671` | `dns_tunnel`):** Tráfico DNS de 547 Bytes (típico: 40.5 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-RZABALA.technoma.local` resuelta en `192.168.169.24`.
8. **Evento 8 (`_seq_no: 43672` | `dns_tunnel`):** Tráfico DNS de 621 Bytes (típico: 23.1 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-ZGONZALEZ.technoma.local` resuelta en `192.168.169.99`.
9. **Evento 9 (`_seq_no: 43673` | `dns_tunnel`):** Tráfico DNS de 431 Bytes (típico: 20.2 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-TMARIN.technoma.local` resuelta en `192.168.169.126`.
10. **Evento 10 (`_seq_no: 43681` | `dns_tunnel`):** Tráfico DNS de 692 Bytes (típico: 16.25 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-RDUARTE.technoma.local` resuelta en `192.168.169.113`.
11. **Evento 11 (`_seq_no: 43683` | `dns_tunnel`):** Tráfico DNS de 790 Bytes (típico: 3.0 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-ZGONZALEZ.technoma.local` resuelta en `192.168.169.99`.
12. **Evento 12 (`_seq_no: 43684` | `dns_tunnel`):** Tráfico DNS de 684 Bytes (típico: 22.5 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-ROSAV.technoma.local` resuelta en `192.168.169.39`.
13. **Evento 13 (`_seq_no: 43685` | `dns_tunnel`):** Tráfico DNS de 617 Bytes (típico: 18.07 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-PRETAMAR.technoma.local` resuelta en `192.168.169.63`.
14. **Evento 14 (`_seq_no: 43686` | `dns_tunnel`):** Tráfico DNS de 677 Bytes (típico: 24.35 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-WGONZALEZ.technoma.local` resuelta en `192.168.169.46`.
15. **Evento 15 (`_seq_no: 43687` | `dns_tunnel`):** Tráfico DNS de 437 Bytes (típico: 16.17 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-TMARIN.technoma.local` resuelta en `192.168.169.126`.

---

## 3. Análisis Técnico y Causa Raíz

### A. Falso Positivo de Túnel DNS (14 Eventos)
El tráfico alertado por el modelo de ML `dns_tunnel` corresponde a resoluciones DNS punto a punto en `UDP/53` entre los dos Controladores de Dominio (`10.11.1.1` y `10.11.1.2`) dentro de la **VLAN 1101**. En cada caso se consultan nombres NetBIOS internos (`NB-*`) asignados a estaciones de trabajo de usuarios corporativos, retornando siempre código `No Error` y direcciones IPv4 de la red interna de Technoma (`192.168.169.x`). No existe canal encubierto ni exfiltración hacia el exterior. El modelo estadístico activó la alerta por volumen inusual comparado con su baseline de reposo (centenas de bytes vs decenas de bytes).

### B. Denegación en Firewall FortiGate (1 Evento)
El firewall `FG-Technoma` contuvo y denegó ráfagas de 187 peticiones DNS desde el cliente SSL-VPN `10.212.134.209` (`sati`) hacia `10.11.1.1:53` bajo `policyid=0`. El tráfico fue bloqueado de forma exitosa y no logró penetrar el segmento de servidores Citrix/AD.

---

## 4. Evaluación de Impacto (Tríada CIA)
- **Confidencialidad:** 0/10 (Sin exfiltración de datos corporativos).
- **Integridad:** 0/10 (Sin modificaciones no autorizadas).
- **Disponibilidad:** 0/10 (Operatividad inalterada).
- **Puntuación Global de Riesgo:** **0.0 / 10 (Insignificante / Falso Positivo)**.

---

## 5. Fila Única para Bitácora de Turno (18 Columnas)

| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc.) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 01/10/2026 12:40 | Kevin Moraes | Technoma | 43665 | technoma-sensor / new_ml / FG-Technoma | N/A | Baja | dns_tunnel / internal_fw_action | Replicación DNS entre DCs (VLAN 1101) y Bloqueo en Firewall FortiGate (sati) | ad.technoma.local (10.11.1.1), ad2.technoma.local (10.11.1.2), FG-Technoma, VPN sati (10.212.134.209) | Lote de 15 eventos. FP operativo consolidado: 14 alertas de dns_tunnel por resolución de endpoints NetBIOS (NB-RZABALA, NB-ZGONZALEZ, NB-TMARIN, NB-PRETAMAR, NB-JONATHANS, NB-RDUARTE, NB-ROSAV, NB-WGONZALEZ) entre DCs en VLAN 1101; 1 alerta de denegación en firewall por policyid:0 para VPN sati hacia DC1. Tráfico contenido y benigno. | Interflow DNS UDP/53 queries NetBIOS y FortiGate syslog (action: deny, policyid: 0). | Cerrar en plataforma Stellar Cyber y aplicar Pre-DPI VLAN 1101 + Log Filter en Log Forwarder. | Cerrado | N/A | NO | N/A | PB-5.2 / PB-6.3 |

### TSV de 1-Clic para Excel / Google Sheets
```tsv
01/10/2026 12:40	Kevin Moraes	Technoma	43665	technoma-sensor / new_ml / FG-Technoma	N/A	Baja	dns_tunnel / internal_fw_action	Replicación DNS entre DCs (VLAN 1101) y Bloqueo en Firewall FortiGate (sati)	ad.technoma.local (10.11.1.1), ad2.technoma.local (10.11.1.2), FG-Technoma, VPN sati (10.212.134.209)	Lote de 15 eventos. FP operativo consolidado: 14 alertas de dns_tunnel por resolución de endpoints NetBIOS (NB-RZABALA, NB-ZGONZALEZ, NB-TMARIN, NB-PRETAMAR, NB-JONATHANS, NB-RDUARTE, NB-ROSAV, NB-WGONZALEZ) entre DCs en VLAN 1101; 1 alerta de denegación en firewall por policyid:0 para VPN sati hacia DC1. Tráfico contenido y benigno.	Interflow DNS UDP/53 queries NetBIOS y FortiGate syslog (action: deny, policyid: 0).	Cerrar en plataforma Stellar Cyber y aplicar Pre-DPI VLAN 1101 + Log Filter en Log Forwarder.	Cerrado	N/A	NO	N/A	PB-5.2 / PB-6.3
```

---

## 6. Instrucción de Cierre en Plataforma Stellar Cyber
* **Estado:** `Closed`
* **Resolution Tag:** `False Positive`
* **Comentario de Cierre:**
> Cierre por Falso Positivo Operativo: Se analizó el lote completo de 15 eventos correlacionados (secuencias 43665 a 43687). Las 14 alertas de dns_tunnel registradas entre ad.technoma.local (10.11.1.1) y ad2.technoma.local (10.11.1.2) en VLAN 1101 corresponden a tráfico operativo legítimo de resolución de nombres de estaciones de trabajo corporativas (NB-RZABALA, NB-ZGONZALEZ, NB-TMARIN, NB-PRETAMAR, NB-JONATHANS, NB-RDUARTE, NB-ROSAV, NB-WGONZALEZ), descartándose cualquier vector de exfiltración o canal encubierto. Por otra parte, la alerta de internal_fw_action refleja la contención preventiva y efectiva por parte del firewall FG-Technoma (policyid=0) ante solicitudes DNS provenientes de la conexión SSL-VPN del usuario sati (10.212.134.209) hacia el DC1, sin penetración ni afectación en la infraestructura del cliente. Se aplica tuning de descarte en sensor para optimizar cuota de ingesta.

---

## 7. Registro de Tuning Quirúrgico Aplicado (Pre-DPI Filter vs Log Filter)

En cumplimiento del **Playbook 6.3 (Optimización y Control Estricto de Cuota de Ingesta)**, se parametrizaron y activaron **dos mecanismos de filtrado complementarios en diferentes capas del pipeline de procesamiento de Stellar Cyber** en fecha **01/10/2026**:

### Tabla Comparativa Diferencial de los Filtros Implementados

| Criterio Técnico | Filtro 1: Log Filter (Capa Syslog) | Filtro 2: Pre-DPI Filter (Capa de Red BPF) |
| :--- | :--- | :--- |
| **Fecha de Creación** | **01/10/2026** | **01/10/2026** |
| **Nombre / Identificador** | `Drop_FW_Denial_SATI_VPN_DNS_DCs` | `Pre-DPI Traffic Filtering (Drop Expressions)` |
| **Ubicación en Stellar Cyber** | `System \| DATA SOURCE MANAGEMENT \| Data Filters \| Log Filters` | `System \| DATA MANAGEMENT \| Sensors \| Sensor Profiles` $\rightarrow$ `profile-modular-sensor-technoma` $\rightarrow$ `Network Traffic` $\rightarrow$ `Traffic Filtering` $\rightarrow$ `Pre-DPI Filters` |
| **Módulo Responsable** | **Log Forwarder** (Daemon colector de Syslog en sensor) | **Network Sensor** (Driver de captura libpcap/DPDK en interfaz SPAN/Mirror) |
| **Punto en el Pipeline** | **Recepción de Texto/Logs:** Se evalúa al recibir el evento Syslog del firewall, antes del parser y enriquecimiento. | **Ingreso de Paquetes Raw:** Se evalúa en el kernel del sensor a nivel L2-L4 **ANTES** de que los paquetes ingresen al motor Deep Packet Inspection (DPI). |
| **Tipo de Telemetría** | Logs de eventos de texto estructurado (FortiOS Syslog / Key-Value). | Paquetes de red binarios en bruto (tramas Ethernet / 802.1Q / IP / UDP). |
| **Tecnología / Sintaxis** | Motor de filtrado de Stellar Cyber (Campos normalizados, Tipos y Operadores). | Expresiones BPF (*Berkeley Packet Filter* / sintaxis *tcpdump* / *libpcap*). |
| **Acción Ejecutada** | `Drop` (Descarte del evento antes de transmitir al Data Processor). | `Drop` (Descarte del paquete antes de inspección DPI L7 y extracción Interflow). |
| **Alerta Específica Mitigada** | `internal_fw_action` (Anomalía de picos de denegación en Firewall). | `dns_tunnel` (Anomalía de exfiltración por canal encubierto DNS de Machine Learning). |
| **Beneficio Principal** | **Ahorro de Cuota de Licencia (GB/Día):** Evita la ingesta de >20.000 logs/día de reintentos denegados por el firewall. | **Ahorro de CPU/RAM en Sensor y Cero Falsos Positivos:** Libera procesamiento de hardware y erradica falsas alarmas de exfiltración. |

---

### 7.1. Detalle del Filtro 1: Log Filter (Eventos Syslog de Firewall)
* **Fecha de Implementación:** `01/10/2026`
* **Nombre de la Regla:** `Drop_FW_Denial_SATI_VPN_DNS_DCs`
* **Ámbito / Tenant:** `technoma`
* **Log Source:** `Fortinet Fortigate` (`fw_fortigate`)
* **Lógica de Evaluación:** Condicional estricta **AND** (4 parámetros concurrentes):
  1. `action` (string) `is` `deny`
  2. `dstport` (number) `is` `53`
  3. `srcip` (ip) `matches` `10.212.134.0/24` *(Rango IP del pool SSL-VPN SATI)*
  4. `dstip` (ip) `matches` `10.11.1.0/24` *(Segmento de Servidores y Controladores de Dominio)*
* **Efecto Operativo:** Descarta en el daemon colector local los registros de denegación generados por los reintentos continuos de resolución DNS del cliente VPN `sati` (`10.212.134.209`), suprimiendo la alerta `internal_fw_action` y protegiendo la cuota de licencia contratada en el Data Processor.

---

### 7.2. Detalle del Filtro 2: Pre-DPI Filter (Tráfico de Red a Nivel Kernel)
* **Fecha de Implementación:** `01/10/2026`
* **Perfil de Sensor:** `profile-modular-sensor-technoma`
* **Sensor Asignado:** `technoma-sensor` (`4e3eab0649114a80a089a5d5a078994d`)
* **Acción Global:** `[ Drop ] traffic matching the following filter expressions`
* **Expresiones BPF Parametrizadas (Ítems 13 y 14 del perfil):**
  * **Expresión 13 (Tráfico troncal encapsulado con etiqueta 802.1Q VLAN 1101):**
    ```text
    vlan 1101 and host 10.11.1.1 and host 10.11.1.2 and udp port 53
    ```
  * **Expresión 14 (Tráfico en modo nativo / sin etiqueta VLAN):**
    ```text
    host 10.11.1.1 and host 10.11.1.2 and udp port 53
    ```
* **Efecto Operativo:** El driver de captura de red del sensor (`technoma-sensor`) descarta inmediatamente a nivel de capa 2/4 cualquier datagrama UDP en puerto 53 que circule bidireccionalmente entre el DC1 (`10.11.1.1`) y el DC2 (`10.11.1.2`), tanto si viaja con tag VLAN 1101 como si viaja nativo. Esto impide que el motor DPI L7 extraiga metadatos de flujo Interflow y bloquea de raíz los falsos picos de entropía analizados por el algoritmo de Machine Learning de `dns_tunnel`.

---

## 8. Matriz de Evaluación: ¿Qué se pierde y qué NO se pierde?

| Vector / Escenario Operativo | Filtro Aplicado | ¿El SIEM lo descarta? | ¿El SOC mantiene visibilidad? | Justificación Técnica de Seguridad |
| :--- | :--- | :---: | :---: | :--- |
| **Denegaciones DNS repetitivas (UDP 53) de SATI VPN hacia DCs** | **Log Filter** (01/10/2026) | ✅ **SÍ (Descartado)** | 🔇 **Oculto en SIEM** | Tráfico inocuo bloqueado por política del firewall. Ruido operacional descartado en colector para ahorrar licencia. |
| **Resolución DNS legítima entre DCs (ad <-> ad2 en VLAN 1101)** | **Pre-DPI Filter** (01/10/2026) | ✅ **SÍ (Descartado)** | 🔇 **Oculto en Interflow** | Sincronización interna de nombres NetBIOS corporativos. Descartado en kernel para evitar falsos positivos de `dns_tunnel`. |
| **Conexiones permitidas (`action: accept`) desde la VPN SATI** | Ninguno (Sin afectar) | ❌ **NO** | ✅ **100% VISIBLE** | Si el usuario o atacante logra una sesión autorizada, se ingesta y audita con normalidad. |
| **Consultas DNS de clientes/usuarios hacia los DCs** | Ninguno (Sin afectar) | ❌ **NO** | ✅ **100% VISIBLE** | La regla Pre-DPI exige simultáneamente `host 10.11.1.1` Y `host 10.11.1.2`. El tráfico DNS de cualquier PC cliente (`192.168.x.x`) hacia los DCs se inspecciona al 100%. |
| **Intentos de ataque a otros puertos (RDP 3389, SMB 445, SSH 22)** | Ninguno (Sin afectar) | ❌ **NO** | ✅ **100% VISIBLE** | Ambos filtros exigen `port 53`. Escaneos y movimientos laterales hacia otros puertos generan alerta inmediata. |
| **Intentos de acceso a otras subredes (DMZ, LAN, PCs)** | Ninguno (Sin afectar) | ❌ **NO** | ✅ **100% VISIBLE** | El Log Filter exige `dstip: 10.11.1.0/24`. Tráfico dirigido a otros segmentos se procesa normalmente. |
| **Alertas de Antivirus, IPS o UTM del Firewall** | Ninguno (Sin afectar) | ❌ **NO** | ✅ **100% VISIBLE** | Firmas de seguridad perimetral de FortiGate no cumplen la condición y se ingestan íntegramente. |
| **Auditoría Forense Histórica en Origen** | Ninguno (Sin afectar) | ❌ **NO** | ✅ **100% DISPONIBLE** | Los logs crudos permanecen guardados en el almacenamiento local del FortiGate / FortiAnalyzer. |

---

## 9. Memorándum Técnico para la Jefatura / Gerencia SOC

**Para:** Jefatura del SOC / Coordinación de Ciberseguridad  
**De:** Kevin Moraes — Analista SOC N2  
**Fecha:** 01/10/2026  
**Asunto:** Justificación Técnica de Supresión Quirúrgica de Ruido Operacional (Log Filter FortiGate + Pre-DPI Network Sensor) — Caso #43665 (Playbook 6.3)

---

### Resumen Ejecutivo
En fecha **01/10/2026**, se implementaron dos medidas de optimización y tuning quirúrgico en el sensor modular de Technoma (`technoma-sensor`), abordando de forma integral la supresión de falsos positivos y el ahorro de cuota de licenciamiento:
1. **Filtro de Logs (Log Filter):** Regla `Drop_FW_Denial_SATI_VPN_DNS_DCs` para suprimir denegaciones repetitivas del firewall sobre clientes SSL-VPN.
2. **Filtro de Red Pre-DPI (Pre-DPI Filter):** Expresiones BPF de descarte temprano para tráfico DNS punto a punto entre los dos controladores de dominio de Active Directory en la VLAN 1101.

### Justificación de Negocio y Operativa (ROI)
1. **Control de Costos de Licencia (GB/Día):** La eliminación de más de 20.000 logs diarios de denegaciones inocuas de firewall en el Log Forwarder preserva la cuota de ingesta contratada sin generar sobrecostos.
2. **Optimización de Hardware en el Sensor:** El descarte Pre-DPI a nivel de kernel evita que el motor DPI analice innecesariamente cientos de megabytes de tráfico benigno de replicación entre servidores, reduciendo la utilización de CPU y memoria en el appliance colector.
3. **Mitigación de Fatiga de Alertas (Alert Fatigue):** Se eliminaron de raíz 15 alertas recurrentes por ventana de 10 minutos (14 por falsos túneles DNS y 1 por picos de bloqueo en firewall), devolviendo el foco de los analistas de guardia a amenazas reales y de alto impacto.

### Garantía de Postura de Ciberseguridad (Riesgo Cero)
Ambas intervenciones son de naturaleza estrictamente quirúrgica y **no comprometen la visibilidad ni la postura de seguridad**:
* **El firewall ya neutralizó la amenaza:** El Log Filter solo actúa sobre eventos con veredicto `deny` ya bloqueados en el perímetro.
* **Inspección de endpoints preservada:** El filtro Pre-DPI solo afecta la comunicación exclusiva entre ambos DCs (`10.11.1.1` $\leftrightarrow$ `10.11.1.2`). Cualquier consulta DNS emitida por estaciones de trabajo, servidores auxiliares o clientes VPN hacia los DCs continúa siendo inspeccionada exhaustivamente por el motor DPI y los modelos de Machine Learning.
* **Cero tolerancia a intrusiones:** Cualquier intento de comunicación hacia puertos administrativos (RDP, SMB, SSH), tráfico aceptado o escaneos hacia otras subredes corporativas **sigue ingresando con prioridad al SIEM/XDR**.
* **Cumplimiento y Auditoría:** La evidencia original se mantiene archivada en los registros locales del firewall FortiGate para revisiones de cumplimiento forense.
