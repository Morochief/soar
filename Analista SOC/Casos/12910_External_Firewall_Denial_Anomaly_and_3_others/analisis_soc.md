### 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `False Positive`, `Firewall Denial`, `Fortinet Cloud Services`, `FortiGuard DoT`, `Egress Policy`

### Análisis Lote de Eventos (4 Eventos Recibidos)
Se han analizado de forma individual y secuencial los 4 eventos de denegación perimetral registrados por el sensor de red.

---

### 🎯 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Alerta Detectada:** External Firewall Denial Anomaly (12910).
* **Activos Involucrados:** 
  - **Origen Interno:** Estación de trabajo `192.168.169.131`.
  - **Destinos Externos:** Servidores oficiales de la infraestructura Cloud de Fortinet / FortiGuard:
    1. `96.45.46.46` (Servidor DNS-over-TLS de FortiGuard - Puerto DoT/853)
    2. `141.109.161.95` (`globalproductapi.fortinet.net.geo.fortinet.net` - Puerto HTTPS/443)
    3. `96.45.45.45` (Servidor DNS-over-TLS de FortiGuard - Puerto DoT/853)
    4. `173.243.143.6` (`globalfctupdate.fortinet.net` - Puerto HTTPS/443)
* **Comportamiento Anómalo:** Elevado número de conexiones salientes bloqueadas por el firewall FortiGate (`action="deny"`) en los puertos TCP/853 (DNS-over-TLS) y TCP/443 (HTTPS), registrando entre 166 y 183 denegaciones en intervalos de 5 minutos.
* **Causalidad Probable:** Falso positivo. El agente FortiClient en la máquina `192.168.169.131` intentó conectarse a la API global de productos y servicios de actualización de Fortinet (`globalproductapi.fortinet.net` / `globalfctupdate.fortinet.net`), además de realizar consultas DNS cifradas (DoT) hacia la infraestructura perimetral de FortiGuard (`96.45.45.45` / `96.45.46.46:853`). El firewall denegó la salida por políticas restrictivas en la VLAN local. El modelo estadístico de Stellar Cyber (`external_fw_action`) disparó la anomalía de volumen por los reintentos automáticos del agente.

---

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Origen | Destino / FQDN Fortinet | Acción Firewall |
|---|---|---|---|---|
| 2026-08-02T02:10:00 | 2026-08-01 23:10:00 | `192.168.169.131` | `96.45.46.46:853` (FortiGuard DoT) | **Deny** (166 intentos) |
| 2026-08-02T02:15:00 | 2026-08-01 23:15:00 | `192.168.169.131` | `141.109.161.95:443` (`globalproductapi...`) | **Deny** (181 intentos) |
| 2026-08-02T02:20:00 | 2026-08-01 23:20:00 | `192.168.169.131` | `96.45.45.45:853` (FortiGuard DoT) | **Deny** (174 intentos) |
| 2026-08-02T02:25:00 | 2026-08-01 23:25:00 | `192.168.169.131` | `173.243.143.6:443` (`globalfctupdate...`) | **Deny** (183 intentos) |

---

### 🔬 Desglose Técnico y Disección Forense
* **Proceso / Aplicación:** FortiClient Telemetry, Updates & DoT Resolver (`Fortinet-FortiGuard` / `Fortinet-Web`).
* **Puertos y Protocolos:** TCP 853 (DNS-over-TLS) y TCP 443 (HTTPS).
* **Reputación:** Excelente. Infraestructura oficial global de Fortinet Inc.

**Payload / Evidencia Principal:**
```json
{
  "payload_type": "Firewall Egress Policy Log",
  "payload_value": "globalproductapi.fortinet.net / globalfctupdate.fortinet.net / 96.45.45.45:853",
  "payload_hash": "N/A (Tráfico de red)",
  "payload_firma": "Fortinet-FortiGuard / Fortinet-Web",
  "payload_accion": "DENY (Bloqueado por regla perimetral FortiGate)",
  "payload_destino": "141.109.161.95:443 / 173.243.143.6:443 / 96.45.45.45:853"
}
```

**Contexto del SIEM (Stellar Cyber):**
Las reglas de detección de anomalías perimetrales supervisan el conteo acumulado de denegaciones salientes. Al carecer el segmento `192.168.169.x` de permiso explícito para los endpoints de la API, actualizaciones y resolvedores DoT de Fortinet, el cliente reintenta la conexión, acumulando más de 180 bloqueos en 5 minutos y sobrepasando la línea base típica (`typical: 10`), lo que activa la anomalía perimetral.

