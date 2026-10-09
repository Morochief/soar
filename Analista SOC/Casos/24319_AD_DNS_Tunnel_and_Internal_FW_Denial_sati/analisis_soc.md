# Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR

## 1. Identificación del Caso
- **ID de Caso:** `24319_AD_DNS_Tunnel_and_Internal_FW_Denial_sati`
- **ID de Secuencia Stellar:** 24319, 24320, 24321, 24322, 24323, 24343, 24344, 24345, 24346, 24347, 24348, 24349, 24350, 24355, 24356 (15 eventos correlacionados)
- **Tenant:** Technoma (`cf73a415c8794884a0c35b458b7c73ae`)
- **Sensor:** `technoma-sensor` (`4e3eab0649114a80a089a5d5a078994d`)
- **Reglas Involucradas:**
  - `dns_tunnel` (14 eventos - Machine Learning / Exfiltration)
  - `internal_fw_action` (1 evento - NBA / Firewall Denial Anomaly)
- **Ventana Temporal de Detección:** 25/09/2026 14:46:06 UTC a 14:56:25 UTC (11:46:06 a 11:56:25 Local)
- **Analista Responsable:** Kevin Moraes
- **Veredicto Técnico:** Falso Positivo (Actividad Legítima de Infraestructura Active Directory / Tráfico VPN Bloqueado en Firewall)

---

## 2. Declaración de Cantidad y Desglose Individual del Lote (15 Eventos)

Se procesaron **15 eventos individuales** contenidos en el volcado de telemetría:

