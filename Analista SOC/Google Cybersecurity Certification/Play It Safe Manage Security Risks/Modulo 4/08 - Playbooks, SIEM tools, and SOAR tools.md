# Playbooks, SIEM tools, and SOAR tools

Anteriormente, aprendiste que los equipos de seguridad se enfrentan a amenazas (*threats*), riesgos (*risks*), vulnerabilidades (*vulnerabilities*) e incidentes de forma regular, y que siguen manuales de estrategia (*playbooks*) para abordar estos problemas de seguridad [cite: 22]. En esta lectura complementaria de los expertos de Google, aprenderás más sobre los *playbooks*, incluyendo cómo se utilizan dentro de la gestión de información y eventos de seguridad (**SIEM**) y en la orquestación, automatización y respuesta de seguridad (**SOAR**) [cite: 22].

---

## Introducción de los Expertos de Google

En el núcleo operativo de un Centro de Operaciones de Seguridad (**SOC**), la visibilidad de las alertas debe estar respaldada inmediatamente por la capacidad de respuesta coordinada [cite: 22]. Comprender cómo interactúan los *playbooks* lógicos con las infraestructuras automáticas de detección te permitirá mitigar incidentes críticos reduciendo drásticamente el margen de error humano [cite: 22].

---

## Playbooks y Herramientas SIEM

Los equipos de ciberseguridad utilizan los *playbooks* en el momento en que se produce un incidente [cite: 22]. Estas guías ayudan a los equipos de seguridad a responder a los incidentes garantizando que se siga una lista consistente de acciones de una manera prescrita y estandarizada, independientemente de qué analista esté trabajando en el caso [cite: 22]. 

Los *playbooks* pueden ser sumamente detallados y suelen incluir diagramas de flujo (*flow charts*) y tablas lógicas para esclarecer qué acciones tomar y en qué orden específico ejecutarlas [cite: 22].

> [!IMPORTANT]
> Los *playbooks* también se emplean críticamente para los procedimientos de recuperación en caso de un ataque de *ransomware* [cite: 22]. Cada tipo diferente de incidente de seguridad posee su propio *playbook* dedicado, el cual detalla minuciosamente quién debe tomar qué acción y en qué momento exacto hacerlo [cite: 22].

Por lo general, los *playbooks* se utilizan de forma conjunta con las herramientas SIEM [cite: 22]. Si, por ejemplo, una herramienta SIEM marca o genera una alerta sobre un comportamiento inusual de un usuario, el *playbook* correspondiente proporciona a los analistas del SOC las instrucciones exactas sobre cómo abordar y resolver el problema [cite: 22].

---

## Playbooks y Herramientas SOAR

Los *playbooks* también se integran de manera nativa con las herramientas SOAR [cite: 22]. Las herramientas SOAR son similares a las herramientas SIEM en el sentido de que ambas se utilizan para el monitoreo de amenazas [cite: 22]. 

> [!NOTE]
> El **SOAR** (*Security Orchestration, Automation, and Response*) es una solución de software utilizada para automatizar tareas repetitivas generadas por herramientas como un SIEM o un sistema de detección y respuesta gestionada (**MDR** - *Managed Detection and Response*) [cite: 22].

*   **Ejemplo de Automatización:** Si un usuario intenta iniciar sesión en su computadora demasiadas veces con una contraseña incorrecta, el sistema SOAR bloqueará automáticamente su cuenta para detener una posible intrusión en tiempo real sin requerir la intervención de un analista [cite: 22].
*   **Rol del Analista:** Una vez que el SOAR ejecuta la acción automatizada de contención, los analistas recurren al *playbook* para seguir los pasos necesarios y resolver el problema de fondo [cite: 22].

---

## Puntos Clave (Key Takeaways)

*   **Concepto de Runbooks:** Lo más importante que debes saber es que los *playbooks* —a los que a veces también se les denomina ***runbooks***— proporcionan acciones detalladas que los equipos de seguridad deben tomar en caso de un incidente [cite: 22].
*   **Reducción del Impacto:** Conocer con total exactitud quién debe hacer qué y cuándo ayuda a reducir considerablemente el impacto de un incidente de seguridad [cite: 22].
*   **Protección de Activos:** La estandarización de estos procesos disminuye drásticamente el riesgo de daños graves contra los activos críticos (*critical assets*) de una organización [cite: 22].
