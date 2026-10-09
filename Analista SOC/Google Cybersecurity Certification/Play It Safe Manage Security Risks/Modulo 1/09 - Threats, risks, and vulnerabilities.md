# Threats, risks, and vulnerabilities

Como analista de seguridad de nivel de entrada, uno de tus muchos roles será manejar los activos físicos y digitales de una organización. Como recordatorio, un activo (*asset*) es cualquier elemento que se percibe con valor para una organización.

Durante su vida útil, las organizaciones adquieren todo tipo de activos, incluyendo espacios de oficinas físicas, computadoras, la PII de los clientes (Información Personal Identificable), propiedad intelectual como patentes o datos con derechos de autor, y mucho más. Desafortunadamente, las organizaciones operan en un entorno salvaje que presenta múltiples **amenazas, riesgos y vulnerabilidades** para sus activos. 

Repasemos qué significan exactamente estos tres conceptos clave y discutamos algunos ejemplos comunes de cada uno.

## 1. Amenazas (Threats)
Una amenaza es cualquier circunstancia o evento que pueda impactar negativamente a los activos. 

Un ejemplo clásico de una amenaza es un ataque de ingeniería social (*Social Engineering*). La ingeniería social es una técnica de manipulación que explota el error humano (y la psicología) para obtener información privada, acceso o bienes de valor corporativo. 

> [!WARNING]
> Los enlaces maliciosos incrustados en mensajes de correo electrónico corporativo que parecen provenir de empresas o personas legítimas son un método letal de ingeniería social conocido como *Phishing*. Esta técnica se utiliza todos los días para adquirir datos confidenciales de los empleados, como nombres de usuario, contraseñas o información bancaria.

## 2. Riesgos (Risks)
Los riesgos son conceptualmente muy diferentes de las amenazas. Un riesgo es **cualquier cosa que pueda impactar la Confidencialidad, Integridad o Disponibilidad (CIA)** de un activo. 

Piensa en un riesgo corporativo como *la probabilidad* de que ocurra una amenaza real. Un ejemplo de un riesgo interno para una organización podría ser la absoluta falta de protocolos de copia de seguridad (*Backups*) para asegurar que la información almacenada pueda recuperarse tras un ataque de *Ransomware* o un incendio en el servidor.

Las organizaciones tienden a calificar los riesgos en diferentes niveles (bajo, medio y alto) dependiendo de la probabilidad y el valor monetario del activo afectado:
*   **Activo de bajo riesgo:** Es información que, de verse comprometida, no dañaría la reputación, no detendría las operaciones y no causaría daño financiero. Esto incluye información pública como el contenido del sitio web abierto.
*   **Activo de riesgo medio:** Incluye información que no está disponible al público y puede causar cierto daño a las finanzas o la reputación. Por ejemplo, la publicación anticipada y filtrada de las ganancias trimestrales de una empresa podría impactar negativamente el valor de sus acciones en la bolsa de valores.
*   **Activo de alto riesgo:** Es cualquier información protegida por regulaciones o leyes (como PII o SPII). Si se ve comprometida, tendría un impacto negativo severo y catastrófico en las finanzas, las operaciones continuas o la reputación corporativa.

## 3. Vulnerabilidades (Vulnerabilities)
Una vulnerabilidad es una **debilidad** específica que puede ser explotada por una amenaza. Vale la pena señalar una regla de oro en ciberseguridad: **para que exista un riesgo real, tanto una vulnerabilidad como una amenaza deben estar presentes al mismo tiempo**.

Ejemplos técnicos de vulnerabilidades incluyen: un firewall de red desactualizado, software sin parchear (*unpatched*), aplicaciones heredadas (*Legacy*), contraseñas débiles o bases de datos sin encriptar.

> [!IMPORTANT]
> **El Eslabón Humano:** Las personas también pueden ser consideradas una vulnerabilidad (a menudo, la más grande de la organización). Las acciones de la gente pueden afectar significativamente la red interna. Ya sea un cliente, un proveedor externo o un empleado de finanzas, mantener la seguridad debe ser un esfuerzo unido corporativo (*Responsabilidad Compartida*).

Por lo tanto, los analistas SOC deben educar y empoderar a las personas para que sean más conscientes de la seguridad. Educar a los empleados sobre cómo identificar un intento de *Phishing* es un excelente punto de partida. Utilizar tarjetas magnéticas de acceso para otorgar permisos a espacios físicos (control de acceso) mientras se restringe severamente a los visitantes externos es otra buena medida defensiva.

Las organizaciones deben mejorar continuamente sus esfuerzos tácticos cuando se trata de identificar y mitigar vulnerabilidades para minimizar el daño. Los analistas de Nivel 1 apoyan activamente este objetivo animando a los empleados a reportar actividades sospechosas de inmediato y monitoreando los registros del SIEM sobre quién accede a los activos críticos.

Ahora que estás familiarizado con las diferencias clave entre amenazas, riesgos y vulnerabilidades, a continuación discutiremos en profundidad cómo estas variantes impactan a las operaciones comerciales del negocio.
