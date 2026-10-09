# Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR

## 1. Identificación del Caso
- **ID de Caso:** `43573_AD_DNS_Tunnel_Internal_FW_Denial_and_GPO_Sync`
- **ID de Secuencia Stellar:** 43573, 43574, 43575, 43576, 43577, 43578, 43579, 43581, 43582, 43593, 43594, 43595, 43596, 43597, 43605 (15 eventos correlacionados)
- **Tenant:** Technoma (`cf73a415c8794884a0c35b458b7c73ae`)
- **Sensor:** `technoma-sensor` (`4e3eab0649114a80a089a5d5a078994d`)
- **Reglas Involucradas:**
  - `dns_tunnel` (10 eventos - Machine Learning / Exfiltration)
  - `internal_fw_action` (3 eventos - NBA / Firewall Denial Anomaly)
  - `exploit_attempt_correlation` (1 evento - NBA / Exploited C&C Connection)
  - `exploit_attempt_priv_pub` (1 evento - IDS Traffic Anomaly)
- **Ventana Temporal de Detección:** 01/10/2026 13:40:14 UTC a 13:51:30 UTC (10:40:14 a 10:51:30 Local)
- **Analista Responsable:** Kevin Moraes
- **Veredicto Técnico:** Falso Positivo (Actividad Legítima de Infraestructura Active Directory / Replicación GPO / Bloqueos Preventivos en Firewall)

---

## 2. Declaración de Cantidad y Desglose Individual del Lote (15 Eventos)

Se procesaron **15 eventos individuales** contenidos en el volcado de telemetría:

