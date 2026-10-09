# Reporte del SOC: Análisis de Alertas - Caso 12198

Se han detectado **3 eventos independientes** en el lote de logs analizado. A continuación se realiza el procesamiento técnico individual e independiente de cada uno de ellos, seguido de una correlación y cierre maestro unificado del caso.

---

# [Parte I] Análisis Individual de Eventos

## Análisis Evento 1: Internal SMB Read Anomaly

### 📘 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `SMB` | `GPO Sync` | `SAMR` | `Active Directory` | `False Positive`

### 📝 Resumen Ejecutivo del Evento 1 (Formato Nativo Stellar)
- **Origen:** El host `nb-agarcia.technoma.local` (IP: `192.168.169.76`, usuario `adrianagarcia` verificado en AD) dentro de la subred `VLAN1101`.
- **Comportamiento:** Picos de solicitudes de lectura SMB (84 consultas vs 12 típicas en 5 minutos) accediendo a los recursos compartidos administrativos de dominio.
- **Destino / Activo Afectado:** Controlador de Dominio `ad.technoma.local` (IP: `10.11.1.1`).
- **Severidad / Acción:** Severidad baja (20).

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-15 15:57:18 | 2026-07-15 12:57:18 | smb_read_anomaly | 84 | 12 | 7.0x | El host consulta recursos administrativos para actualización de directivas GPO. |

### 🔍 Desglose Técnico y Disección Forense
- **Recursos Involucrados:** El endpoint `192.168.169.76` accedió a los recursos compartidos `\\ad.technoma.local\IPC$` y `\\ad.technoma.local\SysVol`.
- **Traducción de Comandos SMBv2 (Rosetta Stone):**
  - **Comando 1 (`SMB2_OP_SESSION_SETUP`):** El host inicia el intercambio de credenciales y autenticación de la sesión.
  - **Comando 3 (`SMB2_OP_TREE_CONNECT`):** Establece la conexión al recurso IPC$.
  - **Comando 5 (`SMB2_OP_CREATE`):** Abre manejadores (handles) de archivos o pipes de intercomunicación.
  - **Comando 16 (`SMB2_OP_GETINFO`):** Consulta metadatos del archivo y descriptor de seguridad/permisos ACL.
  - **Comando 8 (`SMB2_OP_READ`):** Ejecuta la lectura del contenido.
  - **Comando 6 (`SMB2_OP_CLOSE`):** Cierra el manejador de forma voluntaria.
- **Causalidad:** Este patrón de comandos y el acceso secuencial a `IPC$` y `SysVol` corresponde al comportamiento normal del sistema operativo Windows al realizar la sincronización automática de Políticas de Grupo (GPO Refresh) o al consultar las OUs del usuario a través de llamadas RPC SAMR durante el login.

**Payload / Evidencia Principal (Evento 1):**
```json
{
  "payload_type": "SMB Share Access",
  "payload_value": "\\\\ad.technoma.local\\IPC$ y \\\\ad.technoma.local\\SysVol",
  "payload_hash": "N/A",
  "payload_firma": "N/A",
  "payload_accion": "Allowed Session & File Reads",
  "payload_destino": "10.11.1.1:445"
}
```

#### Comandos de Diagnóstico Recomendados
* Para diagnosticar el refresco de GPO en el host: `gpupdate /force`
* Para verificar sesiones SMB activas en el DC: `Get-SmbSession -ClientAddress "192.168.169.76"`

#### Hipótesis Formuladas
| Hipótesis | Detalles y Validación | Veredicto |
| :--- | :--- | :--- |
| **Volcado de Directorio / Reconocimiento** | Un atacante escanea las carpetas compartidas del dominio en búsqueda de credenciales (SYSVOL XMLs). Refutada porque el volumen y los comandos se limitan al flujo nativo de GPO. | Refutada |
| **Sincronización de Directivas (GPO)** | Comportamiento del sistema operativo Windows actualizando políticas locales. Confirmada por comandos de Rosetta Stone y recursos involucrados. | **Confirmada** |

