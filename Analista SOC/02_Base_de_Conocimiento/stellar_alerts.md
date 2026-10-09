# Diccionario Global de Alertas de Stellar Cyber XDR

Este documento contiene la base de conocimientos de tipos de alertas (Machine Learning y basadas en reglas) ordenadas alfabéticamente por su nombre de visualización. Diseñado para servir de contexto técnico para agentes de IA y analistas SOC.

---

## 1. Alertas de Comportamiento y Procesos de Host (Endpoint & OS)

### Abnormal Parent / Child Process
* **Descripción:** Detecta cuando un proceso padre que normalmente lanza un número pequeño y constante de procesos hijos, genera un hijo nuevo o inusual.
* **XDR Event Name:** `parent_child` | **Severidad:** 25
* **Subtipos:** Machine Learning Anomaly Detection, Rule Based Detection.
* **MITRE ATT&CK:** Persistent Foothold | Tactic: XDR EBA (XTA0001) | Technique: XDR Process Relationship Anomaly (XT1002)
* **Campos de Supresión:** `parent_proc_name`, `hostip`, `stellar.rule_id`
* **Campos Clave:** `process_name`, `stability`, `days_stable`, `diversity`, `child_count`.

### Backup Catalogs Deleted by Ransomware
* **Descripción:** Detecta el uso de la utilidad `wbadmin.exe` para eliminar el catálogo de copias de seguridad, una técnica típica de ransomware para evitar la recuperación del sistema.
* **XDR Event Name:** `ransomware_delete_backup_catalogs` | **Severidad:** 80
* **MITRE ATT&CK:** Defense Evasion (TA0005) | Technique: Indicator Removal on Host (T1070.004)
* **Campos de Supresión:** `computer_name`
* **Campos Clave:** `hostip`, `process_name`, `event_data.CommandLine`.

### Command Anomaly
* **Descripción:** Un comando se ejecuta un número anómalamente alto de veces en comparación con su histórico o con otros comandos.
* **XDR Event Name:** `command_anomaly` | **Severidad:** 15
* **MITRE ATT&CK:** Execution (TA0002) | Technique: Command and Scripting Interpreter (T1059)
* **Campos de Supresión:** `command`
* **Campos Clave:** `actual`, `typical`, `cwd`, `hostip`, `username`.

### Encoded PowerShell
* **Descripción:** Ejecución de scripts de PowerShell que contienen flags de codificación u ofuscación (ej. campos enriquecidos de Stellar `2100` o `2101` con flag oculto).
* **XDR Event Name:** `encoded_powershell` | **Severidad:** 80
* **MITRE ATT&CK:** Execution (TA0002) | Technique: Command and Scripting Interpreter (T1059)
* **Campos de Supresión:** `srcip`
* **Campos Clave:** `event_data.ContextInfo`, `event_data.Payload`.

### File Action Anomaly / File Creation Anomaly
* **Descripción:** Un usuario realiza acciones masivas (mover, copiar, eliminar, cambiar atributos) o crea archivos a una tasa anómalamente alta (`actual` vs `typical`).
* **XDR Event Name:** `anomalous_file_action` / `file_creation` | **Severidad:** 70
* **MITRE ATT&CK:** Impact (TA0040) / Persistent Foothold (XTA0001)
* **Campos de Supresión:** `secondary` (username)
* **Campos Clave:** `path`, `actual`, `typical`.

### Mimikatz Credential Dump
* **Descripción:** Intento de acceso sospechoso al proceso `lsass.exe` utilizando máscaras de acceso específicas asociadas con herramientas de extracción de credenciales en memoria (Flag enriquecido `2301`).
* **XDR Event Name:** `mimikatz_mem_scan` | **Severidad:** 90
* **MITRE ATT&CK:** Credential Access (TA0006) | Technique: OS Credential Dumping (T1003)
* **Campos de Supresión:** `access_subject`, `computer_name`
* **Campos Clave:** `access_mask`, `hostip`.

### Mimikatz DCSync
* **Descripción:** Intento de replicación de Active Directory por primera vez en un controlador de dominio o mediante una cuenta que raramente realiza esta acción. Riesgo crítico de volcado de hashes de contraseñas.
* **XDR Event Name:** `mimikatz_dcsync` | **Severidad:** 90
* **MITRE ATT&CK:** Credential Access (TA0006) | Technique: OS Credential Dumping (T1003)
* **Campos de Supresión:** `computer_name`, `event_data.SubjectUserSid`
* **Campos Clave:** `event_data.SubjectDomainName`, `event_data.SubjectUserName`, `event_data.Properties`.

### Password Cracking with Hashcat
* **Descripción:** Ejecución de scripts o comandos en Windows que invocan `hashcat.exe` o utilizan sus parámetros conocidos (`-a -m 1000 -r`) para descifrar archivos SAM extraídos del registro.
* **XDR Event Name:** `password_cracking_with_hashcat` | **Severidad:** 90
* **MITRE ATT&CK:** Credential Access (TA0006) | Technique: Brute Force (T1110)
* **Campos de Supresión:** `hostip`, `event_data.Image`, `event_data.CommandLine`

### Password Spraying Attempts Using Dsacls
* **Descripción:** Intento de abuso de la herramienta legítima `dsacls.exe` empleando los parámetros `/user` y `/passwd` de manera sospechosa para realizar password spraying en entornos Active Directory.
* **XDR Event Name:** `password_spraying_attempts_using_dsacls` | **Severidad:** 50
* **MITRE ATT&CK:** Defense Evasion (TA0005) | Technique: Signed Binary Proxy Execution (T1218)
* **Campos de Supresión:** `computer_name`, `event_data.CommandLine`, `event_data.OriginalFileName`, `process_name`.

### Potentially Malicious Windows Event
* **Descripción:** Regla genérica para identificar eventos de seguridad de Windows altamente correlacionados con la desactivación o el bloqueo de indicadores de defensa.
* **XDR Event Name:** `windows_security_malicious_event`
* **MITRE ATT&CK:** Defense Evasion (TA0005) | Technique: Impair Defenses (T1562.006)
* **Campos de Supresión:** `computer_name`, `event_data.TargetUserName`, `event_id`, `stellar.rule_id`.

