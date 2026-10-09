# Reporte de Análisis SOC: Internal SMB Anomaly & Internal SMB Read Anomaly

- **Fecha y Hora del Análisis:** 2026-09-06
- **Analista / Rol:** Mentor SOC Senior (DFIR)
- **Cliente:** Technoma (`technoma.local`)
- **Host Origen:** `192.168.169.8` (`nb-jrivarola.technoma.local`, VLAN 1101)
- **Host Destino:** `10.11.1.1:445` (`ad.technoma.local`, Controlador de Dominio)
- **Veredicto General:** Falso Positivo (Actividad administrativa y operacional benigna)

---

## 1. Resumen Ejecutivo
Se analizaron dos alertas de Interflow correlacionadas por Machine Learning (`new_ml`) en Stellar Cyber:
1. `internal_smb_read_anomaly` (Event Score 34, Sev 20): Registro de 73 lecturas SMB.
2. `internal_smb_anomaly` (Event Score 47, Sev 40): Registro de 17 escrituras SMB sobre tuberías nombradas.

La inspección forense a nivel de protocolo confirma que ambas alertas corresponden a un ciclo estándar y sincronizado de actualización de políticas de grupo (Group Policy Client / `gpsvc`) y resolución de identificadores de seguridad (LSA Lookup) entre un endpoint corporativo autenticado y el Controlador de Dominio primario de la organización.

---

## 2. Hallazgos Forenses por Evento

### Evento 1: `internal_smb_read_anomaly` (`SysVol` / `gpt.ini`)
- **Acción:** Peticiones de lectura SMB2.
- **Recursos Involucrados:**
  - `\\ad.technoma.local\SysVol`
  - `technoma.local\Policies\{3F7D6B5B-761B-4B7D-9C9D-9D3E8E200B52}\gpt.ini`
  - `technoma.local\Policies\{8172E035-096F-4520-9BFF-42E70678B00F}\gpt.ini`
- **Comandos SMB2 Observados:**
  - `SMB2_COMMAND_TREE_CONNECT` (Comando 3): Conexión al recurso compartido `SysVol`.
  - `SMB2_COMMAND_CREATE` (Comando 5): Apertura de los descriptores de archivo `gpt.ini`.
  - `SMB2_COMMAND_READ` (Comando 8): Lectura del archivo de versión y estado de cada GPO.
  - `SMB2_COMMAND_CLOSE` (Comando 16): Cierre ordenado de los handles.
- **Conclusión Técnica:** Comportamiento idéntico al proceso `gpsvc.dll` leyendo directivas de dominio en background. Coincide con la memoria institucional de falsos positivos recurrentes de Technoma.

### Evento 2: `internal_smb_anomaly` (`IPC$` / `lsarpc`)
- **Acción:** Escritura/transmisión de datos sobre tubería nombrada.
- **Recursos Involucrados:**
  - `\\ad.technoma.local\IPC$`
  - Named pipe: `lsarpc`
- **Comandos SMB2 Observados:**
  - `SMB2_COMMAND_CREATE` (Comando 5): Establecimiento del canal RPC hacia `lsarpc`.
  - `SMB2_COMMAND_WRITE` (Comando 9): Emisión de payloads de solicitud RPC (LsaLookupNames / LsaLookupSids).
  - `SMB2_COMMAND_READ` (Comando 8): Recepción de las respuestas RPC del DC.
- **Conclusión Técnica:** Stellar Cyber clasifica las llamadas RPC encapsuladas sobre SMB Named Pipes como "SMB Writes" debido a la utilización del comando `SMB2_COMMAND_WRITE`. Se trata de una comunicación nativa de Windows para validar permisos, identidades y tokens de seguridad.

---

## 3. Evaluación de la Tríada CIA y Marco NIST SP 800-61 Rev. 2
- **Confidencialidad:** No comprometida. Tráfico autenticado mediante Kerberos/SMB2 en red local.
- **Integridad:** No comprometida. No hubo modificación de archivos ni alteración de configuraciones.
- **Disponibilidad:** No comprometida. Tráfico regular sin afectación de servicios ni consumo anómalo de recursos.
- **Fase NIST:** Detección y Análisis completada. No requiere Contención, Erradicación ni Recuperación.

---

## 4. Registro Unificado para Bitácora Excel

| Fecha Alerta | ID Alerta / Caso | Cliente | Severidad | IP Origen | Hostname Origen | IP Destino | Hostname Destino | Puerto / Protocolo | Tipo de Evento / Alerta | Clasificación | Causa Raíz / Justificación | Acción Tomada | Estado | Ticket Externo | Analista | Observaciones | Fecha Cierre |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-06 | GN5ZdKABI3UnQyDOD-iX / UM8dcqABI3UnQyDOVNka | Technoma | Baja (20-40) | 192.168.169.8 | nb-jrivarola.technoma.local | 10.11.1.1 | ad.technoma.local | 445/TCP (SMB) | internal_smb_read_anomaly / internal_smb_anomaly | Falso Positivo | Sincronización estándar de GPO (SysVol) y consultas RPC de identidades (lsarpc). | Validación forense de comandos SMB2 y cruce con memoria institucional. | Cerrado | N/A | Mentor SOC | Actividad administrativa legítima recurrente de Windows en dominio. | 2026-09-06 |

---

## 5. Plantilla de Comentario de Cierre Maestro para Stellar Cyber

```text
[SOC VERDICT] - FALSE POSITIVE / NO ACTION REQUIRED

- Incidente/Lote: Internal SMB Read Anomaly & Internal SMB Anomaly (Lote Unificado)
- Host Evaluado: 192.168.169.8 (nb-jrivarola.technoma.local) -> 10.11.1.1:445 (ad.technoma.local)
- IDs de Anomalía: GN5ZdKABI3UnQyDOD-iX / UM8dcqABI3UnQyDOVNka
- Análisis Técnico:
  1. Lectura SMB (SysVol): Tráfico legítimo correspondiente a la comprobación periódica de directivas de grupo (GPO) procesando archivos 'gpt.ini' bajo las directivas {3F7D6B5B-761B-4B7D-9C9D-9D3E8E200B52} y {8172E035-096F-4520-9BFF-42E70678B00F}.
  2. Escritura SMB (IPC$/lsarpc): Intercambio legítimo de llamadas RPC encapsuladas sobre la tubería 'lsarpc' para resolución de SIDs y membresía de grupos en el Active Directory.
  3. No se detectaron patrones de propagación lateral, intentos de acceso a recursos no autorizados ni volcado malicioso de credenciales. Coincide con la memoria institucional de comportamiento esperado de estaciones de trabajo del dominio Technoma.
- Estado: Closed
- Resolution Tag: False Positive
```
