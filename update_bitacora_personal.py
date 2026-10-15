import os
import sys

def update_bitacora():
    file_path = r"c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\Bitacora_Personal_Casos_SOC.md"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} no existe.")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Limpiar menciones de Cockpit personal en Caso 018
    old_sec5 = """#### 5. Acciones de Automatizacin SOAR
* [x] Diseada e integrada la clase `DPAPIStorageAutoRemediatorWorker` en `command_center.py` para auto-auditar y auto-cerrar casos 100% puros de DPAPI.
* [x] Aadida la accin `action_soar_dpapi` al men de hiper-automatizacin SOAR (total: 4 auto-cierres + 1 auto-guardia).
* [x] Verificado el compilador de Python sin errores de sintaxis (`py_compile` exit code 0).
* [x] Caso cerrado y documentado en bitcora oficial."""

    # Also check if it was encoded in UTF-8
    old_sec5_utf8 = """#### 5. Acciones de Automatización SOAR
* [x] Diseñada e integrada la clase `DPAPIStorageAutoRemediatorWorker` en `command_center.py` para auto-auditar y auto-cerrar casos 100% puros de DPAPI.
* [x] Añadida la acción `action_soar_dpapi` al menú de hiper-automatización SOAR (total: 4 auto-cierres + 1 auto-guardia).
* [x] Verificado el compilador de Python sin errores de sintaxis (`py_compile` exit code 0).
* [x] Caso cerrado y documentado en bitácora oficial."""

    new_sec5 = """#### 5. Conclusión y Cierre
* [x] Análisis forense completado: descartada extracción ofensiva o abuso de credenciales.
* [x] Causa raíz atribuida al comportamiento legítimo de Windows DPAPI contra el DC.
* [x] Caso cerrado como Falso Positivo (Benign True Positive) en la consola de Stellar Cyber."""

    if old_sec5 in content:
        content = content.replace(old_sec5, new_sec5)
    elif old_sec5_utf8 in content:
        content = content.replace(old_sec5_utf8, new_sec5)

    # 2. Agregar Caso 019 y Caso 020
    nuevos_casos = """

---

### Caso 019 - Investigación Forense Cortex XDR: Carga a Proton Drive (NB-FMORA)
* **ID / Referencia:** Alerta Cortex Magnifier / DLP & Upload Anomaly
* **Fecha:** 15/10/2026 09:15:00
* **Plataforma:** Palo Alto Networks Cortex XDR (Magnifier + Endpoint Agent)
* **Analista:** Kevin Moraes
* **Activo Involucrado:** `NB-FMORA` (Notebook corporativa - Fabio Mora)
* **Destino Remoto:** `fra-storage.proton.me` (`185.205.70.10`, Frankfurt - Proton AG)
* **Volumen:** 10.2 GB (608 sesiones HTTPS / TLS en puerto 443)
* **Veredicto Final:** **Uso No Autorizado de Herramienta Cloud / Sin Fuga de Información Sensible (Benigno)**

#### 1. Contexto y Detección
Cortex XDR Magnifier alertó sobre un volumen inusual de carga de datos (10.2 GB) desde el endpoint `NB-FMORA` hacia la nube de almacenamiento de Proton Drive durante el fin de semana del 12-13 de octubre.

#### 2. Evidencia Forense Recabada (Consultas Cortex XQL)
1. **Actividad de Proceso y Carpeta Local:**
   - La consulta XQL sobre el endpoint confirmó la ejecución de `ProtonDrive.exe` (`C:\\Users\\fabiomora\\AppData\\Local\\Proton\\ProtonDrive\\`).
   - El usuario configuró como carpeta local de sincronización `Downloads\\Mis cosas\\`.
2. **Conciliación de Datos (10.2 GB):**
   - El análisis del sistema de archivos local evidenció imágenes ISO y máquinas virtuales OVA (laboratorios de sistemas operativos para estudio técnico).
   - El peso total de dichos archivos totalizó exactamente 10.2 GB, cuadrando 1 a 1 con la telemetría de red de Magnifier.
3. **Evidencia de Configuración de Cuenta:**
   - Se localizó el archivo `proton-recovery-phrase.pdf` (frase de recuperación generada por Proton al crear la cuenta) depositado el 13/10 a las 06:18 AM en la misma carpeta.
4. **Validación Operativa:**
   - Se verificó con personal de Helpdesk que el usuario se encuentra estudiando activamente para certificaciones técnicas, lo que motivó el respaldo personal de sus laboratorios. No hubo compromiso de credenciales corporativas ni exfiltración de bases de datos/documentos de la empresa.

---

### Caso 020 - Optimización de Cuota Stellar Cyber: Log Filter Quirúrgico FortiGate WiFi
* **ID de Casos Asociados:** Casos #16302 (4.116 alertas) y #12661 (10 alertas)
* **Fecha:** 15/10/2026 09:50:00
* **Plataforma:** Stellar Cyber OpenXDR v7.0.0s / Fortinet FortiGate (`FG-Technoma`)
* **Analista:** Kevin Moraes
* **Tipo de Alerta:** `External Firewall Denial Anomaly` (Etapa Kill Chain: *Initial Attempts*)
* **Activos Involucrados:** Subred WiFi Corporativa (`192.168.169.102`, `192.168.169.131` en `WiFi_Corp`)
* **Veredicto Final:** **Falso Positivo / Ruido Operativo de Firewall (Benigno)**

#### 1. Diagnóstico y Causa Raíz
Dispositivos conectados a la red `WiFi_Corp` intentaban resolver nombres y sincronizar servicios de seguridad hacia resolvers públicos (Google DNS) y la nube de FortiGuard. La política de seguridad del firewall (`Block_WIFI-Corp`, ID 214) denegó estas salidas, generando miles de logs de descarte (`action: deny`) que saturaron la ingesta de Stellar Cyber e inflaron la cuota diaria (caso 16302 con más de 4.100 eventos).

#### 2. Implementación de Mitigación Quirúrgica (Sin Puntos Ciegos)
Para erradicar el ruido masivo sin generar cegueras ante posibles amenazas reales (DNS Tunneling o C2 saliente), se implementó un filtro de ingesta condicional estricto:
* **Filtro Creado:** `DROP-FG-Technoma-WIFI_Corp-Known-Public-DNS`
* **Ruta en Consola:** `System` → `Log Forwarders` (Log Filters)
* **Condiciones Aplicadas:**
  - `fw_policy_id` **is** `FG-Technoma_214`
  - `dstport` **is** `53, 853, 443` (DNS clásico, DNS-over-TLS y HTTPS FortiGuard)
  - `dstip` **matches** `96.45.46.46, 96.45.45.45, 173.243.140.18, 173.243.132.25, 173.243.143.6, 141.109.161.95, 8.8.8.8, 8.8.4.4` (Resolvers oficiales benignos)
  - `action` **is** `deny`
  - **Acción:** `DROP`

#### 3. Impacto Operativo
* Se neutraliza la generación de casos falsos masivos derivados de la política WiFi corporativa.
* Se preserva el almacenamiento diario de la licencia Stellar Cyber.
* Se garantiza visibilidad total: cualquier intento de conexión hacia IPs no listadas (malware, C2) sigue siendo capturado y alertado con normalidad.
"""

    content += nuevos_casos

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("[+] Bitácora personal actualizada exitosamente con Caso 019 y Caso 020.")
    return True

if __name__ == "__main__":
    update_bitacora()
