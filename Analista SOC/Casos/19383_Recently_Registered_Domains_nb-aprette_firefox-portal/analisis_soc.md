# Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR

## 1. Identificación del Caso
- **ID de Caso:** `19383_Recently_Registered_Domains_nb-aprette_firefox-portal`
- **ID de Secuencia Stellar:** 19383, 19384, 19400, 19415, 19414, 19434, 19447, 19448, 19481 (9 eventos correlacionados)
- **Tenant:** Technoma (`cf73a415c8794884a0c35b458b7c73ae`)
- **Regla Detectada:** `new_registered_domain` (Recently Registered Domains)
- **Táctica / Técnica:** Initial Attempts / XDR NBA (`XTA0002`) - XDR New Domain (`XT2008`)
- **Ventana Temporal de Detección:** 24/09/2026 14:38:30 UTC a 15:07:52 UTC (11:38:30 a 12:07:52 Local)
- **Analista Responsable:** Kevin Moraes
- **Veredicto Técnico:** Falso Positivo (Actividad Benigna de Sistema / Telemetría de Navegador)

---

## 2. Descripción y Actores Involucrados
| Parámetro | Detalle de Origen | Detalle de Destino |
| :--- | :--- | :--- |
| **Dirección IP** | `192.168.169.118` | `10.11.1.1` (DNS local) -> CDN Fastly / Mozilla |
| **Hostname** | `nb-aprette.technoma.local` | `ad.technoma.local` (Controlador de Dominio) |
| **VLAN / Red** | VLAN 1101 (`vlan1101`) | Segmento Servidores / Dominio Local |
| **Dominio Consultado**| `firefox-portal-detection.com` (Consultas tipo A y AAAA) | IPs de Respuesta: `151.101.1.91`, `151.101.65.91`, `151.101.129.91`, `151.101.193.91` |
| **Protocolo y Puerto**| UDP 49665, 50898, 53941, 56227, 57820, 58414, 59318, 61570, 61815 | UDP 53 (DNS) |

---

## 3. Análisis de Causa Raíz
Se identificaron 9 eventos de consultas DNS (tipos A y AAAA) originadas desde el equipo de usuario `nb-aprette.technoma.local` (`192.168.169.118`) dirigidas al resolver interno de la organización `ad.technoma.local` (`10.11.1.1:53 UDP`) para resolver el nombre de dominio `firefox-portal-detection.com`.
El motor de analítica de comportamiento de red (NBA) de Stellar Cyber disparó la regla `new_registered_domain` debido a que la fecha de creación del dominio es `2026-07-01T15:40:13Z` (<90 días de antigüedad).
Sin embargo, `firefox-portal-detection.com` constituye la infraestructura oficial de Mozilla Corporation para la función nativa de Detección de Portales Cautivos (*Captive Portal Detection*) implementada en el navegador Mozilla Firefox para verificar el estado de conexión a Internet de la estación de trabajo. Las respuestas retornaron rangos de direcciones IP legítimas de la CDN de Fastly asignadas a Mozilla, con reputación limpia, sin entropía maliciosa (DGA score 0) ni evidencia de actividad de mando y control (C2).

---

## 4. Evaluación de Impacto (Triada CIA)
- **Confidencialidad:** 0/10 (Sin filtración ni exfiltración de credenciales o datos).
- **Integridad:** 0/10 (Integridad de registros DNS y del endpoint inalterada).
- **Disponibilidad:** 0/10 (Servicio de navegación y resolución operativa normal).
- **Puntuación Global de Riesgo:** **0.0 / 10 (Insignificante / Falso Positivo)**.

---

## 5. Cierre en Plataforma Stellar Cyber
- **Estado:** `Closed`
- **Resolution Tag:** `False Positive`
- **Comentario de Cierre Condensado:**
> Cierre por Falso Positivo: Las consultas DNS hacia firefox-portal-detection.com emitidas por el endpoint nb-aprette.technoma.local (192.168.169.118) hacia ad.technoma.local (10.11.1.1) corresponden a la rutina estándar del navegador Mozilla Firefox para la detección automática de portales cautivos y verificación de acceso a Internet. La alerta new_registered_domain se generó debido a la fecha de registro reciente (<90 días), pero el destino corresponde a infraestructura legítima de Mozilla/Fastly CDN con reputación favorable y DGA score 0, descartándose actividad maliciosa.