### PowerShell Remote Access
* **Descripción:** Ejecución de scripts de PowerShell que embeben direcciones IP remotas o interactúan activamente con hosts externos de C&C (Flags enriquecidos `2200` y `2201`).
* **XDR Event Name:** `powershell_cnc` | **Severidad:** 80
* **MITRE ATT&CK:** Execution (TA0002) | Technique: Command and Scripting Interpreter (T1059)
* **Campos de Supresión:** `computer_name`, `remote_ip`
* **Campos Clave:** `event_data.ScriptBlockText`.

### Process Anomaly / Uncommon Process Anomaly
* **Descripción:** Un proceso se lanza una cantidad masiva de veces en un periodo corto o se ejecuta un binario que nunca antes se había visto (`days_silent`) en el entorno supervisado.
* **XDR Event Name:** `bad_process` (Severidad 15) / `network_uncommon_process` (Severidad 30)
* **MITRE ATT&CK:** Persistent Foothold | Technique: XDR Process Anomaly (XT1001)
* **Campos de Supresión:** `process_name`
* **Campos Clave:** `actual`, `typical`, `hostip`, `wineventlog_user`.

### Volume Shadow Copy Deletion (via VssAdmin / WMIC)
* **Descripción:** Eliminación de Shadow Copies de volumen utilizando comandos de `vssadmin.exe` o `wmic.exe` para deshabilitar los mecanismos de recuperación del sistema operativo ante ataques de ransomware.
* **XDR Event Name:** `ransomware_volume_shadow_copy_deletion_via_vssadminedit` / `..._via_wmicredit` | **Severidad:** 80
* **MITRE ATT&CK:** Impact (TA0040) | Technique: Inhibit System Recovery (T1490)
* **Campos de Supresión:** `computer_name` / `hostip`
* **Campos Clave:** `event_data.CommandLine`, `process_name`.

---

## 2. Alertas de Red, Tráfico e Infraestructura (NTA / NBA)

### Application Usage Anomaly / Uncommon Application Anomaly
* **Descripción:** Conexiones salientes masivas desde una aplicación interna hacia hosts externos superando el percentil 99.99%, o detección de un protocolo/aplicación web que nunca antes se había visto (`days_silent`).
* **XDR Event Name:** `pri_pub_appid` (Severidad 15) / `network_uncommon_app` (Severidad 20)
* **MITRE ATT&CK:** Initial Attempts / Initial Access | Technique: XDR App Anomaly (XT2003)
* **Campos de Supresión:** `appid`
* **Campos Clave:** `actual`, `stellar.threshold`, `srcip_host`, `dstip_host`, `appid_name`.

### Bad Destination / Source Reputation Anomaly & Bad Reputation Login
* **Descripción:** Flujos anómalos de red hacia o desde IPs clasificadas con mala reputación global, o inicios de sesión exitosos provenientes de infraestructura históricamente maliciosa.
* **XDR Event Name:** `dstip_bad_reps` (Sev 30) / `srcip_bad_reps` (Sev 30) / `bad_reputation_login` (Sev 50)
* **MITRE ATT&CK:** Persistent Foothold / Initial Attempts | Technique: XDR Bad Reputation (XT2010)
* **Campos de Supresión:** `dstip`, `srcip`
* **Campos Clave:** `actual`, `typical`, `srcip_reputation`, `dstip_reputation`, `login_type`, `username`.

### Command & Control Reputation Anomaly / Suspected Network Beaconing Activities
* **Descripción:** Conexiones recurrentes hacia servidores conocidos de C&C o detección analítica de balizamiento de red (beacons). Los patrones de balizamiento se confirman si la frecuencia (`period_mean`) está estrictamente entre 100 y 400 segundos y es persistente (`period_cnt`) por más de 24 horas hacia destinos de baja prevalencia.
* **XDR Event Name:** `cnc_reputation` (Sev 70) / `c2beaconing` (Sev 70)
* **MITRE ATT&CK:** Command and Control (TA0011) / XDR Intel (XTA0005)
* **Campos de Supresión:** `dstip`, `srcip`, `dstport`
* **Campos Clave:** `period_cnt`, `period_mean`, `connection_prevalence`.

### Cryptojacking
* **Descripción:** Tráfico de red interceptado por firmas de IDS que coincide inequívocamente con la actividad de minería de criptomonedas no autorizada.
* **XDR Event Name:** `cryptojacking` | **Severidad:** 70
* **MITRE ATT&CK:** Impact (TA0040) | Technique: Resource Hijacking (T1496)
* **Campos de Supresión:** `srcip`, `dstip`, `ids.signature`
* **Campos Clave:** `srcip_host`, `dstip_host`.

### Data Ingestion Volume Anomaly / Sensor Status Anomaly
* **Descripción:** Desviación masiva (alta o baja) en el volumen de ingesta de datos de un sensor o desconexión abrupta del agente (`ade_outbytes_anomaly_flip`).
* **XDR Event Name:** `ade_outbytes_anomaly` / `ade_outbytes_anomaly_flip` | **Severidad:** 10
* **Subtipos de Estado:** Sensor Status Flipped, Disconnected but still sending, Disconnected and stopped sending, Disconnected and inactive.
* **Campos de Supresión:** `engid`
* **Campos Clave:** `actual`, `typical`, `engid_name`, `metadata.status`.

### DHCP Server Anomaly
* **Descripción:** Aparición de un nuevo servidor DHCP en la red que podría indicar ataques de suplantación (Rogue DHCP) para desviar o interceptar el tráfico.
* **XDR Event Name:** `dhcp_anomaly` | **Severidad:** 20
* **MITRE ATT&CK:** Exploration | Tactic: XDR NBA | Technique: XDR Server Anomaly (XT2007)
* **Campos de Supresión:** `dstip`, `metadata.response.server_ip`
* **Campos Clave:** `engid`, `srcip_host`.

