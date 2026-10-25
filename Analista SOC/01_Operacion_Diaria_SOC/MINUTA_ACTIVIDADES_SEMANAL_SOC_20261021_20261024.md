# 🛡️ MINUTA DE ACTIVIDADES Y GESTIÓN TÉCNICA — SOC TECHNOMA

* **Para:** Jefatura de Operaciones SOC / Dirección de Ciberseguridad  
* **De:** Kevin Moraes — Analista / Ingeniero de Operaciones SOC  
* **Periodo Reportado:** Miércoles 21 de Octubre al Sábado 24 de Octubre de 2026  
* **Estado General de Operación:** Cola de Casos en **0** | Sensores al **100%** | Retención y Cuota **Normalizadas**  

---

## 1. RESUMEN EJECUTIVO (HITOS PRINCIPALES)

1. **Cola de Incidentes en Cero (0 pendientes):** Se identificaron y gestionaron 21 incidentes de Cortex XDR que carecían de caso en Stellar Cyber por limitaciones en reglas de ingesta previas. Se desarrollaron herramientas de integración SOAR que crearon los tickets, vincularon la evidencia forense atómica y cerraron los 21 casos con dictamen técnico formal individual (`Resolved` / `False Positive`).
2. **Estabilización Total de Security Onion 3:** Se resolvió la caída cíclica del motor Logstash (reinicios cada 15 min por desincronización de SaltStack), se purgaron índices locales antiguos recuperando gigabytes en `/nsm` sin alterar datos de clientes (Valores y Vascol intactos) y se solucionaron las colisiones HTTP 409 de ElastAlert2.
3. **Upgrade Mayor Exitoso a Security Onion 3.3.0 y Aporte al Open Source:** Se diagnosticó y solucionó un fallo crítico en el runtime Go HTTP/2 de Docker Buildx durante la actualización `soup -y`. El parche fue probado con éxito en producción y se envió como **Pull Request oficial firmado (#16343)** al repositorio global de Security Onion Solutions.
4. **Auditoría de Gobernanza y Cero Puntos Ciegos:** Se auditó el 100% de los 54 Log Filters de Stellar Cyber y se emitió dictamen técnico sobre el puerto TCP 7002 (keep-alives de señalización digital) y TCP 8010 (respaldos Veeam hacia QNAP), garantizando que las exclusiones no afectan tráfico de seguridad (UTM/IPS).

---

## 2. DESGLOSE CRONOLÓGICO DE ACTIVIDADES

### 📅 Miércoles 21 de Octubre de 2026
* **Unificación de Políticas de Ingesta (Stellar ➔ SO3):**
  * Sincronización e inyección automatizada de los 54 filtros de descarte homologados de Stellar Cyber hacia las pipelines de Logstash en Security Onion (`/opt/so/conf/logstash/pipelines/`).
  * *Resultado:* Reducción drástica del ruido no analítico (broadcast, traps internos y pings de salud) antes de ser indexados en Elasticsearch, optimizando ancho de banda y CPU.
* **Estabilización de Motor de Alertas ElastAlert2:**
  * Diagnóstico y mitigación de excepciones recurrentes `HTTP 409 Conflict` provocadas por colisión concurrente de hilos en los índices `elastalert_status*`.
  * *Resultado:* Supresión de saturación de logs en `/opt/so/log/elastalert/` y normalización de la evaluación continua de reglas.
* **Ingeniería Inversa y Documentación Maestra de Arquitectura SO3:**
  * Relevamiento y redacción del inventario técnico y fichas de arquitectura de los 23 contenedores Docker de Security Onion (`so-elasticsearch`, `so-logstash`, `so-kibana`, `so-kratos`, `so-suricata`, `so-zeek`, `so-fleet`, etc.).
  * Documentación del núcleo orquestador SaltStack (topología ZeroMQ, puertos 4505/4506 y estados Salt).
* **Mejora del Bot de Alertas SOC (Telegram):**
  * Enriquecimiento del detalle de alertas para extraer y enviar en tiempo real Hostname real, Usuario y vector técnico en alertas de endpoint/Cortex.

---

### 📅 Jueves 22 de Octubre de 2026
* **Diagnóstico y Solución Definitiva de Logstash (Reinicio Cíclico cada 15 min):**
  * *Causa Raíz:* En `/opt/so/saltstack/local/pillar/logstash/soc_logstash.sls` coexistía una clave obsoleta `pipeline_config:`. Al ejecutarse el cron de Salt (`highstate_schedule`), se interpretaba un cambio ficticio en reglas de pipeline, disparando `docker_container.mod_watch` que mataba y recreaba el contenedor `so-logstash` cada cuarto de hora.
  * *Acción:* Limpieza quirúrgica del Pillar, reasignación estricta de permisos `660` (`logstash:socore`) y verificación de estabilidad continua al 100%.
* **Auditoría Forense y Liberación de Espacio en `/nsm`:**
  * Depuración controlada de índices de prueba locales de Zeek y Suricata caducos.
  * *Gobernanza:* Cero impacto en datos de clientes; se verificó la preservación absoluta de los **12.6 millones de eventos** de Valores Casa de Bolsa (`valores-ndr`) y los **4.8 millones de eventos** de Vascol RDS (`secops-vascol`).
* **Desarrollo del Buscador Universal Federado SOC (`universal_soc_hunter.py`):**
  * Implementación de herramienta de cacería simultánea en un solo comando para correlacionar IPs, Dominios, Usuarios e IOCs entre Stellar Cyber y Security Onion 3.
* **Preparación y Lanzamiento del Upgrade SO 3.3.0:**
  * Resguardo de configuraciones críticas y ejecución del proceso oficial de actualización (`soup -y`).

---

### 📅 Viernes 23 de Octubre de 2026
* **Resolución de Bloqueo Crítico en Upgrade SO 3.3.0 (Go HTTP/2 PROTOCOL_ERROR):**
  * *El Problema:* Al transferir imágenes pesadas (`so-elastic-fleet-package-registry` de 1.8 GB y `so-elasticsearch` de 1.5 GB) hacia el registro local `localhost:5000`, la negociación HTTP/2 del runtime Go en Docker Buildx abortaba el stream (`PROTOCOL_ERROR`), provocando la caída fatal de `soup`.
  * *Solución Aplicada:* Configuración de `GODEBUG=http2client=0` (forzando HTTP/1.1 secuencial y estable) e implementación de fallback robusto a `docker push` en `so-image-common`.
  * *Resultado:* Transferencia exitosa de las 24 imágenes Docker oficiales en tiempos récord (0.9s y 1.0s) y culminación limpia de la actualización de la plataforma.
* **Resolución de Bloqueo en Paquetes Elastic Fleet:**
  * Ajuste de límites de watermark de disco en Elasticsearch y culminación de la actualización de 10 paquetes esenciales de Elastic Fleet.
* **Sincronización del Nodo Satélite (`secops-vascol`):**
  * Corrección de discrepancia de versión en SOC Grid mediante la ejecución dirigida del estado Salt `sensoroni`, alineando el contenedor del sensor a la versión 3.3.0.
* **Auditoría Forense Integral de los 54 Log Filters (Stellar Cyber):**
  * Análisis de riesgo y ceguera para eventos en puerto TCP 7002 (MagicInfo) y TCP 8010 (Veeam hacia QNAP Storage `10.11.5.4`).
  * *Dictamen:* Se validó que el descarte aplica exclusivamente sobre logs de sesión cerrados (`type: traffic` / `action: close`), manteniendo intactos al 100% todos los eventos de seguridad (`type: utm` / IPS / Malware).
* **Contribución Oficial al Repositorio de Security Onion Solutions:**
  * Documentación del Bug Report formal en el Issue [#16342].
  * Creación y envío del Pull Request oficial [#16343] sobre la rama `3/dev`, firmado criptográficamente con SSH (badge verde **Verified**).

---

### 📅 Sábado 24 de Octubre de 2026
* **Control Cruzado y Auditoría de Alertas Cortex XDR en Data Lake:**
  * Se auditó el Data Lake de Stellar Cyber (`aella-ser-*` y Syslog) de octubre 2026, detectando 21 incidentes generados por Cortex XDR que no contaban con Caso en la consola.
* **Desarrollo y Puesta en Producción de Suite SOAR de Cortex:**
  * `auto_create_cortex_cases.py`: Script que valida la lista de casos vivos, crea el ticket vía API (`POST /connect/api/v1/cases`) y asocia atómicamente el array forense de alertas (`_index` y `_id`) para trazabilidad de línea de tiempo completa.
  * `check_missing_cortex_cases.py`: Auditor rápido de conciliación entre alertas e incidentes.
  * Creación exitosa de los tickets **#18169 al #18189**.
* **Triaje Forense y Dictamen Individual:**
  * Análisis técnico de cada uno de los 21 casos: falsos positivos por entornos de desarrollo (OpenAI Codex, extensiones headless de VS Code, utilitarios de compilación), herramientas legítimas de productividad (Super Productivity, Dropbox API) y telemetría de resguardo autorizada (Proton Drive, Google Cloud Code).
* **Cierre Masivo con Trazabilidad Completa y Comentarios por API:**
  * Cierre por API de los 21 casos con estado `Resolved` y resolución `False Positive`.
  * Integración en el script `close_cases_bulk.py` de la llamada a `POST /connect/api/v1/cases/{id}/comments`, inyectando el motivo técnico individualizado en la pestaña *Comments* de cada caso.
* **Normalización de Cola Abierta en Stellar Cyber:**
  * Triaje y cierre de 2 casos abiertos adicionales (#18190 de telemetría de desarrollo local y #18167 de sincronización interna entre Controladores de Dominio AD).
  * **Cola de Casos Abiertos finalizó en 0**.
* **Gobernanza y Versionado:**
  * Actualización de la `Bitacora_Personal_Casos_SOC.md` (Casos 040 al 044).
  * Actualización de la `bitacora.md` (Entrada 18).
  * Resguardo de todos los scripts y bitácoras individuales en el repositorio Git de producción (`Morochief/soar`).

---

## 3. TABLA CONSOLIDADA DE CASOS CORTEX XDR GESTIONADOS Y CERRADOS

| Ticket Stellar | Case Cortex | Endpoint | Detección / Amenaza | Resolución | Justificación Registrada |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **#18169** | `617` | `NB-MANUELALM` | LOLBIN scripting engine rare host | **False Positive** | Actividad legítima de desarrollo vía Node/Wscript interactuando con repositorio reconocido. |
| **#18170** | `616` | `NB-GVERA` | PowerShell calling invoke expression | **False Positive** | Asistente de desarrollo OpenAI Codex CLI ejecutando compilación local. |
| **#18171** | `615` | `NB-KMORAEZ` | Fetching file from TOR domain | **False Positive** | Pruebas operativas de Threat Intelligence en estación de analista SOC. Sin compromiso. |
| **#18172** | `614` | `NB-RALEMAN` | Super Productivity Dropbox sync | **False Positive** | Aplicación open-source de productividad sincronizando notas con API de Dropbox. |
| **#18173** | `613` | `NB-ODACOSTA` | 23 hosts connection attempts | **False Positive** | Tareas administrativas de gestión de red entre subredes de IT/soporte. |
| **#18174** | `612` | `NB-EORLANDINI` | curl www.mastertech.com.py | **False Positive** | Petición HTTP legítima de desarrollo hacia partner local vía curl. |
| **#18175** | `611` | `NB-GVERA` | PowerShell calling invoke expression | **False Positive** | Invocación de herramientas de build automatizado desde entorno IDE. |
| **#18176** | `610` | `NB-EORLANDINI` | LOLBIN executable rare host | **False Positive** | Descarga de paquetes y dependencias de desarrollo con utilitarios nativos. |
| **#18177** | `609` | `NB-KMORAEZ` | Upload daily-cloudcode-pa.googleapis.com | **False Positive** | Sincronización de telemetría de Cloud Code / Google Antigravity contra Google Cloud. |
| **#18178** | `607` | `NB-FMORA` | Upload fra-storage.proton.me | **False Positive** | Resguardo y backup de archivos en cliente oficial de Proton Drive. |
| **#18179** | `604` | `NB-JTORALES` | AMSI obfuscation technique | **False Positive** | Concatenación de variables en script administrativo de soporte (falso positivo heurístico). |
| **#18180** | `601` | `NB-GMARTINEZ` | Suspicious payload executable | **False Positive** | Compilación local de ejecutable interno no indexado previamente en WildFire. Hash seguro. |
| **#18181** | `599` | `NB-FBENEGAS` | conhost powershell --headless | **False Positive** | Terminal integrada headless generada por Visual Studio Code. |
| **#18182** | `597` | `NB-EDVELAZQUEZ`| BITS transfer execution | **False Positive** | Servicio estándar BITS de Windows para actualización y descarga de paquetes del SO. |
| **#18183** | `596` | `NB-RBARRETO` | conhost powershell --headless | **False Positive** | Proceso secundario headless originado por entorno de programación local. |
| **#18184** | `595` | `NB-NOC2` | winget videolan.c3sl.ufpr.br | **False Positive** | Instalación/actualización de VLC vía Windows Package Manager desde mirror universitario oficial. |
| **#18185** | `594` | `NB-EORLANDINI` | curl huggingface.co | **False Positive** | Descarga legítima de modelos y datasets de IA desde Hugging Face. |
| **#18186** | `593` | `NB-FBENEGAS` | winget videolan.c3sl.ufpr.br | **False Positive** | Actualización de software vía `winget` desde mirror oficial. |
| **#18187** | `588` | `NB-IMAYOR` | conhost powershell --headless | **False Positive** | Tarea de automatización y terminal en segundo plano de herramientas de desarrollo. |
| **#18188** | `586` | `NB-FBENEGAS` | conhost powershell --headless | **False Positive** | Terminal integrado de editor de código. |
| **#18189** | `541` | `NB-JTORALES` | 16 hosts connection attempts | **False Positive** | Sondeo de conectividad interna ejecutado por personal de SOC en monitoreo rutinario. |

---

## 4. ESTADO ACTUAL DE PLATAFORMAS (CONCLUSIÓN TÉCNICA)

* **Stellar Cyber OpenXDR:** 
  * Casos abiertos: **0**.
  * Consumo de licencia y cuota: **Estabilizado y bajo control** tras la calibración de los 54 log filters y reglas de descarte.
  * Trazabilidad de Cortex XDR: Integrada y documentada en los procedimientos oficiales.
* **Security Onion 3 (soc-onion):**
  * Versión del clúster: **3.3.0 operativa** en Manager y nodo satélite (`secops-vascol`).
  * Contenedores: **23/23 en estado Up**, sin reinicios cíclicos de Logstash y sin colisiones en ElastAlert2.
  * Almacenamiento en `/nsm`: **Optimizado**, con 100% de retención de telemetría de clientes asegurada.
* **Repositorios y Control de Cambios:**
  * Código SOAR, scripts de automatización y bitácoras: Versionados y respaldados en rama `main` de GitHub.
  * Fix de Docker Buildx: Enviado a revisión global en rama `3/dev` de Security Onion Solutions.
