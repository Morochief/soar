# Plantillas de Cierre SOC (Stellar Cyber)

Este documento contiene las respuestas estandarizadas para el cierre de incidentes recurrentes en la plataforma Stellar Cyber. El objetivo es mantener consistencia en la auditorÃ­a, reducir el MTTR y alimentar correctamente los modelos de Machine Learning.

## 1. InstalaciÃ³n de Software LegÃ­timo / Herramientas TI (Ej: RustDesk, Controladores)
**CategorÃ­a:** Falso Positivo
**Contexto:** Alertas de Cortex XDR (BIOC) o similares por ejecuciÃ³n de instaladores o herramientas de administraciÃ³n remota autorizadas.
**Plantilla:**
> "Alerta descartada como Falso Positivo. El anÃ¡lisis confirma que el ejecutable detectado (`[NOMBRE_ARCHIVO]`) corresponde a una instalaciÃ³n o ejecuciÃ³n legÃ­tima de software corporativo/TI (`[NOMBRE_SOFTWARE]`) en el host `[HOST_O_IP]`. El hash es benigno y no se observa comportamiento post-explotaciÃ³n o movimiento lateral. Actividad autorizada."

## 2. AnomalÃ­as de Red por Windows Update / Delivery Optimization
**CategorÃ­a:** Falso Positivo
**Contexto:** Picos de conexiones detectados por IA (App Usage Anomaly) hacia CDNs de Microsoft o Akamai (`windows_update`, `windows_marketplace`).
**Plantilla:**
> "Alertas analÃ­ticas de red descartadas como Falso Positivo. La investigaciÃ³n de la telemetrÃ­a confirma que el host `[IP_ORIGEN]` estaba ejecutando descargas concurrentes de parches de Windows Update a travÃ©s del servicio Delivery Optimization. Las peticiones apuntaron exclusivamente a CDNs legÃ­timos. Actividad benigna de mantenimiento."

## 3. AnomalÃ­as de Procesos por Mantenimiento en Servidores Linux (unattended-upgrades / dpkg)
**CategorÃ­a:** Falso Positivo
**Contexto:** Alertas de Command Anomaly o Uncommon Process disparadas en Linux porque procesos como `dpkg` o `systemd` se actualizan tras largos periodos de inactividad.
**Plantilla:**
> "ClÃºster de alertas descartado como Falso Positivo. El anÃ¡lisis de causa raÃ­z sobre la telemetrÃ­a de Auditbeat confirma que los comandos inusuales detectados (`[PROCESOS]`) fueron generados legÃ­timamente por rutinas de mantenimiento (ej: `unattended-upgrades`, `dpkg`) durante el ciclo automÃ¡tico de instalaciÃ³n de parches. No existe actividad maliciosa."

## 4. Fallos Operativos de EDR (Ej: Sophos Update Failure)
**CategorÃ­a:** Falso Positivo
**Contexto:** Alertas mapeadas agresivamente como EvasiÃ³n de Defensas (Impair Defenses / T1562) que en realidad son errores de software del agente de seguridad.
**Plantilla:**
> "Alerta descartada como Falso Positivo. Se revisÃ³ la telemetrÃ­a del EDR (Sophos), determinando que el evento original es un fallo operativo de actualizaciÃ³n (`[TIPO_DE_ERROR]`). Stellar Cyber mapeÃ³ errÃ³neamente este error de software a la tÃ¡ctica de EvasiÃ³n de Defensas (T1562). No hay indicios de manipulaciÃ³n intencional por malware. Se recomienda a soporte TI verificar el agente."

## 5. Anomalía de Lectura SMB por Sincronización GPO
**Categoría:** Falso Positivo
**Contexto:** Alertas de Internal SMB Read Anomaly disparadas por lectura de políticas en el Controlador de Dominio (SysVol/IPC$).
**Plantilla:**
> "Alerta descartada como Falso Positivo. El análisis de metadatos SMB y las trazas de red confirman que los picos de lectura hacia el Controlador de Dominio se limitan a recursos compartidos administrativos (\SysVol, \IPC$) con el objetivo de actualizar y sincronizar políticas de grupo (GPO - gpt.ini). Comportamiento legítimo y esperado en infraestructura Active Directory."

