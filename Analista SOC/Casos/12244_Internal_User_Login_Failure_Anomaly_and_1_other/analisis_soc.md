### 📘 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `Windows` `Kerberos` `T1110` `ActiveDirectory` `HealthMailbox`

### 📝 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
*   **Origen:** El host interno `VM-MARANDU` (`172.16.201.4`) está registrando picos anómalos de fallos de autenticación (168 intentos).
*   **Destino:** Las validaciones Kerberos apuntan al Controlador de Dominio secundario `VMBASE8` (`172.16.201.8`).
*   **Vector/Técnica:** Táctica de Acceso a Credenciales (`TA0006`) a través de fuerza bruta potencial (`T1110`), evento originado por el servicio Kerberos (`EventID 4768`).
*   **Identidades Involucradas:** La cuenta origen de la anomalía es un buzón de monitoreo residual de Exchange: `HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py` (Usuario no hallado en el inventario oficial de AD de Technoma/CajaAnde).

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 09:46:41 | 05:46:41 | `internal_user_login_fail` | 168 | 0 | 1 | Evento 1: Fallo masivo en ventana de 5 mins. |
| 09:46:41 | 05:46:41 | `internal_user_login_fail` | 168 | 0 | 1 | Evento 2: Registro concurrente reportado por el sensor (Duplicado del comportamiento). |

### 🔍 Desglose Técnico y Disección Forense

#### Análisis Evento 1
*   **Evento:** Fallo de Autenticación Kerberos (TGT Request).
*   **Forense:** El sistema `VM-MARANDU` intenta solicitar un Ticket Granting Ticket (TGT) para una cuenta que el KDC (`VMBASE8`) no reconoce (`Status 0x6`).

#### Análisis Evento 2
*   **Evento:** Fallo de Autenticación Kerberos (TGT Request).
*   **Forense:** Evento 2 es un duplicado exacto del Evento 1 (misma marca de tiempo base `1784195201795`, diferente bucket de evaluación de ML `accumulated_anomalous_failures: 1133`), generado por la agregación de la plataforma XDR.

**Payload / Evidencia Principal:**
```json
{
  "payload_type": "Kerberos TGT Request",
  "payload_value": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
  "payload_hash": "N/A",
  "payload_firma": "N/A",
  "payload_accion": "TGT Request Failed (0x6 - KDC_ERR_C_PRINCIPAL_UNKNOWN)",
  "payload_destino": "krbtgt/CAJAANDE.LOCAL"
}
```

**Comandos de Diagnóstico Recomendados (Live Response en VM-MARANDU):**
```powershell
Get-EventLog -LogName Security -InstanceId 4768 -Newest 10 | Where-Object {$_.Message -match "HealthMailbox"}
```

**Hipótesis Formuladas:**
| Hipótesis | Probabilidad | Justificación |
| :--- | :--- | :--- |
| Fuerza Bruta Interna | Baja | Una fuerza bruta utilizaría diccionarios de usuarios reales o secuencias numéricas, no hashes hexadecimales fijos atados a "HealthMailbox". Además, el `Status 0x6` indica que el usuario no existe, no un fallo de contraseña (`0x18`). |
| Ruido Administrativo / Deuda Técnica | Muy Alta | La memoria institucional confirma que `VM-MARANDU` posee un Exchange mal desinstalado o mal migrado que sigue ejecutando sondeadores cíclicos de salud (Managed Availability) usando buzones sintéticos huérfanos. |

### ❓ ¿Por qué es (o no es) una Amenaza?
**No es una amenaza (Falso Positivo Estructural).** 
Como mentor, te explico el comportamiento: El servicio de "Managed Availability" de Microsoft Exchange crea decenas de cuentas invisibles llamadas "HealthMailboxes" para probar la salud de las bases de datos enviándose correos a sí mismo de manera continua. Cuando un servidor Exchange es migrado o desmantelado incorrectamente, el servicio de diagnóstico puede seguir corriendo en el servidor antiguo, intentando validar buzones en el Active Directory que ya fueron purgados, generando ráfagas de errores Kerberos `0x6` contra el KDC. Esto es deuda técnica, no actividad maliciosa.

### 🔐 Análisis de Impacto CIA Triad
```json
{
  "Confidentiality": "Sin impacto. Las credenciales no se comprometieron, la cuenta no existe.",
  "Integrity": "Sin impacto. No hubo modificación de datos ni evasión de controles.",
  "Availability": "Impacto nulo/muy bajo. Solo generación de ruido en los logs del AD que consume un mínimo espacio de almacenamiento."
}
```

