# Manual Operativo: Stellar Cyber MCP Server & CLI Unificado (`stellar_cli.py`)

> **Propósito:** Documento de referencia permanente para analistas SOC y agentes de IA. Detalla el funcionamiento, autenticación, herramientas disponibles y sintaxis de ejecución del endpoint MCP y del motor CLI `stellar_cli.py`.

---

## 1. Arquitectura y Reglas Críticas

1. **PROHIBICIÓN ESTRICTA:** **NUNCA** ejecutar comandos Python de una línea (`python -c`). Siempre utilizar el script permanente [**`stellar_cli.py`**](file:///c:/Users/kevinmoraes/Documents/soc-env/stellar_cli.py) o scripts versionados.
2. **Sincronización Obligatoria:** Todo cambio o nuevo script debe estar presente tanto en `soc-env` como en `SOC_SOAR/soar` y pusheado a GitHub (`origin/main`).
3. **Endpoint MCP Oficial:**
   * **URL:** `https://technoma.stellarcyber.cloud/mcp`
   * **Transporte:** HTTP SSE / JSON-RPC 2.0 (`Accept: application/json, text/event-stream`)
   * **Headers obligatorios:** `Authorization: Bearer <JWT_ACCESS_TOKEN>`

---

## 2. Mecanismo de Autenticación (JWT Token Exchange)

Para comunicarse con el endpoint MCP o con la API REST de Stellar Cyber:
* **Host:** `technoma.stellarcyber.cloud`
* **Credenciales:** `kevinmoraes@technoma.com.py:796e625a6552636a4e326b54784a553868504f47514a387768636b4d32646f364375494d485050516b763131766a4f65`
* **Flujo:**
  1. Codificar `EMAIL:TOKEN` en Base64.
  2. Enviar `POST https://technoma.stellarcyber.cloud/connect/api/v1/access_token` con encabezado `Authorization: Basic <B64>`.
  3. Extraer `access_token` del JSON de respuesta.
  4. Usar dicho token como `Bearer <access_token>` en los headers y como argumento `"access_token": "<token>"` en cada llamada MCP.
* *Nota:* [**`stellar_cli.py`**](file:///c:/Users/kevinmoraes/Documents/soc-env/stellar_cli.py) realiza esta negociación automáticamente en segundo plano.

---

## 3. Catálogo de Herramientas MCP de Stellar Cyber

| Nombre de Herramienta MCP | Argumentos Requeridos | Tipo de Datos / Formato | Descripción |
| :--- | :--- | :--- | :--- |
| **`getCaseDetail`** | `ticket_id`, `access_token` | `ticket_id`: **`string`** *(OBLIGATORIO: e.g. `"17813"`, NUNCA int `17813`)* | Obtiene el expediente forense completo del caso (alertas, observables, timeline, SLA). |
| **`listCases`** | `limit` (opcional), `access_token` | `limit`: `int` (def: 15) | Lista los casos abiertos, en progreso o resueltos con severidad y scores. |
| **`updateCase`** | `case_id`, `access_token`, `status`, `assignee` | `case_id`: `string` (Mongo ID `6ad1...`) | Modifica estado (`In Progress`, `Closed`, `Resolved`) o asigna analista. |
| **`getCaseAlerts`** | `ticket_id`, `access_token` | `ticket_id`: **`string`** | Lista todas las alertas individuales vinculadas al caso. |
| **`getAlertDetail`** | `alert_id`, `access_token`, `index` (opc) | `alert_id`: `string` (UUID) | Extrae la alerta individual con su log crudo (`parser_raw_msg`). |
| **`listTenant`** | `access_token` | *(vacío)* | Lista los nombres e IDs de los tenants y sub-tenants configurados. |
| **`getTenant`** | `tenant_id`, `access_token` | `tenant_id`: `string` | Retorna detalles y configuración de un tenant específico. |

---

## 4. Guía de Uso del CLI Unificado (`stellar_cli.py`)

El archivo [**`stellar_cli.py`**](file:///c:/Users/kevinmoraes/Documents/soc-env/stellar_cli.py) se encuentra en la raíz del entorno y unifica el servidor MCP y los endpoints REST de Stellar.

### 4.1. Consultar Detalle de un Caso
```powershell
.\Scripts\python.exe stellar_cli.py --case 17813
```
* **Qué hace:** Llama a `getCaseDetail`, formatea el resumen, tabla de alertas con IPs/puertos/reglas de firewall, observables y auditoría de estado. Guarda además una copia forense en `caso_17813_detail.json`.
* **Para salida JSON cruda:**
  ```powershell
  .\Scripts\python.exe stellar_cli.py --case 17813 --json
  ```

### 4.2. Listar Casos de Incidentes
```powershell
.\Scripts\python.exe stellar_cli.py --list-cases --limit 15
```
* **Filtrar por estado:**
  ```powershell
  .\Scripts\python.exe stellar_cli.py --list-cases --status "In Progress"
  ```

### 4.3. Actualizar Estado o Asignado de un Caso
```powershell
.\Scripts\python.exe stellar_cli.py --update-case 6ad1e7d7a9a3e2ee2766f9e2 --set-status "Resolved"
```

### 4.4. Consultar Alertas Asociadas a un Ticket
```powershell
.\Scripts\python.exe stellar_cli.py --case-alerts 17813
```

### 4.5. Consultar Consumo de Cuota y Almacenamiento (GB)
```powershell
.\Scripts\python.exe stellar_cli.py --quota
```
* **Qué hace:** Consulta el endpoint REST `/storage-usages/daily_and_monthly` y muestra el acumulado mensual y el último consumo diario por tenant (`CAJAANDE`, `technoma`, etc.).

### 4.6. Threat Hunting en el Data Lake (Interflow)
```powershell
.\Scripts\python.exe stellar_cli.py --search "srcip:192.168.169.11"
```
* **Filtrar por tenant específico:**
  ```powershell
  .\Scripts\python.exe stellar_cli.py --search "dstport:443 AND action:deny" --tenant e511c3fc54cd4d668bb67612c2ef4b04
  ```

### 4.7. Listar Filtros de Logs Activos (Log Filters)
```powershell
.\Scripts\python.exe stellar_cli.py --filters
```

### 4.8. Listar Tenants Configurados
```powershell
.\Scripts\python.exe stellar_cli.py --tenants
```

---

## 5. Gotchas y Errores Conocidos (Lecciones Aprendidas)

1. **Error `-32602: Expected string, received number for path ['ticket_id']`:**
   * **Causa:** Enviar `{"ticket_id": 17813}` en lugar de `{"ticket_id": "17813"}`.
   * **Solución:** Siempre enviar el ticket como cadena de texto.
2. **Error `401 Unauthorized` al invocar `get_access_token` en MCP:**
   * **Causa:** El endpoint MCP espera una clave generada en *User Profile -> API Keys* (Scoped Key), no el token básico del usuario.
   * **Solución:** `stellar_cli.py` resuelve esto intercambiando el Basic Auth contra `/connect/api/v1/access_token` y pasando el JWT resultante como `access_token` en los argumentos del MCP.
3. **Persistencia de Sesión:**
   * Si el agente de IA reinicia o pierde contexto de sesión, **debe leer este archivo primero** antes de intentar crear cualquier nuevo script de conexión.