### Plantilla 5: Falso Positivo por Filtrado Web (WebControlViolation)
**Uso:** Cuando Stellar Cyber marca User Execution (T1204) pero el log original indica que Sophos bloqueó la navegación del usuario por políticas de categoría web (Ej. Traductores, Streaming).
**Resolution Tag:** False Positive
**Comentario:**
> Alerta descartada como falso positivo. Tras revisar la telemetría base, se confirma que el evento original de Sophos es un simple WebControlViolation debido a que el usuario intentó acceder a una URL bloqueada por política de filtrado corporativo. No hubo ejecución de código malicioso ni intención ofensiva. Mapeo exagerado de táctica T1204 en el SIEM.

> Alerta descartada como falso positivo. Tras revisar la telemetría base, se confirma que el evento original de Sophos es un simple WebControlViolation debido a que el usuario intentó acceder a una URL bloqueada por política de filtrado corporativo. No hubo ejecución de código malicioso ni intención ofensiva. Mapeo exagerado de táctica T1204 en el SIEM.

## 6. Falso Positivo por Firmas IDS Informativas / APIs Benignas
**CategorÃ­a:** Falso Positivo
**Contexto:** Alertas disparadas por firmas IDS de baja severidad que detectan trÃ¡fico a servicios de marketing, telemetrÃ­a o APIs comunes (Ej: Clearbit).
**Plantilla:**
> "Alerta descartada como Falso Positivo. El anÃ¡lisis de la consulta confirma que la firma IDS se disparÃ³ debido a un patrÃ³n esperado y benigno hacia un servicio comercial o API pÃºblica (Ej. descarga de recursos web, marketing). No existe impacto en CIA ni comportamiento malicioso asociado."

## 7. AnomalÃ­a EstadÃ­stica de Machine Learning (TLD Inusual / Cloud Load Balancers)
**CategorÃ­a:** Falso Positivo
**Contexto:** El motor de ML dispara alertas de anomalÃ­a (ej. Uncommon Top-Level Domain) basÃ¡ndose en dÃ­as de inactividad hacia TLDs raros, pero que en realidad pertenecen a infraestructura Cloud legÃ­tima (Ingress Nginx, AWS, GCP).
**Plantilla:**
> "Alerta descartada como Falso Positivo. Tras el anÃ¡lisis de los metadatos de red, se comprueba que el evento originado fue disparado exclusivamente por comportamiento estadÃ­stico (dominio o patrÃ³n no visto en X dÃ­as) por el motor de ML. El destino resuelto pertenece a una infraestructura legÃ­tima de nube, sin riesgo de Command and Control ni fuga de datos."

## 8. Persistencia Temporal RunOnce por Instaladores WiX / Burn (Instalación o Desinstalación)
**Categoría:** Falso Positivo
**Contexto:** Alertas de Cortex XDR o EDRs asociadas a persistencia (T1547.001) por la escritura temporal de ejecutables en la clave `RunOnce` bajo parámetros de limpieza `/burn.runonce` o `-burn.clean.room`.
**Plantilla:**
> "Alerta descartada como Falso Positivo. El análisis confirma que la adición del ejecutable (`[NOMBRE_ARCHIVO]`) a la clave de registro `RunOnce` corresponde a una operación temporal y legítima de instalación o desinstalación de software corporativo (`[NOMBRE_SOFTWARE]`) utilizando el empaquetador WiX Toolset / Burn. El binario está firmado digitalmente por una entidad confiable (`[FIRMA_VENDOR]`) y no presenta comportamiento anómalo posterior."

## 9. Resoluciones DNS de Servicios de Comunicación / Redes Sociales (Discord, Slack, WhatsApp)
**Categoría:** Falso Positivo
**Contexto:** Alertas de exploit o anomalías estadísticas (NBA/IDS) detonadas por resoluciones de dominio ordinarias hacia plataformas de mensajería o colaboración.
**Plantilla:**
> "Alerta descartada como Falso Positivo. Tras revisar la telemetría base, se confirma que el evento original corresponde a una resolución DNS ordinaria hacia la plataforma de comunicación `[PLATAFORMA]` (`[DOMINIO]`) por el uso de la aplicación o navegador del usuario en el host `[HOST]`. La firma IDS detectada es informativa y no representa indicio de comportamiento ofensivo ni canales C2."

