### 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `False Positive`, `Active Directory`, `Kerberos`, `Exchange HealthMailbox`, `Technical Debt`

### Análisis Evento 1

### 🎯 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Alerta Detectada:** Internal Credential Stuffing / Cloud Account Login Failure Anomaly
* **Activos Involucrados:** `172.16.201.4` (`VM-MARANDU`) -> `172.16.201.8` (`VMBASE8`)
* **Comportamiento Anómalo:** Múltiples fallos continuos de autenticación (Cientos de fallos por minuto con tasa de éxito 0%). El ML asume un ataque de fuerza bruta o Credential Stuffing.
* **Causalidad Probable:** Comportamiento documentado en la base de conocimientos. El servidor origen (`VM-MARANDU`) posee deuda técnica de Microsoft Exchange y está intentando autenticar cuentas sintéticas (`HealthMailbox...`) que ya no existen o están corruptas en el dominio `CAJAANDE.LOCAL`.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Fallos Acumulados | Tasa Fallo | Observación Forense |
|---|---|---|---|---|---|
| 2026-07-25T23:05:25 | 2026-07-25 20:05:25 | Internal Account Login Failure | 146 | 100% | Bucle de EventID 4768 (Kerberos) |
| 2026-07-25T23:09:26 | 2026-07-25 20:09:26 | Internal Credential Stuffing | N/A | 32.8 fail/min | Algoritmo detecta usuarios "desconocidos". |

### 🔬 Desglose Técnico y Disección Forense
* **Flujo de Tráfico:** Peticiones locales de Active Directory (Kerberos) originadas desde la IP `172.16.201.4` contra el Controlador de Dominio de CAJAANDE `VMBASE8`.
* **Identificador de Evento Windows:** `Event ID 4768` (A Kerberos authentication ticket (TGT) was requested).
* **Estado Kerberos:** `Status: 0x6` (Client not found in Kerberos database). Esto significa que el usuario directamente no existe en el Active Directory.

**Payload / Evidencia Principal:**
```json
{
  "payload_type": "Windows Security Event (4768)",
  "payload_value": "TargetUserName: HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
  "payload_status": "0x6",
  "payload_service": "krbtgt/CAJAANDE.LOCAL",
  "payload_origen": "VM-MARANDU (172.16.201.4)"
}
```

### 🧠 ¿Por qué es (o no es) una Amenaza?
**No es una amenaza (Falso Positivo de Deuda Técnica).** La memoria institucional del SOC (`SOC_GEM_v2.md`) tiene perfectamente mapeado este comportamiento. El servicio `Managed Availability` de Microsoft Exchange Server invoca validaciones cíclicas de estado utilizando cuentas sintéticas (`HealthMailboxes`). En el servidor `VM-MARANDU` ocurrió una falla, migración incompleta o borrado de dichas cuentas en el KDC, por lo que el agente local sigue ciegamente pidiendo tickets Kerberos para usuarios fantasma. Al ver que nadie se loguea exitosamente y hay cientos de fallos, el SIEM detona alertas críticas de Stuffing.

---

### Análisis Eventos 2 al 459

**Los 458 eventos restantes son la misma detonación cíclica del ML a lo largo del tiempo**. El motor de anomalías "Identity Detection" de Stellar Cyber agrupa los fallos de autenticación en buckets de 25 minutos. Cada vez que el bucket se llena con estos falsos positivos de Exchange (promediando de 146 a 150 intentos fallidos por intervalo con un anomaly score ponderado superior a 500), se genera un nuevo doc en el índice. Todos son idénticos y comparten la misma IP origen, IP destino y usuarios (HealthMailboxes).

---

### Cierre Maestro Unificado

### 🛡️ Análisis de Impacto CIA Triad
```json
{
  "Confidentiality": "Sin impacto.",
  "Integrity": "Sin impacto.",
  "Availability": "Bajo (Ruido en los logs de seguridad del DC VMBASE8)."
}
```

