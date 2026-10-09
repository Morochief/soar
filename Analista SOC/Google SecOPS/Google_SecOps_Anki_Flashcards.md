# Google Security Operations (SIEM) - Flashcards de Estudio & Anki

> **Guía de Memorización Activa:** Flashcards completas categorizadas por Módulo y Lección para repasar conceptos críticos, sintaxis de YARA-L, arquitectura de ingesta, RBAC y UDM.
> **Total de Tarjetas:** 48 tarjetas.

---

## Módulo 1: Intro to SIEM

### Lección 1: Resumen General de SIEM

#### Tarjeta 1
**Pregunta (Anverso / Front):**
> ¿Cuáles son las 4 fases fundamentales del ciclo de vida de operaciones de seguridad cubiertas por Google SecOps?

**Respuesta (Reverso / Back):**
  1. **Recolección de Telemetría (*Telemetry Collection*):** Ingesta, normalización y enriquecimiento de datos a gran escala.
  2. **Búsqueda y Analítica de Riesgo (*Search & Risk Analytics*):** Búsqueda de amenazas (*threat hunting*), anomalías y patrones ocultos.
  3. **Detección (*Detection*):** Análisis continuo con reglas personalizadas/curadas e inteligencia de amenazas nativa.
  4. **Respuesta (*Response - SOAR*):** Orquestación y mitigación automatizada mediante playbooks.

*Etiquetas:* `SecOps::Modulo1::Overview`

---

#### Tarjeta 2
**Pregunta (Anverso / Front):**
> ¿Cuál es la diferencia de enfoque operativo entre Google SecOps SIEM y SOAR?

**Respuesta (Reverso / Back):**
  * **SIEM:** Se enfoca en la ingesta masiva, normalización a UDM, analítica de datos, búsqueda (*search*) y detección proactiva mediante reglas YARA-L.
  * **SOAR:** Se enfoca en la orquestación, gestión de casos (*cases*), automatización y ejecución de playbooks de mitigación/respuesta ante incidentes.

*Etiquetas:* `SecOps::Modulo1::Overview`

---

### Lección 2: Métodos de Ingesta Admitidos

#### Tarjeta 3
**Pregunta (Anverso / Front):**
> ¿Cuáles son los 4 métodos principales de ingesta de datos en Google SecOps SIEM?

**Respuesta (Reverso / Back):**
  1. **Ingesta Directa (*Direct Ingestion*):** Desde Google Cloud (Cloud Logging, Cloud Asset Metadata, SCC Findings) en tiempo casi real.
  2. **Ingesta Cloud-to-Cloud / Feeds de Datos (*Data Feeds*):** Extracción (*Pull*) desde buckets o APIs de 3ros (ej. Okta), o streaming (*Push*) mediante Webhooks.
  3. **Agentes de Recolección (*Collection Agents*):** Recolector BindPlane (OpenTelemetry por ObserveIQ) para redes locales (*on-prem*) y VMs.
  4. **API de Ingesta (*Ingestion API*):** Endpoint RESTful directo para envíos programáticos de clientes o MSSPs.

*Etiquetas:* `SecOps::Modulo1::Ingestion`

---

#### Tarjeta 4
**Pregunta (Anverso / Front):**
> ¿Qué tecnología y agente utiliza Google SecOps para la recolección de logs en entornos locales (on-premise) y VMs?

**Respuesta (Reverso / Back):**
  Utiliza **BindPlane** (agente de colección basado en **OpenTelemetry**, desarrollado por **ObserveIQ**), cuya licencia viene incluida sin coste adicional con Google SecOps.

*Etiquetas:* `SecOps::Modulo1::Ingestion`

---

### Lección 3: Configuración de RBAC - Resumen

#### Tarjeta 5
**Pregunta (Anverso / Front):**
> ¿Cuáles son las 3 capas principales de control de acceso (RBAC) en Google SecOps y dónde se configuran?

**Respuesta (Reverso / Back):**
  1. **Feature RBAC:** Controla el acceso a funcionalidades de SIEM (crear reglas, buscar). Se gestiona en **Google Cloud IAM**.
  2. **Data RBAC:** Restringe el acceso a los datos de logs específicos (mediante etiquetas/scopes). Se configura dentro de la **UI de Google SecOps**.
  3. **SOAR RBAC:** Controla el acceso a casos, alertas y playbooks. Se gestiona dentro de la consola SOAR.
  *Nota:* La visión futura de Google es unificarlas en Cloud IAM.

*Etiquetas:* `SecOps::Modulo1::RBAC`

