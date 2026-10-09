# Playbook SOC: Diagnostico y Remediacion de Sophos Event::Endpoint::ServiceNotRunning

**Alerta Stellar Cyber:** Sophos Event: XDR Endpoint Indicator of Threat
**Evento Nativo Sophos:** Event::Endpoint::ServiceNotRunning
**Descripcion del Evento:** "One or more Sophos services are missing or not running"
**Tactica / Tecnica:** XDR EBA (XTA0001) / XDR Endpoint Indicator of Threat (XT1004) - Stage: Persistent Foothold
**Clasificacion:** Falso Positivo de Intrusion / Alerta Operacional de Salud del Agente (Transitorio por AutoUpdate)

---

## 1. Contexto y Causa Raiz Institucional

Cuando Sophos Central reporta Event::Endpoint::ServiceNotRunning, el 95% de las incidencias en estaciones de trabajo y servidores no corresponde a un ciberataque ni a la detencion forzada de procesos por actores maliciosos.

En la gran mayoria de los casos observados, obedece a **ciclos automaticos de actualizacion de componentes de Sophos Endpoint**:
1. El actualizador (SophosUpdate.exe nanoservicio) inicia la descarga y sustitucion de firmas o modulos (ej. Sophos File Scanner, HitmanPro.Alert).
2. Para inyectar los nuevos binarios, el instalador desregistra y detiene momentaneamente el servicio anterior (Posting service uninstalled event).
3. Si el proceso de instalacion supera la ventana de gracia (update grace period, aprox. 3 a 5 minutos), el monitor local SophosHealth.exe asume que el servicio se encuentra caido y transiciona su estado a Overall: 1, Service: 1, Threat: 0, enviando la alerta a Sophos Central.
4. Tras finalizar la instalacion, el servicio arranca nuevamente de forma automatica (Running Auto), pero Sophos Central retiene la notificacion hasta que el agente reporte un nuevo latido de salud saludable (Overall: 0).

---

## 2. Protocolo de Diagnostico Rapido via Live Response

Al conectarse al host mediante **Sophos Central Live Response** (sesion con privilegios de Administrador / SYSTEM), ejecutar los siguientes comandos en PowerShell:

### Paso 1: Validar si los motores criticos de proteccion estan corriendo
Get-CimInstance Win32_Service | Where-Object {$_.PathName -like "*Sophos*" -or $_.PathName -like "*HitmanPro*"} | Select-Object Name, DisplayName, State, StartMode | Format-Table -AutoSize

* Criterio: Verificar que Sophos File Scanner Service, hmpalertsvc (HitmanPro), SntpService (Network Threat Protection) y Sophos Endpoint Defense Service esten en estado Running con inicio Auto.

### Paso 2: Verificar procesos activos en memoria
Get-Process *sophos*, *sed*, *hmpa*, *ssp* -ErrorAction SilentlyContinue | Select-Object Id, ProcessName, Path, CPU | Format-Table -AutoSize

* Criterio: Deben figurar en ejecucion procesos clave como SophosFileScanner, hmpalert, SEDService, SophosHealth, SophosNetFilter y SSPService.

### Paso 3: Inspeccionar el log de salud reciente
Get-Content -Path "C:\ProgramData\Sophos\Health\Logs\Health.log" -Tail 25

* Diagnostico: Buscar lineas con "Ignored service check results: during update grace period" y "Posting service uninstalled event". Esto confirma que el evento fue causado por la actualizacion automatica.

### Paso 4: Comprobar si hay reinicio pendiente
Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager" -Name PendingFileRenameOperations -ErrorAction SilentlyContinue | Select-Object -ExpandProperty PendingFileRenameOperations -ErrorAction SilentlyContinue | Measure-Object | Select-Object Count

* Si Count = 0: No hay reinicio pendiente.
* Si Count > 0: La actualizacion finalizo pero requiere reinicio del equipo al finalizar la jornada.

---

## 3. Procedimiento de Remediacion y Reseteo de Salud

Si los servicios ya estan en estado Running pero Sophos Central mantiene la alerta activa, forzar el re-escaneo y la sincronizacion inmediata:

### 1. Reiniciar el monitor de salud local
Stop-Process -Name SophosHealth -Force

*(El servicio guardian SEDService lo levantara de forma automatica en 2 segundos, obligandolo a re-evaluar todos los servicios).*

### 2. Forzar actualizacion y envio de telemetria a Sophos Central
& "C:\Program Files\Sophos\AutoUpdate\SophosUpdate.exe"

### 3. Verificar retorno a estado Saludable (Verde)
Esperar 10 a 15 segundos y ejecutar:
Get-Content -Path "C:\ProgramData\Sophos\Health\Logs\Health.log" -Tail 15

* Criterio de Exito: Debe mostrar la linea:
  Health state has changed to - Overall: 0, Service: 0, Threat: 0

---

## 4. Que hacer si un servicio realmente esta detenido o faltante

### Caso A: El servicio existe pero esta en estado Stopped
Get-Service *Sophos* | Where-Object {$_.Status -eq "Stopped"} | Start-Service -Verbose

### Caso B: Fallo repetitivo por corrupcion de WMI (Error 80041f00)
Si los servicios fallan al iniciar debido a errores de repositorio de Windows:
winmgmt /resetrepository
net stop winmgmt /y
net start winmgmt
rd /s /q "C:\ProgramData\Sophos\AutoUpdate\Cache"
shutdown /r /t 300 /c "Soporte IT: Reinicio preventivo para estabilizar componentes de seguridad."

### Caso C: El servicio fue desinstalado por completo (Missing en Windows 10/11)
En Windows 10/11 x64, desplegar de manera silenciosa el instalador maestro corporativo sobre la instalacion existente:
SophosSetup.exe --quiet

---

## 5. Plantilla de Cierre para Stellar Cyber

* Estado: Resolved
* Resolucion: False Positive
* Asignado: Operador en turno (ej. kevinmoraes@technoma.com.py)

Texto de Cierre:
"Event::Endpoint::ServiceNotRunning - Falso Positivo Operacional (Actualizacion Transitoria de Sophos)

Se procede al cierre de la alerta tras auditar la estacion de trabajo mediante Live Response y comprobar que la notificacion derivo de un evento transitorio durante el ciclo automatico de actualizacion de componentes de Sophos Endpoint.

La revision forense de Health.log constato que a la hora del incidente el instalador desmonto momentaneamente el binario de Sophos File Scanner para sustituirlo por la version actualizada, superando temporalmente el periodo de gracia y disparando la alerta a Central. La telemetria en vivo confirma que todos los servicios y procesos defensivos (Sophos File Scanner Service, HitmanPro.Alert hmpalertsvc, Sophos Endpoint Defense y SntpService) se encuentran activos y en ejecucion (Running Auto), con la proteccion en tiempo real plenamente restaurada. Se forzo la sincronizacion de salud retornando a estado Overall: 0. Incidente cerrado formalmente como Falso Positivo Operacional."
