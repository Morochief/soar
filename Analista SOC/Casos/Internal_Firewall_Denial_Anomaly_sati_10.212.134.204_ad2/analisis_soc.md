# Reporte SOC - Caso: Internal Firewall Denial Anomaly (sati - 10.212.134.204 -> ad2)

**Tenant:** Technoma | **Sensor:** technoma-sensor (`190.104.178.146`) | **Dispositivo:** FG-Technoma (`FG120GTK24022543`)  
**XDR Event:** Internal Firewall Denial Anomaly (`internal_fw_action`) | **Técnica:** XT2002 (XDR Firewall Anomaly) | **Táctica:** XTA0002 (XDR NBA) | **Kill Chain:** Exploration

---

## Declaración de Conteo Inicial
Se han detectado **3 eventos independientes** en el lote de alertas nativas de Interflow/Stellar Cyber:
- **Evento 1 (ID Anomaly: `yTgvkKABI3UnQyDO2Mng`):** 410 denegaciones en una ventana de 5 minutos (frente a 58 típicas) registradas a las 08:15:23 (-0300) por `FG-Technoma` sobre tráfico DNS (UDP/53) desde la IP de VPN `10.212.134.204` (usuario `sati`) hacia el Controlador de Dominio secundario `10.11.1.2` (`ad2.technoma.local`).
- **Evento 2 (ID Anomaly: `ozlCkKABI3UnQyDOBJrZ`):** 495 denegaciones en una ventana de 5 minutos (frente a 59 típicas) registradas a las 08:35:10 (-0300) sobre el mismo destino secundario `10.11.1.2:53`.
- **Evento 3 (ID Anomaly: `oTlGkKABI3UnQyDOmdQ4`):** 640 denegaciones en una ventana de 5 minutos (frente a 59 típicas) registradas a las 08:40:07 (-0300) en continuidad del ciclo de failover de resolución DNS.

---

### Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `#FalsoPositivo` `#RuidoOperativo` `#InternalFirewallDenial` `#FortiGate` `#FGTechnoma` `#SSLVPN` `#sati` `#DNS` `#FailoverDNS` `#ad2`

---

## Análisis Evento 1 (Anomaly ID: yTgvkKABI3UnQyDO2Mng)

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Actividad Observada:** Tras la denegación continua de consultas DNS hacia el DC primario (`10.11.1.1`), el resolver del cliente en la IP `10.212.134.204` (usuario `sati` vía SSL VPN `ssl.root`) ejecutó un failover automático hacia el servidor DNS secundario configurado en la red: `10.11.1.2` (`ad2.technoma.local`), generando 410 consultas UDP/53.
* **Acción de Seguridad:** El firewall perimetral `FG-Technoma` denegó el 100% de las conexiones de forma inmediata bajo la regla por defecto `policyid=0` (Implicit Deny).
* **Mapeo en SIEM (Stellar Cyber):** La anomalía volumétrica de denegaciones disparó la regla `internal_fw_action` con una severidad de 60 y `event_score: 71`.

### Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local GMT-3) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-11 11:15:22 | 2026-09-11 08:15:23 | FortiGate Traffic Log | 410 blocks | 58 | 7.1x | Failover de DNS hacia `10.11.1.2:53` denegado por `policyid=0`. |
| 2026-09-11 11:17:19 | 2026-09-11 08:17:19 | Ingesta Syslog | `yTgvkKABI3UnQyDO2Mng` | - | - | Normalización del registro en Interflow. |
| 2026-09-11 11:25:02 | 2026-09-11 08:25:02 | Disparo de Alerta ML | Severidad 60 | - | - | Cálculo de desviación estadística sobre umbral basal. |

### Desglose Técnico y Disección Forense
* **Flujo de Tráfico:** `10.212.134.204:40911` -> `10.11.1.2:53` (UDP/17). Origen: `ssl.root` (VPN). Destino: `Citrix Servers` (LAN).
* **Mecanismo de Descarte:** `action="deny" policyid=0`. Tráfico completamente descartado en frontera perimetral (`sentbyte=0, rcvdbyte=0, duration=0`).

```json
/* Payload / Evidencia Principal: */
{
  "payload_type": "Syslog Network Connection",
  "payload_value": "srcip=10.212.134.204 srcport=40911 dstip=10.11.1.2 dstport=53 proto=17 action=deny policyid=0",
  "payload_hash": "N/A",
  "payload_firma": "FG-Technoma_0 (Implicit Deny)",
  "payload_accion": "deny",
  "payload_destino": "10.11.1.2:53 (ad2.technoma.local)"
}
```

---

## Análisis Evento 2 (Anomaly ID: ozlCkKABI3UnQyDOBJrZ)

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Actividad Observada:** Ráfaga consecutiva de 495 solicitudes DNS bloqueadas hacia `10.11.1.2:53` entre las 08:30 y 08:35 (-0300).
* **Acción de Seguridad:** Descarte efectivo en el firewall bajo `policyid=0`.
* **Correlación:** Al no recibir respuesta de ninguno de los dos servidores DNS (`10.11.1.1` y `10.11.1.2`), el stack TCP/IP del cliente VPN continúa ciclando sus reintentos de resolución según los temporizadores de timeout del sistema operativo.

### Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local GMT-3) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-11 11:35:09 | 2026-09-11 08:35:10 | FortiGate Traffic Log | 495 blocks | 59 | 8.4x | Denegación consecutiva por `policyid=0` en puerto UDP/53. |
| 2026-09-11 11:37:08 | 2026-09-11 08:37:08 | Ingesta Syslog | `ozlCkKABI3UnQyDOBJrZ` | - | - | Ingesta de telemetría de firewall en Interflow. |
| 2026-09-11 11:45:08 | 2026-09-11 08:45:08 | Disparo de Alerta ML | Severidad 60 | - | - | Segunda alerta volumétrica sobre host secundario. |

---

## Análisis Evento 3 (Anomaly ID: oTlGkKABI3UnQyDOmdQ4)

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Actividad Observada:** Pico de 640 denegaciones en 5 minutos registrado a las 08:40:07 (-0300) hacia `10.11.1.2:53`.
* **Acción de Seguridad:** Bloqueo ininterrumpido por la política implícita 0 de `FG-Technoma`.
* **Correlación Global:** Cierre del ciclo de sondeo repetitivo del proveedor `sati`. El volumen acumulado refleja la persistencia de las aplicaciones locales (servicios del sistema y navegador) por resolver nombres corporativos sin una ruta/política DNS permitida.

### Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local GMT-3) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-11 11:40:06 | 2026-09-11 08:40:07 | FortiGate Traffic Log | 640 blocks | 59 | 10.8x | Denegación por `policyid=0` en interfaz `ssl.root` hacia `10.11.1.2:53`. |
| 2026-09-11 11:42:07 | 2026-09-11 08:42:07 | Ingesta Syslog | `oTlGkKABI3UnQyDOmdQ4` | - | - | Syslog procesado por analizador de FortiGate. |
| 2026-09-11 11:50:03 | 2026-09-11 08:50:03 | Disparo de Alerta ML | Severidad 60 | - | - | Tercera alerta volumétrica generada por el motor de ML. |

---

## ¿Por qué es (o no es) una Amenaza?
No representa una amenaza para la seguridad de Technoma. El usuario `sati` es un proveedor externo autorizado que brinda soporte al ERP Odoo. Al conectarse mediante FortiClient SSL VPN, su equipo tiene configurados los dos servidores DNS corporativos del dominio: `10.11.1.1` (primario) y `10.11.1.2` (secundario). Al ser bloqueadas las consultas al primario por no existir una regla permisiva de VPN hacia servidores internos, el resolver conmuta automáticamente al secundario `10.11.1.2`, donde ocurre exactamente el mismo bloqueo por `policyid=0`. El control perimetral fue 100% efectivo. Se trata de un problema de postura y configuración de red documentado en la Memoria Institucional (`SOC_GEM_v2.md`).

---

## Cierre Maestro Unificado del Caso

### Análisis de Impacto CIA Triad
```json
{
  "confidencialidad": "C0",
  "integridad": "I0",
  "disponibilidad": "A0",
  "justificacion": "La totalidad de las solicitudes UDP/53 fueron denegadas en frontera por el firewall (policyid=0, bytes transmitidos=0). Sin impacto en datos, sistemas ni servicios operativos."
}
```

### Veredicto y Confianza Analítica
```json
{
  "veredicto": "Falso Positivo",
  "confianza": "100%",
  "clasificacion_soc": "Ruido Operativo / Problema de Postura VPN - Failover DNS (Documentado en SOC_GEM_v2.md)",
  "justificacion": "Peticiones DNS legitimas generadas por proveedor de soporte Odoo (sati) que conmutan hacia el DC secundario (10.11.1.2) al fallar el primario. Descarte efectivo por politica de firewall."
}
```

### Indicador de Fatiga de Alertas
```json
{
  "fatiga_detectada": "Alta",
  "frecuencia": "Patron recurrente en tenant technoma",
  "razon": "Ciclo continuo de alertas hacia ambos controladores de dominio (10.11.1.1 y 10.11.1.2) debido a la ausencia de resolucion DNS autorizada en el perfil VPN del usuario sati.",
  "accion_recomendada": "Reclamar al equipo de Infraestructura la asignacion de servidores DNS publicos en el perfil de conexion FortiClient de sati o habilitar regla de firewall para puerto 53 hacia los DCs."
}
```

### Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Detección y Análisis | Correlación de eventos de failover DNS en Interflow, validación contra memoria institucional (`SOC_GEM_v2.md`) y verificación de descarte perimetral. |
| Contención, Erradicación y Recuperación | Contención preventiva activa y consistente por el firewall `FG-Technoma`. No requiere remediación en endpoints. |
| Post-Incidente | Traslado de requerimiento técnico a Infraestructura para corregir la postura del servicio VPN. |

