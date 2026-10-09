# Guia Operativa de Triaje de Alertas en 7 Etapas (SOC Analyst Standard)
**Integracion con Plataforma Stellar Cyber OpenXDR y Gobernanza Technoma SOC**

---

## 1. Fundamentos del Triaje de Alertas en el SOC

El triaje de alertas es el procedimiento sistematico y estructurado de recibir alertas de seguridad, evaluar su legitimidad, determinar su severidad real y ejecutar la accion operativa correspondiente: cerrar un falso positivo, mitigar un evento operativo o escalar a respuesta a incidentes (DFIR).

El triaje efectivo responde tres interrogantes operativas indispensables:
1. **Es real la alerta?** (Determinacion precisa entre True Positive, False Positive, Benign True Positive o Unclear).
2. **Cual es su gravedad e impacto?** (Evaluacion de criticidad del activo, etapa en la cadena de ataque y radio de explosion).
3. **Que accion ejecutamos a continuacion?** (Cierre justificado en Stellar Cyber, contencion en endpoint, escalacion formal o ajuste de reglas).

---

## 2. El Proceso de Triaje en 7 Etapas

1. [Etapa 1: Ingestion y Centralizacion] (Interflow, EDR, NDR, FW, Syslog)
2. [Etapa 2: Categorizacion y Mapeo] (MITRE ATT&CK, Activos, Tipo de Amenaza)
3. [Etapa 3: Priorizacion por Riesgo] (Criticidad, Etapa, CTI, Score ML vs Baseline, Horario)
4. [Etapa 4: Investigacion y Evidencias] (IOCs, Ventana +/- 30 min, Historial, Alcance Lateral)
5. [Etapa 5: Determinacion y Veredicto] (TP / FP / BTP / Unclear + CIA Triad + Confianza %)
6. [Etapa 6: Escalacion y Respuesta] (SLA 15 min: Tier 1 -> Tier 2/3, Playbooks Technoma)
7. [Etapa 7: Documentacion y Mejora] (Cierre Humanizado Stellar, Bitacora, Tuning Deteccion)

---

### Etapa 1: Ingestion y Centralizacion
Toda alerta recibida por el SOC debe capturarse en la plataforma centralizada (Stellar Cyber OpenXDR / Interflow).
- **Regla de Integridad:** Ninguna fuente de alerta debe ser descartada silenciosamente. Eventos de EDR (Sophos, Cortex), NDR, Firewalls FortiGate, Active Directory y gateways de correo fluyen al lago de datos en formato Interflow estandarizado.
- **Correlacion Multi-Log:** Cuando se analiza un ticket o incidente compuesto por multiples eventos (documentos _doc en Elasticsearch/Stellar), se cuantifica el lote completo y se analiza de forma unificada para no perder la vision global.

### Etapa 2: Categorizacion Estrategica
Se clasifica el incidente segun:
- **Taxonomia de Amenazas:** Exfiltracion de datos, ejecucion no autorizada, anomalia de login, denegacion perimetral, movimiento lateral o comunicacion a dominio sospechoso.
- **Mapeo MITRE ATT&CK:** Identificacion precisa de Tactica (ej. Credential Access, Defense Evasion, Persistence) y Tecnica (ej. T1110, T1078, T1059, T1204).
- **Segmentacion de Activos:** Servidor de Directorio Activo (DC), Servidor de Correo, Base de Datos, Servidor Web DMZ o Estacion de Trabajo de Usuario Final.

### Etapa 3: Priorizacion Dinamica (Scoring Multidimensional)
No todas las alertas ameritan la misma urgencia inmediata. La priorizacion se evalua cruzando 5 factores:
1. **Criticidad del Activo:** Un incidente sobre un Controlador de Dominio (VMBASE8, ad.technoma.local) o un servidor financiero requiere prioridad inmediata frente a una estacion en la red Guest.
2. **Etapa del Ataque:** Un escaneo de reconocimiento temprano permite evaluacion planificada; una ejecucion activa o comunicacion con C2 exige respuesta en tiempo real.
3. **Cruce de Inteligencia de Amenazas (CTI):** Reputacion de IOCs en VirusTotal, AbuseIPDB, URLScan y verificacion en el catalogo CISA KEV (Known Exploited Vulnerabilities).
4. **Score de Anomalia vs. Linea Base (Baseline):** Comparacion del puntaje asignado por los modelos no supervisados de Stellar Cyber contra el comportamiento habitual del host o usuario en los ultimos 30 dias.
5. **Contexto de Negocio:** Evaluacion de si el evento ocurre en horario comercial estandar, fin de semana, madrugada (3 AM) o durante una ventana declarada de mantenimiento de TI.