### 🔬 Desglose Ultra Quirúrgico (Evento 1)
- **Capa de Red/Enrutamiento:** Conexión origen en `VLAN1101` y destino en `VLAN1101` (comunicación directa interna).
- **Capa de Transporte:** Protocolo TCP (proto 6), puerto origen efímero `49743` y puerto destino `445` (SMB).
- **Capa de Aplicación:** Protocolo SMBv2 (versión 2 en el log), comandos de lectura e información.
- **Motor ML:** El motor `new_ml` detecta la anomalía de comportamiento de red (`internal_smb_read_anomaly`) basándose en una desviación estadística (84 lecturas frente a un promedio normal de 12 eventos en el mismo rango de 5 minutos).

---

## Análisis Evento 2: Exploit Attempt - AnyDesk Relay Domain (Internal DNS Query)

### 📘 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `DNS` | `AnyDesk` | `Remote Access` | `IDS Anomaly` | `False Positive`

### 📝 Resumen Ejecutivo del Evento 2 (Formato Nativo Stellar)
- **Origen:** El host `nb-farias.technoma.local` (IP: `192.168.169.94`) dentro de la subred administrativa `VLAN1101`.
- **Comportamiento:** Picos de resolución DNS hacia dominios dinámicos de AnyDesk (`relay-cc931ef4.net.anydesk.com`) para establecer enlaces de soporte remoto.
- **Destino / Activo Afectado:** Servidor DNS local / Controlador de Dominio `ad.technoma.local` (IP: `10.11.1.1`).
- **Severidad / Acción:** Severidad baja (25).

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-15 16:10:14 | 2026-07-15 13:10:14 | DNS Query / exploit_attempt_priv_priv | 9 | 1.5 | 6.0x | Petición DNS local hacia CDN/Relay de AnyDesk bloqueada o registrada por firmas IDS. |

### 🔍 Desglose Técnico y Disección Forense
- **Mecanismo:** La aplicación legítima AnyDesk realiza ráfagas de consultas UDP/53 (DNS) paralelas para encontrar la ruta de retransmisión más rápida hacia sus servidores de relevo global (`relay-*.net.anydesk.com`).
- **Firma IDS Interceptada:** `INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup` (`SID: 2060507`). Esta firma es puramente informativa, pero el motor de Machine Learning de Stellar la clasifica como un pico volumétrico de explotación debido al conteo dinámico acumulado.

**Payload / Evidencia Principal (Evento 2):**
```json
{
  "payload_type": "DNS Query",
  "payload_value": "relay-cc931ef4.net.anydesk.com",
  "payload_hash": "N/A",
  "payload_firma": "N/A",
  "payload_accion": "Allowed Query (A)",
  "payload_destino": "10.11.1.1:53"
}
```

#### Comandos de Diagnóstico Recomendados
* Para validar procesos de red de AnyDesk: `Get-NetTCPConnection -RemotePort 443 | Where-Object { (Get-Process -Id $_.OwningProcess).Name -eq "AnyDesk" }`

#### Hipótesis Formuladas
| Hipótesis | Detalles y Validación | Veredicto |
| :--- | :--- | :--- |
| **Herramienta de Acceso No Autorizado** | Un atacante instaló software de control remoto para evadir controles perimetrales. Refutada porque AnyDesk es software institucionalmente autorizado en Technoma. | Refutada |
| **Uso de soporte técnico autorizado** | El host ejecuta el cliente institucional AnyDesk para recibir asistencia remota. Confirmada por las bases de datos de software de Technoma. | **Confirmada** |

### 🔬 Desglose Ultra Quirúrgico (Evento 2)
- **Capa de Red/Enrutamiento:** Conexión origen en `VLAN1101` y destino en `VLAN1101` (comunicación directa al resolvedor DNS local).
- **Capa de Transporte:** Protocolo UDP (proto 17), puerto origen `52493` y puerto destino `53` (DNS).
- **Capa de Aplicación:** Protocolo DNS, consulta tipo A para la resolución del subdominio de retransmisión.
- **Motor ML:** El motor `new_ml` detecta la anomalía de comportamiento de red (`exploit_attempt_priv_priv`) basándose en la activación de la firma Suricata `INFO Anydesk Relay Domain`.

