# INFORME FORENSE SOC & THREAT HUNTING: CAMPAÑA PHISHING NETLIFY SUBDOMAINS

**Fecha del Dictamen:** 20 de Octubre de 2026  
**Investigador:** Kevin Moraes (Auditoría Forense Fuera de Turno)  
**Plataforma / Fuentes:** Stellar Cyber OpenXDR, Suricata IDS, URLScan.io, ANY.RUN Sandbox, VirusTotal API, AbuseIPDB  
**Tenants Afectados:** Technoma (`e511c3fc54cd4d668bb67612c2ef4b04`)  
**Clasificación:** Incidente Potencial / Phishing - Credential Harvesting (MITRE ATT&CK: TA0001 - T1566)  
**Estado:** Investigado / Requiere Contención Preventiva de Credenciales  

---

## 1. Resumen Ejecutivo
Durante la revisión rutinaria de telemetría y auditoría del panel de **Intrusion Signatures (IDS)** en Stellar Cyber, se detectaron alertas críticas correspondientes a la firma:
`HUNTING Suspicious Netlify Hosted DNS Request - Possible Phishing Landing`.

Tras un análisis exhaustivo con herramientas de inteligencia de amenazas (CTI), correlación profunda de tráfico de red (ADR e Interflow) e inspección en vivo de infraestructura externa, se determinó que **la red de Technoma fue objeto de navegación hacia subdominios efímeros de Netlify comúnmente utilizados para el robo de credenciales**.

---

## 2. Indicadores de Compromiso (IoCs)

| Indicador | Tipo | Categoría / Veredicto | Detalle de Infraestructura |
| :--- | :---: | :---: | :--- |
| `unruffled-shannon-1a7413.netlify.app` | FQDN | **Malicioso / Phishing** | Clasificado como Phishing activo en Sandbox ANY.RUN. Actualmente en estado **HTTP 404 (Takedown)** verificado en URLScan.io (`01a15953-53af-76fd-8dfe-9146a8098320`). |
| `sage-crumble-d13d8c.netlify.app` | FQDN | **Sospechoso / Phishing** | Subdominio efímero Netlify consultado el 20-10-2026. Actualmente en estado **HTTP 404 (Takedown)**. |
| `54.232.119.62` | IPv4 | CDN / Hosting | AWS Data Services São Paulo, Brasil (AS16509). IP Anycast de Netlify. |
| `2a05:d014:58f:6200::259` | IPv6 | CDN / Hosting | Amazon AWS Frankfurt, Alemania (AS16509). IP Anycast de Netlify. |

---

## 3. Cronología y Equipos Involucrados en Technoma

### Caso 1: Notebook `NB-SDONCELL` (Impacto Moderado - Atención Requerida)
* **Usuario:** `sdoncell` (S. Doncell)
* **Host:** `nb-sdoncell.technoma.local` (`192.168.169.101`)
* **Fecha y Hora:** 12 de Octubre de 2026, 20:50:43 UTC (17:50 PYT)
* **Evento:**
  1. El host resolvió vía DNS interno (`10.11.1.1:53`) el dominio `unruffled-shannon-1a7413.netlify.app`.
  2. Inmediatamente estableció dos flujos bidireccionales TLS/HTTPS hacia `54.232.119.62:443`:
     * Flujo 1 (Puerto efímero 59656): `5,344 bytes In` / `3,261 bytes Out`.
     * Flujo 2 (Puerto efímero 51751): `4,530 bytes In` / `3,350 bytes Out`.
* **Dictamen Forense:** En esa fecha el sitio de phishing se encontraba activo en Netlify antes del takedown. El volumen de subida (3.2 KB) es consistente con el envío de un formulario HTTP POST o carga de sesión. **Existe riesgo de compromiso de credenciales corporativas.**

### Caso 2: Notebook `NB-WGONZALEZ` (Sin Impacto / Intento Fallido)
* **Usuario:** W. González
* **Host:** `nb-wgonzalez.technoma.local` (`192.168.169.30`)
* **Fecha y Hora:** 20 de Octubre de 2026, 12:30:02 UTC (09:30 PYT)
* **Evento:**
  1. El host resolvió vía DNS el dominio `sage-crumble-d13d8c.netlify.app`.
  2. Intentó la conexión HTTPS hacia la CDN de Netlify.
* **Dictamen Forense:** El sitio ya se encontraba dado de baja por Netlify (HTTP 404). No hubo intercambio de credenciales exitoso.

---

## 4. Dictamen de Amenaza y Correlación
Los actores de amenazas utilizan plataformas PaaS/CDN gratuitas (como Netlify, Vercel y Cloudflare Pages) para desplegar páginas de clonación de Microsoft 365, Webmail o portales bancarios con certificados TLS válidos (DigiCert / Let's Encrypt). 
La campaña se dispersa mediante enlaces en correos fraudulentos o chats. Aunque la plataforma receptora dio de baja el sitio días después, la interacción inicial de `nb-sdoncell` amerita contención preventiva.

---

## 5. Medidas de Remediación y Pasos a Seguir

1. **Gestión de Identidades:**
   * **Forzar reseteo de credenciales inmediato** para el usuario `sdoncell` en Active Directory y Microsoft 365.
   * Revocar tokens de sesión activos de M365 (Revoke Sessions).
2. **Revisión en Endpoint (Cortex XDR):**
   * Inspeccionar si se descargaron archivos ejecutables o scripts en `nb-sdoncell.technoma.local` alrededor de las 17:50 PYT del 12-10-2026.
3. **Control Perimetral y DNS (FortiGate / Stellar Cyber):**
   * Bloquear o enviar a advertencia estricta en el Firewall la resolución de subdominios con el patrón `*.netlify.app` que no correspondan a aplicaciones legítimas de desarrollo de la empresa.

---
*Reporte generado y documentado automáticamente en la base de conocimiento forense del SOC Technoma.*
