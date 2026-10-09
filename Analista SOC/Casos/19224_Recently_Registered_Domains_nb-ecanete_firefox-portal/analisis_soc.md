# Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR

## 1. Identificación del Caso
- **ID de Caso:** `19224_Recently_Registered_Domains_nb-ecanete_firefox-portal`
- **ID de Secuencia Stellar:** 19224 y 19333
- **Tenant:** Technoma (`cf73a415c8794884a0c35b458b7c73ae`)
- **Regla Detectada:** `new_registered_domain` (Recently Registered Domains)
- **Táctica / Técnica:** Initial Attempts / XDR NBA (`XTA0002`) - XDR New Domain (`XT2008`)
- **Fecha y Hora de Detección:** 24/09/2026 13:29:36 UTC (10:29:36 Local) y 14:15:55 UTC (11:15:55 Local)
- **Analista Responsable:** Kevin Moraes
- **Veredicto Técnico:** Falso Positivo (Actividad Benigna de Sistema / Telemetría de Navegador)

---

## 2. Descripción y Actores Involucrados
| Parámetro | Detalle de Origen | Detalle de Destino |
| :--- | :--- | :--- |
| **Dirección IP** | `192.168.169.77` | `10.11.1.1` (DNS local) -> CDN Mozilla Fastly |
| **Hostname** | `nb-ecanete.technoma.local` | `ad.technoma.local` (Controlador de Dominio) |
| **VLAN / Red** | VLAN 1101 (`vlan1101`) | Segmento Servidores / Dominio Local |
| **Dominio Consultado**| `firefox-portal-detection.com` | IP Respuestas: `151.101.65.91`, `151.101.193.91`, `151.101.129.91`, `151.101.1.91` |
| **Protocolo y Puerto**| UDP 50569 / 58395 | UDP 53 (DNS) |

---

## 3. Análisis de Causa Raíz
Se identificaron 2 eventos de consulta DNS originados desde el equipo corporativo de usuario `nb-ecanete.technoma.local` (`192.168.169.77`) dirigidos al servidor Active Directory/DNS interno `ad.technoma.local` (`10.11.1.1`), resolviendo el FQDN `firefox-portal-detection.com`.
El motor de correlación de Stellar Cyber generó la alerta debido a que el dominio fue registrado en fecha `2026-07-01T15:40:13Z` (<90 días de antigüedad al momento del evento). 
Sin embargo, `firefox-portal-detection.com` corresponde a la infraestructura oficial y documentada de Mozilla Corporation utilizada por el navegador Mozilla Firefox para la detección automática de portales cautivos y verificación de estado de red (CPD - Captive Portal Detection). Las respuestas retornaron direcciones IP públicas oficiales pertenecientes a la CDN global de Fastly asignada a los servicios de Mozilla, sin indicios de conexiones sospechosas, generación algorítmica de dominios (DGA score 0) ni exfiltración.

---

## 4. Evaluación de Impacto (Triada CIA)
- **Confidencialidad:** 0/10 (Sin compromiso de datos corporativos).
- **Integridad:** 0/10 (No se alteraron configuraciones ni servicios).
- **Disponibilidad:** 0/10 (Operatividad de red y resolución DNS sin afectación).
- **Puntuación Global de Riesgo:** **0.0 / 10 (Insignificante / Falso Positivo)**.

---

## 5. Cierre en Plataforma Stellar Cyber
- **Estado:** `Closed`
- **Resolution Tag:** `False Positive`
- **Comentario de Cierre Condensado:**
> Cierre por Falso Positivo: Las consultas DNS hacia firefox-portal-detection.com desde el endpoint nb-ecanete.technoma.local (192.168.169.77) hacia ad.technoma.local (10.11.1.1) corresponden a la rutina legítima de Mozilla Firefox para la verificación de conectividad y detección de portales cautivos. La regla new_registered_domain activó la detección por registrarse hace menos de 90 días, pero las respuestas resuelven a la CDN oficial de Fastly sin indicios de exfiltración ni DGA, descartándose cualquier vector de compromiso.
