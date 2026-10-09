# Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR

## 1. Identificación del Caso
- **ID de Caso:** `19445_Internal_Firewall_Denial_WUDO_7680_VLAN15_nb-odacosta`
- **ID de Secuencia Stellar:** 19445 y 19848
- **Tenant:** Technoma (`cf73a415c8794884a0c35b458b7c73ae`)
- **Dispositivo / Firewall:** `FG-Technoma` (`FG120GTK24022543`)
- **Regla Detectada:** `internal_fw_action` / `fw_action` (Internal Firewall Denial Anomaly)
- **Táctica / Técnica:** Exploration / XDR NBA (`XTA0002`) - XDR Firewall Anomaly (`XT2002`)
- **Fecha y Hora de Detección:** 24/09/2026 14:50:04 UTC (11:50:05 Local) y 16:25:06 UTC (13:25:06 Local)
- **Analista Responsable:** Kevin Moraes
- **Veredicto Técnico:** Falso Positivo (Ruido Operativo / Bloqueo Legítimo de Firewall Inter-VLAN por Windows Update Delivery Optimization - WUDO P2P)

---

## 2. Descripción y Actores Involucrados
| Parámetro | Detalle de Origen | Detalle de Destino |
| :--- | :--- | :--- |
| **Dirección IP** | `192.168.15.16` | `192.168.169.71` |
| **Hostname / Usuario** | Host en segmento de datos (`VLAN-15`) | `nb-odacosta.technoma.local` / `OSCARACOSTA` |
| **VLAN / Interfaz** | `VLAN-15` (`lan`, `vlan0`) | `WiFi_Corp` (`lan`, `vlan0`) |
| **Protocolo y Puerto** | TCP 51824 / 53347 | TCP 7680 (WUDO / Delivery Optimization) |
| **Política FortiGate** | `policyid=0` (Denegación implícita) | Acción: `deny`, `sentbyte=0`, `rcvdbyte=0` |

---

## 3. Análisis de Causa Raíz
Se procesaron 2 eventos correlacionados que totalizan **467 paquetes TCP bloqueados** en el puerto 7680:
1. **Secuencia 19445 (11:50:05 local):** 186 paquetes bloqueados dirigidos hacia `192.168.169.71:7680`.
2. **Secuencia 19848 (13:25:06 local):** 281 paquetes bloqueados dirigidos hacia `192.168.169.71:7680`.

El tráfico fue generado por el servicio del sistema operativo Windows para la distribución de actualizaciones entre pares (*Windows Update Delivery Optimization* - WUDO / DoSvc) desde el equipo `192.168.15.16`, intentando establecer una conexión P2P local con la estación inalámbrica de usuario `nb-odacosta.technoma.local` (`192.168.169.71`, asignada a `OSCARACOSTA` en `WiFi_Corp`). 

Debido a la segmentación de red corporativa, el firewall FortiGate `FG-Technoma` no cuenta con reglas que autoricen tráfico lateral inter-VLAN entre la red de datos `VLAN-15` y la red inalámbrica `WiFi_Corp` en el puerto 7680, por lo que el tráfico fue descartado de forma estricta y transparente por la política implícita (`policyid=0`, `sentbyte=0`, `rcvdbyte=0`). El volumen de reintentos superó el umbral basal habitual (22-32 denegaciones/5 min), disparando la anomalía de Machine Learning. Se descarta actividad de escaneo o compromiso.

---

## 4. Evaluación de Impacto (Triada CIA)
- **Confidencialidad:** 0/10 (Tráfico bloqueado inmediatamente; 0 bytes transmitidos).
- **Integridad:** 0/10 (Sin modificaciones en configuraciones ni hosts involucrados).
- **Disponibilidad:** 0/10 (Segmentación y aislamiento inter-VLAN operando correctamente).
- **Puntuación Global de Riesgo:** **0.0 / 10 (Insignificante / Falso Positivo)**.

---

## 5. Cierre en Plataforma Stellar Cyber
- **Estado:** `Closed`
- **Resolution Tag:** `False Positive`
- **Comentario de Cierre Condensado:**
> Cierre por Falso Positivo: Las alertas de internal_fw_action sobre el host 192.168.15.16 (VLAN-15) corresponden a denegaciones legítimas de firewall (policyid=0) ante intentos de conexión en el puerto TCP 7680 hacia el endpoint nb-odacosta.technoma.local (192.168.169.71, OSCARACOSTA) en WiFi_Corp, originados por el servicio nativo de optimización de entrega de Windows Update (WUDO P2P), bloqueándose la totalidad del tráfico con 0 bytes transferidos y descartándose cualquier vector de compromiso.