### 🎯 Veredicto y Confianza Analítica
```json
{
  "Veredicto": "False Positive",
  "Confianza": "100%",
  "Motivo": "Comportamiento documentado en la Memoria Institucional de SOC_GEM_v2.md, característico de Exchange HealthMailbox."
}
```

### ⚠️ Indicador de Fatiga de Alertas
```json
{
  "Nivel_Fatiga": "Alto",
  "Recomendacion_Afinamiento": "Se debe generar un filtro de supresión estricto en Stellar Cyber (Rule: Mute) que suprima eventos 'internal_user_login_fail' cuyo 'srcip' sea 172.16.201.4 y el 'username' empiece con 'HealthMailbox'."
}
```

### 🔄 Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Análisis y Detección | Correlación del patrón de autenticación contra la base de conocimientos SOC. |
| Post-Incidente | Documentar la necesidad de supresión y reportar a Ingeniería la deuda técnica en VM-MARANDU. |

### 🧪 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| PB-02 | Falso Positivo / Ruido Administrativo | Clasificación directa basada en las directrices del SOC GEM v2 y ausencia de compromiso real. |

### 🏷️ Resolution Tag para Stellar Cyber
*   **Tag:** `Benign`
*   **Descripción:** Actividad administrativa o residual de la plataforma.

### 📋 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc.) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-16 | Analista SOC | Technoma/CajaAnde | 12244 | Interflow / Elastic | - | Baja | `internal_user_login_fail` | Internal User Login Failure Anomaly | `VM-MARANDU` (172.16.201.4) | Anomalía detectada (168 intentos) de autenticación fallida Kerberos por parte de un HealthMailbox de Exchange residual. | Logs Kerberos Event 4768 Status 0x6 | Cerrar caso en Stellar y recomendar supresión. | Cerrado | - | No | - | Falso Positivo / Ruido Administrativo |

### ✅ Instrucción para Cierre en Stellar Cyber
*   **Estado:** Closed
*   **Resolution Tag:** Benign
*   **Comentario:** 
> "Alerta descartada como falso positivo de acuerdo con la memoria institucional SOC. Los fallos masivos de autenticación (Event 4768, Status 0x6) provienen del host interno VM-MARANDU e intentan validar cuentas sintéticas 'HealthMailbox' de Microsoft Exchange que ya no existen en el dominio local. Esto obedece a un proceso residual de 'Managed Availability' (deuda técnica). No representa riesgo de fuerza bruta ni de seguridad. Se recomienda aplicar regla de supresión para este origen."

> [!TIP]
> **Actualización de Memoria:** Este patrón exacto ya se encuentra validado en `SOC_GEM_v2.md`. Sin embargo, dado que el archivo `plantillas_cierre_soc.md` no existe actualmente en el workspace, sugiero que aprovechemos la oportunidad para crearlo y añadir esta plantilla de cierre para futuros turnos.

### 🔬 Desglose Ultra Quirúrgico
*   **Red/Enrutamiento:** Conexión interna dentro del bloque `/16`, desde `172.16.201.4` (VM-MARANDU) hacia el KDC en `172.16.201.8` (VMBASE8).
*   **Transporte/Conexión:** Puertos dinámicos TCP (ej. `30246` en un evento) hacia el puerto 88 (Kerberos).
*   **Aplicación/DPI:** Protocolo Kerberos. `event_id: 4768` (TGT Request).
*   **Metadatos Específicos:** 
    *   `Status: 0x6`: Clave absoluta de la disección. Significa KDC_ERR_C_PRINCIPAL_UNKNOWN (el KDC afirma que la cuenta solicitada no existe en la base de datos).
    *   `TargetUserName: HealthMailbox0ab06aa...`: Denota cuentas de sistema generadas por MS Exchange Managed Availability, no usuarios humanos.
*   **Motor ML:** El motor generó un `weighted_anomaly_score` superior a 1100, gatillando la alerta de "Internal User Login Failure Anomaly" (severidad 60) debido al alto volumen (`168` fallos) y un ratio de fallo del `100%`. El motor XDR no comprende el contexto de que un Exchange antiguo está actuando de forma errática.

**Resumen Quirúrgico Final:**
El flujo es estrictamente transaccional administrativo. Un servicio remanente de diagnóstico de Exchange en VM-MARANDU envía peticiones TGT continuas al Active Directory consultando por cuentas sintéticas (HealthMailbox) que fueron eliminadas del bosque en alguna migración anterior. El KDC responde un error estándar (0x6), y el sensor Winlogbeat captura la auditoría de seguridad 4768, enviándola a Stellar Cyber. El motor de ML observa la alta cadencia de errores de login y la clasifica genéricamente como un ataque de fuerza bruta. La firma es inofensiva y puramente relacionada a deuda técnica de infraestructura.
