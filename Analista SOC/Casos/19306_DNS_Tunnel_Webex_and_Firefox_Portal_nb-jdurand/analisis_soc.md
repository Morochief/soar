# Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR

## 1. Identificación del Caso
- **ID de Caso:** `19306_DNS_Tunnel_Webex_and_Firefox_Portal_nb-jdurand`
- **ID de Secuencia Stellar:** 19306 y 19631
- **Tenant:** Technoma (`cf73a415c8794884a0c35b458b7c73ae`)
- **Reglas Detectadas:**
  - `dns_tunnel` (DNS Tunneling Anomaly / Exfiltration & Impact - T1048)
  - `new_registered_domain` (Recently Registered Domains / Initial Attempts - XT2008)
- **Fecha y Hora de Detección:** 24/09/2026 14:02:53 UTC (11:02:53 Local) y 15:27:57 UTC (12:27:57 Local)
- **Analista Responsable:** Kevin Moraes
- **Veredicto Técnico:** Falso Positivo (Tráfico Legítimo de Aplicaciones Corporativas / Cisco Webex y Mozilla Firefox)

---

## 2. Descripción y Actores Involucrados
| Parámetro | Detalle de Origen | Detalle de Destino |
| :--- | :--- | :--- |
| **Dirección IP** | `192.168.169.144` | `10.11.1.1` (DNS / AD local) |
| **Hostname** | `nb-jdurand.technoma.local` | `ad.technoma.local` (Controlador de Dominio) |
| **VLAN / Red** | VLAN 1101 (`vlan1101`) | Segmento Servidores / Infraestructura Local |
| **Dominios Involucrados** | `client-logs-a.wbx2.com` / `wbx2.com`, `firefox-portal-detection.com` | Servidores oficiales de Cisco Webex y CDN Fastly (Mozilla) |
| **Protocolo y Puertos** | TCP 49670 / UDP 65403 | TCP/UDP 53 (DNS) |

---

## 3. Análisis de Causa Raíz
Se identificaron 2 eventos correlacionados desde el endpoint de usuario `nb-jdurand.technoma.local` (`192.168.169.144`):
1. **Secuencia 19306 (`dns_tunnel`):** El motor ML alertó sobre un volumen de 415 Bytes de tráfico DNS de alta entropía asociado al dominio `wbx2.com`. La inspección de los payloads del túnel (`prod-achm-registration2.wbx2.com.wxt-registration-ingressgateway-ds.wxtreg-prod-achm-registration2.d71.prod.infra.webex.com.ns-1371.awsdns-43.org`, `mercury-connection-partition0-a`, `locus-a`, `meeting-container-a`) confirma que se trata de nombres FQDN internos de microservicios utilizados de forma nativa por la aplicación cliente Cisco Webex para registro de sesión, descubrimiento de servicios de mensajería (Mercury) y telemetría de logs (`client-logs-a.wbx2.com`).
2. **Secuencia 19631 (`new_registered_domain`):** Consulta DNS hacia `firefox-portal-detection.com`. Alertada por registrarse con menos de 90 días de antigüedad (`2026-07-01`), corresponde al mecanismo oficial de Mozilla Firefox para la detección de portales cautivos de red (CPD), resolviendo en direcciones IP pertenecientes a la CDN oficial de Fastly.

Ambos eventos corresponden a patrones normales de operación de herramientas corporativas y navegadores sin ningún tipo de persistencia anómala, comunicación maliciosa C2 ni exfiltración de datos.

---

## 4. Evaluación de Impacto (Triada CIA)
- **Confidencialidad:** 0/10 (Sin exfiltración ni exposición de información corporativa).
- **Integridad:** 0/10 (Sin alteraciones en sistemas, resolutores ni datos).
- **Disponibilidad:** 0/10 (Resolución DNS y servicios de red operando nominalmente).
- **Puntuación Global de Riesgo:** **0.0 / 10 (Insignificante / Falso Positivo)**.

---

## 5. Cierre en Plataforma Stellar Cyber
- **Estado:** `Closed`
- **Resolution Tag:** `False Positive`
- **Comentario de Cierre Condensado:**
> Cierre por Falso Positivo: Las alertas de dns_tunnel y new_registered_domain generadas sobre nb-jdurand.technoma.local (192.168.169.144) corresponden a tráfico legítimo de software corporativo; la primera refleja registros de servicio y telemetría estándar de Cisco Webex (wbx2.com e infraestructura AWS oficial), mientras que la segunda responde al chequeo automático de conectividad de Mozilla Firefox (firefox-portal-detection.com) resolviendo en la CDN de Fastly, descartándose actividad de exfiltración o vectores adversarios.
