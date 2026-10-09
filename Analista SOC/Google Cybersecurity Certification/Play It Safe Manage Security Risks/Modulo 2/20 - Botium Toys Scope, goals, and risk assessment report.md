# Botium Toys: Informe de Alcance, Objetivos y Evaluación de Riesgos (Botium Toys: Scope, goals, and risk assessment report)

¡Bienvenido de nuevo! Como parte de tu formación práctica en el *Google Cybersecurity Certificate*, es momento de sumergirse en un escenario del mundo real a través de tu primera actividad de portafolio profesional. En este ejercicio, actuarás como un analista de seguridad encargado de revisar la documentación inicial preparada por la gerencia de tecnología de la información (**IT**) de una empresa en pleno crecimiento.

Las auditorías de seguridad y las evaluaciones de riesgos son los mecanismos clave que aseguran que se realicen las verificaciones periódicas necesarias para monitorear amenazas (*threats*), mitigar riesgos y subsanar vulnerabilidades antes de que afecten la continuidad del negocio y los activos críticos de una organización.

---

## Introducción del Instructor

En esta sección de tu portafolio, trabajarás sobre el caso de **Botium Toys**. Tu objetivo principal como analista será asimilar el alcance, las metas estratégicas y el informe de riesgos provisto por la dirección de IT, sirviendo como base indispensable para completar posteriormente la lista de verificación de controles y cumplimiento (*controls and compliance checklist*). ¡Comencemos con el análisis!

---

## Alcance y Objetivos de la Auditoría (Scope and goals of the audit)

*   **Alcance (*Scope*):** El alcance de esta auditoría se define de manera integral como la totalidad del programa de seguridad en Botium Toys. Esto incluye todos sus activos técnicos (*assets*), tales como los dispositivos y equipos utilizados por los empleados, su red interna (*internal network*) y sus sistemas de información corporativos. Tu labor requiere revisar exhaustivamente los activos tangibles e intangibles de la empresa, así como los controles y las prácticas de cumplimiento (*compliance*) implementadas hasta la fecha.
*   **Objetivos (*Goals*):** Evaluar con precisión los activos existentes y completar la lista de verificación de controles y cumplimiento para determinar de forma clara cuáles controles técnicos y mejores prácticas normativas deben implementarse con urgencia para robustecer la postura de seguridad (*security posture*) de Botium Toys.

---

## Activos Actuales de la Empresa (Current assets)

Los activos gestionados directamente por el departamento de IT de Botium Toys se clasifican de la siguiente manera:

*   **Infraestructura Local:** Equipos e instalaciones físicas locales (*on-premises*) necesarios para las operaciones diarias de la oficina principal.
*   **Equipos de los Empleados:** Dispositivos de usuario final (computadoras de escritorio, *laptops*, smartphones), estaciones de trabajo remotas, auriculares, cables, teclados, ratones corporativos y estaciones de acoplamiento (*docking stations*).
*   **Infraestructura de Videovigilancia y Almacén:** Cámaras de seguridad físicas y todos los productos de la tienda disponibles para la venta minorista tanto en el sitio físico como en la plataforma en línea, almacenados en el almacén contiguo de la compañía.
*   **Sistemas, Software y Servicios:** Gestión centralizada de las plataformas de contabilidad, telecomunicaciones, bases de datos corporativas, herramientas de seguridad, sistemas de comercio electrónico (*ecommerce*) y plataformas de gestión de inventario.
*   **Conectividad y Redes:** Acceso corporativo a Internet y administración de la red interna de la organización.
*   **Almacenamiento de Datos:** Sistemas dedicados a la retención y almacenamiento seguro de la información comercial y de clientes.
*   **Sistemas Heredados (*Legacy systems*):** Mantenimiento y supervisión de sistemas informáticos antiguos que han llegado al fin de su vida útil (*end-of-life*) y que requieren obligatoriamente de monitoreo humano continuo al no recibir actualizaciones automáticas.

---

## Evaluación de Riesgos (Risk assessment)

### Descripción del Riesgo (*Risk description*)
Actualmente, existe una gestión y administración inadecuada de los activos tecnológicos de la empresa. Adicionalmente, Botium Toys carece de la implementación de controles de seguridad críticos y fundamentales, lo que significa que la organización podría no estar cumpliendo plenamente con las regulaciones y estándares legales vigentes, tanto dentro de los Estados Unidos como a nivel internacional.

### Mejores Prácticas de Control (*Control best practices*)
Tomando como eje la primera de las funciones core del Marco de Ciberseguridad de NIST (**NIST CSF**), la cual es **Identificar** (*Identify*), Botium Toys tiene la necesidad imperiosa de dedicar recursos técnicos y financieros para identificar con precisión todos sus activos con el fin de gestionarlos adecuadamente. 

Asimismo, el equipo de IT deberá clasificar los activos existentes y determinar con exactitud el impacto que tendría la pérdida o el compromiso de cada sistema sobre la continuidad del negocio (*business continuity*).

