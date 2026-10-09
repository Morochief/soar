# Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR

## 1. Identificación del Caso
- **ID de Caso:** `27810_Internal_SMB_Write_and_Read_Anomaly_GPO`
- **ID de Secuencia Stellar:** 27810, 28345, 28353, 28377 (4 eventos correlacionados)
- **Tenant:** Technoma (`cf73a415c8794884a0c35b458b7c73ae`)
- **Sensor:** `technoma-sensor` (`4e3eab0649114a80a089a5d5a078994d`)
- **Reglas Involucradas:**
  - `internal_smb_anomaly` (1 evento - Machine Learning / Lateral Movement)
  - `internal_smb_read_anomaly` (3 eventos - Machine Learning / Lateral Movement)
- **Ventana Temporal de Detección:** 26/09/2026 07:55:54 UTC a 26/09/2026 11:40:49 UTC (04:55:54 a 08:40:49 Local)
- **Analista Responsable:** Kevin Moraes
- **Veredicto Técnico:** Falso Positivo (Actividad Legítima de Active Directory: Sincronización de GPO y LSA RPC)

---

## 2. Declaración de Cantidad y Desglose Individual del Lote (4 Eventos)

Se procesaron **4 eventos individuales** de anomalía volumétrica de protocolo SMB:

1. **Evento 1 (`_seq_no: 27810` | `internal_smb_anomaly`):** 10 peticiones SMB de escritura registradas en 5 minutos (típico: 2) originadas desde la IP `192.168.169.155` hacia el DC `10.11.1.1:445` (`ad.technoma.local`). La actividad consistió en la conexión a la carpeta compartida oculta `\\ad.technoma.local\IPC$` y la apertura de la tubería con nombre (`named pipe`) `lsarpc` (Local Security Authority RPC).
2. **Evento 2 (`_seq_no: 28345` | `internal_smb_read_anomaly`):** 50 peticiones SMB de lectura en 5 minutos (típico: 9) originadas desde `192.168.169.9` (`nb-noc1.technoma.local`) hacia `10.11.1.1:445`. Acceso a la carpeta `\\ad.technoma.local\sysvol` para leer los archivos de directivas de grupo: `technoma.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\User\Preferences\Shortcuts\Shortcuts.xml` y `gpt.ini`.
3. **Evento 3 (`_seq_no: 28353` | `internal_smb_read_anomaly`):** 43 peticiones SMB de lectura en 5 minutos (típico: 9) desde `192.168.169.15` (`nb-jrivarola.technoma.local`) hacia `10.11.1.1:445`. Acceso a `\\ad.technoma.local\SysVol` y `IPC$` para verificar y sincronizar las plantillas de GPO `{31B2F340-016D-11D2-945F-00C04FB984F9}\gpt.ini` y `{87B52B57-07B6-4758-9B97-96AA41B2A7B6}\gpt.ini`.
4. **Evento 4 (`_seq_no: 28377` | `internal_smb_read_anomaly`):** 51 peticiones SMB de lectura en 5 minutos (típico: 8) desde `192.168.169.9` (`nb-noc1.technoma.local`) hacia `10.11.1.1:445`. Conexión combinada a `\\ad.technoma.local\sysvol` e `IPC$` interactuando con la tubería `lsarpc`.

---

## 3. Descripción y Actores Involucrados
| Parámetro | Estaciones de Trabajo (Endpoints) | Controlador de Dominio (Destino) |
| :--- | :--- | :--- |
| **Equipos Involucrados** | `192.168.169.155` (Host local), `192.168.169.9` (`nb-noc1`), `192.168.169.15` (`nb-jrivarola`) | `10.11.1.1` (`ad.technoma.local` - DC Primario) |
| **Protocolo / Puerto** | TCP 445 (Microsoft-DS / SMBv2) | TCP 445 (Microsoft-DS / SMBv2) |
| **Recursos Solicitados** | `\\ad.technoma.local\IPC$`, `\\ad.technoma.local\sysvol` | Recursos nativos de Active Directory |
| **Archivos / Tuberías** | `lsarpc`, `gpt.ini`, `Shortcuts.xml` | Objetos de Directiva de Grupo (GPO) |

---

## 4. Análisis Técnico y Causa Raíz (Cruce con Rosetta Stone y Memoria Institucional)

### A. Interacción con Tubería Named Pipe `lsarpc` (Eventos 1 y 4)
En los eventos 1 y 4, las estaciones se conectan al recurso `IPC$` (Inter-Process Communication) y abren la interfaz RPC `lsarpc`. Traduciendo los comandos según la especificación SMBv2 (`SMB_Rosetta_Stone.md`):
* Comando 1 (`SMB2_SESSION_SETUP`): Establecimiento de sesión autenticada.
* Comando 3 (`SMB2_TREE_CONNECT`): Montaje de la carpeta `IPC$`.
* Comando 5 (`SMB2_CREATE`): Apertura del endpoint `lsarpc`.
* Comandos 8 y 9 (`SMB2_READ` y `SMB2_WRITE`): Intercambio de transacciones de RPC sobre la tubería para consultar identificadores de seguridad (SIDs), validar la membresía de grupos del dominio y aplicar directivas de seguridad local. Este comportamiento es el estándar nativo de Windows al comunicarse con un Controlador de Dominio.

