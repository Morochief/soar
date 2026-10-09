### 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `True Positive (Blocked)`, `Threat Intercepted`, `Web Filtering`, `Policy Violation`, `Mal/HTMLGen-A`, `Sophos Endpoint`

### Análisis Lote de Eventos (4 Eventos Recibidos)
Se han analizado de forma secuencial los 4 eventos incluidos en el volcado de alertas de Interflow para el host `CJPPA20260814` (`172.16.202.17`), usuario `CAJAANDE\lortellado`.

- **Evento 1 (ID Anomaly: `7KK8haABI3UnQyDO0RSK`):** `Event::Endpoint::WebFilteringBlocked` - Acceso bloqueado a `uhg.edu.py` por amenaza `Mal/HTMLGen-A`.
- **Evento 2 (ID Anomaly: `7aK8haABI3UnQyDO0RSK`):** `Event::Endpoint::WebControlViolation` - Acceso bloqueado a `https://translate.google.com` por categoría `Proxies & Translators`.
- **Evento 3 (ID Anomaly: `SaLBhaABI3UnQyDOYjge`):** Duplicado exacto del Evento 1 (mismo `sophos.id: 75c1abfb-91fb-4994-9685-5bf4cb8d93b9`, retransmisión de log con `write_time` posterior).
- **Evento 4 (ID Anomaly: `SqLBhaABI3UnQyDOYjge`):** Duplicado exacto del Evento 2 (mismo `sophos.id: 3dbaddc5-9f68-4689-b9af-efbccd6f8f3d`, retransmisión de log con `write_time` posterior).

---

### 🎯 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Alerta Detectada:** `Sophos Event: User Execution` (`Event::Endpoint::WebFilteringBlocked` y `Event::Endpoint::WebControlViolation`).
* **Activos Involucrados:** Host `CJPPA20260814` (`172.16.202.17`) - Dominio `CAJAANDE` (Usuario: `CAJAANDE\lortellado`).
* **Comportamiento Anómalo:** El agente Sophos Endpoint en la estación de trabajo interceptó dos intentos de navegación:
  1. Conexión hacia `uhg.edu.py` (Universidad Hispano Guaraní, IP `149.50.148.67`), clasificada con la firma maliciosa `Mal/HTMLGen-A`.
  2. Conexión hacia `https://translate.google.com`, clasificada bajo la categoría restringida `Proxies & Translators`.
* **Causalidad Probable:** Navegación web legítima del usuario institucional que intentó ingresar al portal académico `uhg.edu.py` (el cual sufre una infección activa en su gestor de contenidos WordPress o inyección de scripts maliciosos tipificados por Sophos como `Mal/HTMLGen-A`, confirmado por 12 motores en VirusTotal y Google Safe Browsing). Paralelamente intentó usar Google Translate, bloqueado por directiva local. Ambos accesos fueron frustrados en el perímetro del endpoint por Sophos.

---

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Destino / Detalle | Actual | Typical | Observación Forense |
|---|---|---|---|---|---|---|
| 2026-09-09 10:33:31 | 2026-09-09 07:33:31 | WebFilteringBlocked | `uhg.edu.py` (`Mal/HTMLGen-A`) | 1 | 0 | Bloqueo preventivo de exploit/código web malicioso. |
| 2026-09-09 10:33:55 | 2026-09-09 07:33:55 | WebControlViolation | `https://translate.google.com` | 1 | 0 | Bloqueo administrativo por política de categorías web. |
| 2026-09-09 10:33:51 | 2026-09-09 07:33:51 | WebFilteringBlocked | `uhg.edu.py` | 1 | 0 | Reemisión en índice aella-syslog (duplicado). |
| 2026-09-09 10:34:14 | 2026-09-09 07:34:14 | WebControlViolation | `translate.google.com` | 1 | 0 | Reemisión en índice aella-syslog (duplicado). |

---

### 🔬 Desglose Técnico y Disección Forense

