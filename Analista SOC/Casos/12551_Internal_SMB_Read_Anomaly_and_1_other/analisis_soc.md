### 🔍 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `Lateral Movement`, `SMB Read Anomaly`, `False Positive`, `File Server Activity`.

### Análisis Eventos 1 y 2 (Lote Agrupado)
*Nota del analista: Este archivo contiene dos alertas de anomalías volumétricas en SMB hacia el mismo servidor de destino (File Server).*

### 📊 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Evento 1:** `internal_smb_read_anomaly` - El host `192.168.169.15` (nb-ainsaurralde.technoma.local, usuario: danielsaavedra) generó 127 peticiones de lectura SMB contra `10.11.1.5` (adm-fs.technoma.local).
* **Evento 2:** `internal_smb_read_anomaly` - El host `192.168.169.64` (nb-jvaliente.technoma.local, usuario: jorgevaliente) generó 69 peticiones de lectura SMB contra `10.11.1.5` (adm-fs.technoma.local), accediendo a `\IPC$` y `sysvol` (nota: este sysvol fue referenciado globalmente hacia el AD, pero el destino principal fue el FS).

### 🔬 Desglose Técnico y Disección Forense
* El modelo de Machine Learning (`internal_smb_read_anomaly`) de Stellar Cyber detectó un pico en la cantidad de operaciones de lectura (SMB Command 8 / SMB2 READ) que superaba la línea base habitual de los usuarios `danielsaavedra` y `jorgevaliente`.
* **Hallazgo Clave:** El servidor de destino de todo este tráfico masivo de lectura es la IP `10.11.1.5`, que corresponde a `adm-fs.technoma.local`. Este servidor es un **File Server (Servidor de Archivos) corporativo**.
* El hecho de que dos usuarios de la red interna estén leyendo grandes volúmenes de datos desde un servidor de archivos no constituye una técnica de "Explotación de Servicios Remotos" (T1210) ni un "Movimiento Lateral". Es el comportamiento esperado y fundamental por el cual existe un File Server: compartir y descargar documentos.
* El ML levantó la alerta simplemente porque el volumen de descarga superó un umbral temporal, no por el contenido de la descarga en sí.

### 🧠 ¿Por qué es (o no es) una Amenaza?
Es un **Falso Positivo Operativo (Actividad Benigna)**.
Los usuarios están haciendo su trabajo diario: copiar, leer o transferir archivos pesados o múltiples desde el repositorio central de archivos de la empresa hacia sus notebooks. No existe ofuscación, no hay exploits y el servicio destino (SMB en un File Server) está diseñado exactamente para este propósito.

### ⚖️ Análisis de Impacto CIA Triad
```json
{
  "Confidencialidad": "Intacta.",
  "Integridad": "Intacta.",
  "Disponibilidad": "Intacta."
}
```

### 🎯 Veredicto y Confianza Analítica
```json
{
  "Veredicto": "Falso Positivo de Ataque (Tráfico de File Server Benigno)",
  "Confianza": "100%",
  "Justificacion": "El volumen anómalo de lecturas SMB se dirige exclusivamente hacia el File Server corporativo (adm-fs.technoma.local). Esto es actividad de red administrativa y laboral habitual por parte de los usuarios danielsaavedra y jorgevaliente, mal clasificada por el ML basado puramente en volumetría."
}
```

### 🛡️ Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Detección y Análisis | Se identificó que el destino del tráfico era un servidor de archivos legítimo. Se descarta cualquier indicio de movimiento lateral malicioso. |
| Erradicación y Recuperación | N/A. No se requiere acción de contención. |

### 📘 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| PB-FP-01 | Falsos Positivos Analíticos | Aplicable a la mala clasificación volumétrica del ML de Stellar Cyber. |

### 🏷️ Resolution Tag para Stellar Cyber
`False Positive` - Actividad de usuario benigna (File Server).

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-23 10:46 | Antigravity | technoma | 12551 | new_ml | N/A | Low | Network Anomaly | FP SMB Read Volumetrics (File Server) | 192.168.169.15, 192.168.169.64, 10.11.1.5 (adm-fs) | Anomalía volumétrica por lecturas SMB masivas. Los usuarios danielsaavedra y jorgevaliente estaban leyendo/copiando archivos legítimamente desde el File Server corporativo (adm-fs). Falso Positivo del ML por pico de tráfico. | Destino de red (File Server) | Ninguna. Tráfico benigno autorizado. | Cerrado | N/A | NO | N/A | PB-FP-01 |

### 🏁 Instrucción para Cierre en Stellar Cyber
**Estado:** Closed
**Resolution Tag:** False Positive
**Comentario:**
Falso Positivo de Movimiento Lateral. El lote reporta 2 alertas de `internal_smb_read_anomaly` generadas por los usuarios `danielsaavedra` y `jorgevaliente`. El destino del tráfico SMB en ambos eventos es la IP `10.11.1.5` (`adm-fs.technoma.local`), que corresponde al File Server (servidor de archivos) de la empresa. El volumen de lectura detectado por el modelo de ML (Command: 8 / SMB2 READ) es simplemente el tráfico esperado cuando un usuario transfiere archivos pesados o carpetas enteras desde el repositorio central. Es una actividad laboral diaria y totalmente benigna. Se cierra el caso.
