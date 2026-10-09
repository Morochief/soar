# Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR

## 1. Identificación del Caso
- **ID de Caso:** `19610_AD_DNS_Tunnel_and_Internal_FW_Denial_sati`
- **ID de Secuencia Stellar:** 19610, 19615, 19616, 19617, 19618, 19619, 19620, 19621, 19638, 19639, 19640, 19641, 19642, 19643, 19644 (15 eventos correlacionados)
- **Tenant:** Technoma (`cf73a415c8794884a0c35b458b7c73ae`)
- **Reglas Detectadas:**
  - `dns_tunnel` (13 eventos - Machine Learning)
  - `new_registered_domain` (1 evento - NBA)
  - `internal_fw_action` (1 evento - NBA / Firewall Anomaly)
- **Ventana Temporal de Detección:** 24/09/2026 15:17:55 UTC a 15:28:54 UTC (12:17:55 a 12:28:54 Local)
- **Analista Responsable:** Kevin Moraes
- **Veredicto Técnico:** Falso Positivo (Actividad Legítima de Infraestructura / Tráfico Bloqueado sin Compromiso)

---

## 2. Descripción y Actores Involucrados
| Parámetro | Grupo 1: DNS Tunneling y Dominio | Grupo 2: Firewall Denial (SSL-VPN) |
| :--- | :--- | :--- |
| **Origen** | `10.11.1.1` (`ad.technoma.local`) | `10.212.134.200` (Usuario VPN `sati`, `ssl.root`) |
| **Destino** | `10.11.1.2` (`ad2.technoma.local`) | `10.11.1.1` (`ad.technoma.local`, `Citrix Servers`) |
| **Protocolo / Puerto** | UDP 53 (DNS) | UDP 53 (DNS) |
| **Eventos / Volumen** | 13 anomalías ML DNS Tunnel + 1 New Domain | 1 evento ML (474 peticiones denegadas en 5 min) |
| **Acción / Veredicto** | Permitido (Resolución interna y forwarding) | Denegado en Firewall (`action="deny"`, `policyid=0`) |

---

## 3. Análisis de Causa Raíz
1. **Falso Positivo de Túnel DNS (13 eventos):** El modelo de Machine Learning (`dns_tunnel`) detectó una desviación estadística de entropía y bytes transferidos entre los controladores de dominio primario y secundario (`ad` `10.11.1.1` y `ad2` `10.11.1.2`). Al analizar las cargas útiles, todas corresponden a consultas y respuestas DNS de registros tipo A para nombres de host NetBIOS y servidores del dominio local (e.g. `NB-RFGONZALEZ`, `NB-ZGONZALEZ`, `NB-WGONZALEZ`, `NB-TIBANEZ`, `SRV-AZADCONNECT`, `NB-JCRISTALDO`, `NB-OALVARENGA`, `NB-SFERNANDEZ`, `NB-RMARTINEZ`), respondiendo con direcciones IP privadas válidas (`192.168.169.x`). Se confirma tráfico operativo legítimo del Directorio Activo.
2. **Dominio Recientemente Registrado (1 evento):** Consulta forwardeada desde `ad` hacia `ad2` para `firefox-portal-detection.com`, correspondiente al mecanismo oficial de detección de portales cautivos de Mozilla Firefox.
3. **Bloqueo en Firewall de Cliente VPN (1 evento):** El usuario remoto `sati` conectado vía SSL-VPN (`10.212.134.200`) intentó resolver consultas DNS contra `ad.technoma.local` (`10.11.1.1:53`), las cuales fueron descartadas por la regla implícita de denegación (`policyid=0`) del FortiGate `FG-Technoma`. El firewall actuó según diseño, conteniendo el tráfico sin vulneración de perímetro.

---

## 4. Evaluación de Impacto (Triada CIA)
- **Confidencialidad:** 0/10 (No hubo exfiltración; la carga útil fue validada como nombres de equipos de dominio).
- **Integridad:** 0/10 (Sin alteraciones de registros ni de configuraciones de seguridad).
- **Disponibilidad:** 0/10 (Operatividad normal de los controladores de dominio y servicios).
- **Puntuación Global de Riesgo:** **0.0 / 10 (Insignificante / Falso Positivo)**.

---

## 5. Cierre en Plataforma Stellar Cyber
- **Estado:** `Closed`
- **Resolution Tag:** `False Positive`
- **Comentario de Cierre Condensado:**
> Cierre por Falso Positivo: Las anomalías de túnel DNS entre ad.technoma.local (10.11.1.1) y ad2.technoma.local (10.11.1.2) corresponden a tráfico operativo de resolución de nombres de endpoints del dominio corporativo technoma.local, descartándose túneles encubiertos o exfiltración. Asimismo, la consulta hacia firefox-portal-detection.com obedece a telemetría benigna del navegador Mozilla Firefox, y las peticiones DNS del usuario VPN sati (10.212.134.200) fueron descartadas preventivamente por la regla implícita policyid=0 del firewall FortiGate, manteniéndose la postura de seguridad sin indicios de compromiso.