---

## Análisis Evento 3: Exploit Attempt - AnyDesk Relay Domain (External DNS Forwarder)

### 📘 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `DNS` | `AnyDesk` | `Domain Controller` | `DNS Forwarder` | `False Positive`

### 📝 Resumen Ejecutivo del Evento 3 (Formato Nativo Stellar)
- **Origen:** Servidor Controlador de Dominio `ad.technoma.local` (IP: `10.11.1.1`).
- **Comportamiento:** Peticiones DNS recursivas dirigidas externamente hacia `8.8.8.8` para resolver el subdominio `relay-cc931ef4.net.anydesk.com`.
- **Destino / Activo Afectado:** Servidor DNS de Google `dns.google` (IP: `8.8.8.8`).
- **Severidad / Acción:** Severidad baja (27).

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-15 16:10:14 | 2026-07-15 13:10:14 | DNS Query / exploit_attempt_priv_pub | 7 | 1 | 7.0x | El DC reenvía de forma recursiva a 8.8.8.8 la consulta DNS recibida del cliente 192.168.169.94. |

### 🔍 Desglose Técnico y Disección Forense
- **Mecanismo (La Trampa del DNS Forwarder):** El Controlador de Dominio `10.11.1.1` actúa como el resolvedor DNS de la red interna. Cuando el cliente `192.168.169.94` (Evento 2) consulta por un dominio externo, el DC realiza una consulta recursiva y la reenvía a su forwarder externo configurado (`8.8.8.8`).
- **Mapeo Erróneo:** Los sensores IDS perimetrales detectan al DC iniciando conexiones DNS outbound de AnyDesk y asumen erróneamente que el servidor crítico está infectado con un agente de acceso remoto.
- **Correlación:** Este evento está 100% correlacionado y es consecuencia directa de la consulta legítima de AnyDesk detallada en el **Evento 2**.

**Payload / Evidencia Principal (Evento 3):**
```json
{
  "payload_type": "DNS Query Outbound",
  "payload_value": "relay-cc931ef4.net.anydesk.com",
  "payload_hash": "N/A",
  "payload_firma": "N/A",
  "payload_accion": "Allowed Forwarded Query",
  "payload_destino": "8.8.8.8:53"
}
```

#### Comandos de Diagnóstico Recomendados
* Para verificar los Forwarders en el Controlador de Dominio (PowerShell): `Get-DnsServerForwarder`

#### Hipótesis Formuladas
| Hipótesis | Detalles y Validación | Veredicto |
| :--- | :--- | :--- |
| **Infección C2 en Servidor Crítico** | El DC hospeda un implante de AnyDesk no autorizado. Refutada porque el DC no tiene sockets AnyDesk propios; actúa exclusivamente como resolvedor recursivo de la LAN. | Refutada |
| **Trampa de Reenvío DNS (Forwarder)** | El DC procesa recursivamente la resolución solicitada por la workstation del usuario. Validada por timestamps y puertos de conexión. | **Confirmada** |

### 🔬 Desglose Ultra Quirúrgico (Evento 3)
- **Capa de Red/Enrutamiento:** Conexión origen en `VLAN1101` hacia la red externa (WAN) de internet.
- **Capa de Transporte:** Protocolo UDP (proto 17), puerto origen `62452` y puerto destino `53` (DNS).
- **Capa de Aplicación:** Protocolo DNS, consulta recursiva enviada por el resolvedor interno.
- **Motor ML:** El motor `new_ml` detecta la anomalía de comportamiento de red (`exploit_attempt_priv_pub`) basándose en la consulta externa saliente hacia Google DNS.

---

# [Parte II] Correlación y Cierre Maestro de Caso