---

### Lección 4: Resumen de UDM

#### Tarjeta 6
**Pregunta (Anverso / Front):**
> ¿Qué es UDM (*Unified Data Model*) en Google SecOps y qué problema crítico resuelve?

**Respuesta (Reverso / Back):**
  Es el **esquema estándar y unificado** de Google SecOps para datos de ciberseguridad.
  Resuelve el problema de la heterogeneidad de los *raw logs* propietarios (ej. Palo Alto vs Fortinet), normalizando campos dispares (como `srcip` o `src`) en un único identificador consistente (`principal.ip`). Permite escribir una sola regla o playbook universal.

*Etiquetas:* `SecOps::Modulo1::UDM`

---

#### Tarjeta 7
**Pregunta (Anverso / Front):**
> ¿Qué significa que Google SecOps utilice un modelo *Schema-on-Write* para UDM y qué ventajas aporta?

**Respuesta (Reverso / Back):**
  Significa que la normalización ocurre **en el momento exacto de la ingesta** (no al consultar).
  Ventajas:
  1. Incorporación inmediata (*faster onboarding*): nuevas fuentes quedan cubiertas al instante por reglas existentes.
  2. Búsquedas y ejecuciones analíticas a velocidad de sub-segundo.
  3. Enriquecimiento automático (IP geo, IdP) durante la ingesta.

*Etiquetas:* `SecOps::Modulo1::UDM`

---

### Lección 5: Canalización y Normalización

#### Tarjeta 8
**Pregunta (Anverso / Front):**
> ¿Cuáles son las 4 fases de la canalización de datos (*Data Pipeline*) en Google SecOps?

**Respuesta (Reverso / Back):**
  1. **Ingesta (*Ingest*):** Recepción de telemetría cruda y metadatos de fuentes.
  2. **Validación (*Validate*):** Verificación de integridad, codificación y estructura del payload.
  3. **Parseo (*Parse - CBN*):** Mapeo de registros crudos al esquema UDM mediante lógica Logstash/Grok.
  4. **Enriquecimiento (*Enrich*):** Adición automática de contexto de entidad (IP geo, IdP, Threat Intel).

*Etiquetas:* `SecOps::Modulo1::Pipeline`

---

#### Tarjeta 9
**Pregunta (Anverso / Front):**
> ¿Qué es CBN en Google SecOps y cómo trata a los registros que fallan durante el parseo?

**Respuesta (Reverso / Back):**
  **CBN (*Configuration-Based Normalization*):** Es el motor declarativo basado en sintaxis de Logstash para transformar logs en UDM.
  Si un registro falla el parseo, **NO se descarta**: se preserva íntegro en almacenamiento como *raw log* para garantizar cumplimiento normativo y permitir búsquedas de texto crudo (*Raw Log Search*).

*Etiquetas:* `SecOps::Modulo1::Normalization`

---

### Lección 6: Métodos de Búsqueda - Resumen

#### Tarjeta 10
**Pregunta (Anverso / Front):**
> ¿Cuáles son los 3 métodos de búsqueda principales en Google SecOps SIEM y cuándo usar cada uno?

**Respuesta (Reverso / Back):**
  1. **Búsqueda de Registros en Bruto (*Raw Log Search - RLS*):** Búsqueda textual no estructurada con regex; ideal cuando el log no parsea o se busca un string literal exacto.
  2. **Búsqueda UDM (*UDM Search*):** Búsqueda estructurada sobre campos normalizados (ej. `$e.principal.ip = ...`); ultrarrápida para investigaciones.
  3. **Búsqueda Estadística UDM (*Statistical Search / Group By*):** Agregaciones, sumas, promedios y recuentos para análisis de frecuencia y anomalías.

*Etiquetas:* `SecOps::Modulo1::Search`

---

### Lección 7: Resumen de Visualizaciones

#### Tarjeta 11
**Pregunta (Anverso / Front):**
> ¿Qué diferencia existe entre los paneles heredados (*Legacy Looker Dashboards*) y los paneles nativos de Google SecOps?

**Respuesta (Reverso / Back):**
  * **Legacy Dashboards (Looker):** Construidos sobre Looker embebido; dependen del modelo LookML.
  * **Dashboards Nativos (YARA-L):** Construidos directamente sobre el motor de Google SecOps utilizando sintaxis YARA-L; ofrecen visualizaciones personalizadas en tiempo real con mayor velocidad y flexibilidad.

*Etiquetas:* `SecOps::Modulo1::Dashboards`

---

