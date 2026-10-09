# Use SIEM tools to protect organizations

Anteriormente, se presentó una introducción a las herramientas de Gestión de Información y Eventos de Seguridad (**SIEM**) y a algunos de sus paneles de control (*dashboards*) [cite: 24]. También aprendiste sobre las diferentes amenazas, riesgos y vulnerabilidades que una organización puede experimentar [cite: 24]. En esta lectura de los expertos de Google, profundizarás en los datos de los *dashboards* de SIEM y en cómo los profesionales de la ciberseguridad utilizan esa información de telemetría para identificar y mitigar una potencial amenaza, riesgo o vulnerabilidad corporativa [cite: 24].

---

## Introducción de los Expertos de Google

En el ecosistema de un Centro de Operaciones de Seguridad (**SOC**), los analistas dependen críticamente de interfaces visuales para interpretar los millones de eventos que ocurren en la red [cite: 24]. Esta lectura está diseñada para brindarte una comprensión profunda de cómo soluciones líderes del mercado estructuran sus datos para acelerar las investigaciones y optimizar la postura de seguridad de la organización [cite: 24].

---

## Splunk

Splunk ofrece diferentes opciones de herramientas SIEM altamente integradas en la industria: **Splunk® Enterprise** y **Splunk® Cloud** [cite: 24]. Ambas variantes te permiten revisar los datos masivos de una organización a través de paneles de control o *dashboards* avanzados [cite: 24]. Esto ayuda notablemente a los profesionales de la seguridad a gestionar la infraestructura interna de una empresa mediante la recopilación, búsqueda, monitoreo y análisis de datos de registros (*logs*) procedentes de múltiples fuentes, obteniendo así una visibilidad completa de las operaciones cotidianas de la organización [cite: 24].

A continuación, se detallan los principales *dashboards* de Splunk y sus propósitos operativos dentro del SOC:

### Panel de Postura de Seguridad (*Security posture dashboard*)
El *security posture dashboard* está diseñado específicamente para las operaciones del SOC [cite: 24]. Despliega las últimas 24 horas de los eventos y tendencias de seguridad más notables de una organización, lo que permite a los profesionales determinar de inmediato si la infraestructura y las políticas de seguridad están rindiendo según lo diseñado [cite: 24]. Los analistas de seguridad utilizan este panel para monitorear e investigar posibles amenazas en tiempo real, como actividad de red sospechosa que se origina desde una dirección IP específica [cite: 24].

### Panel de Resumen Ejecutivo (*Executive summary dashboard*)
El *executive summary dashboard* analiza y monitorea la salud general y el estado de la organización a lo largo del tiempo [cite: 24]. Esto ayuda a los equipos de seguridad a robustecer y mejorar las medidas de protección que reducen el riesgo corporativo [cite: 24]. Los analistas de seguridad suelen utilizar este panel para proporcionar información estratégica de alto nivel (*high-level insights*) a las partes interesadas (*stakeholders*), como la generación de un resumen consolidado de incidentes y tendencias de seguridad durante un período de tiempo determinado [cite: 24].

### Panel de Revisión de Incidentes (*Incident review dashboard*)
El *incident review dashboard* permite a los analistas identificar patrones sospechosos que pueden ocurrir durante o antes de un incidente de seguridad [cite: 24]. Su función principal es asistir al analista resaltando aquellos elementos de mayor riesgo que requieren una revisión humana inmediata [cite: 24]. Este panel es de gran utilidad debido a que proporciona una línea de tiempo visual detallada de los eventos que condujeron directamente a un incidente [cite: 24].

### Panel de Análisis de Riesgos (*Risk analysis dashboard*)
El *risk analysis dashboard* ayuda a los analistas a identificar el riesgo asociado a cada objeto de riesgo específico de la infraestructura, como un usuario determinado, una computadora o una dirección IP [cite: 24]. Muestra cambios inusuales en la actividad o el comportamiento relacionado con el riesgo, como un usuario legítimo iniciando sesión fuera de sus horas normales de trabajo o un tráfico de red inusualmente alto procedente de una computadora específica [cite: 24]. Un analista de seguridad puede usar este panel para analizar el impacto potencial de las vulnerabilidades en activos críticos (*critical assets*), lo que ayuda a priorizar los esfuerzos de mitigación de riesgos del equipo de ciberseguridad [cite: 24].

---

## Chronicle

Chronicle es una herramienta SIEM nativa de la nube (*cloud-native*) de Google, diseñada específicamente para retener, analizar y realizar búsquedas masivas de datos de registros con el fin de identificar potenciales amenazas de seguridad, riesgos y vulnerabilidades [cite: 24]. Chronicle te permite recopilar y analizar datos de *logs* de acuerdo con cuatro variables fundamentales [cite: 24]:
*   Un activo (*asset*) específico [cite: 24].
*   Un nombre de dominio [cite: 24].
*   Un usuario [cite: 24].
*   Una dirección IP [cite: 24].

Chronicle proporciona múltiples *dashboards* especializados que ayudan a los analistas a monitorear los registros de la organización, crear filtros lógicos y alertas automatizadas, y realizar el seguimiento continuo de nombres de dominio sospechosos [cite: 24].

A continuación, se desglosan los principales *dashboards* de Chronicle y sus propósitos operativos:

