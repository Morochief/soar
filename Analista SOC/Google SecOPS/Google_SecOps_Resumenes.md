# Google Security Operations (SecOps) - Resúmenes de Estudio

> **Curso:** Introducción a Google Security Operations (SIEM)  
> **Ruta oficial:** [Google Security Operations Learning Path](https://www.skills.google/paths/581)  
> **Regla de estilo:** Todo término "SIM" se normaliza a **SIEM**. Contenido estructurado y traducido al español.

---

## Estructura y Programa del Curso (Syllabus)

```
├── Módulo 1: Intro to SIEM (Introducción a SIEM)
│   ├── [Completado] Tema 1: Resumen General de SIEM (SIEM Overview)
│   ├── [Completado] Tema 2: Métodos de Ingesta Admitidos - Resumen (Supported Ingestion Methods Overview)
│   ├── [Completado] Tema 3: Configuración de RBAC en SIEM - Resumen (RBAC Overview)
│   ├── [Completado] Tema 4: Resumen de UDM (UDM Overview)
│   ├── [Completado] Tema 5: Canalización y Normalización (Pipeline & Normalization)
│   ├── [Completado] Tema 6: Métodos de Búsqueda en SIEM - Resumen (Methods of Searching SIEM Overview)
│   ├── [Completado] Tema 7: Resumen de Visualizaciones (Visualizations Overview)
│   ├── [Completado] Tema 8: Resumen del Motor de Detección (Detection Engine Overview)
│   └── [Completado] Evaluación: Comprobación de Conocimientos de Intro to SIEM (Knowledge Check)
│
├── Módulo 2: SIEM Setup (Configuración de SIEM)
│   ├── [Completado] Ingesta: Ingesta Directa (Direct Ingestion)
│   ├── [Completado] Ingesta: Recolección vía APIs de Terceros (Third Party APIs)
│   ├── [Completado] Ingesta: Recolección vía Cloud Storage Buckets
│   ├── [Completado] Ingesta: Servicios de Streaming (Streaming Services)
│   ├── [Completado] Ingesta: Gestión de Feeds (Feed Management)
│   ├── [Completado] Ingesta: Recolección On-Prem: Resumen (On-Prem Overview)
│   ├── [Completado] Ingesta: Patrones de Despliegue de BindPlane (BindPlane Deployment Patterns)
│   ├── [Completado] Ingesta: Configuración de BindPlane (BindPlane Configuration)
│   ├── [Completado] RBAC: RBAC de Funcionalidades (Feature RBAC)
│   ├── [Completado] RBAC: Configuración de Feature RBAC
│   ├── [Completado] RBAC: RBAC de Datos (Data RBAC)
│   ├── [Completado] RBAC: Ámbitos y Etiquetas (Scopes & Labels)
│   ├── [Completado] RBAC: Implementación y Gestión de Data RBAC
│   ├── [Completado] Normalización: Normalización basada en Configuración (CBN - flujo, estructura, funciones)
│   ├── [Completado] Normalización: Extracción de datos (formateados y grok)
│   ├── [Completado] Normalización: Manipulación de datos
│   ├── [Completado] Normalización: Revisión de Parser Completo
│   ├── [Completado] Normalización: Gestión de Parsers y Tipos de Parsers
│   ├── [Completado] Normalización: Demostración de Extensiones de Parsers
│   └── [Completado] Evaluación: SIEM Setup Knowledge Check
│
├── Módulo 3: SIEM Investigation (Investigación en SIEM)
│   ├── [Completado] Tema 1: Búsqueda de Registros en Bruto (Raw Log Search)
│   ├── [Completado] Tema 2: Esquema UDM y Familias de Campos (UDM Schema & Field Families)
│   ├── [Completado] Tema 3: Búsqueda UDM (UDM Search)
│   ├── [Completado] Tema 4: Introducción a Tablas de Datos (Data Tables Introduction)
│   ├── [Completado] Tema 5: Búsqueda Estadística y Agregaciones en UDM (UDM Statistical Search & Aggregation)
│   ├── [Completado] Tema 6: Demostración de Búsqueda UDM (UDM Search Demo)
│   └── [Completado] Evaluación: SIEM Investigation Knowledge Check
│
├── Módulo 4: SIEM Dashboards (Paneles de Control SIEM)
│   ├── [Completado] Tema 1: Introducción a Dashboards y Contenido Curado
│   ├── [Completado] Tema 2: Construcción de Consultas YARA-L para Dashboards
│   ├── [Completado] Tema 3: Filtrado en Dashboards
│   ├── [Completado] Tema 4: Funcionalidades Avanzadas de Dashboards Nativos
│   ├── [Completado] Tema 5: Dashboards Heredados (Legacy Looker Dashboards)
│   └── [Completado] Evaluación: SIEM Dashboards Knowledge Check
│
└── Módulo 5: SIEM Detections (Detecciones en SIEM)
    ├── [Completado] Tema 1: Categorías de Detecciones Curadas, Conjuntos de Reglas y Dependencias
    ├── [Completado] Tema 2: Construcción de Reglas YARA-L, Estructura y Variables
    ├── [Completado] Tema 3: Coincidencia por Regex, Listas de Referencia y Campos Repetidos
    ├── [Completado] Tema 4: Funciones YARA-L
    ├── [Completado] Tema 5: Secciones Opcionales (Match, Outcome, Options)
    ├── [Completado] Tema 6: Reglas de Evento Único (Single Event Rule)
    ├── [Completado] Tema 7: Reglas de Múltiples Eventos (Multiple Event Rule)
    ├── [Completado] Tema 8: Comparativa: Evento Único vs Múltiples Eventos
    ├── [Completado] Tema 9: Resumen de Reglas Compuestas (Composite Rules Overview)
    ├── [Completado] Tema 10: Contexto de Entidad (Entity Context)
    ├── [Completado] Tema 11: Aprovechamiento del Grafo de Entidades en Reglas (Entity Graph)
    ├── [Completado] Tema 12: Pruebas y Validación de Reglas (Rule Testing)
    ├── [Completado] Tema 13: De Eventos a Alertas (From Events to Alerts)
    ├── [Completado] Tema 14: Métodos para Optimizar Reglas YARA-L
    └── [Completado] Evaluación: SIEM Detections Knowledge Check
```

---

# Módulo 1: Intro to SIEM (Introducción a SIEM)

---

### Lección 1: Introducción a SIEM: Resumen General de SIEM (*Intro to SIEM: SIEM Overview*)

#### 1. Capacidades Centrales del Ciclo de Operaciones de Seguridad
Google SecOps SIEM cubre de extremo a extremo el ciclo de vida de operaciones de seguridad mediante cuatro fases fundamentales:

```
[ Ingesta y Colección ] ➔ [ Búsqueda y Analítica ] ➔ [ Detección ] ➔ [ Respuesta (SOAR) ]
```

1. **Recolección de Telemetría (*Telemetry Collection*):**
   * Ingesta, normalización y enriquecimiento de datos de todo el entorno.
   * Constituye el pilar fundamental para analizar y correlacionar información a gran escala.
2. **Búsqueda y Analítica de Riesgo (*Search & Risk Analytics*):**
   * Permite realizar búsquedas de amenazas (*threat hunting*), investigar comportamientos anómalos y descubrir patrones ocultos o riesgos potenciales.
3. **Detección (*Detection*):**
   * Análisis proactivo y continuo de los datos recolectados.
   * Integra reglas de detección, inteligencia de amenazas nativa y analítica avanzada para visibilizar señales de seguridad relevantes.
4. **Respuesta (*Response - SOAR*):**
   * Orquestación y automatización de respuesta ante incidentes.
   * *Nota:* Mientras que SIEM se enfoca en recolección, analítica y detección, el componente **SOAR** (*Security Orchestration, Automation, and Response*) se encarga de ejecutar acciones y flujos de mitigación automatizados.

#### 2. Hoja de Ruta y Estructura del Curso
El módulo introductorio sienta las bases conceptuales que se profundizarán en módulos dedicados:
* **Ingesta de Datos (*Data Ingestion*):** Fundamento de la plataforma; cubre métodos directos, conectores en la nube, agentes de recolección y APIs.
* **Control de Acceso Basado en Roles (*RBAC*):** Gestión de permisos y roles en SIEM (diferenciado del modelo SOAR).
* **Modelo de Datos Unificado (*UDM*):** Búsqueda estructurada y normalizada sobre logs, combinada con la búsqueda de texto crudo (*Raw Log Search*).
* **Módulo de Investigación (*SIEM Investigation*):** Metodologías de análisis y exploración profunda de entidades y eventos.
* **Parseo y Normalización (*Parsing & Normalization*):** Transformación de telemetría heterogénea a UDM en la canalización (*pipeline*) de datos.
* **Visualización y Paneles (*Dashboards*):** Transición de paneles *legacy* (Looker) a paneles nativos basados en YARA-L.
* **Motor de Detección (*Detection Engine*):** Creación y ejecución de reglas analíticas personalizadas y curadas.

---

### Lección 2: Introducción a SIEM: Métodos de Ingesta de Datos Admitidos (*Intro to SIEM: SIEM Supported Data Ingestion Methods - Overview*)

Comprender la ingesta de datos es esencial, ya que sienta las bases para la detección eficaz de amenazas, la investigación y la respuesta dentro de Google SecOps. La plataforma admite la recolección de registros de eventos en bruto (*raw event logs*), alertas de seguridad y fuentes de datos contextuales tanto en entornos locales (*on-premise*) como en la nube.

#### Los 4 Métodos de Ingesta Principales

```
                  ┌──────────────────────────────────────────────────────────┐
                  │               Google SecOps SIEM                         │
                  │              (Ingestion Service)                         │
                  └─────────────────────────▲────────────────────────────────┘
                                            │
       ┌──────────────────────┬─────────────┴────────────┬──────────────────────┐
       │                      │                          │                      │
[ Ingesta Directa ]    [ Ingesta Cloud ]        [ Agentes Colección ]    [ Ingesta API ]
  (GCP Cloud Logging     (Data Feeds, Cloud       (ObserveIQ BindPlane,    (RESTful API,
   SCC Findings, etc.)    Buckets, Webhooks,      On-premise / VMs)        Desarrollo propio)
                          APIs de 3ros: Okta)
```

1. **Ingesta Directa (*Direct Ingestion*):**
   * Permite recopilar fuentes de telemetría directamente desde Google Cloud (GCP) hacia Google SecOps en tiempo casi real.
   * Se configura mediante filtros de **Cloud Logging** dentro de la consola de GCP.
   * Aplica a eventos de Cloud Logging, metadatos de activos en la nube (*Cloud Asset metadata*) y hallazgos de **Security Command Center (SCC) Premium**.

2. **Ingesta Cloud-to-Cloud / Fuentes de Datos (*Data Feeds*):**
   * Diseñada para telemetría generada en otros entornos de nube.
   * **Extracción estática (*Pull*):** Obtiene logs desde almacenes externos (ej. buckets de Google Cloud Storage) o APIs de terceros admitidas (ej. Okta).
   * **Servicios de transmisión continua (*Push / Streaming*):** Admite mecanismos como **Webhooks**, que transmiten los eventos en tiempo casi real al ocurrir, en vez de depender de un temporizador de consulta (*polling*).
   * Se configuran mediante el servicio de gestión de feeds (*Feed Management*), accesible desde la interfaz web o mediante la API de gestión de feeds.

3. **Agentes de Recolección (*Collection Agents*):**
   * Software diseñado para capturar eventos en redes locales de clientes (*on-premise*) o máquinas virtuales administradas en la nube.
   * Basados en **BindPlane** (recolector de OpenTelemetry desarrollado por ObserveIQ), cuya licencia viene incluida con Google SecOps.
   * Se puede instalar en múltiples sistemas operativos para recolectar, clasificar y reenviar una extensa variedad de fuentes de logs hacia Google SecOps.

4. **API de Ingesta (*Ingestion API*):**
   * API RESTful que sirve como punto de entrada frontal para todo el servicio de ingesta de Google SecOps.
   * Aunque los métodos anteriores interactúan internamente con ella, los clientes, socios tecnológicos o MSSPs (*Managed Security Service Providers*) pueden desarrollar aplicaciones personalizadas para transmitir registros directamente a esta API sin intermediarios.

---

### Lección 3: Introducción a SIEM: Configuración de RBAC (SIEM) - Resumen de RBAC (*Intro to SIEM: Configuring RBAC (SIEM) - RBAC Overview*)

#### 1. ¿Qué es RBAC y por qué es importante?
El Control de Acceso Basado en Roles (*Role-Based Access Control - RBAC*) en Google SecOps permite definir con precisión exacta qué **funcionalidades** y qué **datos** pueden acceder los distintos grupos de usuarios.
* Proporciona un control de permisos granular bajo el principio de privilegio mínimo (*least privilege*).
* **Ejemplo práctico de segregación:**
  * **Grupo A:** Puede consultar logs de fuentes específicas (ej. A, B y C), pero tiene restringidos los logs confidenciales (X, Y y Z). A nivel funcional, puede realizar búsquedas pero tiene prohibido redactar reglas de detección.
  * **Grupo B:** Perfil con privilegios más amplios; puede consultar todos los conjuntos de logs y además tiene permisos para crear y modificar reglas de detección YARA-L.

---

#### 2. Las 3 Capas Principales de Control de Acceso en SecOps

```
┌────────────────────────────────────────────────────────────────────────┐
│                      Capas de Control RBAC                             │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Feature RBAC (Cloud IAM)  ➔ Permisos sobre funciones de SecOps SIEM │
│ 2. Data RBAC (SecOps UI)     ➔ Restricción granular a nivel de logs    │
│ 3. SOAR RBAC                 ➔ Privilegios para alertas y playbooks    │
└────────────────────────────────────────────────────────────────────────┘
```

1. **RBAC de Funcionalidades (*Feature RBAC en Cloud IAM*):**
   * Aplica control de acceso granular sobre las funcionalidades de Google SecOps SIEM utilizando las políticas de **Google Cloud IAM** (Identity and Access Management).
   * Define quién puede ver interfaces, crear reglas, ejecutar búsquedas, etc.

2. **RBAC de Datos (*Data RBAC en la UI de SecOps*):**
   * Configurado dentro de la propia interfaz de Google SecOps.
   * Restringe el acceso a datos de registros específicos (mediante etiquetas/scopes), garantizando que los analistas solo visualicen la telemetría estrictamente relevante para su rol.

3. **RBAC de SOAR (*SOAR RBAC*):**
   * Gestiona que los equipos de SecOps cuenten con los privilegios adecuados para investigar alertas, así como para diseñar y ejecutar *playbooks* de respuesta automatizada.

---

#### 3. Visión a Futuro de Google
* La visión a largo plazo de Google es **consolidar estas tres capas dentro de Google Cloud IAM**, ofreciendo una experiencia unificada que simplifique la administración centralizada de accesos y permisos en toda la plataforma SecOps.
* En este curso de SIEM, el foco principal estará en **Feature RBAC (Cloud IAM)** y **Data RBAC**. (SOAR RBAC se cubre en el curso específico de SOAR).


---

### Lección 4: Introducción a SIEM: Resumen de UDM (*Intro to SIEM: UDM Overview*)

#### 1. El Problema de los Registros en Bruto (*Raw Logs*)
* **Falta de Estandarización:** Los datos de seguridad llegan de forma desestructurada y heterogénea. Cada fabricante registra el mismo tipo de evento (ej. un bloqueo de red) en su propio formato y con nombres de campo propietarios.
* **Ejemplo Práctico:**
  * **Palo Alto Firewall:** Nombres de campo propietarios para fecha/hora, acción, IP origen, IP destino, puerto, etc.
  * **Fortinet Firewall:** Describe exactamente el mismo evento pero utilizando nombres de campos totalmente diferentes (`srcip`, `dstip`, etc.) y formatos distintos de sesión.
* **Consecuencia:** Sin un esquema unificado, los analistas se ven obligados a memorizar la sintaxis y nombres de campos de cada fabricante solo para realizar una consulta simple o redactar una regla.

---

#### 2. La Solución de Google SecOps: El Modelo de Datos Unificado (*UDM*)
Google SecOps normaliza estos registros desestructurados hacia un esquema común estándar (**Unified Data Model - UDM**).

| Concepto de Red / Seguridad | Campo Propietario (Palo Alto / Fortinet) | Campo Estándar UDM |
| :--- | :--- | :--- |
| **Fecha y Hora del Evento** | `timestamp` / `time` | `metadata.event_timestamp` |
| **Acción Tomada** | `action="allow"` / `action="deny"` | `security_result.action` |
| **Dirección IP Origen** | `src` / `srcip` | `principal.ip` |
| **Dirección IP Destino** | `dst` / `dstip` | `target.ip` |
| **Puerto Destino** | `dport` / `dstport` | `target.port` |
| **Protocolo / Sesión** | `proto`, `sessionid` | Campos consistentes en UDM |

---

#### 3. Beneficios Clave de UDM para el Analista
1. **Búsquedas Simplificadas:** Un solo nombre de campo para consultar datos de cualquier fabricante simultáneamente.
2. **Reutilización Universal:** Las reglas de detección YARA-L y los *playbooks* de SOAR se redactan una sola vez contra el esquema UDM y funcionan automáticamente para todos los orígenes de datos.
3. **Ahorro de Tiempo en Investigaciones:** Los analistas no necesitan saltar de una consola de producto a otra; todo se correlaciona bajo un único lenguaje.

---

#### 4. Ventajas de la Normalización en Tiempo de Ingesta (*Schema-on-Write*)
En Google SecOps, los datos se normalizan a UDM **en el mismo instante de la ingesta**, lo que aporta beneficios arquitectónicos superiores:
* **Incorporación Inmediata de Fuentes (*Faster Onboarding*):** Al agregar un nuevo dispositivo, si sus datos se parsean a UDM, quedan inmediatamente cubiertos por las reglas y playbooks existentes sin requerir desarrollo adicional.
* **Telemetría Completa y Escalable:** Diseñado específicamente para ciberseguridad, con soporte para entidades múltiples y campos repetidos (*repeated fields*).
* **Enriquecimiento Automático de Datos (*Data Enrichment*):** Durante la ingesta se incorpora contexto valioso (geolocalización, metadatos, reputación) de forma automática sin requerir consultas manuales ni comandos adicionales en tiempo de búsqueda.
* **Documentación Oficial:** Google proporciona el diccionario completo de campos y tipos de datos en la [Guía de Sintaxis de Campos UDM](https://cloud.google.com/chronicle/docs/unified-data-model/udm-field-list).


---

### Lección 5: Introducción a SIEM: Canalización y Normalización (*Intro to SIEM: Pipeline & Normalization*)

#### 1. Las 4 Fases de la Canalización de Datos (*Data Pipeline*)
Google SecOps procesa los registros sin procesar mediante un flujo estructurado de 4 etapas:

```
[ 1. Ingestión ] ➔ [ 2. Normalización ] ➔ [ 3. Indexación ] ➔ [ 4. Vinculación / Aliasing ]
```

1. **Ingestión (*Ingestion*):**
   * Recolección de registros en bruto (*raw logs*) desde herramientas de endpoint, plataformas en la nube, cortafuegos o pasarelas de correo en su formato nativo original.
2. **Normalización (*Normalization*):**
   * Fase donde los analizadores sintácticos (*parsers*) procesan y transforman los logs sin procesar en el esquema estandarizado **UDM** (*Unified Data Model*).
3. **Indexación y Enriquecimiento (*Indexing & Enrichment*):**
   * Extracción de campos clave (usuarios, direcciones IP, dominios, marcas de tiempo), enriquecimiento con metadatos contextuales y organización de la información para permitir búsquedas ultrarrápidas, visualizaciones y evaluación de reglas.
4. **Vinculación de Identidades (*Aliasing*):**
   * Conexión de puntos y relaciones entre entidades del entorno (por ejemplo, asociar una dirección IP dinámica a un dispositivo específico y a su usuario correspondiente en un momento exacto), creando una visión unificada de la actividad.

---

#### 2. Definición y Características del Modelo UDM
La normalización traduce registros dispares de múltiples proveedores hacia la estructura común de UDM.
* **Estructura en árbol con campos anidados:** Describe con precisión las distintas entidades involucradas en un evento.
* **Características Clave de UDM:**
  * **Exhaustivo (*Comprehensive*):** Cubre telemetría de red y endpoint, incluyendo atributos específicos de usuarios y activos.
  * **Independiente del Fabricante (*Vendor Independent*):** Cualquier registro se mapea a la misma estructura conceptual.
  * **Flexible y Extensible (*Flexible & Extensible*):** Admite la incorporación continua de nuevas fuentes y tipos de registros sin romper esquemas previos.

---

#### 3. Tipos de Datos en UDM: Eventos vs. Entidades

```
┌────────────────────────────────────────────────────────────────────────┐
│                        Modelos de Datos en UDM                         │
├────────────────────────────────────────────────────────────────────────┤
│ • Datos de Eventos (Event Data):  Ocurren en un punto en el tiempo     │
│   Ejemplo: Inicio de sesión, modificación de archivo, bloqueo de red.   │
├────────────────────────────────────────────────────────────────────────┤
│ • Datos de Entidades (Entity Data / Entity Graph): Estado o contexto   │
│   Ejemplo: Departamento del usuario, rol, nivel de privilegios.         │
│   Pueden ser perpetuos o actualizarse conforme cambia el contexto.     │
└────────────────────────────────────────────────────────────────────────┘
```
* **Cosido Contextual (*Stitching*):** El proceso de normalización une (*stitches*) la telemetría de eventos con el contexto de las entidades, creando eventos enriquecidos con información que no estaba presente en el log sin procesar original.

---

#### 4. Parsers: Normalización Basada en Configuración (CBN)
Los analizadores o **CBNs** (*Configuration-Based Normalizers*) contienen la lógica que traduce los logs en bruto a eventos UDM normalizados.
* **Sintaxis:** Muy similar a **Logstash**, ofreciendo potentes funciones para extraer campos y procesar valores en bruto.
* **Gestión por Interfaz Web (*Parser Management UI*):** Permite administrar, probar y activar parsers directamente desde la consola de Google SecOps.
* **Gestión por Línea de Comandos (`chronicle_cli`):** Ideal para equipos avanzados y desarrolladores que requieren automatización, integración con pipelines de CI/CD, scripting y control de versiones (Git) para compilar, probar, validar y desplegar parsers de forma programática.


---

### Lección 6: Introducción a SIEM: Métodos de Búsqueda (SIEM) - Resumen (*Intro to SIEM: Methods of Searching (SIEM) Overview*)

#### 1. Búsqueda e Investigación: Personas y Casos de Uso
La búsqueda es el núcleo de cualquier investigación en SecOps SIEM, permitiendo aislar actividad relevante entre volúmenes masivos de telemetría. Diferentes perfiles (*personas*) aprovechan estas capacidades:

* **Propietarios de Datos (*Data Owners*):**
  * Configuran fuentes de datos y validan que el registro y parseo sean exitosos, asegurando que la información sea accesible para detecciones y análisis.
* **Ingenieros de Detección (*Detection Engineers*):**
  * Utilizan criterios de búsqueda para diseñar, probar y operacionalizar reglas YARA-L, verificando que los campos críticos estén correctamente parseados.
* **Cazadores de Amenazas (*Threat Hunters*):**
  * Exploran conjuntos amplios de datos a lo largo de períodos extensos para confirmar o refutar hipótesis de ataque, o para descubrir nuevos criterios que originen futuras detecciones.
* **Analistas de Seguridad (*Security Analysts*):**
  * Investigan alertas y salidas de detecciones YARA-L, reconstruyen la secuencia de eventos y ejecutan acciones de respuesta ante incidentes.

---

#### 2. Los Dos Métodos de Búsqueda Principales: Raw Log Search vs. UDM Search

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      Métodos de Búsqueda en SecOps                          │
├──────────────────────────────────────┬──────────────────────────────────────┤
│ 1. Raw Log Search                    │ 2. UDM Search                        │
│ (Búsqueda de Registros en Bruto)     │ (Búsqueda sobre el Modelo Unificado) │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ • Datos no parseados (originales)    │ • Datos normalizados y enriquecidos  │
│ • Búsqueda por cadenas / Regex libre │ • Consultas estructuradas por campos │
│ • Ideal para auditoría/cumplimiento  │ • Ideal para análisis transversal    │
│ • Velocidad más lenta                │ • Velocidad rápida a media           │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

1. **Búsqueda de Registros en Bruto (*Raw Log Search*):**
   * Consulta directa sobre el texto original sin procesar tal como fue ingerido línea por línea.
   * Admite coincidencias directas de cadenas de texto (*string matching*) y expresiones regulares (*regex*).
   * **Ventajas y Casos de Uso:** Muy útil para requerimientos de cumplimiento (*compliance*), auditorías forenses estrictas o para inspeccionar logs cuando aún no se dispone de un parser.
   * **Limitación:** Al operar sobre texto desestructurado, la velocidad de respuesta es más lenta en comparación con UDM.

2. **Búsqueda UDM (*UDM Search*):**
   * Consulta sobre datos estandarizados, parseados y enriquecidos en el momento de la ingesta bajo el esquema UDM.
   * Permite realizar búsquedas estructuradas y consistentes a través de múltiples fuentes de fabricantes heterogéneos en una única consulta.
   * **Operadores Avanzados:** Soporta lógica booleana (`AND`, `OR`, `NOT`), expresiones regulares sobre campos concretos, comparaciones numéricas/enteros (`>=`, `<`) y visualización en tablas estructuradas.
   * **Velocidad y Precisión:** Rendimiento de búsqueda significativamente más rápido, convirtiéndose en el método predilecto para investigaciones activas y cacería de amenazas (*threat hunting*).


---

### Lección 7: Introducción a SIEM: Resumen de Visualizaciones (*Intro to SIEM: Visualizations Overview*)

#### 1. Propósito e Importancia de los Paneles (*Dashboards*)
* **Visibilidad Rápida:** Los paneles proporcionan a los analistas una forma ágil y visual de comprender la actividad en su entorno, abarcando desde tendencias de alto nivel hasta investigaciones detalladas.
* **Cobertura de Datos:** Facilitan la visualización y análisis de datos de seguridad:
  * Telemetría y métricas de ingesta.
  * Detecciones y alertas.
  * Indicadores de Compromiso (IoCs).
* **Interfaz Intuitiva:** Transforma datos de seguridad complejos en gráficos, diagramas y mapas claros que ayudan a identificar rápidamente patrones y anomalías.
* **Consolidación de Casos de Uso:** Permite a los analistas centralizar tareas clave en un único lugar:
  * Rastrear tendencias.
  * Monitorear la salud y estado de los datos.
  * Apoyar la investigación de incidentes.
  * Priorizar alertas de seguridad.
* **Esquema Estandarizado (UDM):** Las visualizaciones se basan en un esquema estandarizado: el Modelo de Datos Unificado (*Unified Data Model - UDM*). Con la nueva sintaxis unificada (en fase *preview*), es posible generar gráficos directamente a partir de criterios de búsqueda existentes.

#### 2. Evolución de los Paneles en Google SecOps: *Legacy* vs. Nativos

| Característica | Paneles Heredados (*Legacy*) | Paneles Nativos (Estándar Futuro) |
| :--- | :--- | :--- |
| **Tecnología base** | Instancia embebida de **Looker**. | Construidos directamente dentro de **Google SecOps**. |
| **Motor de Consultas** | Consultas basadas en Looker. | Impulsados por sintaxis **YARA-L** para consultas avanzadas y potentes. |
| **Seguridad y Control** | Limitado al Looker embebido. | Soporta capacidades empresariales como control de acceso basado en roles (**RBAC**). |
| **Estado actual** | Aún visibles/disponibles temporalmente. | En proceso de adopción; se convertirán en el estándar predeterminado. |

#### 3. Navegación y Acceso en la Consola
Para acceder a los paneles dentro de la interfaz de Google SecOps:
1. Abrir el menú de navegación principal del *tenant*.
2. Ir a la sección **Dashboards and Reports** (*Paneles e Informes*).
3. Seleccionar la vista correspondiente:
   * **SIEM Dashboards** (*Paneles de SIEM*)
   * **Preview Dashboards** (*Paneles en vista previa*)
   * **SOAR Dashboards and Reports** (*Paneles e informes de SOAR*)

---

### Lección 8: Introducción a SIEM: Resumen del Motor de Detección (*Intro to SIEM: Detection Engine Overview*)

#### 1. Importancia y Propósito del Motor de Detección
El motor de detección (*Detection Engine*) es uno de los componentes más críticos dentro de la plataforma; se encuentra en el núcleo de Google SecOps permitiendo a los equipos de seguridad monitorear continuamente amenazas en sus entornos.

* **Monitoreo Continuo y Correlación:** Analiza eventos de seguridad provenientes de múltiples fuentes para detectar patrones sospechosos e incidentes potenciales en redes, endpoints o aplicaciones.
* **Inteligencia de Amenazas Nativa (*Threat Intelligence*):** Contrasta de forma automática Indicadores de Compromiso (IoCs)—tanto provistos por Google como personalizados por el cliente—contra los datos de eventos ingeridos. Esto genera alertas de concienciación y permite afinar la lógica de detección.
* **Analítica Avanzada y Basada en Riesgo:** Aprovecha datos contextuales, funciones matemáticas y métricas derivadas para detectar ataques sofisticados que las técnicas tradicionales suelen pasar por alto.

#### 2. Los 3 Componentes Clave (*Building Blocks*) del Motor de Detección

1. **Sintaxis YARA-L:**
   * Lenguaje de detección derivado de **VirusTotal**, diseñado específicamente para casos de uso de ciberseguridad.
   * Permite a los analistas escribir reglas precisas sobre la telemetría de registros (logs) para identificar actividad maliciosa o sospechosa.
2. **Detecciones Seleccionadas / Curadas (*Curated Detections*):**
   * Conjuntos de reglas listos para usar (*out-of-the-box*) y mantenidos por Google.
   * Proporcionan cobertura inmediata contra un amplio espectro de amenazas comunes sin necesidad de crearlas desde cero.
3. **Editor de Reglas (*Rules Editor*):**
   * Interfaz donde los usuarios pueden crear detecciones avanzadas y personalizadas.
   * Admite capacidades como agregaciones, correlaciones complejas y generación de alertas en tiempo casi real (*near real-time*), permitiendo frenar amenazas mientras se están desarrollando.

---

### Lección 9: Comprobación de Conocimientos (*Intro to SIEM: Knowledge Check*)

A continuación se presentan las preguntas de evaluación traducidas al español con su respuesta correcta y justificación técnica:

#### 1. ¿Cuál de los siguientes es un elemento central del Motor de Detección en Google SecOps?
* **Respuesta Correcta:** **Sintaxis YARA-L (*YARA-L Syntax*)**
* *Justificación:* YARA-L es el lenguaje de reglas especializado desarrollado para consultar telemetría estructurada y modelar la lógica de detección dentro de Google SecOps.

#### 2. ¿Cuál es la diferencia entre la Búsqueda de Registros sin Procesar (*Raw Log Search*) y la Búsqueda UDM (*UDM Search*) en Google SecOps?
* **Respuesta Correcta:** **La Búsqueda de Registros sin Procesar consulta datos no parseados mediante coincidencias de texto o expresiones regulares, mientras que la Búsqueda UDM consulta datos normalizados a través de la interfaz de búsqueda SIEM.** (*Raw Log Search queries unparsed data using string matches or regular expressions, while UDM Search queries normalized data through the SIEM Search interface*).
* *Justificación:* *Raw Log Search* busca sobre el texto original/crudo del registro, mientras que *UDM Search* aprovecha la estructura de campos estandarizados del modelo UDM.

#### 3. ¿Por qué es ventajoso parsear datos a UDM en el momento de la ingesta para la ingeniería de detección?
* **Respuesta Correcta:** **Permite el uso inmediato de datos normalizados en las reglas de detección.** (*It enables immediate use of normalized data in detection rules.*)
* *Justificación:* Al estandarizar el esquema de los logs en tiempo de ingesta (*schema-on-write*), el motor de detección puede evaluar reglas YARA-L de inmediato sin tener que reinterpretar o transformar los logs en cada consulta.

#### 4. ¿Cuáles son los componentes clave involucrados en la normalización dentro de Google SecOps?
* **Respuesta Correcta:** **Sintaxis CBN, Interfaz de Gestión de Parsers (y/o la herramienta chronicle_cli)** (*CBN syntax, Parser Management UI (and/or the chronicle_cli tool)*)
* *Justificación:* El parser mapping usa sintaxis CBN (Customer Built Normalization) y se administra desde la interfaz de usuario de administración de parsers o mediante la utilidad de consola `chronicle_cli`.

#### 5. ¿Cuál es el rol de UDM (Modelo de Datos Unificado) en Google SecOps?
* **Respuesta Correcta:** **Proporciona un esquema de datos estandarizado que normaliza telemetría de seguridad diversa para una búsqueda, detección y análisis consistentes.** (*It provides a standardized data schema that normalizes diverse security telemetry for consistent search, detection, and analysis*)
* *Justificación:* UDM unifica registros de cientos de fabricantes distintos bajo un formato común de entidades y eventos.

#### 6. ¿Qué regula el Control de Acceso Basado en Roles (RBAC) en Google SecOps?
* **Respuesta Correcta:** **Determina a qué funciones y datos pueden acceder los usuarios.** (*It determines which features and data users can access*)
* *Justificación:* RBAC establece permisos granulares asignando roles a usuarios para delimitar las acciones que pueden ejecutar y los datos visibles.

#### 7. ¿Cuáles son los métodos de ingesta de datos admitidos en Google SecOps SIEM?
* **Respuesta Correcta:** **Ingesta Directa, Nube, Agentes de Recolección y API de Ingesta.** (*Direct Ingestion, Cloud, Collection Agents, and Ingestion API*)
* *Justificación:* Google SecOps permite enviar datos directamente desde servicios soportados, conectores *cloud-to-cloud*, agentes reenviadores (forwarders/collection agents) y mediante su Ingestion API REST.

---

# Módulo 2: SIEM Setup (Configuración de SIEM)

---

### Lección 1: Configuración de SIEM: Ingesta de Datos - Recolección mediante Ingesta Directa (*SIEM Data Ingestion - Data Collection using Direct Ingestion*)

#### 1. ¿Qué es la Ingesta Directa (*Direct Ingestion*)?
Es la capacidad nativa e integrada de Google SecOps para recopilar telemetría de eventos y datos de contexto directamente desde servicios de Google sin requerir infraestructura intermedia.
* **Fuentes admitidas actualmente:**
  * Registros de **Google Cloud (GCP Logs)**.
  * Metadatos de activos en la nube (**Cloud Asset metadata** de Cloud Asset Inventory).
  * Hallazgos de **Security Command Center (SCC) Premium**.
  * Registros de actividad de **Google Workspace** (ej. auditoría de Gmail, Drive, etc.).

---

#### 2. Requisitos Previos por Tipo de Fuente
* **Google Cloud Platform (GCP):**
  * Proyecto de Google Cloud vinculado al *tenant* de Google SecOps.
  * Para **Cloud Asset metadata**: Licencia de SCC Standard o SCC Premium.
  * Para **SCC Premium Findings**: Licencia activa de SCC Premium.
* **Google Workspace:**
  * Licencias corporativas compatibles: **Workspace Enterprise Standard** o **Workspace Enterprise Plus**.

---

#### 3. Beneficios Clave de la Ingesta Directa
* **Sin Infraestructura Adicional:** No requiere configurar buckets de almacenamiento (Cloud Storage), tópicos Pub/Sub, ni instalar agentes recolectores (BindPlane).
* **Tiempo Casi Real (*Near Real-Time*):** Los eventos se transfieren de inmediato a SecOps para acelerar la detección y respuesta.
* **Alcance a Nivel de Organización GCP (*Organization-Level*):** Habilita la recolección centralizada a través de toda la organización de GCP de forma predeterminada, garantizando visibilidad global sobre todos los recursos vinculados.

---

#### 4. Procedimiento de Configuración

##### A. Para Fuentes de Google Cloud (GCP):
1. Ingresar a la consola de Google Cloud y seleccionar el proyecto asociado a SecOps.
2. En el menú de navegación, ir a la sección de productos de seguridad y seleccionar **Google SecOps**.
3. Hacer clic en la pestaña **Ingestion** (Ingesta).
4. Habilitar los interruptores correspondientes (Google Cloud Logs, Cloud Asset Metadata, SCC Premium Findings).
5. **Filtro de Exportación Personalizado (*Custom Export Filter*):**
   * *Por defecto:* Incluye **Cloud Audit Logs** (actividad de administradores y eventos del sistema) y registros de **Cloud DNS**.
   * *Personalización:* Permite agregar fuentes adicionales mediante la sintaxis de Cloud Logging (ej. Cloud IDS, Cloud Load Balancing, Cloud Next Generation Firewall, Apigee, reCAPTCHA Enterprise, etc.) o excluir telemetría irrelevante.

##### B. Para Registros de Google Workspace (3 Pasos):
1. **Paso 1:** Obtener el ID de cliente (*Customer ID*) desde la consola de administración de Google Workspace.
2. **Paso 2:** En la consola de Google SecOps, ir a la pestaña de configuración SIEM para Google Workspace, ingresar el *Customer ID* y hacer clic en **Generate Token**.
3. **Paso 3:** Usar el token generado y el *Instance ID* de SecOps en la consola de Workspace Admin para autorizar el enlace.

---

#### 5. Consideraciones Críticas y Limitaciones

* **Proyectos gestionados por terceros / MSSP:**
  * Si el cliente no aloja directamente el proyecto GCP vinculado a SecOps (escenario habitual en MSSPs), se requiere un **código de acceso de un solo uso (*one-time access code*)** provisto por un representante de Google para autorizar la conexión entre la organización GCP del cliente y la instancia SecOps.
* **Solo Registros Hacia Adelante (*No Historical Logs*):**
  * La ingesta directa solo captura eventos generados a partir del momento en que se habilita el filtro de exportación. **No importa logs históricos**. Si se requieren datos del pasado, debe utilizarse otro método (ej. Cloud Storage buckets).
* **Catálogo Fijo de Fuentes:**
  * Las fuentes de Workspace o GCP no contempladas en la ingesta directa (como contexto de usuarios o grupos de Workspace) deben ingerirse mediante Feeds o Cloud Storage.
* **Sin Soporte de Namespaces ni Ingestion Labels:**
  * **Espacios de Nombres (*Namespaces*):** Característica de SecOps para diferenciar activos con direcciones IP solapadas en redes distintas (ej. red on-premise vs red cloud privada). La ingesta directa **no** permite asignar namespaces.
  * **Etiquetas de Ingesta (*Custom Ingestion Labels*):** Pares clave-valor arbitrarios para enriquecer datos en la ingesta. La ingesta directa **no** permite asignar etiquetas personalizadas directamente (se requiere hacerlo mediante data feeds, BindPlane o modificando el parser).

---

### Lección 2: Configuración de SIEM: Ingesta de Datos - Recolección de Registros mediante APIs de Terceros (*SIEM Data Ingestion - Collecting Logs Using Third Party APIs*)

#### 1. ¿Qué son los Feeds de API de Terceros (*Third-Party API Feeds*)?
Son conectores gestionados nube a nube (*cloud-to-cloud*) provistos de forma nativa por Google SecOps para extraer (*pull*) registros de eventos e información contextual directamente desde los endpoints de APIs REST seguras de plataformas SaaS y proveedores de nube externos.
* **Cobertura:** Google SecOps soporta feeds preconstruidos para cerca de **50 fuentes populares en la nube**, incluyendo:
  * **Identidad y Accesos (IAM):** Microsoft Entra ID (antes Azure AD), Okta, Duo Security.
  * **Seguridad y EDR:** Palo Alto Networks, Proofpoint.
  * **Gestión de Servicios e Inteligencia:** ServiceNow, Anomali, etc.
* **Mecanismo:** La plataforma consulta los endpoints de las APIs de los servicios externos de forma programada (*scheduled basis*), garantizando una ingesta continua sin intervención manual.

---

#### 2. Permisos Requeridos en Google Cloud IAM
Para administrar y crear feeds dentro de Google SecOps, el usuario debe poseer los permisos de IAM correspondientes en el proyecto GCP vinculado.
* **Rol predeterminado recomendado:** Rol de IAM **`Chronicle API Admin`** (incluye los permisos necesarios para gestionar la configuración de feeds).

---

#### 3. Proceso de Configuración en la Interfaz (UI)
1. **Navegación:** Ir a **SecOps Settings** ➔ **SIEM Settings** ➔ **Feeds**.
2. **Creación:** Hacer clic en **Add New**.
3. **Tipo de Origen (*Source Type*):** Seleccionar **Third Party API**.
4. **Tipo de Log (*Log Type*):** Escoger el formato de origen compatible correspondiente (ej. Microsoft Entra ID / Azure AD).
5. **Parámetros de Entrada (*Input Parameters*):** Dependen de cada proveedor. Generalmente requieren:
   * Identificadores de cuenta / Tenant ID / Nombre de usuario.
   * Credenciales seguras: Contraseña, secreto de cliente (*Client Secret*) o Clave API (*API Key*).
   * En ciertos casos, permisos específicos sobre una cuenta de servicio configurada en la aplicación origen.
6. **Espacios de Nombres (*Namespaces*) y Etiquetas de Ingesta (*Ingestion Labels*):**
   * *A diferencia de la Ingesta Directa, aquí sí es posible configurar Namespaces e Ingestion Labels.*
   * **Ejemplo de Ingestion Label:** Clave: `environment`, Valor: `corporate` (o `production`).
   * En los eventos normalizados resultantes en UDM, esto se refleja en el campo:
     ```
     metadata.ingestion_labels["environment"] = "corporate"
     ```
   * Permite filtrar y segmentar datos con total precisión en búsquedas, paneles y reglas YARA-L.
7. **Revisión y Envío:** Revisar los valores y hacer clic en **Submit**.

---

#### 4. Monitoreo del Estado del Feed
En la tabla de **Feed Management UI**:
* La columna **Status** confirma si la conexión fue exitosa (*Success*) o si presentó fallos (*Failed*).
* Un estado fallido suele deberse a credenciales incorrectas, permisos insuficientes en el proveedor de origen o URLs de API no válidas. Al posar el cursor sobre el icono de interrogación `?` se obtienen detalles del error.

---

#### 5. Ventajas y Limitaciones

* **Ventajas:**
  * **Sencillez y Rapidez:** Configuración ágil en pocos clics.
  * **Completamente Gestionado:** Mantenido y actualizado por Google ante cambios de APIs de terceros.
  * **Cero Middleware:** No requiere instalar agentes ni mantener servidores o bases de datos intermedias.
  * **Soporte de Etiquetas:** Permite etiquetar la telemetría con metadatos personalizados y asociar *namespaces*.

* **Limitaciones / Cuándo considerar otras opciones:**
  * **Fuentes no soportadas:** Si la plataforma SaaS del cliente no figura en la lista oficial de feeds soportados, se debe recurrir a almacenamiento en Cloud Storage (Buckets), Webhooks o agentes BindPlane.
  * **Sin transformación previa al envío (*No pre-filtering/masking*):** Los feeds API de terceros no permiten enmascarar datos sensibles (PII) ni descartar subconjuntos de eventos antes de que ingresen a SecOps. Si se requiere modificar o anonimizar los logs previo a la ingesta, se debe utilizar un agente recolector intermedio como BindPlane.

---

### Lección 3: Configuración de SIEM: Ingesta de Datos - Recolección de Registros mediante Buckets de Almacenamiento en la Nube (*SIEM Data Ingestion - Collecting Logs Using Cloud Storage Buckets*)

#### 1. ¿Cuándo usar la Ingesta por Buckets de Almacenamiento?
Cuando una fuente de telemetría no admite ingesta directa ni cuenta con un feed preconstruido de API de terceros, o cuando las aplicaciones escriben sus logs directamente en almacenamiento de objetos en la nube.
* **Servicios de Almacenamiento Compatibles:**
  1. **Google Cloud Storage (GCS)**
  2. **Amazon Simple Storage Service (Amazon S3)**
  3. **Microsoft Azure Blob Storage**
* **Mecanismo:** Google SecOps extrae (*pulls*) los datos almacenados en el bucket periódicamente (actualmente con un intervalo de **cada 15 minutos**).
* **Universalidad:** Dado que cualquier tipo de dato puede depositarse en un bucket, **prácticamente cualquier fuente de logs puede ser ingerida en SecOps** a través de este método.

---

#### 2. Requisitos Previos Esenciales

1. **Datos en el Bucket:** La fuente debe escribir los logs directamente en el bucket (o el cliente debe implementar una automatización para depositarlos allí).
2. **Etiqueta de Ingesta Estándar / Tipo de Log (*Log Type / Data Ingestion Label*):**
   * Es la etiqueta interna que identifica el formato de los logs que se están recopilando.
   * **Propósito fundamental:** SecOps utiliza este valor para **asignar el analizador sintáctico (*parser*) adecuado** que normalizará los eventos a UDM.
   * El valor de `log_type` queda registrado en los eventos normalizados. Si no existe una etiqueta para un formato particular, debe solicitarse a Google antes de ingerir los datos.
3. **Cuenta de Servicio con Permisos de Lectura:**
   * Google SecOps requiere credenciales o cuentas de servicio con privilegios suficientes para leer los objetos del bucket.

---

#### 3. Particularidades de Configuración por Proveedor

* **Google Cloud Storage (GCS):**
  * Se genera una cuenta de servicio desde la interfaz de *Feed Management*.
  * En GCP Cloud IAM se le debe otorgar como mínimo el rol **`Storage Object Viewer`**.
  * Si se activa la opción de **Eliminación de Origen (*Source Deletion*)** (para que SecOps borre los archivos ya transferidos), la cuenta requiere el rol **`Storage Object Admin`**.
* **Amazon S3:**
  * Es indispensable especificar de forma exacta en la ruta URI si se trata de un **archivo único**, un **directorio**, o un **directorio con subdirectorios** para que el escaneo funcione correctamente.
  * Si se activa la eliminación de origen, las credenciales de acceso (*Access Key*) deben contar con permisos de borrado (`s3:DeleteObject`).

---

#### 4. Cuatro Consideraciones Críticas (*Best Practices*)

1. **Costos Operativos (*Cost*):**
   * Además del coste de almacenar los archivos, SecOps realiza lecturas constantes (cada 15 min). Se recomienda seleccionar una clase de almacenamiento (*storage tier*) que tolere solicitudes de lectura frecuentes sin incurrir en costes elevados por operaciones API.
2. **Datos Históricos (*Historical Data*):**
   * A diferencia de la Ingesta Directa, **los buckets permiten ingerir datos históricos pasados**.
   * *Recomendación:* Establecer políticas de ciclo de vida/retención en el bucket o habilitar la eliminación de origen en SecOps para evitar reprocesar o re-listar archivos antiguos en cada ciclo.
3. **Rendimiento y Volumen de Archivos (*Throughput*):**
   * Muchos archivos muy pequeños (*small files*) degradan drásticamente el rendimiento de transferencia del feed.
   * *Recomendación:* Consolidar múltiples archivos pequeños en archivos de mayor tamaño antes o durante su depósito en el bucket para acelerar el proceso de ingesta.
4. **Etiquetado Preciso de Datos (*Accurate Data Labeling*):**
   * **Regla estricta:** Solo se puede asignar **un único `log_type` (etiqueta de ingesta) por feed**.
   * *Recomendación:* Separar orígenes de logs en buckets distintos o mediante estructuras de subdirectorios aislados (un URI único por tipo de log). Nunca mezclar formatos de logs distintos en la misma ruta de bucket.

---

### Lección 4: Configuración de SIEM: Ingesta de Datos - Ingesta en la Nube: Servicios de Streaming (*SIEM Data Ingestion - Cloud Ingestion - Streaming Services*)

#### 1. Transferencia por Lotes (*Batch*) vs. Servicios de Streaming (*Streaming*)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   Batch Transfer vs. Streaming Services                     │
├──────────────────────────────────────┬──────────────────────────────────────┤
│ Lotes / Batch (Cloud Storage Buckets)│ Servicios de Streaming (Push)        │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ • Extracción periódica (Pull).       │ • Envío continuo e inmediato (Push). │
│ • Frecuencia programada (cada 15 m). │ • En tiempo casi real (Near RT).     │
│ • Mayor latencia de ingesta.         │ • Menor latencia, mayor throughput.  │
│ • Retraso en detección y alertas.    │ • Reduce el tiempo medio de detección│
│                                      │   (MTTD - Mean Time to Detect).      │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

* **Servicios de Streaming Soportados:**
  * **Amazon Data Firehose**
  * **Amazon Simple Queue Service (Amazon SQS)**
  * **Google Cloud Pub/Sub**
  * **Microsoft Azure Event Hubs**
  * **Webhooks** (HTTP/HTTPS)

---

#### 2. Requisitos Previos Generales
Para configurar la ingesta por servicios de transmisión HTTPS, comúnmente se requiere:
1. Proyecto de Google Cloud Platform vinculado al *tenant* de Google SecOps.
2. Clave secreta generada para el feed (*Feed Secret Key*).
3. Clave de API de GCP (*API Key*) para que el origen externo se autentique contra SecOps.

---

#### 3. Ingesta Mediante Amazon SQS (Notificaciones de S3)
En lugar de que SecOps sondee periódicamente un bucket de Amazon S3 cada 15 minutos, se puede configurar una cola **Amazon SQS** que reciba eventos de notificación inmediatos cuando se escriben nuevos objetos en el bucket.
* SecOps lee las notificaciones de la cola SQS e ingiere al instante los archivos correspondientes del bucket S3.
* **Beneficio:** Convierte una ingesta *pull* en una solución reactiva basada en *push*, mejorando el rendimiento (*throughput*) y la puntualidad de los datos.
* **Configuración Clave:**
  * Tipo de origen en Feed Management: **Amazon SQS**.
  * La cuenta de servicio debe tener permisos para leer e ingerir del bucket S3 y **permisos para eliminar mensajes procesados en la cola SQS** (`sqs:DeleteMessage`).

---

#### 4. Configuración Paso a Paso de Webhooks (Uno de los Métodos Más Populares)

##### Paso 1: Configurar el Feed en Google SecOps
1. Ir a **Feed Management UI** y hacer clic en **Add New**.
2. **Source Type:** Seleccionar **Webhook**.
3. **Parámetros:** Definir el delimitador entre registros (por defecto salto de línea `\n`, aunque depende del emisor). Opcionalmente configurar *Namespaces* e *Ingestion Labels*.
4. Hacer clic en **Submit**.

##### Paso 2: Generar y Copiar Identificadores Críticos
* En la ventana resultante, hacer clic en **Generate Secret Key** ➔ **Copiar y guardar la Clave Secreta**.
* En la pestaña **Details**, localizar y copiar el **Feed ID**.
* Verificar el endpoint generado por SecOps.

##### Paso 3: Crear la API Key en GCP Cloud Console
1. Acceder a la consola de GCP en el proyecto vinculado a SecOps.
2. Ir a **APIs & Services** ➔ **Credentials** ➔ **Create Credentials** ➔ **API Key**.
3. *Buena práctica de seguridad:* Restringir la API Key para que únicamente pueda invocar la **Chronicle API**.

##### Paso 4: Configurar la Fuente de Datos Emisora
La aplicación emisora enviará las solicitudes HTTP POST hacia la URL de destino estructurada con los siguientes parámetros:
* `REGION`: Región GCP donde se aloja SecOps.
* `PROJECT_NUMBER`: Número de proyecto GCP vinculado.
* `CUSTOMER_ID`: ID de cliente de SecOps (obtenido en *SIEM Settings*).
* `FEED_ID`: El ID del feed copiado previamente.

**Autenticación en la Fuente:**
* *Método recomendado:* Pasar la **API Key** y la **Secret Key** en los **encabezados HTTP (*Headers*)**.
* *Alternativa:* Si la aplicación origen no admite encabezados personalizados, se permite enviar ambos valores como parámetros de consulta en la URL (*query string*).

---

### Lección 5: Configuración de SIEM: Ingesta de Datos - Ingesta en la Nube: Gestión de Feeds (*SIEM Data Ingestion - Cloud Ingestion - Feed Management*)

#### 1. Marco Unificado de Gestión de Feeds (*Feed Management Framework*)
Todas las fuentes de ingesta nube a nube (*cloud-to-cloud*) en Google SecOps operan bajo el mismo marco de trabajo unificado, administrable tanto desde la consola web (**Feed Management UI**) como mediante programación (**Feed Management API**).

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    Marco Unificado de Feed Management                       │
│                     (Consola Web UI y RESTful API)                          │
├─────────────────────────────────────────────────────────────────────────────┤
│ • APIs de Terceros (Third-Party API Feeds)  ➔ Extracción (Pull) programada  │
│   (Okta, Microsoft Entra ID, ServiceNow, Duo, etc.)                         │
├─────────────────────────────────────────────────────────────────────────────┤
│ • Buckets de Almacenamiento (Cloud Buckets) ➔ Extracción (Pull) en lotes    │
│   (Google Cloud Storage, Amazon S3, Azure Blob)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ • Servicios de Streaming                    ➔ Ingesta continua (Push)       │
│   (Amazon SQS, Google Pub/Sub, Webhooks, Azure Event Hubs)                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

#### 2. Capacidades de la Interfaz Web (*Feed Management UI*)
Ubicada en: **SecOps Settings ➔ SIEM Settings ➔ Feeds**.
* **Información Visible por Feed:**
  * Estado operativo (*Status*): Indica si la ingesta está activa y saludable o si presenta errores.
  * Tipo de origen (*Source Type*).
  * Tipo de log normalizado (*Log Type*).
  * Marca de tiempo de la última ingesta exitosa (*Timestamp of last successful ingestion*).
* **Operaciones Disponibles (Menú contextual de 3 puntos):**
  * **Habilitar / Deshabilitar (*Enable / Disable*):** Pausar temporalmente la recolección sin borrar la configuración.
  * **Ver Propiedades (*View Properties*):** Inspeccionar parámetros, etiquetas de ingesta y endpoints.
  * **Editar (*Edit*):** Modificar credenciales, rutas de buckets o configuraciones de red.
  * **Eliminar (*Delete*):** Suprimir el feed permanentemente.

---

#### 3. Automatización mediante la API de Gestión de Feeds (*Feed Management API*)
Diseñada para clientes corporativos y proveedores de servicios gestionados (**MSSPs**) que administran múltiples *tenants* o requieren automatización continua:
* Permite listar, crear, actualizar, activar, desactivar y eliminar feeds mediante scripts o herramientas de CI/CD (infraestructura como código).
* **Documentación Oficial de la API:** Especifica para cada origen los parámetros obligatorios/opcionales, límites de consultas (*query limits*), cronogramas de ingesta por defecto, formatos de solicitud y respuestas de ejemplo.

---

#### 4. Tabla Comparativa de Métodos de Ingesta Nube a Nube (*Cloud-to-Cloud*)

| Método de Feed | Mecanismo | Frecuencia / Latencia | Casos de Uso Típicos |
| :--- | :--- | :--- | :--- |
| **APIs de Terceros** | Extracción (*Pull*) | Programada periódicamente | Servicios SaaS (Okta, Entra ID, Salesforce, ServiceNow). |
| **Buckets de Almacenamiento** | Extracción (*Pull*) | Lotes programados (cada 15 min) | Archivos estáticos en S3, GCS, Azure Blob; datos históricos. |
| **Servicios de Streaming** | Inserción (*Push*) | Tiempo casi real (*Near Real-Time*) | Telemetría continua de alto volumen (SQS, Webhooks, Pub/Sub, Event Hubs). |

---

### Lección 6: Configuración de SIEM: Ingesta de Datos - Recolección de Datos On-Premise: Resumen (*SIEM Data Ingestion - On-Prem Data Collection: Overview*)

#### 1. Necesidad de Recolección Local y Sustitución de Chronicle Forwarder
En entornos corporativos donde la infraestructura reside en redes locales (*on-premise*) o nubes privadas administradas por el cliente, se requiere recolectar los logs en el origen y reenviarlos de forma segura a Google SecOps.
* **Evolución tecnológica:** El agente de recolección **BindPlane** reemplaza por completo a la solución anterior denominada *Chronicle Forwarder*, proporcionando capacidades modernas de recopilación y procesamiento.
* **Alianza estratégica:** BindPlane (antes conocido como ObserveIQ) es socio de Google Cloud y uno de los principales contribuyentes del proyecto de código abierto **OpenTelemetry (OTel)**.

---

#### 2. Componentes de la Solución BindPlane

```
┌────────────────────────────────────────────────────────────────────────┐
│                        Arquitectura BindPlane                          │
├────────────────────────────────────────────────────────────────────────┤
│ 1. BindPlane Server (Opcional / Recomendado):                          │
│    Consola central para orquestar configuración, rutas y agentes.      │
├────────────────────────────────────────────────────────────────────────┤
│ 2. BindPlane Collection Agent (Agente OTel):                           │
│    Instalado en endpoints/servidores. Recolecta, clasifica y envía.    │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Agente de Recolección BindPlane (*BindPlane Collection Agent*):**
   * Es la distribución optimizada de BindPlane del *OpenTelemetry Collector*.
   * Recolecta, clasifica y reenvía telemetría de eventos hacia Google SecOps.
   * **Amplio soporte de sistemas operativos:** Compatible con Windows, Linux, macOS, Kubernetes y Red Hat OpenShift.
   * **Diversidad de fuentes soportadas:** Logs de eventos de Windows (Event Viewer/WEF), consultas SQL directas a bases de datos, reenvío de Syslog, archivos locales, etc.
   * **Bifurcación avanzada de datos (*Routing / Splitting*):** Capacidad de enviar telemetría simultáneamente a múltiples destinos de Google (Google SecOps, Cloud Logging, BigQuery).

2. **Servidor BindPlane (*BindPlane Server*):**
   * Componente opcional pero altamente recomendado para la gestión centralizada de múltiples agentes desplegados en la infraestructura.
   * Centraliza la lógica de recolección, filtrado y enrutamiento en un único panel de control.

---

#### 3. Licenciamiento y Ediciones de BindPlane en SecOps

Todos los clientes de Google SecOps tienen derecho a licencias de BindPlane incluidas con su suscripción:

| Nivel de Suscripción Google SecOps | Edición de BindPlane Incluida | Capacidades Destacadas |
| :--- | :--- | :--- |
| **SecOps Standard / Enterprise** | **BindPlane Google Edition** | Agente y Servidor incluidos. Reenvío a destinos de Google (SecOps SIEM, Cloud Logging, BigQuery). |
| **SecOps Enterprise Plus** | **BindPlane Enterprise Google Edition** | Funciones avanzadas: **bifurcación a destinos que no son de Google** y capacidades de **redacción / transformación de datos** (enmascarar PII, filtrar logs antes de la ingesta). |
| *Suscripción de pago opcional* | **BindPlane Enterprise** | Licencia completa de BindPlane para casos avanzados multicloud / observabilidad general. |

---

#### 4. Descarga, Instalación y Soporte Técnico
* **Opciones de Descarga:**
  1. *Desde SecOps:* Ir a **SIEM Settings ➔ Collection Agents**, que enlaza al repositorio oficial de GitHub con los binarios de instalación.
  2. *Desde BindPlane Server:* Generar comandos automáticos de despliegue para descargar y ejecutar el agente directamente en los servidores.
* **Modelo de Soporte:**
  * **Google:** Proporciona soporte técnico de primer nivel (Nivel 1) para el **BindPlane Collection Agent**.
  * **BindPlane (ObserveIQ):** Brinda soporte para el componente **BindPlane Server**.

---

### Lección 7: Configuración de SIEM: Ingesta de Datos - Recolección On-Premise: Patrones de Despliegue de BindPlane (*SIEM Data Ingestion - On-Prem Data Collection: BindPlane Deployment Patterns*)

#### 1. Conceptos y Roles de BindPlane
* **BindPlane Agent:** Se instala directamente en servidores y terminales para recopilar logs locales y reenviarlos.
* **BindPlane Gateway:** Es el mismo agente BindPlane configurado en rol de **agregador intermedio**, posicionado entre los orígenes de datos locales y Google SecOps.
* **BindPlane Server:** Consola de gestión centralizada (SaaS o local) para orquestar y configurar masivamente los agentes y pasarelas.

---

#### 2. Los 4 Patrones de Despliegue de Agentes y Pasarelas

```
Patrón 1: Agente Directo           Patrón 2: Gateway Syslog
[ Endpoint (Agent) ] ──TLS──> SecOps   [ Syslog Sources ] ──Syslog──> [ Gateway ] ──TLS──> SecOps

Patrón 3: Agente a Gateway (OTel)  Patrón 4: Bifurcación / Multi-Destino
[ Endpoints (Agents) ] ──OTel─┐        [ Agent / Gateway ] ──┬──> Google SecOps
                              ▼                              ├──> Cloud Logging
                      [ Gateway ] ──TLS──> SecOps            └──> BigQuery / 3rd Party
```

##### Patrón 1: Envío Directo desde Agentes en Endpoints (*Direct to SecOps*)
* El agente BindPlane se instala en los servidores/hosts y envía los registros directamente al endpoint de SecOps.
* Asigna la etiqueta de ingesta de SecOps (`log_type`) en el origen.
* **Escenario ideal:** Entornos que no requieren agregación intermedia y cuentan con proxies autenticados o firewalls Layer 7 que permiten conexiones salientes directas hacia las APIs de Google SecOps.

##### Patrón 2: Recolección Centralizada por Syslog mediante BindPlane Gateway
* Dispositivos de red, firewalls o appliances envían logs por protocolo Syslog al **BindPlane Gateway**.
* **Mejor Práctica (*Best Practice*):** Asignar un **puerto de escucha único por tipo de fuente** en el Gateway.
  * *Ejemplo:* Palo Alto al puerto TCP `10514`, Zscaler VPN al `10515`, switches Cisco al `10516`.
  * El Gateway asigna automáticamente el `log_type` correspondiente según el puerto de entrada y reenvía el tráfico encriptado a SecOps.
* **Reemplazo directo:** Es la ruta estándar y directa para migrar despliegues del antiguo *Chronicle Forwarder*.

##### Patrón 3: Agentes Locales hacia BindPlane Gateway mediante OpenTelemetry (OTel)
* Los agentes instalados en hosts envían sus logs hacia el BindPlane Gateway mediante el protocolo nativo **OpenTelemetry Protocol (OTLP)**:
  * Puerto **TCP 4317** para gRPC.
  * Puerto **TCP 4318** para HTTP.
* El valor de `log_type` asignado por el agente se preserva intacto al pasar por el Gateway.
* **Beneficios:** Minimiza drásticamente las conexiones salientes a Internet (solo el Gateway sale por el firewall corporativo), admite alta disponibilidad (*load balancing*) y permite arquitecturas híbridas (mezcla de agentes OTel y fuentes Syslog).

##### Patrón 4: Bifurcación de Datos (*Data Bifurcation / Multi-Destination*)
* Permite dividir la telemetría y enviarla a múltiples destinos simultáneamente.
* *Ejemplo:* Enviar logs de seguridad a **Google SecOps**, telemetría operativa a **GCP Cloud Logging** y copias para análisis a **BigQuery**.
* **Estrategia de Optimización de Costos (*Tiering*):** Envío de telemetría de auditoría/cumplimiento de bajo valor a almacenes económicos (Cloud Logging) y eventos críticos a SecOps.
* *Nota de Licencia:* La bifurcación a destinos de Google viene incluida en *BindPlane Google Edition*. El envío a destinos externos no-Google (SIEMs de terceros) requiere *BindPlane Enterprise Google Edition* (SecOps Enterprise Plus) o *BindPlane Enterprise*.
* Permite además canalizar **Logs, Métricas (Cloud Monitoring) y Trazas (Cloud Trace)** desde el mismo agente.

---

#### 3. Opciones de Despliegue de la Consola BindPlane Server

| Opción de Despliegue | Tipo de Alojamiento | Características |
| :--- | :--- | :--- |
| **1. BindPlane Cloud (SaaS)** | Alojado por BindPlane (`app.bindplane.com`) | Cero instalación. Comunicación agente-servidor vía protocolo OAMP (*Open Agent Management Protocol*) sobre TLS (puerto 443). Incluido con *Google Edition*. |
| **2. BYOL en GCP Marketplace** | Máquina Virtual dentro del proyecto GCP del cliente | Despliegue directo desde Google Cloud Marketplace. |
| **3. BindPlane Server On-Premise** | Linux local (Debian, RPM, Docker) | Para organizaciones con políticas estrictas que prohíben consolas SaaS externas. |

---

### Lección 8: Configuración de SIEM: Ingesta de Datos - Recolección On-Premise: Configuración de BindPlane (*SIEM Data Ingestion - On-Prem Data Collection: BindPlane Configuration*)

#### 1. Instalación del Agente BindPlane
A través del asistente de instalación (*Installation Wizard*) en BindPlane Server (ej. BindPlane Cloud):
* Se selecciona la versión del agente, el sistema operativo (Windows, Linux, macOS, Kubernetes u OpenShift) y un nombre de configuración.
* El asistente genera un comando de una sola línea adaptado al SO que descarga e instala el agente y lo conecta de forma segura a BindPlane Server.

---

#### 2. Anatomía de una Configuración en BindPlane
Una configuración le indica al agente **qué recolectar**, **cómo procesarlo** y **a dónde enviarlo**.
* *Regla:* Una misma configuración puede asignarse a muchos agentes, pero **cada agente solo puede tener una única configuración activa**.

```
┌─────────────────┐       ┌──────────────────────┐       ┌──────────────────────┐
│ Fuentes         │  ──>  │ Procesadores         │  ──>  │ Destinos             │
│ (Sources)       │       │ (Processors)         │       │ (Destinations)       │
│ Windows Events, │       │ Estandarización      │       │ Google SecOps SIEM   │
│ TCP/UDP Syslog  │       │ log_type, Regex, etc.│       │ (gRPC o HTTPS)       │
└─────────────────┘       └──────────────────────┘       └──────────────────────┘
```

---

#### 3. Configuración de Fuentes Comunes (*Sources*)

* **Eventos de Windows (*Windows Event Logs*):**
  * Se selecciona la fuente *Windows Event*.
  * Permite marcar los canales estándar (*Application*, *Security*, *System*).
  * **Configuración Crítica:** Es indispensable activar la opción **`Raw Logs`** en las opciones avanzadas, ya que el parser de Windows en Google SecOps espera recibir el log en su formato crudo original para normalizarlo correctamente a UDM.
* **Fuentes Syslog de Red (en BindPlane Gateway):**
  * Se debe seleccionar la fuente **`TCP Logs`** o **`UDP Logs`** según corresponda.
  * *Advertencia:* No usar la fuente genérica "Syslog" de BindPlane si esta modifica o pre-parsea el registro alterando el formato esperado por el parser de SecOps.
  * **Asignación de Puertos Únicos:** Crear una fuente por cada tipo de dispositivo con un puerto alto libre (ej. TCP `10514` para Palo Alto, `10515` para VPN, etc.).

---

#### 4. Configuración del Destino (*Google SecOps Destination*)
Al elegir como destino **Google SecOps**:
* **Protocolos Soportados:**
  * **gRPC:** Conecta a los endpoints *Malachite* de SecOps utilizando credenciales en archivo JSON de cuenta de servicio.
  * **HTTPS:** Conecta a la API moderna de plano de datos (*Data Plane API*) de Google SecOps.
* **Campos Requeridos (Flujo gRPC):**
  1. **Authentication Method:** Seleccionar **JSON** y pegar el contenido de la clave de cuenta de servicio (descargada en SecOps en *SIEM Settings ➔ Collection Agents*).
  2. **Customer ID:** Ingresar el identificador del tenant de SecOps (*SIEM Settings ➔ Profile / Organization Settings*).
  3. **Fallback Log Type (Recomendado):** Asignar una etiqueta por defecto (ej. `catch_all`) para etiquetar logs que no vengan explícitamente tipificados.
  4. Opcionalmente configurar *Namespaces* o *Ingestion Labels* para el gateway.

---

#### 5. Procesadores en BindPlane: Etiquetado Preciso con `log_type`
Los procesadores transforman y manipulan la telemetría antes de enviarla a Google SecOps.
* **Puntos de Inserción:**
  * **Después de las Fuentes (*After Sources*):** Afecta únicamente a ese flujo particular. *(Práctica recomendada para asignar el tipo de log lo más cerca del origen posible).*
  * **Antes de los Destinos (*Before Destinations*):** Aplica a todo el tráfico que sale hacia el destino común.
* **Procesador de Estandarización de Google SecOps (*Google SecOps Standardization Processor*):**
  * Permite inyectar la etiqueta obligatoria **`log_type`** (ej. `PAN_FIREWALL`, `WINEVTLOG`, etc.) para que SecOps aplique el parser correcto en la ingesta.
  * Permite añadir **condiciones lógicas** para asignar diferentes `log_type` si por una misma fuente o puerto fluyen múltiples tipos de eventos.

---

#### 6. Validación y Despliegue (*Rollout*)
* **Vista previa en vivo (*Live Preview*):** BindPlane permite visualizar la telemetría en tránsito haciendo clic en los procesadores para validar que el formato y las etiquetas sean correctos sin almacenar nunca los datos en el servidor de BindPlane.
* **Start Rollout:** Publica y activa la configuración hacia todos los agentes asignados. Tras unos minutos, los registros comienzan a ingresar a SecOps y pueden verificarse mediante una búsqueda de registros en bruto (*Raw Log Search*).

---

### Lección 9: Configuración de SIEM: Configuración de RBAC (SIEM) - RBAC de Funcionalidades (*Configuring RBAC (SIEM) - Feature RBAC*)

#### 1. Del Modelo Heredado (*Legacy RBAC*) al Modelo Moderno (*Feature RBAC*)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    Evolución del Control de Acceso (RBAC)                   │
├──────────────────────────────────────┬──────────────────────────────────────┤
│ Modelo Heredado (Legacy RBAC)        │ Modelo Moderno (Feature RBAC)        │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ • Gestionado solo dentro de la UI.   │ • Integrado directamente en Cloud IAM│
│ • No permitía crear roles a medida.  │ • Roles predefinidos y personalizados│
│ • Sin registros de auditoría (logs). │ • Registro automático en Audit Logs. │
│ • Sin base para RBAC a nivel de datos│ • Habilita y sustenta Data RBAC.     │
│ • Ya no está en uso / deprecado.     │ • Estándar actual de Google SecOps.  │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

* **Limitaciones del Legacy RBAC:** Solo ofrecía cuatro roles fijos e inalterables sin granularidad y sin trazabilidad forense de las acciones realizadas por los administradores.
* **Ventajas de Feature RBAC con Google Cloud IAM:**
  * **Asignación basada en políticas de IAM:** Vincula grupos de identidades corporativas con roles específicos de SecOps.
  * **Roles Predefinidos (*Predefined Roles*):** Alineados exactamente con los cuatro roles originales para una migración limpia.
  * **Roles Personalizados (*Custom IAM Roles*):** Permite crear combinaciones de permisos exactas para las necesidades operativas de la organización.
  * **Trazabilidad y Auditoría (*Cloud Audit Logs*):** Toda acción administrativa queda registrada automáticamente en logs de auditoría de GCP, los cuales pueden reinyectarse a SecOps para su propia supervisión.
  * **Visión Unificada:** Se extenderá a otros módulos como Google SecOps SOAR para gobernar toda la plataforma desde Cloud IAM.

---

#### 2. Requisitos Previos para la Migración
Para habilitar y migrar a Feature RBAC, los clientes deben cumplir con dos condiciones fundamentales:
1. **BYOP (*Bring Your Own Project*):** Disponer de un proyecto de Google Cloud Platform (GCP) formalmente vinculado al *tenant* de Google SecOps.
2. **BYOIDP (*Bring Your Own Identity Provider*):** Contar con un proveedor de identidades corporativo (IdP) configurado mediante **Federación de Identidades (*Identity Federation*)** y políticas de Google Cloud IAM establecidas.

---

#### 3. Métodos de Migración y Habilitación
* **Clientes Directos:**
  * Se activa desde la consola de GCP: Navegar al proyecto vinculado ➔ **Google SecOps** ➔ pestaña **Access Management** ➔ Habilitar Feature RBAC.
* **Proveedores de Servicios de Seguridad Gestionada (MSSPs):**
  * La API de gestión de clientes (*Customer Management API*) cuenta con el endpoint **`generate IAM migration commands`**.
  * Genera automáticamente los comandos de consola de `gcloud` necesarios para aprovisionar las políticas de Cloud IAM equivalentes, acelerando la migración masiva de múltiples clientes.

---

### Lección 10: Configuración de SIEM: Configuración de RBAC (SIEM) - Configuración Práctica de Feature RBAC (*Configuring Feature RBAC*)

#### 1. Roles Predefinidos en Google Cloud IAM (*Predefined Roles*)
Constituyen el punto de partida recomendado para implementar Feature RBAC, ya que siguen las mejores prácticas de seguridad y son mantenidos directamente por Google.
* **Roles Principales de Chronicle API:**
  * **`Chronicle API Admin`:** Control administrativo total sobre la plataforma, configuración de feeds e ingesta.
  * **`Chronicle API Editor`:** Permisos de lectura, edición y creación de reglas/búsquedas, sin privilegios destructivos o de administración global.
  * **`Chronicle API Viewer`:** Acceso de solo lectura para análisis, visualización e investigación de incidentes.
* **Asignación en la Consola de GCP:**
  1. En la consola de Google Cloud, acceder a **IAM & Admin** en el proyecto vinculado a SecOps.
  2. Hacer clic en **Grant Access** (Otorgar acceso).
  3. En **Add Principals**, ingresar el usuario, grupo corporativo, cuenta de servicio o identidad de fuerza de trabajo (*Workforce Identity*).
  4. En **Assign Roles**, filtrar por la palabra clave `chronicle` y seleccionar el rol predefinido adecuado siguiendo el principio de mínimo privilegio (*least privilege*).
  5. Guardar los cambios.

---

#### 2. Creación y Gestión de Roles Personalizados (*Custom IAM Roles*)
Cuando los roles predefinidos no satisfacen los requisitos organizacionales específicos, se pueden crear roles personalizados desde: **IAM & Admin ➔ Roles** dentro del proyecto GCP de SecOps.

Existen dos estrategias principales de implementación:

##### Estrategia A: Duplicación a partir de un Rol Predefinido (*Create from Role*)
* **Propósito:** Tomar como base un rol oficial y realizar pequeños ajustes (añadir o retirar permisos puntuales).
* **Flujo:**
  1. Localizar el rol oficial (ej. `Chronicle API Editor`).
  2. Hacer clic en **Create from Role** (Crear a partir de rol).
  3. Asignar un nuevo nombre descriptivo al rol personalizado.
  4. Quitar los permisos innecesarios o incorporar los permisos específicos requeridos por la política interna.

##### Estrategia B: Enfoque de Roles por Capas (*Layered Custom Role Approach*)
* **Propósito:** Combinar la estabilidad y actualización automática de los roles estándar de Google con permisos hiperespecializados para funciones concretas.
* **Ejemplo Práctico:**
  * Se asignan **dos roles simultáneos** al mismo usuario (ej. Sam Johnson):
    1. **Rol Base (Predefinido):** `Chronicle API Viewer` ➔ Otorga visibilidad general de solo lectura en toda la plataforma SecOps y se actualiza automáticamente con nuevas capacidades que libere Google.
    2. **Rol Elevado (Personalizado):** `custom_chronicle_native_dashboard_permissions` ➔ Concede permisos específicos únicamente para crear, duplicar y modificar **Paneles Nativos (Native Dashboards)**.
* **Beneficio:** Evita tener que otorgar permisos excesivos de Administrador/Editor general a usuarios que solo necesitan operar un componente especializado.

---

### Lección 11: Configuración de SIEM: Configuración de RBAC (SIEM) - RBAC de Datos (*Configuring RBAC (SIEM) - Data RBAC*)

#### 1. Concepto y Utilidad de Data RBAC
Mientras que **Feature RBAC** controla *qué acciones* puede realizar un usuario en la plataforma (ej. buscar, editar reglas), **Data RBAC** restringe *qué eventos y registros específicos* puede ver ese usuario según sus atributos y etiquetas.
* **Casos de Uso Esenciales:**
  * Entornos multi-equipo o multi-inquilino (*multi-tenant*).
  * Separación estricta de telemetría por líneas de negocio, geografías o criticidad (ej. analistas de IAM que solo deben ver logs de Okta, o equipos de red que solo deben acceder a firewalls).

---

#### 2. Tipos de Acceso a Datos
1. **Acceso Global a Datos (*Global Data Access*):**
   * Acceso irrestricto a toda la telemetría ingerida en el *tenant* de SecOps.
2. **Acceso Delimitado por Ámbitos (*Scoped Data Access*):**
   * Acceso restringido exclusivamente a los datos que coinciden con los **Ámbitos de Datos (*Scopes*)** asignados al usuario o grupo.

---

#### 3. ¿Qué es un Ámbito (*Data Scope*)?
Un **Ámbito (*Scope*)** es una política de acceso a datos construida a partir de una **combinación lógica de Etiquetas de Datos (*Data Labels*)**.
* Los *Scopes* se crean y definen dentro de la interfaz web de Google SecOps.
* Posteriormente se asignan a identidades o grupos mediante **Políticas Condicionales en Google Cloud IAM**.

#### 4. Alcance y Cobertura de Data RBAC

| Componentes donde APLICA Data RBAC | Componentes donde NO APLICA Data RBAC |
| :--- | :--- |
| ✅ Búsqueda SIEM (*SIEM Search*) | ❌ Detecciones Curadas (*Curated Rules*) |
| ✅ Reglas de detección personalizadas YARA-L | ❌ Paneles Heredados (*Legacy Looker Dashboards*) |
| ✅ Tablas de Datos (*Data Tables*) | ❌ UEBA (*User and Entity Behavior Analytics*) |
| ✅ Paneles Nativos (*Native Dashboards*) | |

---

#### 5. Ciclo de Implementación de Data RBAC en 4 Pasos

```
[ 1. Planificación ] ➔ [ 2. Categorización ] ➔ [ 3. Crear Scopes ] ➔ [ 4. Asignar en IAM ]
(Identificar grupos)   (Definir Data Labels)   (En SecOps UI)          (Políticas Condicionales)
```

1. **Paso 1: Planificación:** Identificar los grupos de usuarios y las fuentes a restringir (ej. ingenieros de IAM que solo necesitan telemetría de autenticación).
2. **Paso 2: Categorización de Datos:** Usar etiquetas existentes o definir etiquetas personalizadas (*custom data labels*).
3. **Paso 3: Creación de Ámbitos (*Scopes*):** Configurar los *Scopes* en la interfaz de SecOps combinando las etiquetas pertinentes.
4. **Paso 4: Asignación a Grupos:** Vincular los *Scopes* como condiciones dentro de los roles de Google Cloud IAM asignados a los usuarios o grupos.

---

#### 6. Habilitación y Permisos Necesarios
* **Ruta de Acceso:** Ir a **Settings ➔ SIEM Settings ➔ Data Access**.
* **Activación:** Si la pestaña *Data Access* no está disponible, se debe solicitar su habilitación al representante comercial o técnico de Google SecOps.
* **Permiso Crítico de IAM:**
  * Para que la pestaña de *Scopes* esté activa (no en gris), el administrador de SecOps debe contar con el permiso:
    ```
    resourcemanager.projects.getIamPolicy
    ```
  * *Solución si está deshabilitado:* Crear un rol personalizado en GCP con dicho permiso y asignarlo a la identidad del administrador.

---

### Lección 12: Configuración de SIEM: Configuración de RBAC (SIEM) - Ámbitos y Etiquetas (*Configuring RBAC (SIEM) - Scopes & Labels*)

#### 1. Concepto de Ámbitos de Datos (*Data Access Scopes*)
Un **Ámbito (*Scope*)** es la política formal que define qué datos tiene permitido ver un usuario y qué datos tiene excluido ver dentro de Google SecOps.
* **Ubicación en Consola:** **Settings ➔ SIEM Settings ➔ Data Access ➔ Scopes**.
* **Criterios para Construir un Scope:** Se pueden combinar múltiples atributos:
  1. **Tipo de Log (*Log Type*):** Formato del log (ej. `OKTA`, `PAN_FIREWALL`).
  2. **Espacio de Nombres (*Namespace*):** Segmentación por red.
  3. **Etiquetas de Ingesta (*Ingestion Labels*):** Metadatos arbitrarios añadidos en feeds/BindPlane.
  4. **Etiquetas Personalizadas (*Custom Labels*):** Filtros avanzados generados mediante consultas UDM.

---

#### 2. Comportamiento y Reglas de los Scopes
* **Denegación por Defecto (*Default Deny*):** Un usuario sujeto a un scope comienza con **cero acceso a los datos**. Toda visibilidad debe ser otorgada explícitamente (*Allow*).
* **Lógica Combinada (Permitir y Excluir):** Un scope puede contener múltiples declaraciones. Permite conceder acceso a un conjunto amplio de datos y aplicar exclusiones precisas.
  * *Ejemplo:* Permitir el acceso a **todos los registros de Okta**, pero **excluir** aquellos registros que coincidan con un criterio confidencial específico.
* **Inmutabilidad del Nombre:**
  * La definición lógica del scope puede editarse en cualquier momento.
  * **El nombre del scope es estático y no se puede modificar una vez creado**. Incluso si se elimina, el nombre queda reservado para mantener la integridad con las políticas de Cloud IAM que lo referencian.
* **Prueba Segura (*Test Scope*):** Permite ejecutar búsquedas UDM de prueba simulando la perspectiva del usuario para validar con exactitud qué registros serán visibles y cuáles quedarán bloqueados antes de desplegarlo a producción.

---

#### 3. Etiquetas Personalizadas (*Custom Labels*)
Ubicadas en: **Settings ➔ SIEM Settings ➔ Data Access ➔ Custom Labels**.
* **Propósito:** Proporcionan granularidad extrema cuando las etiquetas estándar no son suficientes.
* **Construcción con Búsqueda UDM:**
  * Al crear una etiqueta personalizada, se abre la ventana de **UDM Search**.
  * El usuario redacta y prueba una consulta UDM que describa con precisión los datos objetivo (ej. eventos con determinadas acciones, IPs o usuarios).
  * La consulta guardada se convierte en la etiqueta personalizada.
* **Inyección en Tiempo de Ingesta:**
  * La etiqueta se evalúa e inyecta durante la ingesta de los logs en el campo UDM:
    ```
    metadata.base_labels.custom_labels
    ```
* **Reutilización:** Una vez creada, la etiqueta personalizada puede seleccionarse como criterio de inclusión o exclusión dentro de los *Scopes*.
* **Limitación Crítica (*No Retroactiva*):**
  * Las etiquetas personalizadas **solo se aplican a los datos nuevos que ingresan a partir de su creación**. No se etiquetan de forma retroactiva los registros históricos ya almacenados.

---

### Lección 13: Configuración de SIEM: Configuración de RBAC (SIEM) - Implementación y Gestión de Data RBAC (*Implementing & Managing Data RBAC*)

#### 1. Asignación de Roles de Cloud IAM para Data RBAC
Para aplicar la restricción de datos a un usuario o grupo sin otorgar acceso global, deben asignarse dos roles predefinidos clave en Cloud IAM:
1. **`Chronicle API Restricted Data Access`:**
   * Es el rol que **aplica y ejecuta las políticas de Data RBAC** definidas en SecOps.
2. **`Chronicle API Restricted Data Access Viewer`:**
   * Proporciona los permisos de lectura funcionales necesarios (ver búsquedas, detecciones y dashboards dentro de los límites de su ámbito).

> [!WARNING]
> **Regla de Oro contra Sobrescritura de Scopes:**  
> Ningún usuario o grupo restringido debe tener asignado roles de acceso global como `Chronicle API Admin`, `Editor`, `Viewer` o `Limited Viewer`. Estos roles globales **anulan y desactivan por completo el aislamiento de Data RBAC**, exponiendo todos los datos del *tenant*.

---

#### 2. Vinculación del Scope Mediante Condiciones de IAM (*IAM Conditions*)
Para atar el rol restringido con el ámbito exacto creado en SecOps:
1. En la consola de GCP ➔ **IAM & Admin**, editar la asignación del rol `Chronicle API Restricted Data Access`.
2. Hacer clic en **Add IAM Condition** (Añadir condición de IAM).
3. **Parámetros de la Condición:**
   * **Type (Tipo):** Seleccionar **`Name`**.
   * **Operator (Operador):** Seleccionar **`ends with`** (termina con).
   * **Value (Valor):** Escribir **`/nombre-del-scope`** *(es indispensable incluir la barra diagonal `/` al principio)*.
4. **Múltiples Scopes y Límites:**
   * Si el usuario requiere acceso a varios scopes, se agregan declaraciones encadenadas mediante el operador lógico **`OR`**.
   * Se admiten hasta **12 condiciones por cada vinculación de rol (*role binding*)**. Si se requieren más de 12 scopes, basta con añadir una segunda vinculación del mismo rol con hasta 12 condiciones adicionales.

---

#### 3. Verificación de Acceso en SecOps
Para comprobar que la política está activa y aislada:
1. En Google SecOps, navegar a **Settings ➔ SIEM Settings ➔ Profile**.
2. Revisar la sección **Scopes Assigned** (Ámbitos asignados):
   * Debe listar **únicamente** los scopes autorizados para esa identidad.
   * *Alerta:* Si aparece la leyenda **Global Scope**, significa que el usuario heredó permisos globales (por ejemplo, a través de la membresía en algún grupo secundario) y el aislamiento de datos no está funcionando.

---

#### 4. Ampliación Segura de Funcionalidades (Reglas YARA-L y Tablas de Datos)
Si un usuario acotado (*scoped user*) necesita realizar tareas avanzadas, como crear reglas de detección:
1. **Crear un Rol Personalizado de Funciones:**
   * Asignar permisos específicos de edición (ej. `custom_chronicle_rbac_rule_permissions` con permisos para crear, actualizar y validar texto de reglas).
   * **Evitar estrictamente permisos globales:** Nunca incluir `chronicle.dataAccessScopes.permit` o `chronicle.globalDataAccessScopes.permit`, ya que rompen la restricción de datos.
2. **Vinculación Obligatoria de Reglas a Scopes (*Bind to Scope*):**
   * Al redactar una regla de detección YARA-L en la interfaz de SecOps, el usuario acotado verá el menú obligatorio **Bind to Scope**.
   * La regla queda atada a su ámbito (ej. solo logs de Okta) y **únicamente evaluará y alertará sobre los eventos pertenecientes a ese scope**.
3. **Tablas de Datos (*Data Tables*):**
   * Las tablas de datos (sustitutas de las listas de referencia) también se rigen por Data RBAC. Los usuarios acotados solo pueden leer o escribir en aquellas tablas de datos asociadas a sus scopes autorizados.

---

### Lección 14: Configuración de SIEM: Normalización - Normalización Basada en Configuración (*Configuration-Based Normalization - CBN: Flujo, Estructura y Funciones*)

#### 1. Concepto de CBN y su Rol en la Ingesta
* **Normalización Basada en Configuración (CBN):** Es el proceso y la lógica mediante la cual los registros en bruto (*raw logs*) se analizan, extraen y transforman en el Modelo de Datos Unificado (**UDM**).
* En Google SecOps, los términos **CBN** y **Parser** se utilizan de forma intercambiable.
* **El nexo entre Ingesta y Parseo:** Toda fuente de datos debe tener asignada una **Etiqueta de Datos (`log_type`)**. Esta etiqueta identifica el tipo de tecnología e indica al motor de SecOps exactamente qué parser CBN debe ejecutarse para procesar los eventos. El valor queda plasmado en el campo `metadata.log_type`.

---

#### 2. Arquitectura y Estructura de un Parser CBN
A diferencia de Logstash tradicional (que requiere bloques `input`, `filter` y `output`), los parsers CBN de Google SecOps son más limpios y simplificados:
* **Bloque Único `filter { ... }`:** Toda la lógica de extracción, transformación y mapeo reside dentro de un único bloque contenedor.
* No se definen entradas ni salidas manuales; SecOps alimenta automáticamente el texto del log al filtro y recolecta el objeto UDM resultante.

---

#### 3. Las 3 Fases del Flujo de Parseo (*Parsing Flow*)

```
[ 1. Extracción de Datos ] ➔ [ 2. Manipulación de Datos ] ➔ [ 3. Asignación a UDM ]
 (Grok, JSON, KV, XML, CSV)   (Mutate: rename, replace,     (Mapeo a campos UDM y
                              convert, drop, condicionales)  generación del evento)
```

1. **Fase 1: Extracción de Datos (*Data Extraction*):**
   * Descompone la cadena de texto del log sin procesar en campos individuales utilizando el filtro apropiado según el formato:
     * `json`: Para logs estructurados en JSON.
     * `grok`: Para logs desestructurados o Syslog usando expresiones regulares y patrones.
     * `kv`: Para pares clave-valor (ej. `src=10.0.0.1 dst=10.0.0.2`).
     * `xml`, `csv`: Para formatos tabulares o XML.
     * `array`: *(Función propia de Google SecOps)* para iterar y manejar estructuras JSON anidadas.

2. **Fase 2: Manipulación y Limpieza de Datos (*Data Manipulation*):**
   * Limpia, formatea y transforma los valores extraídos antes de asignarlos al modelo:
     * `mutate { rename => ... }`: Renombra variables temporales a nombres finales.
     * `mutate { replace => ... }`: Sobrescribe o formatea cadenas.
     * `mutate { convert => ... }`: *(Mejora de SecOps)* Convierte tipos de datos (ej. string a entero o flotante).
     * `date`: Convierte cadenas de fecha/hora en marcas de tiempo estandarizadas en UTC (`ISO 8601`).
     * `base64`: *(Mejora de SecOps)* Decodifica cadenas codificadas en Base64.
     * `for`: Bucle iterativo sobre listas o arrays.
     * `drop`: Descarta eventos no deseados o de ruido operativo (ej. eventos informativos internos de depuración).
     * `state_dump`: Función exclusiva para desarrollo y *troubleshooting* que vuelca el estado interno de las variables durante la prueba del parser.

3. **Fase 3: Asignación a UDM (*Data Assignment*):**
   * Los valores procesados se asignan a las ramas oficiales de UDM:
     * Obligatorio: `metadata.event_type` (ej. `NETWORK_CONNECTION`, `USER_LOGIN`).
     * Actores: `principal.ip`, `target.ip`, `target.port`, `target.user.userid`.
     * Resultados: `security_result.action` (ej. `ALLOW`, `BLOCK`).
   * La salida se fusiona en el objeto final del evento y se envía indexada a SecOps.

---

### Lección 15: Configuración de SIEM: Normalización - Extracción de Datos: Formateados y Grok (*Data Extraction - Formatted & Grok*)

#### 1. Propósito de la Fase de Extracción
Es el primer paso activo dentro del bloque `filter { ... }`. Consiste en analizar el mensaje del registro crudo (`message`) y descomponerlo en campos y variables intermedias antes de proceder a su manipulación y asignación a UDM.

---

#### 2. Los 5 Métodos de Extracción de Datos

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      Métodos de Extracción de Datos                         │
├───────────────────────────────────┬─────────────────────────────────────────┤
│ 1. json                           │ Registros estructurados en JSON         │
│ 2. xml                            │ Registros formateados en XML            │
│ 3. kv                             │ Pares clave-valor (Key-Value)           │
│ 4. csv                            │ Valores separados por comas sin claves  │
│ 5. grok                           │ Texto desestructurado (Patrones / Regex)│
└───────────────────────────────────┴─────────────────────────────────────────┘
```

##### 1. Filtro `json` (Datos Estructurados y Arrays Anidados)
* Extrae directamente las claves raíz del objeto JSON.
* **Manejo de Arrays Anidados con `array`:**
  * Si el log contiene un array anidado (ej. `ips: ["1.1.1.1", "2.2.2.2"]`), se utiliza la función `array` con el parámetro `split_columns`.
  * Esto aplana el array en campos indexados accesibles (`ips.0`, `ips.1`, etc.), permitiendo mapear cada elemento de manera individual.

##### 2. Filtro `xml` (Rutas XPath y Bucles)
* Extrae valores de logs XML definiendo rutas **XPath**.
* **Valores simples:** Mapea elementos específicos (ej. `/event/serial_number`) a variables de destino.
* **Colecciones repetidas / Arrays XML:** Se combina con un bucle `for` para iterar sobre nodos repetitivos (ej. listas de dispositivos), aplanando el resultado en campos indexados (`models.0`, `models.1`).

##### 3. Filtro `kv` (Pares Clave-Valor)
* Ideal para logs donde los datos vienen en secuencias como `key:value` o `key=value` con delimitadores fijos.
* **Parámetros Esenciales:**
  * **`field_split`:** Define el carácter que separa cada par (ej. `|` o espacio).
  * **`value_split`:** Define el carácter que separa la clave de su valor (ej. `:` o `=`).
  * *Ejemplo:* Si el log contiene `|timestamp:2026-01-01|devId:45|`, el parser genera automáticamente las variables `timestamp` y `devId`.

##### 4. Filtro `csv` (Datos Tabulares Delimitados)
* Procesa líneas con valores separados por comas u otros delimitadores sin nombres de clave explícitos.
* **Comportamiento:** Asigna nombres genéricos por posición: `column1`, `column2`, `column3`, etc.
* **Paso siguiente obligado:** Se utiliza un bloque `mutate { rename => ... }` para renombrar `column1` a `user`, `column2` a `email`, etc.

---

#### 3. Filtro `grok` (Registros Desestructurados y Syslog)
Grok es el método por excelencia para procesar texto libre o registros donde los campos no tienen formato rígido. Admite dos enfoques:

##### Enfoque A: Patrones Preconstruidos (*Pre-built Grok Patterns*)
* Utiliza identificadores predefinidos y reutilizables mediante la sintaxis:
  ```
  %{PATRON:nombre_variable}
  ```
* *Ejemplos comunes:*
  * `%{IP:source_ip}` ➔ Coincide con una dirección IPv4 o IPv6.
  * `%{WORD:method}` ➔ Coincide con una palabra (ej. método HTTP: GET, POST).
  * `%{NUMBER:bytes}` ➔ Coincide con valores numéricos.

##### Enfoque B: Expresiones Regulares Personalizadas (*Custom Regex con RE2 / Golang*)
* Otorga control quirúrgico cuando no existe un patrón preconstruido.
* **Sintaxis Nombrada en RE2 (Golang):**
  * Requiere anteponer una `P` entre el signo de interrogación y el nombre del token:
    ```
    (?P<token_name>patron_regex)
    ```
  * *Escape de caracteres:* En Golang regex, las barras invertidas para clases de caracteres deben escaparse doblemente (ej. `\\d+`, `\\s+`).
* **Ejemplos prácticos:**
  * Dirección MAC: `(?P<mac_address>[0-9A-Fa-f:]{17})`
  * Protocolo alternativo: `(?P<protocol>TCP|UDP)`

---

#### 4. Ejercicio de Extracción HTTP con Grok
* **Log en Bruto:**
  ```text
  192.168.1.50 GET /api/v1/login 1420 0.045
  ```
* **Patrón Grok de Extracción:**
  ```text
  %{IP:client_ip} %{WORD:http_method} %{URIPATH:request_path} %{NUMBER:bytes_sent} %{NUMBER:duration}
  ```
  Permite aislar limpiamente la IP cliente, el verbo HTTP, la ruta solicitada, los bytes y la duración para prepararlos para la siguiente fase de manipulación.

---

### Lección 16: Configuración de SIEM: Normalización - Manipulación y Asignación de Datos (*Data Manipulation*)

#### 1. Sintaxis de Referencia a Variables y Tokens
Uno de los puntos clave al redactar parsers CBN es diferenciar cómo se hace referencia a los valores:

| Sintaxis | Propósito | Ejemplo de Uso |
| :--- | :--- | :--- |
| **`[nombre_token]`** (Corchetes) | Acceso directo al token (en condiciones lógicas o asignaciones). | `if [status] == "SUCCESS"` |
| **`%{nombre_token}`** (Porcentaje y llaves) | Inserción o interpolación de la variable dentro de una cadena de texto. | `replace => { "desc" => "Alerta: %{user}" }` |
| **`"texto_literal"`** (Comillas dobles) | Valor constante literal (no hace referencia a variables). | `replace => { "proto" => "TCP" }` |

* **Prefijos UDM Oficiales:**
  * Telemetría de Eventos: `event.idm.read_only_udm` (o el objeto `event`).
  * Telemetría de Contexto / Grafo: `event.idm.graph`.

---

#### 2. Funciones Clave del Plugin `mutate`

* **`convert` (Conversión de Tipos de Datos):**
  * Transforma strings en enteros, booleanos o flotantes exigidos por el esquema UDM.
  * *Ejemplo:* Transformar `"56"` (texto) a `56` (entero para `network.sent_bytes`).
* **`gsub` (Reemplazo por Expresión Regular):**
  * Reemplaza todas las apariciones de un patrón regex en una cadena por un nuevo valor.
  * *Ejemplo:* Limpiar caracteres extraños sustituyendo espacios o guiones por guiones bajos.
* **`rename` (Renombrado y Asignación Directa):**
  * Asigna el valor de un token temporal a un campo UDM y elimina el token original.
  * **Uso indispensable:** Funciona tanto para números como cadenas (ideal para puertos y bytes).
* **`replace` (Asignación Exclusiva de Cadenas):**
  * **Regla estricta:** `replace` **solo funciona sobre campos de tipo string**.
  * Se usa comúnmente para inicializar variables vacías o fijar enumerados estáticos (ej. `"TCP"`).
* **`merge` (Campos Repetidos y Arrays en UDM):**
  * Obligatorio para poblar campos repetidos (*arrays*) en UDM.
  * Si el campo es un array simple (ej. `target.ip`), se hace `merge` directo.
  * Si se trata de un objeto complejo repetido (ej. `security_result`), primero se construyen sus campos internos (`action`, `description`) y luego se hace `merge` sobre la rama padre `security_result`.

---

#### 3. Funciones de Flujo, Control y Limpieza

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   Funciones de Control y Robustez en CBN                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ • if / else if / else ➔ Lógica condicional (==, !=, >, <, =~ regex, !~).    │
│ • on_error            ➔ Captura de fallos en filtros para crear fallback.   │
│ • drop                ➔ Descarta logs corruptos o de ruido operativo.       │
│ • date                ➔ Normaliza timestamps a formato UTC ISO 8601.        │
│ • state_dump          ➔ Imprime variables en desarrollo (solo debug).       │
│ • for                 ➔ Iteración sobre listas y arrays.                    │
│ • base64              ➔ Decodificación de cargas útiles codificadas.         │
└─────────────────────────────────────────────────────────────────────────────┘
```

* **Lógica Condicional (`if` / `else`):**
  * Permite clasificar acciones de seguridad: si el evento dice `deny`, `drop` o `block`, se asigna `security_result.action = "BLOCK"`; si dice `allow`, se asigna `"ALLOW"`.
* **Manejo de Errores con `on_error`:**
  * Permite añadir la propiedad `on_error => "label_name"` a un filtro. Si falla (ej. Grok no pudo parsear una IP), se activa la etiqueta de fallo y un bloque `if` desvía el valor hacia el campo `hostname`, evitando que el log quede sin parsear.
* **Depuración con `state_dump`:**
  * Vuelca en pantalla el estado exacto de todas las variables durante las pruebas. *(Solo funciona en entorno de prueba/desarrollo, se ignora en producción)*.
* **Normalización de Fechas con `date`:**
  * **Componente obligatorio:** Mapea marcas de tiempo crudas a `metadata.event_timestamp` en formato UTC ISO 8601 con soporte de zonas horarias (`timezone`).

---

#### 4. Ejercicio Completo de Mapeo a UDM (Resolución)
Tomando los campos extraídos en la lección anterior:
1. `client_ip` ➔ Se asigna mediante **`merge`** a `principal.ip` (porque `principal.ip` es un campo repetido).
2. `bytes_sent` ➔ Se transforma con **`convert`** a entero sin signo (`uinteger`). Si falla, se atrapa con `on_error` hacia `no_bytes_sent`. Si tiene éxito, se asigna con **`rename`** a `network.sent_bytes` (ya que `replace` no admite números).
3. `http_method` ➔ Se asigna con **`replace`** a `network.http.method` (válido al ser una cadena).

---

### Lección 17: Configuración de SIEM: Normalización - Revisión de Parser Completo (*Completed Parser Review*)

#### 1. Propósito y Valor del Proceso de Revisión
Asegurar que los registros se procesen, normalicen y validen exhaustivamente antes de pasar a producción.
* **Beneficios directos:** Datos fiables para el motor de detección y SOAR, reducción drástica de falsos positivos, campos UDM uniformes y prevención de pérdida involuntaria de datos.
* **Pilares de revisión:** Manejo de errores, auditoría de descartes (*drops*), validación del esquema UDM, tasa de normalización y casos especiales.

---

#### 2. Gestión de Errores y Uso Responsable del Filtro `drop`
* **Etiquetado de Descartes (*Tagged Drops*):**
  * Si un registro está completamente corrupto o no contiene valor de seguridad, se descarta mediante el filtro `drop` asociando una etiqueta para que quede registrado en las métricas de ingesta.
  * **Etiquetas comunes recomendadas:**
    * `TAG_UNSUPPORTED` (Formato de log no soportado).
    * `TAG_MALFORMED_ENCODING` (Codificación corrupta).
    * `TAG_MALFORMED_MESSAGE` (Mensaje roto o incompleto).
    * `TAG_NO_SECURITY_VALUE` (Sin valor analítico para seguridad).
* **Auditoría de Drops Innecesarios:**
  * Buscar en el código del parser todas las apariciones de `drop {`.
  * **Mejor Práctica:** Si los datos son imperfectos pero aún aprovechables (ej. un espacio en blanco adicional que rompió un patrón Grok estricto), **NO descartar el log**.
  * En su lugar, asignar una clasificación de contingencia como:
    ```
    metadata.event_type = "GENERIC_EVENT"
    ```
  * Esto permite que el evento permanezca indexado en SecOps y disponible para búsquedas e investigaciones.

---

#### 3. Errores de Validación de UDM (*UDM Validation Errors*)
Ocurren cuando el parser se ejecuta sintácticamente bien pero el evento resultante no cumple con los requisitos obligatorios del esquema UDM (ej. `UDM validation failed: target field is not set`).
* **Causa común:** El tipo de evento exige ciertos campos obligatorios (ej. un evento `USER_LOGIN` requiere obligatoriamente `target.user`, o una conexión de red requiere un destino).
* **Metodología de Corrección:**
  1. Durante pruebas, establecer valores estáticos para aislar el campo faltante.
  2. Ajustar la lógica de extracción para capturar el valor real desde el log crudo.
  3. **Advertencia crítica:** Los valores estáticos son **únicamente para depuración local**; nunca deben enviarse a producción ya que falsean los datos reales de la organización.

---

#### 4. Ratio de Normalización (*Normalization Ratio*)
Es la métrica de calidad que mide el porcentaje de logs parseados y mapeados exitosamente a UDM respecto al total de logs recibidos.
* **Objetivo de Oro:** Mantener una tasa de normalización de **99.99% o superior**.
  $$\text{Normalization Ratio} = \left( \frac{\text{Logs Normalizados Exitosamente}}{\text{Total de Logs Ingeridos}} \right) \times 100$$
* *Ejemplo:* De 100,000 logs, un máximo de 10 pueden quedar sin normalizar para alcanzar el 99.99%.
* Una caída en este ratio indica pérdida de visibilidad, debilitando las reglas de detección y los informes forenses.
* *Nota:* En fuentes de muy bajo volumen de eventos, pequeñas fluctuaciones pueden causar caídas porcentuales temporales no críticas.

---

#### 5. Errores Comunes de Código y Casos Especiales

##### A. Grupos de Captura Nombrados Obligatorios en Regex
* En el motor de expresiones regulares de SecOps (RE2), expresiones genéricas como `.*$` fallan dentro del parser.
* **Regla estricta:** Todo regex personalizado debe incluir un **grupo de captura nombrado**:
  * ❌ *Incorrecto:* `.*$`
  * ⭕ *Correcto:* `(?P<token_catchall>.*)$`
  * Si falta el nombre de captura, SecOps arrojará: `Filter grok failed to parse data with all match patterns`.

##### B. Estandarización de Identidades y Nombres de Usuario
* Los campos de usuarios y correos electrónicos son fundamentales para el motor de vinculación (*aliasing*) y correlación de SecOps.
* Deben mapearse de manera consistente y uniforme en todos los parsers:
  * `user.userid` (Nombre de usuario).
  * `user.email_addresses` (Dirección de correo).
  * `user.employee_id` (Identificador de empleado).
  * `product_object_id` (Identificador interno del producto).

---

### Lección 18: Configuración de SIEM: Normalización - Gestión de Parsers y Tipos de Parsers (*Parser Management & Types of Parsers*)

#### 1. Métodos de Gestión: Interfaz Visual (UI) vs. Línea de Comandos (`chronicle_cli`)
Para administrar el ciclo de vida de los analizadores, Google SecOps ofrece dos vías:
* **Consola Visual (*Parser Management UI*):**
  * Ubicación: **Settings ➔ SIEM Settings ➔ Parsers**.
  * Ofrece validación integrada paso a paso, visualización de métricas de normalización y comparativa visual de código. Recomendada para la mayoría de entornos corporativos y operaciones diarias.
* **Línea de Comandos (*Chronicle CLI*):**
  * Herramienta avanzada que sustituye a la antigua utilidad CBN CLI.
  * Permite generar conjuntos de prueba de logs (con 1, 10 o 1,000 líneas para testing rápido), validar sintaxis y activar parsers mediante scripts programáticos e integración en pipelines de CI/CD (GitOps).

---

#### 2. Los 3 Tipos de Parsers en Google SecOps

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       Tipos de Parsers en Google SecOps                     │
├──────────────────────┬───────────────────────────────┬──────────────────────┤
│ 1. Preconstruidos    │ 2. Extensiones de Parser      │ 3. Personalizados    │
│    (Pre-built)       │    (Parser Extensions)        │    (Custom Parsers)  │
├──────────────────────┼───────────────────────────────┼──────────────────────┤
│ • Creados por Google │ • Capa complementaria cliente │ • Creados 100% por el│
│ • Mantenidos y actual│ • Añade campos a UDM          │   cliente desde cero │
│   izados en la nube  │ • Mantiene updates de Google  │ • No recibe updates  │
└──────────────────────┴───────────────────────────────┴──────────────────────┘
```

1. **Parsers Preconstruidos / Por Defecto (*Pre-built / Default Parsers*):**
   * Desarrollados y mantenidos oficialmente por el equipo de ingeniería de Google SecOps.
   * Contienen la lógica estándar para transformar la telemetría del fabricante a UDM.
2. **Extensiones de Parser (*Parser Extensions*):**
   * Bloques de lógica creados por el cliente que operan **por encima del parser por defecto**.
   * *Entrada:* El evento UDM ya normalizado por Google.  
   * *Salida:* El mismo evento UDM enriquecido con campos adicionales o etiquetas específicas del cliente.
   * **Ventaja competitiva:** Permiten añadir personalizaciones sin perder las actualizaciones continuas que Google publica sobre el parser base.
3. **Parsers Personalizados (*Custom Parsers*):**
   * Desarrollados íntegramente por el cliente para fuentes propietarias o cuando no existe un parser oficial de Google.
   * **Advertencia:** Quedan fuera del ciclo de mantenimiento automático de Google.

---

#### 3. Ciclo de Actualizaciones de Parsers Preconstruidos (*Pending State & Opt-out*)
Cuando Google mejora o corrige un parser por defecto, los cambios no se aplican a ciegas:
* **Período de Revisión de 15 Días (*Pending State*):** La actualización entra en estado pendiente durante 15 días, permitiendo:
  * Comparar el código antiguo y nuevo lado a lado (*Diff view*).
  * Inspeccionar el historial de versiones.
* **Opciones del Administrador:**
  * **Opt-in Anticipado:** Aplicar y activar la actualización inmediatamente.
  * **Opt-out (Desactivar actualización):** Si el cambio de Google colisiona con la telemetría local, el administrador puede rechazarlo. Al hacer esto, **el parser se convierte automáticamente en un Custom Parser**, deteniendo de forma definitiva las actualizaciones automáticas de Google para esa fuente.

---

#### 4. Creación de Extensiones de Parser: Métodos y Limitaciones

##### Métodos de Creación:
* **Interfaz de Mapeo de Campos (*Field Mapping UI*):** Interfaz gráfica intuitiva sin código (*no-code*), ideal para mapear campos simples desde logs estructurados (JSON/XML), añadir condiciones y elegir entre anexar (*append*) o reemplazar (*replace*).
* **Editor de Código (*Code Editor*):** Editor completo con sintaxis CBN. Indispensable para transformaciones complejas, datos desestructurados, regex avanzado o estructuras anidadas profundas.

##### Limitaciones de las Extensiones de Parser:
* **Solo una extensión por tipo de log:** No se admiten múltiples extensiones para un mismo `log_type`.
* **Requiere datos recientes (últimos 30 días):** Para validar la extensión en la consola se requiere telemetría real reciente en el *tenant*.
* **Campos Repetidos:** Al modificar un array/campo repetido en una extensión, el nuevo valor **sobrescribe** el array completo; no lo anexa.
* **No Retroactivo:** Solo aplica hacia adelante. Para normalización histórica de logs antiguos se debe contactar a soporte de Google.

---

#### 5. Validación de Parsers (*Parser Validation Rules*)
Fase de control de calidad obligatoria antes de activar cualquier cambio:
* **Volumen menor a 10,000 líneas de log:** Exige una precisión del **100% de éxito** para poder publicarse.
* **Volumen mayor a 10,000 líneas de log:** Tolera un margen mínimo de fallos sin bloquear la activación, permitiendo identificar las líneas puntuales que fallaron para su afinamiento continuo.

---

### Lección 19: Configuración de SIEM: Normalización - Demostración Práctica de Extensiones de Parsers (*Parser Extension Demo*)

#### 1. Planteamiento del Caso de Uso Real
* **Escenario:** Un registro de consultas DNS (*DNS Query Log*) se procesa con el parser por defecto de Google.
* **Situación:** Campos como la IP origen, nombre de consulta y protocolo quedan correctamente normalizados en UDM. Sin embargo, el campo de red origen (`source_network`) se almacena por defecto dentro del objeto genérico `additional.fields`.
* **Objetivo de la Extensión:** Elevar el valor de `source_network` para mapearlo directamente en el campo estructurado de contexto:
  ```
  principal.asset.attribute.cloud.vpc_name
  ```
  Esto optimiza la correlación de red, búsquedas forenses y reglas de detección que evalúan el nombre de la VPC en la nube.

---

#### 2. Método 1: Enfoque Sin Código (*No-Code Field Mapping UI*)
Recomendado cuando el log origen es estructurado (JSON, XML, CSV) y se requiere un mapeo directo campo a campo.
1. En la lista de parsers, abrir el menú contextual del parser y seleccionar **Create Parser Extension**.
2. En *Extension Method*, elegir **Map Data Fields**.
3. **Raw Data Field (Campo en bruto):** Introducir la ruta del campo en el payload del log (ej. `jsonPayload.source_network`).
4. **UDM Field (Campo de destino):** Seleccionar del desplegable:
   `principal.asset.attribute.cloud.vpc_name`.
5. *(Opcional)* Añadir condiciones previas (*preconditions*) si solo debe aplicar bajo ciertas circunstancias.
6. Hacer clic en **Preview UDM Output** para validar que el valor se inyecta en el campo deseado.

---

#### 3. Método 2: Enfoque con Código (*CBN Code Editor*)
Recomendado para transformaciones complejas, logs desestructurados o cuando se requieren filtros avanzados.

##### A. Construcción Inicial del Código CBN
```ruby
filter {
  # 1. Tratamiento del payload como JSON con manejo de arrays
  json {
    source => "message"
    array => {
      split_columns => true
    }
  }

  # 2. Asignación del campo mediante replace
  mutate {
    replace => {
      "principal.asset.attribute.cloud.vpc_name" => "%{source_network}"
    }
  }

  # 3. Fusión en el evento UDM final
  merge {
    source => "event"
    target => "output"
  }
}
```

##### B. Depuración Práctica de un Error con `state_dump`
* **Error obtenido al probar:** `source_network field not set`.
* **Técnica de Solución:** Se inserta el filtro temporal de depuración:
  ```ruby
  state_dump {}
  ```
* **Diagnóstico del Volcado:** Al inspeccionar el volcado interno de variables generado por `state_dump`, se descubre que la variable no se llama `source_network` a secas, sino que está anidada como `jsonPayload.source_network`.
* **Ajuste y Corrección:** Se actualiza la referencia en el bloque `replace`:
  ```ruby
  mutate {
    replace => {
      "principal.asset.attribute.cloud.vpc_name" => "%{jsonPayload.source_network}"
    }
  }
  ```
* **Resultado:** La validación pasa con éxito. El nombre de la VPC queda poblado en `principal.asset.attribute.cloud.vpc_name`, mientras que el parser por defecto sigue preservando el valor original en `additional.fields` sin perder compatibilidad ni actualizaciones futuras de Google.

---

### Lección 20: Comprobación de Conocimientos de Configuración de SIEM (*SIEM Setup: Knowledge Check*)

> **Nota de aprobación requerida:** 80%  
> **Temas evaluados:** Ingesta de almacenamiento cloud, roles IAM para feeds, rol de normalización UDM, BindPlane, Streaming vs Buckets, extensiones de parsers, arquitectura BindPlane, Feature RBAC vs Legacy, e Ingesta Directa.

---

#### Preguntas y Respuestas Técnicas Desarrolladas

#### 1. ¿Qué servicios de almacenamiento en la nube son compatibles para la recolección e ingesta de datos en Google SecOps? (*Which cloud storage services are supported for data collection and ingestion in Google SecOps?*)

* [ ] Cloud SQL, BigQuery, and Firebase Storage
* [x] **Google Cloud Storage, Amazon S3, and Microsoft Azure Blob**
* [ ] Snowflake, Redshift, and Cloud Spanner
* [ ] Google Drive, Dropbox, and OneDrive

> **Explicación técnica:** Google SecOps soporta de forma nativa la recolección e ingesta automatizada de telemetría y registros almacenados en los tres principales proveedores cloud: **Google Cloud Storage (GCS)**, **Amazon S3** (vía SQS v2 o SNS/SQS) y **Microsoft Azure Blob Storage**. Los demás servicios listados corresponden a bases de datos relacionales/data warehouses o almacenamiento colaborativo de archivos personales.

---

#### 2. ¿Qué rol de IAM en Google Cloud incluye los permisos requeridos para gestionar feeds de APIs de terceros? (*Which IAM role in Google Cloud includes the permissions required to manage 3rd Party API feeds?*)

* [ ] Log Analytics Viewer
* [x] **Chronicle API Admin**
* [ ] Chronicle Feed Operator
* [ ] Security Admin

> **Explicación técnica:** El rol predefinido **`roles/chronicle.admin` (Chronicle API Admin)** proporciona control administrativo integral sobre los recursos de Chronicle/SecOps, incluyendo la capacidad de crear, autenticar, listar, modificar y eliminar feeds de ingestión de APIs de terceros (*3rd Party API Feeds*). Roles como *Viewer* solo otorgan lectura y *Feed Operator* no es el rol predefinido de IAM para la gestión integral de feeds.

---

#### 3. ¿Qué papel desempeña la normalización en el pipeline de datos de Google SecOps? (*What role does normalization play in the Google SecOps data pipeline?*)

* [x] **Mapea los registros en bruto ingeridos al modelo UDM utilizando parsers que identifican el tipo de registro mediante Etiquetas de Datos (Data Labels)** (*It maps ingested raw logs to the UDM model using parsers that identify the log type through Data Labels*)
* [ ] Comprime los datos de registro en bruto para optimizar los costos de almacenamiento.
* [ ] Encripta la telemetría en reposo y en tránsito dentro de la nube.
* [ ] Filtra y descarta automáticamente registros duplicados antes de la indexación.

> **Explicación técnica:** La normalización es la fase del pipeline donde los registros sin estructurar (*raw logs*) se transforman en eventos de seguridad estructurados dentro del modelo unificado **UDM** (*Unified Data Model*). Esto se logra mediante parsers configurados (*CBN*), los cuales se seleccionan y aplican según la etiqueta de datos (**Data Label** o `log_type`) asignada a la fuente durante la ingesta.

---

#### 4. ¿Cuál es el uso principal de BindPlane en la arquitectura de ingesta? (*What is the primary use of BindPlane?*)

* [ ] Generar alertas de seguridad y detección de anomalías en endpoints.
* [x] **Reenviar y gestionar la recolección de datos de registros a través de múltiples orígenes** (*Forwarding and managing log data collection across sources*)
* [ ] Ejecutar consultas YARA-L directamente sobre servidores locales.
* [ ] Crear respaldos periódicos de la base de datos de Google SecOps.

> **Explicación técnica:** **BindPlane** (desarrollado por observIQ y adoptado por Google SecOps) es la solución para la recolección y gestión de telemetría local (*on-premises*) y multi-cloud. Su función primaria es desplegar agentes/recolectores, configurar pipelines de recolección y reenviar de manera centralizada y segura los registros hacia Google SecOps.

---

#### 5. ¿Cuál es la diferencia clave entre la transferencia por Streaming y la ingesta por Cloud Storage Buckets? (*What is the difference between Streaming Transfer and Cloud Storage Bucket Ingestion?*)

* [ ] Los buckets de almacenamiento tienen menor latencia que las colas de streaming.
* [x] **El streaming empuja datos a SecOps en tiempo real, reduciendo la latencia y mejorando el rendimiento (*throughput*)** (*Streaming pushes data to SecOps in real time, reducing latency and improving throughput*)
* [ ] El streaming solo soporta registros de Microsoft Windows Event Logs.
* [ ] La ingesta por buckets no admite compresión gzip.

> **Explicación técnica:** Los servicios de streaming (como Google Cloud Pub/Sub, AWS SQS/Kinesis o Kafka) utilizan un modelo basado en eventos o *push* continuo que entrega los registros a SecOps en cuestión de milisegundos a segundos. En cambio, los Cloud Storage Buckets operan típicamente mediante sondeo periódico por lotes (*polling/batch*), lo que añade latencia de recolección en comparación con streaming.

---

#### 6. ¿Qué describe con precisión a las Extensiones de Parsers (*Parser Extensions*)? (*What is an accurate description of Parser Extensions?*)

* [ ] Son scripts de Python externos ejecutados en máquinas virtuales independientes.
* [x] **Son lógica creada por el cliente que extrae datos adicionales hacia UDM mientras sigue recibiendo actualizaciones del parser por defecto** (*They are customer-created logic that extract additional data into UDM while still receiving updates from the default parser*)
* [ ] Son reglas de detección diseñadas para reemplazar reglas YARA-L defectuosas.
* [ ] Son configuraciones que sobrescriben por completo y eliminan el parser predefinido de Google.

> **Explicación técnica:** Una **Extensión de Parser** permite a las organizaciones personalizar el enriquecimiento o extracción de campos específicos (por ejemplo, extraer un ID interno o mover un dato no contemplado a un campo UDM específico) encima del parser por defecto de Google. La gran ventaja frente a un parser personalizado (*custom parser*) es que el cliente mantiene la compatibilidad y sigue recibiendo las mejoras y actualizaciones automáticas del parser base oficial.

---

#### 7. ¿Cuál es una descripción precisa del Collector y el Server de BindPlane? (*Which is an accurate description of the BindPlane Collector and Server?*)

* [ ] El Server recopila registros locales y el Collector los almacena en discos duros locales.
* [x] **El BindPlane Collector reenvía registros, mientras que el BindPlane Server administra los agentes y centraliza la recolección** (*The BindPlane Collector forwards logs, while the BindPlane Server manages agents and centralizes collection*)
* [ ] El Collector gestiona los roles de IAM y el Server aplica parsers CBN.
* [ ] Ambos componentes cumplen la misma función y se eligen indistintamente.

> **Explicación técnica:** En la arquitectura de BindPlane, el **Collector (Agent)** es el componente ligero instalado en los endpoints, servidores o puertas de enlace de red que extrae y reenvía telemetría. El **Server (Master/Control Plane)** es el plano de control que centraliza la administración remota, actualización de configuraciones, monitoreo del estado de salud de los agentes y orquestación del flujo.

---

#### 8. ¿Cómo mejora el Feature RBAC respecto al RBAC Heredado (*Legacy RBAC*)? (*How does Feature RBAC improve upon Legacy RBAC?*)

* [ ] Elimina la necesidad de credenciales de Google Workspace.
* [x] **Se integra con Cloud IAM, admite roles personalizados y habilita el registro de auditoría de actividad administrativa** (*It integrates with Cloud IAM, supports custom roles, and enables admin activity audit logging*)
* [ ] Restringe el acceso a la plataforma únicamente mediante direcciones IP fijas.
* [ ] Aplica políticas basadas únicamente en etiquetas UDM sin intervención de IAM.

> **Explicación técnica:** El nuevo **Feature RBAC** traslada el control de acceso desde la consola interna aislada de SecOps hacia **Google Cloud IAM estándar**. Esto habilita:
> 1. Gestión centralizada de identidades y grupos de Google Workspace/Cloud Identity.
> 2. Creación de roles personalizados con granularidad fina de permisos (`chronicle.*`).
> 3. Trazabilidad y auditoría completa de acciones mediante **Cloud Audit Logs**.

---

#### 9. ¿Cuál es una ventaja clave de la Ingesta Directa (*Direct Ingestion*)? (*What is an advantage of Direct Ingestion?*)

* [ ] Requiere instalar agentes pesados en cada instancia de Compute Engine.
* [x] **Permite el procesamiento inmediato de registros directamente desde GCP, reduciendo la latencia y la complejidad de configuración** (*It enables immediate processing of logs directly from GCP, reducing latency and setup complexity*)
* [ ] Solo se puede configurar mediante llamadas REST manuales y no admite auditoría.
* [ ] Convierte automáticamente todos los registros a texto plano sin etiquetado UDM.

> **Explicación técnica:** La **Ingesta Directa (GCP Direct Ingestion / Cloud Logging Export to SecOps)** permite enrutar telemetría desde Google Cloud Logging directamente a la instancia de SecOps con un simple checkbox o filtro de exportación. No requiere servidores intermediarios, agentes de reenvío ni credenciales complejas de APIs de terceros, ofreciendo la menor latencia y la configuración más simple posible en entornos GCP.

---

## Módulo 3: SIEM Investigation (Investigación en SIEM)

### Lección 1: Búsqueda de Registros en Bruto (*Raw Log Search - RLS*)

> **Objetivo:** Comprender qué es la búsqueda de registros en bruto, cuándo utilizarla frente a UDM Search, sus casos de uso específicos, su sintaxis (coincidencia de cadena y expresiones regulares RE2), y las diferencias operativas entre la interfaz heredada (*legacy*) y la nueva interfaz de búsqueda unificada en Google SecOps SIEM.

---

#### 1. Introducción y Propósito de Raw Log Search (RLS)

En Google SecOps SIEM, los datos ingeridos se almacenan en dos capas persistentes:
1. **El Registro Original en Bruto (*Raw Log*):** Texto exacto tal como fue recibido desde la fuente (Syslog, JSON, CEF, XML, etc.).
2. **El Evento Normalizado UDM (*Parsed UDM Event*):** Estructura normalizada y enriquecida generada por el pipeline de parsers CBN.

**Raw Log Search (RLS)** es el método para consultar directamente los registros en bruto no estructurados sin depender del esquema UDM.

> [!IMPORTANT]
> **Rendimiento y Propósito:**  
> *Raw Log Search* **no está diseñado para consultas de alto rendimiento ni para investigaciones forenses masivas rutinarias**. Su función principal es la exploración no estructurada, diagnóstico de ingesta y resolución de problemas de parsing. Para investigaciones avanzadas, correlaciones y reglas de detección, siempre se debe utilizar **UDM Search**.

---

#### 2. Casos de Uso Clave para Raw Log Search

* **Validación de la Ingesta de Datos (*Data Ingestion Validation*):** Confirmar en tiempo real que los registros están llegando a la plataforma desde una fuente recién configurada (feeds, storage buckets o BindPlane).
* **Exploración Básica de Nuevas Fuentes (*Data Exploration*):** Inspeccionar visualmente la estructura, cabeceras y formato de eventos de fuentes desconocidas o recién incorporadas.
* **Verificación y Solución de Problemas de Parsers (*Parser Troubleshooting*):** Comparar directamente el registro original recibido contra los campos mapeados en UDM para detectar discrepancias, campos no mapeados en `additional.fields` o errores de extracción.

---

#### 3. Métodos y Sintaxis de Búsqueda en Raw Log Search

Se admiten dos modalidades de consulta:

| Modalidad | Sintaxis | Descripción y Ejemplo |
| :--- | :--- | :--- |
| **Coincidencia Exacta de Cadena (*Exact String*)** | `raw = "cadena"` | Busca coincidencias literales de texto dentro del registro crudo. Ej: `raw = "failed login"` |
| **Expresiones Regulares (*RE2 Regex*)** | `raw = /expresión/` | Utiliza la biblioteca de expresiones regulares seguras de Google (**RE2**). La expresión se encierra entre barras inclinadas (`/ /`). |

* **Patrón Comodín Universal:** El patrón `.*` (o simplemente `.` en la interfaz anterior) indica que se devuelvan todos los registros disponibles de una fuente dentro del rango temporal seleccionado. Es ideal para verificar flujo de datos.
* **Sensibilidad a Mayúsculas y Minúsculas (*Case Sensitivity*):** En la nueva interfaz se dispone de un interruptor (*toggle*) para activar o desactivar la distinción entre mayúsculas y minúsculas en cadenas literales.
* **Selector de Fuentes de Datos (*Log Sources Dropdown*):** Al escribir `raw =`, la barra de búsqueda despliega automáticamente una lista de tipos de fuentes (`log_type`), agregando la sintaxis necesaria a la consulta sin necesidad de recordarla de memoria.

---

#### 4. Comparativa de Interfaces: Legacy UI vs. Nueva Interfaz Unificada

Google SecOps permite ejecutar búsquedas de registros en bruto tanto en la interfaz de búsqueda unificada como en la clásica (*Legacy Search* accesible desde **Investigation > SIEM Search > Go to legacy search**).

| Característica | Interfaz Heredada (*Legacy Search*) | Nueva Interfaz Unificada (*Unified SIEM Search*) |
| :--- | :--- | :--- |
| **Límite de Resultados** | Primeros **10,000 registros** coincidentes. | Primeros **10,000 registros** coincidentes. |
| **Organización de Resultados** | Orden cronológico (antiguo a reciente) en panel izquierdo. | Orden **cronológico inverso** (más reciente arriba) en la parte inferior derecha. |
| **Distribución de Paneles** | 3 paneles:<br>• Izquierda: Lista de logs.<br>• Centro: Gráfico de barras de volumen.<br>• Derecha: Filtros procedimentales. | Integrada y moderna:<br>• Centro-superior: Gráfico de barras de volumen en el tiempo.<br>• Inferior-izquierda: Filtros procedimentales (*Procedural Filtering*).<br>• Inferior-derecha: Lista de registros. |
| **Filtros Procedimentales** | Permiten refinar por `log_type`, `namespace`, etc., sin reescribir la consulta. | Idem: filtrado interactivo inmediato sobre los 10,000 resultados devueltos. |
| **Visualizador de Detalle del Evento** | Se abre en una **ventana emergente (*pop-out window*)** con vista lado a lado (*Side-by-Side*). | Se abre integrado en un **panel lateral de vista previa (*preview panel*)** a la derecha sin salir de la página. |
| **Resaltado de Términos** | El texto que coincide con la búsqueda/regex se resalta en amarillo. | Idem: texto coincidente resaltado automáticamente. |

---

#### 5. Componentes del Visor Detallado de Eventos (*Event Viewer*)

Al hacer clic en un registro en la nueva interfaz, el panel de vista previa muestra pestañas contextuales (según si el log fue normalizado o no):
1. **Entidades Resaltadas (*Highlighted Entities*):** Identificación visual inmediata de artefactos clave como IPs, nombres de usuario o nombres de host.
2. **Pestaña Registros en Bruto (*Raw Log Tab*):** Texto plano del registro original con el término de búsqueda resaltado.
3. **Pestaña Campos UDM (*UDM Fields Tab*):** Vista estructurada en árbol que muestra cómo el parser normalizó el registro en el esquema UDM.
4. **Pestaña Alertas (*Alerts Tab*):** Muestra si el evento normalizado coincidió con alguna regla del motor de detección y generó una alerta asociada.

> [!TIP]
> **Práctica Recomendada:**  
> Al realizar búsquedas sobre fuentes de registro de muy alto volumen (por ejemplo, proxies web, firewalls o DNS), reduzca siempre la ventana de tiempo (últimos 15 o 30 minutos) y seleccione explícitamente el tipo de registro (*Log Source*) para optimizar el tiempo de respuesta y evitar alcanzar el límite de los 10,000 resultados antes de ver los eventos relevantes.

---

### Lección 2: Esquema UDM y Familias de Campos (*UDM Schema & Field Families*)

> **Objetivo:** Comprender en profundidad la estructura lógica del Modelo de Datos Unificado (*UDM - Unified Data Model*), distinguiendo entre registros de eventos (*UDM Events*) y registros de entidades contextuales (*UDM Entities*), así como el rol de las familias de campos de nivel superior, sustantivos (*nouns*), relaciones (*relations*) y el grafo contextual (*Entity / Context Graph*).

---

#### 1. Los Dos Tipos de Registros en UDM: Eventos vs. Entidades

Google SecOps organiza toda la información bajo el esquema UDM en dos grandes categorías conceptuales:

| Dimensión | Registros de Eventos UDM (*UDM Events*) | Registros de Entidades UDM (*UDM Entities*) |
| :--- | :--- | :--- |
| **Definición** | Describen una **actividad o acción ocurrida en un instante de tiempo puntual**. | Describen **objetos del entorno y su contexto acumulado a lo largo del tiempo**. |
| **Temporalidad** | Poseen una marca temporal fija (`metadata.event_timestamp`). | No tienen un timestamp único de evento; son válidas para un **intervalo de tiempo (*time window / interval*)**. |
| **Objetivo** | Responder a: *¿Qué sucedió, cuándo ocurrió y qué sistemas/usuarios interactuaron?* | Enriquecer la telemetría respondiendo a: *¿Quién es este usuario, qué rol tiene, a qué departamento pertenece y de quién es este dispositivo?* |
| **Uso Principal** | Detecciones de actividad, correlación de registros y búsqueda en tiempo de ejecución. | Enriquecimiento contextual, poblado del **Grafo de Entidades (*Context Graph*)** y reglas avanzadas con análisis de comportamiento/riesgo. |

---

#### 2. Estructura del Evento UDM (*UDM Event Structure*) y Familias de Campos de Nivel Superior

Cada registro de evento UDM se origina en el objeto raíz `event` y se ramifica en familias de campos (*field families*) especializadas:

```
event
├── metadata          (Datos generales, marcas de tiempo, tipo de evento, proveedor/producto)
├── nouns             (Actores y objetos involucrados: principal, target, src, observer, intermediary, about)
├── network           (Detalles de red, protocolos, bytes transferidos, peticiones HTTP, emails)
├── security_result   (Veredictos de seguridad, riesgos detectados, acciones como allow/block)
└── extensions        (Datos contextuales especializados: authentication, vulnerability)
```

##### Detalle de las Familias de Campos del Evento:
* **`metadata` (Metadatos):** Información general del evento.
  * `metadata.event_type`: El **discriminador más crítico** de todo el evento. Es un campo enumerado obligatorio que define la naturaleza de la actividad (ej. `USER_LOGIN`, `NETWORK_CONNECTION`, `PROCESS_LAUNCH`).
  * `metadata.log_type`: Etiqueta de ingesta asignada al origen (ej. `ZSCALER_WEBPROXY`, `WINDOWS_DEFENDER`).
  * `metadata.event_timestamp`: Marca temporal precisa en UTC en que ocurrió el evento.
* **`nouns` (Sustantivos / Entidades en el Evento):** Representan a los participantes de la actividad. Se desglosan en subtipos comunes como `hostname`, `ip`, `mac`, `user` y `process`.
* **`network` (Red):** Almacena métricas y protocolos de comunicación (ej. bytes enviados y recibidos, URLs completas, métodos HTTP, cabeceras de correo).
* **`security_result` (Resultado de Seguridad):** Almacena las conclusiones de herramientas de seguridad que inspeccionaron el evento.
  * **Campos Enumerados (*Enumerated fields*):** Utilizan valores fijos estándar como `allow`, `block`, `quarantine`, `unknown_action`.
  * `action_details`: Preserva el veredicto o código original de la herramienta para referencia forense.
  * `url_back_to_product`: Enlace directo hipervinculado hacia la consola del fabricante de seguridad donde se generó el hallazgo.
* **`extensions` (Extensiones):**
  * `authentication`: Información detallada sobre intentos de inicio de sesión, mecanismos (MFA, contraseñas, Kerberos) y resultados.
  * `vulnerabilities`: Información sobre vulnerabilidades observadas (CVEs, severidad CVSS).

---

#### 3. Profundización en los Sustantivos de Eventos (*Noun Field Family*)

Los *nouns* constituyen los ejes pivotales fundamentales de casi cualquier investigación de seguridad. Definen el rol específico de cada elemento en la acción:

| Sustantivo UDM | Rol en el Evento | Ejemplo Típico |
| :--- | :--- | :--- |
| **`principal`** | El actor o dispositivo que **inicia o ejecuta activamente la acción**. | La estación de trabajo de un usuario, la IP origen de un cliente, la cuenta de usuario que lanzó un script. |
| **`target`** | La entidad **sobre la cual recae o se dirige la acción**. | El servidor de destino contactado, el archivo eliminado, la cuenta de usuario que fue modificada. |
| **`src`** | La entidad de origen físico o de red desde donde se origina el tráfico (cuando difiere del actor principal). | Dirección IP o puerto de origen en un registro de firewall. |
| **`intermediary`** | Un dispositivo o sistema que **intermedia, enruta o procesa la actividad**. | Un servidor proxy web corporativo, un balanceador de carga, un firewall de red. |
| **`observer`** | Un dispositivo que **solo monitorea y registra la actividad pasivamente sin interactuar directamente con ella**. | Un sensor IDS/IPS en modo espejo (SPAN port / TAP), un sniffer de paquetes de red. |
| **`about`** | Cualquier entidad u objeto referenciado en el evento que **no encaja directamente en los otros roles**. | Un dominio de C2 mencionado en una alerta de inteligencia de amenazas, un hash de archivo referenciado. |

> [!NOTE]
> **Campos Repetidos (*Repeated Fields*):**  
> Dentro de los sustantivos, campos como `ip` o `mac` son campos repetidos (*arrays*). Esto permite que una entidad (por ejemplo, un servidor multihome) contenga múltiples direcciones IP o interfaces de red dentro del mismo registro sin romper la estructura.

---

#### 4. Estructura de Entidades UDM (*UDM Entity Structure*) y Grafo Contextual

A diferencia de los eventos que son instantáneos, las **Entidades UDM** funcionan como contenedores de contexto duradero sobre los activos y usuarios del entorno, alimentando el **Grafo de Entidades (*Context Graph*)**.

##### Componentes de la Estructura de una Entidad:
1. **`metadata`:**
   * `metadata.entity_type` (**Campo Obligatorio Clave**): Define qué es el objeto (ej. `USER`, `ASSET`, `RESOURCE`, `DOMAIN`).
   * Contiene identificadores de producto, proveedor e IDs únicos (`product_entity_id`).
2. **`entity` (Nouns de Entidad):**
   * Describe los atributos intrínsecos del objeto: nombres, correos electrónicos, roles corporativos (`user`), detalles de hardware/sistema operativo y nombre de proyecto cloud (`asset`).
3. **`relations` (Relaciones):**
   * Establecen vínculos direccionales entre diferentes entidades del entorno (ej. un `USER` que *posee* o es *dueño* de un `ASSET`, o un `PROCESS` que *accede* a un `RESOURCE`).
   * Las relaciones apuntan de regreso a sustantivos (*nouns*), modelando la topología completa de la organización.
4. **`additional`:**
   * Espacio flexible para atributos personalizados y específicos del fabricante que no encajan en el esquema rígido, permitiendo extender la información sin romper la estandarización.

---

#### 5. Impacto en la Investigación y Reglas de Detección

* **Notación de Grafo (*Graph Notation*):** Permite cruzar en una misma búsqueda UDM o regla YARA-L un evento de telemetría (ej. conexión de red sospechosa) con los atributos de entidad de su ejecutor (ej. si el usuario pertenece al grupo "Ejecutivos VIP" o si el host es un "Servidor de Producción Crítico").
* **Pivoteo Dinámico:** La consistencia uniforme entre sustantivos de eventos y entidades permite al analista saltar fluidamente de un hash a un host, de un host a un usuario, y de un usuario a todas sus sesiones de autenticación en cuestión de segundos.

---

### Lección 3: Búsqueda UDM (*UDM Search*)

> **Objetivo:** Dominar la construcción y ejecución de consultas sobre eventos normalizados utilizando la sintaxis de UDM Search, operadores lógicos y de comparación, campos agrupados (*grouped fields*), tablas dinámicas (*pivot tables*), validación estricta de esquemas y la asistencia asistida por IA generativa con Gemini.

---

#### 1. Sintaxis, Operadores y Modificadores en UDM Search

Las consultas en UDM Search siguen un patrón estandarizado:  
`campo_udm [operador] "valor" [modificador]`

* **Operadores Lógicos:** `AND`, `OR`, `NOT` para combinar múltiples condiciones.
* **Control de Precedencia:** Uso de paréntesis `( )` para agrupar expresiones y controlar el orden exacto de evaluación lógica.
* **Operadores de Comparación:**
  * Igualdad / Desigualdad: `=`, `!=`
  * Numéricos / Tamaños: `>`, `>=`, `<`, `<=` (ej. `network.sent_bytes >= 67108864` para filtrar eventos donde se transmitieron al menos 64 MB).
* **Modificador Insensible a Mayúsculas y Minúsculas (`nocase`):**
  * Se añade al final de las condiciones sobre cadenas de texto para evitar falsos negativos por discrepancias tipográficas.
  * Ejemplo: `target.user.userid = "alice" nocase` coincide con "Alice", "ALICE" o "alice".
* **Expresiones Regulares (RE2):** Coincidencias de patrones delimitadas por barras diagonales `/patrón/`.

##### Ejemplo de Consulta Completa:
```sql
(metadata.log_type = "CORE_LIGHT" OR metadata.log_type = "GCP_IDS") AND
target.hostname != "" AND
network.sent_bytes >= 67108864 AND
(target.user.userid = /.*alice.*/ nocase)
```

> [!WARNING]
> **Validación Estricta del Esquema UDM:**  
> A diferencia de los motores de texto no estructurado, Google SecOps valida la sintaxis antes de ejecutar la consulta:
> 1. **Campos Enumerados:** **NO admiten expresiones regulares**. Una consulta como `metadata.event_type = /USER_.*/` es inválida y producirá un error de sintaxis; debe usarse un valor enumerado literal exacto como `metadata.event_type = "USER_LOGIN"`.
> 2. **Campos de Marca Temporal:** Deben definirse en formato numérico **Unix Epoch** en segundos/milisegundos, o seleccionarse interactivamente desde el selector de fecha y hora (*Date/Time Picker*) de la interfaz.

---

#### 2. Visualización e Interpretación de Resultados

Al ejecutar la búsqueda (*Run Search*), la interfaz unificada presenta:
1. **Resumen Asistido por Gemini (*Overview with Gemini Insights*):** En la parte superior, Gemini analiza automáticamente los eventos devueltos, resumiendo tipos de eventos, actividad de usuarios, volumen total e identificando patrones o anomalías sin requerir filtros manuales adicionales.
2. **Línea de Tiempo Cronológica (*Event Timeline*):** Histograma interactivo que distribuye la frecuencia de eventos a lo largo del tiempo para identificar ráfagas (*spikes*) de actividad anómala.
3. **Pestaña de Alertas (*Alerts Tab*):** Muestra de forma inmediata cualquier alerta del motor de detección vinculada a los eventos devueltos en la búsqueda.
4. **Lista de Resultados en Orden Cronológico Inverso:** Los eventos más recientes se muestran al principio.
5. **Columnas Personalizables:** Posibilidad de agregar o quitar columnas de campos UDM específicos (ej. `principal.ip`, `target.user.userid`, `metadata.event_type`) para comparar registros lado a lado en formato tabular sin abrir cada evento uno a uno.

---

#### 3. Visor de Detalles del Evento y Prefijos U / E

Al seleccionar un evento para inspeccionarlo, el visor de eventos detalla:
* **Entidades Relacionadas:** Resaltado de IPs, usuarios y activos involucrados.
* **Pestaña Raw Log:** El texto en bruto original.
* **Pestaña UDM Fields:** Mapeo jerárquico de campos. Cada campo cuenta con un prefijo visual identificador:
  * **Prefijo `[U]` (*UDM Parsed*):** Campo extraído y normalizado directamente del registro en bruto por el parser CBN.
  * **Prefijo `[E]` (*Enriched*):** Campo enriquecido automáticamente por la infraestructura de Google SecOps durante la ingesta (ej. geolocalización IP, datos WHOIS, resolución DNS histórica, contexto de Google Cloud).

---

#### 4. Campos Agrupados (*Grouped Fields*)

En investigaciones complejas, un indicador clave (como una IP o un usuario) puede aparecer en múltiples ubicaciones del esquema (`principal.ip`, `target.ip`, `src.ip`, etc.). Para evitar consultas interminables con múltiples `OR`, Google SecOps introduce **Campos Agrupados (*Grouped Fields*)**.

* **Ejemplo Práctico:**  
  En lugar de escribir:
  ```sql
  principal.ip = "1.1.1.1" OR target.ip = "1.1.1.1" OR src.ip = "1.1.1.1" OR observer.ip = "1.1.1.1"
  ```
  Se escribe simplemente:
  ```sql
  ip = "1.1.1.1"
  ```
* **Los 9 Campos Agrupados Disponibles:**
  1. `ip`
  2. `domain`
  3. `email`
  4. `file_path`
  5. `hash`
  6. `hostname`
  7. `namespace`
  8. `process_id`
  9. `user`
* Además de agilizar la consulta, los campos agrupados pueden insertarse como columnas directas en la tabla de resultados.

---

#### 5. Tablas Dinámicas (*Pivot Tables*)

Las tablas dinámicas permiten agregar y resumir métricas sobre los eventos devueltos directamente en la consola sin escribir scripts externos:
* **Estructura Clave (3 Componentes):**
  * **`Group by` (Agrupar por):** Define los campos UDM que formarán las filas de la tabla (ej. agrupar por `principal.user.userid` y `metadata.event_type`).
  * **`Values` (Valores / Métrica):** Define la agregación estadística (recuento de eventos `count`, sumatoria `sum`, promedio `avg`, etc.).
  * **`Order by` (Ordenar por):** Permite ordenar ascendentemente o descendentemente por las métricas calculadas.
* **Exportación:** Los resultados de la tabla dinámica pueden exportarse a **CSV (hasta 10,000 filas)** para informes ejecutivos o análisis forense complementario.

---

#### 6. Integración con Gemini AI: Búsqueda en Lenguaje Natural

Google SecOps integra Gemini en la barra de búsqueda para analistas:
* **Generación de Consultas (*Natural Language to UDM Query*):** Permite escribir una solicitud en lenguaje natural cotidiano (ej. *"Successful Okta login events from users outside the United States"*) y, con un clic en **Generate Query**, Gemini la traduce automáticamente a una consulta estructurada con los campos, operadores y condiciones UDM correspondientes.
* **Buenas Prácticas:** Ideal para acelerar el aprendizaje del esquema UDM y crear consultas base rápidamente. No obstante, en investigaciones críticas siempre se debe verificar y ajustar la lógica generada antes de dar por concluidos los resultados.

---

### Lección 4: Introducción a Tablas de Datos (*Data Tables Introduction*)

> **Objetivo:** Comprender la naturaleza y arquitectura de las Tablas de Datos (*Data Tables*) como la evolución y reemplazo moderno de las Listas de Referencia (*Reference Lists*), analizando sus casos de uso (listas de permitidos, listas de vigilancia y enriquecimiento contextual), límites operativos, tipos de datos, configuración de TTL, sintaxis de coincidencia por columnas y filas, y visualización en UDM Search con el prefijo `[D]`.

---

#### 1. ¿Qué son las Tablas de Datos (*Data Tables*)?

Las **Tablas de Datos (*Data Tables*)** proporcionan la capacidad de almacenar conjuntos de datos tabulares estructurados en filas y columnas dentro de Google SecOps.

* **Evolución Tecnológica:** Representan el reemplazo directo y la modernización de las antiguas **Listas de Referencia (*Reference Lists*)**. Mientras que una lista de referencia tradicional era unidimensional (una única lista de cadenas o IPs), las Data Tables son esencialmente **hojas de cálculo o tablas relacionales multicolumna**.
* **Integración Global en la Plataforma:** Pueden ser consumidas en todas las capacidades basadas en consultas de Google SecOps:
  * **Búsqueda SIEM (*SIEM Search*)**
  * **Paneles de Control (*Dashboards*)**
  * **Reglas de Detección YARA-L (*Detection Rules*)**
  * **Playbooks de SOAR** (mediante la integración nativa *Google Chronicle SOAR Integration* con acciones para consultar y actualizar tablas automáticamente).

---

#### 2. Capacidades y Límites Operativos

| Característica | Detalle Técnico |
| :--- | :--- |
| **Capacidad Máxima de Almacenamiento** | Hasta **10 millones de filas (*entries*)** por tabla de datos. |
| **Límite de Visualización / Edición en UI** | Hasta **10,000 filas** visibles y editables directamente en la consola web. |
| **Recomendación de Gestión** | Para tablas grandes (más de 10,000 registros), se recomienda encarecidamente la administración automatizada vía **API** o **SOAR Playbooks**. |
| **Importación de Datos** | Admite carga manual en la interfaz y subida masiva de archivos planos delimitados por comas (**CSV**) o por tabulaciones (**TSV**). |
| **Tiempo de Vida / Expiración (*TTL - Time to Live*)** | Configurable opcionalmente por tabla. Permite que las filas expiren automáticamente dentro de un rango de **24 horas hasta 365 días** (ideal para IoCs efímeros o listas de cuarentena temporal). |

---

#### 3. Casos de Uso Fundamentales

1. **Listas de Permitidos (*Allow Lists / Safe Lists*):**
   * **Propósito:** Filtrar y suprimir eventos legítimos o de bajo riesgo para reducir el ruido y evitar falsos positivos.
   * **Ejemplos:** Rangos CIDR de redes internas seguras, cuentas de servicio autorizadas para escaneos de vulnerabilidades, nombres de host de mantenimiento.
2. **Listas de Vigilancia (*Watch Lists*):**
   * **Propósito:** Elevar la prioridad y enfocar la detección sobre actividades o activos de alto riesgo.
   * **Ejemplos:** Indicadores de compromiso (IoCs) de campañas activas, cuentas de ejecutivos o administradores VIP, activos clasificados como "joyas de la corona" (*Crown Jewels*), IPs de países bloqueados.
3. **Enriquecimiento y Búsquedas Contextuales (*Enrichment / Lookups*):**
   * **Propósito:** Realizar cruces (*joins*) entre campos UDM de telemetría y datos contextuales que no existen en los registros originales.
   * **Ejemplo Práctico:** Un registro de log incluye el nombre del departamento del usuario (`Security Operations`), pero no los datos de contacto de escalado. Una *Data Table* puede mapear el departamento con el correo del gerente y el canal de Slack correspondiente, inyectando estos datos directamente en la alerta para acelerar la respuesta del analista.

---

#### 4. Estructura, Esquema y Tipos de Datos

* **Fila de Cabecera Obligatoria:** La primera fila de la tabla está reservada estrictamente para los nombres de las columnas (*keys*), separados por comas.
* **Tipos de Datos Soportados:**
  * `string`: Cadenas de texto alfanuméricas.
  * `regex`: Expresiones regulares para coincidencias flexibles de patrones.
  * `cidr`: Notación de bloques de red IPv4/IPv6 (ej. `10.0.0.0/8`, `192.168.1.0/24`).
  * `number`: Valores numéricos enteros o decimales.
  * `unspecified`: Tipo especial utilizado para asignaciones avanzadas del Grafo de Entidades (*Entity Graph*).

> [!CAUTION]
> **Inmutabilidad del Esquema:**  
> Los nombres de los encabezados de las columnas y sus tipos de datos **NO pueden modificarse después de que la tabla de datos ha sido guardada**. Es crucial verificar minuciosamente la estructura antes de confirmar la creación.

---

#### 5. Sintaxis de Búsqueda con Data Tables en UDM Search

La sintaxis conserva la conocida palabra clave `in`, pero ahora requiere especificar la columna sobre la cual se realiza la comprobación:

* **Comparación Basada en Columnas (*Column-based comparison*):**
  * Sintaxis: `campo_udm in %nombre_tabla.nombre_columna%`
  * Ejemplo (Lista de permitidos):
    ```sql
    principal.ip in %redes_autorizadas.rango_cidr%
    ```
* **Comparación Inversa (`not in`):**
  * Se antepone el operador `not`:
    ```sql
    not (principal.ip in %redes_autorizadas.rango_cidr%)
    ```
* **Comparaciones Basadas en Filas (*Row-based comparison*):**
  * Vinculan el evento con una fila específica de la tabla de datos. La condición se evalúa como verdadera **solo si todas las condiciones coinciden dentro de una misma fila** de la tabla.

---

#### 6. Visualización de Resultados: Prefijo `[D]`

Cuando una consulta en UDM Search utiliza una tabla de datos:
* Aparece automáticamente una nueva columna en la tabla de resultados identificada con el prefijo **`[D]`** (*Data Table*).
* Esta columna muestra el valor coincidente de la fila de la tabla de datos correspondiente al evento.
* El analista puede agregar columnas adicionales de la tabla de datos a la vista de resultados para mostrar el contexto enriquecido sin salir de la búsqueda.

---

### Lección 5: Búsqueda Estadística y Agregaciones en UDM (*UDM Statistical Search & Aggregation*)

> **Objetivo:** Comprender la arquitectura, sintaxis y casos de uso de la Búsqueda Estadística en UDM (*UDM Stats*), comparándola con las reglas YARA-L, analizando el rol de las variables de marcador de posición (*placeholder variables*), las secciones `match`, `outcome`, `order` y `limit`, y las funciones matemáticas y de agregación para el análisis de tendencias sobre grandes volúmenes de telemetría.

---

#### 1. ¿Qué es la Búsqueda Estadística en UDM (*UDM Statistical Search*)?

La **Búsqueda Estadística en UDM (*UDM Stats*)** es una funcionalidad analítica avanzada integrada en la consola de búsqueda de Google SecOps. Permite a los analistas calcular métricas, tendencias y resúmenes sobre grandes volúmenes de telemetría a lo largo de amplios rangos temporales (semanas o meses) sin tener que inspeccionar eventos uno a uno ni recurrir a herramientas de exportación externas.

* **Casos de Uso Típicos:**
  * *¿Cuántos intentos de inicio de sesión fallidos ocurrieron el mes pasado desglosados por usuario?*
  * *¿Cuáles son las 10 IPs externas que transmitieron el mayor volumen de bytes hacia servidores internos?*
  * *¿Qué tipos de eventos están generando el mayor volumen de ingesta en la plataforma?*
* **Ventaja de Unificación:** Emplea una sintaxis inspirada fuertemente en el motor de reglas **YARA-L**, ofreciendo una experiencia coherente entre la búsqueda interactiva, la analítica en paneles y la creación de detecciones.

---

#### 2. Comparativa Fundamental: UDM Statistical Search vs. Reglas YARA-L

Aunque comparten un estilo sintáctico similar, están optimizadas para propósitos diferentes:

| Aspecto | Búsqueda Estadística UDM (*UDM Stats*) | Motor de Detección (*YARA-L Rules*) |
| :--- | :--- | :--- |
| **Propósito Principal** | **Búsqueda analítica, exploración de datos, agregación e informes.** | **Lógica de detección de amenazas, generación de alertas en tiempo real.** |
| **Estructura de Secciones** | • Filtrado inicial (*Filter statement*)<br>• Agrupación (`match`)<br>• Cálculos agregados (`outcome`)<br>• Ordenamiento (`order`)<br>• Límite de filas (`limit`) | • Metadatos (`meta`)<br>• Definición de eventos (`events`)<br>• Ventana de tiempo y correlación (`match`)<br>• Contexto y puntuación de alerta (`outcome`)<br>• Opciones de ejecución (`condition` / `options`) |
| **Variables Soportadas** | Solo **Variables Marcador de Posición (*Placeholder Variables*)** con prefijo `$` (ej. `$userid`, `$sent_bytes`). | Variables de eventos (ej. `$e.principal.ip`), variables de coincidencia temporal y variables de outcome. |
| **Manejo del Tiempo en `match`** | **No requiere definir ventana temporal en el código.** Utiliza automáticamente el rango seleccionado en el selector de fecha/hora de la interfaz (*Time Picker*). | **Obligatorio** definir la ventana de tiempo en la cláusula `match` (ej. `over 10m` o `over 1h`) para correlacionar flujos continuos de eventos. |

---

#### 3. Estructura y Secciones de una Consulta UDM Stats

Una consulta estadística completa se compone de los siguientes bloques lógicos:

```
[Sentencia de Filtrado Inicial (Filter Statement)]
match:
    [Campos o variables de agrupación (Group by)]
outcome:
    [Cálculos matemáticos y agregaciones]
order:
    [Ordenamiento ascendente o descendente]
limit:
    [Límite numérico de filas]
```

##### Detalle de Cada Sección:

##### A. Sentencia de Filtrado Inicial (*Filtering Statement*)
* Es donde comienza toda consulta. Funciona exactamente igual que una búsqueda UDM estándar (operadores booleanos `AND`, `OR`, `NOT`, comparadores, `nocase` y expresiones regulares RE2).
* **Asignación de Variables Marcador de Posición:** Permite vincular campos UDM a variables arbitrarias con el signo `$` para reutilizarlas en las secciones posteriores.
* Admite funciones booleanas de YARA-L en el filtrado (ej. funciones de rangos CIDR o manipulación de tiempo).

##### B. Sección de Agrupación (`match`)
* Equivalente a la cláusula `GROUP BY` de SQL. Organiza los eventos coincidentes según los campos o placeholders indicados.
* Permite agrupar por campos UDM directos (ej. `principal.ip`) o por placeholders (ej. `$principal_ip`, `$target_ip`).
* No utiliza la palabra clave `over <tiempo>`, ya que la ventana temporal se hereda del selector de tiempo de la interfaz.

##### C. Sección de Cálculos y Agregaciones (`outcome`)
* Define los cálculos matemáticos que se aplicarán sobre los eventos agrupados. **Cada variable calculada en el `outcome` se convierte en una columna en la tabla de resultados.**
* Puede existir incluso sin una sección `match` previa (en cuyo caso la agregación se calcula sobre el total de eventos filtrados).
* **Funciones de Agregación Soportadas:**
  * `count($variable)`: Recuento total de ocurrencias.
  * `count_distinct($variable)`: Recuento de elementos únicos.
  * `sum($variable)`: Sumatoria de valores numéricos (ej. total de bytes).
  * `min($variable)` / `max($variable)`: Valores mínimos y máximos.
  * `avg($variable)`: Promedio aritmético.
  * `stddev($variable)`: Desviación estándar (útil para detectar anomalías de tráfico).
  * `array($variable)` / `array_distinct($variable)`: Agrupa los valores coincidentes en una lista/array.
* **Funciones Matemáticas:**
  * `math.round(expresión, decimales)`: Redondea al entero más cercano o a un número específico de decimales.
  * `math.log(expresión)`: Calcula el logaritmo para normalizar escalas numéricas amplias.

##### D. Sección de Ordenamiento (`order`)
* Controla cómo se ordenan los resultados devueltos utilizando las variables definidas en `match` o `outcome`.
* Sintaxis: `variable [asc | desc]`.
* Admite múltiples criterios en una misma línea (ej. `order: $fecha asc, $total_eventos desc`).

##### E. Sección de Límite (`limit`)
* Restringe el número máximo de filas a mostrar en la interfaz (ej. `limit: 10` o `limit: 30`).
* Permite aislar los "Top N" infractores, usuarios o destinos con mayor consumo o actividad.

---

#### 4. Ejemplo Práctico Integrado

El siguiente ejemplo cuantifica el número de eventos de inicio de sesión de usuario, agrupados según el veredicto de seguridad (*Allow* o *Block*), ordenados de mayor a menor frecuencia y limitados a los 10 primeros resultados:

```yara
// 1. Filtrado inicial y asignación de variables
metadata.event_type = "USER_LOGIN"
security_result.action = $sec_action
$sec_action = "BLOCK" or $sec_action = "ALLOW"

// 2. Agrupación por el veredicto de seguridad
match:
    $sec_action

// 3. Agregación estadística de eventos únicos
outcome:
    $total_logins = count_distinct(metadata.id)

// 4. Ordenamiento descendente
order:
    $total_logins desc

// 5. Límite de resultados
limit: 10
```

* **Salida generada:** Una tabla resumida de dos columnas (`sec_action` y `total_logins`) que presenta inmediatamente la proporción de accesos bloqueados frente a permitidos sin requerir procesamiento manual de registros.

---

### Lección 6: Demostración de Búsqueda UDM (*UDM Search Demo*)

> **Objetivo:** Repasar y aplicar de manera práctica en la consola de Google SecOps las herramientas operativas de investigación: historial de búsquedas, administrador de búsquedas (*Search Manager*), búsquedas compartidas y parametrizadas, búsqueda inversa en el esquema (*UDM Lookup*), personalización de columnas, análisis en panel de eventos (*Event Viewer*), pivoteo dinámico, exportación de datos y asistencia con Gemini AI.

---

#### 1. Navegación e Historial de Búsquedas (*Search History*)

* **Ruta de Acceso:** `Investigation > SIEM Search`.
* **Barra de Búsqueda Unificada:** Sirve tanto para búsquedas en texto sin procesar (*Raw Log Search*) como para búsquedas estructuradas en el modelo unificado (*UDM Search*).
* **Historial de Consultas (*History Menu*):**
  * Es una función a la que el usuario debe suscribirse explícitamente (*opt-in*).
  * Los resultados de las búsquedas ejecutadas se conservan en caché durante un máximo de **24 horas**, evitando la necesidad de volver a procesar y recalcular consultas idénticas.
  * Si no está activado, la consola no almacena registros temporales de las búsquedas previas y cada sesión inicia desde cero.

---

#### 2. Administrador de Búsquedas (*Search Manager*) y Consultas Guardadas

* **Búsquedas Guardadas (*Saved Searches*):**
  * Permiten almacenar consultas complejas y recurrentes bajo la sección *Your saved searches* para reutilizarlas en investigaciones periódicas.
  * Por defecto son de visibilidad **privada**, pero pueden compartirse con toda la organización (*Shared UDM Searches*).
* **Búsquedas Curadas por Google (*Published by Google*):**
  * Búsquedas predefinidas integradas en la plataforma, identificables por el icono de Google SecOps. Al hacer clic sobre cualquiera de ellas, se cargan automáticamente en la barra de búsqueda listas para ser ejecutadas.
* **Funciones del Administrador de Búsquedas (*Search Manager*):**
  * Renombrar, editar, organizar y eliminar consultas guardadas o gestionar el historial.
  * **Consultas Parametrizadas con Variables Dinámicas:** Es posible introducir variables de marcador de posición interactivas entre llaves, por ejemplo:
    ```sql
    metadata.vendor_name = ${vendor_name}
    ```
    Al ejecutar una búsqueda guardada con esta sintaxis, la consola solicita al analista que introduzca interactivamente el valor deseado antes de lanzar la consulta.

---

#### 3. Búsqueda Inversa en el Esquema (*UDM Lookup*)

Herramienta integrada para asistir en la construcción de consultas cuando no se recuerda la estructura exacta del esquema:
* **Búsqueda por Valor:** Permite introducir un artefacto conocido (una dirección IP, un dominio o un nombre de usuario) y la herramienta identifica en qué campos UDM se encuentra alojado dicho valor en los registros de la organización.
* **Búsqueda por Nombre de Campo:** Permite localizar campos por texto predictivo, copiar la ruta exacta del campo UDM (ej. `principal.user.userid`) e insertarla directamente en la barra de búsqueda.

---

#### 4. Operadores Prácticos en Búsqueda UDM

Permite articular lógica condicional avanzada combinando:
* Operadores lógicos: `AND`, `OR`, `NOT` y agrupación por paréntesis `( )`.
* Operadores de comparación: `=`, `!=`, `>`, `<`, `>=`, `<=`.
* Modificador insensible a mayúsculas/minúsculas: `nocase`.
* Expresiones regulares delimitadas por barras: `/patrón/`.

##### Consulta de Ejemplo de la Demostración:
```sql
(metadata.log_type = "WINDOWS_SYSMON" OR metadata.log_type = "WINDOWS_DEFENDER_ATP")
AND metadata.event_type = "NETWORK_CONNECTION"
AND principal.user.userid = /.*harvey.*/ nocase
```
* **Interpretación:** Recupera todas las conexiones de red registradas por Sysmon o Defender ATP iniciadas por cualquier cuenta cuyo identificador de usuario contenga la subcadena "harvey", sin importar si está escrita en mayúsculas o minúsculas.

---

#### 5. Exploración de Resultados, Personalización y Event Viewer

* **Línea de Tiempo (*Timeline*):** Gráfico interactivo en la parte superior que ilustra la concentración temporal de los eventos devueltos.
* **Tabla de Resultados:** Orden cronológico inverso (los eventos más recientes aparecen primero).
* **Pestaña de Alertas (*Alerts Tab*):** Muestra si alguno de los eventos listados activó una regla de detección.
* **Administrador de Columnas (*Column Manager*):** Permite personalizar los campos UDM visibles en la tabla principal (añadir IPs, usuarios, tipos de eventos), permitiendo evaluar los datos de un vistazo sin necesidad de abrir cada registro individualmente.
* **Visor de Eventos (*Event Viewer*):** Al hacer clic sobre un registro:
  * **Event Fields:** Vista detallada de las entidades involucradas (`principal`, `target`, `metadata`).
  * **Raw Log:** Vista lado a lado del registro en bruto original para contrastar la normalización efectuada.

---

#### 6. Filtrado, Agrupación, Pivoteo y Exportación

* **Campos Agrupados (*Grouped Fields*):** Agilizan búsquedas multifield. Por ejemplo, escribir:
  ```sql
  ip = "8.8.8.8"
  ```
  evalúa automáticamente y de forma simultánea `principal.ip`, `src.ip`, `target.ip`, `observer.ip` e `intermediary.ip`.
* **Pestaña Pivot (*Pivot Tab*):** Permite agrupar los resultados devueltos por cualquier campo UDM (como `hostname`, `user` o `event_type`) para calcular recuentos y observar tendencias.
* **Capacidad de Exportación:** La plataforma permite exportar hasta **1,000,000 de filas (1 millón)** a un archivo **CSV** para análisis masivo complementario o reporting externo.

---

#### 7. Búsqueda Asistida por IA (Gemini Search)

* Permite formular búsquedas en lenguaje natural cotidiano:  
  *Ejemplo:* *"Successful Okta login outside the US in the last year"*.
* Gemini traduce la oración directamente a la sintaxis estructurada UDM correspondiente.
* **Recomendación para el Analista:** Funciona como un acelerador de productividad, pero siempre debe revisarse la consulta generada para verificar la exactitud de los campos y operadores antes de tomar decisiones operativas críticas.

---

### Lección 7: Comprobación de Conocimientos de Investigación en SIEM (*SIEM Investigation: Knowledge Check*)

> **Nota de aprobación requerida:** 75%  
> **Temas evaluados:** Casos de uso de Data Tables, propósito de UDM Statistical Search, rol del sustantivo UDM `principal`, y funcionalidades de la pestaña UDM Overview.

---

#### Preguntas y Respuestas Técnicas Desarrolladas

#### 1. ¿Cuál es un caso de uso principal para las Tablas de Datos en Google SecOps? (*What is a primary use case for Data Tables in Google SecOps?*)

* [ ] Proporcionar almacenamiento de registros a largo plazo que eluda el modelo de retención de Chronicle (*Providing long-term log storage that bypasses Chronicle’s retention model*)
* [ ] Importar automáticamente todos los feeds externos de inteligencia de amenazas sin configuración previa (*Automatically importing all external threat intelligence feeds without configuration*)
* [ ] Servir como reemplazo de los eventos UDM al escribir lógica de detección (*Serving as a replacement for UDM events when writing detection logic*)
* [x] **Almacenar conjuntos de datos de referencia que se pueden cruzar o consultar en Búsquedas, Paneles de Control y Reglas** (*Storing reference datasets that can be joined or queried in Searches, Dashboards, and Rules*)

> **Explicación técnica:** Las **Data Tables** son esencialmente conjuntos de datos estructurados tabulares (listas de referencia multicolumna) diseñados para alojar listas de permitidos (*allow lists*), listas de seguimiento (*watch lists*) y datos de enriquecimiento/búsqueda contextual (*lookups*). Estos datos pueden cruzarse (*join*) de forma directa con los eventos UDM en las búsquedas SIEM, widgets de dashboards y reglas de detección YARA-L utilizando la sintaxis `campo in %tabla.columna%`.

---

#### 2. ¿Cuál es el propósito principal de la Búsqueda Estadística en UDM (*Statistical UDM Search*)? (*What is the primary purpose of Statistical UDM Search?*)

* [ ] Proporcionar alertas en tiempo real basadas únicamente en puntuaciones de anomalía (*To provide real-time alerting based solely on anomaly scores*)
* [ ] Reescribir eventos UDM en un esquema normalizado antes de la ingesta (*To rewrite UDM events into a normalized schema before ingestion*)
* [ ] Generar automáticamente nuevas reglas YARA-L basadas en detecciones recientes (*To automatically generate new YARA-L rules based on recent detections*)
* [x] **Analizar grandes volúmenes de eventos UDM y descubrir tendencias utilizando funciones estadísticas** (*To analyze large volumes of UDM events and uncover trends using statistical functions*)

> **Explicación técnica:** **UDM Statistical Search (UDM Stats)** está concebida para la analítica y agregación masiva sobre telemetría en amplios rangos temporales. Mediante funciones de cálculo (`count`, `count_distinct`, `sum`, `avg`, `min`, `max`, `stddev`), permite a los analistas calcular tendencias, volumetría y comportamientos atípicos agrupados por dimensiones clave sin tener que revisar eventos individuales uno por uno.

---

#### 3. ¿Qué representa el sustantivo UDM `principal` en un evento? (*What does the UDM noun principal represent in an event?*)

* [ ] Una entidad de origen sobre la que actúa el principal (*A source entity being acted upon by the principal*)
* [ ] Un dispositivo que observa la actividad pero no interactúa directamente (*A device that observes the activity but does not directly interact*)
* [ ] La entidad sobre la cual se actúa, como el objetivo de la actividad (*The entity that is acted upon, such as the target of the activity*)
* [x] **La entidad o dispositivo actor que realiza o inicia la actividad** (*The acting entity or device that performs the activity*)

> **Explicación técnica:** Dentro del modelo de sustantivos (*nouns*) de UDM, el **`principal`** siempre describe al sujeto o actor que inicia, ejecuta o genera activamente la acción (por ejemplo, el endpoint del cliente, la cuenta de usuario que ejecuta un comando o el host que origina la conexión). En contraste, el objeto que recibe la acción es el **`target`**, y un dispositivo intermedio es un **`intermediary`** o **`observer`**.

---

#### 4. ¿Qué proporciona la pestaña UDM Overview a los analistas? (*What does the UDM Overview tab provide to analysts?*)

* [x] **Visibilidad rápida de los resultados de búsqueda al resumir tipos de eventos clave, usuarios y distribución de registros** (*Quick visibility into search results by summarizing key event types, users, and log distribution*)
* [ ] Una transmisión en tiempo real de todos los eventos UDM enriquecidos en cada fuente de datos (*A real-time feed of all enriched UDM events across every data source*)
* [ ] Una lista de todas las reglas compuestas y las detecciones que han generado (*A list of all composite rules and the detections they have generated*)
* [ ] Creación automática de nuevas reglas de detección basadas en consultas de búsqueda recientes (*Automatic creation of new detection rules based on recent search queries*)

> **Explicación técnica:** La pestaña **UDM Overview** (apoyada con la inteligencia contextual de **Gemini**) proporciona una síntesis visual inmediata sobre los resultados devueltos por la consulta, agrupando la distribución de tipos de eventos (`metadata.event_type`), la actividad destacada de usuarios y el volumen global a lo largo del tiempo, permitiendo al analista comprender patrones macroscópicos sin necesidad de aplicar filtros manuales adicionales.

---

## Módulo 4: SIEM Dashboards (Paneles de Control SIEM)

### Lección 1: Introducción a Dashboards y Contenido Curado (*Dashboards Introduction & Curated Content*)

> **Objetivo:** Comprender la nueva generación de paneles de control nativos de Google SecOps desplegados a partir de 2025 (sustitutos de la integración heredada de Looker), la arquitectura y tipos de widgets basados en consultas YARA-L, el uso del contenido curado out-of-the-box por Google, las fuentes de datos admitidas con sus límites de retención temporal y la gobernanza unificada mediante Feature RBAC y Data RBAC.

---

#### 1. La Nueva Generación: Dashboards Nativos vs. Looker Heredado (*Legacy*)

Google SecOps introdujo una arquitectura de visualización nativa completamente renovada:
* **Dashboards Nativos (*Native Dashboards*):** Construidos y renderizados directamente en el núcleo de Google SecOps, aplicables tanto a **SIEM** como a **SOAR**.
* **Migración desde Looker:** Reemplazan a los paneles heredados basados en una instancia integrada de Looker (*Looker-powered Dashboards*), los cuales están en proceso de obsolescencia (*deprecation*). Se recomienda la transición inmediata a la nueva interfaz.
* **Ventajas Clave de la Arquitectura Nativa:**
  * **Rendimiento y Tiempos de Carga:** Eliminación de capas intermedias; las visualizaciones cargan notablemente más rápido.
  * **Sintaxis Unificada YARA-L:** Los widgets se construyen utilizando la misma sintaxis aprendida en *UDM Statistical Search* y reglas de detección.
  * **Gobernanza Automatizada de Acceso:** Compatibilidad nativa e implícita con **Data RBAC Scopes**.
  * **Automatización Completa:** Totalmente gestionables y automatizables vía API REST.

---

#### 2. Navegación y Tipos de Contenido: Curados vs. Personalizados

* **Ruta de Acceso:** `Dashboards & Reports > Dashboards`.
* **Paneles Curados (*Curated Dashboards*):**
  * Paneles preconfigurados y mantenidos activamente por Google SecOps para casos de uso comunes de seguridad (ej. tráfico de red, detección de amenazas, inicios de sesión corporativos).
  * **Filtrado Rápido:** En la vista de paneles, se puede filtrar por `type = curated` o `owner = Google SecOps`.
  * **Duplicación y Personalización:** Todo panel curado puede ser **duplicado (*Duplicate*)**, permitiendo a las organizaciones adaptar widgets, agregar métricas propietarias o ajustar filtros sin perder la plantilla base.
  * **Actualización Continua:** Google añade y actualiza periódicamente nuevos paneles curados en la biblioteca global de la plataforma sin requerir intervención del usuario.

---

#### 3. Componentes y Estructura de un Widget

Cada visualización dentro de un dashboard nativo se compone de cuatro elementos básicos:

```
[Widget del Dashboard]
├── 1. Consulta (Query)       -> Construida en sintaxis YARA-L (filtros, match, outcome).
├── 2. Línea de Tiempo        -> Rango relativo (ej. últimos 7 días) o rango absoluto de fechas.
├── 3. Tipo de Gráfico        -> Mosaicos numéricos (tiles), barras, líneas, medidores (gauges),
│                                tablas y mapas geográficos con Google Maps.
└── 4. Detalles del Widget    -> Nombre del widget y breve descripción funcional.
```

---

#### 4. Fuentes de Datos Admitidas y Límites de Intervalo Temporal

Los paneles nativos pueden consultar múltiples conjuntos de datos dentro de Google SecOps utilizando prefijos de consulta específicos:

| Fuente de Datos | Prefijo YARA-L | Descripción del Conjunto de Datos | Límite Temporal Máximo por Consulta |
| :--- | :--- | :--- | :--- |
| **Eventos UDM (*UDM Events*)** | *(Sin prefijo / default)* | Telemetría y eventos de registros normalizados ingeridos en SIEM. | **Hasta 90 días** |
| **Grafo de Entidades (*Entity Graph*)** | `graph.` | Contexto de usuarios, activos y relaciones organizacionales. | **Hasta 365 días** |
| **Detecciones (*Detections*)** | `detection.` | Alertas y hallazgos disparados por el motor de reglas. | **Hasta 365 días** |
| **Ingesta (*Ingestion*)** | `ingestion.` | Métricas operativas de volumen de logs y flujo de fuentes. | **Hasta 365 días** |
| **Reglas de Detección (*Rules*)** | `rule.` | Metadatos y configuraciones del catálogo de reglas. | **Sin límite de intervalo** |
| **Fuentes SOAR (*SOAR Sources*)** | `soar.` | Casos, incidentes, playbooks y métricas de respuesta a incidentes. | **Hasta 365 días** |

---

#### 5. Control de Acceso y Cumplimiento de Data RBAC

La seguridad y privacidad en los paneles de control nativos se gestiona en dos niveles:

1. **Feature RBAC (Permisos de Gestión en Google Cloud IAM):**
   * Controla qué usuarios o grupos pueden **ver, crear, editar, duplicar o eliminar** paneles de control dentro del proyecto de Google Cloud vinculado a SecOps (`chronicle.dashboards.*`).
2. **Cumplimiento Nativo de Data RBAC (*Data RBAC Compliant*):**
   * Los paneles respetan automáticamente los **Data Access Scopes** asignados a cada usuario.
   * **Comportamiento Multi-tenant Seguro:** Dos usuarios con distintos ámbitos de acceso (por ejemplo, un analista de la región EMEA y otro de la región Americas) pueden abrir exactamente el mismo panel y **cada uno visualizará únicamente la telemetría correspondiente a su ámbito asignado**. No se requiere crear paneles duplicados por región ni configuración manual adicional.

---

### Lección 2: Construcción de Consultas YARA-L para Dashboards (*Building a YARA-L Query*)

> **Objetivo:** Dominar la construcción estructurada de consultas YARA-L para alimentar widgets en los paneles nativos de Google SecOps, analizando la función específica de cada sección (`events`, `match`, `outcome`, `condition`, `order`, `limit`), el manejo de variables y umbrales, y los valores predeterminados y límites máximos de filas para visualizaciones.

---

#### 1. Arquitectura de una Consulta YARA-L en Dashboards

En los nuevos paneles nativos de Google SecOps, cada widget visual se sustenta en una consulta YARA-L modular. Aunque comparte sintaxis con las reglas de detección, está adaptada para la analítica de agregación y visualización.

```
[Estructura de Consulta para Widgets]
├── events:     Filtra la telemetría inicial y define variables de campos UDM.
├── match:      (Opcional) Agrupa los eventos por campos o variables clave (GROUP BY).
├── outcome:    Aplica funciones matemáticas y de agregación (columnas resultantes).
├── condition:  (Opcional) Aplica filtros de umbral numérico sobre las métricas calculadas.
├── order:      (Opcional) Ordena los resultados de forma ascendente o descendente.
└── limit:      (Opcional) Restringe el número de filas devueltas (Top N).
```

---

#### 2. Desglose Detallado de Cada Sección

##### A. Sección de Eventos (`events`)
* **Propósito:** Define los criterios de inclusión de telemetría y captura valores en variables de marcador de posición (*placeholders*).
* **Operador Implícito:** Cuando se colocan múltiples condiciones en líneas separadas, el motor asume automáticamente un operador **`AND`** entre ellas.
* **Uso de Variables:** Se pueden declarar variables con el signo `$` para reutilizarlas en las secciones siguientes (ej. `$sec_action = security_result.action`). La asignación a variable es opcional; se puede filtrar directamente contra el campo UDM literal.
* **Soporte Extendido:** Admite expresiones regulares (`/patrón/`) y funciones booleanas de YARA-L.

##### B. Sección de Coincidencia y Agrupación (`match`)
* **Propósito:** Agrupa los eventos según los criterios definidos (similar a `GROUP BY` en SQL).
* **Diferencia Fundamental con Detecciones:** **No requiere ni utiliza ventana de tiempo (`over <tiempo>`)**, ya que el widget se calcula sobre el conjunto de datos completo delimitado por el selector temporal del dashboard.
* Es una sección opcional; si se omite, los cálculos del `outcome` se aplican sobre la totalidad de los eventos filtrados.

##### C. Sección de Resultados y Agregación (`outcome`)
* **Propósito:** Ejecuta operaciones de agregación y cálculos numéricos. **Cada variable definida aquí se convierte en una columna o métrica del gráfico.**
* **Funciones Soportadas:**
  * Agregaciones: `count()`, `count_distinct()` (para contar IDs o elementos únicos), `sum()`, `avg()`, `min()`, `max()`.
  * Matemáticas y no agregadas: `math.round()`, `math.log()`.

##### D. Sección de Condición (*Threshold Filtering*) (`condition`)
* **Propósito:** Actúa como un filtro posterior a la agregación (equivalente a `HAVING` en SQL), mostrando únicamente los grupos que superan un umbral predefinido.
* **Ejemplo de Uso:** Mostrar únicamente usuarios o acciones donde el total de eventos supere un umbral (ej. `$total_events > 500`).
* Admite operadores lógicos y funciones de arrays para filtros avanzados.

##### E. Secciones de Ordenamiento y Límite (`order` y `limit`)
* **`order`:** Define la ordenación de las filas (`asc` o `desc`) utilizando las variables de `match` o `outcome`.
* **`limit`:** Esencial para gráficos de tipo "Top N" (ej. Top 10 atacantes o destinos con mayor consumo):
  * **Límite por Defecto:** Si no se especifica la cláusula `limit`, la plataforma aplica un valor predeterminado de **1,000 filas**.
  * **Límite Máximo Configurable:** Se puede elevar hasta un máximo de **10,000 filas** por widget.

---

#### 3. Caso de Uso Práctico Integrado

**Requerimiento del Analista:** Visualizar los inicios de sesión de usuarios (`USER_LOGIN`), comparar la proporción de accesos permitidos frente a bloqueados, filtrar únicamente aquellos estados con más de 500 eventos, ordenar de mayor a menor y limitar a los 10 primeros resultados.

```yara
events:
    metadata.event_type = "USER_LOGIN"
    $security_result = security_result.action
    ($security_result = "BLOCK" or $security_result = "ALLOW")

match:
    $security_result

outcome:
    $event_count = count_distinct(metadata.id)

condition:
    $event_count > 500

order:
    $event_count desc

limit: 10
```

---

#### 4. Selección del Tipo de Gráfico y Guardado

Una vez ejecutada y validada la consulta YARA-L:
* La interfaz solicita seleccionar el tipo de visualización idóneo para los datos:
  * Para distribuciones categóricas (como Allow vs. Block): **Gráficos de pastel (*pie charts*)**, **gráficos de dona (*donut charts*)** o **tablas**.
  * Para series temporales: **Gráficos de líneas o barras**.
  * Para métricas singulares: **Mosaicos numéricos (*tiles*)** o **medidores (*gauges*)**.
* Es obligatorio asignar un **Nombre (*Name*)** y una breve descripción explicativa al widget antes de guardarlo en el panel.

---

### Lección 3: Filtrado en Dashboards (*Dashboard Filtering*)

> **Objetivo:** Comprender la importancia estratégica del filtrado interactivo en los paneles de Google SecOps para reducir el ruido analítico, con especial énfasis en el funcionamiento, anclaje (*anchor*) e interpretación de las ventanas temporales relativas (*Relative Time Filters*) frente a las ventanas móviles fijas.

---

#### 1. Propósito y Valor del Filtrado en Dashboards

Un panel de control sin filtros tiende a reflejar la totalidad de la telemetría agregada, lo que dificulta la identificación oportuna de anomalías, picos de tráfico y actividad maliciosa genuina.

* **Beneficios Operativos:**
  * **Eliminación de Ruido:** Permite aislar rápidamente eventos críticos segmentando por dimensiones como tipo de registro (`metadata.log_type`), activo (`asset`), usuario (`user`) o rango de tiempo.
  * **Agilidad en la Toma de Decisiones:** Enfoca la perspectiva del equipo SOC en los activos o identidades bajo investigación activa sin alterar la consulta base del panel.
  * **Interactividad Dinámica:** Los filtros aplicados a nivel de dashboard se propagan instantáneamente sobre todos los widgets que compartan ese campo o dimensión.

---

#### 2. Mecánica de Filtros Temporales Relativos (*Relative Time Filters*)

Los filtros de tiempo relativo calculan la ventana de observación de datos dinámicamente tomando como referencia el momento presente (**"ahora" / *now***). 

> [!IMPORTANT]
> **Concepto Clave: Primer Evento Visto (*First Seen Event*):**  
> En las visualizaciones de Google SecOps, la métrica o etiqueta *First Seen* (primer evento visto) dentro de un panel filtrado **representa la ocurrencia más temprana detectada dentro de la ventana de tiempo seleccionada**, y **NO** la primera vez histórica en que el evento ocurrió en el entorno.

---

#### 3. Comparativa de Filtros de Tiempo Relativo y Anclajes (*Anchors*)

La diferencia entre las opciones de tiempo relativo radica en cómo se define el inicio (ancla de calendario vs. ventana móvil):

| Opción de Filtro Relativo | Tipo de Ventana | Comportamiento del Inicio de la Ventana (*Anchor*) | Comportamiento de "First Seen" |
| :--- | :--- | :--- | :--- |
| **Última Semana (*Last 1 Week*)** | **Anclada al Calendario (*Calendar-anchored*)** | Se ancla al **inicio de la semana actual** (comienza a las 00:00 del domingo o lunes según configuración regional). | El evento más antiguo mostrado estará acotado desde la medianoche del inicio de la semana de calendario en curso hasta el momento actual. |
| **Últimos 7 Días (*Last 7 Days*)** | **Ventana Móvil (*Rolling Window*)** | Ventana fija deslizante de **exactamente 168 horas** hacia atrás desde el instante actual (*now*). | El evento más antiguo se calcula retrocediendo exactamente 7 días naturales desde el momento actual (ej. de miércoles a miércoles). |
| **Último Mes (*Last 1 Month*)** | **Anclada al Calendario (*Calendar-anchored*)** | Se ancla al **día 1 del mes calendario actual** a las 00:00 UTC. | Muestra eventos ocurridos desde el primer día del mes en curso hasta el presente. |
| **Últimas 4 Semanas (*Last 4 Weeks*)** | **Ventana Móvil Extendida (*Rolling 4-Week Period*)** | Ventana deslizante de **28 días continuos** calculados desde el momento actual. | Cubre la totalidad de ocurrencias en un periodo móvil estricto de 4 semanas hacia atrás. |

---

#### 4. Impacto en el Análisis Forense

Comprender si se utiliza una ventana móvil (*rolling*) o una ventana basada en calendario (*calendar-anchored*) previene conclusiones erróneas:
* Un analista que consulte un lunes por la mañana un panel configurado en *Last 1 Week* verá solo pocas horas de telemetría (desde la medianoche previa).
* Para comparar tendencias continuas o investigar incidentes de fin de semana, la configuración correcta es seleccionar **ventanas móviles fijas** como *Last 7 Days* o *Last 24 Hours*.

---

### Lección 4: Funcionalidades Avanzadas de Dashboards Nativos (*Native Dashboards Advanced Functionalities*)

> **Objetivo:** Comprender y configurar las tres funcionalidades analíticas e interactivas avanzadas de los paneles nativos de Google SecOps: acciones de profundización (*Drill Downs* con clic izquierdo y derecho), agrupaciones y tipos de representación visual (*Groupings*), y creación de variables y campos calculados (*Custom Fields*).

---

#### 1. Acciones de Profundización (*Drill Downs*)

Los **Drill Downs** transforman un panel estático en una herramienta de investigación interactiva, permitiendo disparar acciones automáticas cuando un analista hace clic sobre cualquier elemento de un gráfico (celdas de tabla, barras, sectores de pastel, líneas o puntos de dispersión).

* **Doble Interacción Configurable:** Es posible definir comportamientos independientes para el **clic izquierdo (*Left-click*)** y para el **clic derecho (*Right-click*)**.
* **Acciones Disponibles para Drill Downs:**

| Acción de Drill Down | Comportamiento Técnico | Ejemplo Práctico de Uso |
| :--- | :--- | :--- |
| **Ejecutar Búsqueda (*Run Search*)** | Abre una nueva pestaña de Google SecOps con **SIEM Search** precargando una consulta contextual con los valores del elemento seleccionado. | Al hacer clic en un tipo de log específico (ej. `WINDOWS_SYSMON`), abre la búsqueda parametrizada: `metadata.log_type = $log_type`. Incluye botón de prueba inmediata (*Test*). |
| **Aplicar Filtro de Dashboard (*Apply Dashboard Filter*)** | Aplica un filtro interactivo a nivel de todo el panel, restringiendo inmediatamente el resto de widgets a la dimensión cliqueada. | Al hacer clic sobre una IP o un usuario en un gráfico de barras, todos los demás gráficos del panel se filtran para mostrar únicamente la actividad de ese usuario o IP. *(Validable en modo runtime tras guardar).* |
| **Abrir Enlace Externo (*Open External Link*)** | Abre una URL externa preconfigurada en una pestaña independiente del navegador. | Redirigir a guías de uso del esquema UDM, playbooks de respuesta corporativos, documentación en wikis internas o portales de inteligencia de amenazas. |

---

#### 2. Agrupaciones y Configuración de Ejes (*Groupings & Data Settings*)

En la configuración de visualización del widget, los ajustes de datos organizan cómo se desglosa y grafica la información:
* **Campo del Eje X (*X-Axis Field*):** Define la dimensión base o línea temporal (ej. `timestamp_hour` para series por hora).
* **Campo del Eje Y (*Y-Axis Field*):** Define la métrica cuantitativa a medir (ej. `count`, `sum_bytes`).
* **Campo de Agrupación (*Group by Field*):** Segmenta los datos en múltiples series coloreadas según una dimensión categórica (ej. agrupar por `log_type` para ver DNS, Firewall y Sysmon identificados por colores distintos).
* **Tipo de Representación de Grupos (*Group Type*):**
  * **Por Defecto (*Default*):** Muestra las series una al lado de la otra de forma paralela.
  * **Apilado (*Stacked*):** Combina las series verticalmente en una sola barra acumulada, mostrando tanto el volumen total agregado como el aporte proporcional de cada segmento.
  * **Percentil / Proporción (*Percentile*):** Normaliza las series como un porcentaje (100%) sobre el total general, facilitando comparar distribuciones relativas sin importar fluctuaciones de volumen absoluto.

---

#### 3. Campos Personalizados (*Custom Fields*)

Los **Campos Personalizados (*Custom Fields*)** permiten derivar métricas, concatenar valores o aplicar lógica condicional en tiempo de ejecución **sin modificar los registros originales de la base de datos**.

* **Definición en la Sentencia de Filtrado (*Filtering Statement*):**
  * Permite combinar variables de campos UDM mediante funciones de YARA-L antes de la agregación.
  * *Ejemplo:* Concatenar una dirección IP de origen con la IP de destino para generar una clave de flujo de red única (`$ip_pair = strings.concat(principal.ip, " -> ", target.ip)`).
* **Definición en la Sentencia de Resultados (*Outcome Statement*):**
  * Crea nuevas columnas o métricas calculadas (*Outcome Variables*) aplicando operaciones matemáticas, lógicas o de redondeo (`math.round()`, `math.log()`, condicionales `if/else`).
  * Estas variables enriquecen el panel con clasificaciones de riesgo ad-hoc o transformaciones de unidades (como convertir bytes a megabytes o gigabytes).

---

### Lección 5: Dashboards Heredados de SIEM (*SIEM Legacy Dashboards*)

> **Objetivo:** Comprender la arquitectura de los paneles heredados basados en Looker embebido (*Looker-powered Dashboards*), los tres ámbitos de paneles disponibles (Default, Personal, Shared), los flujos de exportación e importación en YAML, las opciones del menú de acciones (incluyendo entregas programadas) y los conjuntos de datos de exploración (*Looker Explores*).

---

#### 1. Contexto Tecnológico y Hoja de Ruta de Migración

Históricamente, la visualización en Google SecOps (tanto en SIEM como en SOAR) se construyó sobre una versión embebida de **Looker** (la plataforma de Business Intelligence adquirida por Google en 2019).
* **Capacidades Históricas:** Ofrecían casi 20 tipos de visualización y modelado avanzado de datos mediante LookML / Explores.
* **Estado Actual y Obsolescencia (*Deprecation*):** Los paneles basados en Looker están siendo descontinuados gradualmente en favor de los **Dashboards Nativos**. Los nuevos paneles nativos eliminan la latencia de intermediación, se integran fluidamente con UDM y YARA-L, y ofrecen una velocidad de carga y ejecución sustancialmente superior.
* **Recomendación:** Se exhorta a todos los clientes a migrar cualquier panel o reporte heredado hacia la arquitectura de dashboards nativos.

---

#### 2. Los Tres Grupos de Dashboards en la Experiencia Heredada

Los dashboards se organizan en tres categorías según su propiedad y alcance de acceso:

| Categoría | Propiedad y Control | Visibilidad y Caso de Uso |
| :--- | :--- | :--- |
| **Paneles Predeterminados (*Default Dashboards*)** | Creados y mantenidos por Google. | Visibles para toda la organización. **Son de solo lectura** (no se pueden editar directamente), pero pueden **duplicarse/copiarse** para personalizarse. |
| **Paneles Personales (*Personal Dashboards*)** | Propiedad exclusiva del usuario autenticado. | **Completamente privados.** Solo el autor puede verlos y modificarlos. Ideales para borradores, experimentos o análisis individuales ad-hoc. |
| **Paneles Compartidos (*Shared Dashboards*)** | Administrados por el equipo u organización. | **Accesibles para todos los usuarios autorizados de la organización.** Ideales para flujos de trabajo del SOC, reportería ejecutiva y métricas operativas compartidas. *(Sujetos a RBAC).* |

---

#### 3. Gestión y Portabilidad con Archivos YAML

Tanto los paneles personales como los compartidos admiten operaciones de ciclo de vida e interoperabilidad:
* **Creación desde Cero o Importación YAML:** Desde el menú **Add**, se puede crear un panel en blanco o importar una definición completa desde un archivo **YAML**.
* **Exportación como YAML:** Permite descargar la estructura completa del dashboard en código YAML para:
  * Control de versiones en repositorios Git (*Dashboards as Code*).
  * Promoción entre entornos (de desarrollo o pruebas a producción).
  * Distribución de plantillas entre distintos tenants u organizaciones.
* **Copia entre Ámbitos:** Es posible promover fácilmente un panel desde el espacio personal hacia el espacio compartido una vez validado.

---

#### 4. Menú de Acciones y Entregas Programadas (*Scheduled Delivery*)

Cada panel heredado cuenta con un menú de acciones contextuales:
* **Actualización y Filtros:** Opción de refresco forzado (*Refresh*) y restablecimiento de filtros a valores por defecto (*Reset Filters*).
* **Descarga de Instantáneas:** Exportación directa del panel en formato **PDF** o extracción de datos de tablas en **CSV**.
* **Entregas Programadas (*Scheduled Delivery*):**
  * Permite automatizar el envío periódico de paneles a partes interesadas sin requerir acceso a la consola.
  * **Configuración:** Frecuencia recurrente (diaria, semanal, mensual), lista de correos destinatarios y formato de salida:
    * Documento **PDF** renderizado.
    * Archivo comprimido **ZIP con CSVs** de los datos.
    * Archivo de imagen (**PNG/JPEG**).

---

#### 5. Conjuntos de Datos de Exploración en Looker (*Looker Explores*)

Los paneles de Looker se construyen consultando conjuntos de datos prediseñados (*Explores*), cada uno optimizado para una faceta de seguridad:

| Conjunto de Datos (*Explore*) | Contenido y Finalidad Técnica |
| :--- | :--- |
| **`UDM Events`** | Datos de eventos UDM sin procesar a nivel granular. Ofrece la máxima flexibilidad analítica. |
| **`UDM Events Aggregates`** | Conteos pre-agregados de eventos UDM sumarizados por hora. Optimizado para consultas de alto rendimiento y tendencias históricas. |
| **`Entity Graph`** | Información contextual enriquecida sobre usuarios, hosts y relaciones topológicas. |
| **`IOC Matches`** | Eventos UDM que coincidieron contra indicadores de compromiso (IoCs) de inteligencia de amenazas. |
| **`Rule Detections`** | Instancias donde reglas de detección personalizadas o activadas generaron al menos una coincidencia. |
| **`Rule Sets with Detections`** | Coincidencias generadas por conjuntos de reglas curadas administradas por Google (*Curated Rules*). |
| **`Ingestion Metrics`** | Métricas operativas sobre tasas de ingesta, volumen de logs, latencia y rendimiento de parsers. |

---

### Lección 6: Comprobación de Conocimientos de Dashboards en SIEM (*SIEM Dashboards: Knowledge Check*)

> **Nota de aprobación requerida:** 75%  
> **Temas evaluados:** Características de los Dashboards Nativos de SecOps, propósito de los Drilldowns, fuentes de datos con ventana de 90 días sin prefijo YARA-L, y definición de Paneles Curados (*Curated Dashboards*).

---

#### Preguntas y Respuestas Técnicas Desarrolladas

#### 1. ¿Cuál es una característica clave de los Dashboards en Google SecOps SIEM (no los dashboards heredados basados en Looker)? (*What is one key characteristic of Dashboards in Google SecOps SIEM - not Legacy Dashboards powered by Looker?*)

* [ ] Solo son accesibles a través de Looker Studio y requieren exportación manual de datos (*They are only accessible through Looker Studio and require manual data export*)
* [ ] Reemplazan toda la funcionalidad de API y no se pueden acceder programáticamente (*They replace all API functionality and cannot be accessed programmatically*)
* [ ] No admiten Data RBAC y están limitados a visibilidad exclusiva para administradores (*They do not support Data RBAC and are limited to admin-only visibility*)
* [x] **Se construyen directamente dentro de SecOps utilizando sintaxis al estilo UDM y funciones YARA-L** (*They are built directly within SecOps using UDM-style syntax and YARA-L functions*)

> **Explicación técnica:** Los nuevos **Dashboards Nativos** de Google SecOps se ejecutan directamente sobre la plataforma sin intermediarios de BI externos (como Looker). Cada widget se fundamenta en consultas escritas en **sintaxis UDM y funciones YARA-L**, ofreciendo compatibilidad inherente con Data RBAC, tiempos de carga rápidos y acceso programático vía API.

---

#### 2. ¿Cuál es el propósito principal de los Drilldowns en los dashboards de Google SecOps? (*What is the main purpose of Drilldowns in Google SecOps dashboards?*)

* [x] **Agregar interacciones del usuario dentro de los gráficos del panel, como ejecutar búsquedas, aplicar filtros o abrir enlaces** (*To add user interactions within dashboard charts, such as running searches, applying filters, or opening links*)
* [ ] Modificar la lógica del parser y los mapeos de campos en los dashboards (*To modify parser logic and field mappings in dashboards*)
* [ ] Programar automáticamente exportaciones de informes desde los dashboards (*To automatically schedule report exports from dashboards*)
* [ ] Configurar permisos de usuario y roles de acceso para los dashboards (*To configure user permissions and access roles for dashboards*)

> **Explicación técnica:** Los **Drilldowns** dotan de interactividad a los paneles al permitir configurar comportamientos sobre los clics (izquierdo y derecho) en elementos visuales de los gráficos. Las tres acciones admitidas son: **Run Search** (abre SIEM Search con una consulta parametrizada), **Apply Dashboard Filter** (aplica un filtro dinámico al resto de los widgets del panel) y **Open External Link** (abre URLs a documentación o playbooks).

---

#### 3. ¿Qué fuente de datos en los Dashboards Nativos de Google SecOps tiene un intervalo de tiempo de consulta de 90 días y no utiliza un prefijo YARA-L? (*Which data source in Google SecOps Native Dashboards has a 90-day query time interval and does not use a YARA-L prefix?*)

* [ ] Ingestion Metrics
* [ ] Rule Sets
* [ ] Detections
* [x] **UDM Events**

> **Explicación técnica:** El conjunto de datos de **Eventos UDM (*UDM Events*)** es la fuente de datos predeterminada (*default*) para los widgets de dashboard, por lo que **no requiere ningún prefijo YARA-L** (a diferencia de `detection.`, `graph.`, `ingestion.` o `soar.`). Asimismo, debido a su volumen granular y rendimiento, las consultas sobre eventos UDM están limitadas a una ventana temporal máxima de **hasta 90 días** (mientras que otras fuentes admiten hasta 365 días).

---

#### 4. ¿Qué describe mejor a los Paneles Curados (*Curated Dashboards*) en Google SecOps? (*What best describes Curated Dashboards in Google SecOps?*)

* [ ] Son plantillas de un solo uso que no se pueden editar ni duplicar (*They are one-time templates that cannot be edited or duplicated*)
* [x] **Son creados por Google, cubren casos de uso de seguridad comunes, y se pueden personalizar y actualizar regularmente con nuevo contenido** (*They are Google-created, cover common security use cases, and can be customized and regularly updated with new content*)
* [ ] Solo están disponibles a través de integraciones del marketplace de terceros (*They are available only through third-party marketplace integrations*)
* [ ] Son creados por clientes y no tienen soporte de Google (*They are created by customers and not supported by Google*)

> **Explicación técnica:** Los **Paneles Curados (*Curated Dashboards*)** son plantillas preconfiguradas y mantenidas directamente por Google que proporcionan visibilidad inmediata out-of-the-box sobre actividades frecuentes de seguridad (tráfico de red, accesos de usuarios, detecciones de amenazas). Se pueden **duplicar libremente para adaptarlos** a los requerimientos específicos de cada organización, y Google amplía y actualiza su catálogo automáticamente a lo largo del tiempo.

---

## Módulo 5: SIEM Detections (Detecciones en SIEM)

### Lección 1: Categorías de Detecciones Curadas, Conjuntos de Reglas y Dependencias (*Curated Detection Categories, Rule Sets, Dependencies*)

> **Objetivo:** Comprender la arquitectura jerárquica de las Detecciones Curadas (*Curated Detections*) desarrolladas y mantenidas activamente por el equipo de inteligencia de amenazas de Google Cloud (GCTI), los niveles de precisión de reglas (*Broad* vs. *Precise*), las dependencias de fuentes de registro y parsers por defecto, y el mecanismo de exclusiones (*Exclusions*) para la supresión de falsos positivos.

---

#### 1. ¿Qué son las Detecciones Curadas (*Curated Detections*)?

Las **Detecciones Curadas** son conjuntos de reglas de detección preconstruidas y listas para usar (*out-of-the-box*), diseñadas, probadas y mantenidas continuamente por el equipo **Google Cloud Threat Intelligence (GCTI)**.
* **Ventaja Estratégica:** Proporcionan cobertura de detección inmediata contra tácticas, técnicas y procedimientos (TTPs) de adversarios modernos e indicadores de compromiso (IoCs) sin que el equipo de seguridad tenga que redactar código de detección desde cero.
* **Mantenimiento Automatizado:** La lógica y los patrones de detección se actualizan y refinan continuamente de forma transparente para los clientes.
* **Acceso en la Consola:** `Detection > Rules & Detections > Curated Detections`.

---

#### 2. Jerarquía Organizativa de las Detecciones Curadas

Las detecciones curadas siguen un modelo estructural en tres niveles:

```
Categoría de Amenaza (Threat Category)
└── Conjunto de Reglas (Rule Set)  <-- [Nivel que habilita el analista]
    └── Regla Individual (Curated Rule: Broad / Precise)
```

##### Detalle de los Tres Niveles:
1. **Categorías de Amenazas (*Threat Categories*):** Agrupaciones de alto nivel según dominios de riesgo o vectores de ataque.
   * *Ejemplos:* `Applied Threat Intelligence` (inteligencia aplicada contra IoCs activos), `Cloud Threats` (amenazas multi-cloud), `Chrome Enterprise Premium Threats` (riesgos en navegador).
   * *Dependencia de Licencia:* La disponibilidad de ciertas categorías avanzadas depende del tipo de licenciamiento de Google SecOps adquirido.
2. **Conjuntos de Reglas (*Rule Sets*):** Colecciones lógicas de reglas orientadas a un objetivo concreto dentro de una categoría (ej. *Active Breach Priority Host Indicators*).
   * **Nivel Operativo de Activación:** **Es la unidad que el analista habilita o deshabilita en la plataforma.**
   * **Dependencia Crítica de Fuentes (*Dependent Log Sources*):** Cada conjunto de reglas especifica fuentes de registro obligatorias (ej. Sysmon, CrowdStrike, Zeek, VPC Flow Logs) que deben estar presentes y normalizadas en SecOps para que las reglas puedan operar.
   * **Dependencia de Parsers por Defecto:** Las reglas curadas asumen y confían estrictamente en los mapeos del esquema UDM provistos por los **parsers por defecto** de Google.
3. **Reglas Curadas Individuales (*Curated Rules*):** Lógica específica de detección en YARA-L (inspeccionable en el *Content Hub*). Se pueden duplicar si se desea crear variantes personalizadas.

---

#### 3. Niveles de Reglas: Precisas (*Precise*) vs. Amplias (*Broad*)

Dentro de cada conjunto de reglas coexisten dos niveles de sensibilidad:

| Nivel de Regla | Mecanismo de Coincidencia | Nivel de Confianza | Tasa de Falsos Positivos | Caso de Uso Recomendado |
| :--- | :--- | :--- | :--- | :--- |
| **Precisas (*Precise*)** | Firmas estrictas, IoCs conocidos validados de alta fidelidad. | **Muy Alto** | Mínima (casi nula). | Generación directa de **Alertas automáticas** e inicio de playbooks de respuesta. |
| **Amplias (*Broad*)** | Detección de patrones heurísticos y comportamiento sospechoso. | Moderado | Mayor potencial de falsos positivos. | Detección de amenazas tempranas o emergentes; requiere revisión analítica manual previa. |

* **Activación Flexible:** Dentro de cada conjunto de reglas se puede activar de forma independiente el estado en vivo (*Live detection*) y la generación de alertas (*Alerting*) para las reglas *Precise*, para las *Broad*, o para ambas.

---

#### 4. Estadísticas del Panel de Curated Detections

La página principal ofrece métricas operativas clave para la gobernanza del SOC:
* **Enabled Rule Sets:** Cantidad total de reglas amplias y precisas en ejecución activa.
* **Most Active Rules:** Reglas individuales que están disparando el mayor volumen de detecciones (con enlaces para pivotar a la vista de eventos).
* **Most Active Rule Sets:** Conjuntos de reglas con mayor actividad consolidada.
* **Capacity Tracking:** Monitoreo del impacto de las reglas activadas sobre la capacidad de procesamiento de la instancia.

---

#### 5. Gestión de Falsos Positivos: Exclusiones (*Exclusions*)

Dado que los conjuntos de reglas curados son de solo lectura y **su código base no puede modificarse directamente**, Google SecOps proporciona el mecanismo de **Exclusiones (*Exclusions*)**.

* **Ruta de Acceso:** `Detection > Rules & Detections > Exclusions`.
* **Propósito:** Aplicar filtros específicos a nivel de campos UDM para suprimir detecciones y evitar alertas innecesarias sobre actividades legítimas conocidas (*Known Good*).
* **Alcance:** Una exclusión puede aplicarse a un **único conjunto de reglas o a múltiples conjuntos de reglas simultáneamente**.
* **Flujo de Creación de una Exclusión:**
  1. Identificar la detección legítima o falso positivo recurrente.
  2. Ir a *Create Extension / Exclusion* y seleccionar los *Rule Sets* afectados.
  3. Definir la condición UDM a suprimir (ej. excluir un hash de archivo seguro en `target.file.sha256` o una IP interna en `principal.ip`).
  4. **Ejecutar Simulación (*Run Simulation*):** La consola simula el impacto histórico (ej. *"Esta exclusión habría eliminado 53 de 330 detecciones pasadas"*).
  5. Confirmar y guardar la exclusión para que entre en vigencia de inmediato.

---

### Lección 2: Construcción de Reglas YARA-L, Estructura y Variables (*YARA-L Rule Construction, Structure, & Variables*)

> **Objetivo:** Comprender el origen y propósito del lenguaje YARA-L (*YARA for Logs*), la navegación al editor de reglas (*Rules Editor*), las tres secciones mínimas obligatorias que componen una regla de detección (`meta`, `events`, `condition`), el formateo de pares clave-valor, y la declaración y referencia de variables de eventos (`$e`).

---

#### 1. ¿Qué es YARA-L? (*YARA for Logs*)

* **Evolución Histórica:** Originalmente derivado del lenguaje de firmas **YARA** (creado por VirusTotal para el análisis y escaneo de malware en archivos ejecutables), Google adaptó su sintaxis flexible para aplicarla sobre **flujos continuos de registros y telemetría de seguridad**. De ahí su nombre: **YARA-L** (donde la **"L"** significa *Logs*).
* **Propósito en Google SecOps:** Es el lenguaje declarativo estándar utilizado para redactar reglas de detección personalizadas (*Custom Detection Rules*), capaces de escanear masivamente eventos normalizados en el modelo UDM en busca de amenazas, comportamientos sospechosos o violaciones de políticas corporativas.
* **Ruta de Navegación en la Consola:** `Detection > Rules & Detections > Rules Editor`.

---

#### 2. Anatomía de una Regla YARA-L: Las 3 Secciones Obligatorias

Toda regla válida en YARA-L comienza con su identificador de nombre único y requiere estrictamente **tres secciones obligatorias**:

```
rule [nombre_de_la_regla] {
    meta:
        // 1. Metadatos descriptivos (autor, severidad, descripción, TTPs)
    events:
        // 2. Criterios y lógica de coincidencia sobre eventos UDM
    condition:
        // 3. Condición booleana de activación para disparar la detección
}
```

---

#### 3. Desglose de las Secciones Obligatorias

##### A. Sección de Metadatos (`meta:`)
* **Propósito:** Proporciona contexto documental libre sobre la regla para los analistas que investigan alertas en la consola (*Rules Dashboard*).
* **Sintaxis de Pares Clave-Valor (`clave = "valor"`):**
  * **La Clave (*Key*):** No lleva comillas ni espacios (se utiliza guion bajo si se requieren palabras compuestas, ej. `mitre_attack_technique = "T1078"`).
  * **El Valor (*Value*):** **Siempre debe estar encerrado entre comillas dobles (`"..."`)**.
* **Claves Estandarizadas del Sistema (*Hard-coded Keys*):**  
  Existen claves reservadas que SecOps interpreta automáticamente para poblar los encabezados y filtros de la interfaz:
  * `author = "Nombre o Equipo"` (Creador de la regla).
  * `description = "Texto descriptivo"` (Explica qué amenaza detecta; se visualiza al pasar el cursor sobre el nombre de la regla).
  * `severity = "CRITICAL" | "HIGH" | "MEDIUM" | "LOW" | "INFORMATIONAL"` (Nivel de severidad para priorización en el SOC).
* *Otras claves recomendadas:* `version`, `mitre_attack_technique`, `reference_url`, `data_source`.

##### B. Sección de Eventos (`events:`)
* **Propósito:** Define la lógica nuclear de detección. Funciona de manera análoga a la cláusula `WHERE` de SQL, especificando las condiciones que deben cumplir los eventos UDM para ser capturados.
* **Declaración de Variables de Evento:**  
  Cada evento evaluado debe asignarse a una variable de evento con el prefijo de signo de dólar (típicamente `$e`, pero puede asignarse cualquier identificador representativo, ej. `$login_event` o `$process_event`).
  * *Ejemplo:* `$e.metadata.event_type = "USER_LOGIN"`
* **Operador `AND` Implícito:** Cada nueva línea dentro de la sección `events` asume implícitamente un operador lógico **`AND`**, salvo que se indique explícitamente `OR` o paréntesis de agrupación.

##### C. Sección de Condición (`condition:`)
* **Propósito:** Especifica la condición booleana final que debe evaluarse como verdadera para que la regla genere formalmente una detección (*Detection Trigger*).
* **Referencia a Variables:** Debe apuntar a la variable de evento definida en la sección `events`.
* **Regla de Evento Único Básica:**  
  Si la sección `events` utiliza la variable `$e`, la condición mínima es:
  ```yara
  condition:
      $e
  ```
  Esto indica: *"Genera una detección siempre que exista al menos un evento que cumpla todos los criterios asignados a `$e`"*.

---

#### 4. Ejemplo Práctico Completo: Regla de Detección Básica

**Escenario:** Detectar inicios de sesión exitosos en Microsoft Office 365 originados desde sistemas operativos Mac OS.

```yara
rule office365_mac_system_login {
    meta:
        author = "SOC Detection Engineering"
        description = "Detects user logins into Office 365 originating from Mac OS systems"
        severity = "LOW"
        mitre_technique = "T1078"

    events:
        $e.metadata.vendor_name = "Microsoft"
        $e.metadata.product_name = "Office 365"
        $e.metadata.event_type = "USER_LOGIN"
        $e.principal.platform = "MAC"
        $e.security_result.action = "ALLOW"

    condition:
        $e
}
```

* **Comportamiento en Ejecución:**  
  El motor de detección evalúa continuamente el flujo de eventos UDM. Cuando llega un log que cumple simultáneamente con las cinco condiciones asignadas a `$e`, la sección `condition: $e` evalúa a verdadero y genera una detección categorizada con severidad `LOW` y documentada con la descripción y técnica MITRE definidas en `meta`.

---

### Lección 3: Coincidencia por Regex, Listas de Referencia / Tablas de Datos y Campos Repetidos (*Regex Matching, Reference Lists / Data Tables, & Repeated Fields*)

> **Objetivo:** Dominar las técnicas avanzadas de coincidencia de patrones en YARA-L utilizando expresiones regulares (método en línea vs. función `re.regex`), el tratamiento de campos repetidos (*Repeated Fields*) mediante los cuantificadores `any`, `all` y sus negaciones lógicas, y la integración de Tablas de Datos (*Data Tables*, reemplazo moderno de las Listas de Referencia) en las reglas de detección.

---

#### 1. Coincidencia por Expresiones Regulares en YARA-L

Google SecOps ofrece dos métodos para aplicar expresiones regulares seguras (sintaxis RE2) dentro de la sección `events`:

| Método de Expresión Regular | Sintaxis | Ventajas y Uso Técnico |
| :--- | :--- | :--- |
| **Método En Línea (*Inline Method*)** | `$e.campo = /patrón/` | Se compara el campo directamente contra el patrón delimitado por **barras inclinadas (`/ /`)**. Es la forma más compacta y legible. Ej: `$e.principal.user.userid = /.*admin.*/` |
| **Función Explícita (*Function Method*)** | `re.regex($e.campo, `patrón`)` o `re.regex($e.campo, "patrón")` | Se invoca la función `re.regex()`. Admite dos delimitadores:<br>• **Comillas invertidas (\`...\`):** Permite escribir expresiones limpias **sin necesidad de escapar barras invertidas** (recomendado para rutas Windows o regex complejas).<br>• **Comillas dobles (`"..."`):** Requiere escapar caracteres con doble barra invertida (`\\`). |

---

#### 2. Tratamiento de Campos Repetidos (*Repeated Fields*)

En el esquema UDM, existen campos que pueden contener múltiples valores simultáneos dentro de un mismo evento (por ejemplo, en un correo electrónico los campos `target.user.email_addresses`, `network.email.to`, `network.email.cc` o `network.email.bcc`; o en un host multitarjeta el campo de IPs repetidas).

Para evaluar estos arrays sin ambigüedades, YARA-L introduce los cuantificadores **`any`** y **`all`**:

* **Regla de Sintaxis Obligatoria:** Los cuantificadores `any` y `all` **deben colocarse inmediatamente antes de la variable del evento**; de lo contrario, el compilador emitirá un error de sintaxis:
  ```yara
  // Correcto:
  any $e.network.email.to = /.*@example\.com/

  // Incorrecto (fallo de sintaxis):
  $e.network.email.to = any /.*@example\.com/
  ```

##### Comportamiento de `any` vs. `all`:
* **`any $e.campo`:** La condición se evalúa como verdadera si **al menos uno** de los valores del campo repetido coincide con el patrón especificado.
* **`all $e.campo`:** La condición se evalúa como verdadera únicamente si **todos y cada uno** de los valores del campo repetido coinciden con el patrón.

---

#### 3. Negaciones Lógicas en Campos Repetidos: `not all` vs. `all !=`

La combinación de operadores de negación sobre campos repetidos tiene implicaciones lógicas sutiles pero críticas:

| Expresión Lógica | Regla de Evaluación | Ejemplo con destinatarios: `["Jane", "John", "Doug"]` evaluando contra `"Jane"` |
| :--- | :--- | :--- |
| **`not all $e.campo = "valor"`** | Se cumple si **al menos uno** de los valores repetidos es diferente del valor indicado. | **VERDADERO / COINCIDE:** Dado que John y Doug no son Jane, no todos son Jane. |
| **`all $e.campo != "valor"`** | Se cumple únicamente si **absolutamente todos** los valores repetidos son distintos del valor indicado. | **FALSO / NO COINCIDE:** Como la lista contiene a Jane, la condición falla porque existe al menos una coincidencia. |

---

#### 4. Integración de Tablas de Datos (*Data Tables*) en Reglas YARA-L

Las **Data Tables** son las sucesoras modernas de las *Reference Lists* tradicionales. Funcionan como tablas relacionales multicolumna integradas:
* **Inmutabilidad de Encabezados:** La fila de encabezados y los tipos de datos de las columnas quedan bloqueados tras el guardado inicial; solo se pueden editar, agregar o eliminar las filas de datos inferiores.
* **TTL (Time to Live):** Las filas pueden expirar automáticamente (útil para listas dinámicas de IoCs).
* **Referencia en YARA-L:**
  * Se identifican con el prefijo de porcentaje (`%`): `%nombre_de_la_tabla.nombre_columna`.
  * **Operador `in`:** Comprueba si el valor de telemetría reside en la columna especificada:
    ```yara
    $e.principal.user.email_address in %watch_list_empleados.email%
    ```
  * **Operador `not in`:** Excluye eventos si el valor existe en la columna (ideal para listas de permitidos/exclusiones):
    ```yara
    $e.target.process.file.full_path regex in %procesos_sospechosos.patron_ruta%
    ```

---

### Lección 4: Funciones YARA-L (*YARA-L Functions*)

> **Objetivo:** Comprender las diversas familias de funciones disponibles en el motor YARA-L de Google SecOps para manipular cadenas, realizar cálculos matemáticos y agregaciones, extraer componentes temporales, aplicar lógica condicional (`if`), manipular expresiones regulares (`re.capture`, `re.replace`), manejar colecciones de arrays (`array`, `array_distinct`) y consultar métricas de comportamiento histórico precomputadas (*Metrics Functions*).

---

#### 1. Funciones de Manipulación de Cadenas (*String Functions*)

Permiten transformar, limpiar y concatenar atributos de texto para inspección o para enriquecer el resultado de las alertas:

| Función | Sintaxis / Uso | Descripción y Ejemplo de Aplicación |
| :--- | :--- | :--- |
| **`strings.concat`** | `strings.concat(val1, val2, ...)` | Combina múltiples valores o cadenas literales en un único string coherente. Útil para crear claves compuestas (ej. unir usuario y dominio). |
| **`strings.coalesce`** | `strings.coalesce(campo1, campo2, "fallback")` | Evalúa una lista de campos en orden secuencial y **retorna el primer valor no nulo / no vacío**. Ideal para lidiar con telemetría heterogénea donde el usuario puede venir en `userid` o en `email`. |
| **`strings.to_upper`** | `strings.to_upper(campo)` | Convierte todos los caracteres de una cadena a mayúsculas. |
| **`strings.to_lower`** | `strings.to_lower(campo)` | Convierte todos los caracteres de una cadena a minúsculas, asegurando comparaciones consistentes. |

---

#### 2. Funciones Matemáticas y de Recuento (*Math & Aggregations*)

* **`math.min()` y `math.max()`:** Encuentran el valor mínimo o máximo dentro de una serie de números. En marcas temporales, `min(event.timestamp)` determina el **primer evento** de una secuencia, y `max(event.timestamp)` el **último evento**.
* **`math.round()`:** Redondea valores numéricos con decimales al entero más próximo (o al número de decimales deseado) para generar puntuaciones o métricas legibles.
* **`count()`:** Cuantifica el total de ocurrencias observadas de un campo (típicamente `count($e.metadata.id)` para contar el número total de eventos capturados).
* **`count_distinct()`:** Cuenta exclusivamente la cantidad de valores **únicos** de un campo determinado (ej. `count_distinct($e.principal.ip)` para detectar conexiones desde múltiples direcciones IP distintas).

---

#### 3. Funciones de Marca Temporal (*Timestamp Functions*)

La telemetría en Google SecOps se indexa en segundos transcurridos desde el Unix Epoch (1 de enero de 1970 UTC). YARA-L proporciona funciones de tiempo para correlaciones horarias:
* **`timestamp.current_seconds()`:** Devuelve la hora actual en segundos Unix Epoch al momento de ejecutarse la regla.
* **`timestamp.get_date(segundos)`:** Extrae la fecha en formato civil estándar (`YYYY-MM-DD`).
* **`timestamp.get_timestamp(segundos, [zona_horaria])`:** Extrae la fecha y hora completa (`YYYY-MM-DD HH:MM:SS`), permitiendo opcionalmente especificar desplazamientos de zona horaria (ej. `"-05:00"`).
* **`timestamp.get_hour()`, `timestamp.get_day()`:** Permiten aislar la hora o día de la semana para detectar actividades fuera del horario laboral o durante fines de semana.

---

#### 4. Lógica Condicional (`if`) y Puntuación de Severidad Dinámica

La sentencia `if` permite bifurcar la lógica y asignar dinámicamente variables basándose en el cumplimiento de una condición booleana:

```yara
$account_type = if($e.principal.user.account_type != "DOMAIN_ACCOUNT", "LOCAL_ACCOUNT", $e.principal.user.account_type)
```

* **Encadenamiento y Cálculo de Riesgo:** Se pueden anidar múltiples cláusulas `if` con funciones matemáticas (como `math.max`) para calcular dinámicamente un **Score de Alerta (*Risk Score*)**, elevando la prioridad de la alerta si el activo es crítico o si el comando incluyó parámetros maliciosos.

---

#### 5. Funciones Avanzadas de Expresiones Regulares (`re.*`)

* **`re.regex($campo, /patrón/)`:** Evalúa una coincidencia booleana (`true` / `false`).
* **`re.capture($campo, /patrón_con_grupo/)`:** **Extrae** una subcadena específica de un campo mediante grupos de captura `( )` y la asigna a una nueva variable para su uso en la regla o en la alerta.
* **`re.replace($campo, /patrón/, "reemplazo")`:** Reemplaza partes de un valor por otro texto.  
  * *Caso de uso en SOC (Desarmado de URLs maliciosas):* Desactivar enlaces maliciosos reemplazando puntos por corchetes (`example[.]com`) para evitar clics accidentales de analistas en la consola.

---

#### 6. Funciones de Arrays: `array` vs. `array_distinct`

Cuando se correlacionan múltiples eventos o se opera sobre campos repetidos, estas funciones consolidan los valores coincidentes en una variable de lista:
* **`array($campo)`:** Almacena todos los valores encontrados a lo largo de los eventos, **permitiendo duplicados**.
* **`array_distinct($campo)`:** Almacena los valores encontrados pero **retiene únicamente los elementos únicos**, descartando repeticiones. Esencial en la sección `outcome` para listar los usuarios o destinos afectados sin redundancia.

---

#### 7. Funciones de Métricas de Comportamiento Histórico (*Metrics Functions*)

Permiten a las reglas YARA-L consultar **líneas base históricas de comportamiento precomputadas** por la plataforma, comparando la actividad actual del usuario o dispositivo contra su historial en ventanas de tiempo prolongadas (ej. 30 días).

##### Parámetros Obligatorios de una Función de Métrica:
1. **`period`:** Intervalo en el que se agrupan las observaciones individuales (ej. `1d` = 1 día).
2. **`window`:** Ventana de tiempo histórico completa sobre la cual se agrega la métrica (ej. `30d` = 30 días históricos).
3. **`metric`:** Tipo de cálculo precomputado a consultar (ej. `event_count_sum` para cuantificar intentos de autenticación históricos).
4. **`agg` (Agregación sobre la ventana):** Operación de agregación sobre la ventana histórica (ej. `max`, para obtener el valor diario máximo observado en los 30 días).
5. **`filter` (Opcional):** Filtro numérico o condicional previo sobre los datos precomputados.
6. **`udm_field` (Dimensión de Cruce):** Campo UDM que actúa como clave de enlace (ej. `principal.user.userid` para vincular el evento actual con el historial del mismo usuario).

---

### Lección 5: Secciones Opcionales de YARA-L: Match, Outcome y Options (*Optional Sections: Match, Outcome, Options*)

> **Objetivo:** Dominar las tres secciones opcionales de YARA-L (`match`, `outcome`, `options`), comprendiendo cómo la sección `match` permite la correlación temporal y la agrupación de eventos (*hop window*), cómo la sección `outcome` enriquece las alertas e inyecta la variable especial `risk_score`, y cómo la sección `options` gestiona valores vacíos (`allow_zero_values`) y ventanas de supresión de alertas (*suppression_window*).

---

#### 1. Sección de Coincidencia y Correlación Temporal (`match:`)

La sección `match` agrupa los eventos que comparten una o más variables y define una **ventana temporal estricta** para evaluar la correlación (similar a un `GROUP BY` con ventana temporal en streaming):

* **Sintaxis Estándar:**
  ```yara
  match:
      $variable_pivote over 30m
  ```
  *(La ventana temporal puede expresarse en minutos `m`, horas `h` o días `d`).*
* **Propósito Operativo:**
  * Permite detectar patrones complejos distribuidos en el tiempo (ej. *"5 intentos fallidos de login seguidos de 1 exitoso del mismo usuario en menos de 10 minutos"*).
  * Es opcional para reglas de evento único, pero **estrictamente obligatoria** para reglas de múltiples eventos (*Multi-event rules*).
* **Consolidación de Alertas:** En lugar de disparar una alerta aislada por cada log recibido, el motor agrupa todos los eventos coincidentes del mismo pivote dentro de la ventana de tiempo en una **única detección consolidada**.

---

#### 2. Sección de Resultados y Enriquecimiento Contextual (`outcome:`)

La sección `outcome` se utiliza para extraer datos clave de los eventos analizados y añadirlos directamente a los metadatos de la alerta generada:

* **Visibilidad Directa en la Consola:** Las variables definidas en el `outcome` se exponen en la interfaz de alertas (*Alerts & IOCs*), en dashboards y como parámetros de entrada para playbooks de SOAR.
* **Reglas Obligatorias de Sintaxis en `outcome`:**
  1. **Nombres Únicos:** Cada variable de resultado debe tener un nombre de variable único (ej. `$total_events`, `$distinct_users`).
  2. **Uso de Funciones de Agregación:** Al referenciar campos UDM de eventos (especialmente si hay sección `match`), **es obligatorio aplicar funciones de agregación** (`count`, `count_distinct`, `array`, `array_distinct`, `max`, `min`, `sum`), debido a que la regla puede estar procesando múltiples registros para un mismo grupo.
* **Filtrado en `condition`:** Las variables calculadas en `outcome` pueden utilizarse en la sección `condition` para establecer umbrales numéricos de activación (ej. `condition: $event_count > 5`).

---

#### 3. Puntuación de Riesgo Dinámica: Variable Especial `risk_score`

`risk_score` es una variable entera reservada de Google SecOps utilizada para la priorización cuantitativa de incidentes:
* Se calcula dinámicamente en la sección `outcome` combinando operadores matemáticos y sentencias `if`:
  ```yara
  outcome:
      $risk_score = max(
          if($e.principal.asset.criticality = "HIGH", 85, 30) +
          if($e.security_result.action = "ALLOW", 15, 0)
      )
  ```
* Fluye directamente hacia los algoritmos de análisis de comportamiento de usuarios y entidades (UEBA) y determina la severidad final en la cola de triaje del analista.

---

#### 4. Sección de Opciones de Regla (`options:`)

La sección `options` ajusta el comportamiento operativo y el motor de ejecución de la regla. Cuenta con dos configuraciones fundamentales:

| Opción | Tipo / Valor | Comportamiento Técnico y Caso de Uso |
| :--- | :--- | :--- |
| **`allow_zero_values`** | `true` \| `false` | **Por defecto es `false`:** Una regla no dispara detecciones si las variables del `match` vienen vacías o nulas.<br>**Al fijarse en `true`:** Fuerza la activación de la regla incluso si algunos campos del `match` carecen de valor (crucial cuando la **ausencia de datos** es en sí misma un síntoma de evasión o anomalía). |
| **`suppression_window`** | Valor numérico (minutos) | Controla la frecuencia con la que una regla puede disparar alertas repetidas para la misma entidad.<br>**Requiere una clave de supresión (`suppression_key`):** Se define en la sección `outcome` (ej. `$suppression_key = $user_id`). Evita inundar al SOC con miles de alertas duplicadas ante un mismo ataque sostenido. |

---

#### 5. Ejemplo Práctico Integrado con las 6 Secciones de YARA-L

```yara
rule multiple_failed_logins_targeted_account {
    meta:
        author = "SOC Detection Engineering"
        description = "Detects multiple failed logins on the same account within 15 minutes"
        severity = "MEDIUM"

    events:
        $e.metadata.event_type = "USER_LOGIN"
        $e.security_result.action = "BLOCK"
        $user = $e.target.user.userid

    match:
        $user over 15m

    outcome:
        $failed_attempts = count_distinct($e.metadata.id)
        $source_ips = array_distinct($e.principal.ip)
        $risk_score = max(if($failed_attempts > 10, 80, 50))
        $suppression_key = $user

    condition:
        $failed_attempts >= 5

    options:
        allow_zero_values = false
        suppression_window = 60
}
```

---

### Lección 6: Reglas de Evento Único (*Single Event Rule*)

> **Objetivo:** Comprender la arquitectura, ciclo de vida y diseño de una regla de detección de evento único (*Single Event Rule*) en Google SecOps, analizando la aplicación exclusiva de las secciones obligatorias (`meta`, `events`, `condition`), el uso de buenas prácticas contra valores vacíos (`!= ""`) y el flujo de detección individual log-a-log en tiempo real.

---

#### 1. ¿Qué es una Regla de Evento Único (*Single Event Rule*)?

Una **Regla de Evento Único** evalúa cada registro entrante de forma individual e independiente.
* **Mecanismo de Disparo:** En el momento exacto en que un registro normalizado individual cumple simultáneamente con todos los criterios definidos en la sección `events`, la regla evalúa a verdadero y genera inmediatamente una detección.
* **Ausencia de `match`:** No requiere agrupar registros a lo largo del tiempo ni correlacionar múltiples eventos.
* **Estructura Mínima:** Se compone exclusivamente de las tres secciones obligatorias:
  1. `meta:` Metadatos descriptivos (autor, severidad, descripción).
  2. `events:` Criterios UDM asignados a una única variable de evento (típicamente `$e`).
  3. `condition:` Referencia directa a la variable de evento (`condition: $e`).

---

#### 2. Requisitos Previos para el Éxito de las Reglas

1. **Normalización Consistente:** Los registros deben ser analizados y transformados adecuadamente en campos UDM por los parsers de la plataforma.
2. **Conocimiento del Esquema UDM:** El analista debe conocer con exactitud en qué familias de campos (`principal`, `target`, `metadata`, `security_result`) se ubica la información relevante de cada tecnología.

---

#### 3. Buena Práctica Crítica: Manejo de Cadenas Vacías (`!= ""`)

Al filtrar por campos de texto que deben excluir un valor específico (por ejemplo, buscar accesos provenientes de fuera de un país determinado):

> [!WARNING]
> **El Riesgo de Falsos Positivos por Valores Vacíos:**  
> Si se define una condición de exclusión simple como:
> ```yara
> $e.principal.ip_geo_artifact.country_or_region != "United States"
> ```
> La condición evaluará a verdadero **no solo para países extranjeros**, sino también para **cualquier registro donde el campo de geolocalización esté en blanco, sea nulo o no haya podido ser resuelto**.
> 
> **La Solución Estándar (Doble Condición):**  
> Se debe validar explícitamente que el campo no esté vacío:
> ```yara
> $e.principal.ip_geo_artifact.country_or_region != ""
> $e.principal.ip_geo_artifact.country_or_region != "United States"
> ```

---

#### 4. Caso de Uso y Construcción Paso a Paso

**Escenario Operativo:** Una organización opera exclusivamente dentro de los Estados Unidos. Se requiere una regla que detecte de inmediato cualquier inicio de sesión de usuario exitoso originado desde cualquier país extranjero a través de todas las fuentes de registro disponibles.

```yara
rule user_login_from_outside_the_us {
    meta:
        author = "SOC Team"
        description = "Detects successful user logins originating from outside the United States"
        severity = "MEDIUM"

    events:
        // 1. Filtrar únicamente eventos de inicio de sesión de usuario
        $e.metadata.event_type = "USER_LOGIN"

        // 2. Verificar que el inicio de sesión fue exitoso/permitido
        $e.security_result.action = "ALLOW"

        // 3. Buena práctica: el campo geográfico no debe estar en blanco
        $e.principal.ip_geo_artifact.country_or_region != ""

        // 4. Asegurar que el país de origen no sea Estados Unidos
        $e.principal.ip_geo_artifact.country_or_region != "United States"

    condition:
        $e
}
```

* **Clasificación en la Consola:** Al compilar y guardar esta regla en el *Rules Editor*, la plataforma asigna automáticamente el tipo **Single Event**, optimizando su ejecución en memoria para inspección en tiempo real evento por evento.

---

### Lección 7: Reglas de Múltiples Eventos (*Multiple Event Rule*)

> **Objetivo:** Comprender el diseño, sintaxis y casos de uso de las Reglas de Múltiples Eventos (*Multiple Event Rules*) en Google SecOps, analizando la correlación de secuencias temporales, el uso obligatorio de la sección `match` con ventanas de tiempo (*sliding* vs. *hop windows*), la declaración de variables de eventos múltiples, y el conteo de ocurrencias mediante el prefijo `#` en la sección `condition`.

---

#### 1. ¿Por qué Reglas de Múltiples Eventos?

En investigaciones de seguridad reales, las actividades adversarias rara vez se manifiestan en un único log aislado; suelen abarcar secuencias de eventos distribuidas a lo largo del tiempo (por ejemplo, escaneos de puertos, ataques de fuerza bruta, movimiento lateral o escalada de privilegios).
* **De Palabras a Frases Completas:** Mientras que una regla de evento único detecta un término puntual (ej. *"login desde el extranjero"*), una regla de múltiples eventos describe un comportamiento contextual complejo (ej. *"tres intentos fallidos de login seguidos de uno exitoso en menos de 5 minutos"*).
* **Consolidación:** Agrupa la secuencia en una **única detección consolidada** vinculada a la entidad investigada.

---

#### 2. Requisitos Obligatorios en Reglas de Múltiples Eventos

1. **Variables de Eventos Múltiples:** La sección `events` debe declarar al menos dos variables de eventos distintas (ej. `$fail` para fallos y `$success` para éxitos) o referenciar una misma variable correlacionada con umbrales en `condition`.
2. **Variable de Enlace / Pivote:** Los eventos deben compartir al menos una variable común de entidad (ej. `$user` o `$ip`) para evitar mezclar actividades de diferentes cuentas o dispositivos.
3. **Sección `match:` Obligatoria:** Debe definir el campo pivote y una **ventana de tiempo explícita** (`over <duración>`).
4. **Todas las Variables en `condition:`:** Toda variable de evento declarada en `events` **debe ser referenciada explícitamente en la sección `condition`**.

---

#### 3. Ventanas de Correlación Temporal: Ventana Deslizante (*Sliding*) vs. Ventana Salto (*Hop*)

| Tipo de Ventana Temporal | Mecanismo y Palabras Clave | Ventajas y Caso de Uso Típico |
| :--- | :--- | :--- |
| **Ventana Deslizante (*Sliding Window*)** | Utiliza palabras clave como **`before`** o **`after`** en la sección `match` (ej. `$event_a over 10m before $event_b`). | Exige un orden temporal secuencial estricto. Ideal para eventos infrecuentes o donde el orden de llegada de los logs determina la malicia. |
| **Ventana Salto / Fija (*Hop Window*)** | Agrupa todos los eventos ocurridos dentro de un bloque temporal fijo (ej. `$user over 5m`). | **Altamente optimizada para rendimiento masivo.** La secuencia temporal estricta se garantiza mediante comparaciones de timestamps en `events` (`$event_b.metadata.event_timestamp.seconds > $event_a.metadata.event_timestamp.seconds`). |

---

#### 4. Conteo de Eventos en la Sección `condition`: El Operador `#`

Para evaluar la frecuencia o umbral de ocurrencia de un evento dentro de la ventana de tiempo, YARA-L introduce el cuantificador de recuento con el símbolo almohadilla/numeral (**`#`**):

* **Sintaxis:** `#variable_evento >= N`
* **Significado:** Indica el recuento numérico de eventos individuales capturados bajo esa variable dentro del período definido en `match`.
* *Ejemplo:* `#fail >= 3 and #success >= 1` exige que se hayan registrado al menos 3 eventos de fallo y al menos 1 evento de éxito para esa misma entidad en la ventana de tiempo.

---

#### 5. Caso de Uso Práctico Completo: Detección de Ataque de Fuerza Bruta Exitoso

**Escenario Operativo:** Detectar si un usuario experimenta **3 o más inicios de sesión fallidos** y posteriormente logra **1 inicio de sesión exitoso** en una ventana de **5 minutos**, todo ello ocurriendo desde fuera de los Estados Unidos.

```yara
rule multiple_failed_logins_followed_by_success_outside_us {
    meta:
        author = "SOC Detection Engineering"
        description = "Detects 3+ failed logins followed by a successful login outside the US within 5 minutes"
        severity = "HIGH"
        mitre_technique = "T1110"

    events:
        // 1. Definición del evento de fallo (Bloqueado)
        $fail.metadata.event_type = "USER_LOGIN"
        $fail.security_result.action = "BLOCK"
        $fail.principal.ip_geo_artifact.country_or_region != ""
        $fail.principal.ip_geo_artifact.country_or_region != "United States"
        $user = $fail.target.user.userid

        // 2. Definición del evento de éxito (Permitido) para el mismo usuario
        $success.metadata.event_type = "USER_LOGIN"
        $success.security_result.action = "ALLOW"
        $success.principal.ip_geo_artifact.country_or_region != ""
        $success.principal.ip_geo_artifact.country_or_region != "United States"
        $user = $success.target.user.userid

        // 3. Garantizar la secuencia cronológica: el éxito ocurre DESPUÉS del fallo
        $success.metadata.event_timestamp.seconds > $fail.metadata.event_timestamp.seconds

    match:
        // Agrupar por la cuenta de usuario afectada en una ventana de 5 minutos
        $user over 5m

    condition:
        // Requerir al menos 3 eventos de fallo y al menos 1 de éxito
        #fail >= 3 and #success >= 1
}
```

* **Interpretación del Motor de Reglas:**  
  Al guardar la regla, la consola la clasifica como **Multi Event**. SecOps abre una ventana de correlación de 5 minutos por cada usuario único observado con intentos fallidos fuera de EE.UU. Si dentro de ese lapso se acumulan tres o más fallos y se produce un acceso permitido posterior, se dispara una única alerta consolidada de severidad `HIGH`.

---

### Lección 8: Comparativa: Evento Único vs. Múltiples Eventos (*Single Event vs. Multi-Event Rules*)

> **Objetivo:** Analizar en profundidad las diferencias sintácticas, arquitectónicas y operativas entre las Reglas de Evento Único y las Reglas de Múltiples Eventos en Google SecOps, determinando criterios de selección técnica para el diseño de una estrategia de detección en capas (*Layered Detection Strategy*).

---

#### 1. Comparativa de Sintaxis y Estructura en YARA-L

| Elemento de la Regla | Reglas de Evento Único (*Single Event*) | Reglas de Múltiples Eventos (*Multi-Event*) |
| :--- | :--- | :--- |
| **Sección `events:`** | Contiene **exactamente una variable de evento** (típicamente `$e`). Evalúa un log a la vez. | Puede contener **una o múltiples variables de evento** (ej. `$fail`, `$success`), permitiendo evaluar diferentes fuentes o acciones simultáneas. |
| **Sección `match:`** | **Opcional.** No suele utilizarse porque no se requiere correlación temporal. | **ESTRICTAMENTE OBLIGATORIA.** Debe definir el campo de enlace de entidad y la ventana temporal (`$pivote over <tiempo>`). |
| **Sección `condition:`** | Solo puede referenciar la **única variable de evento** (`condition: $e`). | Combina múltiples variables y recuentos mediante operadores lógicos y cuantitativos (ej. `#fail >= 3 and #success >= 1`). |

---

#### 2. Matriz de Características Técnicas y Operativas

| Característica | Reglas de Evento Único (*Single Event*) | Reglas de Múltiples Eventos (*Multi-Event*) |
| :--- | :--- | :--- |
| **Velocidad de Ejecución** | **Tiempo Casi Real (*Near Real-Time - NRT*):** Se evalúan en memoria en el instante exacto en que el log es ingerido y normalizado. | **Basada en Ventana (*Window-based*):** Se evalúan y activan una vez que transcurre la ventana temporal o se completa la secuencia observada. |
| **Criterio de Activación (*Trigger*)** | Un **único registro de log aislado**. | Un **patrón, secuencia o umbral acumulativo** a través de múltiples registros. |
| **Mejor Caso de Uso (*Best Use*)** | **Indicadores atómicos y directos:** Detección de hashes maliciosos, accesos desde IPs en listas negras (IoCs conocidos), o ejecución de comandos prohibidos puntuales. | **Comportamientos y contexto (*Behavioral / Contextual*):** Ataques de fuerza bruta, movimiento lateral, exfiltración masiva de datos, persistencia en endpoints. |
| **Complejidad de Diseño** | **Baja:** Reglas simples y directas de escribir y mantener. | **Moderada a Alta:** Requiere definir pivotes adecuados, ventanas temporales afinadas y ordenamiento de secuencias. |
| **Riesgo de Falsos Positivos** | **Mayor riesgo:** Al carecer de contexto temporal o correlativo, actividades legítimas benignas pueden disparar alertas accidentales. | **Menor riesgo:** La combinación de múltiples señales contextuales reduce significativamente el ruido y eleva la fidelidad de la alerta. |
| **Ejemplo Típico de SOC** | Coincidencia de una IP con una lista de bloqueo externa (*Blacklist hit*). | 5 intentos de autenticación denegados seguidos de un inicio de sesión exitoso en menos de 10 minutos (*Brute Force Success*). |

---

#### 3. Criterio de Selección para el Ingeniero de Detección

Ambos tipos de reglas no compiten entre sí, sino que se complementan en una arquitectura de defensa en profundidad:
* **Utilice Evento Único si:** La acción es intrínsecamente maliciosa por sí misma (ej. creación de un usuario administrador local no autorizado, ejecución de `mimikatz.exe` o coincidencia con un hash de ransomware).
* **Utilice Múltiples Eventos si:** La acción solo es sospechosa en función de su **frecuencia, volumen o secuencia** respecto a otros eventos (ej. 1 fallo de contraseña es habitual; 50 fallos en 2 minutos seguidos de escalada de privilegios es un incidente de seguridad crítico).

---

### Lección 9: Resumen de Reglas Compuestas (*Composite Rules Overview / Rule Chaining*)

> **Objetivo:** Comprender el concepto y la arquitectura de las Reglas Compuestas (*Composite Detections*) o Encadenamiento de Reglas (*Rule Chaining*), la función de las Reglas Productoras (*Producer / Input Rules*), el esquema de detección (*Detection Schema*) y la correlación multinivel para reducir el cansancio por alertas (*alert fatigue*).

---

#### 1. ¿Qué son las Reglas Compuestas o Encadenamiento de Reglas (*Rule Chaining*)?

El **Encadenamiento de Reglas (*Rule Chaining*)** o **Detecciones Compuestas (*Composite Detections*)** es la técnica avanzada de tomar los resultados y detecciones generadas por una regla preliminar y utilizarlos como criterio de entrada (*input*) en otra regla posterior.
* **Problema que Resuelve:** En ciberseguridad, muchas actividades individuales parecen totalmente inofensivas o de baja severidad si se analizan de manera aislada (ej. un login fuera de horario, la instalación de un software estándar o un intento de acceso denegado). Sin embargo, cuando varios de estos comportamientos coinciden sobre el mismo usuario o activo, se convierten en un incidente crítico.
* **Reducción de Fatiga de Alertas:** Permite mantener las reglas individuales en modo silencioso (sin generar alertas al analista), reservando el disparo de alertas únicamente cuando la **regla compuesta** confirma la convergencia de múltiples comportamientos sospechosos.

---

#### 2. Reglas Productoras o de Entrada (*Producer / Input Rules*)

Las **Reglas Productoras (*Producer Rules*)** son reglas de detección estándar cuya única misión es identificar un comportamiento atómico y registrar la detección en la base de datos interna de SecOps.

* **Detecciones Silenciosas:** Comúnmente no se configuran con alerta habilitada (*Alerting: Off*); simplemente producen telemetría de detección.
* **Recomendación de Diseño Crítica:**
  > [!TIP]
  > **Recomendación de Diseño:**  
  > Se recomienda enfáticamente que las **reglas productoras se escriban como Reglas de Evento Único (*Single Event Rules*) sin sección `match`**.  
  > **Razón Técnica:** Las reglas de evento único se evalúan en tiempo casi real (*Near Real-Time*). Esto garantiza que las detecciones de entrada estén disponibles de inmediato en el almacén de detecciones, evitando desfases o pérdidas por diferencias en las frecuencias de ejecución cuando la regla compuesta aguas abajo intente correlacionarlas.

---

#### 3. Arquitectura y Esquema de Detección (*Detection Schema*)

Una regla compuesta consulta la colección de detecciones existentes (a menudo combinándolas entre sí o cruzándolas con nuevos eventos UDM entrantes).

Para interactuar con las detecciones de entrada, YARA-L utiliza el **Esquema de Detección (*Detection Schema*)**:

| Campo del Esquema de Detección | Descripción Técnica |
| :--- | :--- |
| **`rule_id`** | Identificador UUID unívoco de la regla productora de entrada. |
| **`rule_name`** | Nombre descriptivo de la regla productora que originó el hallazgo. |
| **`match_variables`** | Variables de enlace y pivote definidas en la regla productora original (ej. usuario, host). |
| **`outcome_variables`** | Variables calculadas en la sección `outcome` de la regla productora (ej. `risk_score`, `target_ip`). |
| **`collection_elements`** | Prefijo especial para extraer y consultar los eventos UDM específicos que dispararon la detección productora original. |

---

#### 4. Flujo Operativo de un Escenario Compuesto

```
[Regla Productora 1] -> Detecta: "Login exitoso fuera de país" (Sin alerta)
                                              ↘
                                                [Regla Compuesta (Rule Chaining)] 
                                                -> Cruza por $user en 15m 
                                                -> DISPARA ALERTA CRÍTICA AL SOC
                                              ↗
[Regla Productora 2] -> Detecta: "Acceso anómalo a base de datos" (Sin alerta)
```

1. La **Regla Productora 1** detecta accesos exitosos desde el extranjero para un usuario `$user` y genera una detección de entrada.
2. La **Regla Productora 2** detecta consultas anómalas a bases de datos de producción para el mismo usuario `$user`.
3. La **Regla Compuesta** escucha las detecciones de ambas reglas productoras. Si dentro de una ventana de 15 minutos observa que el mismo `$user` aparece en ambas fuentes de detección, evalúa a verdadero y genera una **alerta de alta prioridad** en la cola de triaje del SOC.

---

### Lección 10: Contexto de Entidad (*Entity Context*)

> **Objetivo:** Comprender la importancia del enriquecimiento contextual de entidades (*Entity Context*) en Google SecOps para responder al "¿quién?" y "¿dónde?" de un evento de seguridad, analizando el mecanismo de enriquecimiento nativo en la ingesta, la distinción entre campos enriquecidos `[E]` y campos parseados `[U]`, y su utilización en reglas de detección YARA-L.

---

#### 1. ¿Qué es el Contexto de Entidad?

El **Contexto de Entidad (*Entity Context*)** complementa la telemetría transaccional básica (*"qué ocurrió"*) con atributos descriptivos e identitarios de los sujetos y objetos involucrados (*"quién lo hizo", "cuál es su cargo en la empresa", "a qué departamento pertenece" o "desde qué país físico se conectó"*).

* **Impacto en las Detecciones:**
  * Permite crear reglas con discriminación fina orientadas a perfiles de alto riesgo (ej. usuarios VIP, administradores de dominio o ingenieros de DevOps).
  * Reduce drásticamente los falsos positivos al contrastar eventos técnicos rutinarios contra el rol legítimo del empleado en la organización.
  * Acelera el triaje del SOC al inyectar metadatos de identidad directamente en la alerta sin requerir consultas manuales a directorios corporativos.

---

#### 2. Enriquecimiento Nativo durante la Ingesta: Campos `[E]` vs. `[U]`

Google SecOps realiza el enriquecimiento contextual de manera **automática y nativa durante el pipeline de ingesta**:

* **Fuentes de Contexto:** Se conecta a proveedores de identidad (**IdP**) como Okta, Google Workspace, Microsoft Entra ID (Azure AD), Ping Identity, así como a bases de datos de inventario de activos (CMDB) y telemetría de red.
* **Mecanismo Temporal:** Al parsear un registro entrante, el motor de ingesta busca el **contexto más reciente disponible** en la base de entidades para asociarlo al evento UDM.
* **Marcadores Visuales en la Consola:**
  * **`[U]` (*Unenriched / Parsed*):** Datos extraídos textualmente del registro crudo por el parser CBN.
  * **`[E]` (*Enriched*):** Datos añadidos dinámicamente por la plataforma durante la ingesta mediante el cruce con fuentes de entidad o inteligencia de Google (ej. geolocalización IP, departamento, título laboral).

---

#### 3. Uso de Campos Enriquecidos en Reglas YARA-L

> [!IMPORTANT]
> **Compatibilidad Plena en Reglas:**  
> Las reglas de detección YARA-L pueden consumir campos enriquecidos exactamente con la misma sintaxis y rendimiento que cualquier otro campo UDM ordinario.

##### Ejemplos de Enriquecimiento en Acción:
1. **Geolocalización IP Integrada (*Google Built-in IP Enrichment*):**  
   Google SecOps enriquece automáticamente las direcciones IP públicas con atributos geográficos sin necesidad de bases de datos externas:
   ```yara
   $e.principal.ip_geo_artifact.country_or_region != "United States"
   ```
2. **Enriquecimiento de Proveedor de Identidad (*IdP Context*):**  
   Permite restringir reglas a departamentos o cargos específicos:
   ```yara
   $e.principal.user.department = "Finance"
   $e.principal.user.title = /.*Director.*/ nocase
   ```

---

#### 4. Cómo Conectar Fuentes de Contexto de Entidad

Para habilitar un contexto más allá de la geolocalización IP nativa de Google:
* Es necesario ingerir registros desde los sistemas IdP y directorios de la organización.
* En el catálogo de parsers por defecto de Google SecOps, se pueden identificar los conectores compatibles buscando la palabra clave **`context`** (ej. parsers de `OKTA_USERS`, `WORKSPACE_USERS`, `AZURE_AD_ENTITIES`).

---

### Lección 11: Aprovechamiento del Grafo de Entidades en Reglas (*Leveraging the Entity Graph in Rules*)

#### 1. ¿Qué es el Grafo de Entidades (*Entity Graph*)?

El **Entity Graph** en Google SecOps es un modelo relacional dinámico que almacena y vincula metadatos contextuales globales e internos sobre entidades (usuarios, máquinas, IPs, dominios, hashes) a lo largo del tiempo.

* **Diferencia frente a campos de eventos directos:**  
  Mientras que las reglas básicas inspeccionan los eventos UDM normalizados (`$e.principal...`, `$e.target...`), el Grafo de Entidades permite consultar la estructura `graph` (`$graph_var.graph...`) para enriquecer y contrastar la telemetría en tiempo de evaluación de la regla con datos que no están presentes en los logs crudos ni en los campos parseados.

```
       ┌──────────────────────────────────────────────┐
       │             Regla YARA-L (events)            │
       └──────────────────────┬───────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
   [Eventos UDM Directos]            [Entity Graph]
    Telemetría transaccional          Metadatos globales y derivados:
    - $e.principal.hostname          - $threat_intel.graph...
    - $e.target.ip                   - $stats.graph.entity...
              │                               │
              └───────────────┬───────────────┘
                              │ Join via variable común ($ip, $hostname)
                              ▼
                 [Detección de Alta Precisión]
```

---

#### 2. Fuentes de Contexto dentro del Entity Graph

Google SecOps organiza el contexto del grafo en dos categorías principales:

##### A. Contexto Global (*Global Context / Threat Intelligence*)
* **Definición:** Inteligencia de amenazas provista y actualizada de forma centralizada por Google (incluyendo Mandiant Threat Intelligence y VirusTotal).
* **Casos de Uso:** Identificación de indicadores maliciosos conocidos (IOCs), reputación de direcciones IP, dominios C2 o hashes de archivos maliciosos asociados a grupos de amenazas (APT).
* **Ejemplo Conceptual:** Correlacionar conexiones de red salientes con IPs categorizadas como maliciosas en el grafo de inteligencia sin necesidad de mantener listas de IOCs manuales.

##### B. Contexto Derivado (*Derived Context / Analytics Interno*)
* **Definición:** Análisis estadístico y comportamiento histórico calculado internamente por Google SecOps a partir de la propia telemetría ingerida de la organización.
* **Métricas Clave:**
  * **`first_seen` / `last_seen`:** Registra la primera y última vez que una entidad fue observada dentro del entorno empresarial.
  * **Prevalencia Diaria (*Prevalence*):** Representa el conteo de cuántos activos o entidades independientes dentro de la red se comunicaron con una entidad específica (ej. un dominio o IP externa) durante un día completo (calculado en ventanas de 00:00 a 23:59 UTC).
  * **Ventana Móvil de 10 Días (*Rolling 10-day Window*):**
    * **`day_count`:** Cantidad de días en los que se observó la entidad en los últimos 10 días.
    * **`rolling_max`:** El valor máximo de prevalencia diaria registrado para esa entidad durante la ventana de 10 días.

> [!TIP]
> **Detección de Anomalías por Prevalencia:**  
> Una IP o dominio externo con una prevalencia (`rolling_max`) muy baja (ej. vista en 1 o 2 dispositivos únicamente) que de repente genera transferencias de datos inusuales representa un fuerte indicador de posible balizaje C2 o exfiltración dirigida, diferenciándolo de tráfico habitual a servicios CDN populares (que tienen alta prevalencia en la empresa).

---

#### 3. Estructura y Sintaxis de Reglas con Entity Graph

Para consultar el Grafo de Entidades dentro de YARA-L, se define una variable específica para el grafo y se une con el evento transaccional a través de una variable común (un *placeholder* o variable de unión).

##### Estructura de Consulta:
```yara
rule entity_graph_threat_intel_match {
  meta:
    author = "SOC Team"
    description = "Detecta comunicación hacia IPs catalogadas como maliciosas en el Entity Graph"
    severity = "CRITICAL"

  events:
    // 1. Telemetría de red regular
    $net.metadata.event_type = "NETWORK_CONNECTION"
    $net.target.ip = $ip

    // 2. Consulta al Grafo de Entidades (Threat Intel)
    $intel.graph.metadata.entity_type = "IP_ADDRESS"
    $intel.graph.entity.ip = $ip
    $intel.graph.metadata.threat.severity = "CRITICAL"

  match:
    $ip over 1h

  condition:
    $net and $intel
}
```

##### Puntos Clave de la Sintaxis:
1. **Prefijo `.graph`:** Todos los atributos del Grafo de Entidades se acceden anteponiendo `.graph` a la variable (ej. `$intel.graph.metadata...`).
2. **Variable de Unión Común:** `$ip` conecta el destino del tráfico (`$net.target.ip`) con el identificador de entidad en el grafo (`$intel.graph.entity.ip`).
3. **Condición Booleana:** Se requiere la conjunción `$net and $intel` para garantizar que la detección se active únicamente si coinciden tanto el evento como la entidad en el grafo.

---

#### 4. Beneficios Operativos en el SOC

| Característica | Reglas Tradicionales Basadas en Logs | Reglas Enriquecidas con Entity Graph |
| :--- | :--- | :--- |
| **Mantenimiento de IOCs** | Listas estáticas manuales que requieren actualización frecuente | Consumo dinámico del feed global de Google y Mandiant |
| **Detección de Rarezas / Novedades** | Difícil de calcular sin consultas analíticas complejas | Disponibilidad inmediata de `rolling_max` y `first_seen` |
| **Volumen de Alertas** | Mayor tasa de falsos positivos por falta de contexto histórico | Alta fidelidad; discrimina servicios masivos vs. destinos atípicos |
| **Eficiencia de Investigación** | El analista debe buscar externamente la reputación del indicador | La alerta ya contiene la metadata contextual de la entidad |

---

### Lección 12: Pruebas y Validación de Reglas (*Rule Testing*)

#### 1. El Ciclo de Vida Temprano de una Regla YARA-L

Cuando se redacta o ajusta una regla de detección (sea una regla curada de Google o una regla personalizada para un caso de uso particular), esta **no produce detecciones en tiempo real ni genera alertas** de inmediato.

* **El dilema de la activación:** En esta fase previa a producción, existe la incertidumbre sobre si la regla generará cero coincidencias o miles de eventos por día (sobrecargando al SOC con ruido).
* **Entorno de validación seguro:** Google SecOps provee dos mecanismos complementarios para simular la ejecución de la regla contra telemetría histórica de forma segura, puramente analítica y sin impacto en producción:
  1. **Prueba de Regla (*Test Rule / Run Test*)**
  2. **Búsqueda Retrospectiva (*Retrohunting*)**

```
   ┌─────────────────────────────────────────────────────────────┐
   │            Desarrollo de la Regla en el Editor              │
   └──────────────────────────────┬──────────────────────────────┘
                                  │
                                  ▼
   ┌─────────────────────────────────────────────────────────────┐
   │        1. Probar Regla (Test Rule - Hasta 14 Días)          │
   │  - No requiere guardar la regla                             │
   │  - Resultados efímeros, sin alertas ni persistencia         │
   │  - Inspección directa de UDM y eventos crudos               │
   └──────────────────────────────┬──────────────────────────────┘
                                  │ ¿Resultados satisfactorios?
                                  ▼
   ┌─────────────────────────────────────────────────────────────┐
   │        2. Búsqueda Retrospectiva (Retrohunt)                │
   │  - Requiere guardar la regla previamente                    │
   │  - Evaluación profunda sobre semanas o meses                │
   │  - Medición de volumen y ajuste fino sensibilidad/ruido     │
   └──────────────────────────────┬──────────────────────────────┘
                                  │ Validación completada
                                  ▼
   ┌─────────────────────────────────────────────────────────────┐
   │      Pase a Producción (Live / Alerting Mode en SIEM)       │
   └─────────────────────────────────────────────────────────────┘
```

---

#### 2. Prueba Rápida de Regla (*Test Rule*)

* **Ubicación en la Consola:** Se ejecuta a través del botón **`Run Test`** situado en la parte inferior del editor de reglas.
* **Alcance Temporal:** Evalúa la lógica sobre un período de hasta **14 días de datos históricos**.
* **Seguridad y Aislamiento:**
  * **No requiere guardar:** Se puede probar código en borrador o experimentar con cambios de lógica sin sobrescribir la regla almacenada.
  * **Sin persistencia ni alertas:** Las coincidencias obtenidas (*matches*) no se almacenan como detecciones permanentes ni disparan alertas al SOC ni acciones SOAR.
* **Herramientas de Análisis en la Prueba:**
  * **Inclusión de Variables de Salida (`outcome`):** Es posible agregar variables calculadas en la sección `outcome` como columnas en la tabla de resultados para verificar los valores extraídos o agregados.
  * **Inspección Profunda:** Cada coincidencia individual se puede desplegar para revisar el registro en crudo (*raw log*) y el evento UDM parseado correspondiente, asegurando que los filtros y condiciones coinciden exactamente con lo previsto.

---

#### 3. Búsqueda Retrospectiva (*Retrohunting*)

Una vez que la regla ha demostrado un comportamiento coherente en la prueba rápida de hasta 14 días, el siguiente paso de validación a escala es el **Retrohunting**.

* **Ubicación en la Consola:** Disponible en el menú contextual de tres puntos (**`⋮`**) de la regla.
* **Requisito Obligatorio:** A diferencia de la prueba rápida, **la regla debe estar guardada** en la plataforma para poder lanzar un retrohunt.
* **Alcance Temporal Extendido:** Ejecuta la lógica sobre grandes volúmenes de datos históricos que abarcan **varias semanas o incluso meses**.
* **Objetivos Operativos del Retrohunting:**
  1. **Comprobación de Existencia Previa:** Determinar si los patrones maliciosos o sospechosos descritos ya ocurrieron en la organización en el pasado.
  2. **Calibración de Ruido y Sensibilidad:** Evaluar la frecuencia teórica de disparo. Si un retrohunt arroja 50,000 coincidencias para un mes de tráfico legítimo, la regla debe afinarse y filtrar excepciones antes de pasar a modo de alerta.
  3. **Cero Impacto Operativo:** Al igual que el test, es un proceso exclusivamente analítico que no ensucia las colas de incidentes en tiempo real.

---

#### 4. Tabla Comparativa: Test Rule vs. Retrohunting

| Criterio | Prueba de Regla (*Test Rule*) | Búsqueda Retrospectiva (*Retrohunting*) |
| :--- | :--- | :--- |
| **Acceso en Consola** | Botón inferior `Run Test` en el editor | Menú de opciones de tres puntos (`⋮`) |
| **Estado de la Regla** | Puede ser un borrador sin guardar | **Debe estar guardada** |
| **Ventana Histórica Máxima** | Hasta 14 días | Varias semanas / meses (según retención contratada) |
| **Propósito Principal** | Verificación sintáctica, lógica e inspección de UDM | Evaluación de volumen histórico y balance sensibilidad/ruido |
| **Volumen de Alertas** | Mayor tasa de falsos positivos por falta de contexto histórico | Alta fidelidad; discrimina servicios masivos vs. destinos atípicos |
| **Eficiencia de Investigación** | El analista debe buscar externamente la reputación del indicador | La alerta ya contiene la metadata contextual de la entidad |

---

### Lección 13: De Eventos a Alertas (*From Events to Alerts*)

#### 1. De la Investigación Manual a la Detección Automatizada

El ciclo completo de detección y respuesta en un SOC moderno comienza con la identificación manual de comportamientos sospechosos y culmina en la automatización de la alerta:

```
   ┌─────────────────────────────────────────────────────────────┐
   │ 1. Investigación Manual (UDM Search)                       │
   │    Filtros interactivos: event_type = USER_LOGIN,           │
   │    security_result.action = BLOCK                           │
   └──────────────────────────────┬──────────────────────────────┘
                                  │ Cientos de eventos dispersos
                                  ▼
   ┌─────────────────────────────────────────────────────────────┐
   │ 2. Construcción de la Regla YARA-L                         │
   │    Se añaden criterios de agregación y frecuencia           │
   │    (ej. múltiples fallos por usuario en 30 minutos)         │
   └──────────────────────────────┬──────────────────────────────┘
                                  │ Guardado (Deshabilitada por defecto)
                                  ▼
   ┌─────────────────────────────────────────────────────────────┐
   │ 3. Estado "Live Rule" (Modo Detección Activa)               │
   │    Genera detecciones periódicas según Run Frequency        │
   │    NO genera alertas visuales ni interrumpe al SOC          │
   └──────────────────────────────┬──────────────────────────────┘
                                  │ Habilitar Alerting Slider
                                  ▼
   ┌─────────────────────────────────────────────────────────────┐
   │ 4. Estado "Alerting" (Producción & SOAR)                    │
   │    - Publica alertas en la vista Alerts and IOCs            │
   │    - Dispara la creación automática de Casos en SOAR        │
   └─────────────────────────────────────────────────────────────┘
```

* **Caso de Uso Real:** Un analista investiga bloqueos de autenticación de usuarios buscando en UDM Search:
  ```sql
  metadata.event_type = "USER_LOGIN" AND security_result.action = "BLOCK"
  ```
* **El Problema del Volumen:** Esta búsqueda puede devolver cientos o miles de eventos ordinarios (contraseñas olvidadas de usuarios legítimos tras vacaciones).
* **La Solución por Detección:** Formalizar una regla YARA-L que agregue frecuencia y ventanas de tiempo (ej. más de 5 intentos fallidos para el mismo usuario en 30 minutos) para discriminar un error humano de un ataque de fuerza bruta o *password spraying*.

---

#### 2. Estados de Activación de una Regla YARA-L

Una vez escrita y guardada la regla en el editor, esta atraviesa distintos estados operacionales mediante dos controles principales:

##### A. Regla Guardada pero Deshabilitada (*Disabled*)
* Al guardar por primera vez, la regla permanece **deshabilitada por defecto**.
* No consume recursos del motor en tiempo real, no genera detecciones ni produce alertas.

##### B. Modo Regla en Vivo (*Live Rule Enabled*)
* **Activación:** Se habilita el conmutador (*toggle*) general de la regla.
* **Comportamiento del Motor:** Empieza a evaluar los logs entrantes y a generar **detecciones (*detections*)** con la periodicidad definida en la configuración de frecuencia de ejecución (**`Run Frequency`**).
* **Ausencia de Ruido en el SOC:** En este estado, la regla **NO genera alertas en la consola ni abre incidentes**.
* **Utilidad Clave:**
  * **Etapa de Maduración/Calibración:** Permite observar en producción cuántas detecciones reales produce y realizar ajustes sin generar trabajo innecesario a los analistas.
  * **Alimentación de Reglas Compuestas (*Rule Chaining / Producer Rules*):** Las detecciones generadas sirven como eventos productores para alimentar reglas compuestas de orden superior.

##### C. Modo Alerta Activado (*Alerting Enabled*)
* **Activación:** Se activa el deslizador específico de **`Alerting`**.
* **Impacto Operativo Inmediato:**
  * **Consola SIEM:** Cada detección se eleva al estatus de **alerta formal**, visible directamente en la página de **`Alerts and IOCs`** dentro de Google SecOps SIEM.
  * **Integración Nativa con SOAR:** Si la plataforma tiene integrada la suite de SOAR, cada alerta genera automáticamente un **Caso (*Case*)** en el sistema de respuesta, mapeando toda la telemetría del evento, artefactos, severidad y disparando los playbooks de contención correspondientes.

---

#### 3. Cuadro Resumen de los Estados de una Regla

| Estado de la Regla | Conmutador `Live` | Deslizador `Alerting` | ¿Genera Detecciones? | ¿Genera Alertas en SIEM? | ¿Crea Casos en SOAR? | Caso de Uso Recomendado |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Borrador / Guardada** | Desactivado | Desactivado | No | No | No | Desarrollo y pruebas en editor |
| **Live (Solo Detección)** | **Activado** | Desactivado | **Sí** (según *Run Frequency*) | No | No | Calibración en producción y reglas productoras para *chaining* |
| **Alerting (Producción Total)** | **Activado** | **Activado** | **Sí** | **Sí** (en *Alerts & IOCs*) | **Sí** (Playbooks / Tickets) | Reglas maduras y afinadas que requieren atención humana |

---

### Lección 14: Métodos para Optimizar Reglas YARA-L (*Methods for Optimizing YARA-L*)

#### 1. Objetivos de la Optimización en YARA-L

La optimización de reglas de detección persigue tres metas fundamentales:
1. **Reducción de Ruido (*Noise Reduction*):** Minimizar falsos positivos consolidando eventos repetitivos.
2. **Eficiencia Computacional (*Performance*):** Disminuir el consumo de recursos de cómputo del motor y acelerar los tiempos de ejecución.
3. **Mantenibilidad y Escalabilidad:** Redactar reglas legibles, modulares y fáciles de actualizar por cualquier miembro del equipo del SOC.

---

#### 2. Principales Estrategias de Optimización

##### A. Filtrado Temprano por Fuente y Tipo de Log (*Log Type & Metadata Filtering*)
* **Mala Práctica:** Buscar patrones de texto o IDs sin restringir el origen de los datos, obligando al motor a escanear toda la telemetría del entorno.
* **Optimización:** Restringir explícitamente el origen (`log_type`) y el tipo de evento en `metadata`:
  ```yara
  $e.metadata.log_type = "WINEVTLOG"
  $e.metadata.event_type = "USER_LOGIN"
  ```

##### B. Coincidencia Exacta de Cadenas vs. Expresiones Regulares (*Exact String vs. Regex*)
* **Mala Práctica:** Usar Regex para comparar identificadores numéricos o cadenas fijas (ej. `/4776/` en campos de texto).
* **Optimización:** Usar comparación directa de igualdad de cadenas contra campos parseados UDM:
  ```yara
  // Mucho más rápido que regex:
  $e.metadata.product_event_type = "4776"
  ```
  *La comparación literal sobre campos parseados por CBN es órdenes de magnitud más veloz que la evaluación de expresiones regulares sobre datos no estructurados.*

##### C. Agrupación y Ventanas de Tiempo en `match` (*Grouping*)
* **Impacto en Ruido:** Si una condición simple de login bloqueado genera 338 detecciones dispersas, agrupar por entidad clave (ej. usuario de destino) dentro de una ventana temporal (ej. 30 minutos) consolida los eventos repetitivos:
  ```yara
  match:
    $target_user over 30m
  ```
  *En el caso de estudio, esta técnica redujo las alertas de 338 a solo 15 detecciones de alta fidelidad sin perder la señal de ataque.*

##### D. Funciones Integradas en Lugar de Expresiones Regulares Complejas
* **Subredes y Rangos IP:**
  * En lugar de construir regex complejas para máscaras de subred (ej. `/192\.168\.1\..*/`), utilizar la función nativa optimizada de red:
    ```yara
    not net.ip_in_range_cidr($e.principal.ip, "192.168.1.0/24")
    ```
* **Regex en una Sola Línea Continua:**
  * Si es necesario evaluar múltiples patrones regex alternativos, es más eficiente consolidarlos en una única expresión regular continua (`/patron1|patron2|patron3/`) en lugar de múltiples líneas de condiciones separadas, reduciendo pasadas de evaluación.

##### E. Filtrado de Valores Nulos o Vacíos (*Zero Value Filtering*)
* En reglas de múltiples eventos (*multi-event rules*), los campos vacíos, nulos o inexistentes en los logs pueden causar coincidencias cruzadas accidentales (*unintentional matching*).
* **Solución:** Excluir explícitamente valores vacíos en los campos de unión o evaluación:
  ```yara
  $e.principal.user.userid != ""
  ```

##### F. Uso de Extensiones de Parser (*Parser Extensions*)
* Si una regla necesita frecuentemente extraer datos mediante regex en tiempo de ejecución (por ejemplo, extraer el dominio de un correo electrónico o subcadenas específicas de URLs):
  * **Optimización Arquitectónica:** Crear una **Extensión de Parser (CBN)** para que el dato se extraiga una sola vez durante el pipeline de ingesta y se almacene en un campo UDM nativo.
  * De este modo, la regla YARA-L evalúa una igualdad de cadena literal (`$e.principal.user.email_domain = "empresa.com"`) en lugar de ejecutar regex pesadas sobre millones de eventos.

##### G. Tablas de Datos (*Data Tables*)
* **Mantenibilidad:** Proporcionan listas consistentes (listas blancas o listas negras) desacopladas de la lógica de la regla.
* **Actualización Automatizada:** Se pueden poblar y sincronizar mediante API o scripts de automatización sin modificar ni recomilar la regla YARA-L.
* **Legibilidad:** Evitan reglas infladas con decenas de operadores `OR` hardcodeados, reduciendo errores humanos.

---

#### 3. Tabla Comparativa de Estrategias de Optimización

| Aspecto | Enfoque Ineficiente (Alto Ruido / Lento) | Enfoque Optimizado (Alta Eficiencia) | Beneficio Principal |
| :--- | :--- | :--- | :--- |
| **Filtrado Inicial** | Escaneo global sin especificar origen | Filtrar por `log_type` y `event_type` | Reduce drásticamente los eventos evaluados |
| **Identificadores Fijos** | Expresión regular: `/4776/` | Igualdad literal: `= "4776"` | Mayor velocidad de ejecución del motor |
| **Rangos de Red** | Regex complejas de IP | Función nativa `net.ip_in_range_cidr()` | Precisión matemática y menor coste de CPU |
| **Extracción Recurrente** | Regex dentro de la regla YARA-L | Extensión de parser CBN en ingesta | Convierte evaluación regex en igualdad literal |
| **Gestión de Entidades** | Agregación de múltiples líneas `OR` en regla | Listas de Referencia o Data Tables | Mantenimiento dinámico y código limpio |
| **Volumen de Alertas** | Disparo individual por cada evento | Agrupación `match: $entity over Xm` | Consolida ruido repetitivo en detecciones claras |

---

### Evaluación: SIEM Detections Knowledge Check

#### Pregunta 1:
**What is the primary purpose of Curated Detections in Google SecOps SIEM?**
* **Respuesta Correcta:** `They provide out-of-the-box, GCTI-maintained rule sets for common threat categories`
* **Justificación Técnica:** Las Detecciones Curadas (*Curated Detections*) son conjuntos de reglas empaquetadas y mantenidas directamente por el equipo de inteligencia de Google Cloud Threat Intelligence (**GCTI**). Están diseñadas para cubrir categorías comunes de amenazas y tácticas de MITRE ATT&CK sin requerir que los clientes desarrollen o mantengan la lógica de detección desde cero. No reemplazan las reglas personalizadas ni desactivan las reglas nativas.

---

#### Pregunta 2:
**How do UDM events receive enriched contextual information?**
* **Respuesta Correcta:** `Enrichment occurs automatically during ingestion using entity data sources`
* **Justificación Técnica:** En Google SecOps, el enriquecimiento contextual (tanto geolocalización IP integrada de Google como metadatos de proveedores de identidad IdP como Okta o Microsoft Entra ID) se aplica de forma **automática durante la fase de ingesta (*pipeline de ingesta*)**. El motor asocia el contexto más reciente de las fuentes de entidad al parsear el evento en UDM, señalizándolo visualmente en la consola con el marcador `[E]`. No requiere agregarlo manualmente en cada regla ni depende de consultas en la interfaz.

---

#### Pregunta 3:
**Which sections are required in every YARA-L rule?**
* **Respuesta Correcta:** `rule name, meta, events, and condition`
* **Justificación Técnica:** La especificación formal de YARA-L exige obligatoriamente cuatro componentes estructurales en toda regla: la declaración del identificador (**rule name**), la sección descriptiva (**`meta:`**), la definición de criterios de registros y variables (**`events:`**), y la lógica booleana de activación (**`condition:`**). Las secciones `match:`, `outcome:` y `options:` son opcionales.

---

#### Pregunta 4:
**What is the purpose of the meta section in a YARA-L rule?**
* **Respuesta Correcta:** `To provide descriptive attributes such as author, description, and severity`
* **Justificación Técnica:** La sección `meta:` almacena metadatos descriptivos clave-valor no ejecutables (ej. `author`, `description`, `severity`, `mitre_attack_technique`). Estos atributos proporcionan contexto documental y de triaje al analista, pero no definen los eventos a coincidir (tarea de `events:`) ni la lógica de disparo (tarea de `condition:`).

---

#### Pregunta 5:
**What is the purpose of running a YARA-L Retrohunt?**
* **Respuesta Correcta:** `To validate detection logic against weeks or months of historical data`
* **Justificación Técnica:** El *Retrohunting* permite ejecutar una regla YARA-L guardada sobre grandes volúmenes de datos históricos acumulados (semanas o meses). Su objetivo fundamental es validar si el comportamiento sospechoso ya existía en el pasado y calibrar el volumen de coincidencias para balancear la sensibilidad frente al ruido antes de pasar la regla a producción. Es un proceso puramente analítico y no genera alertas en vivo.

---

#### Pregunta 6:
**What is a key difference between Single Event Rules and Multi Event Rules?**
* **Respuesta Correcta:** `Single Event Rules trigger on one log entry, while Multi Event Rules rely on sequences or patterns across logs`
* **Justificación Técnica:** Una regla de evento único (*Single Event Rule*) evalúa registros de forma aislada y se activa ante una única entrada de log que cumpla los criterios (ideal para indicadores atómicos). Por el contrario, una regla de múltiples eventos (*Multi-Event Rule*) correlaciona secuencias, frecuencias o agregaciones de diversos eventos a lo largo de una ventana de tiempo definida en la sección `match:`.

---

#### Pregunta 7:
**What does the period parameter represent in a YARA-L metric?**
* **Respuesta Correcta:** `The length of time over which logs are combined into a single observation`
* **Justificación Técnica:** En las métricas de detección y agregación temporal de YARA-L, el parámetro `period` especifica el intervalo o ventana temporal durante el cual se agrupan y consolidan los registros de telemetría en una única observación o punto de evaluación analítica (por ejemplo, en ventanas de agregación o *hop intervals*).

---

#### Pregunta 8:
**What do Composite Rules primarily use to form new detections?**
* **Respuesta Correcta:** `The detections generated by input rules`
* **Justificación Técnica:** Las reglas compuestas (*Composite Rules* o *Rule Chaining*) toman como datos de entrada las **detecciones producidas previamente por otras reglas** (denominadas reglas productoras o *producer rules*). Esto permite vincular comportamientos que de forma individual podrían parecer benignos o de baja severidad, pero que en conjunto representan una amenaza estructurada o de varias fases.











