### ICMP Based Exfiltration or Tunneling
* **Descripción:** Detección de paquetes ICMP con tamaños de carga útil anormalmente grandes (`actual` vs `typical`) en intervalos de 5 minutos, indicando posible tunelización o exfiltración.
* **Nota del SOC / Falsos Positivos:** Comandos manuales de diagnóstico como `ping -l 1400 8.8.8.8` (o `ping -s 1400` en Linux) disparan falsos positivos legítimos al evaluar MTU de red.
* **XDR Event Name:** `icmp_tunnel` | **Severidad:** 50
* **MITRE ATT&CK:** Exfiltration (TA0010) | Technique: Exfiltration Over Alternative Protocol (T1048)
* **Campos de Supresión:** `srcip`, `dstip`
* **Campos Clave:** `inbytes_delta`, `inpkts_delta`, `outbytes_delta`, `outpkts_delta`, `actual`, `typical`.

### Outbytes Anomaly (y Outbytes Delta Anomaly)
* **Descripción:** Un host interno genera un pico masivo o incremento constante de tráfico saliente de red, sugiriendo exfiltración automatizada de datos.
* **XDR Event Name:** `outbytes_anomaly` / sub-tipo `outbytesdelta_spike` | **Severidad:** 35
* **MITRE ATT&CK:** Exfiltration (TA0010) | Technique: Automated Exfiltration (T1020)
* **Campos de Supresión:** `srcip_host`
* **Campos Clave:** `actual`, `typical`, `dstip_host`.

### Protocol Anomalies (External / Internal Non-Standard Port Anomaly)
* **Descripción:** Uso de puertos no estándar para aplicaciones comunes (ej. tráfico HTTP/SSH sobre puertos aleatorios) o combinaciones de `dst_ip` + `dstport` + `appid` nunca antes registradas históricamente.
* **XDR Event Name:** `external_non_std_port_anomaly` (Sev 15) / `internal_non_std_port_anomaly` (Sev 20)
* **MITRE ATT&CK:** Command and Control (TA0011) | Technique: Non-Standard Port (T1571)
* **Campos de Supresión:** `dstip`, `dstport`, `appid`
* **Campos Clave:** `days_silent`, `actual`, `typical`.

### Protocol Pattern Anomaly (Internal / Remote Access)
* **Descripción:** Desviación estadística en los patrones de uso de protocolos de movimiento lateral (SSH, SMB, RDP, LDAP, etc.) o de compartición/almacenamiento en la nube (OneDrive, GitHub, Wireguard).
* **XDR Event Name:** `internal_appflow_outlier` (Sev 15) / `external_appflow_outlier` (Sev 40)
* **MITRE ATT&CK:** Lateral Movement (TA0008) / Exfiltration (TA0010)
* **Campos de Supresión:** `appid_name`, `srcip`
* **Campos Clave:** `num_clust`, `sum_clust_size`, `training_days`.

### Unapproved Asset Activity
* **Descripción:** Detección de actividad proveniente de un activo que previamente fue explícitamente marcado como "No Aprobado" por el equipo de analistas del SOC en la pestaña de Asset Analytics. Genera una alerta diaria hasta su aprobación o mitigación.
* **XDR Event Name:** `asset_violation` | **Severidad:** 50
* **MITRE ATT&CK:** Tactic: XDR NBA | Technique: XDR Unapproved Asset Activity (XT2013)
* **Campos de Supresión:** `asset_id`
* **Campos Clave:** `vendor`.

---

## 3. Seguridad de Identidades, Accesos e Inicios de Sesión (UBA / UBA Cloud)

### Account Created and Deleted in Short Timeframe
* **Descripción:** Alerta cuando una cuenta de usuario es creada y posteriormente eliminada dentro de un umbral menor a 24 horas. Comportamiento típico de persistencia temporal y evasión de defensas.
* **XDR Event Name:** `account_created_deleted_in_short_timeframe` | **Severidad:** 75
* **Subtipo Entra ID:** `azure_ad_account_created_deleted`
* **MITRE ATT&CK:** Defense Evasion (TA0005) | Technique: Valid Accounts (T1078)
* **Campos de Supresión:** ID del recurso objetivo en wineventlog (`correlation_info.0.targetResources.id`), actividad de Entra ID `Delete user`.
* **Campos Clave:** `user.name`, `activityDisplayName`, timestamps de creación/borrado.

### Account Creation Anomaly
* **Descripción:** Generación masiva y anómala de cuentas de usuario en un intervalo de 5 minutos, o primera vez que una cuenta administrativa crea un usuario en un rango de 14 días. Aplica a AWS, Entra ID, Google Workspace y Windows.
* **XDR Event Name:** `account_creation_anomaly` | **Severidad:** 70
* **MITRE ATT&CK:** Persistence (TA0003) | Technique: Create Account (T1136)
* **Campos de Supresión:** `event_data.SubjectUserName`, `srcip_usersid`
* **Campos Clave:** `actual`, `typical`, `event_summary.account_creation.new_users_count`, `new_users_summary`.

### Account MFA Login Failure Anomaly
* **Descripción:** Cantidad anómalamente alta de fallos de autenticación multifactor (MFA) para una cuenta específica en soluciones Cloud/Okta/AWS.
* **XDR Event Name:** `cloud_account_login_failure_okta` | **Severidad:** 45
* **MITRE ATT&CK:** Credential Access (TA0006) | Technique: Brute Force (T1110)
* **Campos de Supresión:** `srcip_usersid`, `eventName`, `eventSource`, `stellar.rule_id`
* **Campos Clave:** `event_summary.total_failed`, `total_successful`, `total_fail_ratio`, `weighted_anomaly_score`.

### Dormant Account Anomaly (Early Access)
* **Descripción:** Una cuenta histórica que no ha registrado interacciones o inicios de sesión interactivos por un periodo prolongado vuelve a activarse de forma repentina. Envía hasta 3 alertas de recordatorio (a los 14, 21 y 28 días de inactividad). Fuentes: AD, Entra ID, O365.
* **XDR Event Name:** `dormant_account` | **Severidad:** 30
* **MITRE ATT&CK:** Persistence (TA0003) | Technique: Valid Accounts (T1078)
* **Campos de Supresión:** `srcip_username`
* **Campos Clave:** `days_silent`, `last_seen_ts`.