### Lección 8: Resumen del Motor de Detección

#### Tarjeta 12
**Pregunta (Anverso / Front):**
> ¿Qué lenguaje utiliza el motor de detección de Google SecOps y qué dos modalidades de reglas ofrece?

**Respuesta (Reverso / Back):**
  * Lenguaje: **YARA-L 2.0** (diseñado específicamente para logs de eventos estructurados en UDM).
  * Dos modalidades:
    1. **Detecciones Curadas (*Curated Detections*):** Mantenidas por GCTI (Google Cloud Threat Intelligence), activables sin codificar.
    2. **Reglas Personalizadas (*Custom Rules*):** Reglas YARA-L creadas o adaptadas a la medida del entorno por los analistas.

*Etiquetas:* `SecOps::Modulo1::Detection`

---

## Módulo 2: SIEM Setup

### Lección 1: Ingesta Directa

#### Tarjeta 13
**Pregunta (Anverso / Front):**
> ¿Cuáles son los tres tipos de telemetría de GCP compatibles con la Ingesta Directa hacia SecOps?

**Respuesta (Reverso / Back):**
  1. **Cloud Logging:** Auditorías, registros de VPC Flow Logs, Firewall, DNS, etc.
  2. **Metadatos de Activos en la Nube (*Cloud Asset Metadata*):** Inventario de recursos de GCP (instancias, buckets, cuentas de servicio).
  3. **Hallazgos de Security Command Center (SCC) Premium:** Vulnerabilidades, amenazas y posturas de seguridad.

*Etiquetas:* `SecOps::Modulo2::DirectIngestion`

---

### Lección 2: APIs de Terceros

#### Tarjeta 14
**Pregunta (Anverso / Front):**
> ¿Cuáles son los 3 métodos de autenticación soportados al configurar Data Feeds para APIs de terceros en SecOps?

**Respuesta (Reverso / Back):**
  1. **Basic Authentication:** Usuario y contraseña codificados.
  2. **API Key / Token:** Clave de acceso secreta en headers HTTP.
  3. **OAuth 2.0:** Flujo de Client ID, Client Secret y Token Endpoint para renovación dinámica de tokens.

*Etiquetas:* `SecOps::Modulo2::APIs`

---

### Lección 3: Buckets de Almacenamiento

#### Tarjeta 15
**Pregunta (Anverso / Front):**
> ¿Qué proveedores de almacenamiento en la nube admite Google SecOps de forma nativa para ingesta y cómo autentica en AWS S3?

**Respuesta (Reverso / Back):**
  * Proveedores soportados: **Google Cloud Storage (GCS)**, **Amazon S3** y **Azure Blob Storage**.
  * En AWS S3, se autentica mediante **IAM Role ARN** y **External ID** proporcionado por Google SecOps, permitiendo asunción de rol segura (*cross-account STS assume role*) sin llaves estáticas.

*Etiquetas:* `SecOps::Modulo2::Storage`

---

### Lección 4: Servicios de Streaming

#### Tarjeta 16
**Pregunta (Anverso / Front):**
> ¿Qué diferencia arquitectónica existe entre un Data Feed tradicional (Pull/Polling) y un Webhook (Push/Streaming)?

**Respuesta (Reverso / Back):**
  * **Pull / Polling:** El motor de SecOps consulta periódicamente a intervalos programados (ej. cada 5 min). Introduce latencia y llamadas API recurrentes.
  * **Push / Streaming (Webhook):** El origen envía inmediatamente el log vía HTTPS POST hacia un endpoint de SecOps tan pronto como se genera el evento. Latencia casi nula.

*Etiquetas:* `SecOps::Modulo2::Streaming`

---

### Lección 5: Gestión de Feeds

#### Tarjeta 17
**Pregunta (Anverso / Front):**
> ¿Qué dos etiquetas o metadatos son obligatorios al configurar un nuevo Data Feed en SecOps?

**Respuesta (Reverso / Back):**
  1. **Log Type:** Define el formato y el parser CBN que procesará los eventos (ej. `OKTA`, `MICROSOFT_WINDOWS`).
  2. **Namespace (Espacio de Nombres):** Identificador para desambiguar solapamientos de IP entre redes o entornos distintos (ej. `corp-net` vs `prod-cloud`).

*Etiquetas:* `SecOps::Modulo2::FeedManagement`

---

### Lecciones 6, 7 y 8: BindPlane On-Premise

#### Tarjeta 18
**Pregunta (Anverso / Front):**
> ¿Cuáles son los dos patrones de despliegue arquitectónico de BindPlane en redes on-premise?

