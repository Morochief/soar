---
name: windows-privilege-escalation-defense
description: Guía de defensa, detección y auditoría de vectores de escalada de privilegios en Windows (Blue Team / SOC). Cobertura de telemetría de eventos de seguridad (Event IDs, Sysmon), reglas de detección en SIEM/EDR (Stellar Cyber, Cortex XDR) y medidas de endurecimiento (Hardening).
---

# Auditoría, Detección y Defensa contra Escalada de Privilegios en Windows

Esta guía está diseñada para **Analistas SOC y Blue Teams**. Su propósito es identificar, correlacionar y mitigar intentos de escalada de privilegios en sistemas operativos Windows sin utilizar código ofensivo ni payloads que disparen falsos positivos en motores de EDR (Cortex XDR, Microsoft Defender, Stellar Cyber).

---

## 1. Mapeo a MITRE ATT&CK (Táctica TA0004: Privilege Escalation)

| Técnica MITRE | Vector de Escalada | Telemetría / Indicador Clave | Event IDs Relevantes |
| :--- | :--- | :--- | :--- |
| **T1068** | Explotación de Vulnerabilidades de Kernel / Drivers | Carga de drivers no firmados o anómalos | Sysmon Event 6 (Driver Loaded), Event 7045 |
| **T1574.009** | Rutas de Servicio No Entrecomilladas (*Unquoted Service Paths*) | Ejecución de binarios intermedios en `Program Files` | Security Event 4688, Sysmon Event 1 |
| **T1543.003** | Creación / Modificación de Servicios del Sistema | Nuevos servicios con binarios en rutas de usuario | Security Event 7045, Event 4697 |
| **T1134** | Abuso de Privilegios de Token (*Access Token Manipulation*) | Asignación de privilegios especiales (`SeImpersonate`, `SeDebugPrivilege`) | Security Event 4672, Event 4673 |
| **T1053.005** | Tareas Programadas con Privilegios Elevados | Creación de tareas con contexto de `SYSTEM` o `Administrators` | TaskScheduler Event 106, Security Event 4698 |
| **T1546.015** | Component Object Model (COM) Hijacking | Modificación de llaves CLSID en `HKCU\Software\Classes\CLSID` | Sysmon Event 12, 13 (Registry Object Added/Modified) |
| **T1548.002** | Evasión de Control de Cuentas de Usuario (*UAC Bypass*) | Procesos hijos con integridad alta generados desde procesos medianos | Sysmon Event 1 (IntegrityLevel: High desde Medium) |

---

## 2. Telemetría y Fuentes de Detección

### A. Registro de Auditoría de Windows (Security Events)
* **Event ID 4688:** Creación de un nuevo proceso (Requiere tener habilitada la directiva: *Include Command Line in Process Creation Events*).
* **Event ID 4672:** Asignación de privilegios especiales a un nuevo inicio de sesión (supervisar inicios de sesión que no provengan de cuentas de servicio documentadas).
* **Event ID 4673:** Intento de llamada a un privilegio sensible (ej. `SeDebugPrivilege`, `SeTcbPrivilege`).
* **Event ID 4697 / System Event ID 7045:** Se instaló un nuevo servicio en el sistema. Debe auditarse el campo `ImagePath` para descartar rutas temporales (`C:\Users\*`, `C:\Temp\*`, `C:\ProgramData\*`).
* **Event ID 4698 / 4702:** Creación o actualización de una Tarea Programada.

### B. Telemetría Avanzada de Sysmon
* **Event ID 1 (Process Creation):** Permite auditar el hash (`sha256`), el árbol genealógico del proceso (`ParentCommandLine`, `ParentProcessId`) y el nivel de integridad (`IntegrityLevel`).
* **Event ID 11 (FileCreate):** Detección de creación de binarios ejecutables en carpetas accesibles a usuarios estándar donde un servicio o DLL hijack podría residir.
* **Event ID 12 / 13 / 14 (Registry Events):** Modificaciones a llaves de persistencia y servicios:
  - `HKLM\SYSTEM\CurrentControlSet\Services`
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
  - `HKCU\Software\Classes\CLSID`

---

## 3. Consultas Analíticas para SIEM / Threat Hunting (Stellar Cyber / Elastic / XDR)

