# Informe de Análisis SOC - Lote Completo Interflow (10 Eventos)
**ID del Caso:** `19072_Lote10_AD_DNS_Tunnel_sati_VPN_and_ET_cc_TLD`  
**Fecha de Análisis:** 2026-09-24 09:52:00 (UTC-03:00)  
**Analista Responsable:** Nivel 1 SOC / DFIR  
**Tenant / Organización:** `Technoma` (`cf73a415c8794884a0c35b458b7c73ae`)  
**Sensores Involucrados:** `technoma-sensor` (`4e3eab0649114a80a089a5d5a078994d`) / `FG-Technoma` (`FG120GTK24022543`)  

---

## 1. Declaración de Cantidad y Desglose del Lote
Se procesaron exhaustivamente **10 eventos de seguridad** nativos de Interflow, clasificados en 4 grupos técnicos correlacionados:

| Nro. | Seq No. | Event Name / Regla | Origen | Destino | Servicio / Objeto |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **1** | `19072` | `new_registered_domain` | `10.11.1.1` (`ad`) | `8.8.8.8` (Google DNS) | `firefox-portal-detection.com` (Tipo A) |
| **2** | `19073` | `dns_tunnel` | `10.11.1.1` (`ad`) | `10.11.1.2` (`ad2`) | `NB-RZABALA.technoma.local` |
| **3** | `19074` | `dns_tunnel` | `10.11.1.1` (`ad`) | `10.11.1.2` (`ad2`) | `NB-RZABALA.technoma.local` |
| **4** | `19085` | `exploit_attempt_priv_priv` (`ET .cc TLD`) | `192.168.169.36` (`nb-daquino`) | `10.11.1.1` (`ad`) | `gtracenep.admaster.cc` (Tipo HTTPS) |
| **5** | `19082` | `dns_tunnel` | `10.11.1.1` (`ad`) | `10.11.1.2` (`ad2`) | `NB-AZORRILLA.technoma.local` |
| **6** | `19083` | `dns_tunnel` | `10.11.1.1` (`ad`) | `10.11.1.2` (`ad2`) | `NB-ODACOSTA.technoma.local` |
| **7** | `19090` | `internal_fw_action` | `10.212.134.203` (VPN `sati`) | `10.11.1.1` (`ad`) | UDP/53 DNS (Policy ID 0 / Deny) |
| **8** | `19089` | `dns_tunnel` | `10.11.1.1` (`ad`) | `10.11.1.2` (`ad2`) | `NB-JRAGUERO.technoma.local` |
| **9** | `19091` | `dns_tunnel` | `10.11.1.1` (`ad`) | `10.11.1.2` (`ad2`) | `NB-TIBANEZ.technoma.local` |
| **10**| `19092` | `dns_tunnel` | `10.11.1.1` (`ad`) | `10.11.1.2` (`ad2`) | `NB-TIBANEZ.technoma.local` |

---

## 2. Análisis Técnico por Grupos de Detección

### Grupo 1: Falso Positivo Clásico de DNS Tunneling entre Controladores de Dominio (7 Eventos)
- **Alertas:** `19073`, `19074`, `19082`, `19083`, `19089`, `19091`, `19092`
- **Mapeo MITRE / XDR:** `TA0010` (Exfiltration) / `T1048` (Exfiltration Over Alternative Protocol).
- **Flujo de Tráfico:** `10.11.1.1:53` (`ad.technoma.local`) $\leftrightarrow$ `10.11.1.2:53` (`ad2.technoma.local`).
- **Análisis Forense:**
  - El motor de Machine Learning de Stellar Cyber disparó la alerta de túnel DNS calculando una métrica de entropía artificialmente elevada (`total_entropy: 118 - 153`) debido a los nombres de host y sufijos del dominio local corporativo (`technoma.local`).
  - La inspección de las cargas útiles decodificadas ("tunnel payloads") revela que el 100% de los identificadores corresponden a nombres de equipos corporativos asignados a colaboradores (`NB-ALOVERA`, `NB-CYUDIZ`, `NB-FCANDIA`, `NB-FSERVIN`, `NB-GCABANAS`, `NB-CFARINA`, `NB-JMARIN`, `NB-RFGONZALEZ`, `NB-JOSEB`, `NB-JPALACIOS`, `NB-JRIVAROLA`, `wpad`, `ad2`, etc.).
  - Las respuestas devuelven IPs privadas corporativas válidas (`192.168.169.x`, `192.168.100.x`, `10.212.x.x`).
  - **Conclusión:** Tráfico operacional estándar de sincronización y resolución de nombres de Active Directory entre los dos servidores DNS primario y secundario de Technoma. No hay exfiltración de datos.

