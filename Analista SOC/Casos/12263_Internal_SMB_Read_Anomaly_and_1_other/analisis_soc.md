### Analisis en Profundidad (Estilo Mentor DFIR)
**Tags:** Network Traffic Analysis, SMB Read, Lateral Movement

---

### Analisis Evento 1
**ID:** 89e00d79...
**Alerta:** Internal SMB Read Anomaly (internal_smb_read_anomaly)

#### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
- **Origen:** El host `nb-alovera.technoma.local` (`192.168.169.96`).
- **Usuario Identificado:** `angelicalovera` (Usuario de dominio válido según inventario).
- **Destino:** `10.11.1.5` (`adm-fs.technoma.local`).
- **Contexto:** Se detectaron 135 lecturas SMB en un periodo de 5 minutos, cuando la línea base esperada (typical) para este host era de 13 lecturas.
- **Accion requerida:** Confirmar si el tráfico es exploración maliciosa de compartidos, extracción de datos o actividad benigna hacia el File Server corporativo.

#### Linea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Ratio | Observacion Forense |
|---|---|---|---|---|---|---|
| 2026-07-16 14:45:24 | 2026-07-16 11:45:24 | smb_read_anomaly | 135 Lecturas | 13 Lecturas | ~10x | Conexiones hacia el servidor de archivos `adm-fs`. |

#### Desglose Tecnico y Diseccion Forense
- La máquina origen negocia sesiones SMB (puerto 445) con el servidor central de archivos `adm-fs.technoma.local`.
- El incremento volumétrico de 135 operaciones de lectura (NT_STATUS_SUCCESS `0` en la mayoría de transacciones) indica el copiado o lectura de múltiples archivos, o el acceso a un directorio con gran cantidad de subelementos.
- `adm-fs` es la infraestructura principal de almacenamiento para áreas como Administración, Contabilidad y Recursos Humanos. La interacción volumétrica hacia él no es una anomalía de seguridad, sino una actividad operativa inherente a su rol.

**Payload / Evidencia Principal:**
```json
{
  "payload_type": "SMB Protocol Metadata",
  "payload_value": "Command 8 (SMB2 Read)",
  "payload_accion": "File System Read",
  "payload_destino": "10.11.1.5"
}
```

**Diagnostico e Hipotesis:**
| Hipotesis Formulada | Resultado de Evaluacion |
|---|---|
| Movimiento Lateral / Ransomware Encryption | Descartado. No hay indicadores de cifrado, ni escritura masiva (SMB Write Anomaly). Las conexiones son lecturas locales. |
| Operación de File Server (Uso Normal) | Confirmado. El usuario `angelicalovera` tiene acceso válido y realiza lecturas estándar sobre el servidor `adm-fs`. |

#### Por que es (o no es) una Amenaza?
No es una amenaza. El motor ML alerta basándose únicamente en una desviación temporal del baseline del usuario (pasó de 13 a 135). Cualquier usuario que decida descargar una carpeta con docenas de documentos, o realizar una búsqueda en el explorador de Windows sobre un disco mapeado, generará este tipo de pico benigno de lectura.

---

### Analisis Evento 2
**ID:** c86a71a9...
**Alerta:** Internal SMB Read Anomaly (internal_smb_read_anomaly)

#### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
- **Origen:** El host `nb-alovera.technoma.local` (`192.168.169.96`).
- **Destino:** `10.11.1.5` (`adm-fs.technoma.local`).
- **Contexto:** 178 lecturas SMB en 5 minutos. El metadato adicional de Stellar revela acceso a los shares `\\10.11.1.5\IPC$` y `\\ad.technoma.local\SysVol`.
- **Accion requerida:** Evaluar el acceso concurrente a recursos IPC$ y de dominio.

#### Linea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Ratio | Observacion Forense |
|---|---|---|---|---|---|---|
| 2026-07-16 14:56:34 | 2026-07-16 11:56:34 | smb_read_anomaly | 178 Lecturas | 13 Lecturas | ~13x | Acceso a `\IPC$` y `\SysVol`. |

#### Desglose Tecnico y Diseccion Forense
- A la par de la actividad en el File Server, el sensor capta operaciones de lectura a los recursos administrativos de Active Directory (`\SysVol` y `\IPC$`).
- La lectura de `\SysVol` es un comportamiento mecánico de todos los sistemas Windows para aplicar y refrescar las Group Policy Objects (GPO - gpupdate).
- El error `nt_status: -1073741412` (STATUS_OBJECT_NAME_NOT_FOUND) observado en el comando 11 es típico cuando el sistema operativo consulta configuraciones de GPO inexistentes o no aplicables en el directorio de red.

