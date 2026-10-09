### 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `False Positive`, `Firewall Denial`, `Fortinet Cloud Services`, `FortiGuard DoT`, `Egress Policy`

### Análisis Lote de Eventos (2 Eventos Recibidos)
Se han analizado de forma individual y secuencial los 2 eventos de denegación perimetral registrados por el sensor de red.

---

### 🎯 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Alerta Detectada:** External Firewall Denial Anomaly (12912).
* **Activos Involucrados:** 
  - **Origen Interno:** Estación de trabajo `192.168.169.131`.
  - **Destino Externo:** Servidor de DNS seguro FortiGuard DoT `96.45.45.45` (Puerto TCP/853).
* **Comportamiento Anómalo:** Elevado número de peticiones salientes de DNS-over-TLS bloqueadas por el firewall FortiGate (`action="deny"`) en el puerto TCP/853, registrando entre 179 y 189 denegaciones en ventanas de 5 minutos.
* **Causalidad Probable:** Falso positivo. El cliente FortiClient en la máquina `192.168.169.131` intentó realizar resoluciones DNS cifradas (DoT) hacia la infraestructura perimetral oficial de FortiGuard (`96.45.45.45:853`). El firewall perimetral denegó la salida por políticas restrictivas en la VLAN local. El modelo estadístico de Stellar Cyber (`external_fw_action`) disparó la anomalía de volumen debido a los reintentos automáticos del agente.

---

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Origen | Destino / Servidor FortiGuard | Acción Firewall |
|---|---|---|---|---|
| 2026-08-02T02:10:00 | 2026-08-01 23:10:00 | `192.168.169.131` | `96.45.45.45:853` (FortiGuard DoT) | **Deny** (179 intentos) |
| 2026-08-02T02:15:00 | 2026-08-01 23:15:00 | `192.168.169.131` | `96.45.45.45:853` (FortiGuard DoT) | **Deny** (189 intentos) |

---

### 🔬 Desglose Técnico y Disección Forense
* **Proceso / Aplicación:** FortiGuard DNS-over-TLS Resolver (`Fortinet-FortiGuard`).
* **Puerto y Protocolo:** TCP 853 (DNS-over-TLS / DoT).
* **Reputación:** Excelente. Infraestructura oficial global de Fortinet Inc.

**Payload / Evidencia Principal:**
```json
{
  "payload_type": "Firewall Egress Policy Log",
  "payload_value": "96.45.45.45:853 (FortiGuard DoT)",
  "payload_hash": "N/A (Tráfico de red)",
  "payload_firma": "Fortinet-FortiGuard",
  "payload_accion": "DENY (Bloqueado por regla perimetral FortiGate)",
  "payload_destino": "96.45.45.45:853"
}
```

**Contexto del SIEM (Stellar Cyber):**
Las reglas de detección de anomalías supervisan el conteo acumulado de denegaciones salientes. Al no contar el segmento `192.168.169.x` con permiso implícito de salida para el puerto DoT/853 hacia FortiGuard (`96.45.45.45`), el cliente reintenta continuamente la conexión, sumando hasta 189 bloqueos en 5 minutos y superando la línea base habitual (`typical: 9`), desencadenando la alerta.

### 🧠 ¿Por qué es (o no es) una Amenaza?
**Es un Falso Positivo (Bloqueo de Política de Salida).** No representa tráfico malicioso ni exfiltración de información. Es una operación legítima del software FortiClient solicitando resolución DNS cifrada que es bloqueada por la política saliente restrictiva del firewall perimetral.

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
  "Motivo": "Tráfico saliente de resolución DNS cifrada (DoT puerto 853) hacia servidores oficiales de FortiGuard (96.45.45.45) bloqueado por la regla de salida del firewall."
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
| Detección y Análisis | Inspección de IPs de destino (FortiGuard DoT). Descarte de amenaza. |
| Erradicación y Recuperación | N/A (Tráfico corporativo). |
| Actividad Post-Incidente | Ajustar políticas perimetrales si se desea permitir el tráfico DoT/853 de FortiClient. |

### 📚 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
|---|---|---|
| PB-002 | Manejo de Falsos Positivos | Cierre de anomalías de volumen por bloqueos de política de firewall en tráfico legítimo. |

### 🏷️ Resolution Tag para Stellar Cyber
`False Positive` - Normal Administrative Behavior / Expected Network Policy Block.

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
`02/08/2026 13:31 | Analista | technoma | 12912 | Stellar Cyber | - | Baja | External Firewall Denial Anomaly | Bloqueo de política saliente a servidor DNS cifrado FortiGuard DoT | 192.168.169.131 | Falso Positivo. El equipo 192.168.169.131 registró picos de denegación saliente en FortiGate al intentar conectarse al servidor de DNS seguro DoT de FortiGuard (96.45.45.45:853). Tráfico inofensivo bloqueado por políticas de salida del firewall. Sin compromiso de seguridad. | FortiGate Traffic Log | Ninguna | Cerrado | - | No | - | PB-002`

### 💻 Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario final:** Falso positivo validado. Las 2 alertas del lote 12912 corresponden a los reintentos de conexión del equipo `192.168.169.131` hacia el servidor de resolución DNS segura DoT de FortiGuard (`96.45.45.45:853`). El firewall FortiGate denegó las conexiones (`action="deny"`), haciendo que Stellar Cyber generara la alerta por acumulación de bloqueos salientes. Se procede al cierre del ticket.

---

### 🔬 Desglose Ultra Quirúrgico

* **Capa 1: Red y Enrutamiento (`srcip` / `dstip` / `proto`)**
  - Origen: `192.168.169.131`.
  - Destino: `96.45.45.45` en puerto DoT/853.
* **Capa 2: Aplicación y DPI (`appid_name` / `dstip_host`)**
  - AppID: `Fortinet-FortiGuard`.
  - Servidor: `96.45.45.45` (FortiGuard DoT Resolver).
* **Capa 3: Firewall y ML (`action` / `external_fw_action`)**
  - `action`: `deny`.
  - El motor `external_fw_action` superó el umbral debido a los reintentos automáticos del cliente (hasta 189 denegaciones).

**Resumen Quirúrgico Final:** Intentos legítimos de resolución DNS-over-TLS enviados por el software cliente FortiClient desde la estación `192.168.169.131` hacia la infraestructura oficial de Fortinet Inc., denegados por las políticas salientes del firewall perimetral. Sin impacto de seguridad.
