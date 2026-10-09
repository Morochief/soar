# Informe de Análisis SOC - Lote Interflow (11 Eventos)
**ID del Caso:** `19558_AD_DNS_Tunnel_Telegram_and_Firefox_Portal`  
**Fecha de Análisis:** 2026-09-24 12:26:00 (UTC-03:00)  
**Analista Responsable:** Nivel 1 SOC / DFIR  
**Tenant / Organización:** `Technoma` (`cf73a415c8794884a0c35b458b7c73ae`)  
**Sensor:** `technoma-sensor` (`4e3eab0649114a80a089a5d5a078994d`)  

---

## 1. Declaración de Cantidad y Desglose del Lote
Se procesaron **11 eventos de seguridad** correlacionados originados desde el Controlador de Dominio principal (`ad.technoma.local`):

1. **`_seq_no: 19559` (`new_registered_domain`):** Consulta DNS para `firefox-portal-detection.com` desde `10.11.1.1` hacia `10.11.1.2` (puerto 53 UDP).
2. **`_seq_no: 19558` (`new_registered_domain`):** Consulta DNS recursiva para `firefox-portal-detection.com` desde `10.11.1.1` hacia Google DNS `8.8.4.4`.
3. **`_seq_no: 19568` (`exploit_attempt_priv_priv`):** Disparo de regla IDS Suricata SID `2071627` (`INFO Observed Telegram Domain in DNS Lookup (telegram .org)`) para el registro HTTPS de `kws2-1.web.telegram.org` entre `10.11.1.1` y `10.11.1.2`. Spike de Machine Learning de severidad acumulada (16.5 vs 2.0).
4. **`_seq_no: 19569` (`exploit_attempt_priv_pub`):** Disparo de regla IDS Suricata SID `2071627` para el registro A de `kws2-1.web.telegram.org` desde `10.11.1.1` hacia `8.8.4.4`. Spike de severidad acumulada (6.0 vs 1.5).
5. **`_seq_no: 19560` (`dns_tunnel`):** Tráfico DNS de 627 Bytes entre `10.11.1.1` y `10.11.1.2` resolviendo `NB-RLLEDO.technoma.local` (`192.168.169.79`). Payloads detectados: `AD2`, `NB-ACHAMORRO`, `NB-ADIARTE`, `NB-AZORRILLA`, `NB-CARANDA`.
6. **`_seq_no: 19562` (`dns_tunnel`):** Tráfico DNS de 576 Bytes entre `10.11.1.1` y `10.11.1.2` resolviendo `NB-LARCE.technoma.local` (`192.168.169.74`). Payloads: `NB-ARESQUIN`, `NB-CFARINA`, `NB-DAQUINO`, etc.
7. **`_seq_no: 19563` (`dns_tunnel`):** Tráfico DNS de 448 Bytes entre `10.11.1.1` y `10.11.1.2` resolviendo `NB-TIBANEZ.technoma.local` (`192.168.169.82`). Payloads: `NB-ABARRETO`, `NB-APAREDES`, `NB-TMARIN`, etc.
8. **`_seq_no: 19564` (`dns_tunnel`):** Tráfico DNS de 661 Bytes entre `10.11.1.1` y `10.11.1.2` resolviendo `NB-RZABALA.technoma.local` (`192.168.169.10`). Payloads: `AD2`, `NB-AZORRILLA`, `NB-DFERNANDEZ`, etc.
9. **`_seq_no: 19565` (`dns_tunnel`):** Tráfico DNS de 546 Bytes entre `10.11.1.1` y `10.11.1.2` resolviendo `NB-WGONZALEZ.technoma.local` (`192.168.169.32`). Payloads: `NB-APRETTE`, `NB-ARESQUIN`, `NB-BBENITEZ`, etc.
10. **`_seq_no: 19566` (`dns_tunnel`):** Tráfico DNS de 499 Bytes entre `10.11.1.1` y `10.11.1.2` resolviendo `NB-MLOPEZ.technoma.local` (`192.168.169.145`). Payloads: `NB-ASAUCEDO`, `NB-DRODAS`, `NB-EVERA`, etc.
11. **`_seq_no: 19576` (`new_registered_domain`):** Consulta DNS adicional para `firefox-portal-detection.com` desde `10.11.1.1` hacia `8.8.4.4`.

---

## 2. Análisis Técnico Detallado

