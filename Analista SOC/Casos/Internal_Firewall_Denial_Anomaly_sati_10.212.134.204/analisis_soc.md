# Reporte SOC - Caso: Internal Firewall Denial Anomaly (sati - 10.212.134.204)

**Tenant:** Technoma | **Sensor:** technoma-sensor (`190.104.178.146`) | **Dispositivo:** FG-Technoma (`FG120GTK24022543`)  
**XDR Event:** Internal Firewall Denial Anomaly (`internal_fw_action`) | **Técnica:** XT2002 (XDR Firewall Anomaly) | **Táctica:** XTA0002 (XDR NBA) | **Kill Chain:** Exploration

---

## Declaración de Conteo Inicial
Se han detectado **2 eventos independientes** en el lote de alertas nativas de Interflow/Stellar Cyber:
- **Evento 1 (ID Anomaly: `qjgrkKABI3UnQyDORJk6`):** 576 denegaciones en una ventana de 5 minutos (frente a 58 típicas) registradas a las 08:10:22 (-0300) por el FortiGate `FG-Technoma` sobre tráfico DNS (UDP/53) originado por la IP de VPN `10.212.134.204` (usuario `sati`) con destino al DC `10.11.1.1`.
- **Evento 2 (ID Anomaly: `czg0kKABI3UnQyDOHv-R`):** 560 denegaciones en una ventana de 5 minutos (frente a 58 típicas) registradas 10 minutos después (08:20:17 -0300) por el mismo flujo repetitivo de consultas DNS denegadas bajo `policyid=0`.

---

### Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `#FalsoPositivo` `#RuidoOperativo` `#InternalFirewallDenial` `#FortiGate` `#FGTechnoma` `#SSLVPN` `#sati` `#DNS` `#Odoo`

---

## Análisis Evento 1 (Anomaly ID: qjgrkKABI3UnQyDORJk6)

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Actividad Observada:** La dirección IP `10.212.134.204`, asignada a través del túnel SSL VPN (`ssl.root`) al usuario autenticado `sati`, generó 576 intentos de conexión UDP al puerto 53 hacia el Controlador de Dominio `10.11.1.1` (`ad.technoma.local`).
* **Acción de Seguridad:** El firewall perimetral `FG-Technoma` denegó de forma estricta e inmediata el 100% de las solicitudes bajo la política implícita de descarte (`policyid=0`).
* **Causa Raíz:** Tráfico legítimo de resolución de nombres de un proveedor externo autorizado (soporte de Odoo). La política de firewall para la VPN SSL no cuenta con una regla que autorice consultas DNS hacia el segmento de servidores `Citrix Servers` donde se ubica el DC, provocando reintentos continuos por parte del cliente.
* **Mapeo en SIEM (Stellar Cyber):** El motor analítico de Machine Learning (`internal_fw_action`) detectó una desviación estadística volumétrica (576 denegaciones frente al valor basal de 58), catalogándola bajo la fase `Exploration`.

### Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local GMT-3) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-11 11:10:21 | 2026-09-11 08:10:22 | FortiGate Traffic Log | 576 blocks | 58 | 9.9x | Denegación por `policyid=0` en interfaz `ssl.root` hacia `10.11.1.1:53`. |
| 2026-09-11 11:12:17 | 2026-09-11 08:12:17 | Ingesta Syslog | `qjgrkKABI3UnQyDORJk6` | - | - | Syslog recibido en sensor y remitido a Interflow. |
| 2026-09-11 11:20:03 | 2026-09-11 08:20:03 | Disparo de Alerta ML | Severidad 60 | - | - | Cálculo de anomalía volumétrica de denegación completado. |

### Desglose Técnico y Disección Forense
* **Flujo de Tráfico:** `10.212.134.204:35437` -> `10.11.1.1:53` (UDP, Protocolo 17). Interfaz origen: `ssl.root` (VPN). Interfaz destino: `Citrix Servers` (LAN).
* **Mecanismo de Descarte:** `action="deny" policyid=0`. Ningún paquete fue cursado hacia la red interna (`duration=0, sentbyte=0, rcvdbyte=0`).
* **Identidad:** Usuario `sati` autenticado contra el servidor local de autenticación VPN (`authserver="sati"`). Corresponde al proveedor externo de soporte del sistema ERP Odoo registrado en la Memoria Institucional (`SOC_GEM_v2.md`).

```json
/* Payload / Evidencia Principal: */
{
  "payload_type": "Syslog Network Connection",
  "payload_value": "srcip=10.212.134.204 srcport=35437 dstip=10.11.1.1 dstport=53 proto=17 action=deny policyid=0",
  "payload_hash": "N/A",
  "payload_firma": "FG-Technoma_0 (Implicit Deny)",
  "payload_accion": "deny",
  "payload_destino": "10.11.1.1:53 (ad.technoma.local)"
}
```

