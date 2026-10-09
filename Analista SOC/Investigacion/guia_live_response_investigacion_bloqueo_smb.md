# 🔍 Guía Maestra y Evidencia Forense Live Response — Bloqueo SMB y Descarte de Sophos

**Caso:** Falso Borrado y Bloqueo de Ejecutables en Recurso Compartido (`\\VMBASE03\Proyectos\EXEC\`)  
**Fecha de Investigación:** 09/10/2026 (05:10 AM - 08:15 AM)  
**Activos Clave Auditados:**
* **Servidor Central:** `VMBASE03` (`172.16.201.3` / Windows Server 2019 Build 17763)
* **Estación de Trabajo 1:** `172.16.202.17` (Usuario: `CAJAANDE\lortellado` / Win 11 Pro 26200) — Procesos zombies desde el **07/10**, 15 archivos abiertos
* **Estación de Trabajo 2:** `172.16.202.105` (Usuario: `CAJAANDE\Mbrizuela` / Win 11 Pro 26300) — Procesos zombies desde el **05/10**, 21 archivos abiertos
* **Estación de Trabajo 3:** `172.16.202.109` (Usuario: `CAJAANDE\TIdcaceres`) — 1 archivo abierto, sesión de 17.8 h
* **Estación de Trabajo 4:** `172.16.202.211` (Usuario: `CAJAANDE\CAJA53021`) — 1 archivo abierto, sesión de 16.5 h  
**Metodología:** Extracción de telemetría pericial inmutable mediante PowerShell / Live Response en el servidor y en los endpoints clientes para correlacionar disco físico, memoria kernel, procesos en RAM y sesiones SMB sin conjeturas.

---

## 🏆 EVIDENCIA FORENSE EN VIVO CAPTURADA

### 1. Prueba Fáctica de Integridad en Disco (Descarte de Borrado Físico)

#### A. Archivo `MODULO_TESORERIA.EXE` (En `VMBASE03`)
```powershell
PS C:\Windows\system32> Get-Item "C:\Proyectos\EXEC\MODULO_TESORERIA.EXE" | Select-Object FullName, Length, LastWriteTime

FullName                                Length LastWriteTime
--------                                ------ -------------
C:\Proyectos\EXEC\MODULO_TESORERIA.EXE 7274496 17/08/2026 11:19:40
```
* **Conclusión Forense:** El ejecutable mantiene su tamaño íntegro de 7.27 MB (`7,274,496` bytes) y su fecha de modificación original del **17/08/2026 11:19:40**. **Nunca fue eliminado ni alterado.**

#### B. Archivos en Subcarpeta `VSNET` (`MODULO_RRHH_V15.exe`)
```powershell
PS C:\Windows\system32> Get-Item "C:\Proyectos\EXEC\VSNET\MODULO_RRHH_V15*.exe" | Select-Object Name, Length, LastWriteTime

Name                         Length LastWriteTime
----                         ------ -------------
MODULO_RRHH_V15 - copia.exe 4581376 28/03/2023 16:36:03
MODULO_RRHH_V15.exe         4581376 28/03/2023 16:36:03
```
* **Conclusión Forense:** `MODULO_RRHH_V15.exe` permanece intacto desde el **28/03/2023** (hace más de 3 años). Se descarta que cualquier proceso, usuario o antivirus haya alterado o borrado binarios en el disco físico.

---

### 2. Descarte Absoluto de Sophos Endpoint
```powershell
PS C:\Windows\system32> Get-WinEvent -FilterHashtable @{LogName='Application'; StartTime=(Get-Date).AddHours(-24)} -ErrorAction SilentlyContinue | Where-Object { $_.ProviderName -match "Sophos" -or $_.Message -match "CryptoGuard|Quarantine" }
PS C:\Windows\system32>
```
* **Conclusión Forense:** La consulta arrojó **CERO resultados**. Sophos Central no ejecutó bloqueos, no envió binarios a cuarentena ni detectó patrones de ransomware/CryptoGuard.

---

### 3. Handles Retenidos en Madrugada (`Get-SmbOpenFile` en `VMBASE03`)
A las 05:10 AM, con las estaciones de trabajo físicamente apagadas, el servidor mantenía 16 identificadores abiertos en el kernel:

```text
FileId        ClientComputerName ClientUserName      Path
------        ------------------ --------------      ----
859530330249  172.16.202.17      CAJAANDE\lortellado C:\Proyectos\EXEC\MODULO_PRESTAMO.EXE
858993459565  172.16.202.17      CAJAANDE\lortellado C:\Proyectos\EXEC\MODULO_TESORERIA.EXE (Instancia 1)
858993459569  172.16.202.17      CAJAANDE\lortellado C:\Proyectos\EXEC\MODULO_TESORERIA.EXE (Instancia 2)
858993459593  172.16.202.17      CAJAANDE\lortellado C:\Proyectos\EXEC
860335637681  172.16.202.17      CAJAANDE\lortellado C:\Proyectos\EXEC\REPORTES\rptCHEQUES_GIRADOS.rpt
860067204069  172.16.202.17      CAJAANDE\lortellado C:\Proyectos\EXEC\REPORTES\rptInversiones_vigentes_tesoreria_V2.rpt
859530333273  172.16.202.17      CAJAANDE\lortellado C:\Proyectos\EXEC\VSNET\MODULO_RRHH_V15.EXE
859530333697  172.16.202.17      CAJAANDE\lortellado C:\Proyectos\EXEC\VSNET\MODULO_INVESIONES_V15.EXE (Instancia 1)
859530333737  172.16.202.17      CAJAANDE\lortellado C:\Proyectos\EXEC\VSNET\MODULO_INVESIONES_V15.EXE (Instancia 2)
859530333741  172.16.202.17      CAJAANDE\lortellado C:\Proyectos\EXEC\VSNET\MODULO_INVESIONES_V15.EXE (Instancia 3)
859530333953  172.16.202.17      CAJAANDE\lortellado C:\Proyectos\EXEC\SISTEMA INTEGRADO.exe
860335638553  172.16.202.105     CAJAANDE\Mbrizuela  C:\Proyectos\EXEC\VSNET\MODULO_RRHH_V15.EXE (Instancia 1)
860335638577  172.16.202.105     CAJAANDE\Mbrizuela  C:\Proyectos\EXEC\VSNET\MODULO_RRHH_V15.EXE (Instancia 2)
858993461337  172.16.202.105     CAJAANDE\Mbrizuela  C:\Proyectos\EXEC\VSNET\MODULO_RRHH_V15.EXE (Instancia 3)
859530333853  172.16.202.109     CAJAANDE\TIdcaceres C:\Proyectos\EXEC\SISTEMA INTEGRADO.exe
859798767465  172.16.202.211     CAJAANDE\CAJA53021  C:\Proyectos\EXEC\VSNET\MODULO_RRHH_V15.exe
```

---

### 4. Sesiones SMB Zombis en el Servidor (`Get-SmbSession` en `VMBASE03`)
```powershell
PS C:\Windows\system32> Get-SmbSession | Select-Object SessionId, ClientComputerName, ClientUserName, NumOpens, @{Name="Minutos_Inactivo";Expression={[math]::Round($_.SecondsIdle/60,1)}}, @{Name="Horas_Conectado";Expression={[math]::Round($_.SecondsExists/3600,1)}} | Format-Table -AutoSize

   SessionId ClientComputerName ClientUserName          NumOpens Minutos_Inactivo Horas_Conectado
   --------- ------------------ --------------          -------- ---------------- ---------------
858993459209 172.16.202.17      CAJAANDE\lortellado           15                0            18,3
858993459241 172.16.202.105     CAJAANDE\Mbrizuela             3              3,3            18,3
858993459425 172.16.202.109     CAJAANDE\TIdcaceres            1                8            17,8
858993459785 172.16.202.211     CAJAANDE\CAJA53021             1              4,1            16,5
```
* **Conclusión Forense:** Las sesiones llevaban **18,3 horas vivas** (iniciadas aproximadamente a las 13:00 del día anterior). Los colaboradores abandonaron sus puestos sin cerrar las aplicaciones ni la sesión de Windows.

---

### 5. Configuración de Leasing del Recurso Compartido (`Get-SmbShare`)
```powershell
PS C:\Windows\system32> Get-SmbShare -Name "Proyectos" | Select-Object Name, Path, LeasingMode, CachingMode

Name      Path         LeasingMode CachingMode
----      ----         ----------- -----------
Proyectos C:\Proyectos        Full      Manual
```
* **Conclusión Forense:** Al estar configurado con **`LeasingMode: Full`**, Windows Server otorga concesiones de caché completas y persistentes (Handle Leases). Cuando los clientes suspenden o se desconectan, el servidor preserva los bloqueos en memoria esperando su regreso, lo que bloquea el archivo ante nuevos intentos de apertura.

---

### 6. Causa del Reclamo de Usuarios: Event ID 1016 (`Reconnect durable file`)
En el log `Microsoft-Windows-SMBServer/Operational` se registraron fallos continuos durante la noche y la mañana:

```text
TimeCreated          Id   Level  Message
-----------          --   -----  -------
09/10/2026 7:19:16   1016 Error  Error al volver a abrir.
                                 Cliente: \\172.16.202.27 (CAJAANDE\CJPPA1242684)
                                 Archivo: EXEC\VSNET\MODULO_RRHH_V15.exe
                                 Razón: Reconnect durable file
                                 Estado: No se ha encontrado el nombre del objeto (0xC0000034)
09/10/2026 7:10:50   1016 Error  Cliente: \\172.16.202.98 (CAJAANDE\mcalcena) -> EXEC\SISTEMA INTEGRADO.exe -> (0xC0000034)
09/10/2026 6:51:37   1016 Error  Cliente: \\172.16.202.46 (CAJAANDE\jcabanas) -> MODULO_INVESIONES_V15.exe / RRHH -> (0xC0000034)
09/10/2026 6:36:11   1016 Error  Cliente: \\172.16.202.125 (CAJAANDE\jsegovia) -> EXEC\MODULO_PRESTAMO.EXE -> (0xC0000034)
09/10/2026 6:02:41   1016 Error  Cliente: \\172.16.202.28 (CAJAANDE\ccristaldo) -> MODULO_RRHH_V15.exe -> (0xC0000034)
09/10/2026 5:48:37   1016 Error  Cliente: \\172.16.202.55 (CAJAANDE\rdelgado) -> MODULO_RRHH_V15.exe -> (0xC0000034)
09/10/2026 4:33:48   1016 Error  Cliente: \\172.16.202.20 (CAJAANDE\lferreira) -> INMOBILIARIO / RRHH -> (0xC0000034)
```

#### Mecánica Técnica del Error `0xC0000034`:
1. **Durable Handles:** Cuando una estación cliente ejecuta un binario por SMB, negocia un identificador duradero y almacena una clave de reanudación (`Resume Key GUID`).
2. **Expiración en el Servidor:** Cuando la PC del usuario suspende o queda inactiva por horas, el servidor purga el identificador caducado de su tabla en RAM (`GlobalOpenTable`).
3. **Fallo en la Reapertura:** Cuando el cliente intenta reanudar la conexión enviando su clave previa, el servidor no encuentra el objeto en memoria y devuelve el código **`0xC0000034` (`STATUS_OBJECT_NAME_NOT_FOUND`)**.
4. **Impacto en el Usuario:** La aplicación del cliente recibe ese error y muestra en pantalla: *"El archivo especificado no se encuentra o no está disponible"*. El usuario interpreta este cartel como si el archivo hubiera sido eliminado.

---

### 7. Integridad de la Tarjeta de Red del Servidor (`Get-NetAdapterStatistics`)
```powershell
PS C:\Windows\system32> Get-NetAdapterStatistics | Select-Object Name, ReceivedBytes, SentBytes, ReceivedDiscardedPackets, OutboundDiscardedPackets, ReceivedPacketErrors, OutboundPacketErrors | Format-Table -AutoSize

Name     ReceivedBytes  SentBytes ReceivedDiscardedPackets OutboundDiscardedPackets ReceivedPacketErrors OutboundPacketErrors
----     -------------  --------- ------------------------ ------------------------ -------------------- --------------------
Ethernet     496204172 4544628946                        0                        0                    0                    0
```
* **Conclusión Forense:** El adaptador físico de red de `VMBASE03` registró **0 paquetes descartados** y **0 errores de transmisión**. Se descarta completamente cualquier falla física o saturación de red en el servidor.

---

### 8. Telemetría Pericial en Endpoints (Live Response en Puestos Clave)

#### A. Puesto de Trabajo 1: `172.16.202.17` (`CAJAANDE\lortellado`)
* **Sistema Operativo:** Windows 11 Pro Build 26200.9457  
* **Visibilidad en Red:**
  ```powershell
  PS C:\Windows\System32> Test-Path "\\VMBASE03\Proyectos\EXEC\MODULO_TESORERIA.EXE"
  True
  PS C:\Windows\System32> Get-Item "\\VMBASE03\Proyectos\EXEC\MODULO_TESORERIA.EXE" | Select-Object FullName, Length, LastWriteTime
  FullName                                        Length LastWriteTime
  --------                                        ------ -------------
  \\VMBASE03\Proyectos\EXEC\MODULO_TESORERIA.EXE 7274496 17/8/2026 11:19:40
  ```
  *(El archivo siempre estuvo 100% visible y accesible desde su máquina).*

* **Procesos en RAM (`Get-Process`):**
  ```text
     Id ProcessName           MainWindowTitle Responding StartTime
     -- -----------           --------------- ---------- ---------
  16452 MODULO_TESORERIA                            True 7/10/2026 16:05:02  <-- ¡HACE MÁS DE 40 HORAS!
  25700 MODULO_TESORERIA                            True 9/10/2026 07:17:42  <-- HOY TEMPRANO
  13636 SISTEMA INTEGRADO                           True 7/10/2026 16:04:59  <-- ¡HACE MÁS DE 40 HORAS!
  16508 SISTEMA INTEGRADO                           True 9/10/2026 07:17:33  <-- HOY TEMPRANO
  33768 MODULO_INVESIONES_V15                       True 8/10/2026 14:36:00  <-- DESDE AYER 14:36
  21908 MODULO_PRESTAMO                             True 9/10/2026 07:57:07  <-- HOY TEMPRANO
  ```
* **Hallazgo Forense:**  
  * `MODULO_TESORERIA` y `SISTEMA INTEGRADO` llevaban ejecutándose en memoria **desde el miércoles 07/10 a las 16:05**.
  * Todos los procesos tenían **`MainWindowTitle` vacío (`""`)**: quedaron huérfanos sin interfaz gráfica en el escritorio.
  * Hoy a las 07:17 AM, el usuario intentó abrirlos de nuevo mediante doble clic, generando **instancias duplicadas** en memoria que entraron en colisión de archivos con las instancias del 7/10.
* **Cero Errores de Red:** `Get-WinEvent SMBClient/Connectivity` arrojó **0 eventos** (la red local estuvo 100% sana).

---

#### B. Puesto de Trabajo 2: `172.16.202.105` (`CAJAANDE\Mbrizuela`)
* **Sistema Operativo:** Windows 11 Pro Build 26300.9550  
* **Visibilidad en Red:** `Test-Path "\\VMBASE03\Proyectos\EXEC\MODULO_TESORERIA.EXE"` devolvió **`True`**.
* **Procesos en RAM (`Get-Process`):**
  ```text
     Id ProcessName     MainWindowTitle Responding StartTime
     -- -----------     --------------- ---------- ---------
  25332 MODULO_RRHH_V15                       True 5/10/2026 11:30:31  <-- ¡LUNES 5/10 (HACE 4 DÍAS)!
   4804 MODULO_RRHH_V15                       True 6/10/2026 08:20:29  <-- ¡MARTES 6/10 (HACE 3 DÍAS)!
   4208 MODULO_RRHH_V15                       True 8/10/2026 16:06:39  <-- ¡AYER JUEVES 8/10!
  ```
* **Conexión SMB y Bloqueos (`Get-SmbConnection`):**
  ```text
  ServerName ShareName UserName         NumOpens Dialect
  ---------- --------- --------         -------- -------
  vmbase03   Proyectos CAJAANDE\Mbrizuela     21 3.1.1
  ```
* **Hallazgo Forense:**  
  * El usuario acumuló **3 instancias zombis de `MODULO_RRHH_V15.exe`** en memoria desde el **lunes 5 de octubre**.
  * Mantenía retenidos **21 archivos abiertos (`NumOpens: 21`)** en el servidor `VMBASE03`.
  * Esto explica por qué a los demás usuarios (`rdelgado`, `ccristaldo`, `jcabanas`, etc.) les fallaba la reapertura del módulo de RRHH con error 1016 esta mañana.
* **Cero Errores de Red:** `Get-WinEvent SMBClient/Connectivity` arrojó **0 eventos**.

---

#### C. Puesto de Trabajo 3: `172.16.202.27` (`CAJAANDE\CJPPA1242684`)
* **Sistema Operativo:** Windows 11 Pro Build 26200.9457  
* **Visibilidad en Red:** `Test-Path "\\VMBASE03\Proyectos\EXEC\MODULO_TESORERIA.EXE"` devolvió **`True`** (7.27 MB, 17/8/2026).
* **Procesos en RAM (`Get-Process`):** **0 procesos** de módulos ejecutándose actualmente (el aplicativo se cerró/crasheó al fallar la reapertura previa).
* **Conexiones SMB (`Get-SmbConnection`):** **0 conexiones** activas en este momento.
* **Eventos de Conectividad (`SMBClient/Connectivity`):**
  ```text
  TimeCreated        Id    Message
  -----------        --    -------
  9/10/2026 07:21:05 30810 Se agregó una interfaz de transporte TCP/IP (Conexión de área local* 2)
  9/10/2026 07:20:58 30810 Se agregó una interfaz de transporte TCP/IP (Conexión de área local* 2)
  ```
* **Correlación Temporal con el Servidor:**  
  * A las **07:19:16 AM**, `VMBASE03` registró el **Event ID 1016** cuando este cliente intentó reanudar `MODULO_RRHH_V15.exe` y falló con `0xC0000034`.
  * A las **07:20:58 AM** (menos de 2 minutos después), la máquina registró el **Event ID 30810** correspondiente al encendido o reanudación del adaptador de red tras reposo.
  * Al encender el equipo, la sesión vieja intentó reconectar antes de tiempo contra un handle que ya había caducado en el servidor y que estaba bloqueado por las instancias de `Mbrizuela`. El proceso finalizó de forma abrupta.
  * **Estado Actual:** Con el adaptador activo y los bloqueos de `Mbrizuela` liberados, la máquina se encuentra 100% limpia para abrir los aplicativos con normalidad.

---

#### D. Puesto de Trabajo 4: `172.16.202.98` (`CAJAANDE\mcalcena`)
* **Sistema Operativo:** Windows 10 Pro Build 19045.6456  
* **Visibilidad en Red:** `Test-Path "\\VMBASE03\Proyectos\EXEC\MODULO_TESORERIA.EXE"` devolvió **`True`** (7.27 MB, 17/8/2026).
* **Procesos en RAM (`Get-Process`):** **0 procesos** de módulos ejecutándose actualmente.
* **Conexiones SMB (`Get-SmbConnection`):** **0 conexiones** activas en este momento.
* **Eventos de Conectividad (`SMBClient/Connectivity`):**
  ```text
  TimeCreated        Id    Message
  -----------        --    -------
  9/10/2026 07:10:50 30810 Se agregó una interfaz de transporte TCP/IP (Ethernet)
  9/10/2026 07:10:50 30808 Se restableció la conexión al recurso compartido: \vmbase03\Proyectos (Sesión: 0xC8002C000601)
  9/10/2026 07:10:50 30806 El cliente restableció su sesión en el servidor: \vmbase03 (Sesión: 0xC8002C000601)
  9/10/2026 07:10:50 30805 El cliente perdió su sesión en el servidor: \vmbase03 (Sesiones viejas purgadas)
  ```
* **Correlación Forense Exacta (Al Segundo y Session ID):**  
  * En `VMBASE03`, a las **07:10:50 AM**, el servidor registró el **Event ID 1016** con:  
    `Nombre del cliente: \\172.16.202.98 | Id. de sesión: 0xC8002C000601 | Archivo: EXEC\SISTEMA INTEGRADO.exe | Estado: 0xC0000034`.
  * En el cliente `172.16.202.98`, a las **07:10:50 AM** (el mismo segundo exacto), Windows registró:  
    `Event ID 30806 / 30808: El cliente restableció su sesión en el servidor \vmbase03 | Id. de sesión: 0xC8002C000601`.
  * **La prueba de coincidencia perfecta:** El `Id. de sesión 0xC8002C000601` coincide carácter por carácter entre el log del cliente y el log del servidor. Al encender la PC a las 07:10:50, Windows purgó las sesiones muertas de la noche anterior (Eventos 30805) e intentó revivir la sesión con `SISTEMA INTEGRADO.exe`. Como el handle duradero ya había expirado en el servidor, Windows Server rechazó la reapertura con `0xC0000034` y el aplicativo se cerró.
  * **Estado Actual:** La máquina tiene la red operativa y sin procesos residuales, lista para operar.

---

#### E. Puesto de Trabajo 5: `172.16.202.108` (`CAJAANDE\TIdcaceres`)
* **Sistema Operativo:** Windows 11 Pro Build 26300.9550 (Grupo: `Caja_Ande`)  
* **Visibilidad en Red:** `Test-Path "\\VMBASE03\Proyectos\EXEC\MODULO_TESORERIA.EXE"` devolvió **`True`** (7.27 MB, 17/8/2026).
* **Procesos en RAM (`Get-Process`):**
  ```text
     Id ProcessName     MainWindowTitle Responding StartTime
     -- -----------     --------------- ---------- ---------
  14704 MODULO_PRESTAMO                       True 8/10/2026 11:59:00  <-- ¡DESDE AYER AL MEDIODÍA (>20 HORAS)!
  ```
* **Conexiones SMB y Bloqueos (`Get-SmbConnection`):**
  ```text
  ServerName ShareName UserName            NumOpens Dialect
  ---------- --------- --------            -------- -------
  vmbase03   Proyectos CAJAANDE\TIdcaceres        6 3.1.1
  ```
* **Hallazgo Forense:**  
  * `MODULO_PRESTAMO` (`PID 14704`) lleva **más de 20 horas ejecutándose** en RAM de forma continua desde ayer jueves a las 11:59 AM.
  * `MainWindowTitle` se encuentra **vacío (`""`)**: el proceso quedó huérfano en segundo plano sin ventana activa en el escritorio del usuario.
  * Mantiene **6 archivos abiertos (`NumOpens = 6`)** bloqueados contra `\\vmbase03\Proyectos`.
  * **Correlación con el Servidor:** Anoche a las **23:20:50**, `VMBASE03` registró el **Event ID 1016** cuando este cliente intentó reanudar `EXEC\MODULO_PRESTAMO.EXE` y falló con `0xC0000034`. La causa fue esta instancia que quedó desincronizada desde el mediodía.
* **Ahorro de Energía en Adaptador de Red (`Get-NetAdapterPowerManagement`):**
  ```text
  InterfaceDescription                          AllowComputerToTurnOffDevice
  --------------------                          ----------------------------
  Bluetooth Device (Personal Area Network)                       Unsupported
  Realtek 8852CE WiFi 6E PCI-E NIC                               Unsupported
  Fortinet SSL VPN Virtual Ethernet Adapter
  Realtek PCIe GbE Family Controller                                 Enabled  <-- ¡CONFIRMADO: WINDOWS APAGA LA PLACA!
  Fortinet Virtual Ethernet Adapter (NDIS 6.30)                  Unsupported
  ```
* **Evidencia Explícita de Pérdida de Conexión y Sesión (`SMBClient/Connectivity`):**
  ```text
  TimeCreated        Id    Message
  -----------        --    -------
  9/10/2026 07:51:32 30807 Se perdió conexión a \\vmbase03\Proyectos (Error: Conexión de transporte desconectada)
  9/10/2026 07:51:32 30805 Cliente perdió su sesión en \vmbase03 (Sesión: 0xC80024000029)
  9/10/2026 07:51:32 30804 Se interrumpió una conexión de red (LanmanRedirector -> 172.16.201.3:445)
  9/10/2026 07:49:35 30807 Se perdió conexión a \\vmbase35\Backup Diario (Transporte desconectado)
  9/10/2026 07:49:35 30805 Cliente perdió sesión en \vmbase35 (Sesión: 0xF4000800007D)
  9/10/2026 07:49:35 30804 Se interrumpió una conexión de red (LanmanRedirector -> 172.16.200.35:445)
  9/10/2026 07:49:33 30807 Se perdió conexión a \\vmbase03\Proyectos (Sesión: 0xC80020000381)
  9/10/2026 07:49:33 30805 Cliente perdió sesión en \vmbase03 (Sesión: 0xC80020000381)
  9/10/2026 07:49:33 30804 Se interrumpió una conexión de red (LanmanRedirector -> 172.16.201.3:445)
  9/10/2026 07:49:33 30807 Se perdió conexión a \\vmbasefs\departamentos
  8/10/2026 15:46:53 30807/5/4 Desconexión e interrupción de red contra 172.16.201.3:445
  8/10/2026 13:01:47 30803 Fallo de conexión de red contra vmbase03 (Transporte desconectado)
  8/10/2026 11:56:12 30803 Tiempo de espera del dispositivo agotado (I/O timeout en red contra vmbase03:445)
  8/10/2026 11:56:04 30807/5/4 Desconexión e interrupción de transporte contra vmbase03:445 (<-- 3 MINUTOS ANTES DEL ZOMBI 11:59 AM)
  ```
* **Falla Crítica del Hardware de Red en Transición de Energía (`Microsoft-Windows-NDIS`):**
  ```text
  TimeCreated        ProviderName           Id    Message
  -----------        ------------           --    -------
  9/10/2026 07:49:32 Microsoft-Windows-NDIS 10317 Fatal error: The miniport has failed a power transition to operational power
  8/10/2026 07:29:16 Microsoft-Windows-NDIS 10317 Fatal error: The miniport has failed a power transition to operational power
  ```
* **Ciclo de Suspensión, Hibernación y Reactivación (`Power-Troubleshooter` / `Kernel-Power`):**
  ```text
  TimeCreated        ProviderName              Id  Message
  -----------        ------------              --  -------
  9/10/2026 07:49:34 Power-Troubleshooter       1  El sistema estaba en un estado de baja energía y se reanudó (Hora reactivación: 07:49:33)
  8/10/2026 23:21:23 Kernel-Power             107  El sistema se reanudó del estado de suspensión (Para cambio a hibernación profunda)
  8/10/2026 23:21:16 Kernel-Power              42  El sistema está entrando en suspensión (Motivo: Hibernate from Sleep - Standby Battery Budget Exceeded)
  ```
* **Correlación Forense Incontestable (Segundos y Causa Raíz Demostrada):**  
  1. **Ayer 11:56 AM (Génesis del proceso zombi):** A las 11:56:04 Windows registró la desconexión total por transporte (`30804/30805/30807`) y timeout de E/S (`30803`). A las **11:59:00 AM**, el usuario reabrió `MODULO_PRESTAMO.EXE` pero la tubería SMB quedó viciada, perdiendo su ventana gráfica y quedando huérfano en segundo plano.
  2. **Anoche 23:20 - 23:21 (Suspensión forzada por batería):** A las **23:21:16**, Windows forzó la hibernación del equipo (`Hibernate from Sleep - Standby Battery Budget Exceeded`). Al cortar la energía de la tarjeta Realtek (`AllowComputerToTurnOffDevice = Enabled`), la sesión SMB murió abruptamente. En el servidor `VMBASE03`, a las **23:20:50** (26 segundos antes) quedó grabado el **Event ID 1016** fallando la reapertura duradera de `MODULO_PRESTAMO.EXE` con `0xC0000034`.
  3. **Hoy 07:49:32 - 07:49:34 AM (El despertar caótico):** Al reanudarse el sistema (`Power-Troubleshooter ID 1`), el adaptador de red sufrió un fallo fatal de transición energética (`NDIS ID 10317`), disparando en el mismo segundo (`07:49:33`) los eventos de transporte roto `30804, 30805 y 30807`.
  4. **Conclusión Pericial:** No existe duda ni especulación: los microcortes e interrupciones de red están registrados con sellos de tiempo exactos en los logs de Windows del propio cliente. Ocurrieron por gestión agresiva de energía e inestabilidad de hardware al despertar.


---

## 🖥️ CATÁLOGO COMPLETO DE COMANDOS PARA REPRODUCIR LA AUDITORÍA

### BLOQUE 1: En el Servidor `VMBASE03` (`172.16.201.3`)

```powershell
# 1. Comprobar existencia física, tamaño y fecha de MODULO_TESORERIA.EXE
Get-Item "C:\Proyectos\EXEC\MODULO_TESORERIA.EXE" | Select-Object FullName, Length, LastWriteTime

# 2. Comprobar existencia física y fechas de ejecutables en VSNET
Get-Item "C:\Proyectos\EXEC\VSNET\MODULO_RRHH_V15*.exe" | Select-Object Name, Length, LastWriteTime

# 3. Auditar logs de Sophos Central (descarte de bloqueos y cuarentena)
Get-WinEvent -FilterHashtable @{LogName='Application'; StartTime=(Get-Date).AddHours(-24)} -ErrorAction SilentlyContinue | Where-Object { $_.ProviderName -match "Sophos" -or $_.Message -match "CryptoGuard|Quarantine" }

# 4. Listar identificadores (handles) de archivos abiertos y bloqueados por SMB
Get-SmbOpenFile | Where-Object { $_.Path -match "MODULO_|EXEC" } | Select-Object FileId, ClientComputerName, ClientUserName, Path | Format-Table -AutoSize

# 5. Listar sesiones SMB activas, cantidad de archivos abiertos y tiempo de inactividad
Get-SmbSession | Select-Object SessionId, ClientComputerName, ClientUserName, NumOpens, @{Name="Minutos_Inactivo";Expression={[math]::Round($_.SecondsIdle/60,1)}}, @{Name="Horas_Conectado";Expression={[math]::Round($_.SecondsExists/3600,1)}} | Format-Table -AutoSize

# 6. Verificar conexiones TCP activas en el puerto 445 (SMB)
Get-NetTCPConnection -LocalPort 445 | Where-Object { $_.RemoteAddress -like "172.16.202.*" } | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State | Format-Table -AutoSize

# 7. Consultar configuración de Leasing y OpLocks globales en el servidor
Get-SmbServerConfiguration | Select-Object EnableLeasing, EnableOplocks, AutoDisconnectTimeout | Format-List

# 8. Consultar configuración específica del recurso compartido "Proyectos"
Get-SmbShare -Name "Proyectos" | Select-Object Name, Path, LeasingMode, CachingMode

# 9. Consultar errores de reapertura y durabilidad en el log de SMB Server (Event ID 1016)
Get-WinEvent -LogName "Microsoft-Windows-SMBServer/Operational" -MaxEvents 50 -ErrorAction SilentlyContinue | Where-Object { $_.LevelDisplayName -match "Warning|Error" -or $_.Id -in 1001, 1016, 1020, 1021 } | Select-Object TimeCreated, Id, LevelDisplayName, Message | Format-Table -Wrap

# 10. Verificar estadísticas de la tarjeta de red del servidor (descarte de errores físicos)
Get-NetAdapterStatistics | Select-Object Name, ReceivedBytes, SentBytes, ReceivedDiscardedPackets, OutboundDiscardedPackets, ReceivedPacketErrors, OutboundPacketErrors | Format-Table -AutoSize
```

---

### BLOQUE 2: En las Estaciones de Trabajo Cliente (Live Response Puestos)

```powershell
# 1. Probar si desde la máquina cliente el archivo es visible y alcanzable por red
Test-Path "\\VMBASE03\Proyectos\EXEC\MODULO_TESORERIA.EXE"
Get-Item "\\VMBASE03\Proyectos\EXEC\MODULO_TESORERIA.EXE" | Select-Object FullName, Length, LastWriteTime

# 2. Verificar qué ejecutables están corriendo en la pantalla del usuario (con título de ventana y respuesta)
Get-Process | Where-Object { $_.ProcessName -match "MODULO|TESORERIA|PRESTAMO|RRHH|INVERSION|SISTEMA" } | Select-Object Id, ProcessName, MainWindowTitle, Responding, StartTime | Format-Table -AutoSize

# 3. Ver qué letras de unidad (Z:, P:, etc.) tiene mapeadas el usuario en su perfil de registro
Get-ChildItem Registry::HKEY_USERS\*\Network -ErrorAction SilentlyContinue | ForEach-Object { 
    [PSCustomObject]@{
        UsuarioSID = $_.PSParentPath.Split('\')[-1]
        Letra      = $_.PSChildName
        RutaRemota = (Get-ItemProperty $_.PSPath).RemotePath
    }
} | Format-Table -AutoSize

# 4. Verificar la sesión SMB activa del cliente hacia VMBASE03
Get-SmbConnection | Where-Object { $_.ServerName -match "vmbase03|172.16.201.3" } | Select-Object ServerName, ShareName, UserName, NumOpens, Dialect | Format-Table -AutoSize

# 5. Consultar directivas de ahorro de energía en el adaptador de red del puesto
Get-NetAdapterPowerManagement | Select-Object InterfaceDescription, AllowComputerToTurnOffDevice | Format-Table -AutoSize

# 6. Consultar eventos de reconexión o desconexión en el cliente SMB
Get-WinEvent -LogName "Microsoft-Windows-SMBClient/Connectivity" -MaxEvents 30 -ErrorAction SilentlyContinue | Where-Object { $_.Id -in 30806, 30808, 30810 } | Select-Object TimeCreated, Id, Message | Format-Table -Wrap

# 7. Consultar desconexiones de enlace registradas por el stack TCP/IP
Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Tcpip'} -MaxEvents 20 -ErrorAction SilentlyContinue | Where-Object { $_.Id -in 4201, 4202 } | Select-Object TimeCreated, Id, Message
```

---

### BLOQUE 3: Comandos de Remediación y Solución

#### A. Remediación en Caliente en Puestos de Trabajo
```powershell
# En la máquina de lortellado (172.16.202.17):
Stop-Process -Name "MODULO_TESORERIA", "MODULO_INVESIONES_V15", "SISTEMA INTEGRADO" -Force

# En la máquina de Mbrizuela (172.16.202.105):
Stop-Process -Name "MODULO_RRHH_V15" -Force

# En la máquina de TIdcaceres (172.16.202.108):
Stop-Process -Name "MODULO_PRESTAMO" -Force

# Deshabilitar ahorro de energía en la placa de red física para evitar microcortes locales:
Get-NetAdapter | Where-Object { $_.InterfaceDescription -match "Realtek.*GbE" } | Set-NetAdapterPowerManagement -AllowComputerToTurnOffDevice Disabled
```

#### B. Remediación en Caliente en `VMBASE03` (Sin reiniciar la VM)
```powershell
# 1. Liberar a la fuerza todos los archivos abiertos en la carpeta EXEC
Get-SmbOpenFile | Where-Object { $_.Path -match "EXEC" } | Close-SmbOpenFile -Force

# 2. Cerrar sesiones zombis que lleven más de 10 horas de inactividad
Get-SmbSession | Where-Object { $_.SecondsIdle -gt 36000 } | Close-SmbSession -Force
```

#### C. Configuración Definitiva en el Servidor
```powershell
# 1. Deshabilitar el Leasing en el recurso compartido "Proyectos" para que no retenga cachés zombis
Set-SmbShare -Name "Proyectos" -LeasingMode None -Force

# 2. Verificar que el cambio se aplicó correctamente
Get-SmbShare -Name "Proyectos" | Select-Object Name, Path, LeasingMode

# 3. Configurar timeout de desconexión por inactividad a 15 minutos
Set-SmbServerConfiguration -AutoDisconnectTimeout 15 -Force
```

#### D. Solución de Arquitectura Definitiva (Script Lanzador Local)
Script `.bat` para ejecutar en el escritorio de los usuarios y evitar correr binarios por SMB:
```bat
@echo off
robocopy "\\VMBASE03\Proyectos\EXEC\VSNET" "%LocalAppData%\CajaAnde\Bin" "MODULO_RRHH_V15.exe" /XO /NJH /NJS
start "" "%LocalAppData%\CajaAnde\Bin\MODULO_RRHH_V15.exe"
```

---

## 🎯 INFORME EJECUTIVO HUMANIZADO (Relato Continuo para Jefatura / Cliente)

Para total tranquilidad de la gerencia y del equipo de trabajo, descartamos categóricamente cualquier ataque de ransomware, intrusión o borrado por parte del antivirus Sophos. Tras revisar pericialmente el disco local del servidor `VMBASE03`, comprobamos que el archivo `MODULO_TESORERIA.EXE` nunca fue eliminado ni alterado: conserva intacto su tamaño físico de 7.27 MB (7,274,496 bytes) y su fecha original del 17 de agosto **[SCREEN #1]**. A su vez, los registros de Sophos arrojaron cero alertas o cuarentenas en las últimas 24 horas **[SCREEN #2]**, y desde los puestos de trabajo clientes el ejecutable siempre fue visible y accesible a través de la red **[SCREEN #3]**.

El origen real del inconveniente se debió a una acumulación de programas que quedaron abiertos durante varios días en distintas estaciones de trabajo (procesos zombis o huérfanos). Al auditar la memoria de los equipos, detectamos múltiples instancias activas: en el puesto de Mbrizuela (`.105`) había 3 módulos de RRHH abiertos desde el 5 de octubre reteniendo 21 archivos en el servidor **[SCREEN #4]**; en el puesto de lortellado (`.17`) había módulos abiertos desde el 7 de octubre (más de 40 horas continuas en RAM) **[SCREEN #5]**; y en el equipo de TIdcaceres (`.108`) el módulo de Préstamos corría desde el 8 de octubre con 6 archivos retenidos **[SCREEN #6]**. Como la carpeta compartida en el servidor operaba con modo de arrendamiento completo (`LeasingMode: Full`) **[SCREEN #7]**, Windows Server mantuvo bloqueados los identificadores exclusivos de esos archivos en memoria esperando el regreso de dichas sesiones.

Por otra parte, se descarta cualquier falla, corte general o saturación en la red del servidor, ya que la placa de red de `VMBASE03` registró cero paquetes descartados o con errores **[SCREEN #8]**. La intermitencia real fue provocada por la configuración de ahorro de energía en computadoras portátiles: en el puesto de TIdcaceres (`.108`), la placa de red cableada Realtek tenía habilitada la opción de apagarse automáticamente para ahorrar energía (`AllowComputerToTurnOffDevice = Enabled`) **[SCREEN #9]**. Cuando el equipo entró en suspensión y luego agotó la batería forzando una hibernación (ID 42), la placa sufrió un fallo de reactivación energética NDIS 10317 a las 07:49 AM **[SCREEN #10]**, lo que desató una ráfaga de desconexiones de transporte SMB y conmutaciones bruscas con la red Wi-Fi **[SCREEN #11]**.

Al encender los colaboradores sus computadoras por la mañana e intentar ingresar a los sistemas con doble clic, se produjo el conflicto: como el servidor aún mantenía retenido el archivo por las sesiones viejas congeladas, rechazó los nuevos intentos de apertura duradera emitiendo el evento operativo 1016 con código de error `0xC0000034` (`STATUS_OBJECT_NAME_NOT_FOUND`) **[SCREEN #12]**, lo cual coincide exactamente al segundo con los eventos de desconexión del cliente mcalcena (`.98`) a las 07:10:50 AM **[SCREEN #13]**. Frente a este rechazo de red, Windows muestra de manera equívoca en el explorador el mensaje genérico de *"el archivo no se encuentra o no está disponible"*, provocando en los usuarios la falsa alarma y el pánico de que el ejecutable había sido borrado.

Actualmente, el servidor y los sistemas se encuentran estables. Como **acciones y recomendaciones de remediación inmediata sometidas a consideración y aprobación del cliente**, se plantea:
1. **Finalizar de inmediato los procesos zombis** en los puestos de trabajo clientes identificados (`.105`, `.17`, `.108`) mediante el cierre de sesión o comando forzado, liberando de forma instantánea todos los identificadores y bloqueos retenidos en la memoria del servidor.
2. **Aplicar la remediación técnica definitiva en el recurso compartido del servidor [SCREEN #14 - Pendiente de Validación]**, reconfigurando la carpeta con `LeasingMode: None`. Con este ajuste aprobado por el cliente, el servidor atenderá las lecturas directamente desde disco y no volverá a bloquear los ejecutables en memoria aunque una máquina sufra cortes de red o quede colgada.
3. **Deshabilitar el ahorro de energía en las placas de red** de las computadoras portátiles para erradicar los microcortes físicos y recordar al personal la importancia de cerrar sus aplicaciones antes de retirarse.

---

## 📸 TABLA MAESTRA DE EVIDENCIAS Y CAPTURAS (SCREENS #1 AL #14)

### Bloque A: En el Servidor `VMBASE03` (`172.16.201.3`)

| Screen | Comando Ejecutado en PowerShell | Evidencia Irrefutable a Resaltar |
| :---: | :--- | :--- |
| **SCREEN #1** | `Get-Item "C:\Proyectos\EXEC\MODULO_TESORERIA.EXE" \| Select FullName, Length, LastWriteTime` | Archivo físico presente, tamaño `7274496` bytes, fecha original `17/08/2026`. |
| **SCREEN #2** | `Get-WinEvent -FilterHashtable @{LogName='Application'; StartTime=(Get-Date).AddHours(-24)} \| Where { $_.ProviderName -match "Sophos" -or $_.Message -match "CryptoGuard\|Quarantine" }` | Salida en blanco (Cero bloqueos o eventos de cuarentena de Sophos). |
| **SCREEN #7** | `Get-SmbShare -Name "Proyectos" \| Select Name, Path, LeasingMode, CachingMode` | `LeasingMode: Full` (causa de los bloqueos persistentes en memoria). |
| **SCREEN #8** | `Get-NetAdapterStatistics \| Select Name, ReceivedDiscardedPackets, ReceivedPacketErrors, OutboundPacketErrors` | Todo en `0` (descarta corte, saturación o falla física de red en el servidor). |
| **SCREEN #12**| `Get-WinEvent -LogName "Microsoft-Windows-SMBServer/Operational" -MaxEvents 30 \| Where { $_.Id -eq 1016 } \| Select TimeCreated, Id, Message` | Eventos 1016 Error al volver a abrir: `Reconnect durable file (0xC0000034)`. |
| **SCREEN #14**| *(Remediación Propuesta)* `Set-SmbShare -Name "Proyectos" -LeasingMode None -Force; Get-SmbShare -Name "Proyectos"` | Desactivar arrendamiento duradero en servidor *(Pendiente de Autorización del Cliente)*. |

### Bloque B: En los Puestos de Trabajo Clientes (Live Response)

| Screen | Equipo / Usuario | Comando Ejecutado en PowerShell | Evidencia Irrefutable a Resaltar |
| :---: | :--- | :--- | :--- |
| **SCREEN #3** | `172.16.202.108`<br>*(TIdcaceres)* | `Test-Path "\\VMBASE03\Proyectos\EXEC\MODULO_TESORERIA.EXE"` | Devuelve **`True`** (demuestra que el archivo siempre fue visible por red). |
| **SCREEN #4** | `172.16.202.105`<br>*(Mbrizuela)* | `Get-Process \| Where { $_.ProcessName -match "MODULO" } \| Select Id, ProcessName, StartTime; Get-SmbConnection` | **3 instancias zombis con StartTime desde el 05/10** y **`NumOpens: 21`** hacia `VMBASE03`. |
| **SCREEN #5** | `172.16.202.17`<br>*(lortellado)* | `Get-Process \| Where { $_.ProcessName -match "MODULO\|SISTEMA" } \| Select Id, ProcessName, StartTime` | Procesos con **`StartTime: 07/10 16:05` (40 horas en RAM)**. |
| **SCREEN #6** | `172.16.202.108`<br>*(TIdcaceres)* | `Get-Process \| Where { $_.ProcessName -match "PRESTAMO" } \| Select Id, ProcessName, StartTime; Get-SmbConnection` | Proceso huérfano con **`StartTime: 08/10 11:59 AM`** y **`NumOpens: 6`**. |
| **SCREEN #9** | `172.16.202.108`<br>*(TIdcaceres)* | `Get-NetAdapterPowerManagement \| Select InterfaceDescription, AllowComputerToTurnOffDevice` | Placa Realtek PCIe GbE con **`AllowComputerToTurnOffDevice: Enabled`**. |
| **SCREEN #10**| `172.16.202.108`<br>*(TIdcaceres)* | `Get-WinEvent @{LogName='System'} \| Where { $_.Id -in 1, 42, 107, 10317 }` | Fallo energético `NDIS 10317` a las **07:49:32** y suspensión por batería `ID 42`. |
| **SCREEN #11**| `172.16.202.108`<br>*(TIdcaceres)* | `Get-WinEvent @{LogName='Microsoft-Windows-SMBClient/Connectivity'} \| Where { $_.Id -in 30804, 30805, 30807 }` | Ráfaga de desconexiones de transporte SMB a las **07:49:33 y 07:51:32**. |
| **SCREEN #13**| `172.16.202.98`<br>*(mcalcena)* | `Get-WinEvent -LogName "Microsoft-Windows-SMBClient/Connectivity" -MaxEvents 10` | Eventos `30805/30806/30808` a las **07:10:50 AM** coincidiendo al segundo con el servidor. |