**Respuesta (Reverso / Back):**
  1. **Despliegue Distribuido / Agente Local (*Host-based*):** Se instala un agente BindPlane en cada servidor o endpoint individual que genera telemetría.
  2. **Despliegue Centralizado / Agregador (*Gateway / Collector Hub*):** Los dispositivos envían logs (Syslog, SNMP) a un servidor BindPlane centralizado en la red local, el cual filtra, comprime y reenvía hacia Google SecOps vía HTTPS saliente.

*Etiquetas:* `SecOps::Modulo2::BindPlane`

---

### Lecciones 9 y 10: Feature RBAC

#### Tarjeta 19
**Pregunta (Anverso / Front):**
> ¿Qué roles predefinidos de Cloud IAM existen en Google SecOps para Feature RBAC?

**Respuesta (Reverso / Back):**
  * **Chronicle Viewer (`roles/chronicle.viewer`):** Acceso de solo lectura (búsquedas, dashboards).
  * **Chronicle Editor (`roles/chronicle.editor`):** Capacidad para crear y modificar reglas YARA-L, dashboards y feeds.
  * **Chronicle Admin (`roles/chronicle.admin`):** Control administrativo total sobre configuración, usuarios y retención.

*Etiquetas:* `SecOps::Modulo2::FeatureRBAC`

---

### Lecciones 11, 12 y 13: Data RBAC

#### Tarjeta 20
**Pregunta (Anverso / Front):**
> ¿Cómo se implementa Data RBAC en Google SecOps y cómo interactúan las Etiquetas (Labels) y los Ámbitos (Scopes)?

**Respuesta (Reverso / Back):**
  1. **Log Labels:** Etiquetas asociadas a los feeds de ingesta (ej. `confidential:true`, `dept:finance`).
  2. **Scopes (Ámbitos):** Definiciones lógicas de inclusión o exclusión basadas en etiquetas de logs.
  3. **Asignación:** Se asigna un Scope a un usuario o grupo en la UI de SecOps, limitando qué datos específicos puede ver en búsquedas e investigaciones.

*Etiquetas:* `SecOps::Modulo2::DataRBAC`

---

### Lección 14: Normalización Basada en Configuración (CBN)

#### Tarjeta 21
**Pregunta (Anverso / Front):**
> ¿Qué es CBN y cuáles son las tres directivas principales de un parser en Google SecOps?

**Respuesta (Reverso / Back):**
  **CBN (*Configuration-Based Normalization*):** Motor de parseo declarativo de SecOps basado en Logstash.
  Tres directivas esenciales:
  1. `filter { ... }`: Bloque principal que orquesta la extracción y transformación.
  2. `mutate { ... }`: Modifica tipos de datos, renombra campos o asigna a UDM.
  3. `date { ... }`: Parsea cadenas de tiempo y las mapea al formato ISO de `metadata.event_timestamp`.

*Etiquetas:* `SecOps::Modulo2::CBN`

---

### Lección 15: Extracción de Datos: Formateados y Grok

#### Tarjeta 22
**Pregunta (Anverso / Front):**
> ¿Cuándo se usa un parser estructurado (JSON/CSV) frente al filtro `grok` en CBN?

**Respuesta (Reverso / Back):**
  * **JSON / CSV / XML:** Se utiliza cuando el log tiene una estructura nativa regular; es rápido y extrae automáticamente parejas clave-valor.
  * **Grok:** Se utiliza en logs no estructurados o de texto libre (ej. Syslog estándar) mediante expresiones regulares y patrones predefinidos (como `%{IP:client_ip}`).

*Etiquetas:* `SecOps::Modulo2::CBN`

---

### Lección 18: Gestión de Parsers y Tipos de Parsers

#### Tarjeta 23
**Pregunta (Anverso / Front):**
> ¿Cuáles son los 3 tipos de parsers en Google SecOps y en qué orden de precedencia se ejecutan?

**Respuesta (Reverso / Back):**
  1. **Customer-Specific Parser (Parser Personalizado):** Creado y mantenido por el cliente.
  2. **Parser Extension (Extensión de Parser):** Código complementario escrito por el cliente sobre un parser default.
  3. **Default / Predefined Parser:** Parser oficial mantenido y actualizado por Google.
  *Precedencia:* Si existe un Custom Parser tiene prioridad total; si no, opera Default + Extension.

*Etiquetas:* `SecOps::Modulo2::Parsers`

---

### Lección 19: Demostración de Extensiones de Parsers