### Panel de Información de la Empresa (*Enterprise insights dashboard*)
El *enterprise insights dashboard* resalta y prioriza las alertas recientes [cite: 24]. Identifica nombres de dominio sospechosos dentro de los registros, los cuales son conocidos en la industria como indicadores de compromiso (**IOCs**) [cite: 24]. Cada resultado desplegado se etiqueta con una puntuación de confianza (*confidence score*) para indicar la probabilidad real de que se trate de una amenaza, y proporciona un nivel de severidad (*severity level*) que indica la relevancia de dicho riesgo para la organización [cite: 24]. Un analista de seguridad utiliza este panel para monitorear intentos de inicio de sesión o de acceso a datos relacionados con un activo crítico —como una aplicación corporativa o un sistema central— desde ubicaciones o dispositivos inusuales [cite: 24].

### Panel de Ingesta y Salud de Datos (*Data ingestion and health dashboard*)
El *data ingestion and health dashboard* muestra de forma gráfica la cantidad de *logs* de eventos, las fuentes de origen de los registros y las tasas de éxito de los datos que se están procesando e ingiriendo dentro de Chronicle [cite: 24]. Un analista de seguridad utiliza este panel para asegurarse de que todas las fuentes de registros estén correctamente configuradas y que los *logs* se estén recibiendo sin ningún tipo de error [cite: 24]. Esto garantiza que los problemas relacionados con los registros se aborden a tiempo para que el equipo del SOC tenga acceso ininterrumpido a la telemetría que necesita [cite: 24].

### Panel de Coincidencias de IOC (*IOC matches dashboard*)
El *IOC matches dashboard* indica las principales amenazas, riesgos y vulnerabilidades activas contra la organización [cite: 24]. Los profesionales de la seguridad utilizan este panel para observar el comportamiento de nombres de dominio, direcciones IP e IOCs de dispositivos a lo largo del tiempo con el fin de identificar tendencias de ataques [cite: 24]. Esta información se utiliza luego para dirigir el enfoque y los recursos del equipo de ciberseguridad hacia las amenazas de mayor prioridad [cite: 24]. Por ejemplo, los analistas de seguridad pueden usar este panel para buscar actividad adicional asociada con una alerta, como el inicio de sesión sospechoso de un usuario desde una ubicación geográfica inusual [cite: 24].

### Panel Principal (*Main dashboard*)
El *main dashboard* despliega un resumen de alto nivel de la información relacionada con la ingesta de datos de la organización, las alertas activas y la actividad general de eventos a lo largo del tiempo [cite: 24]. Los profesionales de la seguridad utilizan este panel para acceder a una línea de tiempo unificada de eventos de seguridad —como un pico abrupto en los intentos fallidos de inicio de sesión— para identificar tendencias de amenazas a través de múltiples fuentes de registros, dispositivos, direcciones IP y ubicaciones físicas [cite: 24].

### Panel de Detecciones de Reglas (*Rule detections dashboard*)
El *rule detections dashboard* proporciona estadísticas automatizadas relacionadas con los incidentes que presentan las mayores ocurrencias, severidades y detecciones a lo largo del tiempo [cite: 24]. Los analistas de seguridad utilizan este panel para acceder a una lista exhaustiva de todas las alertas activadas por una regla de detección específica, como una regla diseñada para alertar al SOC cada vez que un usuario abre un archivo adjunto malicioso conocido desde un correo electrónico corporativo [cite: 24]. Los analistas emplean estas estadísticas para gestionar incidentes recurrentes y establecer tácticas de mitigación que reduzcan el nivel de riesgo general de la empresa [cite: 24].

### Panel de Resumen de Inicios de Sesión de Usuarios (*User sign in overview dashboard*)
El *user sign in overview dashboard* proporciona información analítica sobre el comportamiento de acceso de los usuarios en toda la organización [cite: 24]. Los analistas de seguridad utilizan este panel para acceder a una lista de todos los eventos de inicio de sesión e identificar actividad inusual de las credenciales, como un usuario que intenta iniciar sesión desde múltiples ubicaciones físicas al mismo tiempo [cite: 24]. Esta información se emplea luego para mitigar amenazas, riesgos y vulnerabilidades dirigidas a las cuentas de usuario y a las aplicaciones de la organización [cite: 24].

---

## Puntos Clave (Key Takeaways)

*   **Organización y Enfoque:** Las herramientas SIEM proporcionan *dashboards* especializados que permiten a los profesionales de la seguridad organizar, centralizar y enfocar de manera eficiente sus esfuerzos defensivos [cite: 24].
*   **Mitigación Oportuna:** El uso estratégico de estos paneles visuales permite a los analistas reducir drásticamente el riesgo de la empresa al identificar, analizar y remediar los elementos de mayor prioridad y criticidad de manera oportuna [cite: 24].
*   **Especialización de Splunk:** Splunk segmenta la telemetría en paneles de postura de seguridad, resúmenes ejecutivos, revisión de incidentes y análisis de riesgos, optimizando el flujo de trabajo tanto técnico como gerencial [cite: 24].
*   **Correlación en Google Chronicle:** Chronicle permite rastrear amenazas de forma masiva correlacionando eventos basados en activos, dominios, usuarios o direcciones IP a través de paneles dinámicos de detección de reglas e indicadores de compromiso (IOC) [cite: 24].
*   **Preparación Práctica:** Más adelante en este programa de certificación, tendrás la gran oportunidad práctica de interactuar directamente con estas herramientas utilizando diversas funciones y comandos para ejecutar consultas de búsqueda (*search queries*) en escenarios reales [cite: 24].
