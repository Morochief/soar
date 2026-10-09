### 📘 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `Exchange` `HealthMailbox` `Falso Positivo` `T1110` `Event 4768`

### 📝 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
*   **Origen:** El host interno `VMBASE8` (`172.16.201.8` y `172.16.201.4`).
*   **Destino:** Controlador de Dominio de `CAJAANDE.LOCAL` (Kerberos Service).
*   **Vector/Técnica:** Táctica de Acceso a Credenciales (`TA0006`) y técnica de Fuerza Bruta (`T1110`).
*   **Identidades Involucradas:** `HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py` (y similares).

### ⏱️ Línea de Tiempo Temporal
*Debido a la magnitud de los eventos (Lote de 49 alertas consolidadas), se resumen los hallazgos en un cierre maestro unificado conforme a la Regla 10 del Equipo SOC.*
| Hora (UTC) | Evento Detectado | Observación Forense |
| :--- | :--- | :--- |
| 10:29 - 10:37 | `internal_user_login_fail` / `credential_stuffing` | Múltiples eventos continuos de Error 4768 (Status 0x6) hacia el DC de CAJAANDE.LOCAL originados por VMBASE8. |

### 🔍 Desglose Técnico y Disección Forense

#### Análisis Unificado de Lote (49 Eventos)
*   **Evento:** Múltiples alertas de "Internal Credential Stuffing" e "Internal User Login Failure Anomaly" disparadas por el motor de Machine Learning de Stellar Cyber debido a una alta tasa de fallos por minuto (ej. 32.60 fallos/min).
*   **Forense:** Analizando los metadatos de los 49 registros (Event ID 4768), todos y cada uno de ellos corresponden a solicitudes de ticket TGT de Kerberos (`Task: Kerberos Authentication Service`) que resultan en el código de error `Status: 0x6` (Client not found in Kerberos database).
*   **Contexto Crítico:** El nombre de usuario en todos los eventos sigue el patrón `HealthMailbox<hash>@cajaande.gov.py`. Estas son cuentas sintéticas generadas y utilizadas automáticamente por el servicio "Managed Availability" de Microsoft Exchange Server para monitorear el estado de las bases de datos (Active Monitoring).

**Payload / Evidencia Principal:**
```json
{
  "event_id": 4768,
  "TargetUserName": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
  "ServiceName": "krbtgt/CAJAANDE.LOCAL",
  "Status": "0x6",
  "login_failure_rate": "32.60"
}
```

**Hipótesis Formuladas:**
| Hipótesis | Probabilidad | Justificación |
| :--- | :--- | :--- |
| Ataque de Fuerza Bruta / Credential Stuffing | Nula | Los atacantes no realizan fuerza bruta contra cuentas de monitoreo de Exchange auto-generadas (`HealthMailbox`). Además, un atacante no dispararía errores 0x6 constantes si estuviera probando diccionarios de usuarios válidos. |
| Ruido Administrativo (Deuda Técnica Exchange) | 100% | Patrón exacto documentado en la Memoria Institucional SOC. Las cuentas HealthMailbox a menudo son eliminadas y recreadas por el sistema, y mientras el caché de Active Directory se sincroniza o si quedan huérfanas, los sondeos periódicos generarán avalanchas de errores `0x6`. |

### ❓ ¿Por qué es (o no es) una Amenaza?
**No es una amenaza (Falso Positivo puro).** 
Stellar Cyber ve un volumen alto de fallos de inicio de sesión (`user_login_fail` rate alto) y dispara la regla `internal_credential_stuffing`. Sin embargo, es un proceso legítimo de Microsoft Exchange (Managed Availability Probe) comportándose de manera ineficiente y ruidosa debido a cuentas huérfanas.

### 🔐 Análisis de Impacto CIA Triad
```json
{
  "Confidentiality": "Sin impacto.",
  "Integrity": "Sin impacto. Autenticación rechazada por el DC (Status 0x6).",
  "Availability": "Sin impacto significativo. Generación de ruido en los logs de seguridad de Windows."
}
```

### 🎯 Veredicto y Confianza Analítica
```json
{
  "Veredicto": "False Positive",
  "Confianza": "100%",
  "Motivo": "Identificación positiva de cuentas HealthMailbox de Exchange. Comportamiento benigno documentado."
}
```

### ⚠️ Indicador de Fatiga de Alertas
```json
{
  "Nivel_Fatiga": "Alto",
  "Recomendacion_Afinamiento": "Se recomienda aplicar una regla de exclusión en Stellar Cyber para suprimir las alertas de fuerza bruta o login_fail donde el `username` contenga la cadena `HealthMailbox` y el `event_id` sea `4768` o `4771`."
}
```

### 🔄 Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Análisis y Detección | Identificación de ruido administrativo por sondas de Exchange. |
| Erradicación | Cierre del lote completo de 49 alertas bajo un único análisis (Regla 10). |

### 🧪 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| PL-10 | Ruido Administrativo de Exchange (HealthMailbox) | Plantilla 10 aplicada por coincidencia exacta de indicadores. |

### 📋 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc.) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-16 | Analista SOC | Technoma/CAJAANDE | 12245 | MS Windows / Interflow | - | Baja | `internal_credential_stuffing` | Internal Credential Stuffing and 48 others | `VMBASE8` (172.16.201.4/8) | LOTE UNIFICADO 49 ALERTAS: Falsos positivos de fuerza bruta generados por cuentas de monitoreo HealthMailbox de Exchange (Error 4768 / 0x6). | TargetUser: HealthMailbox... | Cerrar lote completo como FP. Configurar filtro de supresión. | Cerrado | - | No | - | Ruido Administrativo de Exchange |

### ✅ Instrucción para Cierre Maestro en Stellar Cyber
*   **Estado:** Closed
*   **Resolution Tag:** False Positive
*   **Comentario Maestro (Cubre las 49 alertas):** 
> "Alerta descartada como falso positivo de acuerdo con la memoria institucional SOC. Los fallos masivos de autenticación (Event 4768, Status 0x6) intentan validar cuentas sintéticas 'HealthMailbox' de Microsoft Exchange que ya no existen en el dominio local. Esto obedece a un proceso residual de 'Managed Availability' (deuda técnica). No representa riesgo de fuerza bruta ni de seguridad. Se recomienda aplicar regla de supresión para este origen."