#### Tarjeta 24
**Pregunta (Anverso / Front):**
> ¿Qué ventaja tiene crear una Extensión de Parser (*Parser Extension*) en lugar de clonar y reemplazar todo el parser default?

**Respuesta (Reverso / Back):**
  Permite conservar el mantenimiento continuo y las actualizaciones automáticas que Google entrega al parser base, añadiendo únicamente los campos personalizados específicos de la empresa sin riesgo de que la regla de parseo quede obsoleta.

*Etiquetas:* `SecOps::Modulo2::ParserExtension`

---

## Módulo 3: SIEM Investigation

### Lección 1: Búsqueda de Registros en Bruto (Raw Log Search)

#### Tarjeta 25
**Pregunta (Anverso / Front):**
> ¿Cómo funciona la Búsqueda de Registros en Bruto (RLS) en Google SecOps y qué limitaciones tiene?

**Respuesta (Reverso / Back):**
  * **Funcionamiento:** Escaneo textual directo sobre los datos crudos almacenados mediante palabras clave, operadores booleanos (`AND`, `OR`, `NOT`) y expresiones regulares.
  * **Limitaciones:** No aprovecha la indexación ni el enriquecimiento de UDM; es más lenta para grandes rangos temporales y requiere conocer la sintaxis propietaria del fabricante.

*Etiquetas:* `SecOps::Modulo3::RLS`

---

### Lección 2: Esquema UDM y Familias de Campos

#### Tarjeta 26
**Pregunta (Anverso / Front):**
> ¿Cuáles son las 5 familias de campos principales del esquema UDM en Google SecOps?

**Respuesta (Reverso / Back):**
  1. **`metadata`:** Tipo de evento, timestamp del evento y de ingesta, log_type, ID de producto.
  2. **`principal`:** El sujeto que originó la acción (usuario, proceso o máquina origen).
  3. **`target`:** El objeto o destino sobre el que recayó la acción (servidor, archivo, usuario afectado).
  4. **`observer`:** El dispositivo intermediario que presenció o inspeccionó el evento (firewall, proxy, EDR).
  5. **`security_result`:** El veredicto de seguridad (acción tomada: `ALLOW`/`BLOCK`, severidad, regla disparada).

*Etiquetas:* `SecOps::Modulo3::UDMSchema`

---

#### Tarjeta 27
**Pregunta (Anverso / Front):**
> ¿En UDM, qué diferencia existe entre `principal`, `target` y `observer`?

**Respuesta (Reverso / Back):**
  * **`principal`:** Actor que inicia o ejecuta la acción (ej. IP del cliente o usuario que envía la petición).
  * **`target`:** Receptor o recurso al que va dirigida la acción (ej. IP del servidor web o archivo abierto).
  * **`observer`:** Equipo de seguridad intermedio que registra el tráfico sin ser origen ni destino (ej. Firewall Palo Alto o Sensor NIDS).

*Etiquetas:* `SecOps::Modulo3::UDMSchema`

---

### Lección 3: Búsqueda UDM (UDM Search)

#### Tarjeta 28
**Pregunta (Anverso / Front):**
> ¿Qué operadores y sintaxis básica se utilizan en una consulta de Búsqueda UDM?

**Respuesta (Reverso / Back):**
  * Operadores de comparación: `=`, `!=`, `>`, `<`, `>=`, `<=`
  * Coincidencia de texto: Expresiones regulares delimitadas por `/patron/` y modificador `nocase`
  * Operadores booleanos: `AND`, `OR`, `NOT`
  * Ejemplo: `metadata.event_type = "USER_LOGIN" AND security_result.action = "BLOCK"`

*Etiquetas:* `SecOps::Modulo3::UDMSearch`

---

### Lección 4: Introducción a Tablas de Datos (Data Tables)

#### Tarjeta 29
**Pregunta (Anverso / Front):**
> ¿Qué es una Tabla de Datos (*Data Table*) en Google SecOps y en qué se diferencia de una Lista de Referencia (*Reference List*)?

**Respuesta (Reverso / Back):**
  * **Reference List:** Lista unidimensional de valores únicos (ej. lista simple de IPs maliciosas).
  * **Data Table:** Estructura bidimensional tabular (filas y columnas) que almacena pares y relaciones complejas de datos contextuales (ej. IP, Hostname, Dueño, Nivel de Criticidad), permitiendo cruces avanzados en búsquedas y reglas.

*Etiquetas:* `SecOps::Modulo3::DataTables`

---

### Lección 5: Búsqueda Estadística y Agregaciones en UDM