#### Evento 1 & 3: Bloqueo de Amenaza Web (`uhg.edu.py` / `Mal/HTMLGen-A`)
* **Proceso Actor:** Navegador web en sesión activa de `CAJAANDE\lortellado`.
* **Módulo de Protección:** Sophos Web Protection / Web Filtering.
* **Firma Detectada:** `Mal/HTMLGen-A` (Firma heurística genérica de Sophos para páginas HTML con scripts maliciosos, iframes invisibles, redireccionadores de exploit kits o webs WordPress comprometidas).
* **Destino Analizado:** `uhg.edu.py` -> IP `149.50.148.67` (Hosting en Dattatec.com S.R.L., Argentina).
* **Corroboración Externa de Inteligencia de Amenazas:**
  - **VirusTotal:** 12/89 motores detectan el dominio como malicioso/phishing (Sophos, Fortinet, Kaspersky, Forcepoint, etc.).
  - **Google Safe Browsing:** Marcado formalmente como `Malicious for uhg.edu.py`.
  - **Tecnología del Sitio:** CMS WordPress con múltiples librerías JS desactualizadas (vector frecuente de infección por web injection / defacement).
* **Estado de la Conexión:** **Blocked**. El tráfico fue interceptado antes de renderizarse o ejecutarse en el navegador.

#### Evento 2 & 4: Bloqueo por Control de Navegación (`translate.google.com`)
* **Módulo de Protección:** Sophos Web Control.
* **Regla Aplicada:** Restricción a la categoría `Proxies & Translators`.
* **Destino:** `https://translate.google.com`.
* **Estado:** **Blocked**. Política corporativa estándar en CAJAANDE.

```json
/* Payload / Evidencia Principal */
{
  "payload_type": "URL / Domain / Web Threat",
  "payload_value": "uhg.edu.py / https://translate.google.com",
  "payload_hash": "N/A (Intercepción en capa de red/URL)",
  "payload_firma": "Mal/HTMLGen-A | Category: Proxies & Translators",
  "payload_accion": "Blocked (Acceso denegado en el endpoint)",
  "payload_destino": "149.50.148.67 (uhg.edu.py) / Google Services"
}
```

#### Hipótesis Formuladas
| Hipótesis | Evaluación | Veredicto |
|---|---|---|
| 1. Compromiso activo del endpoint por malware / C2 | No se observaron ejecuciones de binarios, descargas de archivos ni persistencia; Sophos bloqueó la conexión a nivel HTTP/socket. | Descartada |
| 2. Compromiso o infección en servidor externo (`uhg.edu.py`) | Confirmado por VirusTotal (12 motores), Google Safe Browsing y CMS WordPress infectado. | Confirmada |
| 3. Violación de política intencional maliciosa por el usuario | Navegación típica de usuario intentando consultar un portal universitario y traductor. | Descartada |

---

### 🧠 ¿Por qué es (o no es) una Amenaza?
**Para el Endpoint interno es un Verdadero Positivo Bloqueado (True Positive - Prevented / No Impact):**
La amenaza en `uhg.edu.py` es real (código web malicioso confirmado externamente), pero el control de seguridad de Sophos actuó de forma exitosa impidiendo la descarga y renderizado del payload infectado. No hubo brecha ni infección local. El bloqueo de Google Translate es una simple aplicación de política corporativa.

---

### Cierre Maestro Unificado

### 🛡️ Análisis de Impacto CIA Triad
```json
{
  "Confidentiality": "Sin impacto. No se produjo exfiltración ni robo de credenciales.",
  "Integrity": "Sin impacto. No se ejecutó código malicioso en el endpoint CJPPA20260814.",
  "Availability": "Sin impacto en la infraestructura interna. Restricción preventiva y conforme a políticas hacia sitios externos."
}
```

### ⚖️ Veredicto y Confianza Analítica
```json
{
  "Veredicto": "True Positive - Threat Mitigated / Blocked",
  "Confianza": "100%",
  "Motivo": "La amenaza Mal/HTMLGen-A en el dominio uhg.edu.py fue bloqueada preventivamente en capa web por Sophos Endpoint. El sitio presenta compromiso activo en Internet pero no afectó la red interna."
}
```

### 📉 Indicador de Fatiga de Alertas
```json
{
  "Fatiga": "Baja",
  "Razón": "Alertas generadas por intercepciones exitosas de controles de seguridad de endpoint (Web Protection)."
}
```

