# Phases of an incident response playbook

Anteriormente, discutimos cómo las herramientas SIEM se utilizan para ayudar a proteger los activos críticos (*critical assets*) y los datos de una organización. En esta sesión, introduciremos otra herramienta fundamental para mantener la seguridad de una empresa, conocida como **playbook** o manual de estrategia.

---

## Introducción del Instructor

En esta clase, el equipo de expertos de Google te guiará a través del concepto de automatización y estandarización de procesos de defensa. Aprenderás cómo los profesionales del Centro de Operaciones de Seguridad (**SOC**) reaccionan ante incidentes de manera predecible, rápida y precisa, eliminando la improvisación frente a los ataques informáticos.

---

## ¿Qué es un Playbook y por qué es esencial?

> [!NOTE]
> Un **playbook** (manual de estrategia) es un manual procedimentual que proporciona detalles exhaustivos sobre cualquier acción operativa. Asimismo, aclara con precisión qué herramientas específicas deben utilizarse en respuesta a un incidente de seguridad determinado.

En el campo de la ciberseguridad, los *playbooks* son absolutamente esenciales. Cuando se identifica una amenaza, factores como la **urgencia, la eficiencia y la precisión** son obligatorios para mitigar el peligro rápidamente y reducir el riesgo potencial. 

Los *playbooks* garantizan que el personal del SOC siga una lista consistente de acciones de una manera prescrita y estandarizada, independientemente de quién sea el analista de turno que esté trabajando en el caso.

### Tipos de Playbooks
Existen diferentes tipos de manuales de estrategia diseñados para propósitos operativos específicos, entre los que se incluyen:
*   *Playbooks* de respuesta a incidentes (*incident response*).
*   *Playbooks* para alertas de seguridad específicas.
*   *Playbooks* orientados a equipos particulares.
*   *Playbooks* dedicados a productos de software específicos.

En esta sección, nos enfocaremos en el manual más utilizado en la industria: el **playbook de respuesta a incidentes** (*incident response playbook*).

---

## El Proceso de Respuesta a Incidentes (Incident Response)

> [!NOTE]
> La **respuesta a incidentes** (*incident response*) es el intento rápido y coordinado de una organización para identificar un ataque, contener el daño y corregir los efectos perjudiciales de una brecha de seguridad (*security breach*).

Un *incident response playbook* es una guía estructurada que consta de **seis fases** cronológicas utilizadas para mitigar y gestionar los incidentes de seguridad de principio a fin:

### 1. Preparación (*Preparation*)
Las organizaciones deben prepararse activamente para mitigar la probabilidad, el riesgo y el impacto de un incidente de seguridad. Esto se logra mediante la documentación detallada de procedimientos, el establecimiento de planes de asignación de personal y la educación continua de los usuarios. La preparación establece la base fundamental para una respuesta a incidentes exitosa. Por ejemplo, las empresas crean planes que delimitan claramente los roles y responsabilidades de cada miembro del equipo de seguridad.

### 2. Detección y análisis (*Detection and analysis*)
El objetivo central de esta fase es detectar y analizar los eventos utilizando procesos definidos y tecnología especializada. El uso de herramientas y estrategias adecuadas durante esta etapa permite a los analistas de seguridad determinar con certeza si ha ocurrido una brecha informática y analizar su posible magnitud o alcance.

### 3. Contención (*Containment*)
La meta de la contención es detener la propagación del ataque, evitar daños adicionales y reducir el impacto inmediato del incidente de seguridad. Durante esta fase, los profesionales toman medidas drásticas y rápidas para aislar los sistemas comprometidos y minimizar el impacto negativo. La contención es de altísima prioridad para las organizaciones porque detiene los riesgos continuos sobre los datos y los activos críticos.

### 4. Erradicación y recuperación (*Eradication and recovery*)
Esta fase implica la eliminación completa de todos los artefactos, rastros y remanentes del incidente para que la organización pueda regresar con seguridad a sus operaciones normales. Los profesionales eliminan códigos maliciosos (*malware*) y mitigan las vulnerabilidades explotadas. Una vez ejercida esta debida diligencia, se procede a restaurar el entorno afectado a un estado seguro, proceso también conocido como **restauración de IT** (*IT restoration*).

### 5. Actividad post-incidente (*Post-incident activity*)
Esta fase incluye la documentación exhaustiva de lo ocurrido, la notificación formal a los líderes de la organización y la aplicación de las lecciones aprendidas (*lessons learned*) para garantizar que la empresa esté mejor preparada para enfrentar futuros incidentes. Dependiendo de la severidad del evento, se puede llevar a cabo un análisis de causa raíz (*root cause analysis*) para implementar actualizaciones y mejoras que eleven la postura de seguridad (*security posture*) global.

### 6. Coordinación (*Coordination*)
La coordinación implica el reporte oportuno de los incidentes y el intercambio seguro de información a lo largo de todo el ciclo de respuesta, basándose en los estándares legales y corporativos establecidos por la organización. Es crucial porque garantiza que la empresa cumpla con los requisitos normativos (*compliance*) y permite una resolución completamente coordinada entre los diferentes departamentos.

---

## Sinergia Defensiva: SIEM + Playbooks

> [!IMPORTANT]
> Las herramientas SIEM y los *playbooks* trabajan de forma conjunta y sinérgica. El SIEM se encarga de recopilar y analizar masivamente los datos para detectar amenazas y generar alertas en tiempo real; cuando el analista de seguridad recibe dicha alerta en su consola de monitoreo, consulta el *playbook* adecuado para guiar de manera estructurada, eficiente y predecible todo el proceso de respuesta.

---

## Puntos Clave (Key Takeaways)

*   **Estandarización Operativa:** Los *playbooks* eliminan la imprevisibilidad en el SOC, asegurando que todos los analistas ejecuten exactamente las mismas acciones validadas ante una amenaza.
*   **Ciclo de Vida del Incidente:** El proceso de *incident response* se divide en seis fases críticas: Preparación, Detección/Análisis, Contención, Erradicación/Recuperación, Actividad Post-incidente y Coordinación.
*   **Prioridad Perimetral:** La contención (*containment*) representa una de las fases más urgentes y críticas para detener el daño activo a la infraestructura y proteger los activos de la empresa.
*   **Aprendizaje y Evolución:** La actividad post-incidente y el análisis de causa raíz garantizan que la organización aprenda de sus brechas e implemente mejoras continuas en su postura de seguridad.
*   **Flujo Integrado:** El éxito de la defensa moderna radica en la integración técnica: el SIEM identifica y alerta, mientras que el *playbook* guía al analista en los pasos de mitigación.
