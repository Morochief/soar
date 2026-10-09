# Reporte SOC - Caso: Sophos CoreBlockedDriverDetection (IntcDAud.sys - CJPPA20170828)

**Fecha de Analisis:** 2026-09-04
**Analista:** Analista SOC Senior (DFIR)
**Tenant:** CAJAANDE
**Case ID:** Sophos_Blocked_Driver_IntcDAud_CJPPA20170828
**Fuente:** Stellar Cyber XDR / Sophos Central (`sophos_CAJA-ANDE-SOPHOS`)
**XDR Event:** `sophos_event-xdr_eba-xdr_endpoint_indicator_of_threat`
**Subtipo:** `Event::Endpoint::CoreBlockedDriverDetection`
**Mapeo MITRE:** T1068 (Exploitation for Privilege Escalation) / T1543.003 (Create or Modify System Process: Windows Service) / T1574 (Hijack Execution Flow) / BYOVD (Bring Your Own Vulnerable Driver)

---

> He detectado **2 eventos independientes** en el bloque JSON. El Evento 2 es una retransmisión idéntica (duplicado) del Evento 1 originada por el mismo registro base en Sophos Central (`sophos.id: fa059987-9724-4b32-99fb-c9e6b727cf33`). Se analizan de forma unificada bajo un único cierre maestro.

---

## Analisis Forense del Evento (Deteccion de Driver Bloqueado)

### Tags:
`#TruePositiveBenigno` `#DriverVulnerable` `#BYOVD` `#IntelDisplayAudio` `#IntcDAud` `#SophosCentral` `#DriverBlocklist` `#CAJAANDE`

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
- **Host Afectado:** `CJPPA20170828` | IP: `172.16.202.86` (Segmento LAN Corporativo Caja Ande)
- **Usuario de Sesión:** `CAJAANDE\MP5681371`
- **Driver Detectado:** `C:\Windows\System32\drivers\IntcDAud.sys`
- **Hash SHA-256:** `5c1135081e29d7f4a97d5caa2c8fbe1dd04ec7a3d8e648e69f2aa9ebdd88ebbb`
- **Origen de la Detección:** `DRIVER_BLOCKLIST` (Lista oficial de bloqueo de controladores de Sophos / Microsoft WDAC)
- **Amenaza Declarada:** `UnauthorizedDriver`
- **Severidad / Score:** Severidad Sophos: `medium` (45) | Event Score Stellar: 45 | Fidelidad: 45
- **Mecanismo de Detección:** `Event::Endpoint::CoreBlockedDriverDetection` (Motor Core de Sophos Intercept X)

### Linea de Tiempo Temporal
| Hora (UTC) | Hora (Local PYT) | Evento Detectado | Observacion Forense |
| :--- | :--- | :--- | :--- |
| 2026-09-04 10:42:10 | 2026-09-04 06:42:10 | Ejecución / Carga de driver `IntcDAud.sys` interceptada por Sophos | Bloqueo preventivo en runtime ejecutado por la regla DRIVER_BLOCKLIST. |
| 2026-09-04 10:42:29 | 2026-09-04 06:42:29 | Emisión del evento en Sophos Central | Registro enviado hacia el SIEM con severidad Media (45). |

### Evidencia Forense Concluyente (Live Response)

1. **Antigüedad del Archivo e Integridad (Falso Ataque descartado):**
   - `CreationTime` y `LastWriteTime`: **12/05/2016 04:32:26** (Archivo presente desde la instalación original del equipo hace 10 años).
   - Firma Digital: **Valid** comprobada por `Microsoft Windows Hardware Compatibility Publisher`.
   - Versión del Fabricante: `Intel(R) Display Audio Driver` versión `6.16.00.3197` (Intel Corporation).

2. **Causa Raíz del Disparo de la Alerta Hoy (Reconstrucción Cronológica):**
   - **07:39:22 Local (10:39:22 UTC):** El equipo encendió/reinició (`LastBootUpTime: 4/9/2026 07:39:22`).
   - **07:39:28 Local (10:39:28 UTC):** El servicio broker de protección de exploits de Sophos (`hmpalertsvc`) arrancó tras el booteo, aplicando las actualizaciones de políticas de mitigación de drivers.
   - **07:42:10 Local (10:42:10 UTC):** Al inicializarse el servicio del Kernel `IntcDAud` (Sonido Intel para pantallas - Start: 3 / Demand Start), el motor `hmpalertsvc` evaluó la versión instalada (`6.16.00.3197`) contra la lista `DRIVER_BLOCKLIST`.
   - Al coincidir con una versión vulnerable obsoleta de 2016 con fallas conocidas de Ring 0 / BYOVD, Sophos generó localmente el **Evento 53 en Application**: `Driver "C:\Windows\System32\drivers\IntcDAud.sys" is not authorized`, bloqueando su interacción no segura.