### Etapa 4: Investigacion y Recoleccion Forense
Recoleccion rigurosa de evidencia objetiva para sustentar el veredicto:
- **IOCs y Artefactos:** Direcciones IP origen/destino, puertos, nombres de dominio (FQDN), hashes SHA256/MD5, rutas completas de archivos y comandos ejecutados.
- **Ventana de Comportamiento (+/- 30 Minutos):** Revision de la actividad previa y posterior inmediata al disparo de la alerta en el endpoint o sensor de red.
- **Patrones Historicos del Activo:** Verificacion de si este mismo evento ya ha ocurrido en el host anteriormente y si fue catalogado como falso positivo justificado en la Memoria Institucional.
- **Alcance Lateral:** Determinacion de si la actividad se encuentra aislada a un unico endpoint o si existe evidencia de barrido/campana afectando a multiples estaciones del dominio.

### Etapa 5: Determinacion y Veredicto (Los 4 Cuadrantes)
El analista emite un dictamen formal e inequivoco en base a 4 estados estandarizados:

| Veredicto | Definicion Tecnica | Accion Operativa |
| :--- | :--- | :--- |
| **True Positive (TP)** | La alerta representa una actividad maliciosa genuina, anomala no autorizada o un compromiso real. | Escalar de inmediato a Tier 2 / IR para contencion activa y aislamiento del host. |
| **False Positive (FP)** | La alerta se disparo sobre una actividad benigna o legitima debido a una firma sobredimensionada o error de log. | Cerrar el caso en Stellar Cyber, redactar la justificacion humanizada y proponer tuning de deteccion. |
| **Benign True Positive (BTP)** | El comportamiento detectado ocurrio realmente, pero corresponde a una actividad autorizada, administrativa o prueba sintetica (ej. HealthMailbox de Exchange, escaneo aprobado de vulnerabilidades). | Cerrar caso con sustento del proceso legitimo y evaluar regla de exclusion. |
| **Unclear (Indeterminado)** | La telemetria y logs disponibles resultan insuficientes para emitir un juicio definitivo con certeza. | Retener caso para recoleccion ampliada o escalar a Analista Senior N2/N3. |

- **Evaluacion de Impacto CIA:**
  - Confidencialidad: C0 (Sin impacto) a C3 (Exposicion masiva confirmada).
  - Integridad: I0 (Sin cambios) a I3 (Modificacion critica de sistemas/archivos).
  - Disponibilidad: A0 (Servicios 100% operativos) a A3 (Interrupcion total de operaciones).
- **Indice de Confianza Analitica:** Calificacion porcentual (0% a 100%) respaldada por la consistencia de la evidencia recolectada.

### Etapa 6: Escalacion y Respuesta (Gobernanza SLA)
- **SLA de Triaje L1 (15 Minutos):** Todo analista Tier 1 debe procesar y dictaminar el caso dentro de la ventana de 15 minutos establecida en el Procedimiento Operativo Estandar (POE).
- **Ruta de Escalacion:**
  - **Tier 1:** Triaje, cierre formal de FP y BTP, clasificacion de TP con paquete de evidencia adjunto.
  - **Tier 2:** Analisis forense profundo en memoria/disco, aislamiento de endpoints en EDR, bloqueo de IPs/dominios en firewall, erradicacion.
  - **Tier 3 / IR Lead / CERT-PY:** Gestion de incidentes criticos mayores, preservacion de cadena de custodia y notificaciones formales regulatorias.
- **Asignacion de Playbook:** Seleccion del playbook operativo oficial correspondiente entre los 28 playbooks de Technoma SOC.

### Etapa 7: Documentacion y Mejora Continua
El cierre de una alerta no es un tramite burocratico, sino la base de la memoria institucional y la optimizacion del SOC:
- **Cierre y Justificacion Humanizada para Stellar Cyber:** Redaccion clara, sin jerga ambigua, explicando que ocurrio y por que el cierre es seguro.
- **Ingenieria de Deteccion (Mitigacion de Alert Fatigue):** Por cada alerta cerrada como FP o BTP, formular la recomendacion tecnica precisa para afinar la regla (whitelist de carpetas, supresion de eventos por combinacion de campos en Stellar Cyber).
- **Bitacora de Auditoria (Excel):** Generacion automatica de la fila unificada para el registro mensual de operaciones del SOC.
- **Gobernanza de Notificaciones (Action Center vs Odoo):** Al tomar un caso o auto-remediar por script/API, nunca forzar el estado 'In Progress'. Asignar unicamente el operador (`assignee`) para registrar el caso y notificar a Slack (`Case assigned`) sin disparar correos a la cola de Odoo (`Case updated`). Para cierres de FP, pasar directamente a `Resolved` asignado al analista.

