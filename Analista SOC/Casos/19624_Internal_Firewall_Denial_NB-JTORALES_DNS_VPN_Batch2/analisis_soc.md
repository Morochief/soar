# Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR

## 1. Identificación del Caso
- **ID de Caso:** `19624_Internal_Firewall_Denial_NB-JTORALES_DNS_VPN_Batch2`
- **ID de Secuencia Stellar:** 19624, 19647, 19663, 19677
- **Tenant:** Technoma (`cf73a415c8794884a0c35b458b7c73ae`)
- **Dispositivo / Firewall:** `FG-Technoma` (`FG120GTK24022543`)
- **Regla Detectada:** `internal_fw_action` / `fw_action` (Internal Firewall Denial Anomaly)
- **Táctica / Técnica:** Exploration / XDR NBA (`XTA0002`) - XDR Firewall Anomaly (`XT2002`)
- **Fecha y Hora de Detección:** 24/09/2026 entre 15:20:00 y 15:35:23 UTC (12:20:00 a 12:35:23 Local)
- **Analista Responsable:** Kevin Moraes
- **Veredicto Técnico:** Falso Positivo (Ruido Operativo / Reintentos de Resolución DNS Multi-Homed de Windows hacia Servidores VPN Inalcanzables)

---

## 2. Descripción y Actores Involucrados
| Parámetro | Detalle de Origen | Detalle de Destino |
| :--- | :--- | :--- |
| **Dirección IP** | `192.168.169.64` | `192.168.100.1`, `192.168.3.1`, `192.168.3.214` |
| **Hostname / Usuario** | `NB-JTORALES` / `josetorales` | Servidores DNS remotos en túneles VPN IPsec (`CASA-ASTI` y `ROGGIO_PRI`) |
| **VLAN / Interfaz** | `WiFi_Corp` (`lan`, `vlan0`) | `CASA-ASTI` / `ROGGIO_PRI` (`ipsecvpn`) |
| **Servicio y Puerto** | UDP dinámicos (49874, 63093, 50196, 52487) | UDP 53 (DNS) |
| **Política FortiGate** | `policyid=0` (Denegación implícita) | Acción: `deny`, `sentbyte=0`, `rcvdbyte=0` |

---

## 3. Análisis de Causa Raíz
Se identificó una nueva ráfaga de 4 eventos correlacionados sumando **11.088 intentos de conexión DNS bloqueados** en un intervalo de 15 minutos:
1. **Secuencia 19624 (12:19:59 local):** 2.926 paquetes denegados hacia `192.168.100.1:53` vía `CASA-ASTI`.
2. **Secuencia 19647 (12:24:59 local):** 3.184 paquetes denegados hacia `192.168.3.1:53` vía `ROGGIO_PRI`.
3. **Secuencia 19663 (12:29:59 local):** 2.409 paquetes denegados hacia `192.168.100.1:53` vía `CASA-ASTI`.
4. **Secuencia 19677 (12:35:22 local):** 2.569 paquetes denegados hacia `192.168.3.214:53` vía `ROGGIO_PRI`.

El comportamiento corresponde a la persistencia del mecanismo nativo de Windows (Smart Multi-Homed Name Resolution) en el equipo corporativo `NB-JTORALES`. Al estar conectado a la red corporativa inalámbrica (`WiFi_Corp`), el sistema operativo mantiene configurados adaptadores de red o entradas estáticas correspondientes a sedes remotas y túneles IPsec (`CASA-ASTI` y `ROGGIO_PRI`). Debido a que el firewall FortiGate `FG-Technoma` no posee reglas que permitan el enrutamiento cruzado desde la Wi-Fi hacia dichas interfaces VPN, el tráfico es inmediatamente bloqueado por la política por defecto (`policyid=0`). No existe actividad hostil, escaneo de puertos ni tráfico bidireccional (`sentbyte=0`, `rcvdbyte=0`).

---

## 4. Evaluación de Impacto (Triada CIA)
- **Confidencialidad:** 0/10 (Tráfico bloqueado en su totalidad; 0 bytes transferidos).
- **Integridad:** 0/10 (Sin alteraciones en políticas, firewall ni hosts).
- **Disponibilidad:** 0/10 (Operatividad de red y servicios VPN sin afectación).
- **Puntuación Global de Riesgo:** **0.0 / 10 (Insignificante / Falso Positivo)**.

---

## 5. Cierre en Plataforma Stellar Cyber
- **Estado:** `Closed`
- **Resolution Tag:** `False Positive`
- **Comentario de Cierre Condensado:**
> Cierre por Falso Positivo: El clúster de 4 alertas de internal_fw_action sobre NB-JTORALES (192.168.169.64, josetorales) en la interfaz WiFi_Corp corresponde a denegaciones legítimas de firewall (policyid=0) ante reintentos masivos de resolución DNS (UDP 53) dirigidos a servidores DNS de túneles IPsec inalcanzables (192.168.100.1, 192.168.3.1 y 192.168.3.214), generados por el comportamiento multi-homed de Windows con 0 bytes transferidos y descartándose cualquier vector de compromiso.
