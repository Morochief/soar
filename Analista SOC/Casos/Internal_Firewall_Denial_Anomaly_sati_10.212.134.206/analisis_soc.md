# Reporte SOC - Caso: Internal Firewall Denial Anomaly (sati - 10.212.134.206)

**Fecha de Analisis:** 2026-09-05
**Analista:** Analista SOC Senior (DFIR)
**Tenant:** technoma
**Case ID:** Internal_Firewall_Denial_Anomaly_sati_10.212.134.206
**Fuente:** Stellar Cyber XDR / FortiGate Syslog (`FG-Technoma` / `FG120GTK24022543`)
**XDR Event:** Internal Firewall Denial Anomaly (`internal_fw_action`) | TTP: MITRE T1046 (Network Service Discovery) / TA0007 (Discovery) / XT2002 (XDR Firewall Anomaly)

---

> He detectado **2 eventos independientes** en el bloque crudo. Ambos corresponden a ventanas consecutivas de 5 minutos sobre la misma sesión VPN. Se analizan secuencialmente concluyendo con el cierre maestro unificado.

---

## Analisis Evento 1 (Denegacion Firewall UDP 53 / Anomalia 738 bloqueos)

### Tags:
`#FortiGate` `#FirewallDenial` `#VPNSSL` `#Sati` `#ProveedorOdoo` `#DNS` `#FalsoPositivo` `#RuidoDePostura`

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
- **Origen:** `10.212.134.206` (Pool IP asignado por túnel SSL VPN `ssl.root`)
- **Usuario Autenticado:** `sati` (Proveedor externo autorizado de soporte Odoo - authserver: `sati`)
- **Destino:** `10.11.1.1:53` (`ad.technoma.local` - Controlador de Dominio / Servidor DNS central)
- **Interfaz Origen / Destino:** `srcintf: ssl.root` -> `dstintf: Citrix Servers` (interfaz LAN)
- **Accion de Firewall:** `deny` por política por defecto (`policyid=0`, `rule_id=0`)
- **Servicio / Protocolo:** `DNS` / UDP puerto 53 (`proto: 17`)
- **Score / Severidad:** Event Score 71 | Severity 60 | Fidelidad: 99.77%
- **Metricas de Trafico:** Actual: 738 denegaciones | Tipico: 83 | Ratio: ~8.9x (en ventana de 5 minutos)

### Linea de Tiempo Temporal
| Hora (UTC) | Hora (Local PYT) | Evento Detectado | Actual | Typical | Ratio | Observacion Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-05 15:15:09 | 2026-09-05 12:15:09 | Ráfaga de 738 consultas DNS bloqueadas por FortiGate hacia 10.11.1.1 | 738 | 83 | 8.89x | Log FortiOS nativo (logid: 0000000013) indicando denegación en policyid: 0. |

### Desglose Tecnico y Diseccion Forense
- **Identidad del Actor y Memoria Institucional:**
  En `SOC_GEM_v2.md` se encuentra documentado textualmente:
  > **Usuario `sati` / IP `10.212.134.x` (VPN `ssl.root`):** Proveedor externo de soporte Odoo — empresa tercera autorizada. Se conecta vía SSL VPN (`ssl.root`, pool IP `10.212.x.x`). Las denegaciones del FortiGate a `policyid: 0` indican que la política VPN no le permite llegar al DC por DNS (puerto 53) — es un problema de configuración, no un ataque. **Falso Positivo / Problema de Postura**.
- **Mecanismo Tecnico de la Falla:**
  Cuando el usuario `sati` levanta el túnel FortiClient SSL VPN, su sistema operativo hereda como servidor DNS la dirección `10.11.1.1` (o su equipo intenta resolver nombres corporativos de Technoma). Sin embargo, en el firewall `FG-Technoma`, las políticas de seguridad para el túnel de proveedores (`ssl.root`) tienen restringido el tráfico hacia la LAN exclusivamente a los servidores de Odoo/aplicaciones, **sin incluir una regla permisiva para el servicio DNS (UDP/53)** hacia el DC `10.11.1.1`.
- **Efecto en Cascada:** Al no recibir respuesta DNS, la pila de red del cliente reintenta de forma automática e insistente resolver nombres de dominio internos o externos, generando cientos de paquetes por minuto (`actual: 738`) que el FortiGate descarta limpiamente (`sentbyte=0, rcvdbyte=0, duration=0, action=deny`).
- **Evaluacion de Riesgo:** El tráfico fue 100% mitigado por el cortafuegos. No hubo penetración, escaneo de puertos ni movimiento lateral.

```json
{
  "payload_type": "firewall_log",
  "payload_value": "srcip=10.212.134.206 dstip=10.11.1.1 dstport=53 proto=17 action=deny policyid=0",
  "payload_hash": "N/A - log de tráfico descartado",
  "payload_firma": "logid=0000000013 | devname=FG-Technoma | user=sati",
  "payload_accion": "Deny / Drop de paquete DNS UDP 53 por regla implícita 0",
  "payload_destino": "10.11.1.1:53 (ad.technoma.local)"
}
```

---