---

## 3. Plantillas Estandar de Salida

### Plantilla 1: Resumen Ejecutivo (Formato Nativo Stellar)
`markdown
### Resumen Ejecutivo del Caso (Formato Nativo Stellar)

* **Resumen General:** [Parrafo unico resumiendo que ocurrio, autor del evento, activo y contexto institucional].
* **Origen de la Amenaza:** [IP origen, Hostname, ASN, Ubicacion, activo interno o externo].
* **Impacto en el Destino:** [IP destino, puertos, criticidad del host, compromiso real vs bloqueado].
* **Mitigacion y Estado:** [Accion del sensor/firewall/EDR (dropped, denied, blocked, alert)].
`

### Plantilla 2: Cierre Humanizado en Stellar Cyber
El comentario de resolucion debe responder con precision tecnica a un auditor externo sin requerir conocimientos previos del ticket:
`markdown
### Instruccion para Cierre en Stellar Cyber (Cierre Humanizado)

* **Estado:** Closed
* **Resolution Tag:** [False Positive | Benign | True Positive]
* **Comentario de Cierre Maestro (Humanizado para Auditoria):**
> Se realizo la evaluacion forense integral de los eventos correlacionados bajo la alerta [Nombre de la Alerta] en el activo [Hostname/IP].
> 
> La revision de los registros de telemetria ([EDR / Syslog / Firewall]) confirmo que la actividad corresponde a [Explicacion de la causa raiz: proceso institucional legitimo, prueba sintetica de monitoreo o bloqueo perimetral preventivo]. No existio ejecucion de codigo malicioso, compromiso de credenciales ni persistencia en el sistema.
> 
> Caso catalogado como [Falso Positivo Operativo / Evento Benigno Autorizado] con impacto nulo sobre la triada CIA (C0-I0-A0). Se da por concluido el ticket de forma segura.
`

---

## 4. Ejemplos Reales de Cierre Humanizado en Technoma SOC

### Caso A: Fallo de Autenticacion Kerberos por Sondas Exchange HealthMailbox
- **Resolution Tag:** False Positive
- **Comentario Humanizado:**
> Se analizaron los eventos correlacionados de anomalias de login sobre el Controlador de Dominio VMBASE8 (172.16.201.8). Los registros de seguridad de Windows (Event ID 4768) confirman que las solicitudes TGT provienen del servidor Microsoft Exchange VM-MARANDU (172.16.201.4) para la cuenta HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py. Los rechazos corresponden a error Kerberos Status 0x6 debido a una disparidad entre el dominio primario SMTP configurado en el servicio MSExchangeHM y el sufijo UPN registrado en Active Directory. No existe actividad interactiva ni compromiso de credenciales. Descartado como falso positivo operativo y cerrado satisfactoriamente.

### Caso B: Bloqueo de Navegacion por Politica de Web Control en Endpoint
- **Resolution Tag:** False Positive
- **Comentario Humanizado:**
> Se examino la alerta de ejecucion de usuario en el endpoint NBCJPPA25003. La telemetria cruda provista por Sophos Central confirma que el evento se origino por un intento de conexion saliente hacia translate.google.com, el cual fue bloqueado de manera preventiva en la estacion bajo la categoria de navegacion corporativa (WebControlViolation). No existio ejecucion de binarios maliciosos, descarga de artefactos sospechosos ni infeccion del equipo. La clasificacion automatica a MITRE T1204 en Stellar Cyber obedecio a una sobrerepresentacion heuristica. Caso cerrado como falso positivo de amenaza sin impacto en el negocio.

### Caso C: Escaneo Externo Denegado en Firewall Perimetral
- **Resolution Tag:** Benign
- **Comentario Humanizado:**
> Se evaluaron las alertas de intentos de acceso denegados en frontera reportados por el firewall FortiGate (190.104.178.146). Los paquetes TCP SYN dirigidos a puertos de administracion fueron descartados integramente en el perimetro de red (policyid=0, bytes transmitidos=0). No existio penetracion a la red interna, exposicion de servicios corporativos ni degradacion operativa. Actividad atribuible a escaneos oportunistas estandar de internet exitosamente mitigados por las directivas de seguridad perimetral. Caso cerrado como evento benigno contenido.