## 10. Falso Positivo: Ruido Administrativo de Exchange (HealthMailbox)
**Categor�a:** Falso Positivo
**Contexto:** Alertas de internal_user_login_fail o fuerza bruta donde el origen es un servidor interno y el usuario atacado es HealthMailbox (Event ID 4768, Status 0x6).
**Plantilla:**
> "Alerta descartada como falso positivo de acuerdo con la memoria institucional SOC. Los fallos masivos de autenticaci�n (Event 4768, Status 0x6) intentan validar cuentas sint�ticas 'HealthMailbox' de Microsoft Exchange que ya no existen en el dominio local. Esto obedece a un proceso residual de 'Managed Availability' (deuda t�cnica). No representa riesgo de fuerza bruta ni de seguridad. Se recomienda aplicar regla de supresi�n para este origen."


## 11. IDS Falso Positivo - SNMP Broadcast (Descubrimiento L2)
**Categor�a:** Falso Positivo
**Contexto:** Alertas de Exploit Anomaly detonadas por consultas SNMP v1/v2c (community: public) desde equipos locales hacia la IP de broadcast.
**Plantilla:**
> 'Se investiga la alerta catalogada como Exploit Anomaly. Tras el an�lisis, se constata que la detecci�n se debe a un falso positivo de la regla IDS (GPL SNMP public access udp). El origen gener� r�fagas de consultas SNMP utilizando la community string 'public' dirigidas a la IP de broadcast de su propia subred. Este comportamiento corresponde a descubrimiento local de red (ej. b�squeda de impresoras o agentes de gesti�n) y no representa un escaneo malicioso ni riesgo de compromiso. Se cierra como Falso Positivo.'

## 12. IDS Falso Positivo - DNS Tunneling por Servicios Cloud
**Categoría:** Falso Positivo
**Contexto:** Alertas de DNS Tunneling (Anomaly) detonadas por volumetría y entropía hacia dominios de Microsoft u otros proveedores Cloud (ej. powerplatform.com, azure-apim.net).
**Plantilla:**
> "Se investiga la alerta de DNS Tunneling. El análisis demuestra que no existe ningún túnel activo ni exfiltración. El motor de ML generó un falso positivo al evaluar la longitud y entropía de las consultas DNS dirigidas a dominios Cloud legítimos (ej. Azure, Power Apps). El volumen de bytes inusual es resultado de las extensas cadenas de resolución CNAME (Traffic Manager) y el uso de GUIDs en los URLs, comportamiento estándar de plataformas de nube. Se cierra la alerta sin acción requerida."

## 6. IDS Falso Positivo - Conexiones AnyDesk (Remote Access)

**Contexto:** Alertas de Exploit Attempt / Command & Control disparadas por resoluciones DNS hacia la infraestructura de AnyDesk (.net.anydesk.com).

> "Alerta descartada como Falso Positivo. Se analizÃ³ la traza de red, confirmÃ¡ndose que el trÃ¡fico catalogado como 'Exploited C&C Connection' corresponde en realidad a una cadena de resoluciones DNS (internas y externas) legÃ­timas hacia el software comercial de control remoto AnyDesk. Los endpoints resuelven dominios de su infraestructura (boot.net.anydesk.com y relay-*.net.anydesk.com). Sin indicadores de persistencia anÃ³mala ni tÃºneles maliciosos. OperaciÃ³n administrativa estÃ¡ndar."


### [FALSO POSITIVO] Generic ML PUA - System.dll (NSIS)
**Veredicto:** Falso Positivo (Software no estÃ¡ndar).

**JustificaciÃ³n TÃ©cnica y Forense:**
Se concluye la investigaciÃ³n de la alerta "Generic ML PUA". La alerta fue detonada por la extracciÃ³n de la librerÃ­a System.dll empaquetada con UPX en las carpetas temporales. El anÃ¡lisis confirma que el proceso desencadenante operÃ³ como un empaquetador del framework NSIS. El anÃ¡lisis del Lineage revela que el proceso padre directo fue svchost.exe, demostrando automatizaciÃ³n en segundo plano por el sistema. El anÃ¡lisis estÃ¡tico en VirusTotal certifica que la DLL es benigna. La auditorÃ­a del endpoint mediante Live Response resultÃ³ limpia, descartando conexiones o persistencia anÃ³mala.