### Login Attempt Location Count
* **Descripción:** Detección de intentos de inicio de sesión de un usuario desde una cantidad inusualmente alta de ubicaciones geográficas distintas dentro de un marco temporal de 24 horas.
* **Nota del Algoritmo:** Stellar Cyber aplica **Geohashing con precisión de 4** (celdas de cuadrícula de ~25 millas de diámetro) para agrupar coordenadas geográficas similares y mitigar falsos positivos causados por el enrutamiento inestable de proveedores de internet.
* **XDR Event Name:** `login_location_count` | **Severidad:** 50
* **MITRE ATT&CK:** Tactic: XDR UBA | Technique: XDR Location Anomaly (XT2001)
* **Campos de Supresión:** `srcip_usersid`
* **Campos Clave:** `actual`, `typical`, `event_summary.login_location_count.location_summary`.

### Login Time Anomaly
* **Descripción:** Inicio de sesión exitoso o intento de un usuario en un horario completamente fuera de su rango histórico habitual (`actual_range` vs `typical_range`). Vincula dinámicamente las zonas horarias del gateway (`engid_gateway`) o la configuración global.
* **XDR Event Name:** `user_login_time` | **Severidad:** 40
* **MITRE ATT&CK:** Tactic: XDR UBA | Technique: XDR Time Anomaly (XT4005)
* **Campos de Supresión:** `srcip_usersid`, `event_data.TargetUserName`
* **Campos Clave:** `srcip_username`, `actual_range`, `typical_range`.

### Password Resets Anomaly
* **Descripción:** Una cuenta de origen restablece o modifica las contraseñas de múltiples cuentas objetivo de forma masiva, excediendo el límite diario dinámico calculado.
* **XDR Event Name:** `password_resets_anomaly` | **Severidad:** 30
* **Subtipo Windows:** `windows_account_password_resets_anomaly`
* **MITRE ATT&CK:** Persistence (TA0003) | Technique: Account Manipulation (T1098)
* **Campos de Supresión:** `event_data.SubjectDomainName`, `event_data.SubjectUserName`
* **Campos Clave:** `actual`, `typical`.

### Successful Login After Brute Force
* **Descripción:** Se registra una autenticación exitosa desde una dirección IP nueva después de que esa misma cuenta de usuario haya sufrido una campaña severa de fuerza bruta (registrada en ventanas de 30 minutos o 24 horas). Alerta crítica de posible compromiso de cuenta.
* **XDR Event Name:** `brute_force_success` | **Severidad:** 90
* **MITRE ATT&CK:** Credential Access (TA0006) | Technique: Brute Force (T1110)
* **Campos de Supresión:** `srcip_usersid`
* **Campos Clave:** `srcip`, `login_type`, `event_summary.unique_failure_ips_short`, `unique_failure_ips_long`, `srcip_asn`.

### User Asset Access Anomaly
* **Descripción:** Un usuario que suele interactuar con un número pequeño y estático de activos corporativos accede por primera vez a un servidor o dispositivo nuevo en la red.
* **XDR Event Name:** `user_asset_access` | **Severidad:** 30
* **Subtipos:** `smb_user_asset_access` (basado en tráfico SMB), `kerberos_user_asset_access` (basado en tickets TGS).
* **MITRE ATT&CK:** Propagation | Tactic: XDR UBA | Technique: XDR Asset Anomaly (XT4004)
* **Campos de Supresión:** `event_data.TargetUserName`, `metadata.request.username`, `srcip_usersid`
* **Campos Clave:** `stability`, `days_stable`, `diversity`, `child_count`, `srcip_username`.

### User Login Location Anomaly (User Login Region)
* **Descripción:** Autenticación exitosa registrada desde una IP cuya distancia geográfica es anómalamente lejana en comparación con el histórico de inicios de sesión permitidos para ese usuario.
* **Mecanismos de Control de Ruido:** Prioriza logs de Entra ID sobre M365 para correlacionar el ID de sesión. Integra histórico de ASN, organización de ASN y User Agent corporativo.
* **XDR Event Name:** `user_login_region` | **Severidad:** 50
* **MITRE ATT&CK:** Tactic: XDR UBA | Technique: XDR Location Anomaly (XT2001)
* **Campos de Supresión:** `srcip_usersid`
* **Campos Clave:** `distance_deviation`, `srcip_geo.countryName`, `srcip_geo.region`, `asn_seen_before`.

### User Process Usage Anomaly
* **Descripción:** Un usuario ejecuta un binario o comando que se sale por completo de su perfil habitual de ejecución dentro del host corporativo.
* **XDR Event Name:** `user_uncommon_process` | **Severidad:** 10
* **MITRE ATT&CK:** Persistent Foothold | Tactic: XDR EBA | Technique: XDR Process Anomaly (XT1001)
* **Campos de Supresión:** `srcip_usersid`, `user.name`
* **Campos Clave:** `process_name`, `stability`, `days_stable`, `diversity`.

---

## 4. Anomalías de Inicios de Sesión y Fuerza Bruta (External vs Internal)

> **Nota de Contexto para la IA:** Stellar Cyber bifurca estrictamente las alertas entre vectores **External** (origen IP pública de Internet hacia el entorno corporativo) e **Internal** (movimiento lateral dentro de los direccionamientos IP privados de la organización). Las alertas internas conllevan una criticidad/severidad intrínseca más alta.

| Nombre de Alerta | Event Name (`xdr_event.name`) | Severidad | Técnica MITRE ATT&CK | Subtipos Disponibles |
| :--- | :--- | :--- | :--- | :--- |
| **External Account Login Failure Anomaly** | `external_cloud_account_login_failure` | 45 | Brute Force (`T1110`) | O365/Entra, Windows Security, VPN Logon (FortiGate, CheckPoint, Palo Alto) |
| **Internal Account Login Failure Anomaly** | `internal_cloud_account_login_failure` | 60 | Brute Force (`T1110`) | Windows Logon, Kerberos, NTLM, Hibun Security Logs |
| **External Brute-Forced Successful Login** | `external_user_success_brute_forcer` | 90 | Brute Force (`T1110`) | Source IP Based, User ID Based |
| **Internal Brute-Forced Successful Login** | `internal_user_success_brute_forcer` | 95 | Brute Force (`T1110`) | Source IP Based, User ID Based |
| **External Credential Stuffing** | `external_credential_stuffing` | 50 | Brute Force (`T1110`) | Monitorea fallos masivos vs AWS, Okta, Windows |
| **Internal Credential Stuffing** | `internal_credential_stuffing` | 75 | Brute Force (`T1110`) | Monitorea fallos masivos en servicios de autenticación locales |
| **External Password Spraying** | `external_password_spray` | 50 | Password Spraying (`T1110.003`) | Identifica contraseñas probadas contra usuarios desconocidos |
| **Internal Password Spraying** | `internal_password_spray` | 75 | Password Spraying (`T1110.003`) | Idem anterior, ejecutado desde hosts de la red interna |
| **External User Login Failure Anomaly** | `external_user_login_fail` | 30 | Brute Force (`T1110`) | Múltiples fuentes combinadas (SSH, RDP, SMB, Okta, etc.) |
| **Internal User Login Failure Anomaly** | `internal_user_login_fail` | 60 | Brute Force (`T1110`) | Múltiples fuentes internas combinadas (AD, NTLM, Kerberos, etc.) |

