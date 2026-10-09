# Informe Ejecutivo y Técnico de Casos Analizados: Palo Alto Cortex XDR
**Área:** Centro de Operaciones de Seguridad (SOC) — Technoma S.A.E.C.A.  
**Elaborado por:** Analista SOC (Kevin Moraes)  
**Destinatario:** SOC Manager / Jefatura de Ciberseguridad  
**Estado:** Documento en construcción continua (Casos recopilados de la consola Cortex XDR)

---

## Metodología Estándar de Investigación SOC (Cortex XDR)
Para cada uno de los incidentes gestionados en la consola de Palo Alto Cortex XDR, el equipo de analistas ejecuta el siguiente procedimiento de 5 etapas:

1. **Triaje y Extracción de Telemetría (JSON / XQL):** Extracción de los metadatos completos del caso, identificando el ID de incidente, severidad, módulo causante (BIOC, BTP, Analytics) y marca de tiempo exacta.
2. **Análisis de Causalidad y Linaje de Procesos (Process Tree):** Identificación del proceso actor (*causality actor*), proceso padre (PPID) y subprocesos hijos, validando líneas de comando (`cmdline`), hashes SHA256 y estado de firma digital (*Signed / Unsigned* / Vendor).
3. **Inspección de Artefactos y Rutas de Archivo:** Análisis del archivo objetivo o recurso accedido (carpetas de sistema, registros, bibliotecas DLL o scripts en `%TEMP%` / `%APPDATA%`).
4. **Verificación de Contexto Operativo y Threat Intel:** Cruce de indicadores con fuentes oficiales (Microsoft, WildFire, bases de datos de vulnerabilidades, listas de políticas CI/WDAC o feeds de reputación).
5. **Determinación del Veredicto y Cierre:** Clasificación formal (*False Positive*, *True Positive / Benign*, *Malicious*) y redacción de la justificación técnica para el cliente o auditoría.

---

## Registro Consolidado de Casos

### Caso 1: Case #412 — Protección contra Evasión de Medidas de Seguridad (CI Policy WDAC)

* **ID de Caso:** Case #412  
* **Alerta / Issue:** `Protection Against Security Measures Bypass Techniques - 347087060`  
* **Sub-clasificación:** `Unauthorized user set CI policy`  
* **Fecha del Evento:** 8 de mayo de 2026, 15:24:00 UTC  
* **Equipo Afectado (Host):** `nb-jtorales`  
* **Usuario:** `SYSTEM`  
* **Procesos Involucrados:** `svchost.exe` ➔ `AggregatorHost.exe` (SHA256: `681b...7f61`)  
* **Ruta del Artefacto Afectado:**  
  `C:\windows\system32\codeintegrity\cipolicies\staged\{8f9cb695-5d48-48d6-a329-7202b44607e3}.cip`  
* **Mapeo MITRE ATT&CK:** Táctica `TA0005 - Stealth / Defense Evasion` | Técnica `T1562 - Impair Defenses`

#### Veredicto:
**Falso Positivo (False Positive / Benign System Activity)**

#### Pasos de Investigación Seguidos:
1. **Extracción del registro JSON y consulta XQL:** Se extrajeron los eventos de endpoint asociados a la alerta `347087060` en el host `nb-jtorales`.
2. **Validación de Causalidad y Firmas:** Se comprobó que el proceso padre era el servicio nativo de Windows `svchost.exe`, el cual invocó a `AggregatorHost.exe`. Ambos ejecutables se ejecutaron bajo el contexto privilegiado de `NT AUTHORITY\SYSTEM` y cuentan con firma digital legítima y verificada de **Microsoft Corporation**.
3. **Identificación de la Política y GUID:** Se inspeccionó la ruta de modificación `C:\windows\system32\codeintegrity\cipolicies\staged\` y se investigó el GUID `{8f9cb695-5d48-48d6-a329-7202b44607e3}`. Se corroboró en la documentación oficial de Microsoft que este identificador pertenece a la actualización automática de la **"Vulnerable Driver Blocklist"** de *Windows Defender Application Control* (WDAC).
4. **Análisis de la Detección del EDR:** Se determinó que el módulo BTP de Cortex XDR posee una regla de endurecimiento preventivo para evitar que atacantes inyecten controladores vulnerables (ataques tipo *Bring Your Own Vulnerable Driver - BYOVD*). Al ver un intento de escritura en la carpeta de políticas de integridad de código (*Code Integrity*), Cortex bloqueó preventivamente el acceso, interceptando una actualización rutinaria del sistema operativo.
5. **Descarte de Amenaza:** No se detectó ninguna inyección de código, persistencia, llamadas anómalas ni técnicas de "Living off the Land" (LotL).

#### Resolución y Justificación de Cierre:
> *"Se cierra el caso como **Falso Positivo**. La actividad fue originada legítimamente por el sistema operativo Windows mediante el proceso `AggregatorHost.exe` (SYSTEM, firmado por Microsoft) con el propósito de actualizar la lista oficial de controladores vulnerables bloqueados por WDAC (`{8f9cb695-5d48-48d6-a329-7202b44607e3}.cip`). Cortex XDR bloqueó la acción de manera preventiva por protección de integridad de políticas. Se descarta compromiso, malware o actividad adversaria."*

---