1. **Evento 1 (`_seq_no: 24319` | `dns_tunnel`):** Tráfico DNS de 616 Bytes (típico: 20.29 B) entre `10.11.1.1` (`ad.technoma.local`) y `10.11.1.2:53` (`ad2.technoma.local`). Consulta tipo A para `SRV-AZADCONNECT.technoma.local` resuelta en `10.11.1.3`. Payloads detectados: `NB-AINSAURRALDE`, `NB-AMUNOZ`, `NB-ANGELRA2`, `NB-CVELAZQUEZ`, `NB-DFERNANDEZ`.
2. **Evento 2 (`_seq_no: 24320` | `dns_tunnel`):** Tráfico DNS de 544 Bytes (típico: 27.68 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-SFERNANDEZ.technoma.local` resuelta en `192.168.169.120`. Payloads: `NB-ALOVERA`, `NB-AORTELLADO`, `NB-ARESQUIN`, `NB-CSEQUEIRA`, `NB-DGODOY`.
3. **Evento 3 (`_seq_no: 24321` | `dns_tunnel`):** Tráfico DNS de 755 Bytes (típico: 9.5 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `SRV-AZADCONNECT.technoma.local` resuelta en `10.11.1.3`. Payloads: `NB-CFARINA`, `NB-EBENITEZ`, `NB-JSERVIN`, `NB-JSOLIS2`, `NB-KMORAEZ`.
4. **Evento 4 (`_seq_no: 24322` | `dns_tunnel`):** Tráfico DNS de 454 Bytes (típico: 20.67 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-RDUARTE.technoma.local` resuelta en `192.168.169.104`. Payloads: `NB-AGILL`, `NB-CLEIVA`, `NB-DSAAVERA`, `NB-GGIMENEZ`, `NB-LBOBADILLA`.
5. **Evento 5 (`_seq_no: 24323` | `dns_tunnel`):** Tráfico DNS de 538 Bytes (típico: 19.4 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-RVERON.technoma.local` resuelta en `192.168.169.46`. Payloads: `NB-CFARINA`, `NB-GCABANAS`, `NB-JROLON`, `NB-MAIVA`, `NB-MGONZALEZ`.
6. **Evento 6 (`_seq_no: 24350` | `internal_fw_action`):** 535 bloqueos en 5 minutos (típico: 24) registrados por `FG-Technoma` (`FG120GTK24022543`) sobre consultas DNS (UDP/53) desde la IP de SSL-VPN `10.212.134.204` (usuario `sati`, `ssl.root`) hacia `10.11.1.1:53` (`ad.technoma.local`, interfaz `Citrix Servers`), descartadas bajo `policyid=0`.
7. **Evento 7 (`_seq_no: 24343` | `dns_tunnel`):** Tráfico DNS de 603 Bytes (típico: 25.76 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-TMARIN.technoma.local` resuelta en `192.168.169.126`. Payloads: `NB-AARAUJO`, `NB-AGARCIA`, `NB-ARUIZ`, `NB-FROJAS`, `NB-HBAZAN`.
8. **Evento 8 (`_seq_no: 24344` | `dns_tunnel`):** Tráfico DNS de 501 Bytes (típico: 17.45 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-XLEGUIZAMON.technoma.local` resuelta en `192.168.169.43`. Payloads: `NB-AGILL`, `NB-AZORRILLA`, `NB-CGALLARDO`, `NB-CLEIVA`, `NB-JPALACIOS`.
9. **Evento 9 (`_seq_no: 24345` | `dns_tunnel`):** Tráfico DNS de 579 Bytes (típico: 32.67 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-RLLEDO.technoma.local` resuelta en `192.168.169.79`. Payloads: `NB-CFARINA`, `NB-EVERA`, `NB-FBENEGAS`, `NB-GCABANAS`, `NB-MGONZALEZ`.
10. **Evento 10 (`_seq_no: 24346` | `dns_tunnel`):** Tráfico DNS de 428 Bytes (típico: 20.5 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-TMARIN.technoma.local` resuelta en `192.168.169.126`. Payloads: `NB-AARAUJO`, `NB-ARUIZ`, `NB-CLENGUAZA`, `NB-FROJAS`, `NB-HBAZAN`.
11. **Evento 11 (`_seq_no: 24347` | `dns_tunnel`):** Tráfico DNS de 680 Bytes (típico: 30.53 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-AMUNOZ.technoma.local` resuelta en `192.168.169.88`. Payloads: `ad2`, `NB-AGILL`, `NB-AZORRILLA`, `NB-CARANDA`, `NB-CGALLARDO`.
12. **Evento 12 (`_seq_no: 24348` | `dns_tunnel`):** Tráfico DNS de 656 Bytes (típico: 1 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-RDUARTE.technoma.local` resuelta en `192.168.169.104`. Payloads: `NB-ANGELRA2`, `NB-CVELAZQUEZ`, `NB-DFERNANDEZ`, `NB-DLOVERA`, `NB-EBARRIOS`.
13. **Evento 13 (`_seq_no: 24349` | `dns_tunnel`):** Tráfico DNS de 415 Bytes (típico: 24.2 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-SFERNANDEZ.technoma.local` resuelta en `192.168.169.120`. Payloads: `NB-CFARINA`, `NB-EVERA`, `NB-FBENEGAS`, `NB-GCABANAS`, `NB-JROLON`.
14. **Evento 14 (`_seq_no: 24355` | `dns_tunnel`):** Tráfico DNS de 696 Bytes (típico: 17 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-PRIQUELME.technoma.local` resuelta en `192.168.169.72`. Payloads: `NB-ALOVERA`, `NB-ABARRETO`, `NB-CGOMEZ`, `NB-CLSALCEDO`, `NB-DGODOY`.
15. **Evento 15 (`_seq_no: 24356` | `dns_tunnel`):** Tráfico DNS de 622 Bytes (típico: 16.73 B) entre `10.11.1.1` y `10.11.1.2:53`. Consulta tipo A para `NB-RZABALA.technoma.local` resuelta en `192.168.169.21`. Payloads: `NB-NOC1`, `NB-AZORRILLA`, `NB-CARANDA`, `NB-DSAAVERA`, `NB-CLEIVA`.

---

## 3. Descripción y Actores Involucrados
| Parámetro | Grupo 1: DNS Tunneling Anomaly (14 Eventos) | Grupo 2: Firewall Denial Anomaly (1 Evento) |
| :--- | :--- | :--- |
| **Origen** | `10.11.1.1` (`ad.technoma.local` - DC Primario) | `10.212.134.204` (Usuario VPN `sati`, `ssl.root`) |
| **Destino** | `10.11.1.2` (`ad2.technoma.local` - DC Secundario) | `10.11.1.1` (`ad.technoma.local`, `Citrix Servers`) |
| **Protocolo / Puerto** | UDP 53 (DNS) | UDP 53 (DNS) |
| **Volumen / Detección** | 14 alertas de Machine Learning (volúmenes de 415 a 755 Bytes en 5 min) | 1 alerta ML FortiGate (535 bloqueos en 5 min vs 24 típicos) |
| **Acción / Estado** | Tráfico Permitido (Resolución y replicación interna DNS) | Denegado en Firewall FortiGate (`action="deny"`, `policyid=0`) |

---

## 4. Análisis Técnico y Causa Raíz

### A. Falso Positivo Heurístico de Túnel DNS (14 Eventos)
El modelo de Machine Learning `dns_tunnel` de Stellar Cyber evalúa la entropía y el tamaño de las respuestas DNS transmitidas en ventanas de 5 minutos. En este caso, el Controlador de Dominio primario `ad.technoma.local` (`10.11.1.1`) remitió consultas DNS hacia el DC secundario `ad2.technoma.local` (`10.11.1.2`) para resolver nombres NetBIOS de estaciones de trabajo corporativas (`NB-*`) y el servicio de sincronización híbrida (`SRV-AZADCONNECT.technoma.local`).

Todas las consultas obtuvieron respuestas estándar `No Error` con registros de tipo `A` que apuntan a la subred interna de estaciones de trabajo (`192.168.169.0/24`) y servidores centrales (`10.11.1.3`). Los supuestos "payloads" listados por el motor (`NB-AARAUJO`, `NB-CFARINA`, `NB-EVERA`, etc.) son simplemente los nombres de host de los equipos corporativos de los funcionarios de Technoma registrados en la base de datos de Active Directory. No existe canal encubierto, codificación Base64, exfiltración ni dominio malicioso externo.

### B. Bloqueo en Firewall de Cliente VPN (1 Evento)
El usuario `sati`, correspondiente al proveedor externo autorizado para soporte y desarrollo sobre Odoo, se conectó al concentrador SSL-VPN recibiendo la IP dinámica `10.212.134.204`. El cliente intentó resolver nombres DNS consultando directamente al DC `10.11.1.1:53` a través de la interfaz `ssl.root`. 

El firewall perimetral `FG-Technoma` (`FG120GTK24022543`) bloqueó de manera sistemática las 535 solicitudes bajo la regla implícita de denegación (`policyid=0`), impidiendo que el túnel VPN alcance el segmento `Citrix Servers` en ese puerto. El firewall actuó con estricto apego a las políticas de seguridad perimetral, descartando el tráfico no autorizado sin riesgo alguno para la infraestructura.

---

## 5. Evaluación de Impacto (Tríada CIA)
- **Confidencialidad:** 0/10 (Sin compromiso de credenciales ni exfiltración de información).
- **Integridad:** 0/10 (Sin modificaciones de registros DNS ni evasión de controles de seguridad).
- **Disponibilidad:** 0/10 (Operación normal y continua de los Controladores de Dominio y servicios de red).
- **Puntuación Global de Riesgo:** **0.0 / 10 (Insignificante / Falso Positivo Operativo)**.

---

## 6. Veredicto y Confianza Analítica
```json
{
  "veredicto": "False Positive",
  "categoria": "Ruido Heuristico de Entropia DNS / Ruido Operativo de Enrutamiento VPN",
  "confianza_analitica": "100%",
  "justificacion": "Las 14 alertas de dns_tunnel reflejan resoluciones DNS legitimas de estaciones corporativas (NB-*) y SRV-AZADCONNECT entre los dos controladores de dominio de Technoma (10.11.1.1 y 10.11.1.2). El evento de firewall denial corresponde a bloqueos normales por policyid=0 del FortiGate sobre peticiones DNS del usuario VPN sati (10.212.134.204)."
}
```

---

## 7. Fila Única para Bitácora de Excel

| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc.) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 25/09/2026 11:56 | Kevin Moraes | Technoma | 24319 | technoma-sensor / new_ml | - | Baja | dns_tunnel / internal_fw_action | Replicación DNS entre Controladores de Dominio y Bloqueo VPN sati en FortiGate | ad.technoma.local (10.11.1.1), ad2.technoma.local (10.11.1.2), FG-Technoma, usuario sati (10.212.134.204) | Lote de 15 eventos (14 dns_tunnel y 1 internal_fw_action). FP operativo: 14 anomalias de tunel DNS por consultas y replicacion legitima de endpoints NetBIOS (NB-*) y SRV-AZADCONNECT entre DCs (10.11.1.1 y 10.11.1.2). 1 evento de 535 bloqueos de consultas DNS en FortiGate para usuario VPN sati denegado por policyid:0. Sin exfiltracion ni compromiso. | DNS UDP/53 queries NetBIOS y FortiGate syslog (proto: 17, dstport: 53, policyid: 0, action: deny, user: sati) | Cerrar en plataforma y aplicar tuning en regla de Machine Learning dns_tunnel para trafico inter-DC. | Cerrado | - | No | - | PB 5.2 |

---

## 8. Instrucción de Cierre en Plataforma Stellar Cyber
* **Estado:** `Closed`
* **Resolution Tag:** `False Positive`
* **Comentario de Cierre Maestro Unificado:**
> Cierre por Falso Positivo: Las anomalías de túnel DNS identificadas entre el Controlador de Dominio primario ad.technoma.local (10.11.1.1) y el secundario ad2.technoma.local (10.11.1.2) obedecen a tráfico legítimo de resolución de nombres y replicación interna de estaciones de trabajo corporativas (NB-*) y el servidor SRV-AZADCONNECT.technoma.local, descartándose canales encubiertos o fuga de información. Asimismo, el evento de denegación volumétrica en el firewall perimetral FG-Technoma corresponde a consultas DNS generadas desde la IP SSL-VPN 10.212.134.204 del proveedor externo autorizado sati, las cuales fueron descartadas de forma segura y preventiva por la regla implícita policyid=0 sin comprometer la postura de seguridad de la red.
