# Graded Quiz: Module 4 challenge

**1. ¿Qué software recopila y envía registros (logs) a una herramienta de gestión de eventos e información de seguridad (SIEM)?**
*(Which software collects and sends logs to a security information and event management (SIEM) tool?)*
- [x] Forwarder (Reenviador, ej. Splunk Universal Forwarder) *(Forwarder)*
- [ ] Analizador de protocolos de red *(Network protocol analyzer)*
- [ ] Firewall *(Firewall)*
- [ ] Sistema de detección de intrusos (IDS) *(Intrusion detection system (IDS))*

**2. Examina el siguiente registro (log):**
`[2022/12/21 17:46:35.232748] NOTIFY: NetworkPropertiesUpdated: wifi_psk_13`
**¿Qué tipo de registro es este?**
*(Which type of log is this?)*
- [ ] Ubicación *(Location)*
- [x] Red (Relacionado con Wi-Fi) *(Network)*
- [ ] Autenticación *(Authentication)*
- [ ] Aplicación *(Application)*

**3. Examina el siguiente registro:**
```json
{ 
“name”: “System test”,
“host”: "167.155.183.139",
“id”: 11111,
“Message”: [error] test, 
}
```
**¿En qué formato de registro está esta entrada?**
*(Which log format is this log entry in?)*
- [x] JSON *(JSON)*
- [ ] Syslog *(Syslog)*
- [ ] CSV *(CSV)*
- [ ] XML *(XML)*

**4. Considera el siguiente escenario: A un analista de seguridad en una empresa mediana se le asigna la tarea de instalar y configurar un sistema de detección de intrusos basado en host (HIDS) en una computadora portátil (laptop). El analista de seguridad instala el HIDS y desea probar si funciona correctamente simulando actividad maliciosa. El analista ejecuta programas no autorizados en la computadora portátil, lo que el HIDS detecta con éxito y sobre lo que genera una alerta. ¿De qué es un ejemplo la computadora portátil?**
*(What is the laptop an example of?)*
- [ ] Un reenviador de registros *(A log forwarder)*
- [ ] Un agente *(An agent)*
- [ ] Una firma *(A signature)*
- [x] Un endpoint (punto final) *(An endpoint)*

**5. ¿Qué opción de regla (*rule option*) se utiliza para indicar el número de veces que se actualiza una firma en Suricata/Snort?**
*(Which rule option is used to indicate the number of times a signature is updated?)*
- [ ] `sid` (ID de la firma)
- [x] `rev` (Revisión) *(rev)*
- [ ] `msg` (Mensaje)
- [ ] `tcp` (Protocolo)

**6. Examina esta firma de Suricata:**
`alert http 167.215.72.95 any -> 156.150.71.141 80 (msg:"GET on wire"; flow:established,to_server; content:"GET"; sid:12345; rev:2;)`
**¿Cuál es el puerto de destino?**
*(What is the destination port?)*
- [ ] 2
- [x] 80 *(80)*
- [ ] 12345
- [ ] 141

**7. Completa el espacio en blanco: Suricata utiliza el formato _____ para la salida de eventos y alertas (logs).**
*(Fill in the blank: Suricata uses the _____ format for event and alert output.)*
- [ ] HTML
- [ ] CEF
- [ ] HTTP
- [x] EVE JSON *(EVE JSON)*

**8. ¿Qué lenguaje de consulta utiliza Splunk?**
*(Which querying language does Splunk use?)*
- [ ] SIEM Processing Language
- [ ] Structured Querying Language (SQL)
- [x] Search Processing Language (SPL) *(Search Processing Language)*
- [ ] Structured Querying Language

**9. ¿Qué campo de búsqueda del Modelo de Datos Unificado (UDM) en Google SecOps/Chronicle especifica una acción de seguridad?**
*(Which Unified Data Model (UDM) field search specifies a security action?)*
- [ ] `block`
- [x] `security_result.action` *(security_result.action)*
- [ ] `action`
- [ ] `metadata.event_type`

**10. Completa el espacio en blanco: Las herramientas SIEM _____ los datos sin procesar (*raw data*) para que tengan un formato consistente.**
*(Fill in the blank: SIEM tools _____ raw data so that it is formatted consistently.)*
- [ ] recolectan *(collect)*
- [x] normalizan *(normalize)*
- [ ] procesan *(process)*
- [ ] ingieren *(ingest)*