#### Hipótesis Formuladas
| ID | Hipótesis | Evaluación | Justificación Forense |
| :--- | :--- | :--- | :--- |
| H1 | Escaneo o reconocimiento interno malicioso | Descartada | Tráfico unidireccional y mono-puerto exclusivo a UDP/53; no existen sondeos horizontales a otros hosts ni puertos. |
| H2 | Túnel DNS o exfiltración encubierta | Descartada | Cero bytes transmitidos o recibidos; denegación inmediata en frontera de firewall. |
| H3 | Problema de postura / Desajuste en política VPN | Confirmada | Comportamiento documentado en `SOC_GEM_v2.md`. El cliente VPN reintenta resolver nombres al no recibir respuesta DNS permitida. |

---

## Análisis Evento 2 (Anomaly ID: czg0kKABI3UnQyDOHv-R)

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Actividad Observada:** Continuación del flujo de reintentos DNS desde la IP de VPN `10.212.134.204` (usuario `sati`) hacia `10.11.1.1:53`, registrando 560 denegaciones en los siguientes 5 minutos.
* **Acción de Seguridad:** El FortiGate `FG-Technoma` mantiene el bloqueo consistente bajo `policyid=0`.
* **Correlación con Evento 1:** Se trata de una extensión directa del Evento 1 originada por el ciclo de temporizadores de resolución DNS del sistema operativo del cliente VPN al persistir el descarte de paquetes.

### Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local GMT-3) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-11 11:20:16 | 2026-09-11 08:20:17 | FortiGate Traffic Log | 560 blocks | 58 | 9.6x | Denegación consecutiva por `policyid=0` en puerto UDP/53. |
| 2026-09-11 11:22:00 | 2026-09-11 08:22:00 | Ingesta Syslog | `czg0kKABI3UnQyDOHv-R` | - | - | Normalización por analizador de FortiGate en Interflow. |
| 2026-09-11 11:30:02 | 2026-09-11 08:30:02 | Disparo de Alerta ML | Severidad 60 | - | - | Segunda alerta volumétrica asociada al mismo origen y comportamiento. |

---

## ¿Por qué es (o no es) una Amenaza?
No representa una amenaza para la confidencialidad, integridad o disponibilidad de la organización. El usuario `sati` es un proveedor legítimo y autorizado que brinda soporte a la plataforma Odoo. Al conectarse mediante FortiClient SSL VPN, la máquina remota intenta resolver nombres de red internos enviando paquetes DNS estándar al DC (`10.11.1.1`), pero la política de firewall no habilita el puerto 53 desde la zona VPN hacia esa interfaz LAN. El firewall actúa con total efectividad bloqueando el tráfico. La alerta generada en Stellar Cyber es consecuencia directa del volumen de reintentos automáticos del cliente, no de un ataque intencional.

---

## Cierre Maestro Unificado del Caso

### Análisis de Impacto CIA Triad
```json
{
  "confidencialidad": "C0",
  "integridad": "I0",
  "disponibilidad": "A0",
  "justificacion": "El trafico fue denegado al 100% en el perimetro de firewall (policyid=0, sentbyte=0, rcvdbyte=0). No existio acceso a datos, modificacion de registros ni degradacion de servicios internos."
}
```

### Veredicto y Confianza Analítica
```json
{
  "veredicto": "Falso Positivo",
  "confianza": "100%",
  "clasificacion_soc": "Ruido Operativo / Problema de Postura VPN (Documentado en SOC_GEM_v2.md)",
  "justificacion": "Trafico DNS legitimate generado por proveedor de soporte Odoo (sati) a traves de SSL VPN, denegado por configuracion estricta en FortiGate. Control perimetral efectivo."
}
```

### Indicador de Fatiga de Alertas
```json
{
  "fatiga_detectada": "Alta",
  "frecuencia": "Patron recurrente documentado (IPs 10.212.134.203, 10.212.134.205, 10.212.134.206 y 10.212.134.204)",
  "razon": "Falta de definicion en la politica de VPN de FortiGate o asignacion de DNS publico en FortiClient, provocando alertas ciclicas de Internal Firewall Denial Anomaly.",
  "accion_recomendada": "Gestionar con el equipo de Infraestructura y Redes la habilitacion de una regla de servicio DNS controlada o asignar DNS publicos en la configuracion del tunel VPN para el usuario sati."
}
```

### Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Detección y Análisis | Correlación de eventos de firewall en Interflow, validación contra memoria institucional (`SOC_GEM_v2.md`) y verificación de descarte perimetral. |
| Contención, Erradicación y Recuperación | Contención preventiva activa y permanente por el firewall `FG-Technoma`. No se requiere intervención reactiva ni aislamiento de activos. |
| Post-Incidente | Reclamación técnica a Infraestructura para corrección de postura en la configuración VPN de Odoo. |

