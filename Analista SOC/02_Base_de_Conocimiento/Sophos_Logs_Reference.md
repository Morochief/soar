# Referencia de Logs de Sophos Endpoint y Server

*Fuente: KBA-000006725 (Sophos Endpoint and Server: Information on Windows log files)*

Este documento proporciona información sobre los diversos archivos de registro (logs) utilizados por cada uno de los componentes de Sophos Central Endpoint y Sophos Central Server en Windows.

## Sophos AutoUpdate
* **sau-service.log**
  * *Ubicación:* `C:\ProgramData\Sophos\AutoUpdate\Logs`
  * *Descripción:* Log del nanoservicio que contiene información sobre cuándo se activa una actualización desde Sophos Central o cambios de política para actualización/comunicación. (Solo aplicable a Windows 10 x64+ y Server 2016+).
* **susvc.log**
  * *Ubicación:* `C:\ProgramData\Sophos\AutoUpdate\Logs`
  * *Descripción:* Log del servicio de Sophos AutoUpdate para plataformas legacy.
* **SophosUpdate.log**
  * *Ubicación:* `C:\ProgramData\Sophos\AutoUpdate\Logs`
  * *Descripción:* Contiene información más detallada sobre el proceso de actualización.
* **su-repair.log**
  * *Ubicación:* `C:\ProgramData\Sophos\AutoUpdate\Logs`
  * *Descripción:* Contiene información sobre las verificaciones del kit de reparación realizadas en una actualización.
* **SAUcli.log**
  * *Ubicación:* `C:\ProgramData\Sophos\AutoUpdate\Logs`
  * *Descripción:* Contiene información sobre los comandos ejecutados manualmente mediante la herramienta `SAUcli`.
* **GatherTelem.log**
  * *Ubicación:* `C:\ProgramData\Sophos\AutoUpdate\Logs`
  * *Descripción:* Contiene información sobre el proceso de recopilación de telemetría.
* **Sophos Autoupdate install log*.txt** / **Sophos SAU Install Log*.txt**
  * *Ubicación:* `C:\Windows\Temp` o `C:\Windows\SystemTemp`
  * *Descripción:* Acciones de instalación de Sophos AutoUpdate.

## Sophos Clean
* **Clean.log** / **SophosCleanup.log**
  * *Ubicación:* `C:\ProgramData\Sophos\Clean\Logs`
  * *Descripción:* Contiene acciones de limpieza, verificación de Safestore, recuento de amenazas, comandos de restauración y registro de flujo de procesos.
* **Scan_*.log**
  * *Ubicación:* `C:\ProgramData\Sophos\Clean\Logs`
  * *Descripción:* Contiene el flujo de procesos de tareas, información de volúmenes, la detección que desencadena la operación de limpieza y el tiempo para completar el análisis.

## Sophos Endpoint Defense
* **sed.log**
  * *Ubicación:* `C:\ProgramData\Sophos\Endpoint Defense\Logs`
  * *Descripción:* Archivo de registro principal que contiene información sobre configuraciones de claves de registro protegidas, elementos bloqueados, intentos de acceso al registro, procesos y archivos protegidos.
* **seds.log**
  * *Ubicación:* `C:\ProgramData\Sophos\Endpoint Defense\Logs`
  * *Descripción:* Contiene información si el controlador SED está cargado y el servicio en ejecución.
* **SSP.log**
  * *Ubicación:* `C:\ProgramData\Sophos\Endpoint Defense\Logs`
  * *Descripción:* Contiene Data Loss Prevention (DLP), Control de Periféricos e información sobre la creación de Threat Cases.
* **SophosScanCoordinator.log**
  * *Ubicación:* `C:\ProgramData\Sophos\Endpoint Defense\Logs`
  * *Descripción:* Registro predeterminado para análisis programados y "Scan now".

## Sophos File Scanner
* **SophosFileScanner.log** / **SophosFS.log**
  * *Ubicación:* `C:\ProgramData\Sophos\Sophos File Scanner\Logs`
  * *Descripción:* Contiene información sobre el proceso de trabajo del SFS (PID, tiempos, versión del motor) y los hilos de trabajo del servicio.

## Sophos Network Threat Protection
* **SntpService.log**
  * *Ubicación:* `C:\ProgramData\Sophos\Sophos Network Threat Protection\Logs`
  * *Descripción:* Muestra configuraciones del perímetro de red, aislamiento de dispositivos, ZTNA y SATC.
* **SophosNetFilter.log**
  * *Ubicación:* `C:\ProgramData\Sophos\Sophos Network Threat Protection\Logs`
  * *Descripción:* Registro de conexiones a sitios web y acciones resultantes del Web Control y Real Time Protection - Internet.

## Sophos Management Communications System (MCS)
* **McsAgent.log**
  * *Ubicación:* `C:\ProgramData\Sophos\Management Communications System\Endpoint\Logs`
  * *Descripción:* Detalla la aplicación de políticas y otras comunicaciones extraídas de los servidores de Central.
* **McsClient.log**
  * *Ubicación:* `C:\ProgramData\Sophos\Management Communications System\Endpoint\Logs`
  * *Descripción:* Detalla las comunicaciones crudas entre el endpoint y los servidores de Sophos Central.

## Sophos HitmanPro Alert
* **sophoshmpaservice.log** / **Sophos.log**
  * *Ubicación:* `C:\ProgramData\HitmanPro.Alert\Logs`
  * *Descripción:* Contiene información relacionada con la protección contra ransomware CryptoGuard y la mitigación de exploits.

---
*Nota: Este documento ha sido depurado y formateado a partir del texto bruto de la base de conocimientos oficial de Sophos para rápida referencia SOC.*