---

## 5. Explotación de Vulnerabilidades y Escaneos (Network Anomalies)

### Exploited C&C Connection
* **Descripción:** Un host interno identificado previamente con vulnerabilidades inicia una conexión saliente directa hacia la dirección IP que originalmente lo atacó. Fuerte indicador de explotación exitosa.
* **XDR Event Name:** `exploit_attempt_correlation` | **Severidad:** 75
* **MITRE ATT&CK:** Initial Attempts | Technique: XDR Command and Control Connection Exploitation (XT2014)
* **Campos de Supresión:** `srcip` y `dstip` del registro original de intento de exploit.
* **Campos Clave:** `exploit_id`, `seen_traffic_id`.

### External / Internal Exploited Vulnerability
* **Descripción:** Correlación en la que un ataque detectado por las firmas de IDS coincide exactamente con el identificador CVE de una vulnerabilidad previamente reportada en ese host por herramientas de escaneo de seguridad corporativas.
* **XDR Event Name:** `external_vuln_exploit_correlation` (Sev 75) / `internal_vuln_exploit_correlation` (Sev 75)
* **MITRE ATT&CK:** Initial Attempts / Exploration | Technique: XDR Exploited Vulnerability (XT2015)
* **Campos de Supresión:** `srcip`, `dstip`, `ids.cve` del log de escaneo.
* **Campos Clave:** `vulnerability.cve`, `ids.cve`, `vulnerability_id`.

### External / Internal Firewall Denial Anomaly
* **Descripción:** Un host infringe las políticas de seguridad y es bloqueado por el firewall una cantidad de veces inusualmente alta en comparación con el comportamiento histórico de la red.
* **XDR Event Name:** `external_fw_action` (Sev 40) / `internal_fw_action` (Sev 60)
* **MITRE ATT&CK:** Initial Attempts / Exploration | Technique: XDR Firewall Anomaly (XT2002)
* **Campos de Supresión:** `srcip_host`
* **Campos Clave:** `actual`, `typical`, `dev_name`, `engid_name`.

### External / Internal Firewall Policy Anomaly
* **Descripción:** Tráfico que activa una regla de firewall que nunca o casi nunca (`days_silent`) se había invocado en la red.
* **XDR Event Name:** `external_fw_policy_id` (Sev 20) / `internal_fw_policy_id` (Sev 40)
* **MITRE ATT&CK:** Initial Attempts / Exploration | Technique: XDR Firewall Anomaly (XT2002)
* **Campos de Supresión:** `fw_policy_id`
* **Campos Clave:** `days_silent`, `dev_name`, `srcip_host`, `dstip_host`.

### External / Internal Handshake Failure
* **Descripción:** Picos masivos de fallos de negociación/handshake entre dos hosts, indicando escaneos agresivos de puertos o denegación de servicio.
* **XDR Event Name:** `external_handshake_failure` (Sev 10) / `internal_handshake_failure` (Sev 10)
* **MITRE ATT&CK:** Reconnaissance (`TA0043`) / Discovery (`TA0007`) | Technique: Active Scanning (`T1595`) / Network Service Scanning (`T1046`)
* **Campos de Supresión:** `srcip`, `dstip`, `appid_name`

### External / Internal IDS/IPS Signature Spike
* **Descripción:** Un host transmite o genera un volumen anómalo de firmas únicas de IDS/IPS. Al calcular el volumen, Stellar Cyber pondera los exploits según criticidad: **Crítico cuenta como 2, Alto como 1, Bajo como 0.5**.
* **XDR Event Name:** `external_ids_signature_spike` (Sev 50) / `internal_ids_signature_spike` (Sev 65)
* **MITRE ATT&CK:** Exploit Public-Facing Application (T1190) / Lateral Movement (TA0008)
* **Campos de Supresión:** `srcip`
* **Campos Clave:** `actual`, `typical`, `event_summary.ids_signatures_summarize`.

### External / Internal IP / Port Scan Anomaly
* **Descripción:** Escaneos dirigidos. Se divide en dos sub-algoritmos: Fallos masivos de conexión tripletas IP:Puerto (Sensor Traffic) o picos de conexiones masivas (Firewall/Windows). El análisis interno (lateral) es mucho más sensible a los umbrales de activación que el externo.
* **XDR Event Name:** `external_port_scan` (Sev 10) / `internal_port_scan` (Sev 40)
* **Campos de Supresión:** `srcip`
* **Campos Clave:** `num_failed`, `num_successful`, `percent_failed`, `summary_port_scan_type`.

### Private to Private / Public Exploit Anomaly & Signature Spikes
* **Descripción:** Correlaciones cruzadas basadas en la dirección de direccionamiento (Privado a Privado / Privado a Público / Público a Privado). Alerta sobre anomalías de firmas IDS e IPS basadas en volumetría e impacto de las acciones tomadas (`ips.action`). Una IP privada inicia un gran número de intentos de explotación identificados por una firma, o un intento de explotación raramente visto hacia otra IP.
* **Direccionamiento (Internal vs External):** Las direcciones con `srcip_type` y `dstip_type` como `private` se consideran internas. Las comunicaciones donde ambos son privados son "Internal communications" (Priv-Priv). El motor siempre marca `srcip` como el IP iniciador, independientemente de la dirección del flujo de datos en la firma IDS (INBOUND/OUTBOUND).
* **XDR Event Names:** `exploit_attempt_priv_priv` (Sev 75), `exploit_attempt_priv_pub` (Sev 60), `exploit_attempt_pub_priv` (Sev 60), `exploit_attempt_pub_pub` (Sev 50).
* **Subtipos:** 
  * `ids_traffic_anomaly`: El número de firmas IDS únicas, ponderado por severidad, se calcula periódicamente.
  * `ips_traffic_anomaly`: Igual que IDS, pero incluye la acción tomada (`ips.action`) que afecta la fidelidad de la alerta.
