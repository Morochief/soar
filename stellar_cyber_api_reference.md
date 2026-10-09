# 🛡️ Stellar Cyber Open XDR — API Reference v6.5.0
> Base URL: `https://technoma.stellarcyber.cloud/connect/api/v1`

---

## 🔑 Autenticación (Flujo Completo)

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | **Obtener Token Base** | `POST /access_token` con Basic Auth (email + All-Access Token) |
| 2 | **Extraer JWT** | Copiar solo el valor del campo `access_token` de la respuesta |
| 3 | **Usar JWT** | Header: `Authorization: Bearer <JWT>` |
| ⚠️ | **Expiración** | JWT expira **10 minutos** después de su creación |

```http
POST /access_token
Authorization: Basic base64(email:all_access_token)
Content-Type: application/json

Body: {}
```

---

## 📋 Módulos de la API

### 🔥 Cases (Casos / Incidentes SOAR)
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/cases` | Listar todos los casos con filtros |
| `POST` | `/cases` | Crear nuevo caso manualmente |
| `GET` | `/cases/{id}` | Detalle completo de un caso |
| `PUT` | `/cases/{id}` | Actualizar estado/asignación del caso |
| `GET` | `/cases/{id}/activities` | Historial de actividad del caso |
| `GET` | `/cases/{id}/activity/score` | Score de actividad del caso |
| `GET` | `/cases/{id}/alerts` | ⭐ Alertas asociadas al caso (Interflow) |
| `POST` | `/cases/{id}/alerts` | Agregar alertas al caso |
| `GET` | `/cases/{id}/comments` | Ver comentarios del caso |
| `POST` | `/cases/{id}/comments` | Agregar comentario al caso |
| `GET` | `/cases/{id}/details` | ⭐ Detalles enriquecidos del caso |
| `GET` | `/cases/{id}/observables` | Lista de observables del caso |
| `GET` | `/cases/{id}/scores` | Scores de severidad y fidelidad |
| `GET` | `/cases/{id}/summary` | Resumen ejecutivo del caso |
| `GET` | `/cases/{id}/updates` | Timeline de actualizaciones |
| `GET` | `/cases/assignees` | Lista de analistas disponibles para asignar |
| `GET` | `/cases/health` | Salud general de la cola de casos |
| `GET` | `/cases/tags` | Tags disponibles para categorizar |
| `GET` | `/cases/minmax` | Rangos de fechas de los casos activos |

---

### 🔍 Queries (Motor de Búsqueda / Threat Hunting)
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/queries` | Listar queries guardadas |
| `POST` | `/queries` | ⭐ **Ejecutar búsqueda en el Data Lake** |
| `POST` | `/queries/_batch` | Ejecutar múltiples queries en lote |
| `GET` | `/queries/{id}` | Resultado de una query específica |
| `PUT` | `/queries/{id}` | Actualizar/re-ejecutar query |
| `DELETE` | `/queries/{id}` | Eliminar query |
| `POST` | `/queries/export` | Exportar queries a archivo |
| `POST` | `/queries/import` | Importar queries desde archivo |

**Estructura de una Query (POST /queries):**
```json
{
  "cust_id": "tenant_uuid",
  "name": "Hunt_IOC_192.168.1.1",
  "conditions": {
    "modifier": "and",
    "conditions": [
      {"type": "query_string", "value": ["_index: aella-ser-* AND srcip: \"192.168.1.1\""]}
    ]
  }
}
```

---

### 🤖 AutoTriage (IA Automática de Alertas)
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/autotriage/v1/case/{id}/summary` | ⭐ Resumen IA del caso |
| `GET` | `/autotriage/v1/case/{id}/activities` | Actividades detectadas por IA |
| `POST` | `/autotriage/v1/case/{id}/feedback/summary` | Enviar feedback sobre el análisis IA |
| `GET` | `/autotriage/v1/alert/{uuid}/summary` | Resumen IA de una alerta individual |
| `POST` | `/autotriage/v1/alert/{uuid}/feedback/verdict` | Marcar veredicto sobre una alerta |
| `POST` | `/autotriage/v1/alert/feedback/verdicts/batch` | Marcar veredictos en lote |

---

### 🚨 Security Events (Eventos del SIEM)
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `PUT` | `/security_events/{index}/{id}/status` | Cambiar estado de un evento |
| `PUT` | `/security_events/{index}/{id}/comments` | Comentar un evento directamente |
| `PATCH` | `/security_events/{index}/{id}/tags` | Taggear un evento |

---

### 📊 Sensors & Health
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/data_sensors` | Todos los sensores conectados |
| `GET` | `/data_sensors/{id}` | Detalle de un sensor |
| `GET` | `/storage-usages/daily_and_monthly` | Uso de almacenamiento del Data Lake |
| `GET` | `/cases/health` | Salud de la cola de alertas/casos |

---

### 👥 Tenants & Users
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/tenants` | Lista de todos los tenants |
| `GET` | `/tenants/{cust_id}` | Detalle de un tenant |
| `GET` | `/users` | Lista de analistas del SOC |
| `GET` | `/users/{id}` | Perfil de un analista |

---

### 🔔 Alert Watchers (Reglas de Notificación)
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/alert_watchers` | Ver reglas activas |
| `PATCH` | `/alert_watchers/{id}` | Modificar una regla |