### 🧠 ¿Por qué es (o no es) una Amenaza?
**Es un Falso Positivo (Bloqueo de Política de Salida).** No representa actividad maliciosa ni exfiltración de datos. Es un comportamiento legítimo del agente cliente FortiClient intentando resolver DNS de forma cifrada y comunicarse con sus servicios de actualización y API oficiales que es bloqueado por las políticas restrictivas de salida del firewall.

---

### Cierre Maestro Unificado

### 🛡️ Análisis de Impacto CIA Triad
```json
{
  "Confidentiality": "Sin impacto.",
  "Integrity": "Sin impacto.",
  "Availability": "Sin impacto."
}
```

### ⚖️ Veredicto y Confianza Analítica
```json
{
  "Veredicto": "False Positive",
  "Confianza": "100%",
  "Motivo": "Tráfico saliente bloqueado hacia servidores oficiales de API, actualizaciones y DNS-over-TLS de Fortinet (globalproductapi.fortinet.net / globalfctupdate.fortinet.net / 96.45.45.45)."
}
```

### 📉 Indicador de Fatiga de Alertas
```json
{
  "Fatiga": "Baja",
  "Razón": "Reintentos de conexión de agentes de seguridad bloqueados por políticas de salida."
}
```

### 📘 Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
|---|---|
| Detección y Análisis | Inspección de FQDNs y IPs de destino Fortinet. Descarte de amenaza. |
| Erradicación y Recuperación | N/A (Tráfico corporativo). |
| Actividad Post-Incidente | Ajustar políticas perimetrales si se desea permitir el tráfico DoT/API de FortiClient. |

### 📚 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
|---|---|---|
| PB-002 | Manejo de Falsos Positivos | Cierre de anomalías de volumen por bloqueos de política de firewall en tráfico legítimo. |

### 🏷️ Resolution Tag para Stellar Cyber
`False Positive` - Normal Administrative Behavior / Expected Network Policy Block.

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
`02/08/2026 12:51 | Analista | technoma | 12910 | Stellar Cyber | - | Baja | External Firewall Denial Anomaly | Bloqueo de política saliente a servidores FortiGuard API, Update y DoT | 192.168.169.131 | Falso Positivo. El host 192.168.169.131 registró picos de denegación saliente en FortiGate al intentar conectarse a la API de productos y servidor de actualizaciones de Fortinet (globalproductapi.fortinet.net / globalfctupdate.fortinet.net) y DNS cifrado DoT (96.45.45.45:853). Tráfico inofensivo bloqueado por políticas de salida del firewall. Sin compromiso de seguridad. | FortiGate Traffic Log | Ninguna | Cerrado | - | No | - | PB-002`

### 💻 Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario final:** Falso positivo validado. Las 4 alertas del lote 12910 corresponden a los reintentos de conexión del equipo `192.168.169.131` hacia la API global de productos y actualizaciones de Fortinet (`globalproductapi.fortinet.net` / `globalfctupdate.fortinet.net`) por HTTPS/443 y la infraestructura de DNS seguro DoT de FortiGuard (`96.45.45.45` / `96.45.46.46:853`). El firewall FortiGate denegó las conexiones (`action="deny"`), haciendo que Stellar Cyber generara la alerta por acumulación de bloqueos. Se procede al cierre del ticket.

---

### 🔬 Desglose Ultra Quirúrgico

* **Capa 1: Red y Enrutamiento (`srcip` / `dstip` / `proto`)**
  - Origen: `192.168.169.131`.
  - Destinos: `96.45.46.46` (DoT/853), `141.109.161.95` (HTTPS/443), `96.45.45.45` (DoT/853) y `173.243.143.6` (HTTPS/443).
* **Capa 2: Aplicación y DPI (`appid_name` / `dstip_host`)**
  - AppID: `Fortinet-FortiGuard` / `Fortinet-Web`.
  - Servidores: `globalproductapi.fortinet.net`, `globalfctupdate.fortinet.net`, `96.45.45.45` / `96.45.46.46` (FortiGuard DoT).
* **Capa 3: Firewall y ML (`action` / `external_fw_action`)**
  - `action`: `deny`.
  - El motor `external_fw_action` superó el umbral debido a los reintentos automáticos del agente cliente (hasta 183 denegaciones).

**Resumen Quirúrgico Final:** Conexiones legítimas de consulta de API, actualizaciones y resolución DNS-over-TLS enviadas por el software cliente FortiClient hacia la infraestructura oficial de Fortinet Inc., denegadas por las políticas de salida restrictivas del firewall perimetral. Sin impacto de seguridad.