### ❓ ¿Por qué es (o no es) una Amenaza?
**No representa una amenaza.** 
- El Evento 1 corresponde a la sincronización rutinaria de GPOs y consultas SAMR entre la máquina de un usuario legítimo (`adrianagarcia`) y el Controlador de Dominio. 
- Los Eventos 2 y 3 corresponden a la resolución normal del servicio AnyDesk en el endpoint `nb-farias.technoma.local` que desencadenó una consulta recursiva desde el Controlador de Dominio hacia internet (`8.8.8.8`). Dado que AnyDesk es la **herramienta oficial autorizada en todos los equipos de Technoma**, las firmas IDS detectadas no corresponden a ninguna brecha de seguridad.

### 🔐 Análisis de Impacto CIA Triad
```json
{
  "Confidentiality": "None",
  "Integrity": "None",
  "Availability": "None",
  "Justification": "Toda la actividad analizada corresponde al funcionamiento operativo normal de herramientas de soporte autorizadas y funciones de infraestructura de Active Directory."
}
```

### 🎯 Veredicto y Confianza Analítica
```json
{
  "Verdict": "False_Positive",
  "Confidence_Score": 100,
  "Justification": "Los picos volumétricos de red y las firmas IDS informativas corresponden a servicios institucionales autorizados (AnyDesk y GPO Sincronización) documentados formalmente en la memoria institucional."
}
```

### ⚠️ Indicador de Fatiga de Alertas
```json
{
  "Fatigue_Level": "High",
  "Reason": "El sistema duplicó la alerta de AnyDesk en el host origen y en el DC (DNS Forwarder Trap), además de generar alertas basadas en umbrales estadísticos de red para procesos estándar de GPO."
}
```

### 🔄 Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| **Detección y Análisis** | Correlación temporal cruzada del cliente y el DC para trazar el flujo DNS y SMB. |
| **Contención, Erradicación y Recuperación** | Silenciar las alertas. Como recomendación de postura, aconsejar a infraestructura configurar resolvedores externos filtrados (ej. Cisco Umbrella) para el DC y desactivar Delivery Optimization o WUDO de red si es necesario. |

### 🧪 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| **PB 2.5/2.6** | Sincronización GPO & Software de Acceso Autorizado | Cubre la resolución legítima de AnyDesk local y el refresco normal de directivas de dominio. |

### 🏷️ Resolution Tag para Stellar Cyber
* **Tag:** `False Positive`
* **Descripción:** Tráfico operativo benigno (AnyDesk e IPC$/SysVol GPO Sync).

### 📋 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc. Puede ser el mismo del Case Evidence ) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-15 16:10:14 | Antigravity | technoma | 12198 | new_ml / Suricata | 12198-M | Baja | False Positive | Falsos positivos por GPO Refresh y tráfico DNS AnyDesk autorizado | nb-agarcia (192.168.169.76), nb-farias (192.168.169.94), ad.technoma.local (10.11.1.1) | Tráfico SMB recursivo hacia DC por sincronización de GPO y resolución DNS externa de AnyDesk desde equipos autorizados | smb_path: \IPC$, \SysVol; domain: relay-*.anydesk.com; sid: 2060507 | Ninguna. Tráfico de red autorizado y operativo. | Cerrado | N/A | No | N/A | PB 2.5 / PB 2.6 |

### ✅ Instrucción para Cierre Maestro en Stellar Cyber
* **Estado:** Cerrado / Falso Positivo
* **Resolution Tag:** `False Positive`
* **Comentario:**
> "Lote de alertas cerrado como Falso Positivo. La investigación confirma que la alerta de red SMB corresponde a un flujo legítimo de sincronización de Políticas de Grupo (GPO Refresh) entre la workstation de `adrianagarcia` (`192.168.169.76`) y el Controlador de Dominio. Asimismo, las alertas IDS de AnyDesk corresponden al uso de la herramienta de soporte remoto autorizada corporativamente desde el endpoint de `nb-farias` (`192.168.169.94`), desencadenando un reenvío recursivo normal en el DC hacia el puerto 53 externo. No se observa actividad maliciosa ni intrusiones de red."

> [!TIP]
> Dado que AnyDesk es el software oficial y las sincronizaciones de GPO son predecibles, estas alertas estadísticas deben silenciarse para evitar la fatiga y optimizar los umbrales de Machine Learning.