#### Tarjeta 30
**Pregunta (Anverso / Front):**
> ¿Cómo se estructura una Búsqueda Estadística en UDM y qué funciones de agregación admite?

**Respuesta (Reverso / Back):**
  Se estructura utilizando la tubería (`|`) de agregación:
  `<filtro UDM> | count(<campo>) by <campo_agrupacion>`
  Funciones comunes:
  * `count()` / `count_distinct()`: Conteo total o de valores únicos.
  * `sum()`, `avg()`, `min()`, `max()`: Cálculos numéricos (ej. bytes transferidos).

*Etiquetas:* `SecOps::Modulo3::StatisticalSearch`

---

## Módulo 4: SIEM Dashboards

### Lección 1: Introducción a Dashboards y Contenido Curado

#### Tarjeta 31
**Pregunta (Anverso / Front):**
> ¿Qué tipos de Dashboards están disponibles en Google SecOps SIEM?

**Respuesta (Reverso / Back):**
  1. **Curated Dashboards (Paneles Curados de Google):** Paneles prediseñados listos para usar sobre fuentes habituales (Cloud Audit, Okta, Windows, MITRE ATT&CK).
  2. **Custom Native Dashboards:** Paneles interactivos creados a medida con consultas YARA-L.
  3. **Legacy Dashboards (Looker):** Paneles de la arquitectura anterior basados en Looker y LookML.

*Etiquetas:* `SecOps::Modulo4::Dashboards`

---

### Lección 2: Construcción de Consultas YARA-L para Dashboards

#### Tarjeta 32
**Pregunta (Anverso / Front):**
> ¿Cómo se compone una consulta YARA-L para widgets en un Dashboard Nativo de SecOps?

**Respuesta (Reverso / Back):**
  Consta de:
  1. **Declaración de eventos:** Filtros sobre campos UDM (`$e.metadata.event_type = ...`).
  2. **Pipes de transformación / agregación:** `| count($e.metadata.id) by $e.principal.user.userid`
  3. **Ordenamiento y límites:** `| order by count desc | limit 10`

*Etiquetas:* `SecOps::Modulo4::YARALQuery`

---

### Lección 3: Filtrado en Dashboards

#### Tarjeta 33
**Pregunta (Anverso / Front):**
> ¿Cuáles son los dos niveles de filtrado que se pueden aplicar en un Dashboard de SecOps?

**Respuesta (Reverso / Back):**
  1. **Filtros a nivel de Widget:** Condiciones embebidas directamente en la consulta YARA-L de un gráfico específico.
  2. **Filtros Globales de Dashboard:** Filtros situados en la cabecera del panel (ej. selector de rango temporal o entorno) que afectan dinámicamente a todos los widgets del dashboard.

*Etiquetas:* `SecOps::Modulo4::Filters`

---

### Lección 4: Funcionalidades Avanzadas de Dashboards Nativos

#### Tarjeta 34
**Pregunta (Anverso / Front):**
> ¿Qué capacidades avanzadas ofrecen los Dashboards Nativos de Google SecOps?

**Respuesta (Reverso / Back):**
  * **Drill-down interactivo:** Hacer clic en un gráfico para saltar directamente a UDM Search con los filtros precargados.
  * **Programación y Exportación:** Envío programado de reportes en PDF/CSV por correo a partes interesadas.
  * **Soporte multivariante:** Múltiples series temporales y visualizaciones en barras, líneas, tablas y mapas de calor.

*Etiquetas:* `SecOps::Modulo4::Advanced`

---

## Módulo 5: SIEM Detections

### Lección 1: Categorías de Detecciones Curadas

#### Tarjeta 35
**Pregunta (Anverso / Front):**
> ¿Qué son las Detecciones Curadas (*Curated Detections*) y quién las mantiene en Google SecOps?

**Respuesta (Reverso / Back):**
  Son conjuntos de reglas de detección preconstruidas y optimizadas, mantenidas y actualizadas de forma continua por **GCTI (*Google Cloud Threat Intelligence*)**.
  Cubren tácticas comunes de MITRE ATT&CK y categorías de amenazas emergentes sin requerir mantenimiento de código por el cliente.

*Etiquetas:* `SecOps::Modulo5::CuratedDetections`

---

### Lección 2: Construcción de Reglas YARA-L, Estructura y Variables

#### Tarjeta 36
**Pregunta (Anverso / Front):**
> ¿Cuáles son las 4 secciones estrictamente obligatorias en toda regla YARA-L?

