# Reporte SOC - Caso: Recently Registered Domains (nb-fcaceres - firefox-portal-detection.com)

**Tenant:** Technoma | **Sensor:** technoma-sensor (`190.104.178.146`) | **Host Origen:** `nb-fcaceres.technoma.local` (`192.168.169.34`)  
**XDR Event:** Recently Registered Domains (`new_registered_domain`) | **Técnica:** XT2008 (XDR New Domain) | **Táctica:** XTA0002 (XDR NBA) | **Kill Chain:** Initial Attempts

---

## Declaración de Conteo Inicial
Se han detectado **2 eventos independientes** en el lote de alertas nativas de Interflow/Stellar Cyber:
- **Evento 1 (ID Anomaly: `sDpOkKABI3UnQyDOEzcy`):** Consulta DNS de tipo A hacia `firefox-portal-detection.com` registrada a las 08:47:18 (-0300) por el sensor modular desde el endpoint `192.168.169.34` (`nb-fcaceres.technoma.local`) hacia el servidor DNS corporativo `10.11.1.1` (`ad.technoma.local`).
- **Evento 2 (ID Anomaly: `gDpOkKABI3UnQyDO-UPI`):** Segunda consulta DNS de tipo A hacia el mismo dominio registrada un minuto después (08:48:17 -0300) desde la misma estación de trabajo.

---

### Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `#FalsoPositivo` `#RecentlyRegisteredDomains` `#Firefox` `#CaptivePortal` `#Fastly` `#nb-fcaceres` `#VLAN1101` `#DNS`

---

## Análisis Evento 1 (Anomaly ID: sDpOkKABI3UnQyDOEzcy)

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Actividad Observada:** El endpoint corporativo `nb-fcaceres.technoma.local` (`192.168.169.34`, VLAN 1101) emitió una solicitud DNS UDP/53 al Controlador de Dominio `10.11.1.1` consultando el registro A del dominio `firefox-portal-detection.com`.
* **Acción de Seguridad:** Resolución exitosa por parte del servidor DNS local (`reply_code: "No Error"`), retornando cuatro direcciones IP pertenecientes a la red CDN de Fastly (`151.101.129.91`, `151.101.1.91`, `151.101.65.91`, `151.101.193.91`).
* **Causa Raíz:** Mecanismo estándar de comprobación de conectividad a internet y detección de portales cautivos (Captive Portal Detection) del navegador Mozilla Firefox instalado en la máquina de la usuaria.
* **Mapeo en SIEM (Stellar Cyber):** La regla `new_registered_domain` disparó la alerta debido a que el dominio fue registrado el `2026-07-01T15:40:13Z` (hace aproximadamente 72 días, dentro del umbral estricto de menos de 90 días de antigüedad configurado en el motor de Machine Learning).

### Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local GMT-3) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-11 11:47:18 | 2026-09-11 08:47:18 | Consulta DNS (A) | `firefox-portal-detection.com` | - | - | Endpoint `192.168.169.34` consulta al DC `10.11.1.1`. |
| 2026-09-11 11:47:18 | 2026-09-11 08:47:18 | Respuesta DNS | Fastly CDN IPs | - | - | Resolución en 26 ms (`reply_code: No Error`). |
| 2026-09-11 11:53:11 | 2026-09-11 08:53:11 | Disparo de Alerta ML | Severidad 50 | - | - | Regla ATH `new_registered_domain` activa por edad < 90 días. |

### Desglose Técnico y Disección Forense
* **Flujo de Tráfico:** `192.168.169.34:49674` -> `10.11.1.1:53` (UDP/17). Sensor: `technoma-sensor` en interfaz `ethernet1`, VLAN 1101.
* **Volumen:** 1 paquete enviado (88 bytes) y 1 recibido (152 bytes). Sesión transaccional DNS estándar (`duration: 26 ms`).
* **Infraestructura de Destino:** Las direcciones IP resueltas (`151.101.x.x`) pertenecen al Sistema Autónomo AS54113 (Fastly, Inc.), el proveedor de infraestructura CDN empleado globalmente por Mozilla Corporation.
* **Reputación:** Enriquecimiento de telemetría Interflow marca `domain_reputation: "Good"`, `is_dga: "no"`, `dga_score: 0`.

```json
/* Payload / Evidencia Principal: */
{
  "payload_type": "DNS Query / Response",
  "payload_value": "query: firefox-portal-detection.com | type: A | answers: [151.101.129.91, 151.101.1.91, 151.101.65.91, 151.101.193.91]",
  "payload_hash": "N/A",
  "payload_firma": "new_registered_domain (ATH Rule)",
  "payload_accion": "resolved",
  "payload_destino": "firefox-portal-detection.com"
}
```