### 📘 Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
|---|---|
| Detección y Análisis | Correlación de telemetría de Sophos, validación de reputación en VirusTotal, urlscan y whois. |
| Contención, Erradicación y Recuperación | Contención automática ejecutada por Sophos (tráfico bloqueado). No se requiere remediación en el host. |
| Actividad Post-Incidente | Cierre de alerta en Stellar Cyber y Sophos Central. Monitoreo pasivo del endpoint. |

---

### 📚 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
|---|---|---|
| PB-007 | Malware / Malicious URL Blocked at Endpoint | Intercepción preventiva de sitios catalogados como maliciosos mediante firmas de filtrado web sin compromiso del activo. |

---

### 🏷️ Resolution Tag para Stellar Cyber
`True Positive` - Mitigated / Policy Violation

---

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
`09/09/2026 08:06 | Analista SOC | CAJAANDE | 7KK8haABI3UnQyDO0RSK | Sophos Events (Stellar Cyber) | - | Baja | Sophos Event: User Execution (WebFilteringBlocked / WebControlViolation) | Bloqueo preventivo de amenaza Mal/HTMLGen-A en uhg.edu.py y política de Web Control en translate.google.com | CJPPA20260814 (172.16.202.17) | True Positive (Mitigado). El agente Sophos en CJPPA20260814 bloqueo acceso a uhg.edu.py por deteccion Mal/HTMLGen-A (sitio universitario con WordPress comprometido segun VirusTotal y Google Safe Browsing) y bloqueo translate.google.com por politica Proxies & Translators. Sin compromiso en el endpoint. | Sophos Central | Ninguna accion requerida en el endpoint; control exitoso | Cierre | - | No | - | PB-007`

---

### 💻 Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** True Positive / Mitigated
* **Comentario final:** El incidente agrupa eventos de protección de navegación web para el equipo `CJPPA20260814` (`172.16.202.17`), usuario `CAJAANDE\lortellado`. El motor Web Protection de Sophos bloqueó exitosamente la conexión hacia `uhg.edu.py` clasificada bajo la firma `Mal/HTMLGen-A`. Se corroboró mediante OSINT (VirusTotal 12/89 y Google Safe Browsing) que el sitio externo cuenta con inyecciones de código malicioso activo. Asimismo, se registró el bloqueo por política web a `translate.google.com` (categoría `Proxies & Translators`). Ambos eventos fueron contenidos de forma preventiva en el endpoint sin llegar a ejecutarse en el equipo. Sin indicios de compromiso. Caso cerrado como True Positive Mitigado.

---

### 🔬 Desglose Ultra Quirúrgico

* **Capa 1: Endpoint y Contexto de Identidad (`computer_name` / `user.name`)**
  - Estación: `CJPPA20260814` (`172.16.202.17`).
  - Identidad de red: `CAJAANDE\lortellado` (UID Sophos: `6926fefb72291113e7f8ca88`).
* **Capa 2: Módulos de Protección y Eventos (`sophos.type` / `threat.name`)**
  - Módulo 1: `Event::Endpoint::WebFilteringBlocked`. Detección activa de firma web `Mal/HTMLGen-A` al intentar conectar con `uhg.edu.py`.
  - Módulo 2: `Event::Endpoint::WebControlViolation`. Aplicación de directiva administrativa sobre `translate.google.com`.
* **Capa 3: Mapeo MITRE ATT&CK en SIEM (`xdr_event.technique`)**
  - Táctica: Execution (`TA0002`).
  - Técnica: User Execution (`T1204`).
  - Mapeo del SIEM: Stellar Cyber clasifica las alertas reportadas por Sophos como User Execution porque derivan de una interacción en el navegador disparada por el usuario.
* **Capa 4: CTI & OSINT del Destino**
  - FQDN: `uhg.edu.py` -> A Record: `149.50.148.67` (ASN 27823 Dattatec, Argentina).
  - Reputación: 12 detecciones en VT y Google Safe Browsing positivo para malware.

**Resumen Quirúrgico Final:** La telemetría demuestra la efectividad de las capas perimetrales del agente Sophos en el endpoint. El usuario intentó acceder a un dominio legítimo institucional de educación en Paraguay que se encuentra vulnerado externamente con malware web (`Mal/HTMLGen-A`). Sophos cortó la conexión al vuelo, imposibilitando la descarga de código malicioso o la ejecución de exploits en la memoria del navegador. No se requieren tareas de erradicación ni aislamiento sobre `172.16.202.17`.