3. **Conclusión Pericial:**
   El equipo estuvo apagado y al encender hoy a las 07:39:22, el inicio del servicio PnP de audio disparó por primera vez la evaluación contra la lista de bloqueo de Sophos. Riesgo contenido y mitigado automáticamente por el EDR.

```json
{
  "driver_path": "C:\\Windows\\System32\\drivers\\IntcDAud.sys",
  "sha256": "5c1135081e29d7f4a97d5caa2c8fbe1dd04ec7a3d8e648e69f2aa9ebdd88ebbb",
  "threat_name": "UnauthorizedDriver (Driver Vulnerable en Blocklist)",
  "vendor": "Intel Corporation (Display Audio)",
  "sophos_action": "Bloqueado en runtime (CoreBlockedDriverDetection)",
  "mecanismo_prevencion": "DRIVER_BLOCKLIST"
}
```

---

## 🏛️ El Concilio SOC ha deliberado

> **Problema a analizar:** Alerta de `CoreBlockedDriverDetection` en `CJPPA20170828` por presencia de `IntcDAud.sys` en la lista negra de drivers.

🔴 **Perspectiva Red Team:**
Los drivers vulnerables legítimos firmados por Intel son vectores clásicos de escalada a Kernel (BYOVD). Sin embargo, aquí no hay un dropper ni herramienta que intente cargar el driver de forma forzada; está ubicado en la ruta estándar de drivers de Windows y su carga fue frustrada por el hook de Sophos.

🔵 **Perspectiva Blue Team:**
El motor de mitigación de explotación de Sophos funcionó a la perfección. La versión instalada en la máquina es obsoleta y vulnerable. Debe coordinarse con Soporte Técnico de Caja Ande la actualización del paquete de drivers de Intel a una versión reciente y no vulnerable para evitar degradación de audio y reincidencia de alertas.

🟢 **Perspectiva Threat Intel:**
El hash corresponde a versiones antiguas de Intel Graphics/Audio ampliamente documentadas en listas de bloqueo de Microsoft y Sophos.

---

## 🧠 Sintesis y Decision Final (Mentor DFIR)

El evento se clasifica técnicamente como **True Positive Benigno / Riesgo Tecnológico Mitigado (Driver Legítimo pero Vulnerable Bloqueado por Política)**.
1. La protección de endpoint contuvo la amenaza automáticamente impidiendo la carga del driver.
2. No hubo compromiso de integridad ni escalada de privilegios.
3. Se debe notificar a soporte para la remediación preventiva (actualización del driver oficial de Intel en la estación).

---

## 🛡️ Analisis de Impacto CIA Triad
```json
{
  "Confidencialidad": "Intacta (No hubo exposicion de informacion)",
  "Integridad": "Intacta (El driver vulnerable fue bloqueado antes de acceder a Ring 0)",
  "Disponibilidad": "Bajo Impacto Potencial (La salida de audio por HDMI/DisplayPort podria no funcionar hasta actualizar el driver)"
}
```

---

## ⚖️ Veredicto y Confianza Analitica
```json
{
  "Veredicto": "True Positive Benigno (Driver Vulnerable Legítimo Bloqueado Exitosamente por EDR)",
  "Confianza": "100%",
  "Justificacion": "El archivo C:\\Windows\\System32\\drivers\\IntcDAud.sys pertenece al controlador de audio HDMI de Intel. Sophos intercepto su carga debido a que la version coincide con la lista de bloqueo (DRIVER_BLOCKLIST) por vulnerabilidades conocidas de Ring 0 (BYOVD). Bloqueo preventivo exitoso sin compromiso."
}
```

---

## 📉 Indicador de Fatiga de Alertas
```json
{
  "nivel_fatiga": "MEDIO",
  "razon": "Reincidencia de bloqueos de drivers desactualizados en endpoints de Caja Ande cada vez que inicia el sistema o se conecta una pantalla.",
  "accion": "Desplegar parches de drivers de Intel via WSUS/SCCM en equipos con hardware similar."
}
```

---