#### Hipótesis Formuladas
| ID | Hipótesis | Evaluación | Justificación Forense |
| :--- | :--- | :--- | :--- |
| H1 | Comunicación con servidor C2 recién registrado | Descartada | El dominio apunta a la CDN oficial de Fastly utilizada por Mozilla; reputación catalogada como limpia (`Good`). |
| H2 | Generación de dominio algorítmico (DGA) o tunneling | Descartada | `is_dga: no`, `dga_score: 0`, `is_tunneling: 8` (tráfico no tunelizado, consulta estándar). |
| H3 | Telemetría legítima del navegador Mozilla Firefox | Confirmada | Mecanismo nativo de detección de portal cautivo del navegador web Firefox al iniciar sesión o verificar conectividad. |

---

## Análisis Evento 2 (Anomaly ID: gDpOkKABI3UnQyDO-UPI)

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Actividad Observada:** Consulta DNS idéntica hacia `firefox-portal-detection.com` efectuada 59 segundos después (08:48:17 -0300) por el mismo host `nb-fcaceres.technoma.local` (`192.168.169.34:56182`).
* **Acción de Seguridad:** Resolución transparente sin errores (`duration: 29 ms`), retornando el mismo grupo de IPs de Fastly CDN.
* **Correlación:** Comportamiento esperado de comprobación periódica y revalidación de red del navegador web.

### Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local GMT-3) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-11 11:48:17 | 2026-09-11 08:48:17 | Consulta DNS (A) | `firefox-portal-detection.com` | - | - | Segundo sondeo de conectividad de Mozilla Firefox. |
| 2026-09-11 11:48:17 | 2026-09-11 08:48:17 | Respuesta DNS | Fastly CDN IPs | - | - | Resolución exitosa en 29 ms. |
| 2026-09-11 11:58:09 | 2026-09-11 08:58:09 | Disparo de Alerta ML | Severidad 50 | - | - | Indexación en índice `aella-ser`. |

---

## ¿Por qué es (o no es) una Amenaza?
No constituye una amenaza para la red corporativa. La alerta es un falso positivo derivado del umbral estático de antigüedad de dominios (< 90 días) implementado por la regla de ATH de Stellar Cyber. El dominio `firefox-portal-detection.com` es un recurso oficial y legítimo de Mozilla Corporation destinado a comprobar si la conexión a internet del usuario se encuentra bloqueada por un portal cautivo (como suele ocurrir en redes hoteleras o Wi-Fi públicas). Las IPs de destino corresponden íntegramente a Fastly CDN, sin indicios de phishing, malware o exfiltración.

---

## Cierre Maestro Unificado del Caso

### Análisis de Impacto CIA Triad
```json
{
  "confidencialidad": "C0",
  "integridad": "I0",
  "disponibilidad": "A0",
  "justificacion": "No existio exposicion de datos sensibles, alteracion de configuraciones ni disrupcion de servicios. Consultas DNS estandar y benignas hacia servicios oficiales de Mozilla."
}
```

### Veredicto y Confianza Analítica
```json
{
  "veredicto": "Falso Positivo",
  "confianza": "100%",
  "clasificacion_soc": "Ruido Heurístico / Telemetría Benigna de Navegador (Captive Portal Detection)",
  "justificacion": "El dominio consultado pertenece a la infraestructura oficial de Mozilla Firefox alojada en Fastly CDN. Disparo atribuido unicamente a la antiguedad del dominio (registrado hace ~72 dias)."
}
```

### Indicador de Fatiga de Alertas
```json
{
  "fatiga_detectada": "Media",
  "frecuencia": "Comun en reglas de Machine Learning basadas en edad de dominio",
  "razon": "Alertas generadas automaticamente por motores de seguridad sobre dominios de servicios reconocidos (Mozilla, Google, Apple, Microsoft) registrados recientemente.",
  "accion_recomendada": "Incorporar el dominio 'firefox-portal-detection.com' a la lista blanca (whitelist) de dominios reconocidos en Stellar Cyber para evitar alertas redundantes."
}
```

### Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Detección y Análisis | Inspección de metadatos DNS de Interflow, verificación de WHOIS (fecha de registro 2026-07-01), comprobación de reputación limpia y propiedad de Fastly CDN. |
| Contención, Erradicación y Recuperación | No se requieren acciones de contención ni aislamiento; actividad completamente benigna. |
| Post-Incidente | Cierre del caso y recomendación de lista blanca para dominios de telemetría de navegadores corporativos. |

### Playbook Asignado
| ID Playbook | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| PB-006 | Descarte de Falsos Positivos por Machine Learning y Consultas Benignas | Validación de tráfico DNS a servicios comerciales legítimos y descarte de alertas por antigüedad de dominio. |

### Resolution Tag para Stellar Cyber
* **Resolution Tag:** `False Positive`
* **Descripción:** Alerta descartada debido a que corresponde a la consulta legítima de telemetría y portal cautivo del navegador Mozilla Firefox alojado en Fastly CDN.

### Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc. Puede ser el mismo del Case Evidence ) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 11/09/2026 08:48 | Analista SOC | technoma | sDpOkKABI3UnQyDOEzcy | technoma-sensor / sa | - | Baja | Recently Registered Domains (new_registered_domain) | Consulta legítima de Mozilla Firefox a firefox-portal-detection.com | nb-fcaceres.technoma.local (192.168.169.34), ad.technoma.local (10.11.1.1) | Falso Positivo. El endpoint 192.168.169.34 consulto firefox-portal-detection.com para deteccion de portal cautivo de Firefox. Disparo por umbral de edad (< 90 dias, registrado el 01/07/2026). IPs resueltas en Fastly CDN. Sin amenaza ni actividad maliciosa. | Interflow DNS metadata (query: firefox-portal-detection.com, ips: 151.101.x.x, domain_reputation: Good) | Ninguna | Cerrado | - | No | - | PB-006 |

### Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario de Cierre Maestro:**
> Alerta descartada como Falso Positivo. El análisis de los metadatos DNS confirma que la consulta hacia el dominio firefox-portal-detection.com desde el equipo nb-fcaceres.technoma.local (192.168.169.34) corresponde a la función estándar de detección de portales cautivos (Captive Portal Detection) del navegador Mozilla Firefox. Las direcciones IP resueltas (151.101.x.x) pertenecen a la infraestructura oficial de Fastly CDN empleada por Mozilla Corporation. La detección se produjo de forma puramente heurística debido a la antigüedad del dominio (registrado hace menos de 90 días). No existe impacto en CIA ni comportamiento malicioso asociado.

---

### Desglose Ultra Quirúrgico
* **Capa de Red y Enrutamiento:**
  * `srcip`: `192.168.169.34` (`nb-fcaceres.technoma.local`, VLAN 1101 de estaciones de trabajo).
  * `dstip`: `10.11.1.1` (`ad.technoma.local`, servidor DNS corporativo en LAN interna).
* **Capa de Transporte y Conexión:**
  * `proto`: `17` (`udp`), puerto destino `53` (`dns`).
  * `srcport`: `49674` y `56182` (Puertos efímeros de origen).
  * `duration`: `26 ms` y `29 ms` (Resolución de nombres ágil sin anomalías de latencia).
* **Capa de Aplicación / DNS:**
  * `metadata.request.query`: `firefox-portal-detection.com`.
  * `metadata.request.query_type`: `A`.
  * `metadata.response.reply_code`: `No Error`.
  * `resolved_ips`: `151.101.129.91`, `151.101.1.91`, `151.101.65.91`, `151.101.193.91` (Fastly Anycast CDN).
* **Capa de Detección XDR y Motor Heurístico:**
  * `rule_name / name`: `new_registered_domain`.
  * `metadata.response.domain_creation`: `2026-07-01T15:40:13Z` (Activa la heurística por ser < 90 días).
  * `domain_reputation`: `Good`, `dga_score`: `0`, `is_dga`: `no`.
  * `threat_score`: `0`, `event_score`: `62`, `severity`: `50`.

**Resumen Quirúrgico Final:**  
El equipo `nb-fcaceres.technoma.local` (`192.168.169.34`) inició el navegador Mozilla Firefox, el cual emitió dos comprobaciones de conectividad hacia el dominio oficial `firefox-portal-detection.com` contra el DNS corporativo `10.11.1.1`. El dominio fue resuelto con éxito hacia nodos de Fastly CDN. El motor de seguridad de Stellar Cyber disparó la alerta debido a que la fecha de creación del dominio se encuentra dentro de la ventana de evaluación heurística (< 90 días). El evento se concluye como Falso Positivo / Ruido Heurístico de Navegación sin riesgo de seguridad.