**ConclusiÃ³n:**
No existe riesgo ni compromiso de la red (TrÃ­ada CIA intacta). Se cierra el incidente de seguridad. Se recomienda escalar un ticket a Soporte TÃ©cnico para la desinstalaciÃ³n del software no estandarizado.
## 13. Firewall Falso Positivo - Internal Firewall Denial Anomaly (SATI Odoo VPN DNS)
**Categoria:** Falso Positivo Operacional
**Contexto:** Alertas de Internal Firewall Denial Anomaly provocadas por la cuenta del proveedor SATI (soporte Odoo) desde conexiones SSL-VPN (pool 10.212.134.0/24) intentando consultar los servidores DNS internos (10.11.1.1 / 10.11.1.2) en el puerto 53 UDP, bloqueadas por la directiva implicita policyid=0 del firewall FG-Technoma.
**Plantilla:**
> "Se procede al cierre del lote de alertas por anomalia de denegacion en firewall tras determinarse que corresponde a un falso positivo operacional generado por el proveedor de soporte Odoo (cuenta de usuario: sati). La estacion de trabajo remota conectada mediante el tunel corporativo SSL-VPN genero consultas DNS (puerto 53) hacia los Controladores de Dominio y servidores DNS internos (10.11.1.1 / 10.11.1.2). Esta actividad deriva del mecanismo de conmutacion por error (failover) del cliente DNS del sistema operativo Windows tras no haber obtenido respuesta en el DNS primario, resultando bloqueado por la directiva de descarte implicito (policyid=0) en el firewall perimetral FG-Technoma. Se audito minuciosamente la totalidad del lote: no existen intentos de conexion hacia puertos criticos ni servicios administrativos (SMB 445, RDP 3389, SSH, HTTP), descartandose movimiento lateral o actividad maliciosa. Incidente clasificado y cerrado formalmente como Falso Positivo."

## 14. Endpoint Falso Positivo - Event::Endpoint::ServiceNotRunning (Actualizacion Transitoria de Sophos)
**Categoria:** Falso Positivo Operacional (Salud de Agente EDR)
**Contexto:** Alertas de Stellar Cyber (Sophos Event: XDR Endpoint Indicator of Threat) disparadas por la notificacion de Sophos Central 'Event::Endpoint::ServiceNotRunning' ('One or more Sophos services are missing or not running'). Ocurre tipicamente durante o inmediatamente despues de un ciclo automatico de actualizacion en el que los servicios (ej. Sophos File Scanner) son desregistrados e instalados de nuevo, superando momentaneamente la ventana de gracia.
**Plantilla:**
> "Se procede al cierre de la alerta tras auditar la estacion de trabajo mediante Live Response y comprobar que la notificacion derivo de un evento transitorio durante el ciclo automatico de actualizacion de componentes de Sophos Endpoint. La revision forense de Health.log constato que a la hora del incidente el instalador desmonto momentaneamente el binario de Sophos File Scanner para sustituirlo por la version actualizada, superando temporalmente el periodo de gracia y disparando la alerta a Central. La telemetria en vivo confirma que todos los servicios y procesos defensivos (Sophos File Scanner Service, HitmanPro.Alert hmpalertsvc, Sophos Endpoint Defense y SntpService) se encuentran activos y en ejecucion (Running Auto), con la proteccion en tiempo real plenamente restaurada. Se forzo la sincronizacion de salud retornando a estado Overall: 0. Incidente cerrado formalmente como Falso Positivo Operacional."

## 15. Endpoint Falso Positivo - Cortex XDR BIOC: route.exe por Cliente VPN (OpenConnect)
**Categor�a:** Falso Positivo / Comportamiento Administrativo Leg�timo
**Contexto:** Alertas de Cortex XDR Analytics BIOC ('Uncommon routing table listing via route.exe' / MITRE T1016) provocadas por clientes VPN de c�digo abierto (OpenConnect-GUI) ejecutando 'cmd.exe /C "route print"' para auditar o configurar el enrutamiento de t�nel en la estaci�n de trabajo.
**Plantilla:**
> "Alerta descartada como Falso Positivo (Benign True Positive). La telemetr�a forense de Cortex XDR confirma que la ejecuci�n de route.exe ('route print') en el host [HOST_O_IP] fue invocada leg�timamente por el cliente VPN corporativo OpenConnect-GUI (openconnect-gui.exe) para inspeccionar la tabla de rutas del sistema operativo durante el ciclo de conexi�n y mantenimiento del t�nel. La regla anal�tica BIOC se deton� por la baja frecuencia hist�rica del comando en el tenant y la firma open-source del software, descart�ndose actividad maliciosa de reconocimiento o evasi�n. Operaci�n leg�tima de software de red."