### Playbook Asignado
| ID Playbook | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| PB 5.2 | Problemas de Configuración, Postura y Servicios Vulnerables Abiertos | Gestión de desajustes en políticas de firewall y accesos de terceros vía VPN que provocan tráfico denegado cíclico. |

### Resolution Tag para Stellar Cyber
* **Resolution Tag:** `False Positive`
* **Descripción:** Alerta descartada como falso positivo operativo por failover de consultas DNS hacia DC secundario bloqueadas por política de firewall en equipo de soporte autorizado.

### Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc. Puede ser el mismo del Case Evidence ) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 11/09/2026 08:40 | Analista SOC | technoma | yTgvkKABI3UnQyDO2Mng | FG-Technoma / new_ml | - | Baja | Internal Firewall Denial Anomaly | Consultas DNS de sati (VPN Odoo) bloqueadas por FortiGate hacia 10.11.1.2 (ad2) | FG-Technoma, ad2.technoma.local (10.11.1.2), usuario sati (10.212.134.204) | 3 alertas (410, 495 y 640 bloqueos). FP operativo: proveedor autorizado Odoo (sati) conectado via SSL VPN ejecuta failover DNS hacia DC secundario 10.11.1.2 tras denegacion en primario. Trafico bloqueado por policyid:0. Control efectivo de firewall. | FortiGate syslog (proto: 17, dstport: 53, policyid: 0, action: deny, user: sati) | Notificar a Infraestructura para ajustar politica VPN de sati o asignar DNS publico en FortiClient. | Cerrado | - | No | - | PB 5.2 |

### Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario de Cierre Maestro:**
> Se analizaron 3 eventos correlacionados bajo la alerta Internal Firewall Denial Anomaly vinculados a la IP 10.212.134.204 (túnel SSL VPN de Technoma) asociada al usuario sati (proveedor externo autorizado para soporte de Odoo).
> 
> La telemetría de FortiGate (FG-Technoma) confirma que los bloqueos corresponden a consultas DNS (UDP puerto 53) dirigidas hacia el controlador de dominio secundario 10.11.1.2 (ad2.technoma.local), producto de un failover automático del resolver del cliente tras no obtener respuesta del primario (10.11.1.1). Todo el tráfico fue descartado de forma estricta por la política implícita por defecto (policyid=0). Comportamiento tipificado en la Memoria Institucional: la política de VPN no autoriza resolución DNS hacia la zona interna, provocando ciclos de reintentos automatizados.
> 
> Actividad descartada como Falso Positivo Operativo / Ruido de Postura. El tráfico se encuentra completamente mitigado por el firewall, sin evidencia de escaneo malicioso ni compromiso.

---

### Desglose Ultra Quirúrgico
* **Capa de Red y Enrutamiento:**
  * `srcip`: `10.212.134.204` (IP asignada por el concentrador SSL VPN de Technoma).
  * `srcintf`: `ssl.root` (Túnel VPN del usuario `sati`).
  * `dstip`: `10.11.1.2` (`ad2.technoma.local`, Controlador de Dominio secundario de Technoma).
  * `dstintf`: `Citrix Servers` (Zona LAN de servidores internos).
* **Capa de Transporte y Conexión:**
  * `proto`: `17` (`udp`).
  * `srcport`: `40911`, `39278` y `39890` (Puertos dinámicos de origen).
  * `dstport`: `53` (`service: DNS`).
* **Capa de Firewall (FortiOS):**
  * `action`: `deny`.
  * `policyid`: `0` (Implicit Deny).
  * `sentbyte`: `0`, `rcvdbyte`: `0`, `duration`: `0` (Sesión abortada inmediatamente).
  * `crscore`: `30`, `craction`: `131072`, `crlevel`: `high` (Métricas de telemetría de Fortinet).
* **Capa de Detección XDR y Motor ML:**
  * `name`: `internal_fw_action` (`Internal Firewall Denial Anomaly`).
  * `actual`: `410`, `495` y `640` vs `typical: 58-59` (Volúmenes que excedieron ampliamente el umbral en intervalos de 5 minutos).
  * `threat_score`: `0`, `event_score`: `71`, `severity`: `60` (Disparo estadístico volumétrico).

**Resumen Quirúrgico Final:**  
Tras el bloqueo reiterado de consultas DNS hacia el DC primario (`10.11.1.1`), el equipo del proveedor `sati` (`10.212.134.204`) conmutó sus solicitudes hacia el servidor secundario `10.11.1.2` (`ad2.technoma.local`). El firewall `FG-Technoma` descartó limpiamente las peticiones en tres intervalos sucesivos (410, 495 y 640 bloqueos) bajo la política implícita 0. El motor de Machine Learning de Stellar Cyber detectó la sobrecarga volumétrica de descartes y generó las alertas. El caso se concluye como Falso Positivo Operativo / Problema de Postura VPN sin impacto en el entorno.