### A. Anomalías de Túnel DNS (6 Eventos)
- **Activos:** `10.11.1.1` (`ad.technoma.local`) $\leftrightarrow$ `10.11.1.2` (`ad2.technoma.local`) en puerto 53 UDP.
- **Naturaleza:** Tráfico de replicación, reenvío y resolución de nombres de Active Directory DNS. Los nombres de dominio consultados (`NB-RLLEDO`, `NB-LARCE`, `NB-TIBANEZ`, `NB-RZABALA`, `NB-WGONZALEZ`, `NB-MLOPEZ`) corresponden a notebooks de usuarios corporativos dentro de la red `192.168.169.0/24`.
- **Causa del Disparo:** Las respuestas DNS contienen registros adicionales de máquinas de la red (`AD2`, `NB-*`). El algoritmo heurístico de Stellar Cyber evalúa la entropía textual y la densidad de caracteres, clasificando erróneamente respuestas multifirma de Active Directory como exfiltración de datos. Falso Positivo conocido de la plataforma.

### B. Supuestos Intentos de Explotación por Firma Suricata (2 Eventos)
- **Firma IDS:** SID `2071627` - `ET INFO Observed Telegram Domain in DNS Lookup (telegram .org)`.
- **Clasificación Original:** `classtype: misc-activity`, Severidad: `Informational` / `Low`.
- **Consulta:** `kws2-1.web.telegram.org` (tipos HTTPS y A).
- **Causa del Disparo:** El sensor detectó un volumen inusual de consultas DNS hacia la infraestructura de Telegram Web en un lapso de 5 minutos (33 eventos internos y 12 externos). El módulo de Machine Learning (`new_ml`) acumuló el puntaje y elevó la alerta genérica `exploit_attempt_priv_priv` y `priv_pub`. No existe ningún intento de intrusión ni vulnerabilidad; es únicamente tráfico informativo de resolución DNS de navegación de usuario.

### C. Dominios Recientemente Registrados (3 Eventos)
- **Dominio:** `firefox-portal-detection.com` (Fecha de registro: 2026-07-01, <90 días).
- **IPs Resueltas:** Red oficial de CDN de Mozilla en Fastly (`151.101.65.91`, `151.101.129.91`, etc.).
- **Diagnóstico:** Peticiones automáticas generadas por navegadores Mozilla Firefox en la red interna para comprobar la presencia de portales cautivos. Tráfico benigno y esperado.

---

## 3. Evaluación de Impacto y Tríada CIA
- **Confidencialidad (0/10):** No existe exfiltración; los registros DNS pertenecen al entorno interno.
- **Integridad (0/10):** Las respuestas DNS son autoritativas y provienen de los controladores de dominio oficiales.
- **Disponibilidad (0/10):** Sin degradación del servicio DNS ni de conectividad.
- **Puntuación de Riesgo Global:** **0.0 / 10** (Insignificante / Tráfico Benigno de Red y Falsos Positivos de ML).

---

## 4. Veredicto Final y Recomendación
- **Veredicto:** **Falso Positivo** (Replicación DNS Interna, Firma Suricata Informativa y Telemetría de Navegador).
- **Acciones:**
  1. Cerrar los 11 eventos en Stellar Cyber de forma unificada bajo la etiqueta de Falso Positivo.
  2. Mantener la regla de exclusión de umbral de entropía DNS entre los controladores de dominio `10.11.1.1` y `10.11.1.2`.

---

## 5. Instrucción de Cierre en Stellar Cyber
* **Estado:** `Closed`
* **Resolution Tag:** `False Positive`
* **Comentario de Cierre (Condensado):**
> Alerta descartada como **Falso Positivo**. El lote de 11 eventos refleja actividad operativa benigna del Controlador de Dominio `ad.technoma.local` (`10.11.1.1`). Las detecciones de `dns_tunnel` hacia `ad2.technoma.local` (`10.11.1.2`) son falsos positivos estadísticos del motor de entropía provocados por la resolución y replicación DNS interna de nombres de equipos corporativos (`NB-*`). Asimismo, las alertas de exploit `priv_priv`/`priv_pub` derivan de un incremento en consultas informativas de DNS para `kws2-1.web.telegram.org` (firma Suricata SID 2071627, clasificada erróneamente por anomalía de volumen acumulado), mientras que los eventos de `new_registered_domain` corresponden a comprobaciones estándar de portal cautivo de Mozilla Firefox (`firefox-portal-detection.com`). No existe túnel encubierto, explotación ni compromiso de seguridad.
