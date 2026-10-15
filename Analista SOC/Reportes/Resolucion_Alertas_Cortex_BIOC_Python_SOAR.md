# 📘 Ficha Forense de Resolución: Alertas BIOC por Scripts de Python en Cortex XDR
**Fecha de Registro:** 14 de Octubre de 2026  
**Analista:** Kevin Moraes  
**Estación de Trabajo:** `NB-KMORAEZ` (`TECHNOMA\kevinmoraes`)  
**Plataforma de EDR:** Palo Alto Networks Cortex XDR  
**Clasificación:** Falso Positivo Operacional (Benign True Positive - BTP)  

---

## 1. Resumen de las Alertas Detonadas

Durante las labores de desarrollo, auditoría y ejecución de la suite SOAR (`command_center.py` y `whois_recon.py`), Cortex XDR detonó dos reglas heurísticas de BIOC en la estación del analista:

| Issue ID | Regla BIOC | Categoría | Proceso | Causa Operativa | Veredicto |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **`#150662 - #150679`** | `Scripting engine connected to a rare external host` | Command and Control | `pythonw.exe` | Conexiones HTTPS salientes de la suite SOAR hacia feeds públicos de CTI (CISA, BleepingComputer, Abuse.ch) y servidores autoritativos de WHOIS/RDAP (RIPEstat, ARIN, AFRINIC, APNIC). | **Resolved - False Positive** |
| **`#150711`** | `Delayed Deletion of Files` | Stealth | `python.exe` | Ejecución en línea interactiva desde consola (`python.exe -c "..."`) para consultar el estado del sensor modular (`technoma-sensor`) contra la API REST de Stellar Cyber. | **Resolved - False Positive** |

---

## 2. Diagnóstico Técnico Forense

### 2.1. Causa Raíz de la Detección
1. **Regla `Scripting engine connected to a rare external host`:**
   * Palo Alto Cortex XDR vigila cualquier conexión externa realizada por intérpretes de scripting (`python.exe`, `pythonw.exe`, `powershell.exe`).
   * Al ejecutarse `command_center.py` o `whois_recon.py`, el script realiza llamadas directas a APIs de fuentes de inteligencia y RDAP que tienen baja frecuencia de uso en la red de Technoma (*rare hosts*), activando la regla de sospecha de C2.
2. **Regla `Delayed Deletion of Files / Stealth`:**
   * La ejecución de comandos `python -c "..."` de una sola línea es monitoreada por Cortex porque es un patrón habitual en atacantes (*Living off the Land*) para inyectar código en memoria y borrar rastros en disco.
   * La telemetría corrobora que el comando ejecutado fue una consulta de solo lectura contra `https://technoma.stellarcyber.cloud/connect/api/v1/data_sensor/...` con credenciales legítimas del analista.

### 2.2. Evidencias de Descarte de Amenaza
* **Integridad del Binario:** El ejecutable utilizado corresponde al intérprete de Python 3.12 instalado en la ruta oficial de Microsoft Store (`C:\Users\kevinmoraes\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe`).
* **Sin Persistencia ni Evasión:** No se crearon claves de registro de inicio automático (`Run`/`RunOnce`), no se modificaron sombras de volumen (`vssadmin`), ni se realizaron inyecciones DLL en procesos del sistema.
* **Destinos Benignos Verificados:** Todos los endpoints contactados son plataformas de seguridad internacionalmente reconocidas y servidores de gobernanza de Internet (ICANN/RIRs).

---

## 3. Plantillas de Cierre Oficial (Cortex XDR)

### Para el lote de alertas de Feeds CTI / RDAP (Issue #150664 y similares):
* **Mark This Issue As:** `Resolved - False Positive`
* **Resolution Tag:** `False Positive`
* **Comentario:**
> "Actividad descartada como Falso Positivo. Las conexiones de red originadas por el binario pythonw.exe en el endpoint NB-KMORAEZ corresponden a la ejecución local del entorno SOAR corporativo operado por el analista Kevin Moraes. Los destinos remotos alertados pertenecen a fuentes públicas y oficiales de Threat Intelligence (CISA, BleepingComputer, Abuse.ch) y servidores autoritativos de WHOIS y RDAP (RIPE, ARIN, AFRINIC) consultados legítimamente durante labores de triaje de indicadores de compromiso y enriquecimiento de telemetría. Se descarta actividad C2 y compromiso del activo."

### Para la alerta de ejecución interactiva (Issue #150711):
* **Mark This Issue As:** `Resolved - False Positive`
* **Resolution Tag:** `False Positive`
* **Comentario:**
> "Falso Positivo. La ejecución de python.exe con parámetro en línea (-c) fue originada interactivamente por el analista Kevin Moraes en la estación NB-KMORAEZ durante labores operativas de soporte y diagnóstico de la infraestructura de monitoreo. El código ejecutado realizó una consulta de solo lectura contra la API de Stellar Cyber (https://technoma.stellarcyber.cloud) para validar métricas y perfiles del sensor modular central. Se descarta actividad maliciosa, evasión de defensas o eliminación encubierta de archivos."

---

## 4. Medidas Preventivas y Tuning Recomendado

1. **Alert Tuning en Consola Cortex XDR:**
   * En Cortex XDR, abrir la alerta ➔ `More Actions` ➔ `Create Exception`.
   * Condición: Excluir `Scripting engine connected to a rare external host` para el Host `NB-KMORAEZ` cuando el proceso padre sea `explorer.exe` y la línea de comandos contenga `*soc-env*` o `*SOC_SOAR*`.
2. **Buenas Prácticas de Ejecución:**
   * Evitar el uso de `python -c` interactivo con código largo en la consola; ejecutar scripts guardados en archivos `.py` para evitar la detonación de la regla de `Stealth / Delayed Deletion`.
