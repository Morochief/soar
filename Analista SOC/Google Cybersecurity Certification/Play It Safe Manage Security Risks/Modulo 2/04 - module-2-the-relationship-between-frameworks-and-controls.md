# Lectura: The relationship between frameworks and controls

Anteriormente, aprendiste cómo las organizaciones utilizan *frameworks* y controles de seguridad para protegerse contra amenazas, riesgos y vulnerabilidades. Esto incluyó discusiones sobre el Marco de Gestión de Riesgos (**NIST RMF**) y el Marco de Ciberseguridad (**NIST CSF**) del Instituto Nacional de Estándares y Tecnología de EE. UU., así como la tríada de Confidencialidad, Integridad y Disponibilidad (CIA). En esta lectura, explorarás más a fondo cómo se utilizan conjuntamente los marcos y los controles para mitigar el riesgo organizacional.

## Marcos y Controles
Los marcos de seguridad son guías metodológicas (*guidelines*) utilizadas para construir planes de defensa y proteger la privacidad. Los marcos ayudan a las organizaciones a cumplir con las estrictas leyes y regulaciones (Compliance). Por ejemplo, la industria de la salud en EE. UU. utiliza marcos para cumplir con **HIPAA** (*Health Insurance Portability and Accountability Act*), que exige bajo pena de ley que los profesionales médicos mantengan la información de los pacientes segura y privada.

Los **controles de seguridad**, por el contrario, son las salvaguardas reales instaladas para reducir riesgos específicos. Son las *medidas* técnicas que utilizan las organizaciones. Por ejemplo, un control que se puede usar *junto* con un marco para garantizar que un hospital cumpla con HIPAA, es obligar a los pacientes y doctores a usar la **Autenticación Multifactor (MFA)** para acceder a sus registros médicos en el portal. Usar una medida técnica como el MFA para validar la identidad de alguien es una forma táctica de mitigar el riesgo.

## Marcos y controles específicos de la industria
Existen muchos marcos y controles diferentes que las organizaciones pueden utilizar para cumplir con las regulaciones de su sector (Salud, Finanzas, Gobierno). Dos marcos muy comunes son el **CTF** y el **ISO 27001**.

### Marco de Amenazas Cibernéticas (Cyber Threat Framework - CTF)
Según la Oficina del Director de Inteligencia Nacional (ODNI) de EE. UU., el CTF fue desarrollado por el gobierno federal para proporcionar *"un lenguaje común para describir y comunicar información sobre actividades de ciberamenazas"*. Al proporcionar un léxico estandarizado, el CTF ayuda a los profesionales del SOC y *Threat Intel* a analizar y compartir inteligencia procesable de manera mucho más eficiente, especialmente frente a actores de amenazas de Estado-Nación.

### Organización Internacional de Normalización (ISO/IEC 27001)
Un marco de trabajo internacionalmente reconocido en el ámbito corporativo es el **ISO 27001**. Esta familia de estándares permite a organizaciones de todos los sectores gestionar la seguridad de activos vitales (información financiera, propiedad intelectual y datos de empleados). 
Este marco describe los requisitos estrictos para establecer un **Sistema de Gestión de Seguridad de la Información (SGSI / ISMS)**. Aunque ISO 27001 no obliga al uso de controles específicos de una marca particular, sí proporciona una enorme biblioteca de controles (Anexo A) que las organizaciones pueden adaptar para mejorar su postura de seguridad y certificarse anualmente.

## Clasificación de los Controles
Los controles se utilizan para reducir la probabilidad o el impacto de un incidente de seguridad. Estos controles se dividen tradicionalmente en tres categorías (**Físicos, Técnicos y Administrativos**) y se utilizan para prevenir, detectar o corregir problemas.

**Ejemplos de controles físicos:**
*   Puertas biométricas, vallas y cerraduras.
*   Guardias de seguridad en las instalaciones.
*   Cámaras de vigilancia (CCTV) y detectores de movimiento en el Data Center.
*   Tarjetas magnéticas de acceso (*Badges*) para entrar a las oficinas.

**Ejemplos de controles técnicos (Lógicos):**
*   Firewalls (Cortafuegos).
*   Autenticación Multifactor (MFA).
*   Software Antivirus / EDR.

**Ejemplos de controles administrativos (Políticas):**
*   **Separación de funciones (*Separation of duties*):** Ninguna persona tiene control absoluto sobre un proceso crítico.
*   Autorización estricta basada en roles (RBAC).
*   Clasificación formal de activos (Ej. "Uso Interno", "Confidencial", "Secreto").

> [!IMPORTANT]
> **Puntos Clave:** Los marcos y controles de ciberseguridad se utilizan *juntos* para establecer la postura de seguridad de una organización. Los marcos son el "qué hacer" administrativo, y los controles son el "cómo hacerlo" técnico. Aunque adoptar muchos de estos marcos es técnicamente voluntario, se recomienda encarecidamente a las organizaciones que los implementen para evitar cuantiosas multas gubernamentales y garantizar la supervivencia del negocio.