* **Cálculo de Anomalía Volumétrica (`actual` vs `typical`):** Se ponderan firmas: `critical` suma 2, `high` suma 1, `low` suma 0.5, otras suman 1.
* **MITRE ATT&CK:** Lateral Movement (TA0008) / Exploitation of Remote Services (T1210).
* **Campos de Supresión:** `ids.signature`, `ips.signature` (deduplica alertas que comparten la misma firma).

---

## 6. Monitoreo de Protocolos Críticos (SMB, LDAP, DNS, ICMP, RDP)

### Tráfico de Red e Inyecciones SMB (Basado en Reglas)
Detecciones deterministas de firmas de explotación de Windows sobre recursos compartidos y Named Pipes:

* **BloodHound Enumeration Activity** (`network_security_bloodhound_enumeration_activity`): Escaneos LDAP masivos buscando vectores de ataque en AD (`objectclass=trusteddomain` u `objectclass=*`).
* **DCERPC SMB Spoolss Named Pipe** (`network_security_win_security_dce_rpc_smb_spoolss_named_pipe`): Tráfico sospechoso apuntando a pipes de impresión (implicaciones de spooler/privilegios).
* **Impacket PsExec / SecretDump Execution** (`network_security_win_security_impacket_psexec` / `network_security_impacket_secretdump`): Movimiento lateral e intentos remotos de volcado de credenciales de Impacket vía SMB.
* **Possible PetitPotam Coerce Authentication Attempt** (`network_security_petitpotam_network_share`): Intento de forzar autenticación (coerción) abusando de funciones de red de Windows.
* **Remote Service / Task Creation via Named Pipes** (`network_security_win_security_svcctl_remote_service` [vía SVCCTL] / `..._atsvc_task` [vía ATSVC]): Manipulación remota de servicios y tareas programadas sobre SMB.
* **Startup/Logon Script Added to GPO** (`network_security_win_group_policy_iniscript`): Modificaciones anómalas de archivos `.ini` en scripts de inicio de políticas de grupo.
* **T1047 Wmiprvse Wbemcomn DLL Hijack** (`network_security_win_security_wmiprvse_wbemcomn_dll_hijack`): Secuestro de DLLs sobre procesos WMI detectado en tráfico de red.
* **Windows Network Access Suspicious desktop.ini Action** (`network_security_net_share_obj_susp_desktop_ini`): Modificación o lectura anómala de archivos ocultos de configuración de carpetas de red.

### Anomalías de Lectura/Escritura SMB y Enumeración de Usuarios
* **External / Internal SMB Read Anomaly:** Tasa inusualmente alta de solicitudes de lectura SMB (`actual` vs `typical`).
* **External / Internal SMB Write Anomaly:** Volumen anómalo de solicitudes de escritura (posible despliegue masivo de archivos o ransomware de red).
* **External / Internal SMB Username Enumeration:** Un único host de origen realiza intentos de inicio de sesión SMB utilizando al menos 5 usuarios únicos con un fallo intermedio, o al menos 10 usuarios únicos en total.
* **XDR Event Names:** `..._smb_read_anomaly`, `..._smb_anomaly`, `..._smb_user_scan`.

### Anomalías DNS y Dominios Maliciosos
* **DGA (Domain Generation Algorithm):** Rastrea consultas hacia dominios inexistentes (`NXDOMAIN`). Al cruzar ciertos umbrales de entropía, se detectan dominios resolubles generados matemáticamente.
* **DNS Query to Anonymous File Upload Domains:** Consultas dirigidas a plataformas de hosting anónimo utilizadas frecuentemente para exfiltrar información.
* **DNS Query to External Service Interaction Domains:** Peticiones DNS orientadas a plataformas de interacción fuera de banda (OAST) utilizadas post-explotación exitosa de RCE (ej: Interactsh, Burp Collaborator).
* **DNS Query to Monero Mining Pools / TOR Proxy Domain:** Intentos de resolución de pools de minado XMR o de dominios `.onion` de la red TOR.
* **DNS Tunneling Anomaly:** Tráfico con alta densidad de información (entropía) encapsulado en registros DNS corporativos. Severidad: 98.
* **Recently Registered Domains / Uncommon Top-Level Domain Anomaly:** Consultas a sitios web creados hace menos de 90 días o con TLDs inusuales (ej. `.zip`, `.click`, `.lol`) utilizados para evadir listas negras reputacionales.

### Amenazas y Ataques sobre RDP (Remote Desktop Protocol)
* **External / Internal RDP BlueKeep:** Escaneos o intentos de explotación dirigidos a la vulnerabilidad crítica CVE-2019-0708.
* **External / Internal RDP Brute Force Attack:** Picos masivos de conexiones RDP entrantes frente a las líneas base habituales del servidor.
* **External / Internal RDP Suspicious Outbound:** Conexión al puerto TCP 3389 iniciada por procesos y herramientas no estándar (Herramientas estándar permitidas: `mstsc.exe`, `RDCMan.exe`, `mRemoteNG.exe`, navegadores como `chrome.exe`, etc. Cualquier otro binario ejecutor detona la alerta).
* **RDP Registry Modification / Port Opening:** Modificación de llaves críticas de registro (`fDenyTSConnections`, `UserAuthentication`) para forzar la habilitación de escritorios remotos o ejecuciones de `netsh` para abrir el puerto 3389.
* **RDP Reverse Tunnel / Session Hijacking:** Un proceso `svchost` que aloja servicios de terminal interactúa sospechosamente con la dirección de loopback local (`127.0.0.1`), o uso ilícito de `tscon.exe` / MSTSC shadowing para secuestrar sesiones activas.
* **RDP Suspicious Logon / Logon Attempt:** Inicios de sesión RDP autenticados que reportan un direccionamiento de origen local (indicio de túnel SSH/RDP inverso) o intentos de conexión remota por parte de usuarios sin privilegios explícitos para iniciar sesión remotamente.

