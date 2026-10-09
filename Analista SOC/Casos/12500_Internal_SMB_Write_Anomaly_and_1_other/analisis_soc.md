### 🔍 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `SMB_Anomaly`, `False Positive`, `Administrative Noise`, `GPO Sync`, `DCE/RPC`.

### Análisis Evento 1
### 📊 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Threat Name:** internal_smb_read_anomaly
* **Host IP (Origen):** `192.168.169.119` (`nb-noc2.technoma.local`)
* **Host IP (Destino):** `10.11.1.1` (`ad.technoma.local`)
* **Description:** In internal traffic, a host... has sent an anomalously large number (#: 94) of SMB read requests, compared to its typical number (#: 10), measured in a 5.0-minute interval. In this time interval, the source host accesses \\ad.technoma.local\IPC$, \\ad.technoma.local\SysVol very frequently.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-22T09:08:12.000Z | 2026-07-22 06:08:12 | SMB Read Anomaly | 94 reqs | 10 reqs | 9.4x | Lecturas hacia SysVol e IPC$ en el Controlador de Dominio. |

### 🔬 Desglose Técnico y Disección Forense
* El host `nb-noc2.technoma.local` (perteneciente al equipo de NOC) interactuó vía SMB (puerto 445) con el Controlador de Dominio `ad.technoma.local`.
* Se observó tráfico dirigido hacia los recursos compartidos administrativos `\SysVol` e `\IPC$`.
* Al analizar la telemetría metadata aplicando la **Piedra de Rosetta SMB**, observamos las siguientes operaciones legítimas de Windows:
  * Comando SMBv2 **3** (`SMB2 TREE_CONNECT`) mapeando la carpeta `\SysVol`.
  * Comando SMBv2 **5** (`SMB2 CREATE`) solicitando apertura/lectura sobre los archivos `technoma.local\Policies\{3F7D6B5B-761B-4B7D-9C9D-9D3E8E200B52}\gpt.ini` y `technoma.local\Policies\{8172E035-096F-4520-9BFF-42E70678B00F}\gpt.ini`.
  * Comando SMBv2 **8** (`SMB2 READ`) y **16** (`SMB2 QUERY_INFO`) para extraer atributos y contenido de las políticas.
* Este comportamiento corresponde exactamente al ciclo nativo de actualización de Políticas de Grupo (GPO) de Windows (Background Refresh).
**Payload / Evidencia Principal:**
```json
{
  "request": {
      "command": 11,
      "filename": "technoma.local\\Policies\\{3F7D6B5B-761B-4B7D-9C9D-9D3E8E200B52}\\gpt.ini",
      "version": 2
  }
}
```

### Análisis Evento 2
### 📊 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Threat Name:** internal_smb_anomaly (SMB Write Anomaly)
* **Host IP (Origen):** `192.168.169.119` (`nb-noc2.technoma.local`)
* **Host IP (Destino):** `10.11.1.1` (`ad.technoma.local`)
* **Description:** In internal traffic, a host... has sent an anomalously large number (#: 28) of SMB write requests, compared to its typical number (#: 4).

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-22T09:09:02.000Z | 2026-07-22 06:09:02 | SMB Write Anomaly | 28 reqs | 4 reqs | 7.0x | Escrituras en la tubería `lsarpc` sobre `\IPC$`. |

### 🔬 Desglose Técnico y Disección Forense
* Inmediatamente después de la lectura de GPO, el mismo host realizó 28 solicitudes de escritura SMB hacia el DC.
* Al traducir la telemetría, se observa:
  * Comando SMBv2 **3** (`SMB2 TREE_CONNECT`) mapeando `\IPC$`.
  * Comando SMBv2 **5** (`SMB2 CREATE`) abriendo el archivo/tubería `lsarpc` (Local Security Authority Remote Procedure Call).
  * Comando SMBv2 **9** (`SMB2 WRITE`) inyectando datos en la tubería nombrada.
* Escribir en `lsarpc` sobre `\IPC$` es la forma nativa y estándar en que un cliente de Windows ejecuta consultas DCE/RPC hacia el dominio (ej. autenticaciones, consultas de SIDs, resolución de nombres, o aplicación de las políticas descargadas previamente).
* El volumen de peticiones (28) es ínfimo y completamente consistente con una sincronización administrativa. La alerta se disparó únicamente porque el "Typical" histórico de la máquina era muy bajo (4), provocando un desvío estadístico matemático, pero no semántico.

### 🧠 ¿Por qué es (o no es) una Amenaza?
Es un **Falso Positivo de ciberataque**. Se trata de tráfico benigno nativo de infraestructura Microsoft (Windows RPC y GPO sync). La máquina de origen pertenece a IT/NOC y está realizando rutinas de mantenimiento e interrogación del directorio activo. Stellar Cyber marcó el comportamiento como "Movimiento Lateral (TA0008)" simplemente por el incremento estadístico en el uso de SMB, sin evaluar el contexto de los comandos RPC y las carpetas accedidas (`\SysVol` para GPO, `lsarpc` para RPC auth).

### ⚖️ Análisis de Impacto CIA Triad
```json
{
  "Confidencialidad": "Intacta. Tráfico legítimo de red interna.",
  "Integridad": "Intacta. No hay alteración no autorizada de datos.",
  "Disponibilidad": "Intacta. El volumen de 94/28 paquetes no representa denegación de servicio (DoS) para el Controlador de Dominio."
}
```

### 🎯 Veredicto y Confianza Analítica
```json
{
  "Veredicto": "Falso Positivo (Ruido Administrativo / Tráfico Windows Nativo)",
  "Confianza": "100%",
  "Justificacion": "Los comandos SMB (Lecturas a \\SysVol\\...\\gpt.ini y Escrituras a \\IPC$\\lsarpc) son operaciones core de sincronización de dominio y DCE/RPC, sin indicadores de explotación."
}
```

### 🥱 Indicador de Fatiga de Alertas
```json
{
  "Fatiga": "Media",
  "Motivo": "La dependencia de Stellar Cyber en umbrales matemáticos bajos (ej. salto de 4 a 28 paquetes) genera falsos positivos constantes en ambientes de dominio ruidosos."
}
```

### 🛡️ Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Preparation | Afinar la política de Machine Learning en Stellar Cyber para tolerar picos de tráfico SMB hacia `ad.technoma.local` desde subredes administrativas (VLAN 1101). |

### 📘 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| PB-TUNE-01 | Afinado de Reglas ML | Modificación de umbrales estadísticos para conexiones internas conocidas hacia el Domain Controller. |

### 🏷️ Resolution Tag para Stellar Cyber
`False Positive` - Tráfico benigno de infraestructura administrativa.

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-22 09:08 | Antigravity | technoma | 12500 | new_ml | N/A | Low | smb_anomaly | Falso Positivo SMB Anomaly (Read/Write) | nb-noc2.technoma.local, ad.technoma.local | Tráfico nativo de GPO y DCE/RPC (SysVol/lsarpc) alertado por desviación estadística. | Metadata SMB | Ninguna. Afinar ML | Cerrado | N/A | NO | N/A | PB-TUNE-01 |

### 🏁 Instrucción para Cierre en Stellar Cyber
**Estado:** Closed
**Resolution Tag:** False Positive
**Comentario:**
Falso Positivo de Ataque. La alerta fue disparada por el motor de Machine Learning debido a un leve salto estadístico en las peticiones SMB (de 4 a 28, y de 10 a 94). Al aplicar la traducción de comandos (SMB Rosetta Stone), se confirma que el host administrativo `nb-noc2.technoma.local` estaba ejecutando un ciclo nativo de background refresh del dominio contra el DC (`ad.technoma.local`). El Evento 1 corresponde a descargas legítimas de archivos de configuración de políticas grupales (Comandos SMB2 CREATE/READ hacia `\SysVol\...\gpt.ini`), y el Evento 2 es la típica comunicación DCE/RPC ejecutada por debajo de SMB (Comandos SMB2 CREATE/WRITE apuntando al named pipe `lsarpc` sobre la compartición `\IPC$`). No hay indicadores de compromiso (IoC) ni de movimiento lateral malicioso (TA0008). Se cierra sin impacto.
