# Resumen Ejecutivo — Alerta "Sensitive Windows Network Share Accessed" (protected_storage)

**Organización:** Technoma / Caja Ande
**Fecha del análisis:** 12/08/2026
**Analista:** SOC / Equipo de seguridad
**Clasificación final:** Falso positivo — comportamiento nativo de Windows (DPAPI Backup Key Sync)

---

## 1. Alerta original

| Campo | Valor |
|---|---|
| Detector | `windows_security_sensitive_networkshare` |
| Event ID | 5145 (Detailed File Share) |
| Técnica MITRE | T1021.002 — SMB/Windows Admin Shares |
| Táctica MITRE | TA0008 — Lateral Movement |
| Referencia del detector | Potential abuse of DPAPI to extract domain backup keys from Domain Controllers |
| Host destino | VMBASE8 (Domain Controller secundario) — 172.16.201.8 |
| Endpoint origen | CJPPA037 — 172.16.202.57 (Windows 10 Pro) |
| Usuario | CAJAANDE\CJPPA_3509448 |
| Recurso accedido | `\\*\IPC$\protected_storage` |
| Resultado | `outcome: success` |
| Hora del evento | 2026-08-12T09:58:38Z (≈05:58 a.m. hora local, UTC-4) |

---

## 2. Comandos ejecutados durante la investigación (Sophos Live Response, sobre CJPPA037)

Todos los comandos fueron de **solo lectura** — no se ejecutó ninguna acción de contención, remediación ni modificación durante la investigación.

| # | Comando | Objetivo |
|---|---|---|
| 1 | `query user` | Confirmar sesión activa del usuario en el endpoint |
| 2 | `Get-WmiObject Win32_LoggedOnUser` | Ver todas las sesiones lógicas activas (sistema y usuario) |
| 3 | `Get-CimInstance Win32_Process \| Select ProcessId, ParentProcessId, Name, CommandLine` | Inventario completo de procesos en ejecución y sus líneas de comando |
| 4 | `Get-NetTCPConnection -State Established` | Conexiones de red activas y proceso propietario de cada una |
| 5 | `Get-Content ...ConsoleHost_history.txt` | Historial de comandos PowerShell ejecutados por el usuario |
| 6 | `Get-WinEvent -LogName Security -Id 4688` | Buscar eventos de creación de procesos (auditoría) |
| 7 | `Get-ChildItem -Path %TEMP%,Downloads,C:\Users\Public -Include *.exe,*.ps1,*.dll` | Buscar binarios/scripts sospechosos recién colocados |
| 8 | `whoami /all` | Confirmar privilegios de la sesión de Live Response |
| 9 | `Get-ChildItem C:\Windows\Prefetch` (todo el día, y acotado a 05:50–06:15) | Reconstruir cronología de ejecutables lanzados en el endpoint durante el 12/08 |

---

## 3. Hallazgos

- **No se identificaron procesos maliciosos ni herramientas de extracción de credenciales** (Mimikatz, SharpDPAPI, Rubeus u otras) en ejecución ni en disco.
- **No se encontró historial de PowerShell sospechoso** — el archivo de historial estaba vacío.
- **No se encontraron binarios/scripts recién colocados** en rutas típicas de staging (TEMP, Downloads, Public).
- **Auditoría de creación de procesos (Event ID 4688) no está habilitada** en el endpoint — limita la capacidad de confirmación retroactiva.
- **Análisis de Prefetch de todo el día (12/08) no muestra ningún ejecutable nuevo lanzado entre las 05:17 a. m. y las 06:47 a. m.**, ventana que cubre por completo el horario de la alerta (05:58 a. m. local). Esto indica que el acceso al share `protected_storage` no fue generado por un programa/herramienta lanzada por el usuario o un atacante, sino por un proceso interno del sistema operativo (`lsass.exe` / `System`).
- **Conexión SMB relevante ya cerrada** al momento de la investigación — consistente con una operación breve y puntual, no con una sesión de exfiltración sostenida.
- **Confirmado por el responsable del área:** la alerta se repite diariamente para múltiples usuarios/endpoints del dominio, coincidiendo con el patrón esperado de sincronización periódica de claves DPAPI.

## 4. Causa raíz

El evento corresponde al mecanismo nativo de Windows **DPAPI Domain Backup Key Sync**: las estaciones unidas al dominio consultan periódicamente al Domain Controller para verificar que tienen sincronizada la clave de respaldo DPAPI vigente. Esta clave permite que Windows recupere datos protegidos por DPAPI del usuario (credenciales guardadas, certificados, Wi-Fi) incluso tras un reset de contraseña. El proceso:

- Ocurre automáticamente en el logon y periódicamente en background.
- Es gestionado directamente por el subsistema de autenticación del SO (no lanza un ejecutable nuevo).
- Es recurrente, diario, y afecta a múltiples endpoints — consistente con lo observado.

El detector de Stellar Cyber (`windows_security_sensitive_networkshare`) no distingue automáticamente entre este patrón legítimo y una extracción manual con herramientas ofensivas, generando el falso positivo.

## 5. Estado y próximos pasos

- **Caso clasificado como falso positivo** con alta confianza, en base a evidencia técnica (ausencia de binarios/conexiones/historial sospechoso) y confirmación funcional del comportamiento por parte del responsable del área.
- **Limitación conocida:** al no estar habilitada la auditoría de creación de procesos (Event ID 4688) en el endpoint, no fue posible obtener una confirmación forense del 100% de certeza retroactiva.
- **Recomendación 1:** Habilitar auditoría de creación de procesos en el endpoint y, de ser posible, vía GPO a nivel de dominio:
  ```
  auditpol /set /subcategory:"Creación de proceso" /success:enable
  ```
- **Recomendación 2:** Ajustar (tunear) el detector en Stellar Cyber para reducir el ruido recurrente de este patrón, filtrando por `event_id = 5145` combinado con los Domain Controllers conocidos de la organización, documentando la excepción como aprobada por criterio de negocio.