## 📘 Fase del Ciclo NIST 800-61
| Fase NIST | Accion Tecnica |
| :--- | :--- |
| Deteccion y Analisis | Confirmacion de bloqueo preventivo de driver vulnerable de Intel. |
| Contencion | Contencion automatica efectiva aplicada por Sophos Central. |
| Erradicacion / Remediacion | Coordinar con TI la actualizacion del controlador Intel Display Audio. |
| Post-Incidente | Cierre del caso en Stellar Cyber y registro en bitacora. |

---

## 📚 Playbooks Asignados
| ID | Nombre | Justificacion Estrategica |
| :--- | :--- | :--- |
| PB-EP-VULN-DRV | Gestion de Drivers Vulnerables y Mitigacion BYOVD | Protocolo para gestion de controladores en lista de bloqueo y actualizacion de firmware/drivers. |

---

## 🏷️ Resolution Tag para Stellar Cyber
**Tag:** `Mitigated` o `True Positive (Benign)`
**Descripcion:** Detección y bloqueo preventivo de versión vulnerable del controlador Intel Display Audio (`IntcDAud.sys`) por la directiva DRIVER_BLOCKLIST de Sophos Central.

---

## 📝 Datos para Bitacora de Excel (UNA SOLA LINEA EN TABLA)

| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Deteccion | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripcion | Evidencia (Logs, etc. Puede ser el mismo del Case Evidence ) | Solicitud de Accion | Estado | URL | Generacion de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-04 06:42 | Analista SOC Senior | CAJAANDE | Sophos_Blocked_Driver_IntcDAud_CJPPA20170828 | sophos_CAJA-ANDE-SOPHOS | N/A | Media | CoreBlockedDriverDetection | Bloqueo preventivo de driver vulnerable IntcDAud.sys en CJPPA20170828 | CJPPA20170828 (172.16.202.86 - MP5681371) | 2 alertas (1 original + 1 duplicado). Sophos Intercept X bloqueo la carga de C:\Windows\System32\drivers\IntcDAud.sys por coincidencia en DRIVER_BLOCKLIST (version obsoleta vulnerable a BYOVD). Bloqueo exitoso en runtime sin compromiso. | SHA256: 5c1135081e29d7f4a97d5caa2c8fbe1dd04ec7a3d8e648e69f2aa9ebdd88ebbb | Solicitar a Soporte TI de Caja Ande la actualizacion del paquete de drivers Intel Graphics/Audio en CJPPA20170828. | Cerrado | N/A | NO | N/A | PB-EP-VULN-DRV |

---

## 💻 Instruccion para Cierre Maestro en Stellar Cyber

**Estado:** Closed  
**Resolution Tag:** Mitigated  
**Comentario de Cierre:**  
> Caso analizado y mitigado. Sophos Central (Intercept X) bloqueó de manera preventiva y exitosa la carga en memoria del controlador `C:\Windows\System32\drivers\IntcDAud.sys` (SHA256: `5c1135081e29d7f4a97d5caa2c8fbe1dd04ec7a3d8e648e69f2aa9ebdd88ebbb`) en la estación `CJPPA20170828` debido a su inclusión en la lista de bloqueo (`DRIVER_BLOCKLIST`). El archivo corresponde al driver legítimo de Intel Display Audio, cuya versión instalada presenta vulnerabilidades conocidas explotables para elevación de privilegios (BYOVD). No existe evidencia de explotación activa ni compromiso. Se recomienda coordinar con el equipo de TI la actualización del driver a su última versión soportada.

---

## 🔬 Desglose Ultra Quirurgico
- **Capa Kernel / Driver:** Intento de registro o carga del servicio del kernel para el dispositivo de audio HDMI de Intel (`IntcDAud.sys`).
- **Capa EDR:** Sophos interceptó la llamada a nivel de Kernel mediante su driver de protección (`CoreBlockedDriverDetection`). Al verificar la firma y el hash contra la base de datos de controladores prohibidos/vulnerables (`DRIVER_BLOCKLIST`), denegó la carga.
- **Capa SIEM:** Stellar Cyber correlaciona el syslog de Sophos duplicando el registro y catalogándolo como `sophos_event-xdr_eba-xdr_endpoint_indicator_of_threat` con severidad Media (45).
- **Resumen Quirúrgico Final:** Mitigación preventiva transparente. El sistema operativo queda protegido contra potenciales ataques BYOVD, requiriendo únicamente el mantenimiento habitual de actualización de drivers por parte del equipo de TI.