### ⚖️ Veredicto y Confianza Analítica
```json
{
  "Veredicto": "False Positive",
  "Confianza": "100%",
  "Motivo": "Comportamiento explícitamente documentado en la base de conocimientos SOC_GEM_v2.md como un falso positivo por deuda técnica de Exchange (Managed Availability)."
}
```

### 📉 Indicador de Fatiga de Alertas
```json
{
  "Fatiga": "Crítica",
  "Razón": "Se generaron 459 alertas en un corto período. Urge el tuning de la plataforma para suprimir este emparejamiento específico."
}
```

### 📘 Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
|---|---|
| Detección y Análisis | Correlación de IPs y nombres de usuario (`HealthMailbox`) contra la memoria institucional. |
| Erradicación y Recuperación | N/A (Problema de infraestructura IT, no de seguridad). |
| Actividad Post-Incidente | Requerir al equipo de infraestructura/sysadmins de CAJAANDE que reparen los HealthMailboxes o detengan el servicio en `VM-MARANDU`. |

### 📚 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
|---|---|---|
| PB-002 | Manejo de Falsos Positivos | Identificación de falsas alarmas generadas por componentes de software rotos (Exchange). |

### 🏷️ Resolution Tag para Stellar Cyber
`False Positive` - Misconfigured System / Technical Debt.

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
`26/07/2026 09:41 | Analista | technoma / CAJAANDE | 12647 | Stellar Cyber | - | Baja | Internal Credential Stuffing | Exchange HealthMailbox Kerberos failures | 172.16.201.4 | Falso Positivo masivo (459 eventos). El servidor VM-MARANDU sufre de deuda técnica (Managed Availability de Exchange) y solicita continuamente TGTs Kerberos al DC VMBASE8 para cuentas HealthMailbox purgadas (Status 0x6). Ya documentado en SOC_GEM_v2.md. | Winlogbeat (EventID 4768) | Escalar a IT Infraestructura | Cerrado | - | No | - | PB-002`

### 💻 Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario final:** Falso positivo masivo por deuda técnica, consolidando 459 eventos en un solo cierre. Tal como indica nuestra base de conocimientos, el servidor `VM-MARANDU` (172.16.201.4) tiene un problema con el componente Managed Availability de Microsoft Exchange, lo que ocasiona que intente autenticar cuentas sintéticas (`HealthMailbox`) que ya no existen en el dominio CAJAANDE.LOCAL contra el Controlador de Dominio `VMBASE8` (172.16.201.8). Kerberos responde constantemente "Client not found" (0x6), lo que el ML de Stellar interpreta erróneamente como Credential Stuffing. Escalar a IT para reparar el Exchange.

> [!CAUTION]
> Debido al inmenso volumen de ruido (459 alertas), es OBLIGATORIO configurar una regla de supresión (Tuning) en Stellar Cyber excluyendo al usuario `*HealthMailbox*` en el sensor interno, o aislar a la IP `172.16.201.4` de estas reglas de Login Failure hasta que el equipo de Infraestructura lo solucione.

### 🔬 Desglose Ultra Quirúrgico
* **Red/Enrutamiento:** Conexión directa entre hosts internos del segmento de servidores (172.16.201.x).
* **Transporte/Conexión:** Windows Event Forwarding. Los logs son capturados nativamente del Event Viewer (Security) del DC `VMBASE8` vía Auditbeat/Winlogbeat.
* **Aplicación/DPI:** Interacción con el KDC (Key Distribution Center). Peticiones de TGT (AS-REQ) rechazadas por Active Directory. 
* **Resumen Quirúrgico Final:** La IA detectó la firma perfecta de un ataque de fuerza bruta/stuffing (100% fallos, 0% éxito, usuarios desconocidos). La carencia de contexto de la máquina es lo que transforma la métrica en un FP. Los sistemas de monitoreo de Exchange (Active Manager / Managed Availability) están diseñados para ser ruidosos, y cuando se corrompen, este es el efecto secundario clásico sobre el SIEM.
