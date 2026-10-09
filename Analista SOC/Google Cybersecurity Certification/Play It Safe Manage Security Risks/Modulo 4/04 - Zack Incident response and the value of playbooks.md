# Zack: Incident response and the value of playbooks

¡Hola de nuevo! Continuamos avanzando con paso firme en este cuarto módulo. En esta sesión, conoceremos la experiencia de un ingeniero de Google con una trayectoria poco convencional, quien nos compartirá una perspectiva fresca y práctica sobre cómo la estandarización de procesos y el uso de *playbooks* salvan el día en situaciones de alta presión dentro del SOC.

---

## Introducción del Instructor

Mi nombre es **Zack** y soy ingeniero de software (*Software Engineer*) en el equipo de seguridad de Google Workspace. Cuento con una trayectoria profesional no tradicional; cuando me gradué de la universidad, originalmente pensé que me dedicaría al derecho, pero tras ser aceptado en la facultad, decidí no asistir. En su lugar, me uní a Google dentro del área de reclutamiento (*recruiting*). 

A través de ese trabajo, realicé un poco de labor estratégica donde aprendí por mi cuenta a hacer extracción de datos web (*web scraping*). Me gustó tanto que tomé uno de los cursos de capacitación interna de Google, lo que me ayudó a realizar la transición desde el reclutamiento hacia la ingeniería de software.

---

## ¿Qué son los Playbooks y cuál es su verdadero valor?

Los procesos y los manuales de estrategia o *playbooks* son la documentación técnica que los ingenieros de software y otros profesionales en Google utilizamos para determinar con exactitud cómo debemos responder ante los eventos que ocurren en la infraestructura. Ya sea que se trate de un incidente de privacidad o seguridad, o de un ataque activo, contamos con conjuntos de pautas o algoritmos que usamos para determinar el mejor curso de acción. Esto nos asegura gestionar correctamente la seguridad y los datos de las personas.

> [!NOTE]
> Soy relativamente nuevo en el ámbito de la ciberseguridad; he sido ingeniero de software aquí durante unos dos años. Cuando estoy de guardia (*on-call*) o ayudando a resolver una vulnerabilidad, no poseo el conocimiento absoluto para responder a cada una de las cosas que potencialmente podrían presentarse en mi camino.

Por esta razón, los *playbooks* son súper importantes para las personas como yo y para otros profesionales que se integran nuevos a la industria: **te permiten resolver un problema complejo respaldado por la experiencia de un especialista senior**. Básicamente, estás incorporando décadas de conocimiento colectivo en tu propia resolución gracias a que puedes confiar en ese *playbook* y en los consejos de otros expertos inscritos en él.

---

## Casos de Uso Comunes para los Playbooks

Dentro del equipo de seguridad de Google Workspace, el abanico de incidentes operacionales para los cuales desplegamos y consultamos *playbooks* incluye de manera habitual:
*   Ataques abiertos e intentos de intrusión activos (*open attacks*).
*   Incidentes de privacidad (*privacy incidents*).
*   Filtraciones o fugas de datos (*data leaks*).
*   Ataques de denegación de servicio (*Denial of Service - DoS*).
*   Alertas críticas de infraestructura y servicios (*service alerts*).

---

## Mi Primer Desafío en el Equipo de Seguridad

Cuando comencé en el equipo de seguridad de Google, mi primera tarea consistió en corregir una vulnerabilidad reportada externamente. Esto significa que un investigador de seguridad externo (*security researcher*) estuvo interactuando con nuestra aplicación en el ecosistema real y descubrió un fallo que potencialmente podría filtrar datos de nuestros usuarios.

Al ser mi primera tarea técnica con el equipo, mirar hacia atrás me hace ver que era algo relativamente fácil de solucionar; sin embargo, **en ese momento me sentí realmente abrumado**. 

> [!IMPORTANT]
> Lo que me salvó fue que, cuando recibimos un reporte de vulnerabilidad, este viene acompañado de una **guía de remediación** (*remediation guidance*). El reporte que me fue asignado incluía pasos específicos que decían: *"Estas son las acciones concretas que consideramos que debes realizar"*. Seguir esa estructura eliminó el estrés y me guió directo a la solución.

---

## Consejos para Iniciarse en la Ciberseguridad

Si estás interesado en comenzar tu carrera en el sector de la ciberseguridad, mi mayor recomendación es que **hables con tantas personas de la industria como te sea posible**. Aprenderás cómo es el trabajo en el día a día, descubrirás las habilidades técnicas específicas que necesitas desarrollar para llegar allí, conocerás los roles y vacantes abiertas, y entenderás cómo es la cultura laboral en diferentes empresas.

Desearía que alguien me hubiera dicho cuando me gradué de la universidad cómo son realmente estos trabajos. Yo pensaba que programar o trabajar en sistemas consistía en estar aislado, con la cabeza baja, escribiendo en una computadora dentro de una oficina oscura durante 12 horas al día. Pero no es así en absoluto.

*   **El 50% del rol es comunicación:** Consiste en interactuar con otras personas, revisar diseños de arquitectura y debatir ideas de forma colaborativa. Esto lo hace sumamente atractivo.
*   **Seguridad Perpetua:** Algunas tecnologías o equipos van y vienen según la moda de la industria, pero **la seguridad es omnipresente**. Es sumamente importante ahora y solo se volverá más crítica en el futuro. Pertenecer a un equipo de seguridad te brinda una gran estabilidad y propósito profesional; definitivamente es un excelente lugar para estar.

---

## Puntos Clave (Key Takeaways)

*   **Caminos No Tradicionales:** El SOC y los equipos de ingeniería de Google se nutren de profesionales con trasfondos diversos (como leyes o reclutamiento) que aprenden habilidades técnicas mediante la práctica y el autoaprendizaje.
*   **Capitalización del Conocimiento:** Los *playbooks* actúan como una transferencia de conocimiento masiva, permitiendo que un analista o ingeniero *junior* resuelva incidentes con la efectividad y experiencia de un veterano de la industria.
*   **Guías de Remediación:** Enfrentar una vulnerabilidad reportada puede ser abrumador al inicio, pero las instrucciones de mitigación (*remediation guidance*) integradas en los reportes de bugs estructuran el camino para neutralizar el riesgo con éxito.
*   **Ciberseguridad es Colaboración:** El mito de la oficina oscura y el aislamiento es falso; la mitad de la jornada laboral de un defensor informático se basa en la comunicación, el diseño conjunto y el intercambio de ideas lógicas.
*   **Un Campo Indispensable:** A diferencia de otras especialidades tecnológicas que fluctúan con las tendencias del mercado, la ciberseguridad es una necesidad constante y creciente para proteger la tríada CIA de las empresas.
