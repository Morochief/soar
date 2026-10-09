# Planificación de una Auditoría de Seguridad (Plan a Security Audit)

¡Hola de nuevo! Qué gran gusto tenerte de regreso en el curso. Ahora que hemos cubierto en detalle diferentes *frameworks*, controles, principios de seguridad y regulaciones de cumplimiento (*compliance*), surge una pregunta fundamental: ¿Cómo funciona todo esto en conjunto dentro de una empresa? La respuesta es sencilla y sumamente crucial: a través de las **auditorías de seguridad**.

En esta sesión, aprenderás qué es una auditoría de seguridad, cuáles son sus fases iniciales de planificación y cómo tú, como analista de seguridad de nivel inicial (*entry-level*), desempeñarás un papel clave en este proceso.

---

## Introducción del Instructor

En esta clase, tu instructor de Google te guiará a través del fascinante proceso de evaluar las defensas de una organización. Las auditorías son la herramienta definitiva para poner a prueba si las políticas teóricas realmente se están cumpliendo en la práctica y para asegurar que la infraestructura esté protegida contra amenazas y vulnerabilidades.

---

## ¿Qué es una Auditoría de Seguridad?

> [!IMPORTANT]
> Una **auditoría de seguridad** (*security audit*) es una revisión exhaustiva de los controles, políticas y procedimientos de seguridad de una organización frente a un conjunto de expectativas o estándares preestablecidos.

Existen dos tipos principales de auditorías de seguridad:
*   **Auditorías Externas:** Realizadas por entidades u organismos ajenos a la empresa.
*   **Auditorías Internas:** Llevadas a cabo por un equipo propio de la empresa. Nos enfocaremos en estas últimas, ya que son el tipo de auditorías en las que los analistas de ciberseguridad principiantes suelen colaborar activamente.

Una auditoría de seguridad interna suele ser ejecutada por un equipo multidisciplinario que puede incluir al oficial de cumplimiento (*compliance officer*), al gerente de seguridad (*security manager*) y a otros miembros del equipo técnico. Su objetivo principal es mejorar la postura de seguridad (*security posture*) de la organización y ayudar a evitar costosas multas de las agencias gubernamentales reguladoras debido a la falta de cumplimiento.

---

## Los Elementos Comunes de una Auditoría Interna

Una auditoría interna se compone de cinco elementos clave:
1.  Establecer el alcance (*scope*) y los objetivos (*goals*) de la auditoría.
2.  Realizar una evaluación de riesgos (*risk assessment*) de los activos de la organización.
3.  Completar una evaluación de controles (*controls assessment*).
4.  Evaluar el cumplimiento (*compliance*).
5.  Comunicar los resultados a las partes interesadas (*stakeholders*).

En esta lección, nos enfocaremos detalladamente en los dos primeros elementos, los cuales forman parte esencial del **proceso de planificación de la auditoría**.

### 1. Establecer el Alcance y los Objetivos

*   **El Alcance (*Scope*):** Se refiere a los criterios específicos y límites de la auditoría de seguridad interna. Definir el alcance exige que las organizaciones identifiquen con precisión a las personas, activos (*assets*), políticas, procedimientos y tecnologías que impactan directamente en su postura de seguridad.
    *   *Ejemplo práctico:* El alcance de una auditoría puede delimitarse específicamente a evaluar los permisos de los usuarios, identificar los controles existentes y auditar la tecnología y los equipos que utiliza actualmente la empresa.
*   **Los Objetivos (*Goals*):** Son un esquema detallado de las metas de seguridad que la organización desea alcanzar para robustecer sus defensas.
    *   *Ejemplo práctico:* Los objetivos pueden incluir la implementación de las funciones core de *frameworks* de la industria (como el NIST CSF), el establecimiento de políticas para asegurar el cumplimiento regulatorio o el fortalecimiento de los controles lógicos de los sistemas.

> [!NOTE]
> Aunque los miembros más experimentados del equipo de ciberseguridad (*senior-level*) y los *stakeholders* son quienes definen formalmente el alcance y los objetivos, como analista de nivel inicial se te pedirá que los revises y comprendas a fondo para poder ejecutar con éxito el resto de los componentes técnicos de la auditoría.

### 2. Realizar una Evaluación de Riesgos (*Risk Assessment*)

La evaluación de riesgos se enfoca en identificar amenazas (*threats*), riesgos y vulnerabilidades potenciales que acechan a la organización. Este análisis exhaustivo ayuda a determinar qué medidas de seguridad adicionales deben implementarse y monitorearse de manera prioritaria para salvaguardar los activos críticos.

Al igual que la definición del alcance, el *risk assessment* suele ser completado por gerentes o especialistas de alto rango. Sin embargo, tu misión como analista consistirá en **analizar los detalles proporcionados en dicha evaluación** para deducir qué tipos de controles y regulaciones de cumplimiento deben ponerse en marcha.

*   *Caso de estudio en el entorno laboral:* Imagina que un reporte de evaluación de riesgos destaca que existen controles y procesos inadecuados para proteger los activos de la empresa. Específicamente, señala una falta de gestión oportuna sobre los activos físicos y digitales (incluyendo los dispositivos de los empleados), advierte que los equipos de almacenamiento de datos no están bien asegurados y concluye que el acceso a la información privada en la **red interna** (*internal network*) requiere de controles lógicos mucho más robustos. Como analista, utilizarás estos hallazgos para proponer e implementar las soluciones técnicas adecuadas en las siguientes fases de la auditoría.

---

## Puntos Clave (Key Takeaways)

*   **Definición de Auditoría:** Una auditoría de seguridad es una evaluación crítica y sistemática de los controles, políticas y procedimientos de una empresa frente a un estándar definido.
*   **Enfoque Interno:** Las auditorías internas permiten identificar riesgos organizacionales de forma temprana, optimizar la postura de seguridad y mitigar multas por incumplimiento normativo.
*   **Fase de Planificación:** El éxito de una auditoría radica en su planificación, la cual depende estrictamente de delimitar el alcance (personas, activos y tecnologías a evaluar) y trazar objetivos claros.
*   **Evaluación de Riesgos:** El *risk assessment* diagnostica las debilidades de la empresa (como fallas en el aseguramiento de la red interna o en los dispositivos de almacenamiento), sirviendo como hoja de ruta para saber dónde robustecer los controles de seguridad.
*   **Rol del Analista Entry-Level:** Aunque la dirección estratégica la definen los perfiles *senior*, el analista operativo analiza los reportes de riesgo y ejecuta las pruebas de controles en el día a día.
