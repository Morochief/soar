# Reporte SOC - Caso: Sophos Event: User Execution / WebControlViolation (CJPPA20120902 - MP6236932)

**Fecha de Analisis:** 2026-09-03
**Analista:** Analista SOC Senior (DFIR)
**Tenant:** CAJAANDE
**Case ID:** Sophos_Event_User_Execution_CJPPA20120902_MP6236932
**Fuente:** Stellar Cyber XDR / Sophos Central (`sophos_CAJA-ANDE-SOPHOS`)
**XDR Event:** Sophos Event: User Execution (`sophos_event-execution-user_execution`) | Subtipo: `Event::Endpoint::WebControlViolation` | MITRE: T1204 (User Execution) / TA0002 (Execution)

---

> He detectado **2 eventos independientes** en el volcado crudo. El Evento 2 es un duplicado exacto del Evento 1 generado por doble reenvío del registro de Sophos Central hacia Stellar Cyber. Se procesan de forma secuencial y unificada con su respectivo cierre maestro.

---

## Analisis Evento 1 (Bloqueo WebControlViolation: translate.google.com)

### Tags:
`#FalsoPositivo` `#WebControlViolation` `#SophosCentral` `#CAJAANDE` `#CJPPA20120902` `#ProxiesAndTranslators` `#FiltradoWeb`

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
- **Origen / Host:** `CJPPA20120902` | IP: `172.16.202.115` (Segmento LAN corporativo de Caja Ande)
- **Usuario:** `CAJAANDE\MP6236932` (ID: `6a985a1e25f55650e21edf2d`)
- **Accion de Seguridad:** Bloqueo preventivo en endpoint por agente Sophos Central (`type: Event::Endpoint::WebControlViolation`)
- **Recurso Consultado:** `https://translate.google.com`
- **Categoria Bloqueada:** `Proxies & Translators`
- **Severidad / Score:** Severidad Sophos: `low` (15) | Event Score Stellar: 15 | Fidelidad: 15
- **Motor / Conector:** `sophos_CAJA-ANDE-SOPHOS` (`sophos_events`)

### Linea de Tiempo Temporal
| Hora (UTC) | Hora (Local PYT) | Evento Detectado | Actual | Typical | Ratio | Observacion Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-03 16:45:48 | 2026-09-03 12:45:48 | Intento de conexion HTTPS a `translate.google.com` bloqueado por politicas de Sophos Web Control | N/A | N/A | N/A | Intercepción preventiva a nivel del navegador en el endpoint. Sin ejecución de código. |

### Desglose Tecnico y Diseccion Forense
- **Causa Raiz del Evento:** El usuario `CAJAANDE\MP6236932` en el equipo `CJPPA20120902` (`172.16.202.115`) intentó acceder a la herramienta de traducción `https://translate.google.com`.
- **Politica de Seguridad:** La directiva corporativa de Sophos Web Control para `CAJAANDE` restringe la categoría `Proxies & Translators`. La petición web fue interceptada y cortada de inmediato.
- **Mapeo en SIEM (Stellar Cyber):** Al igual que en casos anteriores, Stellar Cyber asigna la técnica `T1204 (User Execution)` a los eventos `Event::Endpoint::WebControlViolation`. No existió ejecución de binarios, archivos ni payloads ejecutables.

```json
{
  "payload_type": "web_url_access",
  "payload_value": "https://translate.google.com",
  "payload_hash": "N/A - consulta URL bloqueada",
  "payload_firma": "Event::Endpoint::WebControlViolation | Category: Proxies & Translators",
  "payload_accion": "BLOCKED por Sophos Web Control",
  "payload_destino": "Google Inc. (Translate Service)"
}
```

---

## Analisis Evento 2 (Duplicado de Evento 1)

**El Evento 2 es un duplicado exacto del Evento 1.**
Comparte de forma idéntica:
- Identificador Sophos: `id: e1157deb-d71e-49a6-a099-cdc0ef5ccb2e`
- Timestamp de generacion original: `2026-09-03T16:45:48.000Z`
- Host: `CJPPA20120902` (`172.16.202.115`)
- Usuario: `CAJAANDE\MP6236932`
- URL bloqueada: `https://translate.google.com`

---

## 🏛️ El Concilio SOC ha deliberado

> **Problema a analizar:** Alerta de `User Execution` (T1204) disparada por el bloqueo preventivo de `translate.google.com` en el equipo `CJPPA20120902`.

🔴 **Perspectiva Red Team:**
No hay componente de ejecución de código ni evasión. El intento de navegación web fue frustrado antes del handshake TLS.

🔵 **Perspectiva Blue Team:**
El agente de Sophos cumplió su función aplicando la directiva corporativa. No hay persistencia ni afectación en el host.

🟢 **Perspectiva Threat Intel:**
El destino es infraestructura legítima de Google LLC.