---

## 7. Cloud Security (AWS, Azure, OCI, Google Workspace y O365)

### Amazon Web Services (AWS)
* **AWS AMI Made Public:** Una Amazon Machine Image privada es expuesta al acceso público de Internet de manera anómala.
* **AWS Default VPC Configuration:** Implementación o uso de las configuraciones por defecto de las VPCs de AWS.
* **AWS EC2 Security Group Deleted / Exposed High-Risk Ports:** Eliminación de grupos de seguridad o adición de reglas que exponen puertos de alto riesgo (SSH, RDP, DBs) directamente a Internet (`0.0.0.0/0`).
* **AWS IAM Policy with Wildcard Privileges:** Asignación de políticas IAM excesivamente permisivas que contienen comodines (`*`).
* **AWS Logging Stopped:** Desactivación deliberada de los logs de auditoría en AWS CloudTrail.
* **AWS S3 Bucket Missing Server-Side Encryption / Public Policy:** Almacenamiento en S3 sin cifrado en reposo o con políticas de acceso público no autorizadas.
* **AWS S3 Ransomware:** Comportamiento masivo de cifrado, borrado o alteración de objetos dentro de buckets S3. Severidad: 90.
* **Otras Actividades Sospechosas de AWS:** `aws_malicious_activity`, `aws_suspicious_ebs_activity`, `aws_suspicious_iam_activity`, `aws_suspicious_root_account_activity`, `aws_suspicious_vpc_flow_logs_modification`.

### Microsoft Azure & Entra ID
* **Azure Application Gateway Changed / DNS Zone Changed / CloudShell Created / Security Configuration Changed:** Modificaciones en componentes clave de enrutamiento, DNS público, consolas CloudShell aprovisionadas o alteraciones de seguridad.
* **Microsoft Entra Apps Modified to Allow Multi-Tenant Access:** Modificación sospechosa de los alcances de una aplicación empresarial registrada para permitir accesos Multi-Tenant externos.
* **Reglas Basadas en Eventos de Microsoft Entra ID:**
    * `azure_application_configuration_changes` (Cambios de configuración)
    * `microsoft_entra_app_deleted` (Eliminación de aplicaciones corporativas)
    * `azure_application_permission_changes` (Modificación de permisos y API Scopes)
    * `azure_bitlocker_key_retrieval` (Extracción de llaves de recuperación BitLocker)
    * `azure_suspicious_changes_to_conditional_access_policy` (Alteración de políticas de Acceso Condicional)
    * `azure_changes_to_device_registration_policy` (Cambios en registro de nuevos dispositivos)
    * `azure_changes_to_privileged_account` / `..._privileged_role_assignment` / `..._pim_setting_changed` (Asignación y elevación de roles privilegios o alteración del módulo PIM - Privileged Identity Management)
    * `azure_discovery_using_azurehound` (Uso de herramientas de auditoría ofensiva de identidades AzureHound)
    * `azure_mfa_disabled` (Desactivación de factores de autenticación multi-factor)
    * `azure_sign_in_failures` / `azure_suspicious_sign_in_activity` (Inicios de sesión fallidos o anómalos en Azure corporativo)

### Oracle Cloud Infrastructure (OCI) - *Early Access*
Alertas diseñadas específicamente para telemetría nativa de infraestructura de Oracle:
* `oci_discovery_activity` (Descubrimiento de infraestructura en la nube)
* `oci_insecure_metadata_endpoint` / `oci_instance_metadata_access` (Ataques o accesos a endpoints de metadatos sensibles IMDS)
* `oci_insecure_nfs_export_configuration` (Configuraciones inseguras de almacenamiento compartido NFS)
* `oci_unexpected_user_agent` (Interacciones con la API de OCI utilizando User Agents anómalos o de herramientas de hacking)
* `suspicious_oci_configuration_change_to_network_security_group` / `..._modification_of_route_table` (Modificaciones de seguridad de red y tablas de ruteo)
* `suspicious_oci_bucket_enumeration` / `..._bucket_public_access_type_configuration` (Escaneos o exposición pública de almacenamiento OCI Buckets)
* `suspicious_oci_cross_tenancy_communication` (Peticiones salientes desde un Tenant de OCI apuntando a otra infraestructura de Tenancy externa, fuerte indicador de movimiento lateral multinube)
* `suspicious_oci_event_rule_deletion` / `oci_logging_activity` (Evasión de auditoría mediante eliminación de reglas de eventos o logs)
* `suspicious_oci_iam_activity_impact` / `..._persistence` (Ataques dirigidos a la capa de gestión de accesos e identidades de Oracle)

### Google Workspace (GSuite)
* **Google Workspace Account Manipulation:** El centro de seguridad de Google reporta filtraciones de credenciales corporativas o suspensiones de seguridad de cuentas críticas.
* **Google Workspace Attack Warning:** Alertas directas de intentos persistentes de vulneración de identidades contra un usuario de la organización.
* **Google Workspace Suspicious Activities / User Suspended:** Eventos anómalos de inicio de sesión o suspensiones operativas directas dentro de la suite de colaboración corporativa.
* **XDR Event Names:** `gsuite_account_manipulation`, `gsuite_attack_warning`, `gsuite_suspicious_activities`, `gsuite_user_suspended`.

### Office 365 (O365) & Microsoft Exchange Cloud
* **Office 365 Admin Audit Logging Disabled:** Desactivación de logs administrativos, anulando la visibilidad del SOC.
* **Office 365 Content Filter / Malware Filter Policy Changed:** Alteración de las políticas anti-spam y anti-malware de Exchange, permitiendo el ingreso controlado de correos con adjuntos maliciosos.
* **Office 365 File Sharing with Outside Entities:** Detección de cuentas compartiendo múltiples documentos con dominios y correos fuera del perímetro corporativo.
* **Office 365 Multiple Files Restored / Multiple Users Deleted:** Acciones masivas e inusuales de restauración de archivos (indicios de secuestro previo) o purga masiva de identidades dentro de los tenants.
* **Office 365 Network Security / Password / Sharing Policy Changed:** Cambios atípicos a nivel organizativo en las políticas globales de seguridad de contraseñas o compartición.
* **Office365 Rare Operations:** Ejecución de operaciones inusuales y de baja frecuencia directamente sobre buzones de correo empresariales.
* **Suspicious Office365 Inbox Rule / Mail Transport Rule:** Creación de reglas ocultas en los buzones de los usuarios (ej. redirigir correos entrantes a carpetas ocultas o reenviarlos externamente) técnicas clave para Business Email Compromise (BEC).