### Vector 1: Servicios Sospechosos con Rutas No Estándar (T1543.003)
En entornos corporativos, los servicios legítimos residen en `C:\Windows\System32\` o `C:\Program Files\`. Los servicios maliciosos o exploits locales suelen apuntar a rutas de usuario con permisos de escritura.
```json
{
  "query": {
    "bool": {
      "must": [
        { "term": { "winlog.event_id": 7045 } }
      ],
      "should": [
        { "wildcard": { "winlog.event_data.ImagePath.keyword": "*\\Users\\*" } },
        { "wildcard": { "winlog.event_data.ImagePath.keyword": "*\\Temp\\*" } },
        { "wildcard": { "winlog.event_data.ImagePath.keyword": "*\\AppData\\*" } },
        { "wildcard": { "winlog.event_data.ImagePath.keyword": "*\\ProgramData\\*" } }
      ],
      "minimum_should_match": 1
    }
  }
}
```

### Vector 2: Detección Heurística de UAC Bypass (T1548.002)
Supervisar procesos administrativos (`cmd.exe`, `powershell.exe`, `regsvr32.exe`) cuyo proceso padre sea una utilidad estándar de Windows de elevación automática (`fodhelper.exe`, `computerdefaults.exe`, `eventvwr.exe`, `slui.exe`).
```json
{
  "query": {
    "bool": {
      "must": [
        { "terms": { "process.name": ["cmd.exe", "powershell.exe", "pwsh.exe"] } },
        { "terms": { "process.parent.name": ["fodhelper.exe", "computerdefaults.exe", "eventvwr.exe", "slui.exe"] } }
      ]
    }
  }
}
```

### Vector 3: Detección de Abuso de AlwaysInstallElevated (T1546.016)
Auditar si las directivas de instalación con privilegios elevados están habilitadas por error de configuración:
- Llaves a monitorear:
  * `HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated`
  * `HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated`
- Si el valor es `1`, cualquier usuario no privilegiado puede ejecutar un paquete `.msi` que se ejecutará en contexto de `NT AUTHORITY\SYSTEM`.

---

## 4. Estrategia de Endurecimiento y Hardening (Defensa en Profundidad)

1. **Principio de Mínimo Privilegio (PoLP):**
   - Retirar privilegios de administrador local a las cuentas de usuario finales.
   - Utilizar soluciones de gestión de contraseñas de administrador local (**LAPS - Local Administrator Password Solution**) para evitar movimiento lateral con credenciales compartidas.
2. **Restricción de Privilegios de Token en Cuentas de Servicio:**
   - Asegurarse de que los servicios web o bases de datos (ej. IIS_IUSRS, SQL Server) no ejecuten con cuentas que posean `SeImpersonatePrivilege` o `SeAssignPrimaryTokenPrivilege`, mitigando vectores tipo Potato/Token Impersonation.
3. **Control de Aplicaciones y Ejecución:**
   - Habilitar **AppLocker** o **Windows Defender Application Control (WDAC)** para impedir la ejecución de scripts o binarios no autorizados desde carpetas con permisos de escritura por parte del usuario (`AppData`, `Temp`).
4. **Auditoría de Permisos en Carpetas de Software:**
   - Validar que los directorios donde se instalan aplicaciones en `C:\Program Files` no tengan permisos de escritura heredados para el grupo `Users` o `Everyone` (evitando DLL Sideloading y Service Binary Hijacking).

---

## 5. Playbook de Respuesta ante Detección de Escalada

1. **Triage Inmediato:**
   - Identificar el proceso que generó la elevación y el usuario original.
   - Validar si la cuenta de origen pertenece al departamento de TI o si se trata de un usuario operativo habitual.
2. **Aislamiento de Red:**
   - En caso de confirmarse actividad maliciosa o comandos anómalos, aislar el endpoint desde la consola EDR (Cortex XDR / Stellar Cyber) para cortar el movimiento lateral.
3. **Extracción Forense:**
   - Recolectar árbol de procesos, conexiones de red activas en ese instante y llaves de registro alteradas.
4. **Remediación:**
   - Revocar permisos anómalos, eliminar servicios/tareas programadas no autorizadas y forzar reseteo de credenciales de las cuentas involucradas.