> [!IMPORTANT]
> **Puntuación de Riesgo (*Risk score*):** En una escala del 1 al 10, la puntuación de riesgo actual de Botium Toys se sitúa en **8**, un nivel considerablemente alto. Esta alarmante calificación se debe directamente a la falta de controles de seguridad robustos y a la ausencia de adherencia a las mejores prácticas de cumplimiento normativo.

---

## Comentarios Adicionales y Hallazgos Críticos

> [!NOTE]
> Aunque el impacto potencial derivado de la pérdida de un activo individual está catalogado como **medio** (debido a que el departamento de IT aún no tiene total visibilidad de cuáles activos específicos se encuentran en mayor peligro), el riesgo general para la infraestructura y la posibilidad de recibir penalizaciones o multas severas por parte de los organismos reguladores es **alto**. 

A continuación, se desglosan los hallazgos técnicos y detalles específicos recopilados durante el análisis inicial:

*   **Accesos sin Control:** Actualmente, todos los empleados de Botium Toys tienen acceso irrestricto a los datos almacenados internamente. Esto implica que personal no autorizado podría tener acceso directo a los datos de los titulares de tarjetas de crédito y a la información de identificación personal (*PII*) o información personal sensible (*SPII*) de los clientes.
*   **Ausencia de Cifrado:** No se utiliza ningún tipo de cifrado (*encryption*) para garantizar la confidencialidad de la información financiera y las tarjetas de crédito de los clientes que se aceptan, procesan, transmiten y almacenan de manera local en la base de datos interna de la empresa.
*   **Falta de Políticas de Acceso:** No se han implementado controles de acceso lógicos basados en el principio del menor privilegio (*least privilege*) ni esquemas de separación de funciones (*separation of duties*).
*   **Fortalezas Actuales:** En el lado positivo, el departamento de IT ha logrado garantizar una adecuada disponibilidad de los sistemas e integró controles básicos para asegurar la integridad de los datos. Asimismo, la empresa cuenta con un *firewall* perimetral configurado para bloquear el tráfico sospechoso mediante un conjunto de reglas de seguridad apropiadamente definidas, y mantiene un software *antivirus* instalado y monitoreado regularmente.
*   **Carencia de Detección Proactiva:** El departamento de IT no ha instalado ningún sistema de detección de intrusos (**IDS**).
*   **Falta de Resiliencia:** No existen planes de recuperación ante desastres (*disaster recovery plans*) activos y la empresa no realiza copias de seguridad (*backups*) de sus datos comerciales críticos.
*   **Cumplimiento Parcial de Privacidad:** Se ha desarrollado con éxito un plan para notificar a los clientes de la Unión Europea dentro de las 72 horas posteriores en caso de una brecha de seguridad (*security breach*). Además, se han redactado y aplicado políticas y procesos de privacidad entre los miembros de IT y otros empleados para documentar y mantener los datos correctamente.
*   **Debilidad en Contraseñas:** Aunque existe una política de contraseñas, sus requisitos son mínimos (*nominal*) y obsoletos; no están alineados con las exigencias modernas de complejidad (como exigir un mínimo de ocho caracteres, una combinación de letras, al menos un número y caracteres especiales).
*   **Ausencia de Gestión Centralizada:** No hay un sistema centralizado de gestión de contraseñas corporativas que haga cumplir los requisitos mínimos. Esto afecta de forma recurrente la productividad general, ya que los empleados y proveedores deben enviar constantemente *tickets* de soporte al equipo de IT para recuperar o restablecer sus credenciales.
*   **Desorden en Sistemas Heredados:** Si bien los sistemas heredados (*legacy systems*) se monitorean y mantienen, no existe un calendario o programación regular para estas tareas, y los métodos de intervención técnica en caso de falla son confusos o ambiguos.
*   **Seguridad Física Óptima:** En cuanto a la infraestructura física, la ubicación de la tienda (oficinas principales, fachada y almacén) cuenta con cerraduras suficientes y seguras, un sistema de videovigilancia por circuito cerrado de televisión (**CCTV**) completamente actualizado, así como sistemas funcionales de detección y prevención de incendios.

---

## Puntos Clave (Key Takeaways)

*   **Diagnóstico de Postura:** Botium Toys cuenta con una postura de seguridad vulnerable (puntuación de riesgo: 8) debido a la preocupante falta de controles lógicos internos y debilidades normativas organizacionales.
*   **Vulnerabilidades Críticas de Datos:** La falta de cifrado en la base de datos local y el acceso masivo de los empleados a información de tarjetas y *PII/SPII* exponen a la empresa a incidentes graves de fuga de datos y multas internacionales.
*   **Brechas en Control de Acceso:** Es urgente estructurar e implementar el principio del menor privilegio y la separación de funciones, además de desplegar un sistema de gestión centralizada de contraseñas para erradicar las credenciales nominales débiles.
*   **Falta de Visibilidad y Monitoreo:** La ausencia de un sistema IDS y la falta de un inventario claro de activos impiden al equipo de IT saber con precisión qué recursos se encuentran en riesgo inminente.
*   **Seguridad Física como Fortaleza:** Las barreras físicas, los sistemas contra incendios y las cámaras de CCTV representan el punto más robusto y maduro de la infraestructura actual de la organización.
