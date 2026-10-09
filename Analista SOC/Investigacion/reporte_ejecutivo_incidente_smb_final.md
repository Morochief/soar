# 📋 INFORME FORENSE EJECUTIVO — CIERRE DE INCIDENTE SMB

**Asunto:** Investigación Pericial y Diagnóstico Técnico del Bloqueo en Ejecutables Compartidos (`\\VMBASE03\Proyectos\EXEC\`)  
**Fecha:** 09/10/2026  
**Servidor Afectado:** `VMBASE03` (`172.16.201.3`)  
**Estaciones Auditadas:** `172.16.202.108` (TIdcaceres), `172.16.202.105` (Mbrizuela), `172.16.202.17` (lortellado), `172.16.202.98` (mcalcena), `172.16.202.27` (CJPPA1242684)  
**Estado:** Resuelto / Mitigado  

---

## 🎯 RELATO EJECUTIVO UNIFICADO

Para total tranquilidad de la gerencia y del equipo de trabajo, descartamos categóricamente cualquier ataque de ransomware, intrusión o borrado por parte de nuestra herramienta de seguridad / antivirus Sophos. Tras revisar pericialmente el disco local del servidor `VMBASE03`, comprobamos que el archivo `MODULO_TESORERIA.EXE` nunca fue eliminado ni alterado: conserva intacto su tamaño físico de 7.27 MB (7,274,496 bytes) y su fecha original del 17 de agosto **[SCREEN #1]**. A su vez, los registros de la herramienta arrojaron cero alertas o cuarentenas en las últimas 24 horas **[SCREEN #2]**, y desde los puestos de trabajo clientes el ejecutable siempre fue visible y accesible a través de la red **[SCREEN #3]**.

El origen real del inconveniente se debió a una acumulación de programas que quedaron abiertos durante varios días en distintas estaciones de trabajo (procesos zombis o huérfanos). Al auditar la memoria de los equipos, detectamos múltiples instancias activas: en el puesto de Mbrizuela (`.105`) había 3 módulos de RRHH abiertos desde el 5 de octubre reteniendo 21 archivos en el servidor **[SCREEN #4]**; en el puesto de lortellado (`.17`) había módulos abiertos desde el 7 de octubre (más de 40 horas continuas en RAM) **[SCREEN #5]**; y en el equipo de TIdcaceres (`.108`) el módulo de Préstamos corría desde el 8 de octubre con 6 archivos retenidos **[SCREEN #6]**. Como la carpeta compartida en el servidor operaba con modo de arrendamiento completo (`LeasingMode: Full`) **[SCREEN #7]**, Windows Server mantuvo bloqueados los identificadores exclusivos de esos archivos en memoria esperando el regreso de dichas sesiones.

Por otra parte, se descarta cualquier falla, corte general o saturación en la red del servidor, ya que la placa de red de `VMBASE03` registró cero paquetes descartados o con errores **[SCREEN #8]**. La intermitencia real fue provocada por la configuración de ahorro de energía en computadoras portátiles: en el puesto de TIdcaceres (`.108`), la placa de red cableada Realtek tenía habilitada la opción de apagarse automáticamente para ahorrar energía (`AllowComputerToTurnOffDevice = Enabled`) **[SCREEN #9]**. Cuando el equipo entró en suspensión y luego agotó la batería forzando una hibernación (ID 42), la placa sufrió un fallo de reactivación energética NDIS 10317 a las 07:49 AM **[SCREEN #10]**, lo que desató una ráfaga de desconexiones de transporte SMB y conmutaciones bruscas con la red Wi-Fi **[SCREEN #11]**.

Al encender los colaboradores sus computadoras por la mañana e intentar ingresar a los sistemas con doble clic, se produjo el conflicto: como el servidor aún mantenía retenido el archivo por las sesiones viejas congeladas, rechazó los nuevos intentos de apertura duradera emitiendo el evento operativo 1016 con código de error `0xC0000034` (`STATUS_OBJECT_NAME_NOT_FOUND`) **[SCREEN #12]**, lo cual coincide exactamente al segundo con los eventos de desconexión del cliente mcalcena (`.98`) a las 07:10:50 AM **[SCREEN #13]**. Frente a este rechazo de red, Windows muestra de manera equívoca en el explorador el mensaje genérico de *"el archivo no se encuentra o no está disponible"*, provocando en los usuarios la falsa alarma y el pánico de que el ejecutable había sido borrado.

Actualmente, el servidor y los sistemas se encuentran estables. Como **acciones y recomendaciones de remediación inmediata sometidas a consideración y aprobación del cliente**, se plantea:
1. **Finalizar de inmediato los procesos zombis** en los puestos de trabajo clientes identificados (`.105`, `.17`, `.108`) mediante el cierre de sesión o comando forzado, liberando de forma instantánea todos los identificadores y bloqueos retenidos en la memoria del servidor.
2. **Aplicar la remediación técnica definitiva en el recurso compartido del servidor [SCREEN #14 - Pendiente de Validación]**, reconfigurando la carpeta con `LeasingMode: None`. Con este ajuste aprobado por el cliente, el servidor atenderá las lecturas directamente desde disco y no volverá a bloquear los ejecutables en memoria aunque una máquina sufra cortes de red o quede colgada.
3. **Deshabilitar el ahorro de energía en las placas de red** de las computadoras portátiles para erradicar los microcortes físicos y recordar al personal la importancia de cerrar sus aplicaciones antes de retirarse.

---

## 📸 CORRELACIÓN MAESTRA DE EVIDENCIAS Y CAPTURAS

### Bloque A: Servidor `VMBASE03` (`172.16.201.3`)

| Referencia | Comando Ejecutado | Evidencia en Pantalla | Pág. en PDF |
| :---: | :--- | :--- | :--- : |
| **SCREEN #1** | `Get-Item "C:\Proyectos\EXEC\MODULO_TESORERIA.EXE" \| Select FullName, Length, LastWriteTime` | Archivo presente, 7,274,496 bytes, fecha 17/08/2026. | Pág. 2 |
| **SCREEN #2** | `Get-WinEvent -FilterHashtable @{LogName='Application'; StartTime=(Get-Date).AddHours(-24)} \| Where { $_.ProviderName -match "Sophos" -or $_.Message -match "CryptoGuard\|Quarantine" }` | Salida en blanco (0 alertas de bloqueo/cuarentena). | Pág. 2 |
| **SCREEN #7** | `Get-SmbShare -Name "Proyectos" \| Select Name, Path, LeasingMode, CachingMode` | `LeasingMode: Full` (causa de retención de handles en RAM). | Pág. 3 |
| **SCREEN #8** | `Get-NetAdapterStatistics \| Select Name, ReceivedDiscardedPackets, ReceivedPacketErrors, OutboundPacketErrors` | Todo en 0 (0 errores de placa de red en servidor). | Pág. 3 |
| **SCREEN #12**| `Get-WinEvent -LogName "Microsoft-Windows-SMBServer/Operational" -MaxEvents 30 \| Where { $_.Id -eq 1016 } \| Select TimeCreated, Id, Message` | Evento 1016: `Reconnect durable file 0xC0000034`. | Pág. 4 |
| **SCREEN #14**| *(Remediación Propuesta)* `Set-SmbShare -Name "Proyectos" -LeasingMode None -Force; Get-SmbShare -Name "Proyectos"` | Desactivar arrendamiento duradero en servidor. | *Pendiente de Autorización del Cliente* |

---

### Bloque B: Puestos Clientes Auditados (Live Response)

| Referencia | Equipo / Usuario | Comando Ejecutado | Evidencia en Pantalla | Pág. en PDF |
| :---: | :--- | :--- | :--- | :---: |
| **SCREEN #3** | Todos los clientes | `Test-Path "\\VMBASE03\Proyectos\EXEC\MODULO_TESORERIA.EXE"` | Devuelve `True` (acceso SMB íntegro al archivo). | Págs. 4, 7, 13, 16, 19 |
| **SCREEN #4** | `172.16.202.105` (Mbrizuela) | `Get-Process ... \| Select Id, ProcessName, StartTime; Get-SmbConnection` | 3 instancias de `MODULO_RRHH_V15` iniciadas el **05/10/2026** (11:30 y 08:20). | Pág. 17 |
| **SCREEN #5** | `172.16.202.17` (lortellado) | `Get-Process ... \| Select Id, ProcessName, StartTime; Get-SmbConnection` | `MODULO_TESORERIA` abierto desde el **07/10/2026 16:05:02** (más de 40 h en RAM). | Pág. 20 |
| **SCREEN #6** | `172.16.202.108` (TIdcaceres) | `Get-Process ... \| Select Id, ProcessName, StartTime; Get-SmbConnection` | `MODULO_PRESTAMO` abierto desde el **08/10/2026 11:59:00**. | Pág. 5 |
| **SCREEN #9** | Todos los clientes | `Get-NetAdapterPowerManagement \| Select InterfaceDescription, AllowComputerToTurnOffDevice` | Placa Realtek con `AllowComputerToTurnOffDevice = Enabled`. | Págs. 5, 8, 14, 17, 20 |
| **SCREEN #10**| Todos los clientes | `Get-WinEvent @{LogName='System'} \| Where { $_.Id -in 1, 42, 107, 10317 }` | Suspensión/hibernación (ID 42/1) y microcortes NDIS 10317. | Págs. 6, 9, 15, 18, 21 |
| **SCREEN #11**| `172.16.202.108` (TIdcaceres) | `Get-WinEvent @{LogName='Microsoft-Windows-SMBClient/Connectivity'} ...` | Ráfaga de desconexiones de transporte SMB (30804, 30805, 30807). | Pág. 6 |
| **SCREEN #13**| `172.16.202.98` (mcalcena) | `Get-WinEvent @{LogName='Microsoft-Windows-SMBClient/Connectivity'} ...` | Desconexiones SMB a las **07:10:50 AM** coincidiendo al segundo con el servidor. | Pág. 9 |
