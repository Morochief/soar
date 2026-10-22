# 📚 MAPA MAESTRO DE REPOSITORIOS LOCALES DE DOCUMENTACIÓN (SO3 & STACK COMPLETO)

> **Ubicación:** `G:\Hermes + Antigravity\`  
> **Propósito:** Biblioteca técnica offline para consulta forense, desarrollo de playbooks, reglas y resolución de dudas de arquitectura sin salir a internet.

---

## 🧅 1. Documentación Oficial de Security Onion (SO3 / SO2)

* 📁 **Directorio Local:** [**`G:\Hermes + Antigravity\so3-docs\`**](file:///G:/Hermes%20+%20Antigravity/so3-docs)
* **Contenido:** **154 capítulos técnicos oficiales** cubriendo desde la arquitectura física hasta la operación diaria:
  * `architecture.rst`: Arquitectura de Grid (Manager, Search Nodes, Forward Nodes).
  * `salt.rst`: Explicación de cómo SO usa SaltStack para orquestación.
  * `alerts.rst` & `hunt.rst`: Uso de la interfaz de analista SOC.
  * `suricata.rst` & `zeek.rst`: Configuración de motores de red.
  * `elastic-fleet.rst`: Despliegue de agentes EDR en estaciones.
  * `kratos.rst`: Gestión de identidades y autenticación.
  * `airgap.rst`: Operación en redes desconectadas de internet.
  * `troubleshooting.rst`: Procedimientos de rescate y diagnóstico.

---

## 🧭 2. Índice de Búsqueda Rápida: De Contenedor SO3 a Documentación Específica

| Contenedor SO3 | Tecnología / Proyecto | Directorio Local de Documentación | ¿Qué buscar aquí? |
| :--- | :--- | :--- | :--- |
| **La Plataforma Completa** | **Security Onion (SO3)** | 📁 `G:\Hermes + Antigravity\so3-docs\` | Los 154 capítulos oficiales de SO (arquitectura, comandos `so-...`, instalación, tuning). |
| **Orquestación Global** | **SaltStack** | 📁 `G:\Hermes + Antigravity\salt\doc\` | Sintaxis de Salt States (`.sls`), Jinja2, Grains, Pillars y comandos `salt-call`. |
| **`so-dockerregistry`** | **Distribution Registry (OCI)** | 📁 `G:\Hermes + Antigravity\docker-registry-docs\` | Endpoints de la API v2, garbage collection y almacenamiento en disco. |
| **`so-elastalert`** | **ElastAlert** | 📁 `G:\Hermes + Antigravity\elastalert\docs\` | Tipos de reglas YAML (frequency, spike, flatline, cardinality) y formatos de alerta. |
| **`so-elastic-fleet`** | **Fleet Server** | 📁 `G:\Hermes + Antigravity\elastic-docs-content\` | Enrolamiento de Elastic Agents, políticas de endpoint y variables de recolección. |
| **`so-elastic-fleet-package-registry`** | **Package Registry** | 📁 `G:\Hermes + Antigravity\elastic-docs-content\` | Estructura de paquetes de integraciones locales Airgap. |
| **`so-elasticsearch`** | **Elasticsearch** | 📁 `G:\Hermes + Antigravity\elastic-docs-content\` | Índices, shards, mappings ECS, JVM Heap y Query DSL. |
| **`so-influxdb`** | **InfluxDB** | 📁 `G:\Hermes + Antigravity\influxdb-docs\` | Lenguaje Flux / InfluxQL, buckets y políticas de retención temporal. |
| **`so-kibana`** | **Kibana** | 📁 `G:\Hermes + Antigravity\elastic-docs-content\` | KQL (Kibana Query Language), creación de dashboards y Dev Tools. |
| **`so-kratos`** | **Ory Kratos** | 📁 `G:\Hermes + Antigravity\ory-docs\docs\kratos\` | Flujos de autenticación, esquemas de identidad (`identity.schema.json`) y sesiones web. |
| **`so-logstash`** | **Elastic Logstash** | 📁 `G:\Hermes + Antigravity\logstash-docs\` | Plugins de filtros (Grok, Mutate, KV, GeoIP), inputs y outputs de pipelines. |
| **`so-nginx`** | **NGINX Reverse Proxy** | 📁 `G:\Hermes + Antigravity\nginx-docs\` | Configuración de reverse proxy, directivas de SSL/TLS, buffers y headers de seguridad. |
| **`so-postgres`** | **PostgreSQL** | 📁 `G:\Hermes + Antigravity\postgres-docs\doc\` | Consultas SQL relacionales, esquema de base de datos de casos y utilidades `pg_isready`. |
| **`so-redis`** | **Redis** | 📁 `G:\Hermes + Antigravity\redis-doc\` | Comandos de colas (`LPUSH`, `RPOP`, `LLEN`), optimización de memoria y persistencia RDB. |
| **`so-sensoroni`** | **Sensoroni** | 📁 `G:\Hermes + Antigravity\sensoroni-docs\` | API del daemon de gestión remota de sensores en Go. |
| **`so-soc`** | **Security Onion Console** | 📁 `G:\Hermes + Antigravity\so3-docs\alerts.rst` | Manual oficial de uso de la consola web (Alerts, Hunt, PCAP, Cases, Grid). |
| **`so-strelka-*` (6 microservicios)**| **Target Strelka** | 📁 `G:\Hermes + Antigravity\strelka-docs\docs\` | Backend de escaneo estático de archivos, plugins YARA, OLE, PEfile y arquitectura de workers. |
| **`so-suricata`** | **Suricata NIDS** | 📁 `G:\Hermes + Antigravity\suricata-docs\doc\` | Manual oficial de sintaxis de reglas, opciones de `suricata.yaml`, sockets AF_PACKET y `eve.json`. |
| **`so-telegraf`** | **Telegraf** | 📁 `G:\Hermes + Antigravity\influxdb-docs\` | Plugins de recolección de métricas de Docker, CPU, RAM y contadores de red. |
| **`so-zeek`** | **Zeek NSM** | 📁 `G:\Hermes + Antigravity\zeek-docs\` | Referencia del lenguaje de scripts Zeek, formatos de logs (`conn`, `dns`, `ssl`, `files`) y frameworks. |

---

## 🔍 Ejemplos de Búsqueda Rápida Local en PowerShell:

```powershell
# Buscar cualquier concepto en la documentación oficial de Security Onion:
Get-ChildItem -Path "G:\Hermes + Antigravity\so3-docs" -Filter "*.rst" | Select-String "airgap"
Get-ChildItem -Path "G:\Hermes + Antigravity\so3-docs" -Filter "*.rst" | Select-String "so-rule-update"

# Buscar directivas en Suricata:
Get-ChildItem -Path "G:\Hermes + Antigravity\suricata-docs" -Filter "*.rst" -Recurse | Select-String "threshold"

# Buscar pipelines en Logstash:
Get-ChildItem -Path "G:\Hermes + Antigravity\logstash-docs" -Recurse | Select-String "filter-geoip"
```