## Analisis Evento 2 (Denegacion Firewall UDP 53 / Anomalia 479 bloqueos)

### Tags:
`#FortiGate` `#FirewallDenial` `#Sati` `#ContinuidadDeFalla` `#FalsoPositivo`

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
- **Origen:** `10.212.134.206` (Misma IP de pool SSL VPN)
- **Usuario Autenticado:** `sati`
- **Destino:** `10.11.1.1:53`
- **Accion de Firewall:** `deny` en `policyid=0`
- **Score / Severidad:** Event Score 70 | Severity 60 | Fidelidad: 95.92%
- **Metricas de Trafico:** Actual: 479 denegaciones | Tipico: 83 | Ratio: ~5.7x

### Linea de Tiempo Temporal
| Hora (UTC) | Hora (Local PYT) | Evento Detectado | Actual | Typical | Ratio | Observacion Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-05 15:20:07 | 2026-09-05 12:20:07 | Continuación de la ráfaga de consultas DNS bloqueadas (479 reintentos) | 479 | 83 | 5.77x | Exactamente 5 minutos después del Evento 1. Mismo flujo, misma sesión VPN persistente. |

### Desglose Tecnico y Diseccion Forense
- Continuación cronológica idéntica del Evento 1 dentro de la siguiente ventana de cálculo de 5 minutos del sensor de Stellar Cyber.
- El usuario `sati` permaneció conectado a la VPN trabajando sobre los servidores autorizados mientras su estación de trabajo continuó intentando resolver peticiones DNS de fondo contra el controlador de dominio.
- El cortafuegos `FG-Technoma` mantuvo el descarte efectivo sin permitir ningún flujo hacia `10.11.1.1`.

---

## 🏛️ El Concilio SOC ha deliberado

> **Problema a analizar:** El motor de Stellar Cyber disparó dos alertas con severidad 60 y event_score 71 por más de 1.200 conexiones UDP/53 bloqueadas hacia el controlador de dominio `10.11.1.1` provenientes de una IP del túnel SSL VPN (`10.212.134.206`) perteneciente al usuario `sati`.

🔴 **Perspectiva Red Team:**
Un volumen masivo de cientos de paquetes UDP a puerto 53 descartados por la regla de denegación por defecto (`policyid: 0`) podría simular un intento de reconocimiento de resolución de nombres o un DNS amplification/fuzzing. Sin embargo, no hay variación de puertos destino, no hay escaneo de otros servicios de red ni explotación; es un flujo monótono y automático contra un único servicio estándar.

🔵 **Perspectiva Blue Team:**
El usuario `sati` es el proveedor homologado de soporte del sistema Odoo corporativo. El tráfico proviene de la interfaz VPN oficial `ssl.root`. El firewall FortiGate está cumpliendo su función de bloqueo estricto (`action=deny`). El problema es puramente de arquitectura de red (falta de política DNS o resolución de split-DNS en el cliente VPN).

🟢 **Perspectiva Threat Intel:**
No hay presencia de direcciones IP externas hostiles ni software malicioso. El evento se mantiene confinado a la infraestructura interna y al túnel SSL corporativo.

---

## 🧠 Sintesis y Decision Final (Mentor DFIR)

El caso representa un **Falso Positivo Operativo / Problema de Postura y Enrutamiento VPN Documentado**.
El proveedor externo `sati` se conectó por SSL VPN para tareas operativas de Odoo. Su equipo intentó enviar consultas DNS al resolver institucional `10.11.1.1`, pero debido a que el FortiGate no tiene una regla explícita que permita tráfico DNS desde la VPN de proveedores hacia el DC, los paquetes son descartados por la regla por defecto (`policyid=0`), disparando la anomalía volumétrica de Stellar Cyber.

---

## 🛡️ Analisis de Impacto CIA Triad
```json
{
  "Confidencialidad": "Intacta (El trafico fue denegado y ningun dato fue expuesto)",
  "Integridad": "Intacta (No hubo acceso a configuraciones ni modificaciones)",
  "Disponibilidad": "Baja en el cliente (El usuario sati podria tener dificultades de resolucion de nombres internos)"
}
```

---

## ⚖️ Veredicto y Confianza Analitica
```json
{
  "Veredicto": "Falso Positivo (Problema de Postura / Ruteo DNS en Tunel VPN sati)",
  "Confianza": "100%",
  "Justificacion": "Comportamiento plenamente tipificado en la Memoria Institucional de Technoma (SOC_GEM_v2.md). Corresponde a reintentos DNS del proveedor externo sati bloqueados por la regla de denegacion por defecto (policyid: 0) en el FortiGate. Impacto de seguridad nulo."
}
```

---

## 📉 Indicador de Fatiga de Alertas
```json
{
  "nivel_fatiga": "MUY ALTO",
  "razon": "Cada vez que el proveedor sati se conecta a la VPN para trabajar en Odoo, genera cientos de eventos de firewall denial y detona alertas en Stellar Cyber.",
  "accion": "Derivar a Infraestructura para corregir la politica en el FortiGate (habilitar DNS a 10.11.1.1 o configurar DNS publico en el perfil VPN) o afinar la regla internal_fw_action para excluir srcip 10.212.134.x hacia puerto 53."
}
```