---

## 🧠 Sintesis y Decision Final (Mentor DFIR)

El evento es un **Falso Positivo Operativo (Bloqueo Web Informativo)**. La alerta se debe a la categorización rígida de Sophos sobre traductores web y al posterior mapeo nominal como "User Execution" en el SIEM. Se descarta riesgo de intrusión.

---

## 🛡️ Analisis de Impacto CIA Triad
```json
{
  "Confidencialidad": "Intacta (La conexion fue bloqueada antes de transmitir datos)",
  "Integridad": "Intacta (No existio alteracion en el sistema de archivos)",
  "Disponibilidad": "Intacta (El endpoint opera con total normalidad)"
}
```

---

## ⚖️ Veredicto y Confianza Analitica
```json
{
  "Veredicto": "Falso Positivo (Bloqueo Web Informativo / Mapeo Erroneo T1204)",
  "Confianza": "100%",
  "Justificacion": "El log de Sophos Central confirma que la peticion a translate.google.com fue bloqueada localmente por politicas de categoria de contenido. No hubo ejecucion de malware ni compromiso de cuenta."
}
```

---

## 📉 Indicador de Fatiga de Alertas
```json
{
  "nivel_fatiga": "ALTO",
  "razon": "Eventos recurrentes de navegacion bloqueada son mapeados como incidentes de ejecucion T1204 en Stellar Cyber.",
  "accion": "Configurar supresion o rebajar severidad para WebControlViolation."
}
```

---

## 📘 Fase del Ciclo NIST 800-61
| Fase NIST | Accion Tecnica |
| :--- | :--- |
| Deteccion y Analisis | Descarte y clasificacion como falso positivo. |
| Contencion | No requerida (Mitigado preventivamente por Sophos). |
| Post-Incidente | Registrar en bitacora y cerrar en Stellar Cyber. |

---

## 📚 Playbook Asignado
| ID | Nombre | Justificacion Estrategica |
| :--- | :--- | :--- |
| PB-WEB-FILTER | Gestion de Eventos de Filtrado Web y EDR | Revision de eventos informativos de navegacion web bloqueada por politicas corporativas. |

---

## 🏷️ Resolution Tag para Stellar Cyber
**Tag:** `False Positive`
**Descripcion:** Evento de bloqueo preventivo de navegacion web (`https://translate.google.com`) aplicado por Sophos Central por categoria `Proxies & Translators`.

---

## 📝 Datos para Bitacora de Excel (UNA SOLA LINEA EN TABLA)

| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Deteccion | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripcion | Evidencia (Logs, etc. Puede ser el mismo del Case Evidence ) | Solicitud de Accion | Estado | URL | Generacion de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-03 12:45 | Analista SOC Senior | CAJAANDE | Sophos_Event_User_Execution_CJPPA20120902_MP6236932 | sophos_CAJA-ANDE-SOPHOS | N/A | Baja | Sophos Event: User Execution | Bloqueo preventivo de translate.google.com en CJPPA20120902 | CJPPA20120902 (172.16.202.115 - MP6236932) | 2 alertas (1 original + 1 duplicado). FP: Sophos bloqueo intento de navegacion a Google Translate por categoria Proxies & Translators. Mapeo exagerado de T1204 en SIEM. | sophos event id: e1157deb-d71e-49a6-a099-cdc0ef5ccb2e | Ninguna. Control preventivo aplicado con exito. | Cerrado | N/A | NO | N/A | PB-WEB-FILTER |

---

## 💻 Instruccion para Cierre en Stellar Cyber

**Estado:** Closed  
**Resolution Tag:** False Positive  
**Comentario:**  
> Alerta descartada como falso positivo. Tras revisar la telemetría base, se confirma que el evento original de Sophos es un simple WebControlViolation debido a que el usuario intentó acceder a una URL bloqueada por política de filtrado corporativo (`https://translate.google.com` bajo categoría `Proxies & Translators`) en el equipo `CJPPA20120902`. No hubo ejecución de código malicioso ni intención ofensiva. Mapeo exagerado de técnica T1204 en el SIEM.

---

## 🔬 Desglose Ultra Quirurgico
- **Capa Endpoint:** Estación de trabajo `CJPPA20120902` (`172.16.202.115`) bajo usuario `CAJAANDE\MP6236932`.
- **Capa EDR (Sophos):** Intercepción local de la petición HTTPS por el motor Sophos Web Control. El atributo `name` explicita que el motivo fue la política `Proxies & Translators`. Severidad reportada: `low` (15).
- **Capa SIEM:** Stellar Cyber ingiere el syslog de Sophos duplicando el registro (`id: e1157deb...`) y asigna la técnica `T1204` de forma automática.
- **Resumen Quirúrgico Final:** Acción preventiva exitosa del antivirus en endpoint ante navegación no autorizada por política. Impacto nulo.