**Respuesta (Reverso / Back):**
  1. **Identificador / Nombre de la Regla (`rule <nombre_regla> { ... }`)**
  2. **`meta:`** Metadatos descriptivos (autor, descripción, severidad).
  3. **`events:`** Criterios de eventos UDM y definición de variables.
  4. **`condition:`** Condición booleana de activación (ej. `$e` o `$e1 and $e2`).

*Etiquetas:* `SecOps::Modulo5::YARALStructure`

---

#### Tarjeta 37
**Pregunta (Anverso / Front):**
> ¿Qué tres tipos de variables se pueden definir en una regla YARA-L?

**Respuesta (Reverso / Back):**
  1. **Variables de Evento (ej. `$e`, `$login`):** Representan un registro UDM específico.
  2. **Variables de Marcador de Posición / Unión (*Placeholder / Join Variables*, ej. `$user`):** Conectan campos comunes entre múltiples eventos o grafo.
  3. **Variables de Salida (*Outcome Variables*, ej. `$risk_score`):** Valores calculados o enriquecidos que se muestran al analista en la alerta.

*Etiquetas:* `SecOps::Modulo5::YARALVariables`

---

### Lección 3: Regex, Listas de Referencia y Campos Repetidos

#### Tarjeta 38
**Pregunta (Anverso / Front):**
> ¿Cómo se evalúa la coincidencia contra una Lista de Referencia (*Reference List*) en YARA-L?

**Respuesta (Reverso / Back):**
  Se utiliza el operador **`in %<nombre_lista>`**.
  Ejemplo:
  `$e.principal.ip in %malicious_ip_list`
  `$e.target.hostname in %high_value_servers`

*Etiquetas:* `SecOps::Modulo5::ReferenceLists`

---

#### Tarjeta 39
**Pregunta (Anverso / Front):**
> ¿Cómo se evalúa un campo repetido (*repeated field*, ej. lista de destinatarios de correo) en YARA-L?

**Respuesta (Reverso / Back):**
  Google SecOps evalúa los campos repetidos con semántica existencial automática: la condición se cumple si **al menos uno de los elementos** del arreglo cumple el criterio.
  Ejemplo: `$e.network.email.to = "external@attacker.com"` coincide si ese correo está en cualquier posición de la lista de destinatarios.

*Etiquetas:* `SecOps::Modulo5::RepeatedFields`

---

### Lección 4: Funciones YARA-L

#### Tarjeta 40
**Pregunta (Anverso / Front):**
> ¿Qué función nativa de YARA-L se recomienda utilizar para validar si una IP pertenece a una subred CIDR y por qué es mejor que una regex?

**Respuesta (Reverso / Back):**
  La función **`net.ip_in_range_cidr($e.principal.ip, "192.168.1.0/24")`**.
  Es muy superior a regex porque realiza una comprobación binaria/matemática exacta de subred a nivel de red, con un coste computacional ínfimo en comparación con procesar expresiones regulares en texto.

*Etiquetas:* `SecOps::Modulo5::Functions`

---

### Lección 5: Secciones Opcionales (Match, Outcome, Options)

#### Tarjeta 41
**Pregunta (Anverso / Front):**
> ¿Cuáles son las 3 secciones opcionales en YARA-L y qué función cumple cada una?

**Respuesta (Reverso / Back):**
  1. **`match:`** Agrupa eventos por variables comunes en ventanas de tiempo (ej. `$user over 10m`).
  2. **`outcome:`** Calcula métricas, valores agregados o asigna severidad dinámica para la alerta (ej. `$fail_count = count($e.metadata.id)`).
  3. **`options:`** Configura directivas de ejecución del motor (ej. supresión de valores vacíos).

*Etiquetas:* `SecOps::Modulo5::OptionalSections`

---

### Lección 6 y 7: Reglas de Evento Único vs Múltiples Eventos

#### Tarjeta 42
**Pregunta (Anverso / Front):**
> ¿Qué diferencia fundamental existe entre una Regla de Evento Único (*Single Event Rule*) y una Regla de Múltiples Eventos (*Multi-Event Rule*)?

**Respuesta (Reverso / Back):**
  * **Single Event Rule:** Se dispara al evaluar un único registro atómico de forma aislada. No requiere sección `match:`.
  * **Multi-Event Rule:** Correlaciona dos o más eventos (o secuencias temporales del mismo evento) unidos por una variable común en una ventana temporal definida en `match:`. Obligatoria la sección `match:`.

*Etiquetas:* `SecOps::Modulo5::RulesComparison`

---

### Lección 9: Reglas Compuestas (Composite Rules)