### B. Descarga y Verificación de GPOs en SYSVOL (Eventos 2 y 3)
En los eventos 2 y 3, los equipos `nb-noc1` y `nb-jrivarola` acceden al recurso compartido de replicación `SYSVOL`. Los archivos leídos corresponden a:
1. `gpt.ini`: Archivo de configuración que contiene el número de versión de la directiva de grupo. El cliente compara este número con su versión local para determinar si debe descargar cambios.
2. `{31B2F340-016D-11D2-945F-00C04FB984F9}`: GUID universal y estándar de Microsoft que identifica la **Default Domain Policy**.
3. `Shortcuts.xml`: Extensión de preferencias de directiva de grupo (GPE) que distribuye los accesos directos de escritorio a los usuarios del dominio.

El motor de Machine Learning de Stellar Cyber disparó las alertas debido a un incremento transitorio en la cantidad de operaciones por bloque de 5 minutos (10 a 51 operaciones frente a una base típica de 2 a 9), el cual coincide con el ciclo automático de refresco de directivas de Windows (`gpupdate` cada 90 minutos con desfase aleatorio) o el inicio de jornada laboral de las estaciones.

---

## 5. Evaluación de Impacto (Tríada CIA)
- **Confidencialidad:** 0/10 (No existe filtración; las lecturas de SYSVOL e IPC$ son públicas para los miembros autenticados del dominio).
- **Integridad:** 0/10 (No se realizaron escrituras no autorizadas ni modificaciones de directivas).
- **Disponibilidad:** 0/10 (El Controlador de Dominio y las estaciones operan con total normalidad).
- **Puntuación Global de Riesgo:** **0.0 / 10 (Insignificante / Falso Positivo Operativo)**.

---

## 6. Veredicto y Confianza Analítica
```json
{
  "veredicto": "False Positive",
  "categoria": "Ruido Operativo de Sincronizacion de GPO y LSA RPC en Active Directory",
  "confianza_analitica": "100%",
  "justificacion": "Las 4 alertas corresponden a transacciones legitimas SMBv2 hacia el DC primario 10.11.1.1 para la lectura de directivas de grupo en SYSVOL (Default Domain Policy) e invocaciones rutinarias de LSA RPC en IPC$ para autenticacion de estaciones corporativas."
}
```

---

## 7. Fila Única para Bitácora de Excel

| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc.) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 26/09/2026 08:40 | Kevin Moraes | Technoma | 27810 | technoma-sensor / new_ml | - | Baja | internal_smb_anomaly / internal_smb_read_anomaly | Sincronización de GPO y Consultas LSA RPC en Active Directory | ad.technoma.local (10.11.1.1), nb-noc1 (192.168.169.9), nb-jrivarola (192.168.169.15), 192.168.169.155 | Lote de 4 eventos (1 SMB write anomaly y 3 SMB read anomaly). FP operativo: lectura rutinaria de directivas de grupo (Default Domain Policy gpt.ini y Shortcuts.xml) en SYSVOL y llamadas a tubería nombrada lsarpc en IPC$ hacia el DC primario 10.11.1.1. Sin actividad maliciosa ni movimiento lateral. | SMBv2 TCP/445 traffic (named pipe lsarpc, \\\\ad.technoma.local\\sysvol, Default Domain Policy GUID {31B2F340-016D-11D2-945F-00C04FB984F9}) | Cerrar en plataforma como Falso Positivo. | Cerrado | - | No | - | PB 5.2 |

---

## 8. Instrucción de Cierre en Plataforma Stellar Cyber
* **Estado:** `Closed`
* **Resolution Tag:** `False Positive`
* **Comentario de Cierre Maestro Unificado:**
> Cierre por Falso Positivo: Las anomalías de lectura y escritura SMB registradas desde las estaciones corporativas 192.168.169.155, nb-noc1 (192.168.169.9) y nb-jrivarola (192.168.169.15) hacia el Controlador de Dominio ad.technoma.local (10.11.1.1) corresponden a operaciones operativas legítimas del entorno de Directorio Activo. La telemetría analizada confirma la lectura periódica de archivos de directivas de grupo en el recurso compartido SYSVOL, específicamente la verificación de versión de la directiva por defecto del dominio (Default Domain Policy {31B2F340-016D-11D2-945F-00C04FB984F9} a través de gpt.ini y Shortcuts.xml), junto con consultas normales de autenticación y seguridad local sobre la tubería named pipe lsarpc en IPC$. Se descarta movimiento lateral o actividad maliciosa.
