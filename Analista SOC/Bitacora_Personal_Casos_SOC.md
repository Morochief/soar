# 🛡️ Bitácora Personal de Casos e Investigaciones — Analista SOC
**Analista:** Kevin Moraes  
**Rol:** Operador / Analista SOC — Technoma Security Operations Center  
**Propósito:** Cuaderno técnico de triaje, decisiones forenses y justificaciones de resolución para consulta rápida ante jefatura, clientes y auditorías.

---

## 📌 Índice Maestro de Casos Analizados

| # | ID / Caso | Fecha | Plataforma | Host / Activo | Usuario | Alerta / Incidente | Veredicto | Playbook | Enlace |
| :-: | :--- | :---: | :--- | :--- | :--- | :--- | :---: | :---: | :-: |
| **001** | `#147399` | 02/10/2026 | Cortex XDR | `NB-CHIDALGO` | `carloshidalgo` | Rare binary to rare cloud resource | **Falso Positivo (BTP)** | `PB-5.6 / PB-2.2` | [Ver Ficha ➔](#caso-147399---conexión-de-librewolf-a-bucket-s3-carlos-hidalgo) |
| **002** | `ST-ANYDESK-01` | 03/10/2026 | Stellar Cyber | `ad.technoma.local` / `ad2` | `Red Interna` | Exploit C&C Connection / AnyDesk DNS Spikes | **Falso Positivo (BTP)** | `PB-2.2: Monitoreo Operativo` | [Ver Ficha ➔](#caso-002---anomalías-de-exploit-y-cc-por-consultas-dns-de-anydesk-stellar-cyber) |
| **003** | `ST-SOPHOS-01` | 04/10/2026 | Stellar Cyber / Sophos | `VM-MARANDU` | `Sistema (Sophos)` | Sophos Event: Impair Defenses (Update Failure) | **Falso Positivo (Ruido Operativo)** | `PB-2.2: Monitoreo Operativo` | [Ver Ficha ➔](#caso-003---falsa-alarma-de-impair-defenses-por-falla-de-actualización-de-sophos-vm-marandu) |
| **004** | `ST-FW-DNS-01` | 03/10/2026 | Stellar Cyber / FortiGate | `nb-amorinigo` | `angelramos (VPN)` | FW Policy Anomaly (UPAY) & DNS New TLD (.social) | **Falso Positivo (BTP)** | `PB-2.2: Monitoreo Operativo` | [Ver Ficha ➔](#caso-004---anomalía-de-política-firewall-vpn-to-p5-upay-y-dns-cyberplacesocial-nb-amorinigo) |
| **005** | `ST-SENSOR-CAJAANDE` | 04/10/2026 | Stellar Cyber / Red | `Sensor-Modular-CajaAnde` / `VMBASE8` | `Infraestructura` | Caída de Sensor de Red y Agente (Corte de Fibra) | **Incidente Resuelto (Disponibilidad)** | `FL-THN-POS-01 / NOC` | [Ver Ficha ➔](#caso-005---caída-de-sensor-de-red-y-agente-por-corte-de-fibra-caja-ande) |
| **006** | `#148379` | 07/10/2026 | Cortex XDR | `NB-FMORA` | `fabiomora` | Suspicious runonce.exe parent process | **Falso Positivo (BTP)** | `PB-2.2 / PB-4.1` | [Ver Ficha ➔](#caso-148379) |
| **007** | `#148359` | 07/10/2026 | Cortex XDR | `NB-JTORALES` | `josetorales` | PowerShell runs suspicious base64-encoded commands | **Falso Positivo (BTP)** | `PB-2.2: Monitoreo Operativo` | [Ver Ficha ➔](#caso-148359) |
| **008** | `#148460` | 07/10/2026 | Cortex XDR | `NB-GREYES` | `gustavoreyes` | Scripting engine connected to a rare external host | **Falso Positivo (BTP)** | `PB-5.6 / PB-2.2` | [Ver Ficha ➔](#caso-148460) |
| **009** | `#148343` | 06/10/2026 | Cortex XDR | `NB-JTORALES` | `josetorales` | PowerShell runs suspicious base64-encoded commands | **Falso Positivo (BTP)** | `PB-2.2: Monitoreo Operativo` | [Ver Ficha ➔](#caso-148343) |
| **010** | `#148341` | 06/10/2026 | Cortex XDR | `NB-JTORALES` | `josetorales` | PowerShell runs suspicious base64-encoded commands | **Falso Positivo (BTP)** | `PB-2.2: Monitoreo Operativo` | [Ver Ficha ➔](#caso-148341) |
| **011** | `#148309` | 06/10/2026 | Cortex XDR | `NB-JTORALES` | `josetorales` | PowerShell runs suspicious base64-encoded commands | **Falso Positivo (BTP)** | `PB-2.2: Monitoreo Operativo` | [Ver Ficha ➔](#caso-148309) |
| **012** | `ST-DNS-TUNNEL-01` | 07/10/2026 | Stellar Cyber | `ad.technoma.local` / `ad2` | `Active Directory / Red` | DNS Tunneling Anomaly (Lote de 8 alertas entre DCs) | **Falso Positivo (BTP)** | `PB-2.2: Monitoreo Operativo` | [Ver Ficha ➔](#caso-st-dns-tunnel-01) |
| **013** | `ST-DNS-TUNNEL-02` | 07/10/2026 | Stellar Cyber | `ad.technoma.local` / `ad2` | `Active Directory / Red` | DNS Tunneling Anomaly (Lote 2 - 14 alertas entre DCs) | **Falso Positivo (BTP)** | `PB-2.2: Monitoreo Operativo` | [Ver Ficha ➔](#caso-st-dns-tunnel-02) |
| **014** | `ST-SMB-CAJAANDE` | 09/10/2026 | Windows Server / Live Response | `VMBASE03` + 5 Clientes | `CAJAANDE` | Falso Borrado y Bloqueo SMB de Ejecutables (MODULO_TESORERIA) | **Falso Positivo (Incidente Operacional SMB)** | `PB-2.2 / Forense SMB` | [Ver Ficha ➔](#caso-st-smb-cajaande) |
| **015** | `THN-ABUSE-BATCH-01` | 09/10/2026 | Stellar Cyber / FortiGate | DMZ Servers (`190.104.178.146`) | Externo / WAN | Notificación de Abuso a Cloudflare por 5 IPs Atacantes | **True Positive - Blocked (Notificado)** | `Playbook Escaneo y Fuerza Bruta` | [Ver Ficha ➔](#caso-thn-abuse-batch-01) |
| **016-A** | `SAC-2026-1007` | 07/10/2026 | Stellar Cyber (SAC) | Servidor DMZ DigitalCert (`190.104.178.146`) | WAN / Atacantes | Regla de Detección Automatizada: THN FW Ataque Recurrente a DMZ | **Regla Automatizada Desplegada** | `Playbook Escaneo y Fuerza Bruta` | [Ver Ficha ➔](#caso-sac-2026-1007) |
| **016-B** | `GOV-2026-1011` | 11/10/2026 | Stellar Cyber / FortiGate | Cámaras Dahua CCTV (`192.168.16.16`) | Red Interna / CCTV | Creación de Log Filter Quirúrgico DHCP Dahua (Saturación de Cuota) | **Regla Quirúrgica Creada (0% Ceguera)** | `Playbook 6.3 - Log Filtering` | [Ver Ficha ➔](#caso-gov-2026-1011) |
| **016-C** | `GOV-2026-1012` | 11/10/2026 | Stellar Cyber / FortiGate | Servidor Zabbix (`192.168.15.31`) | Red Interna / Agentes | Detección de Ruido Zabbix Agent Polling (TCP 10050) & DNS | **En Seguimiento (Pendiente Validación Jefatura)** | `PB-2.2: Monitoreo Operativo` | [Ver Ficha ➔](#caso-gov-2026-1012) |
| **016-D** | `GOV-2026-1013` | 11/10/2026 | Stellar Cyber / FortiGate | Endpoints VLANs 169 y 100 | Red Interna / P2P | Remediación Quirúrgica WUDO Puerto 7680 (5 Dimensiones) | **Punto Ciego Eliminado (100% Visibilidad)** | `PB-2.2: Monitoreo Operativo` | [Ver Ficha ➔](#caso-gov-2026-1013) |
| **016** | `THN-AUDIT-FILTERS-01` | 14/10/2026 | Stellar Cyber / OpenXDR | `technoma-sensor` / `10.11.1.2` | `Red Interna / WUDO / CCTV` | Auditoría Técnica de Log Filters: Corrección de Reglas Inoperativas (WUDO 7680 & Dahua CCTV) | **Tuning Quirúrgico L7 / Mitigación** | `Playbook 6.3 - Log Filtering` | [Ver Ficha ➔](#caso-016---auditoría-de-log-filters-reglas-inoperativas-wudo-7680-y-dahua-cctv) |
| **017** | `THN-INGEST-GRAFANA-01` | 14/10/2026 | Stellar Cyber / NDR | `technoma-sensor` / `192.168.15.23` | `NOC / Grafana` | Contención Definitiva de Cuota: Pre-DPI BPF Saneado contra Flood DNS de Grafana | **Resolución Técnica / Rescate de Cuota** | `Playbook 6.3 - Ingestion Control` | [Ver Ficha ➔](#caso-017---contención-de-cuota-stellar-pre-dpi-bpf-contra-flood-dns-de-grafana) |
| **018** | `32592` | 15/10/2026 | Stellar Cyber / Windows Agent | `VMBASE8` (`172.16.201.8`) | `Ktroche` | Sensitive Windows Network Share (protected_storage DPAPI) | **Falso Positivo (BTP)** | `PB-5.2 / PB-1.1` | [Ver Ficha ➔](#caso-018---acceso-legítimo-a-protected_storage-en-vmbase8-windows-dpapi) |
| **019** | `CORTEX-FMORA-01` | 15/10/2026 | Cortex XDR / Magnifier | `NB-FMORA` | `fabiomora` | Carga masiva de 10.2 GB a Proton Drive (Shadow IT / Riesgo DLP) | **Uso No Autorizado / Sin Fuga** | `PB-2.2 / DLP` | [Ver Ficha ➔](#caso-019---investigación-forense-cortex-xdr-carga-a-proton-drive-nb-fmora) |
| **020** | `THN-LOGFILT-WIFI` | 15/10/2026 | Stellar Cyber / FortiGate | Subred WiFi (`192.168.169.x`) | Red WiFi | Log Filters Quirúrgicos contra Denegaciones Masivas WiFi (Casos #16302 y #12661) | **Tuning de Cuota / Mitigación** | `Playbook 6.3 - Log Filtering` | [Ver Ficha ➔](#caso-020---optimización-de-cuota-stellar-cyber-log-filter-quirúrgico-fortigate-wifi) |
| **021** | `THN-SOC-102` | 15/10/2026 | Stellar Cyber / AD | `192.168.15.27` (`Zabbix`) | `Mario Flores (Baja)` | Cierre Incidente: Autenticación LDAP Texto Claro 389 y Automatización FL-THN-POS-01 | **Incidente Resuelto / Remediado** | `FL-THN-POS-01 / RFA NOC` | [Ver Ficha ➔](#caso-021---cierre-de-incidente-thn-soc-102-zabbix-ldap-mario-flores-y-estandarización-fl-thn-pos-01) |
| **022** | `ST-BATCH-OCT15` | 15/10/2026 | Stellar Cyber / Interflow | `10.11.1.1`, `NB-ICENTURION`, `192.168.169.78` | `ivancenturion` / Red | Lote 10 Alertas IDS INFO (GitHub, AnyDesk, NTLM, Telegram) y Falsa Correlación C&C LDAP | **Falso Positivo (BTP)** | `PB-3.1 / PB-2.2` | [Ver Ficha ➔](#caso-022---falso-positivo-lote-interflow-firmas-ids-info-y-falsa-correlación-cc-ldap) |
| **023** | `ST-GSUITE-MARIN` | 15/10/2026 | Google Workspace / Stellar | Google Drive | `josemarin` | Falsa Alarma UBA Exfiltración Google Drive: Sincronización AppSheet y AppScript | **Falso Positivo (BTP)** | `PB-6.1 / UBA Cloud` | [Ver Ficha ➔](#caso-023---falso-positivo-uba-cloud-sincronización-google-appsheet--appscript-josé-marín) |
| **024** | `ST-INGEST-PASSTHROUGH` | 15/10/2026 | Stellar Cyber / Modular Sensor | `profile-modular-sensor-technoma` | Red Interna / WAN | Optimización Quirúrgica de Ingesta: Filtro de Descarte Passthrough Benigno FortiGate | **Tuning Quirúrgico / DROP** | `Playbook 6.3 - Log Filtering` | [Ver Ficha ➔](#caso-024---optimización-quirúrgica-de-ingesta-filtro-de-descarte-passthrough-benigno-fortigate) |
| **025** | `INCIDENT-541` | 15/10/2026 | Cortex XDR / Stellar Cyber | `NB-JTORALES` | `josetorales` | Trazabilidad y Conciliación de Auditoría: Incidente Cortex XDR 541 & Caso #17797 | **Falso Positivo (Resolved - Auto)** | `PB-2.2 / T1018` | [Ver Ficha ➔](#caso-025---trazabilidad-y-conciliación-de-auditoría-incidente-cortex-xdr-541-failed-connections---nb-jtorales) |

---

## 📊 Control Diario de Ingesta y Capacidad de Licencias (Stellar Cyber Pool)

> 💡 **Buena Práctica Operativa:** Registrar la telemetría de consumo al cierre de turno para respaldo documental inmediato ante reclamos de jefatura. Si un tenant supera su cuota o el pozo global supera los 10.0 GB/día, queda constancia fehaciente en la bitácora oficial.

| Fecha | Turno | Pozo Global (Consumo / Límite) | Technoma (Límite: 8 GB) | CAJA ANDE (Límite: 5 GB) | Valores (Límite: 1 GB) | Estado del Pozo | Novedad / Deslinde Operativo |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **03/10/2026** | Mañana (06:00 - 14:00) | **14.80 GB** / 10.0 GB (148.0%)<br>*(Pico: 17.05 GB — 170.5%)* | **14.77 GB** ⚠️<br>*(Excedido +6.77 GB / 184%)* | 0.03 GB ✅<br>*(0.6% nominal)* | 0.00 GB ✅<br>*(Sin ingesta)* | 🔴 **POZO DESBORDADO** | **Alerta Crítica de Licencia:** Technoma desbordó su cuota asignada e hiperconsumió el pozo dinámico debido a alto volumen de logs perimetrales/Interflow (330 GB acumulados en el mes). Registrado formalmente en reporte oficial de turno. |
| **04/10/2026** | Mañana (06:00 - 14:00) | **8.69 GB** / 10.0 GB (86.9%)<br>*(Pico: 17.05 GB)* | **8.61 GB** ⚠️<br>*(Leve exceso +0.61 GB / 107%)* | 0.07 GB ✅<br>*(1.4% nominal)* | 0.00 GB ✅<br>*(Sin ingesta)* | 🟢 **Pozo Normal (86.9%)** | **Consumo Nominal:** Pozo global operando dentro del contrato. Technoma con leve exceso habitual (~8.6 GB). Se auditó regla 'Ingestion threshold exceeded' con umbral residual erróneo en 20 MB (0.02 GB). |
| **10/10/2026** | Guardia Sábado (Home Office) | **14.27 GB** / 10.0 GB (142.7%)<br>*(Prom: 14.23 GB)* | **14.23 GB** ⚠️<br>*(99.53% del Clúster)* | 0.04 GB ✅<br>*(0.47% nominal)* | 0.00 GB ✅<br>*(Sin ingesta)* | 🔴 **POZO DESBORDADO** | **Auditoría Forense de Ingesta:** Se aisló la causa raíz de saturación en Syslog de FortiGate (8.22 GB/d, 2.9M eventos) y bucle DNS de Grafana hacia zbx (2.90 GB/d, 1.75M consultas). Emitidos informes ejecutivos y plan maestro para descender a ~6.5 GB/día. |
| **11/10/2026** | Guardia Domingo (Home Office) | **8.60 GB** / 10.0 GB (86.0%) | **8.55 GB** ⚠️<br>*(En rango habitual)* | 0.05 GB ✅<br>*(1.0% nominal)* | 0.00 GB ✅<br>*(Sin ingesta)* | 🟢 **Pozo Normal (86.0%)** | **Consumo Controlado & Remediación:** Filtros Dahua (DHCP) y WUDO 7680 corregidos a 5 dimensiones (0% ceguera). Ruido Zabbix 10050 detectado y puesto en seguimiento formal. |
| **14/10/2026** | Mañana (06:00 - 14:00) | **17.05 GB** / 10.0 GB (170.5%)<br>*(Pico Máximo Registrado)* | **17.01 GB** ⚠️<br>*(Excedido +9.01 GB / 212%)* | 0.04 GB ✅<br>*(0.8% nominal)* | 0.00 GB ✅<br>*(Sin ingesta)* | 🔴 **POZO DESBORDADO** | **Alerta Crítica de Licencia & Tuning:** Technoma desbordó cuota por ráfagas de denegaciones firewall (Dahua CCTV e inter-VLAN). Se ejecutó auditoría técnica sobre 67 Log Filters descartando ceguera en Helpdesk y diseñando filtro L7 para Dahua (Playbook 6.3). |
| **15/10/2026** | Tarde (14:00 - 20:00) | **12.40 GB** / 10.0 GB (124.0%)<br>*(Tendencia a la Baja)* | **12.35 GB** ⚠️<br>*(En descenso post-tuning)* | 0.05 GB ✅<br>*(1.0% nominal)* | 0.00 GB ✅<br>*(Sin ingesta)* | 🟡 **Contención Operativa** | **Tuning Quirúrgico de Log Filters:** Despliegue de filtros API `Drop_FW_Passthrough_Benign_Telemetry`, `Drop_FW_PaloAlto_Traps_Heartbeats` y `Drop_FW_Windows_Diagnostics_Telemetry`. Purga de telemetría passthrough benigna redundante (~170.000 logs/día ahorrados). Conciliación de Incidente Cortex XDR 541 / Caso #17797. |

---

## 📂 Registro Detallado de Casos

---

### Caso #147399 - Conexión de LibreWolf a Bucket S3 (Carlos Hidalgo)

* **Fecha/Hora:** `02/10/2026 23:42:04` (Hora Local GMT-3) / `2026-10-03 03:42:04 UTC`
* **Plataforma:** Palo Alto Networks Cortex XDR (EDR Agent v9.3.0.231)
* **Motor:** `ANALYTICS_BIOC` | **Severidad:** `Low` (1) | **Acción:** `DETECTED`
* **Activo Afectado:** `NB-CHIDALGO` (`192.168.100.7` / Windows 11 Pro Build 26200)
* **Usuario:** `TECHNOMA\carloshidalgo`
* **Táctica / Técnica MITRE:** `TA0011 - Command and Control` / `T1071.001 - Application Layer Protocol: Web Protocols`
* **Playbook Aplicado:** `PB-5.6: Comunicación C2` / `PB-2.2: Monitoreo Operativo`
* **Veredicto Final:** **Benign True Positive (BTP) / Falso Positivo Heurístico**

#### 1. ¿Por qué chilló la consola? (La hipótesis inicial)
El motor de comportamiento de Cortex XDR (`ANALYTICS_BIOC`) disparó la regla de Comando y Control *«Rare binary connected to a rare cloud resource»*. La alerta se activó porque el proceso `librewolf.exe` era un ejecutable nunca antes visto en la organización en los últimos 30 días (`seen on 0 hosts and across 0 unique days`), marcado internamente como no firmado (`Signature: Unsigned`), y estableció conexión cifrada con un host en la nube jamás contactado por la empresa (`infinitysport.s3.amazonaws.com`).

#### 2. Evidencias Clave y Disección Forense
* **Identificación del Binario:**
  * Ruta: `C:\Program Files\WindowsApps\31856maltejur.LibreWolf_157.0.100.0_x64__ssmwz6s360tct\VFS\ProgramFiles\LibreWolf Package Root\librewolf.exe`
  * Origen: Paquete oficial empaquetado por *Malte Jurleit* instalado legalmente desde la **Microsoft Store**.
  * SHA-256: `235de8dc6bc6a8ccd45c496c3fada424f88003d1816661cb3f05848a6a0a8ad1`
  * MD5: `f4d00f5200a7ad794cf9118f7c0bf1a5`
  * **WildFire Score:** **`Benign`** (Binario limpio verificado por la inteligencia de Palo Alto Networks).
* **Árbol de Ejecución de Procesos:**
  * `explorer.exe` (PID 12088) ➔ `librewolf.exe` (PID 26428, lanzamiento interactivo a las 20:48:38).
  * Arquitectura Gecko multiproceso normal (PIDs 2164, 31312) ➔ Pestaña de navegación activa (PID 12728).
* **Comportamiento del Flujo de Red:**
  * Destino: `16.12.1.81:443` (`infinitysport.s3.amazonaws.com` en AWS São Paulo, Brasil).
  * Duración de la sesión: **29 segundos** (`Session Status: SUCCESS`).
  * Tráfico transferido: **Descarga 1.21 MB** vs **Subida 15 KB** (relación típica de descarga de recursos web; sin exfiltración de información ni beaconing de C2).

#### 3. ¿Qué era en realidad? (Causa Raíz)
Navegación web legítima del usuario a la tienda deportiva y de calzado **Infinity Sport** utilizando el navegador de privacidad **LibreWolf** (fork de Firefox) descargado desde la tienda oficial de Windows. Los recursos gráficos del sitio web están alojados en un bucket público de Amazon S3, lo que disparó la alarma de host raro.

#### 4. Justificación Técnica de Cierre (Cortex XDR)
> *"Cerrado como Falso Positivo / BTP. El proceso librewolf.exe (SHA256: 235de8dc...) corresponde al navegador LibreWolf instalado vía Microsoft Store por el usuario carloshidalgo en NB-CHIDALGO (WildFire: Benign). La conexión a infinitysport.s3.amazonaws.com (16.12.1.81:443) consistió en la descarga de 1.21 MB de recursos web de e-commerce durante 29 segundos de navegación interactiva, descartándose patrones de exfiltración de datos, balizamiento o comando y control. No se requieren acciones de contención."*

#### 5. Acciones y Seguimiento
* [x] **Cortex XDR:** Caso cerrado como `False Positive` / `Resolved - Known Behavior`.
* [x] **Bitácora Oficial:** Fila TSV registrada con fecha 02/10/2026.
* [ ] **Control de Políticas (Opcional):** Si Technoma prohíbe el uso de navegadores no corporativos (distintos a Edge/Chrome), notificar a Helpdesk para evaluar desinstalación o bloqueo de descargas desde Microsoft Store mediante GPO.

---

### Caso #002 - Anomalías de Exploit y C&C por Consultas DNS de AnyDesk (Stellar Cyber)

* **Fecha/Hora:** `03/10/2026 15:28:41` (Hora Local GMT-3) / `2026-10-03 14:51:18 - 15:28:41 UTC`
* **Plataforma:** Stellar Cyber OpenXDR v7.0.0s (Interflow IDS / ML Engine)
* **Motor:** `aella_flow`, `maltrace`, `new_ml` | **Severidad:** `Medium` (Puntajes 28 a 47) | **Tenant:** `Technoma`
* **Activos Afectados:**
  * `ad.technoma.local` (`10.11.1.1` - Controlador de Dominio / DNS Primario)
  * `ad2.technoma.local` (`10.11.1.2` - DNS Secundario / Controlador de Dominio)
  * Endpoint interno en VLAN 1101 (`192.168.169.100`)
* **Eventos Disparados en Lote:**
  * `exploit_attempt_correlation` (Exploited C&C Connection / MITRE XT2014)
  * `exploit_attempt_priv_priv` (Private to Private Exploit Anomaly / MITRE T1210)
  * `exploit_attempt_priv_pub` (Private to Public Exploit Anomaly / MITRE T1190)
* **Playbook Aplicado:** `PB-2.2: Monitoreo Operativo` (y descarte formal de `PB-5.6: Comunicación C2`)
* **Veredicto Final:** **Benign True Positive (BTP) / Falso Positivo Operacional (Ruido de IDS Heurístico)**

#### 1. ¿Por qué chilló la consola? (La hipótesis inicial)
Stellar Cyber correlacionó un lote de 4 eventos y disparó una alerta de severidad media alegando que *"un host explotado internamente estableció conexión de Comando y Control (C&C) hacia un atacante"*. Esto se debió a que el sensor IDS detectó picos (*spikes*) de consultas DNS (19, 21 y 28 consultas en ventanas de 5 min) que activaron las firmas informativas `INFO Anydesk Domain in DNS Lookup` (SID 2060512) y `INFO Anydesk Relay Domain in DNS Lookup` (SID 2060507), sumado a un paquete efímero UDP puerto 8002 entre ambos controladores de dominio. El motor de Machine Learning infló la severidad acumulada clasificándolo como un intento de explotación y propagación lateral.

#### 2. Evidencias Clave y Disección Forense
* **Dominios Solicitados:**
  * `boot.net.anydesk.com` (Lookup A inicial)
  * `boot-relays.net.anydesk.com` (Lookup AAAA IPv6)
  * `relay-8a3338e6.net.anydesk.com` (Lookup A resuelto legítimamente a `162.43.190.123`)
* **Flujos de Red Analizados:**
  1. `192.168.169.100:55675` ➔ `10.11.1.1:53` (Endpoint interno en VLAN 1101 consultando a su DNS local).
  2. `10.11.1.1` ➔ `10.11.1.2:53` (Reenvío recursivo de DNS entre controladores de dominio).
  3. `10.11.1.1` ➔ `8.8.8.8:53` / `8.8.4.4:53` (Resolución pública hacia forwarders de Google).
  4. `10.11.1.2:53719` ➔ `10.11.1.1:8002` (Tráfico UDP aislado de 77 bytes de sincronización/comunicación interna).
* **Naturaleza de las Firmas IDS:**
  * Reglas de Emerging Threats: Categoría `Misc activity`, severidad `Informational` (`classtype:misc-activity`, `severity: low`). No son firmas de exploits ni de malware; son firmas de telemetría pensadas únicamente para registrar presencia de herramientas de acceso remoto (RAT/Remote Support).

#### 3. ¿Qué era en realidad? (Causa Raíz)
Tráfico normal, autorizado y legítimo del software de soporte remoto **AnyDesk** utilizado en la infraestructura de Technoma. Al iniciarse o reconectarse sesiones de soporte, AnyDesk consulta sus servidores centrales de arranque (*boot servers*) y relays de balanceo de carga para establecer la sesión. El motor ML de Stellar Cyber malinterpretó el volumen concentrado de consultas de arranque como un "ataque de explotación".

#### 4. Justificación Técnica de Cierre (Stellar Cyber)
> *"El caso corresponde a un falso positivo derivado de la activación de firmas informativas de IDS (ET INFO AnyDesk Domain / Relay Lookup, SIDs 2060512 y 2060507) ante resoluciones DNS legítimas de la herramienta de soporte remoto AnyDesk (boot.net.anydesk.com y relay-8a3338e6.net.anydesk.com) realizadas por el host 192.168.169.100 y reenviadas recursivamente por los controladores de dominio ad.technoma.local (10.11.1.1) y ad2.technoma.local (10.11.1.2) hacia forwarders de Google. La correlación del motor ML con 'Exploited C&C' obedece a un pico estadístico de solicitudes en un intervalo de 5 minutos y no a actividad maliciosa ni compromiso de infraestructura. Se descarta actividad hostil y se procede al cierre."*

#### 5. Acciones y Seguimiento
* [x] **Stellar Cyber:** Caso cerrado como `False Positive` / `Benign`.
* [ ] **Tuning de Detección:** Configurar regla de supresión de alerta en Stellar Cyber para los SIDs `2060507` y `2060512` cuando provengan de los controladores de dominio autorizados (`10.11.1.1`, `10.11.1.2`), evitando futuras tormentas de alertas por AnyDesk.

---

### Caso #003 - Falsa Alarma de Impair Defenses por Falla de Actualización de Sophos (VM-MARANDU)

* **Fecha/Hora:** `04/10/2026 09:27:02` (Hora Local GMT-3) / `2026-10-04 12:27:02 UTC`
* **Plataforma:** Stellar Cyber OpenXDR v7.0.0s (Conector `sophos_events`)
* **Motor:** `log_collector` / Regla XDR `sophos_event-defense_evasion-impair_defenses` | **Severidad:** `Low` (15/100) | **Tenant:** `CAJAANDE`
* **Activo Afectado:** `VM-MARANDU` (`172.16.201.4` / Servidor en Caja Ande / Sophos Server Endpoint)
* **Usuario:** `Sistema / Sophos Update Service`
* **Táctica / Técnica MITRE:** `TA0005 - Defense Evasion` / `T1562 - Impair Defenses` (Catalogación incorrecta del motor XDR)
* **Playbook Aplicado:** `PB-2.2: Monitoreo Operativo y Falsos Positivos` (descarte de `PB-4.1: Malware y Evasión`)
* **Veredicto Final:** **Falso Positivo (Ruido Operativo / Error Transitorio de Red)**

#### 1. ¿Por qué chilló la consola? (La hipótesis inicial)
Stellar Cyber disparó dos alertas correlacionadas catalogadas como *"Sophos Event: Impair Defenses (TA0005 / T1562)"*, sugiriendo que un actor malicioso o un malware estaba intentando degradar o deshabilitar las defensas del servidor `VM-MARANDU`. La alerta fue provocada por un evento nativo de Sophos Endpoint clasificado como `Event::Endpoint::UpdateFailure` de severidad baja, donde falló la descarga de un paquete de firmas (`sdds3.WindowsCloudMDR_2023.2.0.3.f08cc6df02.dat`) desde la CDN oficial de Sophos (`sdds3.sophosupd.net`).

#### 2. Evidencias Clave y Disección Forense
* **Evento Original de Sophos Central:**
  * Event ID: `86ce14c9-43c1-4ca2-b5ca-8456531681fc`
  * Threat Name: `Event::Endpoint::UpdateFailure`
  * Grupo Operativo: `UPDATING` | Severidad: `low`
  * Mensaje: *"Download of sdds3.WindowsCloudMDR_2023.2.0.3.f08cc6df02.dat failed from server https://sdds3.sophosupd.net/suite/sdds3.WindowsCloudMDR_2023.2.0.3.f08cc6df02.dat."*
* **Duplicación de Ingesta en Stellar Cyber:**
  * El lote contenía 2 documentos JSON (`3wnjBqEBI3UnQyDOlLRF` y `gwnoBqEBI3UnQyDOKvcX`) generados con 6 minutos de diferencia (12:30:46 y 12:36:43 UTC) debido a reingesta de syslog del conector `sophos_CAJA-ANDE-SOPHOS`, tratándose exactamente del mismo evento único.
* **Comprobación de Integridad y Autorecuperación Inmediata (Sophos Central):**
  * En ese mismo minuto (`04/10/2026, 09:27`), inmediatamente posterior al fallo de descarga, la consola de Sophos Central registró **`Update succeeded`**.
  * El agente Sophos reintentó la solicitud HTTPS a la CDN y completó la descarga del paquete MDR exitosamente en segundos.
  * El servicio de Sophos no fue detenido, ni desinstalado, ni alterado.
  * No se observaron ejecuciones de comandos de evasión (`sc stop`, `taskkill`, manipulaciones de registro ni bypass de Tamper Protection).

#### 3. ¿Qué era en realidad? (Causa Raíz)
Un hipo de red o microcorte transitorio de conexión HTTPS hacia la CDN de Sophos al descargar un archivo de actualización de definiciones MDR (`.dat`). El agente Sophos cuenta con tolerancia a fallos y reintentó en el mismo minuto (09:27), completando la actualización con éxito (`Update succeeded`). Stellar Cyber correlacionó prematuramente el log de error aislado sin esperar el estado final de la actualización.

#### 4. Justificación Técnica de Cierre (Stellar Cyber)
> *"Cerrado como Falso Positivo / Ruido Operativo. La alerta corresponde a un fallo transitorio de conectividad HTTPS (Event::Endpoint::UpdateFailure) registrado por el agente Sophos Endpoint en el servidor VM-MARANDU (172.16.201.4, Tenant CAJAANDE) al intentar descargar el paquete sdds3.WindowsCloudMDR. Se comprueba en la telemetría nativa de Sophos Central que en el mismo minuto (09:27) el agente reintentó la operación y completó la actualización con éxito ('Update succeeded'). No existió desactivación de motores, manipulación de Tamper Protection ni actividad maliciosa de evasión o degradación de defensas (MITRE T1562). El activo cuenta con protección activa, firmas al día y estado operativo 100% íntegro."*

#### 5. Acciones y Seguimiento
* [x] **Stellar Cyber:** Cerrar alertas duplicadas como `False Positive` / `Benign`.
* [ ] **Tuning de Reglas (Recomendado):** Ajustar la regla `sophos_event-defense_evasion-impair_defenses` en Stellar Cyber para excluir eventos de severidad `low` pertenecientes al grupo `UPDATING` (`Event::Endpoint::UpdateFailure`), reservando T1562 únicamente para eventos donde se deshabilite la protección en tiempo real o se detenga un servicio crítico.

---

### Caso #004 - Anomalía de Política Firewall (VPN TO P5-UPAY) y DNS cyberplace.social (nb-amorinigo)

* **Fecha/Hora:** `03/10/2026 19:31:25 - 20:57:15` (Hora Local GMT-3) / `2026-10-03 22:31:25 - 23:57:15 UTC`
* **Plataforma:** Stellar Cyber OpenXDR v7.0.0s (Conectores `fw_fortigate` y `aella_flow`)
* **Motor / Regla:**
  * `internal_fw_policy_id` (Internal Firewall Policy Anomaly / Score: 53 / `XTA0002` / `XT2002`)
  * `dns_new_tld` (Uncommon Top-Level Domain Anomaly / Score: 33 / `TA0011` / `T1071.001`)
* **Tenant:** `technoma` | **Severidad:** `Medium` (33 a 53)
* **Activo Afectado:** `nb-amorinigo.technoma.local` (`10.212.134.202` / Pool SSL-VPN en FortiGate `FG-Technoma`)
* **Usuario:** `angelramos` (Grupo: `VPN_LDAP`, Servidor: `LDAP_Tech`)
* **Destinos Involucrados:**
  1. `192.168.51.25:80` (Servidor interno UPAY en interfaz `UPAY-P5-PRI` vía regla FW 179)
  2. `10.11.1.1:53` (Controlador de Dominio / DNS Primario Technoma) ➔ Consulta FQDN `cyberplace.social` (Resuelto a `95.216.137.24`)
* **Playbook Aplicado:** `PB-2.2: Monitoreo Operativo y Falsos Positivos` (descarte formal de `PB-5.6: Comunicación C2` y `PB-1.1: Movimiento Lateral`)
* **Veredicto Final:** **Benign True Positive (BTP) / Falso Positivo Operacional (Ruido Heurístico de Línea Base)**

#### 1. ¿Por qué chilló la consola? (La hipótesis inicial)
Stellar Cyber correlacionó dos eventos heurísticos sobre el host remoto conectado por VPN `nb-amorinigo.technoma.local` (`10.212.134.202`):
1. **Anomalía de Política Firewall:** Disparó alerta alegando que la política de firewall `FG-Technoma_179` (`VPN TO P5-UPAY`) *"nunca había sido observada antes tras 203 días de silencio"*.
2. **Anomalía de TLD DNS:** Una hora y media después, el mismo host realizó una consulta DNS al dominio `cyberplace.social`, activando la regla de C2 por tratarse de un TLD (`.social`) *"no visto en la red en los últimos 242 días"*.

#### 2. Evidencias Clave y Disección Forense
* **Análisis de la Conexión de Firewall (Evento 1 - 19:31:25):**
  * Usuario autenticado legítimamente en SSL-VPN: `angelramos` vía LDAP corporativo (`LDAP_Tech`).
  * Tráfico: Intento de acceso HTTP puerto 80 hacia la plataforma interna de pagos `192.168.51.25` (`UPAY-P5-PRI`).
  * Política coincidente: Regla 179 `VPN TO P5-UPAY` con SNAT a `192.168.169.252`.
  * Resultado: `action="timeout"` (5 paquetes enviados, 260 bytes, 0 recibidos). El servidor UPAY no respondió en el puerto 80, cerrándose la sesión por timeout normal.
  * La alerta se debió exclusivamente a que hacía 203 días que esa política específica no registraba tráfico en el baseline de Stellar Cyber.
* **Análisis de la Consulta DNS (Evento 2 - 20:57:15):**
  * Consulta: `cyberplace.social` (Tipo A) enviada al DNS interno `10.11.1.1`.
  * Respuesta DNS: `95.216.137.24` (Hetzner Online GmbH, Alemania).
  * Naturaleza del Dominio: Instancia pública de la red social federada **Mastodon** orientada a la comunidad de ciberseguridad y tecnología (`cyberplace.social`).
  * Reputación: `Good` (`domain_reputation: Good`). No es DGA (`is_dga: "no"`), sin tunneling ni balizamiento C2. Navegación web estándar.

#### 3. ¿Qué era en realidad? (Causa Raíz)
Actividad benigna de un colaborador conectado por VPN (`angelramos`) que:
1. Intentó ingresar a un aplicativo interno de UPAY cuyo servicio HTTP estaba inactivo o no respondió (timeout en regla de firewall autorizada).
2. Realizó navegación web personal/profesional hacia una red social de ciberseguridad en Mastodon (`cyberplace.social`).
Ambas alertas son artefactos matemáticos del motor de Machine Learning de Stellar Cyber que penaliza acciones poco frecuentes (políticas no usadas en 203 días y dominios con TLDs no corporativos tras 242 días).

#### 4. Justificación Técnica de Cierre (Stellar Cyber)
> *"Cerrado como Falso Positivo / BTP. La alerta agrupa dos detecciones heurísticas de línea base sobre el host nb-amorinigo.technoma.local (10.212.134.202) operado legítimamente por el usuario angelramos vía SSL-VPN. La primera alerta obedece a un intento de conexión HTTP con timeout hacia el aplicativo interno UPAY (192.168.51.25) haciendo coincidencia con la regla autorizada de firewall 179 ('VPN TO P5-UPAY'), disparada únicamente por falta de uso previo en 203 días. La segunda alerta corresponde a una consulta DNS de navegación legítima al dominio cyberplace.social (instancia Mastodon en Hetzner con reputación Good), catalogada como anomalía C2 solo por infrecuencia del TLD .social tras 242 días. Se descarta actividad maliciosa, beaconing y compromiso de activo."*

#### 5. Acciones y Seguimiento
* [x] **Stellar Cyber:** Casos cerrados como `False Positive` / `Benign`.
* [ ] **Operaciones TI / Redes (Opcional):** Si el aplicativo UPAY (`192.168.51.25:80`) debía estar activo para el usuario, notificar a soporte de infraestructura para verificar si el servicio web se encuentra caído o si migró a HTTPS (puerto 443).

---

### Caso #005 - Caída de Sensor de Red y Agente por Corte de Fibra (Caja Ande)

* **Fecha/Hora:** `04/10/2026 03:00:00 - 09:00:00` (Hora Local GMT-3)
* **Plataforma:** Stellar Cyber OpenXDR / Enlace Perimetral
* **Motor / Regla:** Monitoreo de Conectividad (Sensor Offline / Heartbeat Lost) | **Severidad:** `Alta (P1)`
* **Activos Afectados:**
  * Sensor de Red: `Sensor-Modular-CajaAnde` (ID: `01f719f1094e4cfaaf2bbb6a0526400a`)
  * Host / Agente: `VMBASE8` (ID: `4c735067a7f5483ca72265eb5324214c`)
  * Gateway IP: `190.52.189.87`
* **Usuario:** `Infraestructura / Red`
* **Táctica / Técnica MITRE:** `N/A (Disponibilidad de Servicio)`
* **Formulario Oficial:** [`FL-THN-POS-01 Rev. 03` (Fila 9)](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/FL-THN-POS-01%20Rev.%2003%20Registro%20de%20Incidencias%20de%20Seguridad%20(1)%20(1).xlsx)
* **Veredicto Final:** **Incidente Operativo Resuelto (Disponibilidad / Corte de Enlace)**

#### 1. Detección Operativa
A las 03:00 AM se registró la pérdida total de telemetría y estado offline simultáneo del sensor modular NDR (`Sensor-Modular-CajaAnde`) y del agente en el controlador de dominio (`VMBASE8`), ambos alojados en la sede de CAJA ANDE tras el gateway `190.52.189.87`.

#### 2. Evidencias Clave y Validación NOC
* **Correlación de Caída:** Coincidencia exacta de desconexión en ambos activos a las 03:00 AM, descartando fallo interno de software o fallo de máquina virtual aislada.
* **Gestión con NOC:** NOC confirmó corte de enlace físico de fibra óptica del proveedor de Internet perimetral que alimenta la sede.
* **Notificación al Cliente:** NOC notificó oportunamente al contacto técnico César (CAJA ANDE) a las 04:00 AM, cumpliendo con el SLA P1 (tiempo de notificación: 1.0 h).

#### 3. Causa Raíz
Corte físico del tendido de fibra óptica del proveedor de conectividad de CAJA ANDE.

#### 4. Solución y Cierre Técnico
A las 09:00 AM el proveedor normalizó el enlace de fibra. El sensor y agente reanudaron automáticamente la conexión segura con Stellar Cyber y restablecieron el flujo normal de telemetría NDR tras 6 horas de interrupción.

#### 5. Acciones y Seguimiento
* [x] **Registro Oficial:** Asentado en Fila 9 de `FL-THN-POS-01 Rev. 03 Registro de Incidencias de Seguridad`.
* [x] **Telemetría:** Consola Stellar Cyber en verde con flujo normal confirmado.
* [x] **Cliente:** Contacto César (Caja Ande) notificado y conformidad confirmada.

---

<a id="caso-148379"></a>
### Caso #148379 - Ejecución de runonce.exe por svchost.exe (Fabio Mora)

* **Fecha/Hora:** `07/10/2026 09:04:15` (Hora Local GMT-3) / `2026-10-07 12:04:15 UTC`
* **Plataforma:** Palo Alto Networks Cortex XDR (EDR Agent v8.x/v9.x)
* **Motor:** `ANALYTICS_BIOC` | **Severidad:** `Low` (1) | **Acción:** `DETECTED`
* **Activo Afectado:** `NB-FMORA` (`192.168.100.1` / `172.22.16.1` / `192.168.23.1`)
* **Usuario:** `TECHNOMA\fabiomora`
* **Táctica / Técnica MITRE:** `TA0003 - Persistence` / `TA0004 - Privilege Escalation` / `T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder`
* **Playbook Aplicado:** `PB-2.2: Monitoreo Operativo` / `PB-4.1: Persistencia y Autoejecución`
* **Veredicto Final:** **Benign True Positive (BTP) / Falso Positivo Heurístico**

#### 1. ¿Por qué chilló la consola? (La hipótesis inicial)
La regla de comportamiento `Suspicious runonce.exe parent process` de Cortex XDR (`ANALYTICS_BIOC`) alertó porque el ejecutable del sistema `runonce.exe` fue invocado por una instancia del servicio de Windows `svchost.exe` (`C:\Windows\System32\svchost.exe`, PID 3844) en lugar de iniciarse por el proceso estándar de inicio interactivo de sesión de usuario (`userinit.exe` o `winlogon.exe`).

#### 2. Evidencias Clave y Disección Forense
* **Identificación de Binarios y Firmas:**
  * Proceso Destino: `C:\Windows\System32\runonce.exe` con argumento `/Explorer`.
  * Proceso Iniciador / Padre: `C:\Windows\System32\svchost.exe` (PID 3844, servicio Appinfo / UAC Elevation).
  * Firma Digital: Ambos procesos firmados legítimamente por `Microsoft Corporation` (`initiatorsigner: Microsoft Corporation`, `osparentsigner: Microsoft Corporation`).
  * Hash SHA-256 de `svchost.exe`: `1222a44a5fdb4efde4dfcb41093648627950e7ec02d8667f1c26ccae31d922e2`.
* **Árbol de Procesos y Contexto:**
  * `services.exe` ➔ `svchost.exe -s Appinfo` (PID 3844) ➔ `runonce.exe /Explorer`.
  * Ocurrió en la estación de trabajo de Fabio Mora (`NB-FMORA`) durante una elevación administrativa UAC / arranque de sesión tras actualización de componentes de shell de Windows.
* **Comportamiento en Registro y Red:**
  * No se crearon ni modificaron llaves de persistencia maliciosa fuera de la ejecución estándar de tareas pendientes de Windows RunOnce.
  * Tráfico de Red: Nulo (`containsfeaturedipaddress: NO`), sin conexiones externas ni beaconing C2.

#### 3. ¿Qué era en realidad? (Causa Raíz)
Comportamiento operativo normal del sistema operativo Windows: inicialización legítima de tareas de interfaz gráfica/shell (`/Explorer`) gestionadas por el servicio `Appinfo` (Application Information Service) bajo el usuario interactivo `fabiomora`.

#### 4. Justificación Técnica de Cierre (Cortex XDR)
> *"Cerrado como Falso Positivo / BTP. El evento 'Suspicious runonce.exe parent process' en el host NB-FMORA (usuario TECHNOMA\fabiomora) corresponde a la ejecución legítima de C:\Windows\System32\runonce.exe con el argumento /Explorer invocado por svchost.exe (PID 3844, servicio de elevación Appinfo). Ambos binarios cuentan con firma digital válida de Microsoft Corporation y hash íntegro. No se constató inyección de código, persistencia anómala en el registro ni conexiones de red asociadas, catalogándose como falso positivo heurístico por linaje de procesos del sistema operativo. Sin impacto en seguridad."*

#### 5. Acciones y Seguimiento
* [x] **Cortex XDR:** Incidente #148379 clasificado como `Resolved - False Positive` / `Benign`.
* [x] **Bitácora Personal:** Asentado en Caso #006.
* [ ] **Tuning BIOC (Opcional):** Evaluar excepción o ajuste de regla BIOC para llamadas legítimas de `runonce.exe /Explorer` originadas por `svchost.exe (Appinfo)` con firma de Microsoft.

---

<a id="caso-148359"></a>
### Caso #148359 - Ejecución de PowerShell Codificado por claude.exe (José Torales)

* **Fecha/Hora:** `07/10/2026 11:41:41` (Hora Local GMT-3) / `2026-10-07 14:41:41 UTC` (Creado: `2026-10-07 02:04:13 UTC`)
* **Plataforma:** Palo Alto Networks Cortex XDR (EDR Agent v8.x/v9.x)
* **Motor:** `ANALYTICS_BIOC` | **Severidad:** `Medium / Low` (1) | **Acción:** `DETECTED`
* **Activo Afectado:** `NB-JTORALES` (`TECHNOMA\josetorales`)
* **Usuario:** `TECHNOMA\josetorales`
* **Táctica / Técnica MITRE:** `TA0002 - Execution` / `T1059.001 - Command and Scripting Interpreter: PowerShell` / `T1027 - Obfuscated Files or Information`
* **Playbook Aplicado:** `PB-2.2: Monitoreo Operativo` (y descarte formal de `PB-4.3: Ejecución de Scripts / LOLBins`)
* **Veredicto Final:** **Benign True Positive (BTP) / Falso Positivo Operativo (Herramienta de Desarrollo)**

#### 1. ¿Por qué chilló la consola? (La hipótesis inicial)
El motor de analítica conductual de Cortex XDR (`ANALYTICS_BIOC`) disparó la alerta *«PowerShell runs suspicious base64-encoded commands»* debido a que el proceso `claude.exe` (PID 1924) ejecutó `powershell.exe` pasándole una cadena extensa codificada en Base64 (`-EncodedCommand ...`), patrón comúnmente empleado por actores de amenazas para ofuscar scripts y evadir filtros perimetrales. Adicionalmente, esta línea de comando fue vista en 0 equipos y 0 días previos en la organización.

#### 2. Evidencias Clave y Disección Forense
* **Identificación del Proceso Padre:**
  * Proceso Padre: `claude.exe` (PID 1924).
  * Origen: CLI / Extensión oficial del asistente de desarrollo **Claude Code** (Anthropic PBC), ejecutado dentro del entorno de desarrollo de José Torales.
  * Proceso Abuelo: `Code.exe` (Microsoft Visual Studio Code) / Terminal de desarrollo.
* **Disección y Decodificación del Payload Base64:**
  * Se decodificó íntegramente la carga útil Base64 en UTF-16LE, confirmando funciones de parsing de AST y ejecución de comandos Git del espacio de trabajo local:
    ```powershell
    git -C C:\Users\josetorales\dis-analytics status -sb
    git -C C:\Users\josetorales\dis-analytics remote -v
    Get-ChildItem C:\Users\josetorales\dis-analytics\docs -Recurse -File | Select-Object -ExpandProperty FullName
    ```
  * Objetivo de la ejecución: Consultar el estado del árbol de control de versiones Git y listar la documentación del proyecto interno `dis-analytics`.
* **Comportamiento en Red y Sistema:**
  * Sin conexiones a C2 externas, sin intentos de descarga de payloads maliciosos, sin manipulación de privilegios ni persistencia.
  * Tráfico de Red: Nulo o estrictamente asociado a los repositorios remotos legítimos del proyecto de desarrollo.

#### 3. ¿Qué era en realidad? (Causa Raíz)
Actividad legítima de desarrollo de software: el asistente de inteligencia artificial para desarrollo Claude Code (`claude.exe`) ejecutando comandos estándar de Git y consulta de archivos mediante PowerShell para asistir a José Torales en el repositorio corporativo `dis-analytics`.

#### 4. Justificación Técnica de Cierre (Cortex XDR)
> *"Cerrado como Falso Positivo / BTP. El incidente #148359 'PowerShell runs suspicious base64-encoded commands' en el endpoint NB-JTORALES (usuario TECHNOMA\josetorales) se originó por la invocación de powershell.exe desde la herramienta de desarrollo claude.exe (PID 1924, Claude Code de Anthropic). La decodificación forense del parámetro Base64 reveló comandos benignos de inspección de repositorio de software ('git status', 'git remote -v' y lectura de la carpeta docs en C:\Users\josetorales\dis-analytics). No se identificó tráfico C2, persistencia ni actividad maliciosa. Caso cerrado como comportamiento operativo conocido."*

#### 5. Acciones y Seguimiento
* [x] **Cortex XDR:** Incidente #148359 cerrado como `False Positive` / `Resolved - Known Behavior`.
* [x] **Bitácora Personal:** Asentado en Caso #007.
* [ ] **Tuning BIOC / Whitelist:** Generar regla de excepción BIOC en Cortex XDR para el binario firmado `claude.exe` invocando comandos locales de desarrollo/git en la estación de José Torales para evitar alertas redundantes durante sus jornadas de programación.

---

<a id="caso-148460"></a>
### Caso #148460 - Conexión de Anki (pythonw.exe) a AnkiWeb (Gustavo Reyes)

* **Fecha/Hora:** `07/10/2026 11:38:02` (Hora Local GMT-3) / `2026-10-07 14:38:02 UTC`
* **Plataforma:** Palo Alto Networks Cortex XDR (EDR Agent v9.3.0.231)
* **Motor:** `ANALYTICS_BIOC` | **Severidad:** `Low` (1) | **Acción:** `DETECTED`
* **Activo Afectado:** `NB-GREYES` (`192.168.169.72` / Windows 11 Build 26300)
* **Usuario:** `TECHNOMA\gustavoreyes`
* **Táctica / Técnica MITRE:** `TA0011 - Command and Control` / `TA0002 - Execution` / `T1071.001 - Application Layer Protocol: Web Protocols` / `T1059 - Command and Scripting Interpreter`
* **Playbook Aplicado:** `PB-5.6: Comunicación C2` / `PB-2.2: Monitoreo Operativo`
* **Veredicto Final:** **Benign True Positive (BTP) / Falso Positivo Heurístico (Sincronización AnkiWeb)**

#### 1. ¿Por qué chilló la consola? (La hipótesis inicial)
La regla de comportamiento `Scripting engine connected to a rare external host` de Cortex XDR (`ANALYTICS_BIOC`) alertó porque el motor de scripting `pythonw.exe` (`C:\Users\gustavoreyes\AppData\Local\AnkiProgramFiles\python\cpython-3.13.5-windows-x86_64-none\pythonw.exe`) estableció conexión cifrada HTTPS saliente (puerto 443) hacia el dominio `ankiweb.net`. El motor analítico consideró sospechoso el evento porque `pythonw.exe` figuraba como ejecutable no firmado dentro de un virtual environment local, y `ankiweb.net` fue clasificado como destino infrecuente en la red corporativa (visto en solo 2 endpoints a lo largo de 5 días en el último mes).

#### 2. Evidencias Clave y Disección Forense
* **Identificación del Binario y Aplicación:**
  * Proceso Iniciador / Intérprete: `pythonw.exe` (SHA256: `16106c2544aa010b33b663840154bb8ca6707bd51ead92ff69af529c2cb55a92`, MD5: `422d38518af068f8d39497782bd0b23f`).
  * Línea de Comandos: `"C:\Users\gustavoreyes\AppData\Local\AnkiProgramFiles\.venv\Scripts/pythonw.exe" -c "import aqt, sys; sys.argv[0] = 'Anki'; aqt.run()"`.
  * Proceso Padre / Propietario de Causalidad (CGO): `C:\Users\gustavoreyes\AppData\Local\Programs\Anki\anki.exe` (SHA256: `bed339a581af01eadda0c66c13874db1e5d3fb8929b9f604c9d4aab95fab9d2d`).
  * **Firma Digital del CGO:** Válida y firmada por **`Ankitects Pty Ltd`** (`cgosigner: Ankitects Pty Ltd`).
* **Módulo Invocado (`aqt`):**
  * El módulo importado `aqt` corresponde a la interfaz gráfica oficial en PyQt del software educativo **Anki** (spaced repetition flashcard system).
* **Flujo de Red y Reputación de Destino:**
  * Destino: `142.132.136.175:443` (FQDN: `ankiweb.net`, alojado en infraestructura de Hetzner Online GmbH, Alemania).
  * Protocolo: SSL/TLS (HTTPS estándar).
  * Finalidad: Sincronización legítima de mazos de tarjetas de estudio, notas y progreso del usuario con los servidores de AnkiWeb.
  * Tráfico de Red: Sesión SSL normal; sin patrones de beaconing interactivo malicioso ni balizamiento C2.

#### 3. ¿Qué era en realidad? (Causa Raíz)
Uso y sincronización legítima del software de tarjetas de memoria y estudio **Anki**, instalado por el usuario Gustavo Reyes para actividades de capacitación/aprendizaje. El ejecutable compilado `anki.exe` (firmado por Ankitects Pty Ltd) delega la ejecución de la GUI y la sincronización con la nube de AnkiWeb a su entorno Python integrado (`pythonw.exe`), disparando el detector heurístico de motores de script comunicándose con destinos raros.

#### 4. Justificación Técnica de Cierre (Cortex XDR)
> *"Cerrado como Falso Positivo / BTP. El incidente #148460 'Scripting engine connected to a rare external host' en el endpoint NB-GREYES (usuario TECHNOMA\gustavoreyes) corresponde a la ejecución legítima del software de aprendizaje Anki. El proceso pythonw.exe fue instanciado por anki.exe (Causality Group Owner con firma digital válida de Ankitects Pty Ltd) ejecutando el módulo aqt.run() para sincronizar mazos de estudio con el servicio oficial en la nube ankiweb.net (142.132.136.175:443). Se descarta actividad C2, exfiltración y presencia de malware. Caso resuelto como comportamiento operativo benigno."*

#### 5. Acciones y Seguimiento
* [x] **Cortex XDR:** Incidente #148460 cerrado como `Resolved - False Positive` / `Benign`.
* [x] **Bitácora Personal:** Asentado en Caso #008.
* [ ] **Tuning BIOC (Opcional):** Si se presentan alertas recurrentes, crear excepción en Cortex XDR para conexiones salientes al dominio `*.ankiweb.net` cuando el ancestro de causalidad sea el binario firmado `anki.exe`.

---

<a id="caso-148343"></a>
### Caso #148343 - Ejecución de PowerShell y Parser AST por claude.exe (José Torales)

* **Fecha/Hora:** `06/10/2026 19:35:06` (Hora Local GMT-3) / `2026-10-06 22:35:06 UTC`
* **Plataforma:** Palo Alto Networks Cortex XDR (EDR Agent v9.3.0.231)
* **Motor:** `ANALYTICS_BIOC` | **Severidad:** `Low` (1) | **Acción:** `DETECTED`
* **Activo Afectado:** `NB-JTORALES` (`192.168.100.14` / Windows 11 Build 26300)
* **Usuario:** `TECHNOMA\josetorales`
* **Táctica / Técnica MITRE:** `TA0002 - Execution` / `T1059.001 - Command and Scripting Interpreter: PowerShell` / `T1027 - Obfuscated Files or Information`
* **Playbook Aplicado:** `PB-2.2: Monitoreo Operativo` (y descarte formal de `PB-4.3: Ejecución de Scripts / LOLBins`)
* **Veredicto Final:** **Benign True Positive (BTP) / Falso Positivo Operativo (Extensión Claude Code en VS Code)**

#### 1. ¿Por qué chilló la consola? (La hipótesis inicial)
El motor de analítica conductual de Cortex XDR (`ANALYTICS_BIOC`) activó la alerta *«PowerShell runs suspicious base64-encoded commands»* debido a que `claude.exe` ejecutó `powershell.exe` pasando una cadena extensa codificada en Base64 (`-EncodedCommand ...`). La regla BIOC clasifica automáticamente los comandos codificados en Base64 no vistos en los últimos 30 días como potencialmente maliciosos por su uso común en evasión de defensas.

#### 2. Evidencias Clave y Disección Forense
* **Identificación del Proceso Iniciador:**
  * Proceso Iniciador / Padre: `claude.exe` (PID: 30320, SHA256: `bcc6d9117aec30ad9414490302a25414359c871f5647e32e49b055c92bf84e0b`).
  * Ruta: `C:\Users\josetorales\.vscode\extensions\anthropic.claude-code-2.1.289-win32-x64\resources\native-binary\claude.exe`.
  * **Firma Digital del Binario:** Válida y firmada por **`Anthropic, PBC`** (`initiatorsigner: Anthropic, PBC`).
  * Proceso Abuelo / CGO: `C:\Users\josetorales\AppData\Local\Programs\Microsoft VS Code\Code.exe` (Firmado por **`Microsoft Corporation`**).
* **Disección y Análisis del Código PowerShell:**
  * El payload decodificado ejecuta una rutina de análisis sintáctico mediante la API oficial de PowerShell:
    `[System.Management.Automation.Language.Parser]::ParseInput(...)` y la función interna `Get-RawCommandElements`.
  * Propósito: Inspeccionar el árbol sintáctico (AST) de comandos de consola ejecutados en el espacio de trabajo para validar sintaxis de scripts antes de su ejecución.
* **Comportamiento en Red y Sistema:**
  * Sin conexiones de red maliciosas (`containsfeaturedipaddress: NO`).
  * Sin alteración de llaves de persistencia ni escalamiento de privilegios.

#### 3. ¿Qué era en realidad? (Causa Raíz)
Operación estándar y legítima de la extensión oficial **Claude Code** para Visual Studio Code (`anthropic.claude-code-2.1.289`), utilizada por José Torales en su estación de trabajo. La herramienta utiliza PowerShell en segundo plano para validar la sintaxis de comandos de desarrollo en entornos Windows.

#### 4. Justificación Técnica de Cierre (Cortex XDR)
> *"Cerrado como Falso Positivo / BTP. El incidente #148343 'PowerShell runs suspicious base64-encoded commands' en NB-JTORALES (usuario TECHNOMA\josetorales) se debió a la invocación de powershell.exe desde el binario firmado claude.exe (PID 30320, firma válida de Anthropic, PBC), alojado dentro de la extensión oficial de VS Code. La carga útil codificada corresponde a rutinas internas de parsing de sintaxis AST ([System.Management.Automation.Language.Parser]) para validación de comandos del entorno de desarrollo. No se constató balizamiento C2, persistencia ni actividad maliciosa. Caso cerrado como comportamiento operativo conocido."*

#### 5. Acciones y Seguimiento
* [x] **Cortex XDR:** Incidente #148343 cerrado como `Resolved - False Positive` / `Benign`.
* [x] **Bitácora Personal:** Asentado en Caso #009.
* [ ] **Tuning BIOC / Whitelist:** Incorporar excepción en Cortex XDR para el binario firmado `claude.exe` (`Anthropic, PBC`) al ejecutar PowerShell con comandos de validación AST.

---

<a id="caso-148341"></a>
### Caso #148341 - Ejecución de PowerShell y Browser Automation por claude.exe (José Torales)

* **Fecha/Hora:** `06/10/2026 19:34:33` (Hora Local GMT-3) / `2026-10-06 22:34:33 UTC`
* **Plataforma:** Palo Alto Networks Cortex XDR (EDR Agent v9.3.0.231)
* **Motor:** `ANALYTICS_BIOC` | **Severidad:** `Low` (1) | **Acción:** `DETECTED`
* **Activo Afectado:** `NB-JTORALES` (`192.168.100.14` / Windows 11 Build 26300)
* **Usuario:** `TECHNOMA\josetorales`
* **Táctica / Técnica MITRE:** `TA0002 - Execution` / `T1059.001 - Command and Scripting Interpreter: PowerShell` / `T1027 - Obfuscated Files or Information`
* **Playbook Aplicado:** `PB-2.2: Monitoreo Operativo` (y descarte formal de `PB-4.3: Ejecución de Scripts / LOLBins`)
* **Veredicto Final:** **Benign True Positive (BTP) / Falso Positivo Operativo (Pruebas Locales de QA en Desarrollo / Claude Code)**

#### 1. ¿Por qué chilló la consola? (La hipótesis inicial)
El motor de comportamiento de Cortex XDR (`ANALYTICS_BIOC`) alertó sobre la regla *«PowerShell runs suspicious base64-encoded commands»* debido a que el proceso `claude.exe` invocó `powershell.exe` con una cadena extensa en Base64 (`-EncodedCommand ...`) que no había sido observada previamente en los últimos 30 días en la organización. El EDR correlacionó el uso de comandos codificados como una técnica típica de ofuscación de scripts.

#### 2. Evidencias Clave y Disección Forense
* **Identificación del Proceso Iniciador:**
  * Proceso Iniciador / Padre: `claude.exe` (PID: 30320, SHA256: `bcc6d9117aec30ad9414490302a25414359c871f5647e32e49b055c92bf84e0b`).
  * Ruta: `C:\Users\josetorales\.vscode\extensions\anthropic.claude-code-2.1.289-win32-x64\resources\native-binary\claude.exe`.
  * **Firma Digital del Binario:** Válida y verificada de **`Anthropic, PBC`** (`initiatorsigner: Anthropic, PBC`).
  * Proceso Abuelo / CGO: `C:\Users\josetorales\AppData\Local\Programs\Microsoft VS Code\Code.exe` (Firmado por **`Microsoft Corporation`**).
* **Decodificación Forense del Script Base64:**
  * Se decodificó íntegramente la carga útil interna en UTF-8, revelando la ejecución de una prueba automatizada de frontend en el entorno de desarrollo local:
    ```powershell
    $dir = "$env:TEMP\claude\c--Users-josetorales-OneDrive---Technoma-SACI-Documentos-VS\e1e276ab-99be-4e9e-97c7-4e29fe7985d8\scratchpad"
    $qa = Join-Path $dir "qa_bar.mjs"
    $node = Join-Path $dir "node20\node-v20.18.1-win-x64\node.exe"
    $out = Join-Path $dir "qa_bar.out"
    & $node "C:\Users\josetorales\.claude\skills\browser-automation\browser.mjs" http://localhost:18088/login/ --script $qa --timeout 180000 > $out 2>&1
    Get-Content $out | Select-Object -First 60
    ```
  * Propósito: Ejecución de la skill de automatización de navegador (`browser-automation`) de Claude Code con Node.js para verificar el endpoint local de pruebas `http://localhost:18088/login/`.
* **Comportamiento en Red y Sistema:**
  * Comunicación estrictamente local (`http://localhost:18088`), sin tráfico a infraestructura externa desconocida (`containsfeaturedipaddress: NO`).
  * Sin alteración de registro de arranque, sin persistencia ni evasión defensiva.

#### 3. ¿Qué era en realidad? (Causa Raíz)
Actividad legítima de pruebas y aseguramiento de calidad (QA) ejecutadas por el desarrollador José Torales mediante el asistente Claude Code en Visual Studio Code. La herramienta ejecutó un script en Node.js para validar la interfaz de login de una aplicación web alojada localmente en su máquina (`localhost:18088`).

#### 4. Justificación Técnica de Cierre (Cortex XDR)
> *"Cerrado como Falso Positivo / BTP. El incidente #148341 'PowerShell runs suspicious base64-encoded commands' en NB-JTORALES (usuario TECHNOMA\josetorales) se originó por la invocación de powershell.exe desde la herramienta de desarrollo claude.exe (PID 30320, firma válida de Anthropic, PBC) dentro de Visual Studio Code. La decodificación del parámetro Base64 demostró la ejecución de un script de pruebas de navegación automatizada (browser-automation) sobre un servicio web local en 'http://localhost:18088/login/'. No existe comunicación externa maliciosa, persistencia ni compromiso del endpoint. Caso resuelto como comportamiento operativo de desarrollo."*

#### 5. Acciones y Seguimiento
* [x] **Cortex XDR:** Incidente #148341 cerrado como `Resolved - False Positive` / `Benign`.
* [x] **Bitácora Personal:** Asentado en Caso #010.
* [ ] **Tuning BIOC / Whitelist:** Regla de exclusión en Cortex XDR para invocaciones de PowerShell con comandos codificados cuyo proceso padre sea el binario firmado `claude.exe` en estaciones de desarrollo autorizadas.

---

<a id="caso-148309"></a>
### Caso #148309 - Ejecución de PowerShell y Edición de Script QA por claude.exe (José Torales)

* **Fecha/Hora:** `06/10/2026 18:36:49` (Hora Local GMT-3) / `2026-10-06 21:36:49 UTC`
* **Plataforma:** Palo Alto Networks Cortex XDR (EDR Agent v9.3.0.231)
* **Motor:** `ANALYTICS_BIOC` | **Severidad:** `Low` (1) | **Acción:** `DETECTED`
* **Activo Afectado:** `NB-JTORALES` (`192.168.100.14` / Windows 11 Build 26300)
* **Usuario:** `TECHNOMA\josetorales`
* **Táctica / Técnica MITRE:** `TA0002 - Execution` / `T1059.001 - Command and Scripting Interpreter: PowerShell` / `T1027 - Obfuscated Files or Information`
* **Playbook Aplicado:** `PB-2.2: Monitoreo Operativo` (y descarte formal de `PB-4.3: Ejecución de Scripts / LOLBins`)
* **Veredicto Final:** **Benign True Positive (BTP) / Falso Positivo Operativo (Ajuste y Ejecución de Tests QA en Desarrollo Local / Claude Code)**

#### 1. ¿Por qué chilló la consola? (La hipótesis inicial)
La regla conductual de Cortex XDR (`ANALYTICS_BIOC`) alertó sobre la regla *«PowerShell runs suspicious base64-encoded commands»* debido a que `claude.exe` ejecutó `powershell.exe` pasando una cadena en Base64 (`-EncodedCommand ...`) no registrada previamente en los últimos 30 días en la organización. El EDR correlaciona comandos codificados extensos con posibles tácticas de evasión o ejecución ofuscada.

#### 2. Evidencias Clave y Disección Forense
* **Identificación del Proceso Iniciador:**
  * Proceso Iniciador / Padre: `claude.exe` (PID: 30320, SHA256: `bcc6d9117aec30ad9414490302a25414359c871f5647e32e49b055c92bf84e0b`).
  * Ruta: `C:\Users\josetorales\.vscode\extensions\anthropic.claude-code-2.1.289-win32-x64\resources\native-binary\claude.exe`.
  * **Firma Digital del Binario:** Válida y verificada de **`Anthropic, PBC`** (`initiatorsigner: Anthropic, PBC`).
  * Proceso Abuelo / CGO: `C:\Users\josetorales\AppData\Local\Programs\Microsoft VS Code\Code.exe` (Firmado por **`Microsoft Corporation`**).
* **Decodificación Forense del Script Base64:**
  * Al decodificar el payload interno en UTF-8, se evidenció la modificación y lanzamiento de un script de pruebas de autenticación local:
    ```powershell
    $dir = "$env:TEMP\claude\c--Users-josetorales-OneDrive---Technoma-SACI-Documentos-VS\e1e276ab-99be-4e9e-97c7-4e29fe7985d8\scratchpad"
    Set-Location $dir
    (Get-Content qa_plg.mjs) -replace "for \(const user of \['josetorales@dis.com.py', 'admin'\]\)", "for (const user of ['IA'])" | Set-Content qa_plg.mjs -Encoding utf8
    & "$dir\node20\node-v20.18.1-win-x64\node.exe" "C:\Users\josetorales\.claude\skills\browser-automation\browser.mjs" http://localhost:18088/login/ --script .\qa_plg.mjs --timeout 180000 2>&1 | Select-Object -Last 80
    ```
  * Propósito: Modificar el usuario de prueba en el archivo local `qa_plg.mjs` y ejecutar una prueba de login automatizada mediante Node.js sobre el servicio web local `http://localhost:18088/login/`.
* **Comportamiento en Red y Sistema:**
  * Comunicación estrictamente confinada al host local (`http://localhost:18088`), sin conexiones externas maliciosas (`containsfeaturedipaddress: NO`).
  * Sin alteración de configuraciones del sistema operativo ni persistencia.

#### 3. ¿Qué era en realidad? (Causa Raíz)
Operación rutinaria de desarrollo y aseguramiento de calidad (QA): el asistente Claude Code modificando parámetros de prueba locales en `qa_plg.mjs` y corriendo la automatización de login con Node.js en el entorno de José Torales.

#### 4. Justificación Técnica de Cierre (Cortex XDR)
> *"Cerrado como Falso Positivo / BTP. El incidente #148309 'PowerShell runs suspicious base64-encoded commands' en NB-JTORALES (usuario TECHNOMA\josetorales) corresponde a la ejecución legítima del asistente de desarrollo claude.exe (PID 30320, firma válida de Anthropic, PBC) dentro de VS Code. La decodificación del parámetro Base64 reveló la sustitución de cadenas de prueba en el archivo local 'qa_plg.mjs' y la posterior ejecución de un test de login automatizado con Node.js sobre el entorno de desarrollo local en 'http://localhost:18088/login/'. Se descarta actividad C2, persistencia o código malicioso. Caso resuelto como comportamiento operativo conocido."*

#### 5. Acciones y Seguimiento
* [x] **Cortex XDR:** Incidente #148309 cerrado como `Resolved - False Positive` / `Benign`.
* [x] **Bitácora Personal:** Asentado en Caso #011.
* [ ] **Tuning BIOC / Whitelist:** Unificar los incidentes #148341, #148343 y #148309 bajo una misma excepción de tuning para el binario firmado `claude.exe` en la estación de José Torales.

---

<a id="caso-st-dns-tunnel-01"></a>
### Caso ST-DNS-TUNNEL-01 - Falsa Alarma de DNS Tunneling entre Controladores de Dominio (ad / ad2)

* **Fecha/Hora:** `07/10/2026 12:25:35 - 12:34:33` (Hora Local GMT-3) / `2026-10-07 15:25:35 - 15:34:33 UTC`
* **Plataforma:** Stellar Cyber OpenXDR v7.0.0s (Interflow NDR / sensor `technoma-sensor`)
* **Motor / Regla:** `dns_tunnel` ("DNS Tunneling Anomaly" / `new_ml`) | **Severidad:** `98 / High` | **Score:** `46 a 70` | **Tenant:** `Technoma`
* **Activos Afectados:**
  * Origen: `ad.technoma.local` (`10.11.1.1` - Controlador de Dominio Primario / DNS)
  * Destino: `ad2.technoma.local` (`10.11.1.2` - Controlador de Dominio Secundario / DNS)
  * Sensor: `technoma-sensor` (`181.103.4.178`, VLAN 1101, interfaz `ethernet1`)
* **Usuario:** `Infraestructura / Active Directory (Servicio DNS)`
* **Táctica / Técnica MITRE:** `TA0010 - Exfiltration` / `T1048 - Exfiltration Over Alternative Protocol`
* **Playbook Aplicado:** `PB-2.2: Monitoreo Operativo` (y descarte formal de `PB-5.3: Exfiltración de Datos`)
* **Veredicto Final:** **Benign True Positive (BTP) / Falso Positivo Heurístico (Resolución Interna de Active Directory / Réplica DNS entre DCs)**

#### 1. ¿Por qué chilló la consola? (La hipótesis inicial)
El motor de Machine Learning de Stellar Cyber (`new_ml`) disparó un lote de 8 alertas críticas de `dns_tunnel` ("DNS Tunneling Anomaly") alegando un volumen anómalamente alto de tráfico DNS de alta entropía (entre 497 y 776 bytes, frente a una línea base típica de 1 a 29 bytes en ventanas de 5 minutos) entre los dos controladores de dominio (`10.11.1.1` y `10.11.1.2`). El modelo de detección confundió los nombres de endpoints corporativos (`NB-RZABALA`, `NB-ROPORTILLO`, `NB-NSILVA`, `SRV-AZADCONNECT`) como supuestos "payloads de túnel malicioso" exfiltrando información fuera de la red.

#### 2. Evidencias Clave y Disección Forense
* **Flujo y Activos Involucrados:**
  * Ambos hosts son los servidores de Active Directory y DNS autoritativos de la empresa: `ad.technoma.local` (`10.11.1.1`) y `ad2.technoma.local` (`10.11.1.2`).
  * Tráfico puramente interno en la VLAN 1101 a través del puerto UDP 53 (`appid: dns`).
* **Análisis de Consultas y Respuestas (Payloads):**
  * Todas las consultas corresponden a nombres de equipos de dominio de la zona corporativa `technoma.local`:
    - `NB-RZABALA.technoma.local` ➔ Resuelto legítimamente a `192.168.169.25` (TTL: 1200, RCODE: No Error).
    - `SRV-AZADCONNECT.technoma.local` ➔ Resuelto legítimamente a `10.11.1.3` (Servidor de sincronización con Azure AD / Entra ID).
    - `NB-TMARIN.technoma.local` ➔ Resuelto a `192.168.169.62`.
    - `NB-RORTIZ.technoma.local` ➔ Resuelto a `192.168.169.107`.
    - `NB-NOC2.technoma.local` ➔ Resuelto a `192.168.169.34`.
    - `NB-WGONZALEZ.technoma.local` ➔ Resuelto a `192.168.169.39`.
    - `NB-ROPORTILLO.technoma.local` ➔ Resuelto a `192.168.169.80`.
    - `NB-RLLEDO.technoma.local` ➔ Resuelto a `192.168.169.17`.
    - `NB-NSILVA.technoma.local` ➔ Resuelto a `192.168.169.111`.
  * **Sin Exfiltración:** Los supuestos "tunnel payloads" etiquetados por el algoritmo (`NB-ACHAPARRO`, `NB-CGALLARDO`, `NB-MALMADA`, etc.) son simplemente los prefijos estándar de nombres de notebooks corporativas de colaboradores de Technoma.
  * Respuestas RFC1918 íntegras con respuesta inmediata (`processing_time: 0`, flags `34176` de respuesta estándar DNS autoritativa).

#### 3. ¿Qué era en realidad? (Causa Raíz)
Tráfico legítimo de resolución de nombres y sincronización de zona DNS interna de Active Directory entre los dos servidores DNS primario y secundario (`10.11.1.1` y `10.11.1.2`). El modelo ML de Stellar Cyber tiene una línea base hiper-estricta (10 a 25 bytes) para ese canal y malinterpretó consultas legítimas de estaciones de trabajo como túneles de exfiltración.

#### 4. Justificación Técnica de Cierre (Stellar Cyber)
> *"Cerrado como Falso Positivo / BTP. El lote de 8 alertas 'DNS Tunneling Anomaly' entre ad.technoma.local (10.11.1.1) y ad2.technoma.local (10.11.1.2) corresponde al tráfico legítimo de resolución de nombres de Active Directory entre los controladores de dominio corporativos. Las consultas analizadas corresponden a registros tipo A de estaciones de trabajo internas (NB-RZABALA, NB-ROPORTILLO, NB-NSILVA, SRV-AZADCONNECT, etc.), resolviendo exitosamente hacia direccionamiento privado RFC1918 (192.168.169.x / 10.11.1.x) con código No Error. Los supuestos payloads de túnel corresponden a los hostnames estándar de endpoints de la empresa. Se descarta exfiltración, tunelización encubierta y actividad anómala. Caso cerrado sin afectación."*

#### 5. Acciones y Seguimiento
* [x] **Stellar Cyber:** Lote de 8 alertas cerrado como `Closed - False Positive` / `Benign`.
* [x] **Bitácora Personal:** Asentado en Caso #012.
* [ ] **Tuning Stellar Cyber:** Configurar whitelist / regla de supresión en el sensor modular para el tráfico DNS (UDP 53) entre las IPs de los Domain Controllers `10.11.1.1` y `10.11.1.2` para el dominio interno `technoma.local`.

---

<a id="caso-st-dns-tunnel-02"></a>
### Caso #013 (`ST-DNS-TUNNEL-02`) - DNS Tunneling Anomaly (Lote 2: 14 Alertas Correlacionadas entre Domain Controllers)

* **Fecha/Hora:** `07/10/2026 12:35:44 - 12:44:56` (Hora Local Asunción GMT-3) / `15:35:44 - 15:44:56 UTC`
* **Plataforma:** Stellar Cyber OpenXDR v4.3.x (Sensor Modular `technoma-sensor`, VLAN 1101)
* **Motor / Regla:** `new_ml` (`dns_tunnel` / *DNS Tunneling Anomaly*) | **Severidad:** `Critical / High` (98 / Score 46-69)
* **Activo Origen (Cliente DNS):** `ad.technoma.local` (`10.11.1.1` / MAC `00:50:56:af:ff:5a` / Asset ID `31ce6d84-caab-11f0-b1b7-828ad4fe26cd`)
* **Activo Destino (Servidor DNS):** `ad2.technoma.local` (`10.11.1.2` / MAC `00:50:56:af:55:19` / Asset ID `3173e6f2-caab-11f0-b1b7-828ad4fe26cd`)
* **Puerto / Protocolo:** UDP 53 (`appid: 32` - `dns`)
* **Táctica / Técnica MITRE:** `TA0010 - Exfiltration` / `T1048 - Exfiltration Over Alternative Protocol`
* **Playbook Aplicado:** `PB-2.2: Monitoreo Operativo` (Triaje de Falsos Positivos de Red)
* **Veredicto Final:** **Benign True Positive (BTP) / Falso Positivo Heurístico de Machine Learning (Baseline Estrecho)**

#### 1. ¿Por qué chilló la consola? (La hipótesis inicial)
El motor de aprendizaje automático (`new_ml`) de Stellar Cyber disparó un lote consecutivo de 14 alertas de alta severidad (Score 46 a 69, Severidad 98) clasificadas como anomalías de tunelización DNS (*DNS Tunneling Anomaly*). El algoritmo detectó un volumen de bytes por intervalo de 5 minutos (entre 429 y 762 Bytes) superior a la línea base aprendida (`typical: 1 a 24.58 Bytes`), asumiendo erróneamente que los prefijos de las estaciones de trabajo corporativas (ej. `NB-ABURGUENO`, `NB-FKOCHMANN`, `NB-ADIARTE`, `NB-DGODOY`, etc.) correspondían a "cargas útiles de túnel" (*tunnel payloads*) y que la entropía observada (124 a 220) sugería exfiltración encubierta de datos.

#### 2. Evidencias Clave y Disección Forense
* **Topología y Canales Identificados:**
  * Ambos endpoints son los Controladores de Dominio y servidores DNS primario y secundario de Technoma (`10.11.1.1` y `10.11.1.2`), conectados a través de la interfaz troncal `ethernet1` bajo VLAN 1101 (`vlan1101`).
* **Inspección de Consultas y Respuestas (Payload DNS Interflow):**
  * `NB-DAQUINO.technoma.local` ➔ Resuelto a `192.168.169.45` (A record, `No Error`).
  * `SRV-AXENTRIA.technoma.local` ➔ Resuelto a `172.17.10.230` (A record, Servidor de Gestión Documental Axentria, `No Error`).
  * `SRV-AZADCONNECT.technoma.local` ➔ Resuelto a `10.11.1.3` (A record, Servidor de Sincronización Azure AD Connect, `No Error`).
  * `NB-FOLAZAR.technoma.local` ➔ Resuelto a `192.168.169.95` (A record, `No Error`).
  * `NB-PRIQUELME.technoma.local` ➔ Resuelto a `192.168.169.71` (A record, `No Error`).
  * `NB-WGONZALEZ.technoma.local` ➔ Resuelto a `192.168.169.39` (A record, `No Error`).
  * `NB-MSOSA.technoma.local` ➔ Resuelto a `192.168.169.115` (A record, `No Error`).
  * `NB-RORTIZ.technoma.local` ➔ Resuelto a `192.168.169.107` (A record, `No Error`).
  * `NB-ROPORTILLO.technoma.local` ➔ Resuelto a `192.168.169.80` (A record, `No Error`).
  * `wpad.technoma.local` ➔ Respuesta de autoridad SOA `ad2.technoma.local` (`Non-Existent Domain / NXDOMAIN`, comportamiento estándar de descubrimiento automático de proxy en Windows sin WPAD configurado).
  * `NB-RZABALA.technoma.local` ➔ Resuelto a `192.168.169.25` (A record, `No Error`).
* **Ausencia Total de Exfiltración:**
  * Todas las resoluciones pertenecen estrictamente al espacio de nombres autoritativo interno `.technoma.local`.
  * Ninguna petición fue dirigida a servidores DNS externos desconocidos, resolvedores públicos, dominios dinámicos (DGA) ni servidores C2 (`is_dga: pending / dga_score: 0`).
  * Tiempos de procesamiento inmediatos (`processing_time: 0`, flags estándar `34176`).

#### 3. ¿Qué era en realidad? (Causa Raíz)
Tráfico legítimo y continuo de resolución de nombres, reenvío condicional y consultas de estaciones de trabajo Windows / servidores de infraestructura entre los dos controladores de dominio de Active Directory (`ad` y `ad2`). El modelo ML de Stellar Cyber posee un umbral de volumen esperado excesivamente bajo (1 a 24 Bytes por intervalo de 5 minutos), lo que provoca que ráfagas normales de resolución de nombres de red durante el horario laboral activo superen el umbral estadístico y se clasifiquen erróneamente como túneles de exfiltración.

#### 4. Justificación Técnica de Cierre (Stellar Cyber)
> *"Cerrado como Falso Positivo / BTP. El lote de 14 alertas 'DNS Tunneling Anomaly' observadas entre ad.technoma.local (10.11.1.1) y ad2.technoma.local (10.11.1.2) corresponde al tráfico legítimo y operacional de resolución de nombres DNS de Active Directory entre los controladores de dominio corporativos. Las consultas examinadas corresponden a registros tipo A de estaciones de trabajo internas (NB-DAQUINO, NB-FOLAZAR, NB-PRIQUELME, NB-WGONZALEZ, NB-MSOSA, NB-RORTIZ, NB-ROPORTILLO, NB-RZABALA), servidores de infraestructura corporativa (SRV-AXENTRIA, SRV-AZADCONNECT) y consulta estándar de WPAD, resolviendo íntegramente hacia direccionamiento privado RFC1918 (192.168.169.x / 172.17.10.x / 10.11.1.x) con código No Error y TTL estándar. Los supuestos payloads de túnel corresponden a los hostnames estándar de endpoints de la empresa. Se descarta compromiso, exfiltración de información y actividad maliciosa. Caso cerrado sin afectación."*

#### 5. Acciones y Seguimiento
* [x] **Stellar Cyber:** Lote de 14 alertas cerrado como `Closed - False Positive` / `Benign`.
* [x] **Bitácora Personal:** Asentado en Caso #013.
* [ ] **Tuning Stellar Cyber:** Configurar regla de supresión / whitelist en el sensor modular para el tráfico DNS (UDP 53) entre las IPs de los Domain Controllers `10.11.1.1` y `10.11.1.2` para el dominio interno `technoma.local`.

---

<a id="caso-st-smb-cajaande"></a>
### Caso #014 (`ST-SMB-CAJAANDE`) - Falso Borrado y Bloqueo SMB de Ejecutables en Servidor Central (Caja Ande)

* **Fecha/Hora:** `09/10/2026 05:10:00 - 12:30:00` (Hora Local Asunción GMT-3)
* **Plataforma:** Windows Server 2019 / Live Response / Sophos Central / Red SMB
* **Activo Central:** `VMBASE03` (`172.16.201.3` - Windows Server 2019 Build 17763)
* **Puestos Clientes Auditados:**
  * `172.16.202.108` (`CAJAANDE\TIdcaceres`)
  * `172.16.202.105` (`CAJAANDE\Mbrizuela`)
  * `172.16.202.17` (`CAJAANDE\lortellado`)
  * `172.16.202.98` (`CAJAANDE\mcalcena`)
  * `172.16.202.27` (`CAJAANDE\CJPPA1242684`)
* **Archivo Clave:** `\\VMBASE03\Proyectos\EXEC\MODULO_TESORERIA.EXE`
* **Playbook Aplicado:** `PB-2.2: Monitoreo Operativo` / Procedimiento Forense Live Response SMB
* **Veredicto Final:** **Falso Positivo de Seguridad / Incidente Operacional de Concurrencia y Configuración SMB (Sin compromiso ni malware)**

#### 1. ¿Por qué chilló la consola / el usuario? (La hipótesis inicial)
Personal de Caja Ande reportó pánico por presunto ataque de ransomware o borrado automático por antivirus Sophos debido a que los usuarios no podían acceder a `MODULO_TESORERIA.EXE` y Windows arrojaba el mensaje genérico *"el archivo no se encuentra o no está disponible"*.

#### 2. Evidencias Clave y Disección Forense
* **Integridad Física en Disco (VMBASE03):**
  * `MODULO_TESORERIA.EXE` presente en `C:\Proyectos\EXEC\` con tamaño íntegro de 7.27 MB (`7,274,496` bytes) y fecha de modificación original del `17/08/2026`.
* **Descarte de Sophos:** Cero detecciones, cero bloqueos y cero cuarentenas en el visor de eventos Application (`CryptoGuard|Quarantine`).
* **Visibilidad de Red:** `Test-Path "\\VMBASE03\Proyectos\EXEC\MODULO_TESORERIA.EXE"` devolvió `True` desde todas las estaciones de trabajo clientes.
* **Procesos Zombis Retenidos en Memoria:**
  * En `172.16.202.105` (Mbrizuela): 3 instancias de `MODULO_RRHH_V15` abiertas desde el `05/10/2026` reteniendo 21 archivos en el servidor (`NumOpens: 21`).
  * En `172.16.202.17` (lortellado): Módulos corriendo desde el `07/10/2026 16:05` (más de 40 horas continuas en RAM).
  * En `172.16.202.108` (TIdcaceres): `MODULO_PRESTAMO` abierto desde el `08/10/2026 11:59 AM` con 6 archivos retenidos.
* **Causa Raíz de Bloqueo SMB:**
  * La carpeta compartida `Proyectos` tenía `LeasingMode: Full`. Windows Server preservó los identificadores duraderos exclusivos en memoria esperando a los clientes inactivos.
* **Microcortes Locales en Puestos Clientes:**
  * Placas Realtek PCIe GbE con `AllowComputerToTurnOffDevice = Enabled`. Al suspender por batería (ID 42), la tarjeta sufrió error de reactivación NDIS 10317 a las 07:49 AM provocando desconexiones de transporte SMB (30804, 30805, 30807).
  * Al intentar reconectar a la mañana, el servidor rechazó las solicitudes emitiendo el evento operativo 1016 con error `0xC0000034` (`Reconnect durable file / STATUS_OBJECT_NAME_NOT_FOUND`).

#### 3. Acciones de Remediación Ejecutadas y Propuestas
1. Documentación pericial completa con 14 capturas de pantalla de servidor y clientes.
2. Elaboración del informe ejecutivo de 5 párrafos y entrega del informe formal en PDF / Markdown para el cliente.
3. Recomendación de finalizar procesos zombis en clientes (`Stop-Process`).
4. Deshabilitación del ahorro de energía en las placas de red de las notebooks (`Set-NetAdapterPowerManagement -AllowComputerToTurnOffDevice Disabled`).
5. Propuesta técnica en espera de autorización del cliente: Desactivar el arrendamiento exclusivo en el servidor (`Set-SmbShare -Name "Proyectos" -LeasingMode None -Force`).

---

<a id="caso-thn-abuse-batch-01"></a>
### Caso #015 (`THN-ABUSE-BATCH-01`) - Notificación de Abuso a Cloudflare por Lote de 5 IPs Atacantes

* **Fecha/Hora:** `09/10/2026 13:45:00` (Hora Local Asunción GMT-3)
* **Plataforma:** Stellar Cyber OpenXDR / FortiGate FG-Technoma (`FG120GTK24022543`)
* **Activo Afectado:** DMZ Servers Technoma (`190.104.178.146` -> NAT `10.11.3.196:443`)
* **Proveedor Notificado:** Cloudflare Inc. (`abuse@cloudflare.com`, CCO: `Ivan`)
* **IPs Atacantes Notificadas:**
  1. `172.71.232.51` (Francia / Cloudflare AS13335) — Escaneo HTTPS
  2. `172.71.119.91` (Francia / Cloudflare AS13335) — Escaneo HTTPS
  3. `172.71.232.50` (Francia / Cloudflare AS13335) — Escaneo HTTPS
  4. `172.71.127.147` (Francia / Cloudflare AS13335) — Fuerza Bruta HTTPS (ETPro: Brute_Forcer, Threat Score 36)
  5. `104.23.254.12` (EE.UU. / Cloudflare AS13335) — Escaneo HTTPS
* **Playbook Aplicado:** `Playbook Escaneo y Fuerza Bruta` (Plantilla 04 ENG)
* **Veredicto Final:** **True Positive - Blocked (Bloqueado por FortiGate Policy 262 'Block_Countries' / 0 bytes cursados) y Notificado Formalmente**

#### 1. Resumen de Actividad
Lote de conexiones perimetrales hacia el servicio HTTPS en DMZ bloqueadas al 100% en la interfaz WAN (`port2`) del FortiGate por la regla de geobloqueo 262 (`Block_Countries`). Ni una sola conexión ingresó a la red interna (`duration=0, sentbyte=0, rcvdbyte=0`). Stellar Cyber enriqueció la telemetría cruzando la IP `172.71.127.147` con la base de firmas de Proofpoint ETPro catalogándola como nodo activo de fuerza bruta (`Brute_Forcer`).

#### 2. Acciones Ejecutadas
* Generación de notificaciones de abuso en formato bilingüe mediante [abuse_report_dialog.py](file:///c:/Users/kevinmoraes/Documents/soc-env/abuse_report_dialog.py).
* Envío de los 5 correos formales a `abuse@cloudflare.com` con copia oculta a supervisión (`Ivan`) adjuntando los extractos de logs con sellos de tiempo GMT-3.
* Registro permanente de las 5 IPs en la base histórica [Registro_IPs_Reportadas_Abuso.md](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Registro_IPs_Reportadas_Abuso.md) y [registro_ips_reportadas.json](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/registro_ips_reportadas.json).

---

### Caso #GOV-2026-1011 - Creación de Log Filter Quirúrgico DHCP Dahua (Saturación de Cuota & Tráfico local-in FortiGate)

* **Fecha/Hora:** `11/10/2026 13:18:00` (GMT-3)
* **Analista Responsable:** Kevin Moraes
* **Plataforma:** `Stellar Cyber / Fortinet FortiGate (FG-Technoma)`
* **Módulo Afectado:** Log Filters & Ingestion Pipeline (Perfil `profile-modular-sensor-technoma`)
* **Activos:** Cámaras Dahua CCTV (`192.168.16.16`, `192.168.16.3`) ➜ Gateway FortiGate (`192.168.16.1`)
* **Táctica / Técnica MITRE:** `N/A - Tráfico Operativo Benigno / Higiene de Telemetría (Zero Blind Spots)`
* **Veredicto Final:** **Regla Quirúrgica de Supresión de Ingesta Creada y Aplicada con Éxito (0% Ceguera)**

#### 1. ¿Por qué se intervino? (Diagnóstico Forense de la Fuga)
Durante la auditoría forense de ingesta y cuota con el SOAR, se detectó una fuga masiva viva de **4,969 alertas** y cientos de flujos continuos en el Data Lake (`aella-adr-*` y `aella-ser-*`) generados por la cámara Dahua (`192.168.16.16`). El filtro preexistente configurado por Iván Centurión (`filter dahua DNS to AD`) tenía 0 hits y nunca contuvo el tráfico porque filtraba erróneamente consultas DNS hacia Active Directory (`53/UDP` a `10.11.1.1`), mientras que la cámara en realidad estaba inundando el firewall con tráfico DHCP local.

#### 2. Evidencias Clave del Log Extraído
* **Mensaje Crudo de FortiGate:** `<189>date=2026-10-10 time=20:22:19 devname="FG-Technoma" devid="FG120GTK24022543" logid="0001000014" type="traffic" subtype="local" vd="root" srcip=192.168.16.16 srcport=68 srcintf="VLAN16" dstip=192.168.16.1 dstport=67 action="accept" policyid=0 policytype="local-in-policy" service="DHCP" app="DHCP/DHCP Relay"`
* **Causa Raíz:** Renovaciones continuas de DHCP client (`srcport: 68`) dirigidas al gateway FortiGate (`dstip: 192.168.16.1`, `dstport: 67`). Al procesarse bajo `policytype="local-in-policy"` (`policyid=0`), FortiGate emitía un syslog completo por cada transacción, saturando la cuota de licencia diaria.
* **Corrección de Validación de Plataforma:** Stellar Cyber requiere obligatoriamente que el campo `proto` sea numérico IANA (`proto: 17` para UDP). El error inicial devuelto por la UI (*"proto debe ser numérico"*) fue subsanado ingresando el entero `17` en lugar de string.

#### 3. Regla Quirúrgica Aplicada por Kevin Moraes (6 Dimensiones - Cero Ceguera)
Se configuró y envió exitosamente el Log Filter en la plataforma bajo `dev_type: fw_fortigate`:
* **srcip:** `192.168.16.16`, `192.168.16.3`
* **dstip:** `192.168.16.1`
* **srcport:** `68` (number)
* **dstport:** `67` (number)
* **proto:** `17` (number - UDP)
* **appid_name:** `DHCP/DHCP Relay` (string)

#### 4. Justificación de Seguridad SOC
> "La regla no genera puntos ciegos: si la cámara Dahua es vulnerada con malware (Mirai/botnet) e intenta escaneo interno (T1046), movimiento lateral (T1021) o balizamiento C2 a Internet (T1071), dicho tráfico utilizará otras IPs y puertos, ingresando al 100% en Stellar Cyber para análisis y correlación. Solo se descarta la renovación local de IP entre la cámara y su router."

---

<a id="caso-gov-2026-1012"></a>
### Caso #GOV-2026-1012 - Detección y Diagnóstico de Ruido Zabbix Agent Polling (TCP 10050) & Telemetría

* **Fecha/Hora:** `11/10/2026 13:49:00` (GMT-3)
* **Analista Responsable:** Kevin Moraes
* **Plataforma:** `Stellar Cyber / Fortinet FortiGate (FG-Technoma)`
* **Módulo Afectado:** Log Filters & Ingestion Pipeline / Sondeo de Agentes
* **Activos:** Servidor Zabbix (`192.168.15.31`) ➜ Clientes / Agentes de Monitoreo Internos (`10.0.0.0/8`, `192.168.0.0/16`)
* **Táctica / Técnica MITRE:** `N/A - Monitoreo Operativo Autorizado / Diagnóstico de Ruido`
* **Veredicto Final:** **En Seguimiento — Detectado y Diagnosticado (Pendiente de Aprobación de Jefatura, Sin Aplicar en Producción)**

#### 1. Diagnóstico Forense y Detección
Durante la auditoría del clúster de Stellar Cyber, el analista Kevin Moraes identificó alertas recurrentes del servidor Zabbix (`192.168.15.31`) bajo el evento `fw_policy_id` al consultar hosts de la red interna (ej. `10.40.2.6`) en el puerto de agente TCP 10050 con aplicación `tcp/10050`. Se constató que los filtros previos no contemplaban esta telemetría de forma quirúrgica.

#### 2. Propuesta Técnica Formulada (5 Dimensiones)
Se diseñó la especificación técnica de mitigación para evaluación con la jefatura:
* **dev_type:** `fw_fortigate`
* **srcip:** `192.168.15.31`
* **dstip:** `10.0.0.0/8`, `192.168.0.0/16`
* **dstport:** `10050` (number)
* **proto:** `6` (number - TCP)
* **appid_name:** `tcp/10050` (string)

#### 3. Estado Operativo y Decisión del Analista
> **NOTA DE CONTROL SOC:** El analista **NO aplicó modificaciones ni remediaciones en producción** sobre el servidor Zabbix. El caso se mantiene formalmente en estado **EN SEGUIMIENTO** para presentar los hallazgos y la propuesta técnica a la Jefatura del SOC / Ivan Centurión para su validación previa.

---

<a id="caso-gov-2026-1013"></a>
### Caso #GOV-2026-1013 - Remediación Quirúrgica de Filtro WUDO 7680 (Cero Ceguera SOC)

* **Fecha/Hora:** `11/10/2026 14:10:00` (GMT-3)
* **Analista Responsable:** Kevin Moraes
* **Plataforma:** `Stellar Cyber / Fortinet FortiGate (FG-Technoma)`
* **Nombre del Filtro:** `Drop_FW_Denial_Internal_WUDO_7680` (Filtro #64)
* **Módulo Afectado:** Log Filters & Ingestion Pipeline
* **Activos:** VLANs de Endpoints / Usuarios (`192.168.169.0/24`, `192.168.100.0/24`)
* **Táctica / Técnica MITRE:** `TA0011 - Command and Control` / `T1046 - Network Service Discovery` / `T1021 - Remote Services`
* **Veredicto Final:** **Filtro Reconfigurado con 5 Dimensiones Estrictas (Punto Ciego Eliminado al 100%)**

#### 1. Diagnóstico Forense del Riesgo Previo (Filtro #64 Genérico)
El filtro original contenía únicamente `action: deny`, `dstport: 7680` y `srcip: 192.168.0.0/16` sin especificar dispositivo, protocolo ni destino (`dstip`). Esto generaba un punto ciego crítico: cualquier intento de comunicación de malware hacia servidores C2 en Internet sobre el puerto 7680 denegado por el firewall, o escaneos laterales hacia Controladores de Dominio y servidores de producción, era silenciado en la ingesta del SIEM.

#### 2. Regla Quirúrgica Aplicada por Kevin Moraes (5 Dimensiones)
Se reconfiguró en la plataforma Stellar Cyber bajo `dev_type: fw_fortigate`:
* **action:** `deny` (string `==`)
* **dstport:** `7680` (number `==`)
* **proto:** `6` (number `==` TCP)
* **srcip:** `192.168.169.0/24`, `192.168.100.0/24` (subredes reales de puestos de trabajo)
* **dstip:** `192.168.169.0/24`, `192.168.100.0/24` (estrictamente destinos peer-to-peer autorizados)

#### 3. Justificación de Seguridad SOC
> "La regla elimina la ceguera por completo: solo se descartan las denegaciones inter-VLAN de tráfico P2P legítimo de Windows Update entre notebooks de usuario. Si una máquina intenta conectarse por el puerto 7680 a cualquier IP pública en Internet (C2) o a servidores corporativos/DCs, el evento ingresa intacto al Data Lake de Stellar Cyber para correlación y alertas."

---

<a id="caso-sac-2026-1007"></a>
### Caso #SAC-2026-1007 - Despliegue de Regla de Alerta Automatizada en SAC (THN FW Ataque Recurrente a DMZ)

* **Fecha/Hora:** `07/10/2026 13:30:00` (Hora Local GMT-3)
* **Analista Responsable:** Kevin Moraes
* **Plataforma:** `Stellar Cyber / System Action Center (SAC)`
* **Nombre de la Regla:** `THN FW Ataque Recurrente a DMZ`
* **Tipo de Regla:** `Query` (Índice: `Traffic`)
* **Activo Protegido:** Servidor DMZ DigitalCert (`190.104.178.146` / `digitalcert.technoma.com.py`)
* **Táctica / Técnica MITRE:** `TA0011 - Command and Control` / `T1190 - Exploit Public-Facing Application` / `T1110 - Brute Force`
* **Playbook Aplicado:** `Playbook Escaneo y Fuerza Bruta` / `PB-2.2: Monitoreo Operativo`
* **Veredicto Final:** **Regla Automatizada Creada, Testeada y Activa en Producción**

#### 1. Diagnóstico y Objetivo Operativo
Ante los continuos escaneos y ráfagas de fuerza bruta observados desde Internet contra la infraestructura expuesta en DMZ (`190.104.178.146`), se requería un mecanismo de respuesta rápida y correlación en tiempo real que notificara al equipo SOC de ráfagas masivas antes de que deriven en denegación de servicio o explotación exitosa, permitiendo el bloqueo expedito en FortiGate.

#### 2. Configuración Técnica en System Action Center (SAC)
* **Frecuencia de Evaluación:** Intervalo cada **5 minutos** sobre todos los tenants seleccionados.
* **Índice Auditado:** `Traffic`.
* **Criterios de Búsqueda (Query: FortiGate - Deny DigitalCert DMZ):**
  * `msg_class`: `firewall`
  * `action`: `deny`
  * `dstip_host`: `190.104.178.146`
* **Condición de Disparo (`Umbral_50_Hits`):**
  * Tipo: Compare Value (Total Hits).
  * Operador: `is greater than or equal to 50` (>= 50 intentos denegados en 5 min).
* **Acciones Automatizadas:**
  * **Email:** Notificación de alta prioridad (`High`) con Interflow incluido.
    * Asunto: `[SOC ALERTA] Posible ataque de escaneo o fuerza bruta a DMZ`
    * Cuerpo: `ALERTA AUTOMÁTICA DEL SOC: Se ha detectado una ráfaga superior a 50 intentos de conexión denegados en 5 minutos contra el servicio digitalcert.technoma.com.py.`
  * **Create Alert:** Generación de alerta en la consola de Stellar Cyber para triaje de IP de origen y bloqueo perimetral.
  * **Mute Override:** Silenciamiento temporal habilitado por **1 hora** tras disparo para prevenir saturación de notificaciones.

#### 3. Justificación de Seguridad y Valor Operativo
> "Esta regla automatizada reduce el tiempo medio de detección (MTTD) ante ataques de escaneo perimetral y fuerza bruta contra servicios DMZ de Technoma. Al correlacionar ráfagas >= 50 hits denegados en 5 minutos, el SOC recibe la alerta temprana con el listado de IPs atacantes e Interflow para proceder al baneo perimetral inmediato y envío de reportes de abuso."

---

## 📋 Registros Oficiales de Cierre de Turno / Guardia (18 Columnas TSV)

### 1. Guardia Domingo (11/10/2026) — Remediación WUDO/Dahua & Zabbix [EN SEGUIMIENTO]
* **Fila TSV Oficial:**
```tsv
11/10/2026 14:25:00	Kevin Moraes	Caja Ande, Technoma	N/A	Cierre de Turno	N/A	Informativo	Cierre de Turno Guardia Domingo	Guardia Domingo - Remediación Filtros WUDO/Dahua y Zabbix (En Seguimiento)	Infraestructura Technoma y CAJA ANDE	"Monitoreo de guardia Technoma y CAJA ANDE sin incidentes activos. Se corrigió en producción el filtro de cámaras Dahua (DHCP) y el filtro WUDO (puerto 7680) eliminando puntos ciegos. Se detectó ruido por sondeo del servidor Zabbix (puerto 10050), el cual queda en seguimiento sin aplicar en producción para validar con jefatura."	"Consolas en verde sin alertas abiertas. Filtros de Dahua y WUDO 7680 actualizados y verificados en clúster. Caso Zabbix en seguimiento para reunión con jefatura."	Revisar propuesta de filtro Zabbix con jefatura	En Seguimiento	N/A	NO	N/A	PB-2.2: Monitoreo Operativo
```

### 2. Guardia Sábado (10/10/2026) — Auditoría de Ingesta & Puntos Ciegos
* **Fila TSV Oficial:**
```tsv
10/10/2026 14:00:00	Kevin Moraes	Caja Ande, Technoma	N/A	Cierre de Turno	N/A	Informativo	Cierre de Turno Guardia Sábado	Guardia Sábado - Auditoría de Ingesta Stellar y Análisis de Puntos Ciegos	Infraestructura Technoma y CAJA ANDE	"Monitoreo de guardia Technoma y CAJA ANDE sin incidentes activos. Se auditó la ingesta del clúster de Stellar Cyber (~16 GB/día) aislando el consumo en logs de FortiGate y bucle DNS de Grafana. Se auditaron los 65 filtros de la plataforma detectando reglas con riesgo de ceguera."	"Consolas en verde sin alertas abiertas. Informes técnicos de causa raíz y plan maestro de reducción de cuota emitidos."	N/A	Cerrado	N/A	NO	N/A	PB-2.2: Monitoreo Operativo
```

### 3. Turno Mañana (07/10/2026) — Regla Especial SAC DMZ & Triaje
* **Fila TSV Oficial:**
```tsv
07/10/2026 14:00:00	Kevin Moraes	Caja Ande, Technoma	N/A	Cierre de Turno	N/A	Informativo	Cierre de Turno Mañana	Reporte de Cierre de Turno Mañana - Technoma y Caja Ande (Regla SAC Ataque Recurrente DMZ)	Infraestructura general Technoma / Endpoints y Servidores CAJA ANDE / DMZ DigitalCert (190.104.178.146)	"REPORTE SOC - TURNO MAÑANA [06:00 a 14:00]. Monitoreo continuo de consolas sobre Tenants Technoma y CAJA ANDE. Descarte de falsos positivos de rutina. Sin anomalías ni incidentes activos durante el periodo. Triaje de casos Cortex XDR #148379, #148359, #148460 y Stellar Cyber ST-DNS-TUNNEL cerrados como BTP. Despliegue de regla automatizada 'THN FW Ataque Recurrente a DMZ' en System Action Center (Umbral 50 hits/5 min)."	"Stellar Cyber / Cortex XDR / Sophos Central: Consolas en estado VERDE sin alertas abiertas para Technoma y CAJA ANDE. Regla 'THN FW Ataque Recurrente a DMZ' guardada, habilitada y testeada en SAC. Monitoreo de telemetría normal."	N/A	Cerrado	N/A	NO	N/A	PB-2.2: Monitoreo Operativo
```

---

## 📋 Plantilla en Blanco para Nuevos Casos







*(Copiar y pegar esta plantilla al final del documento para cada nuevo caso analizado)*

```markdown
---

### Caso #[ID_CASO] - [Título Descriptivo del Caso]

* **Fecha/Hora:** `[DD/MM/AAAA HH:mm:ss]`
* **Plataforma:** `[Cortex XDR / Stellar Cyber / Sophos / FortiGate]`
* **Motor / Regla:** `[Nombre de la regla o firma]` | **Severidad:** `[Baja / Media / Alta / Crítica]`
* **Activo Afectado:** `[Hostname]` (`[IP]`)
* **Usuario:** `[Dominio\Usuario]`
* **Táctica / Técnica MITRE:** `[TAXXXX - Nombre / TXXXX - Nombre]`
* **Playbook Aplicado:** `[PB-X.X: Nombre del Playbook]`
* **Veredicto Final:** `[Falso Positivo (FP) / Benign True Positive (BTP) / True Positive (TP)]`

#### 1. ¿Por qué chilló la consola? (La hipótesis inicial)
[Breve explicación en 2 o 3 líneas de qué vio la plataforma y por qué consideró sospechoso el evento].

#### 2. Evidencias Clave y Disección Forense
* **Proceso / Binario:** `[nombre.exe]` (SHA256: `[...]`) | WildFire/VirusTotal: `[...]`.
* **Ruta de Ejecución:** `[...]`.
* **Árbol de Procesos:** `[padre.exe] ➔ [hijo.exe]`.
* **Destino / Red:** `[IP:Puerto]` (`[Dominio/FQDN]`) | Tráfico: `[Subida / Bajada]`.

#### 3. ¿Qué era en realidad? (Causa Raíz)
[Explicación real de lo que estaba ocurriendo en el equipo o en la red].

#### 4. Justificación Técnica de Cierre
> "[Texto exacto de justificación técnica utilizado para cerrar la alerta en la consola]"

#### 5. Acciones y Seguimiento
* [x] Alerta/Caso cerrado en consola.
* [ ] Acciones pendientes con cliente o Helpdesk (si aplica).
### Caso 016 - Auditoría de Log Filters: Reglas Inoperativas vs Reglas Corregidas (WUDO 7680 y Dahua CCTV)
* **ID Interno:** `THN-AUDIT-FILTERS-01`
* **Fecha:** 14/10/2026 08:42:00
* **Plataforma:** Stellar Cyber OpenXDR v7.0.0s / FortiGate `FG-Technoma`
* **Analista:** Kevin Moraes
* **Activos:** Sensor `technoma-sensor`, Domain Controller `10.11.1.2` (`ad2.technoma.local`), Servidor Helpdesk `192.168.169.44`, Cámara Dahua `192.168.16.16` (`VLAN16`), Subredes LAN/WiFi (`192.168.169.0/24`, `192.168.100.0/24`).
* **Veredicto:** **Tuning Quirúrgico L7 & Eliminación de Ceguera Operativa**
* **Playbook:** `Playbook 6.3 - Log Filtering and Ingestion Control`

#### 1. Contexto y Objetivos Operativos
Durante la guardia del 14/10/2026 se auditó el inventario de 67 reglas de `log_filters` en Stellar Cyber para mitigar el desbordamiento de cuota diaria (170.5% del pozo global). Se identificaron dos reglas críticas que **no estaban funcionando (inoperativas por error de sintaxis / puertos)** y se corrigieron con filtros quirúrgicos en 3 dimensiones sin causar ceguera en el SOC.

---

#### 2. REGLA 1: WUDO (Windows Update Delivery Optimization - Puerto 7680)

##### ❌ Regla Antigua (Por qué NO funcionaba / 0 Hits):
* **Filtro Original:** Se intentaba silenciar el ruido P2P de Windows Update usando reglas genéricas o vinculando el descarte a alias de texto en `fw_policy_id` (ej. `"Block_Countries"` o texto alfanumérico) o a un protocolo sin acotar:
  * El sensor modular de Stellar Cyber compara identificadores de política como números enteros (`uint`). Al recibir strings, el evaluador jamás hacía match.
  * Los broadcasts y denegaciones TCP 7680 entre estaciones de trabajo (`192.168.169.0/24` y `192.168.100.0/24`) seguían saturando la ingesta diaria con miles de eventos denegados.

##### ✅ Regla Nueva / Corregida (La que SÍ funciona ahora):
* **Nombre:** `Drop_FW_Denial_Internal_WUDO_7680`
* **Sintaxis JSON Quirúrgica Aplicada:**
  ```json
  {
    "action": {"type": "string", "op": "==", "value": ["deny"]},
    "dstport": {"type": "number", "op": "==", "value": [7680]},
    "proto": {"type": "number", "op": "==", "value": [6]},
    "srcip": {"type": "ip", "op": "matches", "value": ["192.168.169.0/24", "192.168.100.0/24"]},
    "dstip": {"type": "ip", "op": "matches", "value": ["192.168.169.0/24", "192.168.100.0/24"]}
  }
  ```
* **Evaluación de Ceguera:** **CERO CEGUERA**. Solo silencia denegaciones (`deny`) de tráfico P2P entre puestos de trabajo en el puerto específico 7680/TCP. Si un equipo intenta movimiento lateral en SMB (445), RDP (3389) o SSH (22), es 100% visible.

---

#### 3. REGLA 2: Dahua CCTV a Domain Controller (Anomalía de Bloqueo DNS)

##### ❌ Regla Antigua (Por qué NO funcionaba / 0 Hits contra la anomalía):
* **Nombre del Filtro Existente:** `filter dahua DNS to AD` (creado por `ivancenturion@technoma.com.py`).
* **Definición Antigua en Consola:**
  ```json
  {
    "srcip": {"op": "matches", "value": ["192.168.16.16", "192.168.16.3"]},
    "dstip": {"op": "matches", "value": ["192.168.16.1"]},
    "dstport": {"op": "==", "value": [67]},
    "srcport": {"op": "==", "value": [68]},
    "proto": {"op": "==", "value": [17]},
    "appid_name": {"op": "==", "value": ["DHCP/DHCP Relay"]}
  }
  ```
* **Causa del Fallo:** A pesar de llamarse *"filter dahua DNS to AD"*, la regla tenía configurados los puertos **67/68 (DHCP)** y destino `192.168.16.1`. 
* **Impacto Operativo:** La cámara Dahua (`192.168.16.16`, `AF0A18DPAGB9E8D`) enviaba ráfagas continuas de **200 a 405 consultas DNS por intervalo de 5 minutos** dirigidas al Domain Controller `10.11.1.2:53` (`ad2.technoma.local`), siendo bloqueada por la política 0 (Implicit Deny) del FortiGate y detonando la anomalía de Machine Learning `internal_fw_action` (`Internal Firewall Denial Anomaly`, fidelidad 98-99%). El filtro antiguo jamás descartaba un solo paquete de este ruido porque no filtraba el puerto 53 ni el DC.

##### ✅ Regla Nueva / Corregida (La que SÍ funciona ahora):
* **Nombre:** `Drop_FW_Denial_Internal_CCTV_Dahua_DNS_DC`
* **Sintaxis JSON Quirúrgica Aplicada:**
  ```json
  {
    "action": {"type": "string", "op": "==", "value": ["deny"]},
    "dstport": {"type": "number", "op": "==", "value": [53]},
    "proto": {"type": "number", "op": "==", "value": [17]},
    "srcip": {"type": "ip", "op": "matches", "value": ["192.168.16.16", "192.168.16.3"]},
    "dstip": {"type": "ip", "op": "matches", "value": ["10.11.1.2"]}
  }
  ```
* **Evaluación de Ceguera:** **CERO CEGUERA**. Solo descarta el syslog de denegación de resolución de nombres de la cámara hacia el DC. Si la cámara llega a ser comprometida e intenta un ataque de fuerza bruta, escaneo de red o propagación lateral, el evento será alertado inmediatamente en Stellar Cyber.
* **Acción de Fondo:** Solicitar formalmente a Infraestructura reasignar el DNS del pool DHCP de `VLAN16` hacia el gateway local o forwarders públicos para apagar el tráfico residual en el FortiGate.

---

#### 4. REGLA 3 (Extra): Helpdesk (`Ruido_servidor_helpdesk`)
* **Regla:** `srcip: 192.168.169.44` | `appid_name: PING` | `dstip: 10.49.70.0/24, 10.49.71.0/24`
* **Auditoría:** Se comprobó que el filtro **SÍ funciona** acumulando **70,970 hits (157.58 MB)**. El módulo del Cockpit marcaba falso positivo porque asumía que `PING` no existía en Interflow, cuando en realidad el parser Syslog de FortiGate mapea `service="PING"` directamente a `appid_name="PING"`. Se corrigió el código del Cockpit.

---

### Caso 017 - Contención de Cuota Stellar: Pre-DPI BPF contra Flood DNS de Grafana
* **ID Interno:** `THN-INGEST-GRAFANA-01`
* **Fecha:** 14/10/2026 11:55:00
* **Plataforma:** Stellar Cyber OpenXDR v7.0.0_023bdc1 / NDR Modular Sensor en Linux (`ubuntu-22.04` QEMU)
* **Analista:** Kevin Moraes
* **Activos Involucrados:**
  - Sensor Modular: `technoma-sensor` (`192.168.15.70`, interfaz espejo `ethernet1`)
  - Servidor Grafana NOC: `192.168.15.23`
  - Servidor Zabbix Backend: `192.168.15.31` (`zbx.technoma.com.py`)
  - Domain Controllers / DNS: `10.11.1.1` (`ad.technoma.local`), `10.11.1.2` (`ad2.technoma.local`)
* **Veredicto Final:** **Resolución Técnica / Rescate de Cuota de Licencia**
* **Playbook Aplicado:** `Playbook 6.3 - Ingestion Control and Pre-DPI Optimization`

#### 1. Contexto y Problema Crítico de Compliance
La plataforma Stellar Cyber OpenXDR registraba una violación crítica de cumplimiento de cuota de servicio (*"Violation : System is out of compliance due to continuous daily usage violations for over 21 days"*). El Tenant `technoma` operaba en un rango de 14 a 17 GB/día superando el pozo contratado de 8 GB/día.
La auditoría volumétrica en Interflow Search detectó que una sola máquina (`192.168.15.23`, servidor Grafana del NOC) generaba ráfagas constantes de **~19 consultas DNS por segundo** resolviendo el FQDN `zbx.technoma.com.py` hacia los Domain Controllers de Active Directory, sumando más de **1.760.000 eventos diarios y ~2.88 GB/día** de sobreingesta pura.

#### 2. Causa Raíz y Falla del Motor Pre-DPI Preexistente
Al auditar el perfil del sensor (`profile-modular-sensor-technoma`), se constató que ninguna de las 13 reglas históricas de Pre-DPI estaba descartando paquetes:
1. **Falla Atómica de `pcap_compile()` (PCAP_ERROR -1):** Conforme al estándar BPF (`pcap_compile(3PCAP)`), el motor de Stellar Cyber concatena todas las líneas del perfil con el operador lógico `OR` en un único string. La lista contenía 5 reglas con errores léxicos (`tcp 1500` en vez de `tcp port 1500`, `dst <ip>` sin la palabra clave `host`, y combinaciones ilógicas `host A and host B`). Un solo error de sintaxis causaba el fallo atómico del compilador eBPF, obligando al sensor `aella_flow` a operar en modo *fallback* (*accept all packets*), permitiendo el ingreso indiscriminado de todo el tráfico.
2. **Encapsulamiento 802.1Q (VLAN 1101):** El tráfico físico espejo entra etiquetado con VLAN 1101. En el motor eBPF de libpcap, las reglas deben respetar el formato sin mezclas arbitrarias de desplazamientos de capa de enlace.

#### 3. Implementación de la Solución Quirúrgica
1. **Respaldo:** Se generó el documento de resguardo `Respaldo_Reglas_PreDPI_Stellar.md` con las 15 reglas originales y su corrección formal.
2. **Aislamiento en Pre-DPI (`Action: Drop`):** Se cargó la sintaxis stateless bidireccional pura indicada en la documentación oficial de Stellar Cyber para tráfico pass-through:
   ```text
   src host 192.168.15.23 and dst port 53
   src port 53 and dst host 192.168.15.23
   ```
3. **Eficacia Comprobada:**
   - La regla se sincronizó a las **11:43:40**.
   - El volumen en la ventana de 15 minutos cayó inmediatamente de 12.890 a 6.508 eventos.
   - **0 eventos nuevos** recibidos en Interflow durante más de 12 minutos de monitoreo continuo.

#### 4. Recomendación Definitiva de Arquitectura (NOC / Infraestructura)
Para evitar depender de filtros de red en el futuro:
- En la interfaz web de Grafana (`http://192.168.15.23:3000`), configurar el datasource de Zabbix para apuntar a la IP directa local `http://192.168.15.31/zabbix/api_jsonrpc.php` o habilitar el servicio de caché DNS local (`systemd-resolved`) en el host Linux de Grafana para que las consultas se resuelvan en memoria sin impactar la red.

---

### Caso 018 - Acceso Legítimo a protected_storage en VMBASE8 (Windows DPAPI)
* **ID de Alerta / Caso:** `32592` (Alertas correlacionadas `32592`, `32593`, `32594`)
* **Fecha:** 15/10/2026 08:32:00
* **Plataforma:** Stellar Cyber OpenXDR v7.0.0s / Agente Windows Winlogbeat (`VMBASE8`)
* **Analista:** Kevin Moraes
* **Activos Involucrados:**
  - Servidor Destino: `VMBASE8` (`172.16.201.8`, Windows Server 2019 Standard, DC Secundario CAJAANDE)
  - Estación de Trabajo Origen: `172.16.202.9`
  - Usuario: `CAJAANDE\Ktroche` (SID: `S-1-5-21-4088095093-1662279969-3535480394-1731`)
* **Regla Disparada:** `windows_security_sensitive_networkshare` (`windows_security_152` / `Detailed File Share`)
* **Técnica MITRE:** T1021.002 (SMB/Windows Admin Shares) / TA0008 (Lateral Movement)
* **Veredicto Final:** **Falso Positivo (Benign True Positive - BTP)**
* **Playbook Aplicado:** `PB-5.2: Triaje Forense de Alertas / PB-1.1: Control de Identidades`

#### 1. Contexto y Descripción del Incidente
Stellar Cyber disparó 3 alertas con severidad 75 catalogadas como *Sensitive Windows Network Share File or Folder Accessed* sobre el servidor `VMBASE8` (`172.16.201.8`), advirtiendo un potencial abuso de DPAPI (*Domain DPAPI Backup Key Extraction*) para robar claves maestras de cifrado desde los controladores de dominio.

#### 2. Evidencia Forense Extraída de Interflow (Event ID 5145)
* **Evento Windows:** `5145` (*Detailed File Share*)
* **Recurso Compartido:** `ShareName: \\*\IPC$`
* **Objeto Relativo:** `RelativeTargetName: protected_storage`
* **Máscara de Acceso:** `0x12019f` (Read/Write/Sync estándar de cliente RPC)
* **Resultado:** `outcome: success` / `Auditoría correcta`
* **Proceso Originador:** `process_id: 4` (`System` / `lsass.exe`)

#### 3. ¿Qué era en realidad? (Causa Raíz)
Conforme a la Memoria Institucional del SOC (`SOC_GEM_v2.md`), el acceso a `protected_storage` a través de `IPC$` hacia `VMBASE8` es un comportamiento intrínseco y por diseño de Active Directory. Cuando un usuario de dominio (`Ktroche`) inicia sesión o renueva credenciales en su estación de trabajo (`172.16.202.9`), el subsistema DPAPI del sistema operativo Windows realiza de forma transparente una llamada RPC autenticada al DC para respaldar y custodiar la clave maestra de cifrado del usuario. No existe presencia de ejecutables ofensivos (Mimikatz, SharpDPAPI) ni anomalías de proceso.

#### 4. Justificación Técnica de Cierre
> "Se analizó el lote de eventos de auditoría de seguridad de Windows (Event ID 5145) registrados sobre el Controlador de Dominio secundario VMBASE8 (172.16.201.8). La interacción con el recurso compartido IPC$ y el objeto protected_storage por parte del usuario Ktroche (CAJAANDE\Ktroche) desde la estación 172.16.202.9 corresponde al comportamiento benigno y estándar de Microsoft Windows Data Protection API (DPAPI), el cual efectúa de forma periódica el respaldo de las claves maestras de cifrado de usuario hacia el KDC. La auditoría confirma que la operación concluyó exitosamente bajo privilegios estándar de sesión, sin indicios de manipulación o extracción maliciosa de credenciales (T1021.002)."

#### 5. Conclusión y Cierre
* [x] Análisis forense completado: descartada extracción ofensiva o abuso de credenciales.
* [x] Causa raíz atribuida al comportamiento legítimo de Windows DPAPI contra el DC.
* [x] Caso cerrado como Falso Positivo (Benign True Positive) en la consola de Stellar Cyber.

---


---

### Caso 019 - Investigación Forense Cortex XDR: Carga a Proton Drive (NB-FMORA)
* **ID / Referencia:** Alerta Cortex Magnifier / DLP & Upload Anomaly
* **Fecha:** 15/10/2026 09:15:00
* **Plataforma:** Palo Alto Networks Cortex XDR (Magnifier + Endpoint Agent)
* **Analista:** Kevin Moraes
* **Activo Involucrado:** `NB-FMORA` (Notebook corporativa - Fabio Mora)
* **Destino Remoto:** `fra-storage.proton.me` (`185.205.70.10`, Frankfurt - Proton AG)
* **Volumen:** 10.2 GB (608 sesiones HTTPS / TLS en puerto 443)
* **Veredicto Final:** **Uso No Autorizado de Herramienta Cloud / Sin Fuga de Información Sensible (Benigno)**

#### 1. Contexto y Detección
Cortex XDR Magnifier alertó sobre un volumen inusual de carga de datos (10.2 GB) desde el endpoint `NB-FMORA` hacia la nube de almacenamiento de Proton Drive durante el fin de semana del 12-13 de octubre.

#### 2. Evidencia Forense Recabada (Consultas Cortex XQL)
1. **Actividad de Proceso y Carpeta Local:**
   - La consulta XQL sobre el endpoint confirmó la ejecución de `ProtonDrive.exe` (`C:\Users\fabiomora\AppData\Local\Proton\ProtonDrive\`).
   - El usuario configuró como carpeta local de sincronización `Downloads\Mis cosas\`.
2. **Conciliación de Datos (10.2 GB):**
   - El análisis del sistema de archivos local evidenció imágenes ISO y máquinas virtuales OVA (laboratorios de sistemas operativos para estudio técnico).
   - El peso total de dichos archivos totalizó exactamente 10.2 GB, cuadrando 1 a 1 con la telemetría de red de Magnifier.
3. **Evidencia de Configuración de Cuenta:**
   - Se localizó el archivo `proton-recovery-phrase.pdf` (frase de recuperación generada por Proton al crear la cuenta) depositado el 13/10 a las 06:18 AM en la misma carpeta.
4. **Validación Operativa:**
   - Se verificó con personal de Helpdesk que el usuario se encuentra estudiando activamente para certificaciones técnicas, lo que motivó el respaldo personal de sus laboratorios. No hubo compromiso de credenciales corporativas ni exfiltración de bases de datos/documentos de la empresa.

---

### Caso 020 - Optimización de Cuota Stellar Cyber: Log Filter Quirúrgico FortiGate WiFi
* **ID de Casos Asociados:** Casos #16302 (4.116 alertas) y #12661 (10 alertas)
* **Fecha:** 15/10/2026 09:50:00
* **Plataforma:** Stellar Cyber OpenXDR v7.0.0s / Fortinet FortiGate (`FG-Technoma`)
* **Analista:** Kevin Moraes
* **Tipo de Alerta:** `External Firewall Denial Anomaly` (Etapa Kill Chain: *Initial Attempts*)
* **Activos Involucrados:** Subred WiFi Corporativa (`192.168.169.102`, `192.168.169.131` en `WiFi_Corp`)
* **Veredicto Final:** **Falso Positivo / Ruido Operativo de Firewall (Benigno)**

#### 1. Diagnóstico y Causa Raíz
Dispositivos conectados a la red `WiFi_Corp` intentaban resolver nombres y sincronizar servicios de seguridad hacia resolvers públicos (Google DNS) y la nube de FortiGuard. La política de seguridad del firewall (`Block_WIFI-Corp`, ID 214) denegó estas salidas, generando miles de logs de descarte (`action: deny`) que saturaron la ingesta de Stellar Cyber e inflaron la cuota diaria (caso 16302 con más de 4.100 eventos).

#### 2. Implementación de Mitigación e Ingestión en Stellar Cyber
Para erradicar el ruido masivo y reducir el sobreconsumo de almacenamiento diario de la licencia, se crearon los siguientes filtros de descarte en **System → Log Forwarders (Log Filters)**:

1. **Filtro Inicial de Descarte DNS 53:**
   * **Nombre:** `Drop_FW_Denial_WiFiCorp_DNS_53`
   * **Definición JSON:**
     ```json
     {"fw_policy_id":{"type":"string","op":"==","value":["FG-Technoma_214"]},"dstport":{"type":"number","op":"==","value":[53]},"action":{"type":"string","op":"==","value":["deny"]}}
     ```
   * **Acción:** `DROP` (descarta denegaciones de resolución estándar en puerto 53 de la regla 214).

2. **Filtro Quirúrgico Multipuerto y Destinos Benignos (Sin Puntos Ciegos):**
   * **Nombre:** `DROP-FG-Technoma-WIFI_Corp-Known-Public-DNS`
   * **Condiciones Aplicadas:**
     - `fw_policy_id` **is** `FG-Technoma_214`
     - `dstport` **is** `53, 853, 443` (DNS estándar, DNS-over-TLS y telemetría/firmas FortiGuard)
     - `dstip` **matches** `96.45.46.46, 96.45.45.45, 173.243.140.18, 173.243.132.25, 173.243.143.6, 141.109.161.95, 8.8.8.8, 8.8.4.4`
     - `action` **is** `deny`
   * **Acción:** `DROP` (neutraliza casos masivos como el #16302 y #12661 preservando detección ante C2 o DNS tunneling a IPs no autorizadas).

#### 3. Impacto Operativo
* Se neutraliza la generación de casos falsos masivos derivados de la política WiFi corporativa.
* Se preserva el almacenamiento diario de la licencia Stellar Cyber.
* Se garantiza visibilidad total: cualquier intento de conexión hacia IPs no listadas (malware, C2) sigue siendo capturado y alertado con normalidad.


---

### Caso 021 - Cierre de Incidente THN-SOC-102 (Zabbix LDAP Mario Flores) y Estandarización FL-THN-POS-01
* **ID Oficial de Ticket:** `THN-SOC-102` (Formulario `FL-THN-POS-01 Rev. 03` - Fila 16)
* **Fecha y Hora de Apertura:** 14/10/2026 13:50:00
* **Fecha y Hora de Resolución / Cierre:** 15/10/2026 09:56:00
* **Tiempo de Resolución:** **19.7 horas** (19 h 39 min) — **Cumplió SLA: Sí** (Prioridad P4 / SLA 168 h)
* **Plataforma de Detección:** Stellar Cyber OpenXDR / Logs de Active Directory
* **Analista:** Kevin Moraes | **Resolución:** NOC Technoma / Kevin Moraes
* **Activos Involucrados:** Servidor Zabbix `192.168.15.27`, Controlador de Dominio `10.11.1.1` (`ad.technoma.local`), Cuenta de Dominio: `Mario Flores` (OU Usuarios dados de baja).
* **Veredicto Final:** **Incidente Operativo de Seguridad Resuelto y Remediado**
* **Clasificación:** Compromiso de la información / Vulnerabilidad de Configuración
* **Playbook Aplicado:** `FL-THN-POS-01 Rev. 03` / RFA de Remediación a Infraestructura

#### 1. Diagnóstico y Causa Raíz
El servidor de monitoreo Zabbix (`192.168.15.27`) realizaba intentos persistentes de autenticación contra el Domain Controller primario mediante el protocolo **LDAP simple sin cifrar (puerto 389/TCP)**. Las solicitudes utilizaban credenciales con contraseña por defecto pertenecientes a la cuenta de **Mario Flores**, colaborador que ya había sido desvinculado de la empresa y cuya cuenta residía en la Unidad Organizativa de bajas de Active Directory.

#### 2. Acciones de Contención y Remediación (NOC & SOC)
1. **Emisión de RFA del SOC:** Se escaló formalmente al NOC solicitando auditar el origen de las peticiones en los servidores Zabbix, revocar credenciales huérfanas y migrar la autenticación a canales seguros.
2. **Migración a LDAPS (Puerto 636/TCP):** El NOC modificó los archivos de configuración y DNS en ambas instancias de Zabbix, cambiando el protocolo de `ldap://` a `ldaps://` (tráfico cifrado TLS por puerto 636) y configurando la cuenta de servicio autorizada con Bind DN `zbx-ldaps`.
3. **Purga de Cuenta Local:** Se eliminó la cuenta local residual del usuario Mario Flores en ambas instancias de Zabbix, erradicando los reintentos automáticos.
4. **Verificación:** Monitoreo en Stellar Cyber confirmó el cese total de eventos de autenticación fallida por puerto 389. Cierre con conformidad.

#### 3. Lecciones Aprendidas Institucionales
1. **Checklist de Offboarding Integral:** La desvinculación de un colaborador en Active Directory debe incluir la purga inmediata de sus accesos y cuentas locales residuales en consolas internas de gestión (Zabbix, firewalls, dashboards).
2. **Prohibición de LDAP Simple en Texto Claro:** Establecer como directiva obligatoria de infraestructura el uso exclusivo de **LDAPS (puerto 636)** con certificados corporativos válidos, eliminando el riesgo de intercepción de credenciales (*sniffing*) en la red interna.

#### 4. Estandarización y Blindaje de `FL-THN-POS-01 Rev. 03` (Google Sheets)
Para prevenir errores de arrastre y manipulación manual por parte de los operadores del SOC, se crearon e integraron 4 **Funciones con Nombre** con argumentos dinámicos en la hoja oficial:
* `=CALCULAR_PRIORIDAD(H16; I16)`: Cruza automáticamente Impacto y Urgencia contra la matriz oficial.
* `=CALCULO_TIEMPO_NOTIFICACION(B16; C16; X16; Y16)`: Calcula el tiempo transcurrido hasta la notificación al cliente en horas.
* `=CALCULO_RESOLUCION(B16; C16; AA16; AB16)`: Calcula la duración total de resolución en horas.
* `=SLA(Z16; K16)`: Valida el cumplimiento del SLA contractual según la prioridad.

---

### Caso 022 - Falso Positivo Lote Interflow (Firmas IDS INFO y Falsa Correlación C&C LDAP)
* **ID Interno:** `ST-BATCH-OCT15`
* **Fecha:** 15/10/2026 12:55:00
* **Plataforma:** Stellar Cyber OpenXDR v7.0.0s / Sensor Modular NDR
* **Analista:** Kevin Moraes
* **Activos Involucrados:** `10.11.1.1` (`ad.technoma.local`), `192.168.169.71` (`NB-ICENTURION`), `192.168.169.78`, `192.168.169.19`
* **Severidad:** Low (IDS) elevada a High (75) por Playbook ATH (`Exploited C&C Connection`)
* **Veredicto Final:** **Falso Positivo (False Positive / Benign True Positive)**
* **Playbook:** `PB-3.1 Triaje de Tráfico de Red Anómalo y Falsos Positivos IDS`

#### 1. Triaje Forense y Causa Raíz
Se procesó un lote de 10 eventos correlacionados en Interflow. El análisis de las cargas útiles demostró que las alertas originales correspondían a firmas informacionales de Proofpoint ET (`classtype: misc-activity`):
* `SID 2071407`: Consultas DNS hacia `release-assets.githubusercontent.com` (actualización de software).
* `SID 2060507`: Consultas DNS de relevo AnyDesk (`relay-*.net.anydesk.com`) por soporte técnico.
* `SIDs 2067085, 2067086, 2067087`: Negociación y desafío NTLM/SMB corporativo del usuario `ivancenturion` desde `NB-ICENTURION` hacia `\technoma.local\IPC$` con autenticación exitosa (`NT_STATUS_SUCCESS`).
* `SID 2071627`: Consultas DNS hacia `web.telegram.org` desde el puesto `192.168.169.78`.

#### 2. Falsa Correlación de C&C
El playbook ATH de Stellar Cyber (`exploit_attempt_correlation`) tomó estas firmas INFO como "exploits" y correlacionó erróneamente el tráfico posterior de sincronización de Active Directory por el puerto **389/TCP (LDAP)** entre el DC y los endpoints como supuestas conexiones de Comando y Control.

#### 3. Resolución
Se cerró el caso como Falso Positivo en Stellar Cyber tras confirmar que no hubo intrusión ni balizamiento malicioso, y se documentó la recomendación de excluir firmas `misc-activity` de las reglas de correlación de intrusión.

---

### Caso 023 - Falso Positivo UBA Cloud: Sincronización Google AppSheet / AppScript (José Marín)
* **ID Interno:** `ST-GSUITE-MARIN`
* **Fecha:** 15/10/2026 13:10:00
* **Plataforma:** Stellar Cyber OpenXDR / Conector Google Workspace (`gsuite_Workspace-THN`)
* **Analista:** Kevin Moraes
* **Activo / Cuenta:** `josemarin@technoma.com.py` (Google Workspace)
* **Severidad:** High (70) | Score: 61 | Táctica: Exfiltration (TA0010 / T1567.002)
* **Veredicto Final:** **Falso Positivo Heurístico (Benign True Positive - BTP)**
* **Playbook:** `PB-2.2 Monitoreo Operativo / PB-6.1 Detección de Anomalías Cloud y Exfiltración`

#### 1. Triaje Forense y Causa Raíz
El motor de UBA disparó 7 alertas de *Cloud Drive Data Exfiltration Anomaly* advirtiendo sobre un volumen anómalo de descargas en Google Drive (~7.240 eventos en 24 horas frente a un perfil típico de 1.033).
La inspección de los metadatos de auditoría confirmó que las llamadas a la API `drive.files.get` fueron originadas por dos aplicaciones corporativas autorizadas:
* **Google AppSheet** (OAuth Client ID: `953348912797`)
* **POC Servicio Tecnico AppScript** (OAuth Client ID: `1043972006487`)

#### 2. Conciliación de Objetos
La totalidad de los archivos descargados corresponden a recursos gráficos operativos vinculados a órdenes de trabajo de campo:
* `*.firma_cliente.*.png` y `*.firma_tecnico.*.png` (firmas digitales de conformidad).
* `*.foto_qr.*.jpg` e `*.imagen.*.jpg` (evidencias fotográficas de servicio).
Dichos recursos fueron leídos en lote por la aplicación de soporte técnico para compilar y generar los reportes de servicio al cliente.

#### 3. Resolución
Se descartó compromiso de cuenta o fuga de datos. El caso fue cerrado formalmente como Falso Positivo en Stellar Cyber y se recomendó añadir los Client IDs de AppSheet y AppScript a la lista blanca de la regla UBA de Google Drive.

---

### Caso 024 - Optimización Quirúrgica de Ingesta: Filtro de Descarte Passthrough Benigno FortiGate
* **ID Interno:** `ST-INGEST-PASSTHROUGH`
* **Fecha:** 15/10/2026 13:15:00
* **Plataforma:** Stellar Cyber OpenXDR / Sensor Modular Technoma (`profile-modular-sensor-technoma`)
* **Analista:** Kevin Moraes
* **Área:** Ingeniería y Optimización de Ingesta / Control de Cuota Diaria
* **Acción Implementada:** Descarte de Ruido Benigno Passthrough (`DROP`)
* **Estado:** **Activo y Pegando Hits (Validado Operativamente)**

#### 1. Diagnóstico y Causa Raíz
Durante la auditoría del Data Lake y control de capacidad diaria se identificó un drenaje masivo de eventos continuos provenientes de logs de FortiGate con acción `passthrough` (más de 3.300 eventos por ventana de 5 minutos). 
El desglose de red reveló que correspondían a tráfico operativo estándar de navegación y telemetría de servicios de uso corporativo intensivo que no aportan valor de seguridad como eventos crudos aislados:
* Sincronización continua de ERP Odoo (`190.104.187.132`).
* Conexiones hacia CDNs, APIs y streaming de Google / Android (`142.251.0.0/16`, `172.217.0.0/16`).
* Rangos oficiales de colaboración Google Meet (`142.250.0.0/15`) y Cisco Webex (`64.68.96.0/19`, `66.114.160.0/20`, `66.163.32.0/19`, `170.72.0.0/16`, `173.39.224.0/19`).
* Descargas de medios y mensajería WhatsApp / Meta (`157.240.0.0/16`).
* Telemetría de Microsoft Windows Update y Azure (`20.0.0.0/11`).
* Envíos de telemetría de agentes de seguridad Palo Alto Traps (`162.159.137.105`).

#### 2. Implementación de los Filtros Quirúrgicos
Se diseñaron y desplegaron en Stellar Cyber vía API oficial en **System → Log Forwarders (Log Filters)**:
* **Filtro Principal:** `Drop_FW_Passthrough_Benign_Telemetry` (ID: `6ad0f8dfaa734118df02d27e`)
  * **Sensor Profile:** `profile-modular-sensor-technoma`
  * **Condiciones Aplicadas:**
    - `dev_type` **is** `fw_fortigate`
    - `action` **is** `passthrough`
    - `dstip` **matches** `190.104.187.132, 142.251.0.0/16, 172.217.0.0/16, 74.125.0.0/16, 170.72.0.0/16, 64.68.96.0/19, 173.39.224.0/19, 157.240.0.0/16, 20.0.0.0/11, 162.159.128.0/17, 34.98.77.231, 34.39.195.104, 4.0.0.0/8, 40.0.0.0/8, 51.0.0.0/8`
  * **Acción:** `DROP` (descarte selectivo antes del almacenamiento en Data Lake).

* **Filtros Adicionales Creados:**
  1. `Drop_FW_PaloAlto_Traps_Heartbeats` (ID: `6ad1558baa734118df02d348`): Descarte de handshakes y heartbeats SSL redundantes de los agentes de Cortex XDR hacia `34.98.77.231` y `34.39.195.104` en puerto 443 (~135.000 logs/día ahorrados).
  2. `Drop_FW_Windows_Diagnostics_Telemetry` (ID: `6ad155a7472282b392d236bf`): Descarte de telemetría passthrough de Windows hacia rangos oficiales de Azure Diagnostics `4.0.0.0/8, 40.0.0.0/8, 51.0.0.0/8` (~35.000 logs/día ahorrados).

#### 3. Resultado y Validación Operativa
* Los filtros ya se encuentran activos en producción.
* La tasa de ingesta de passthrough benigno se redujo en un 99.5%, y los heartbeats redundantes de Traps y telemetría de Windows quedaron purgados de la ingesta diaria.
* Se blindó la cuota de licencia diaria manteniendo visibilidad intacta sobre sesiones `accept` y `deny`, así como sobre cualquier destino no contemplado en la lista blanca estricta.


---

### Caso 025 - Trazabilidad y Conciliación de Auditoría: Incidente Cortex XDR 541 (Failed Connections - NB-JTORALES)
* **ID Incidente Cortex XDR:** `INCIDENT-541`
* **ID Alerta Original:** `137403`
* **Fecha de Creación:** 19/08/2026 22:50:06 UTC
* **Fecha de Resolución en Cortex:** 25/09/2026 14:26:23 UTC
* **Plataforma EDR:** Palo Alto Networks Cortex XDR (`technoma.xdr.us.paloaltonetworks.com`)
* **Plataforma SIEM/XDR:** Stellar Cyber OpenXDR v7.0.0s (Conector `CORTEX-XDR-V1`)
* **Analista:** Kevin Moraes
* **Activo Involucrado:** `NB-JTORALES` (IP: `192.168.100.14` / `10.212.134.205`, Agent ID: `ca9e9da710e240e89b3a64013cd02710`)
* **Usuario:** `TECHNOMA\josetorales`
* **Severidad:** Low (1)
* **Ticket de Caso Creado en Stellar Cyber:** `#17797` (`Palo Alto Networks Cortex XDR: Failed Connections` - ID: `6ad12ce1e4fb8b7307d82b1d`)
* **Estado en Stellar Cyber:** `Resolved` | **Resolución:** `False Positive` | **Score:** `9`
* **Veredicto Final:** **Falso Positivo / Ruido Operativo de Navegación (Resolved - Auto)**
* **Táctica MITRE ATT&CK:** `TA0007 - Discovery`
* **Técnica MITRE ATT&CK:** `T1018 - Remote System Discovery`

#### 1. Evidencia Registrada en Stellar Cyber (Interflow Data Lake)
* **Índice de Almacenamiento:** `stellar-index-v1-syslog-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033`
* **Conector:** `palo_alto_networks_cortex_CORTEX-XDR-V1`
* **Clase de Mensaje:** `palo_alto_networks_cortex_xdr_incidents`
* **Incident ID:** `541`
* **Host:** `nb-jtorales` (Agent ID: `ca9e9da710e240e89b3a64013cd02710`)
* **Nombre de la Amenaza:** `Failed Connections`
* **Descripción en Stellar:** `"NB-JTORALES tried to connect to 16 hosts in the last 24 hours"`
* **URL Directa a Cortex XDR:** `https://technoma.xdr.us.paloaltonetworks.com/incident-view?caseId=541`
* **Técnica MITRE:** `T1018 - Remote System Discovery`
* **Táctica MITRE:** `TA0007 - Discovery`

#### 2. Triaje Forense y Causa Raíz
El motor de comportamiento y analítica *Magnifier* de Cortex XDR generó la alerta `137403` al detectar que el equipo `NB-JTORALES` registró 16 intentos fallidos de conexión hacia direcciones IP locales (`192.168.100.97`, `10.61.18.66`, `192.168.18.3`, etc.) en puertos de rango dinámico efímero.
La inspección a nivel de proceso (`xdmsourceprocessexecutablepath`) confirmó que las conexiones fueron generadas exclusivamente por:
* **Proceso Actor:** `C:\Program Files\Mozilla Firefox\firefox.exe`
* **Firma Digital:** `Mozilla Corporation` (`SIGNED_VERIFIED`)
* **Hash SHA256:** `44f0741288e3e884ecc30e31b2d7633505650dffa3238e5fdd3cabb8429d0fc2`
* **Contexto Operativo:** Proceso hijo de contenido (`-contentproc`) intentando restablecer sockets de pestañas y servicios web internos/locales tras reactivación de sesión. No existió escaneo malicioso de red, herramientas de reconocimiento externas ni balizamiento.

#### 3. Resolución y Trazabilidad de Auditoría
El caso fue cerrado automáticamente por el motor de Cortex XDR (`status.resolution_reason: STATUS_080_RESOLVED_AUTO`) bajo la causal *"resolve as part of incident 541"*.
En Stellar Cyber, la telemetría e incidentes sincronizados a través del conector `CORTEX-XDR-V1` ratifican la recepción íntegra del evento bajo la clase `palo_alto_networks_cortex_xdr_incidents`, demostrando correlación y trazabilidad completa entre ambas herramientas para cumplimiento de auditoría.