#### Tarjeta 43
**Pregunta (Anverso / Front):**
> ¿Qué es el encadenamiento de reglas (*Rule Chaining / Composite Rules*) en Google SecOps?

**Respuesta (Reverso / Back):**
  Es la técnica que toma las **detecciones generadas por otras reglas (*producer rules*)** y las utiliza como criterios de entrada en una nueva regla de orden superior, permitiendo correlacionar comportamientos que individualmente parecían benignos pero que en conjunto denotan un ataque coordinado.

*Etiquetas:* `SecOps::Modulo5::CompositeRules`

---

### Lección 10: Contexto de Entidad

#### Tarjeta 44
**Pregunta (Anverso / Front):**
> En la interfaz de Google SecOps, ¿qué significan los marcadores `[U]` y `[E]` junto a los campos de un evento?

**Respuesta (Reverso / Back):**
  * **`[U]` (*Unenriched / Parsed*):** Datos extraídos textualmente del log crudo original por el parser CBN.
  * **`[E]` (*Enriched*):** Datos agregados dinámicamente por la plataforma durante la ingesta mediante enriquecimiento contextual (ej. geolocalización IP, datos del IdP como departamento o título laboral).

*Etiquetas:* `SecOps::Modulo5::EntityContext`

---

### Lección 11: Aprovechamiento del Grafo de Entidades

#### Tarjeta 45
**Pregunta (Anverso / Front):**
> ¿Qué representa el Grafo de Entidades (*Entity Graph*) en YARA-L y qué son `prevalence` y `rolling_max`?

**Respuesta (Reverso / Back):**
  * **Entity Graph:** Modelo relacional (`$var.graph...`) con metadatos globales (Mandiant / VirusTotal) y derivados internos.
  * **`prevalence`:** Conteo de activos de la empresa que contactaron una entidad en un día (00:00 a 23:59 UTC).
  * **`rolling_max`:** Valor máximo de prevalencia diaria en una ventana móvil de 10 días; útil para detectar balizajes C2 hacia destinos atípicos/raros.

*Etiquetas:* `SecOps::Modulo5::EntityGraph`

---

### Lección 12: Pruebas y Validación de Reglas

#### Tarjeta 46
**Pregunta (Anverso / Front):**
> ¿Qué diferencia existe entre probar una regla con 'Run Test' y ejecutar un 'Retrohunt'?

**Respuesta (Reverso / Back):**
  * **Run Test:** Se ejecuta en el editor sobre un borrador (no necesita guardarse) en hasta **14 días de histórico**. Resultados efímeros, sin persistencia ni alertas.
  * **Retrohunting:** Requiere que la regla esté **guardada**; ejecuta la lógica sobre **semanas o meses** de histórico para medir volumen, verificar antecedentes y calibrar ruido.

*Etiquetas:* `SecOps::Modulo5::RuleTesting`

---

### Lección 13: De Eventos a Alertas

#### Tarjeta 47
**Pregunta (Anverso / Front):**
> ¿Cuál es la diferencia operativa entre el estado 'Live' y el estado 'Alerting' de una regla YARA-L?

**Respuesta (Reverso / Back):**
  * **Modo Live:** El motor genera **detecciones** en segundo plano según el *Run Frequency*, pero **NO dispara alertas visuales ni crea tickets**. Ideal para calibración y reglas productoras.
  * **Modo Alerting:** Cada detección se publica formalmente en la vista **Alerts and IOCs** de SIEM y crea automáticamente un **Caso (*Case*) en SOAR** para respuesta con playbooks.

*Etiquetas:* `SecOps::Modulo5::Alerting`

---

### Lección 14: Métodos para Optimizar Reglas YARA-L

#### Tarjeta 48
**Pregunta (Anverso / Front):**
> ¿Cuáles son las principales recomendaciones para optimizar una regla YARA-L ineficiente?

**Respuesta (Reverso / Back):**
  1. **Filtrado Temprano:** Especificar siempre `metadata.log_type` y `metadata.event_type`.
  2. **Comparación Literal:** Usar `= "4776"` en campos parseados en lugar de regex `/4776/`.
  3. **Agrupación:** Usar `match: $entity over Xm` para consolidar cientos de eventos en una sola detección limpia.
  4. **Funciones Nativas:** Emplear `net.ip_in_range_cidr()` para rangos IP.
  5. **Extensiones CBN:** Extraer datos frecuentes durante la ingesta, no en la regla.

*Etiquetas:* `SecOps::Modulo5::Optimization`

---