---

## 📘 Fase del Ciclo NIST 800-61
| Fase NIST | Accion Tecnica |
| :--- | :--- |
| Deteccion y Analisis | Triaje del log de firewall y confirmacion de usuario sati en base de conocimiento institucional. |
| Contencion | No requerida (Mitigado automaticamente por el firewall perimetral). |
| Post-Incidente | Cierre en Stellar Cyber, registro en bitacora y notificacion preventiva a Infraestructura. |

---

## 📚 Playbooks Asignados (Marco Operativo Technoma)
| ID / Playbook | Nombre del Playbook | Rol Asignado | Justificación Estratégica |
| :--- | :--- | :--- | :--- |
| **PB 5.2** | Problemas de Configuración, Postura y Servicios Vulnerables Abiertos | Analista N1 / Infraestructura | Aborda los desajustes de políticas en firewalls y accesos de terceros vía VPN que generan tráfico denegado recurrente. |

---

## 🏷️ Resolution Tag para Stellar Cyber
**Tag:** `False Positive` (o `Policy Enforcement` / `Benign`)
**Descripcion:** Denegación preventiva de consultas DNS (UDP 53) en FortiGate provenientes del proveedor externo sati vía SSL VPN por falta de política permisiva hacia 10.11.1.1. Ruido operativo documentado.

---

## 📝 Datos para Bitacora de Excel (UNA SOLA LINEA EN TABLA)

| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Deteccion | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripcion | Evidencia (Logs, etc. Puede ser el mismo del Case Evidence ) | Solicitud de Accion | Estado | URL | Generacion de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-05 12:20 | Analista SOC Senior | technoma | Internal_Firewall_Denial_Anomaly_sati_10.212.134.206 | FG-Technoma / new_ml | N/A | Baja | Internal Firewall Denial Anomaly | Consultas DNS de sati (VPN Odoo) bloqueadas por FortiGate hacia 10.11.1.1 | FG-Technoma, ad.technoma.local (10.11.1.1), usuario sati (10.212.134.206) | 2 alertas (738 y 479 bloqueos). FP operativo: proveedor autorizado Odoo (sati) conectado via SSL VPN intenta resolver DNS contra 10.11.1.1 pero el trafico es denegado por policyid:0. Control efectivo de firewall. | FortiGate syslog (proto: 17, dstport: 53, policyid: 0, action: deny, authserver: sati) | Notificar a Infraestructura para ajustar politica VPN de sati o asignar DNS publico en FortiClient. | Cerrado | N/A | NO | N/A | PB 5.2 |

---

## 💻 Instruccion para Cierre en Stellar Cyber

**Estado:** Closed  
**Resolution Tag:** `False Positive`  
**Comentario:**  
> Se analizaron 2 eventos correlacionados bajo la alerta `Internal Firewall Denial Anomaly` vinculados a la IP `10.212.134.206` (túnel SSL VPN de Technoma) asociada al usuario `sati` (proveedor externo autorizado para soporte de Odoo).
> 
> La telemetría de FortiGate (`FG-Technoma`) confirma que los bloqueos corresponden exclusivamente a tráfico DNS (UDP puerto 53) dirigido hacia el controlador de dominio `10.11.1.1`, descartado limpiamente por la política de seguridad por defecto (`policyid=0`). Comportamiento tipificado en la Memoria Institucional: la política de VPN no contempla resolución DNS hacia el segmento del DC, provocando reintentos automatizados por parte del cliente.
> 
> Actividad descartada como Falso Positivo Operativo / Ruido de Postura. El tráfico se encuentra completamente mitigado por el firewall, sin evidencia de escaneo malicioso ni compromiso.

---

## 🔬 Desglose Ultra Quirurgico
- **Capa de Red / Enrutamiento:** Túnel SSL VPN establecido (`srcintf: ssl.root`) asignando la dirección IP `10.212.134.206` al usuario `sati`. El destino es `10.11.1.1` a través de la interfaz `Citrix Servers` (rol LAN).
- **Capa de Transporte:** Paquetes UDP con puerto origen efímero (`41446` y `53305`) y puerto destino `53` (`service: DNS`, `proto: 17`).
- **Capa de Firewall (FortiOS):** Regla evaluada: `policyid=0` (Implicit Deny). El motor de firewall aplica la acción `deny`, registrando `duration=0, sentbyte=0, rcvdbyte=0, crscore=30, craction=131072`.
- **Capa SIEM (Stellar Cyber):** El analizador `filter_stellar_parser-forti_fortigate` normaliza el syslog y el modelo de Machine Learning (`internal_fw_action`) dispara la alerta debido a que el recuento de denegaciones (`actual: 738` y `479`) superó la media típica esperada (`typical: 83`).
- **Resumen Quirúrgico Final:** La denegación en cascada es producto de un desajuste de configuración en el pool de clientes VPN de terceros y la falta de permiso para tráfico DNS hacia el DC. Mitigación transparente y cierre como Falso Positivo.