### Grupo 2: Resolución Recursiva hacia Google DNS de Portal Cautivo Firefox (1 Evento)
- **Alerta:** `19072` (`new_registered_domain`)
- **Flujo:** `10.11.1.1` (`ad.technoma.local`) $\rightarrow$ `8.8.8.8:53` (`dns.google`).
- **Consulta:** `firefox-portal-detection.com` (Tipo A).
- **Análisis (Fast-Track Regla 5):**
  - Es la resolución recursiva generada por el servidor DNS corporativo para responder a la solicitud efectuada previamente por el equipo `192.168.169.107` con navegador Mozilla Firefox.
  - El dominio es oficial de Mozilla, tiene reputación limpia (`domain_reputation: Good`), resuelve en Fastly CDN y no presenta indicadores DGA.

### Grupo 3: Firma IDS ET para TLD .cc Disparada por Navegación Web (1 Evento)
- **Alerta:** `19085` (`exploit_attempt_priv_priv` / `ids_traffic_anomaly`)
- **Firma IDS:** Suricata SID `2027758` (`ET DNS Query for .cc TLD`, severidad nativa: `Informational`).
- **Flujo:** `192.168.169.36` (`nb-daquino.technoma.local`) $\rightarrow$ `10.11.1.1:53`.
- **Consulta:** `gtracenep.admaster.cc` (Tipo HTTPS).
- **Análisis:**
  - La firma Emerging Threats alerta informativamente ante cualquier consulta DNS que finalice en el TLD `.cc` (Islas Cocos). Stellar Cyber agrupó 6 consultas del usuario en un bucket de 5 minutos y lo catalogó como anomalía de exploit (`T1210 / Propagation`).
  - El dominio `admaster.cc` es una plataforma legítima de analítica y rastreo web alojada en servidores DNS de Wix (`ns6.wixdns.net`), consultada de forma transparente por componentes de páginas web durante la navegación de `nb-daquino`. No existe intento de explotación remota ni ataque lateral.

### Grupo 4: Bloqueo de Tráfico DNS desde Cliente VPN en FortiGate (1 Evento)
- **Alerta:** `19090` (`internal_fw_action`)
- **Flujo:** `10.212.134.203` (Usuario SSL-VPN: `sati`) $\rightarrow$ `10.11.1.1:53` (`Citrix Servers`).
- **Acción:** `deny` vía política predeterminada `policyid=0` (373 bloqueos en 5 min).
- **Análisis:**
  - El cliente remoto `sati` conectado por túnel VPN `ssl.root` genera consultas DNS hacia `10.11.1.1`. Al intentar acceder a la interfaz `Citrix Servers` donde no existe una regla que habilite explícitamente el reenvío DNS desde ese segmento VPN, el firewall bloquea el tráfico y el host reintenta la resolución.
  - Comportamiento operativo idéntico al documentado previamente para este mismo usuario, sin riesgo de intrusión.

---

## 3. Evaluación de Impacto y Tríada CIA
- **Confidencialidad (0/10):** Ningún dato confidencial fue exfiltrado (los supuestos "túneles" son resoluciones internas de nombres NetBIOS/AD).
- **Integridad (0/10):** Sin alteraciones en servicios ni ejecución de payloads.
- **Disponibilidad (0/10):** Infraestructura operativa al 100%.
- **Puntuación de Riesgo Global:** **0.0 / 10** (Insignificante / Falso Positivo Sistémico).

---

## 4. Veredicto Final y Recomendación
- **Veredicto:** **Falso Positivo** (Ruido de Infraestructura AD DNS, Navegación Web y Políticas de Firewall VPN).
- **Recomendación de Tuning:**
  1. Configurar una lista blanca / excepción en el motor ML de DNS Tunneling para excluir las consultas de resolución mutua entre los controladores de dominio `10.11.1.1` y `10.11.1.2` bajo la zona `technoma.local`.
  2. Ajustar la severidad de la firma IDS `2027758` (`ET DNS Query for .cc TLD`) para no alimentar anomalías de tipo exploit ante navegación web estándar.
  3. Cerrar los 10 eventos en Stellar Cyber como Falso Positivo.