1. **Evento 1 (`_seq_no: 43581` | `internal_fw_action`):** 987 bloqueos en 5 minutos (típico: 23) registrados por `FG-Technoma` sobre consultas DNS (UDP/53) desde el dispositivo móvil Android `192.168.171.142` (`VLAN304`) hacia `10.11.1.1:53` (`ad.technoma.local`, interfaz `Citrix Servers`), descartadas bajo `policyid=0`.
2. **Evento 2 (`_seq_no: 43582` | `internal_fw_action`):** 258 bloqueos en 5 minutos (típico: 23) en `FG-Technoma` sobre peticiones DNS desde la IP SSL-VPN `10.212.134.208` (usuario `FABIANACUñA`, interfaz `ssl.root`) hacia `10.11.1.1:53`, descartadas bajo `policyid=0`.
3. **Evento 3 (`_seq_no: 43573` | `dns_tunnel`):** Tráfico DNS de 578 Bytes (típico: 28.62 B) entre `10.11.1.1` (`ad.technoma.local`) y `10.11.1.2:53` (`ad2.technoma.local`). Consulta tipo A para `NB-SFERNANDEZ.technoma.local` resuelta en `192.168.169.120`. Payloads: `ad2`, `NB-ADIARTE`, `NB-AORTELLADO`, `NB-CARANDA`, `NB-CFARINA`.
4. **Evento 4 (`_seq_no: 43574` | `dns_tunnel`):** Tráfico DNS de 586 Bytes (típico: 19.33 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-TMARIN.technoma.local` resuelta en `192.168.169.126`. Payloads: `ad2`, `NB-AMARTINEZ`, `NB-ANGELRA2`, `NB-AZORRILLA`, `NB-DRODAS`.
5. **Evento 5 (`_seq_no: 43575` | `dns_tunnel`):** Tráfico DNS de 675 Bytes (típico: 23.77 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `SRV-AZADCONNECT.technoma.local` resuelta en `10.11.1.3`. Payloads: `NB-CLEIVA`, `NB-JENCISO`, `NB-ECANETE`, `NB-FBENEGAS`, `NB-HVERA`.
6. **Evento 6 (`_seq_no: 43576` | `dns_tunnel`):** Tráfico DNS de 563 Bytes (típico: 27.67 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-RLLEDO.technoma.local` resuelta en `192.168.169.79`. Payloads: `NB-ADIARTE`, `NB-ODACOSTA`, `NB-AORTELLADO`, `NB-CARANDA`, `NB-NSANCHEZ`.
7. **Evento 7 (`_seq_no: 43577` | `dns_tunnel`):** Tráfico DNS de 534 Bytes (típico: 19.36 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-TMARIN.technoma.local` resuelta en `192.168.169.126`. Payloads: `NB-AMARTINEZ`, `NB-AZORRILLA`, `NB-FCANDIA`, `NB-GCABANAS`, `NB-HCOLMAN`.
8. **Evento 8 (`_seq_no: 43578` | `dns_tunnel`):** Tráfico DNS de 655 Bytes (típico: 18.8 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-WGONZALEZ.technoma.local` resuelta en `192.168.169.46`. Payloads: `NB-ARUIZ`, `NB-RDESCALZO`, `NB-DFERNANDEZ`, `NB-JAQUINO`, `NB-ECANETE`.
9. **Evento 9 (`_seq_no: 43579` | `dns_tunnel`):** Tráfico DNS de 609 Bytes (típico: 18.33 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-SFERNANDEZ.technoma.local` resuelta en `192.168.169.120`. Payloads: `NB-ADIARTE`, `NB-ALPIZZUTI`, `NB-AORTELLADO`, `NB-GVERA`, `NB-JMARIN`.
10. **Evento 10 (`_seq_no: 43593` | `exploit_attempt_correlation`):** Correlación de regla de playbook ("Exploited C&C Connection") entre `10.11.1.2` y `10.11.1.1:49672` (MSRPC `ms_ad`), ligada a la firma IDS `HUNTING Possible Powershell .ps1 Script Use Over SMB` (`SID: 2027204`). La inspección profunda confirma lectura legítima de la directiva de grupo `technoma.local\policies\{21D4988D-E575-4017-8FFB-70C6D8D618F9}\gpt.ini` y consultas RPC (`lsarpc`) durante la replicación inter-DC.
11. **Evento 11 (`_seq_no: 43594` | `dns_tunnel`):** Tráfico DNS de 573 Bytes (típico: 30.8 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-TIBANEZ.technoma.local` resuelta en `192.168.169.81`. Payloads: `NB-ACHAMORRO`, `NB-AGILL`, `NB-DLOVERA`, `NB-FKOCHMANN`, `NB-FROJAS`.
12. **Evento 12 (`_seq_no: 43595` | `internal_fw_action`):** 204 bloqueos en 5 minutos (típico: 23) en `FG-Technoma` sobre consultas DNS desde la IP SSL-VPN `10.212.134.209` (usuario `sati`, interfaz `ssl.root`) hacia `10.11.1.1:53`, descartadas bajo `policyid=0`.
13. **Evento 13 (`_seq_no: 43605` | `exploit_attempt_priv_pub`):** Pico de severidad IDS (8.5 vs 1.5 típico) desde `10.11.1.1` hacia `8.8.8.8:53` por la firma informacional `INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup` (`SID: 2060507`), acompañada de resoluciones estándar de Microsoft Teams / TrafficManager (`trouter-atm-pub-ent.trafficmanager.NET`).
14. **Evento 14 (`_seq_no: 43596` | `dns_tunnel`):** Tráfico DNS de 602 Bytes (típico: 22.8 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-ODACOSTA.technoma.local` resuelta en `192.168.169.76`. Payloads: `NB-ANGELRA2`, `NB-AORTELLADO`, `NB-ARESQUIN`, `NB-ASAUCEDO`, `NB-CALVAREZ`.
15. **Evento 15 (`_seq_no: 43597` | `dns_tunnel`):** Tráfico DNS de 566 Bytes entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `SRV-AZADCONNECT.technoma.local` resuelta en `10.11.1.3`.

---

## 3. Descripción y Actores Involucrados

| Parámetro | Grupo 1: DNS Tunneling Anomaly (10 Eventos) | Grupo 2: Firewall Denial Anomaly (3 Eventos) | Grupo 3: C&C Correlation & GPO Sync (1 Evento) | Grupo 4: IDS AnyDesk DNS (1 Evento) |
| :--- | :--- | :--- | :--- | :--- |
| **Origen** | `10.11.1.1` (`ad.technoma.local` - DC1) | `192.168.171.142` (Android VLAN304), `10.212.134.208` (`FABIANACUñA`), `10.212.134.209` (`sati`) | `10.11.1.2` (`ad2.technoma.local` - DC2) | `10.11.1.1` (`ad.technoma.local`) |
| **Destino** | `10.11.1.2` (`ad2.technoma.local` - DC2) | `10.11.1.1:53` (`ad.technoma.local`, `Citrix Servers`) | `10.11.1.1:49672` (MSRPC / DCERPC) | `8.8.8.8:53` (Google DNS) |
| **Protocolo / Puerto** | UDP 53 (DNS) | UDP 53 (DNS) | TCP 49672 / TCP 445 (MSRPC / SMB) | UDP 53 (DNS) |
| **Volumen / Detección** | 10 alertas de Machine Learning (volúmenes de 534 a 675 Bytes) | 3 alertas ML FortiGate (987, 258 y 204 bloqueos en 5 min) | 1 alerta correlacionada (regla `exploit_attempt_correlation`) | 1 alerta IDS informacional (`SID: 2060507`) |
| **Acción / Estado** | Tráfico Permitido (Resolución y replicación interna DNS) | Denegado en Firewall FortiGate (`action="deny"`, `policyid=0`) | Tráfico Permitido (Sincronización legítima de Active Directory) | Tráfico Permitido (Resolución DNS externa) |

---

## 4. Análisis Técnico y Causa Raíz

### A. Falso Positivo Heurístico de Túnel DNS (10 Eventos)
El modelo de Machine Learning `dns_tunnel` de Stellar Cyber evalúa la entropía y el tamaño de las respuestas DNS transmitidas en ventanas de 5 minutos. En este lote, el Controlador de Dominio primario `ad.technoma.local` (`10.11.1.1`) remitió consultas DNS hacia el DC secundario `ad2.technoma.local` (`10.11.1.2`) para resolver nombres NetBIOS de estaciones de trabajo corporativas (`NB-SFERNANDEZ`, `NB-TMARIN`, `NB-RLLEDO`, `NB-WGONZALEZ`, `NB-TIBANEZ`, `NB-ODACOSTA`) y el servidor de sincronización híbrida (`SRV-AZADCONNECT.technoma.local`). Todas las respuestas fueron exitosas (`No Error`) apuntando a IPs privadas de la LAN (`192.168.169.x`) y servidores internos (`10.11.1.3`). No existe canal encubierto, exfiltración ni dominio malicioso.

### B. Bloqueos Preventivos en Firewall FortiGate (3 Eventos)
El firewall perimetral `FG-Technoma` (`FG120GTK24022543`) descartó bajo la regla implícita de denegación (`policyid=0`) ráfagas de consultas DNS dirigidas al puerto `UDP/53` de `10.11.1.1`:
- Un dispositivo móvil Android conectado a `VLAN304` (`192.168.171.142`) con 987 intentos bloqueados.
- Dos clientes conectados por SSL-VPN: el usuario `FABIANACUñA` (`10.212.134.208`) con 258 bloqueos y el usuario `sati` (`10.212.134.209`) con 204 bloqueos.
En todos los casos, el firewall contuvo las solicitudes de forma segura en el perímetro sin impacto en la infraestructura interna.

### C. Falsa Correlación de C&C por Replicación de GPO (1 Evento)
La alerta `Exploited C&C Connection` fue generada por una regla automática de correlación al detectar una sesión MSRPC entre los dos controladores de dominio (`10.11.1.2` $\rightarrow$ `10.11.1.1:49672`) asociada a un evento previo de IDS con la firma `HUNTING Possible Powershell .ps1 Script Use Over SMB` (`SID: 2027204`). Al auditar los metadatos SMB, se comprobó que el flujo corresponde estrictamente a la lectura de directivas de grupo del Directorio Activo (`technoma.local\policies\{21D4988D-E575-4017-8FFB-70C6D8D618F9}\gpt.ini`) y llamadas de autenticación RPC `lsarpc`. No hubo ejecución de PowerShell malicioso ni conexión con servidores de Comando y Control externos.

### D. Firma IDS Informacional AnyDesk (1 Evento)
La alerta `exploit_attempt_priv_pub` obedeció a consultas DNS salientes hacia los servidores recursivos de Google (`8.8.8.8`) para dominios legítimos de retransmisión de AnyDesk (`relay-*.net.anydesk.com`) y enrutamiento de Microsoft Teams (`trafficmanager.net`), clasificadas como actividad menor (`severity: low` / `Informational`).

---

## 5. Evaluación de Impacto (Tríada CIA)
- **Confidencialidad:** 0/10 (Sin exfiltración de datos; las cargas DNS y SMB corresponden a nombres NetBIOS y archivos de directivas públicas de dominio).
- **Integridad:** 0/10 (Sin alteraciones de configuraciones ni ejecución no autorizada de código).
- **Disponibilidad:** 0/10 (Operación normal y continua de los Controladores de Dominio y servicios de red).
- **Puntuación Global de Riesgo:** **0.0 / 10 (Insignificante / Falso Positivo Operativo)**.

---

## 6. Veredicto y Confianza Analítica
```json
{
  "veredicto": "False Positive",
  "categoria": "Ruido Heuristico de Entropia DNS / Bloqueos Esperados de Firewall / Replicacion Legítima de GPO",
  "confianza_analitica": "100%",
  "justificacion": "Las 10 alertas de dns_tunnel reflejan resoluciones DNS legitimas de endpoints corporativos (NB-*) y SRV-AZADCONNECT entre DCs. Las 3 alertas de firewall corresponden a bloqueos esperados por policyid=0 para VPN y VLAN304. El evento de C&C es una falsa correlacion provocada por replicacion legitima de directivas GPO (gpt.ini) en SMB/RPC entre los Controladores de Dominio."
}
```

---

## 7. Fila Única para Bitácora de Turno (18 Columnas)

| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc.) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 01/10/2026 10:51 | Kevin Moraes | Technoma | 43573 | technoma-sensor / new_ml | - | Baja | dns_tunnel / internal_fw_action / exploit_attempt_correlation | Replicación DNS entre DCs, Bloqueos en Firewall FortiGate y Replicación GPO | ad.technoma.local (10.11.1.1), ad2.technoma.local (10.11.1.2), FG-Technoma, VPN sati/FABIANACUñA, Android VLAN304 | Lote de 15 eventos. FP operativo consolidado: 10 alertas de dns_tunnel por resolucion legitima de endpoints NetBIOS (NB-*) y SRV-AZADCONNECT entre DCs; 3 alertas de bloqueos en FortiGate por policyid:0 para VPN (sati, FABIANACUñA) y Android VLAN304 hacia DC1; 1 falsa correlacion de C&C por lectura legitima de GPO (gpt.ini) sobre SMB/RPC; 1 firma IDS informativa AnyDesk. Sin compromiso. | DNS UDP/53 queries NetBIOS, FortiGate syslog (policyid: 0, action: deny) y SMB GPO read gpt.ini | Cerrar en plataforma Stellar Cyber y verificar aplicacion de Pre-DPI Filter para trafico inter-DC en UDP/53. | Cerrado | - | No | - | PB 5.2 |

### TSV de 1-Clic para Excel / Google Sheets
```tsv
01/10/2026 10:51	Kevin Moraes	Technoma	43573	technoma-sensor / new_ml	-	Baja	dns_tunnel / internal_fw_action / exploit_attempt_correlation	Replicación DNS entre DCs, Bloqueos en Firewall FortiGate y Replicación GPO	ad.technoma.local (10.11.1.1), ad2.technoma.local (10.11.1.2), FG-Technoma, VPN sati/FABIANACUñA, Android VLAN304	Lote de 15 eventos. FP operativo consolidado: 10 alertas de dns_tunnel por resolucion legitima de endpoints NetBIOS (NB-*) y SRV-AZADCONNECT entre DCs; 3 alertas de bloqueos en FortiGate por policyid:0 para VPN (sati, FABIANACUñA) y Android VLAN304 hacia DC1; 1 falsa correlacion de C&C por lectura legitima de GPO (gpt.ini) sobre SMB/RPC; 1 firma IDS informativa AnyDesk. Sin compromiso.	DNS UDP/53 queries NetBIOS, FortiGate syslog (policyid: 0, action: deny) y SMB GPO read gpt.ini	Cerrar en plataforma Stellar Cyber y verificar aplicacion de Pre-DPI Filter para trafico inter-DC en UDP/53.	Cerrado	-	No	-	PB 5.2
```

---

## 8. Instrucción de Cierre en Plataforma Stellar Cyber
* **Estado:** `Closed`
* **Resolution Tag:** `False Positive`
* **Comentario de Cierre Maestro Unificado:**
> Cierre por Falso Positivo: Las anomalías de túnel DNS registradas entre los Controladores de Dominio ad.technoma.local (10.11.1.1) y ad2.technoma.local (10.11.1.2) obedecen a tráfico operativo legítimo de resolución de nombres de estaciones de trabajo corporativas (NB-*) y del servicio de sincronización híbrida SRV-AZADCONNECT.technoma.local, descartándose canales encubiertos o fuga de información. De forma análoga, la alerta de conexión de Comando y Control corresponde a una falsa correlación derivada de la sincronización rutinaria de directivas de grupo de Active Directory (lectura de gpt.ini y llamadas RPC) entre ambos controladores, sin evidencia de ejecución anómala ni balizamiento externo. Por último, los eventos de denegación volumétrica en el firewall perimetral FG-Technoma reflejan bloqueos preventivos y efectivos bajo la regla implícita policyid=0 sobre peticiones DNS provenientes de clientes VPN (sati y FABIANACUñA) y de un dispositivo móvil en VLAN304, manteniéndose la postura de seguridad de la red sin indicios de compromiso.
