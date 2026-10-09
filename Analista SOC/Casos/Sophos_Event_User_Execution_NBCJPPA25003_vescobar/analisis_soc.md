# Reporte SOC - Caso: Sophos Event: User Execution / WebControlViolation (NBCJPPA25003 - vescobar)

**Fecha de Analisis:** 2026-09-03
**Analista:** Analista SOC Senior (DFIR)
**Tenant:** CAJAANDE
**Case ID:** Sophos_Event_User_Execution_NBCJPPA25003_vescobar
**Fuente:** Stellar Cyber XDR / Sophos Central (`sophos_CAJA-ANDE-SOPHOS`)
**XDR Event:** Sophos Event: User Execution (`sophos_event-execution-user_execution`) | Subtipo: `Event::Endpoint::WebControlViolation` | MITRE: T1204 (User Execution) / TA0002 (Execution)

---

> He detectado **2 eventos independientes** en el volcado crudo. El Evento 2 es un duplicado exacto del Evento 1 originado por el reenvío o doble ingesta del mismo registro en el índice de syslog de Stellar. Se procesan de forma secuencial y unificada con su respectivo cierre maestro.

---

## Analisis Evento 1 (Bloqueo WebControlViolation: translate.google.com)

### Tags:
`#FalsoPositivo` `#WebControlViolation` `#SophosCentral` `#CAJAANDE` `#NBCJPPA25003` `#ProxiesAndTranslators` `#PoliticaNavegacion`

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)

- **Origen / Host:** `NBCJPPA25003` | IP: `172.16.202.21` (Segmento LAN corporativo de Caja Ande)
- **Usuario:** `CAJAANDE\vescobar` (ID: `6926ff53e598016d827c8ad4`)
- **Accion de Seguridad:** Bloqueo preventivo en endpoint por agente Sophos Central (`type: Event::Endpoint::WebControlViolation`)
- **Recurso Consultado:** `https://translate.google.com`
- **Categoria Bloqueada:** `Proxies & Translators`
- **Severidad / Score:** Severidad Sophos: `low` (15) | Event Score Stellar: 15 | Fidelidad: 15
- **Motor / Conector:** `sophos_CAJA-ANDE-SOPHOS` (`sophos_events`)

### Linea de Tiempo Temporal

| Hora (UTC) | Hora (Local PYT) | Evento Detectado | Actual | Typical | Ratio | Observacion Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-03 14:16:55 | 2026-09-03 10:16:55 | Intento de conexion HTTPS a `translate.google.com` bloqueado por politicas de Sophos Web Control | N/A | N/A | N/A | El endpoint intercepto la peticion web localmente. Accion preventiva inmediata sin payload malicioso. |

### Desglose Tecnico y Diseccion Forense

- **Causa Raiz del Evento:** El usuario `CAJAANDE\vescobar` en el endpoint `NBCJPPA25003` intentó acceder al servicio público de traducción de Google (`https://translate.google.com`) mediante su navegador web.
- **Politica Aplicada:** La politica corporativa de Sophos Web Control para el tenant `CAJAANDE` tiene restringida la categoria `Proxies & Translators` para evitar filtracion de informacion o circunvalacion de controles perimetrales.
- **Mapeo Exagerado en el SIEM:** Stellar Cyber ingiere este evento y, basándose en la regla genérica de correlación de Sophos, lo clasifica como `Sophos Event: User Execution` asociándolo a la técnica MITRE `T1204 (User Execution)` bajo la etapa de `Persistent Foothold`. Este mapeo es erróneo y desproporcionado: no hubo ejecucion de ningun binario, script, macro ni exploit en el sistema operativo; se trató exclusivamente de un filtrado de URL a nivel de navegación web.

```json
{
  "payload_type": "web_url_access",
  "payload_value": "https://translate.google.com",
  "payload_hash": "N/A - consulta URL bloqueada por proxy/EDR",
  "payload_firma": "Event::Endpoint::WebControlViolation | Category: Proxies & Translators",
  "payload_accion": "BLOCKED en capa endpoint por Sophos Web Control",
  "payload_destino": "Google Inc. (Translate Service)"
}
```

**Comandos de Diagnostico Recomendados:**
```powershell
# Verificar estado y politicas de Sophos Endpoint en la estacion NBCJPPA25003
Get-Service -Name "Sophos Web Control Service", "Sophos Endpoint Defense Service"
```

**Hipotesis Formuladas:**

| N | Hipotesis | Probabilidad | Razon |
|---|---|---|---|
| H1 | Navegacion rutinaria de usuario intentando traducir un texto o documento laboral | Alta (98%) | El destino es el portal publico oficial de Google Translate. Es una herramienta de ofimatica estandar. |
| H2 | Intento intencional de usar el traductor como proxy web para saltar restricciones | Baja (2%) | Aunque tecnicamente factible, no hay patrones recurrentes ni herramientas de evasion asociadas. |
| H3 | Compromiso por malware / Ejecucion de codigo | Nula (0%) | Telemetria no registra procesos sospechosos ni conexiones C2. El evento es 100% un bloqueo de URL. |