## 16. Cloud Falso Positivo - Cloud Drive Exfiltration Anomaly por AppSheet / Apps Script
**Categor�a:** Falso Positivo / Comportamiento Empresarial Automatizado (UBA)
**Contexto:** Alertas de Machine Learning (cloud_drive_data_exfiltration_anomaly / MITRE T1567.002) generadas por sincronizaciones de alto volumen de archivos de imagen (firmas y fotograf�as operacionales) mediante Google AppSheet o scripts internos de Google Apps Script.
**Plantilla:**
> "Alerta descartada como Falso Positivo (Benign True Positive). La auditor�a forense de Google Workspace confirma que el volumen at�pico de descargas en Google Drive por parte del usuario [USUARIO] corresponde a la sincronizaci�n automatizada de la plataforma corporativa Google AppSheet y/o Google Apps Script ([APLICACION]). Las solicitudes 'drive.files.get' recuperan leg�timamente anexos operacionales (firmas digitales y fotograf�as de servicio t�cnico) para la compilaci�n de actas y �rdenes de trabajo dentro del tenant institucional. Descartado compromiso de cuenta o fuga hacia almacenamiento externo. Operaci�n benigna autorizada."

## 17. Red Benign True Positive - Port Scan & Firewall Denial Anomaly por Evaluacion de Vulnerabilidades (Nmap / Pentesting Autorizado)
**Categoria:** Benign True Positive / Evaluacion de Seguridad Autorizada
**Contexto:** Alertas de Machine Learning ('internal_port_scan' / 'internal_fw_action') disparadas en el firewall perimetral (FortiGate) por escaneos masivos de puertos e IP (Nmap, Nessus, scanners de red) ejecutados por personal autorizado del equipo de Ciberseguridad / SOC durante tareas de pentesting o auditoria interna.
**Plantilla:**
> "Se concluye la investigacion del lote de alertas de escaneo interno (internal_port_scan) y denegacion anomala en firewall (internal_fw_action) clasificandolo como Benign True Positive. La telemetria de FortiGate (FG-Technoma) registro picos masivos de conexiones y descartes (policyid=0) desde el host [HOST_O_IP] ([USUARIO]) barriendo segmentos de red internos ([SUBNETS_OBJETIVO]) en rangos extendidos de puertos TCP. La actividad fue validada y corroborada formalmente como parte de una evaluacion controlada de vulnerabilidades y escaneo de puertos (Nmap/Pentesting interno) conducido de manera autorizada por el equipo de Ciberseguridad de Technoma. El firewall bloqueo adecuadamente los accesos no autorizados hacia los segmentos protegidos y no existe impacto ni vulneracion a la triada CIA. Incidente cerrado formalmente como actividad tecnica autorizada."

## 18. Identidad Falso Positivo - Login Time Anomaly (Horario Laboral / Acceso Anticipado en Equipo Asignado)
**Categoria:** Falso Positivo / Comportamiento de Usuario Benigno (UBA)
**Contexto:** Alertas de Machine Learning ('user_login_time' / 'Login Time Anomaly' / Event ID 4776 o 4624) disparadas por el motor de User Behavior Analytics (UBA) al registrar inicios de sesion legitimos de colaboradores fuera de su franja tipica (ej. llegadas tempranas antes de las 06:00/07:00 AM o guardias) desde sus estaciones de trabajo habituales.
**Plantilla:**
> "Alerta descartada formalmente como Falso Positivo. La auditoria del registro de seguridad de Windows en el Controlador de Dominio [CONTROLADOR_DOMINIO] corrobora que la validacion de credenciales (Event ID 4776 / 4624) para la cuenta [USUARIO] concluyo exitosamente (Status: 0x0 / STATUS_SUCCESS), originada desde su equipo oficial asignado ([EQUIPO_ORIGEN]). La alerta analitica de UBA (user_login_time) se detono unicamente debido a que el inicio de sesion se produjo en un horario ligeramente anticipado respecto a su franja historica modelada ([FRANJA_TIPICA]), tratandose de un acceso laboral normal a primera hora. Se descartan intentos fallidos, fuerza bruta o saltos laterales. Operacion legitima de usuario con triada CIA intacta."