---

### 🛡️ Detection Management
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/detections` | Lista de detecciones activas con fuentes de datos |
| `GET` | `/detections/profiles` | Perfiles de detección disponibles |

---

## 🎯 DIAGNÓSTICO: Estado Actual del Threat Hunting en el Cockpit

### Lo que funciona actualmente:
- ✅ Búsqueda manual por campo + valor (srcip, username, process_name)
- ✅ 2 macros predefinidas (alertas sin caso, payloads HTTP en IDS)
- ✅ Selección de índice del Data Lake (6 índices)
- ✅ Selección de tenant (2 tenants hardcodeados)

### Lo que FALTA (Gap Analysis):

| Carencia | Impacto | Prioridad |
|----------|---------|-----------|
| Solo 3 campos de búsqueda (srcip, username, process_name) | 🔴 Crítico — La mayoría de los IOCs son hashes MD5/SHA256, dominios, puertos | Alta |
| Resultado crudo sin parsear ni resumir | 🟡 Medio — El analista debe leer JSON gigante manualmente | Media |
| No hay historial de hunts previas guardado | 🟡 Medio — Cada sesión empieza de cero | Media |
| No soporta búsqueda por rango de fechas | 🟡 Medio — Solo busca en todo el rango | Media |
| Solo 2 macros de cacería | 🔴 Crítico — No hay playbooks reales de MITRE ATT&CK | Alta |
| No se usa `/queries/_batch` para correlación multi-IOC | 🔴 Crítico — Para investigar una campaña con 10 IOCs, hay que lanzar 10 hunts | Alta |
| No se accede al AutoTriage IA de Stellar (`/autotriage/v1`) | 🟡 Medio — Stellar tiene su propio motor IA que no se consume | Media |
| No hay integración con `/cases/{id}/details` | 🟡 Medio — Solo se usa `/cases/{id}` que tiene menos información | Baja |

---

## 🚀 Roadmap de Mejoras Recomendadas

### Fase A — Threat Hunting Profesional (Prioridad ALTA)

**A1. Expandir Campos de Búsqueda (IOC Coverage):**
Agregar al combo de campos:
- `dstip` — IP de destino
- `domain` / `dns_name` — Dominio consultado
- `md5` / `sha256` / `sha1` — Hashes de archivos
- `dstport` — Puerto de destino (para hunting por protocolo)
- `process_name` / `process_cmdline` — Procesos ejecutados
- `url` — URLs visitadas/bloqueadas
- `hostname` — Hostname del endpoint
- `user_name` — Usuario comprometido

**A2. Nuevas Macros MITRE ATT&CK:**
```
• T1059 — Ejecución de Script (PowerShell, cmd.exe con flags sospechosos)
• T1078 — Valid Accounts (Logins fuera de horario laboral)
• T1571 — Non-Standard Port (Conexiones en puertos no HTTP/HTTPS)
• T1048 — Exfiltración por DNS (Consultas DNS con alta entropía)
• T1190 — Exploit de Servicio Público (CVE en IDS con payload HTTP)
• Movimiento Lateral (SMB con múltiples destinos desde un mismo origen)
```

**A3. Multi-IOC Batch Hunt (`/queries/_batch`):**
Agregar un area de texto para pegar hasta 10 IOCs. El Cockpit dispara una sola llamada batch a la API y muestra resultados agrupados por IOC.

**A4. Filtro de Rango de Fechas:**
Agregar dos `QDateTimeEdit` (Desde / Hasta) al panel de Hunt. La query se enriquece con `_exists_: timestamp AND timestamp:["fecha_inicio" TO "fecha_fin"]`.

---

### Fase B — Enriquecimiento de Resultado (Prioridad MEDIA)

**B1. Parseo Automático del JSON de Resultados:**
En vez de mostrar el JSON crudo, parsear los hits del Data Lake y renderizarlos en una tabla `QTableWidget` con columnas: Timestamp, IP Origen, IP Destino, Severidad, Evento.

**B2. Contador de Hits:**
Mostrar cuántos eventos coincidieron con la búsqueda ("Se encontraron **47 eventos** en el Data Lake").

**B3. Exportar Hunt a CSV:**
Botón "Exportar" que guarda los resultados en un `.csv` en la carpeta del Cockpit.

---

### Fase C — AutoTriage & Integración Avanzada (Prioridad BAJA)

**C1. Panel de Resumen IA Nativo de Stellar:**
Consumir `/autotriage/v1/case/{id}/summary` para mostrar el análisis de IA del propio Stellar Cyber (separado de tu análisis Gemini).

**C2. Asignación Dinámica de Analistas:**
Consumir `/cases/assignees` para poblar el combo de asignación con los nombres reales del equipo en lugar de tener IDs hardcodeados.

**C3. Tags de Casos Dinámicos:**
Consumir `/cases/tags` para que el analista pueda taggear casos directamente desde el Cockpit.

---

## ⚡ Implementación Sugerida para Empezar (A1 + A2)

La mejora de mayor impacto y menor riesgo es **expandir los campos de búsqueda** y **agregar macros MITRE**. No requiere nueva lógica de red, solo actualizar los `QComboBox` en la interfaz gráfica.

¿Arrancamos?