### Por que es (o no es) una Amenaza?

**Veredicto del Evento: Falso Positivo Operativo (Bloqueo Preventivo de Politica Web).**
El acceso a `translate.google.com` no constituye un incidente de seguridad, una intrusión ni una amenaza persistente. La política de seguridad funcionó de forma óptima bloqueando la conexión antes de que se estableciera el flujo. No hay compromiso del endpoint ni riesgo de persistencia.

---

## Analisis Evento 2 (Duplicado de Evento 1)

**El Evento 2 es un duplicado exacto del Evento 1.**
Comparte de forma idéntica:
- Identificador de evento Sophos: `id: 14521ad6-c2e1-4319-bc95-183515510065`
- Timestamp de generacion original: `2026-09-03T14:16:55.000Z`
- Host: `NBCJPPA25003` (`172.16.202.21`)
- Usuario: `CAJAANDE\vescobar`
- URL bloqueada: `https://translate.google.com`

Se clasifica de forma identica como Falso Positivo por duplicacion de telemetria en ingesta.

---

## 🏛️ El Concilio SOC ha deliberado

> **Problema a analizar:** Ingesta de 2 alertas con severidad 15 mapeadas como `User Execution` (T1204) en un endpoint corporativo de Caja Ande debido al bloqueo de `translate.google.com`.

🔴 **Perspectiva Red Team:**
Los traductores web como Google Translate son ocasionalmente utilizados para intentar visualizar sitios restringidos emulando un proxy web reverso. No obstante, en este caso el control del endpoint lo interceptó y mitigó en el acto. No hay vector ejecutable.

🔵 **Perspectiva Blue Team:**
El agente de Sophos aplicó correctamente la política de filtrado web (`Proxies & Translators`). El SIEM exagera la severidad catalogándolo como ejecución de usuario. Actividad contenida por diseño, impacto nulo.

🟢 **Perspectiva Threat Intel:**
El dominio consultado pertenece a la infraestructura legítima de Google LLC. Reputación confiable.

---

## 🧠 Sintesis y Decision Final (Mentor DFIR)

El evento es un **Falso Positivo / Ruido de Monitoreo**. Corresponde a una violación benigna de navegación web bloqueada preventivamente por el antivirus/EDR. No requiere remediación técnica, aislamiento de host ni investigación forense profunda. Se procede al cierre administrativo del caso.

---

## 🛡️ Analisis de Impacto CIA Triad

```json
{
  "Confidencialidad": "Intacta (La conexion fue bloqueada antes de transmitir datos)",
  "Integridad": "Intacta (No existio alteracion de archivos ni configuracion en el host)",
  "Disponibilidad": "Intacta (El endpoint opera con normalidad)"
}
```

---

## ⚖️ Veredicto y Confianza Analitica

```json
{
  "Veredicto": "Falso Positivo (Bloqueo Web Informativo / Mapeo Erroneo T1204)",
  "Confianza": "100%",
  "Justificacion": "El log crudo de Sophos certifica que la peticion a translate.google.com fue bloqueada localmente por politicas de categoria de contenido. No existio ejecucion de malware ni compromiso de cuenta."
}
```

---

## 📉 Indicador de Fatiga de Alertas

```json
{
  "nivel_fatiga": "ALTO",
  "razon": "Stellar Cyber asigna la tecnica MITRE T1204 (User Execution) a simples bloqueos de navegacion web (WebControlViolation), saturando la cola del SOC con falsos positivos de ejecucion.",
  "accion": "Crear regla de supresion o bajar severidad en Stellar para eventos de Sophos cuyo subtype sea event_endpoint_webcontrolviolation."
}
```

---

## 📘 Fase del Ciclo NIST 800-61

| Fase NIST | Accion Tecnica |
| :--- | :--- |
| Preparacion | Verificar politicas de filtrado web aplicadas a endpoints en Sophos Central. |
| Deteccion y Analisis | Completada. Identificado como falso positivo por mapeo generico de SIEM. |
| Contencion | No requerida (Mitigado preventivamente por el agente Sophos). |
| Erradicacion | N/A para solicitudes web bloqueadas. |
| Recuperacion | N/A. |
| Post-Incidente | Documentar en bitacora de Excel y cerrar alerta en Stellar Cyber. |

---

## 📚 Playbook Asignado

| ID | Nombre | Justificacion Estrategica |
| :--- | :--- | :--- |
| PB-WEB-FILTER | Gestion de Eventos de Filtrado Web y EDR | Revision de eventos informativos de navegacion web bloqueada por politicas corporativas. |

---

## 🏷️ Resolution Tag para Stellar Cyber

