# Playbook de Troubleshooting: Sophos AutoUpdate

Este documento unifica las directrices oficiales de Sophos (KBA-000006284 y KBA-000004473) junto con la experiencia en campo del SOC para resolver problemas críticos con el servicio de actualizaciones de Sophos Endpoint en Windows.

---

## Escenario 1: El Servicio `Sophos AutoUpdate Service` NO EXISTE (Missing)
*Síntoma: El servicio desapareció por completo de `services.msc` o PowerShell (`Get-Service`) luego de un fallo de caché, corrupción de WMI o actualización fallida.*

### Resolución Rápida (Sin Reinicio ni Descarga)
Si la carpeta de caché no ha sido eliminada por completo, es posible recuperar el servicio inyectando el instalador MSI local que Sophos guarda como respaldo.

1. Abre una consola de PowerShell con privilegios de Administrador.
2. Verifica si el archivo `.msi` de rescate existe ejecutando:
   ```powershell
   Get-ChildItem -Path 'C:\ProgramData\Sophos\' -Filter 'Sophos AutoUpdate.msi' -Recurse -ErrorAction SilentlyContinue | Select-Object FullName
   ```
3. Si el archivo **existe**, navega a su ubicación (usualmente `C:\ProgramData\Sophos\AutoUpdate\Cache\decoded\sau`).
4. Ejecuta el archivo para reinstalar el servicio de forma silenciosa:
   ```cmd
   msiexec.exe /i "C:\ProgramData\Sophos\AutoUpdate\Cache\decoded\sau\Sophos AutoUpdate.msi" /qn
   ```
5. Abre la interfaz de Sophos (`C:\Program Files\Sophos\Sophos UI\Sophos UI.exe`), ve a *Acerca de* y presiona **Actualizar Ahora**.
   *Nota: Si el `.msi` no existe (ej. porque se vació la carpeta Cache manualmente), se deberá ejecutar el instalador general `SophosSetup.exe`.*

---

## Escenario 2: El Servicio Existe pero NO Actualiza (Amber Status)
*Síntoma: Endpoint Self Help muestra estado "Amber" (Alerta) en actualizaciones, la red funciona correctamente y el servicio de AutoUpdate está corriendo.*

### Resolución: Limpieza de Caché y Forzado de Actualización
Sigue estos pasos para purgar las carpetas corruptas y forzar a Sophos a descargar las firmas nuevamente.

1. Abre una línea de comandos (CMD) como Administrador.
2. Desactiva temporalmente el actualizador por CLI:
   ```cmd
   cd "C:\Program Files\Sophos\AutoUpdate"
   SAUcli.exe DisableUpdates
   ```
   *(En plataformas legacy, en lugar del comando anterior, detén el servicio: `net stop "Sophos AutoUpdate Service"`)*
3. Renombra las carpetas de caché corruptas para que Sophos cree nuevas:
   * `C:\ProgramData\Sophos\AutoUpdate\Cache\decoded` ➡️ renombrar a `decoded_old`
   * `C:\ProgramData\Sophos\AutoUpdate\data\repo` ➡️ renombrar a `repo_old`
4. Elimina el archivo de estado de actualización local:
   * Borrar: `C:\ProgramData\Sophos\AutoUpdate\data\status\SophosUpdateStatus.xml`
5. Vuelve a encender el actualizador:
   ```cmd
   SAUcli.exe EnableUpdates
   ```
   *(En plataformas legacy, arranca el servicio: `net start "Sophos AutoUpdate Service"`)*
6. Abre la interfaz de usuario de Sophos Endpoint, ve a *Acerca de* y haz clic en **Actualizar Ahora**.

> [!WARNING]
> **Aviso de Reinicio:** Completar estos pasos de purga de caché usualmente generará una alerta de **Reinicio Pendiente** en el Endpoint una vez que la actualización termine de inyectar los nuevos archivos descargados.

---
*Documento mantenido por el Equipo SOC.*

### Advertencia: Plataformas Modernas (Windows 10+)
En equipos modernos, el archivo .msi no existe. Si intentas ejecutar su-setup64.exe desde la cache, fallara con el error GetMultistringValue(SetupArgs) failed. No pierdas tiempo intentando instalarlo manualmente. Para Windows 10+, la unica solucion para un servicio faltante es desplegar el instalador maestro (SophosSetup.exe) sobre la instalacion existente de forma silenciosa.