### Playbook Asignado
| ID Playbook | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| PB 5.2 | Problemas de Configuración, Postura y Servicios Vulnerables Abiertos | Aplica para la gestión y seguimiento de desajustes en políticas de red y accesos VPN que generan tráfico denegado recurrente. |

### Resolution Tag para Stellar Cyber
* **Resolution Tag:** `False Positive`
* **Descripción:** Alerta descartada como falso positivo operativo por consultas DNS de VPN bloqueadas por política de firewall en equipo de soporte autorizado.

### Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc. Puede ser el mismo del Case Evidence ) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 11/09/2026 08:20 | Analista SOC | technoma | qjgrkKABI3UnQyDORJk6 | FG-Technoma / new_ml | - | Baja | Internal Firewall Denial Anomaly | Consultas DNS de sati (VPN Odoo) bloqueadas por FortiGate hacia 10.11.1.1 | FG-Technoma, ad.technoma.local (10.11.1.1), usuario sati (10.212.134.204) | 2 alertas (576 y 560 bloqueos). FP operativo: proveedor autorizado Odoo (sati) conectado via SSL VPN intenta resolver DNS contra 10.11.1.1 pero el trafico es denegado por policyid:0. Control efectivo de firewall. | FortiGate syslog (proto: 17, dstport: 53, policyid: 0, action: deny, user: sati) | Notificar a Infraestructura para ajustar politica VPN de sati o asignar DNS publico en FortiClient. | Cerrado | - | No | - | PB 5.2 |

### Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario de Cierre Maestro:**
> Se analizaron 2 eventos correlacionados bajo la alerta Internal Firewall Denial Anomaly vinculados a la IP 10.212.134.204 (túnel SSL VPN de Technoma) asociada al usuario sati (proveedor externo autorizado para soporte de Odoo).
> 
> La telemetría de FortiGate (FG-Technoma) confirma que los bloqueos corresponden exclusivamente a tráfico DNS (UDP puerto 53) dirigido hacia el controlador de dominio 10.11.1.1 (ad.technoma.local), descartado limpiamente por la política de seguridad por defecto (policyid=0). Comportamiento tipificado en la Memoria Institucional: la política de VPN no contempla resolución DNS hacia el segmento del DC, provocando reintentos automatizados por parte del cliente.
> 
> Actividad descartada como Falso Positivo Operativo / Ruido de Postura. El tráfico se encuentra completamente mitigado por el firewall, sin evidencia de escaneo malicioso ni compromiso.

---

### Desglose Ultra Quirúrgico
* **Capa de Red y Enrutamiento:**
  * `srcip`: `10.212.134.204` (IP asignada dinámicamente del pool SSL VPN de Technoma).
  * `srcintf`: `ssl.root` (Túnel VPN autenticado del cliente remoto).
  * `dstip`: `10.11.1.1` (`ad.technoma.local`, Controlador de Dominio principal).
  * `dstintf`: `Citrix Servers` (Zona LAN de servidores internos).
* **Capa de Transporte y Conexión:**
  * `proto`: `17` (`udp`).
  * `srcport`: `35437` y `52108` (Puertos efímeros estándar de cliente DNS).
  * `dstport`: `53` (`service: DNS`).
* **Capa de Firewall (FortiOS):**
  * `action`: `deny`.
  * `policyid`: `0` (Implicit Deny / Regla de descarte por defecto).
  * `sentbyte`: `0`, `rcvdbyte`: `0`, `duration`: `0` (Descarte sin establecimiento de sesión).
  * `crscore`: `30`, `craction`: `131072`, `crlevel`: `high` (Métricas internas de telemetría de Fortinet asociadas a tráfico denegado).
* **Capa de Detección XDR y Motor ML:**
  * `name`: `internal_fw_action` (`Internal Firewall Denial Anomaly`).
  * `actual`: `576` y `560` vs `typical: 58` (Incremento anómalo que superó el umbral en ventanas móviles de 5 minutos).
  * `threat_score`: `0`, `event_score`: `71`, `severity`: `60` (Alerta generada por volumen estadístico y no por firma de exploit).

**Resumen Quirúrgico Final:**  
El usuario autorizado `sati` (proveedor de Odoo) se conectó al entorno corporativo mediante SSL VPN recibiendo la IP `10.212.134.204`. Al carecer de resolución DNS local permitida en el túnel, la máquina remota generó ráfagas automáticas de consultas UDP/53 hacia el DC `10.11.1.1`, las cuales fueron denegadas de forma sistemática por el FortiGate bajo `policyid=0`. El motor de Machine Learning de Stellar Cyber detectó la anomalía volumétrica de denegaciones y generó las alertas. El evento queda resuelto como Falso Positivo Operativo / Problema de Postura VPN sin riesgo de seguridad.