**Tag:** `False Positive`
**Descripcion:** Evento de bloqueo preventivo de navegacion web (`https://translate.google.com`) aplicado por Sophos Central por categoria `Proxies & Translators`. Sin ejecucion maliciosa.

---

## 📝 Datos para Bitacora de Excel (UNA SOLA LINEA EN TABLA)

| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Deteccion | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripcion | Evidencia (Logs, etc. Puede ser el mismo del Case Evidence ) | Solicitud de Accion | Estado | URL | Generacion de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-03 10:16 | Analista SOC Senior | CAJAANDE | Sophos_Event_User_Execution_NBCJPPA25003_vescobar | sophos_CAJA-ANDE-SOPHOS | N/A | Baja | Sophos Event: User Execution | Bloqueo preventivo de translate.google.com en NBCJPPA25003 | NBCJPPA25003 (172.16.202.21 - vescobar) | 2 alertas (1 original + 1 duplicado). FP: Sophos bloqueo intento de navegacion a Google Translate por categoria Proxies & Translators. Mapeo exagerado de T1204 en SIEM. | sophos event id: 14521ad6-c2e1-4319-bc95-183515510065 | Ninguna. Control preventivo aplicado con exito. | Cerrado | N/A | NO | N/A | PB-WEB-FILTER |

---

## 💻 Instruccion para Cierre en Stellar Cyber

**Estado:** Closed
**Resolution Tag:** False Positive
**Comentario:**
> Alerta descartada como falso positivo. Tras revisar la telemetría base, se confirma que el evento original de Sophos es un simple WebControlViolation debido a que el usuario intentó acceder a una URL bloqueada por política de filtrado corporativo (`https://translate.google.com` bajo categoría `Proxies & Translators`) en el equipo `NBCJPPA25003`. No hubo ejecución de código malicioso ni intención ofensiva. Mapeo exagerado de técnica T1204 en el SIEM.

> [!TIP]
> Confirmar en `SOC_GEM_v2.md` la regla permanente de ruido operativo: **Eventos de Sophos `Event::Endpoint::WebControlViolation` categorizados como User Execution (T1204) corresponden a bloqueos preventivos de navegación web y deben cerrarse como Falso Positivo.**

---

## 🔬 Desglose Ultra Quirurgico

**Capa de Endpoint / Dispositivo:**
- `computer_name: NBCJPPA25003`: Computadora asignada a usuario corporativo en el tenant `CAJAANDE`.
- `hostip: 172.16.202.21`: Direccion IP perteneciente a la subred corporativa de endpoints de Caja Ande (`172.16.202.0/24`).
- `user.name: CAJAANDE\vescobar`: Cuenta de dominio Active Directory autenticada localmente en la estacion.

**Capa de Seguridad / Agente EDR (Sophos Central):**
- `msg_class: sophos_events`: Registro recibido por el conector API de Sophos Central hacia Stellar.
- `threat.name / type: Event::Endpoint::WebControlViolation`: Identificador nativo del producto Sophos. Especifica una violacion a la directiva de control web, no una deteccion de malware (`MalwareDetected`) ni comportamiento sospechoso (`HMPA/Exploit`).
- `name: 'https://translate.google.com' blocked due to category 'Proxies & Translators'`: Cadena textual explícita que confirma la URL solicitada y la justificación de filtrado.
- `severity: 15 / low`: Severidad mínima asignada por Sophos, indicando carácter informativo/político.

**Capa de Correlacion SIEM / XDR (Stellar Cyber):**
- `xdr_event.name: sophos_event-execution-user_execution`: Stellar Cyber mapeó la cadena de Sophos a su clase general de ejecución.
- `technique.id: T1204 (User Execution)`: Clasificación automatica del framework MITRE ATT&CK basada en que un usuario interactuó con el sistema. En este contexto es un falso positivo metodológico, ya que no hubo ejecución de payload ejecutable.
- `fidelity: 15` / `threat_score: 0`: Parámetros que demuestran que el propio sistema reconoce la inocuidad del suceso frente a un incidente de ataque activo.

**Resumen Quirurgico Final:**
El usuario `CAJAANDE\vescobar` en la estación de trabajo `NBCJPPA25003` (`172.16.202.21`) intentó navegar hacia el servicio web `https://translate.google.com`. El agente Sophos Endpoint interceptó la petición HTTP/TLS y aplicó un bloqueo preventivo local en base a la política corporativa que restringe la categoría `Proxies & Translators`. La notificación fue enviada a la consola de Sophos Central e ingerida por Stellar Cyber en dos registros duplicados (`id: 14521ad6...`). Stellar Cyber lo catalogó erróneamente bajo la técnica T1204 (User Execution), inflando de forma nominal el tipo de alerta. Se comprueba un comportamiento preventivo exitoso, ausencia absoluta de malware y un impacto CIA completamente nulo.