**Diagnostico e Hipotesis:**
| Hipotesis Formulada | Resultado de Evaluacion |
|---|---|
| BloodHound / Sharphound AD Enum | Descartado. No hay enumeración masiva de LSA, SAM o endpoints en el dominio. |
| Group Policy Sync / Tráfico Base SMB | Confirmado. La validación de `\SysVol` es tráfico perimetral benigno de Windows (Background Refresh). |

#### Por que es (o no es) una Amenaza?
Es un comportamiento estándar. Windows actualiza políticas en segundo plano accediendo al recurso SysVol. Esta acción, superpuesta en el tiempo con la lectura al `adm-fs`, elevó aún más el contador de lecturas (178), reconfirmando la desviación de la línea base pero sin cruzar el umbral del riesgo de seguridad.

---

### CIERRE MAESTRO UNIFICADO

#### Analisis de Impacto CIA Triad
```json
{
  "Confidencialidad": "Intacta. La lectura de archivos en el File Server fue ejecutada por el propio usuario del equipo con sus credenciales autorizadas.",
  "Integridad": "Ninguna.",
  "Disponibilidad": "Ninguna."
}
```

#### Veredicto y Confianza Analitica
```json
{
  "Veredicto": "Falso Positivo",
  "Confianza": "Alta",
  "Justificacion": "Uso nativo de File Server corporativo y sincronización automática de Políticas de Dominio."
}
```

#### Indicador de Fatiga de Alertas
```json
{
  "Clasificacion": "Ruido Operacional / Administrativo",
  "Recomendacion": "Ninguna requerida de forma urgente, el ML se reajustará al nuevo baseline. Sin embargo, puede aplicar la plantilla 5 y 8 combinada para el cierre."
}
```

#### Fase del Ciclo NIST 800-61
| Fase NIST | Accion Tecnica |
|---|---|
| Preparacion | ML entrenado para calcular baselines de volumetría SMB de 5 min. |
| Deteccion y Analisis | Análisis de transacciones de lectura SMB que confirman la ausencia de cifrado o volcado de SAM. Cruce exitoso con Active Directory de la usuaria `angelicalovera`. |
| Contencion | No requerida. |
| Erradicacion | No requerida. |
| Recuperacion | No requerida. |
| Actividades Post-Incidente | Cierre del ticket con notas detalladas de comportamiento benigno mixto. |

#### Playbook Asignado
| ID | Nombre | Justificacion Estrategica |
|---|---|---|
| PB-001 | Falso Positivo / Ruido | Tráfico correspondiente a uso cotidiano de red empresarial. |

#### Resolution Tag para Stellar Cyber
- **Etiqueta:** False Positive
- **Descripcion:** Actividad legítima de lectura hacia File Server y actualización de Políticas (GPO).

#### Datos para Bitacora de Excel (UNA SOLA LINEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Deteccion | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripcion | Evidencia | Solicitud de Accion | Estado | URL | Generacion de Ticket | TICKET | Playbook |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 16/07/2026 14:45 | Antigravity | technoma | 12263 | Stellar Cyber | N/A | 34 | Internal SMB Read Anomaly | Falso Positivo - Acceso File Server y GPO | nb-alovera.technoma.local | El equipo de A. Lovera generó picos de lecturas SMB a la IP de adm-fs y resolvió políticas de SysVol. Comportamiento administrativo normal de la red. | Log TCP/SMB | Ninguna | Cerrado | N/A | No | N/A | PB-001 |

#### Instruccion para Cierre en Stellar Cyber
**Estado:** Closed
**Resolution Tag:** False Positive
**Comentario final:**
Alerta descartada como Falso Positivo. El análisis de metadatos SMB y las trazas de red confirman un comportamiento mixto totalmente benigno y correspondiente a infraestructura Active Directory. Por un lado, la usuaria (angelicalovera) generó picos de interacción de lectura de archivos locales hacia el servidor central `adm-fs` que superaron su línea base temporal (baseline ML). Por otro lado, el equipo actualizó políticas de grupo interactuando con los recursos administrativos (`\SysVol`, `\IPC$`). No hay indicadores de recolección maliciosa de información (BloodHound) ni de exfiltración lateral. Se cierra sin acción.