---

## 8. Web Application Firewall (Anomalías WAF)

### WAF Internal Attacker Anomaly
* **Descripción:** Solicitudes HTTP internas originadas desde direccionamientos IP privados son bloqueadas o alertadas de forma masiva por el WAF corporativo. Fuerte indicio de un activo interno comprometido atacando los aplicativos web propios.
* **XDR Event Name:** `waf_internal_attacker` | **Severidad:** 60
* **Soporte de Ingesta:** F5 BIG-IP / Silverline WAF, Barracuda WAF, AWS CloudWatch WAF, Imperva Incapsula.
* **Campos Clave:** `srcip`, `action`, `event.severity_str`, `event.uri`, `event.reason`.

### WAF Rule Violation Anomaly
* **Descripción:** Incremento masivo o pico estadístico en la activación de reglas del WAF, o invocación de una firma de seguridad web que históricamente se reporta como inactiva en el entorno de producción.
* **XDR Event Name:** `waf_rule_violation` | **Severidad:** 50
* **Campos de Supresión:** `event.sig_id`
* **Campos Clave:** `actual`, `typical`, `event.web_application_name`, `event.uri`, `event.reason`.

---

## 9. La Matemática del Riesgo (Entity & Case Scoring)

A diferencia de los SIEM tradicionales que suman alertas de forma lineal, el motor de Machine Learning de Stellar Cyber procesa el riesgo en dos capas: **Scores de Entidades (Asset/User)** y **Scores de Casos (Incidentes Correlacionados)**.

### Cálculo del Risk Score en Activos y Usuarios
El score de riesgo de un activo o usuario es dinámico, se calcula **cada 10 minutos** y procesa una ventana deslizante de las **últimas 24 horas** de actividad.

* **Penalización por Diversidad:** El algoritmo castiga más la presencia de *múltiples tipos de alerta diferentes* que una gran cantidad de eventos repetidos del mismo tipo. Si un host genera 100 alertas de escaneo de puertos, su impacto en el riesgo es menor que si genera 1 alerta de escaneo, 1 de persistencia y 1 de movimiento lateral.
* **El Multiplicador de Importancia (Criticality):** Los activos tienen un nivel de importancia asignado (Low, Medium, High, Critical). El nivel actúa como un multiplicador directo: el mismo set de alertas generará un score drásticamente más alto en un Domain Controller o un servidor productivo expuesto a Internet que en una laptop de pruebas.
* **Remediacióm en Tiempo Real:** Si un analista **cierra** un evento de seguridad (Status: *Closed* o *Resolved*), este se elimina automáticamente del siguiente cálculo de 10 minutos, provocando que el score del activo o usuario baje de inmediato.

### La Fórmula Matemática de los Casos (Cases)
Cuando el motor de grafos agrupa múltiples alertas correlacionadas en un solo caso unificado (incidente), calcula el `final_score` del caso utilizando la siguiente ecuación de normalización:
`final_score = (total_score^2) / 100.0`
Donde `total_score` es la combinación ponderada de los `event_score` individuales de todos los tipos de alerta involucrados. Esto causa un crecimiento exponencial: a mayor variedad de tácticas detectadas en el incidente, el score escala rápidamente hacia el rango Crítico (>= 75).

---

## 10. Impossible Travel: Umbrales y Evasión de Falsos Positivos

### Los Umbrales Físicos
Para la detección analítica de viajes imposibles (`user_impossible_travel`), Stellar Cyber evalúa secuencialmente dos inicios de sesión exitosos bajo las siguientes constantes físicas:
* **Distancia de Activación:** Los dos puntos geográficos calculados deben estar separados por una distancia geodésica mínima de **100 millas**.
* **Velocidad de Vuelo Comercial:** El umbral analítico está configurado bajo la velocidad de la aviación comercial estándar (**600 millas por hora**). Si la velocidad requerida para moverse entre ambas ubicaciones supera este límite, la alerta se dispara.

### Estrategia de Ingeniería contra VPNs e iCloud Private Relay
Campos de Enriquecimiento Críticos en el JSON para filtrar falsos positivos de Zscaler/GlobalProtect/Apple Relay:
* `asn_seen_before` (boolean): Indica si el usuario ya se ha autenticado previamente desde ese Sistema Autónomo.
* `asn_org_seen_before` (boolean): Indica si la organización dueña de ese bloque de IPs (ej: *Zscaler Inc.*) ya es conocida en el historial del usuario o del Tenant.
* `user_agent_seen_before` (boolean): Valida si el navegador o cliente que originó el "viaje" es el mismo dispositivo habitual.

**Lógica SOC:** Si `xdr_event.name == "user_impossible_travel"` pero `asn_org_seen_before == true` y `user_agent_seen_before == true`, el evento es un Falso Positivo / Ruido Administrativo causado por un salto de red lógico.

---

## 11. BEC, Phishing e Ingesta de Correo (Análisis JSON Avanzado)

Stellar Cyber procesa vectores iniciales de correo integrándose con Microsoft Graph Security, Proofpoint y Mimecast.
La alerta clave para compromiso de buzón es: `office365_rare_operations`.

**Campos JSON a auditar en incidentes de correo:**
* `office365.Operation`: Búsqueda de `New-InboxRule` o `Set-Mailbox` (Creación de reglas de desvío inmediatamente después de un login anómalo).
* `office365.Parameters`: Cadenas como `ForwardingAddress`, `DeleteMessage` o desvíos a la carpeta `Deleted Items` indican robo y ocultación de correos.
* `dstip_domain_creation`: Un timestamp menor a **14 días** indica enlaces a infraestructura atacante recién registrada.
* `metadata.request.user_agent`: User agents genéricos o headless (Python/Go) que no coinciden con la telemetría corporativa (`Microsoft Office/16.0`).
