# Explore the CISSP security domains, Part 2

En este video, cubriremos los últimos cuatro dominios de seguridad de la certificación **CISSP**: Gestión de Identidad y Acceso, Evaluación y Pruebas de Seguridad, Operaciones de Seguridad, y Seguridad en el Desarrollo de Software.

## 5. Gestión de Identidad y Acceso (Identity and Access Management / IAM)
El quinto dominio se enfoca estrictamente en el acceso y la autorización para mantener los datos seguros, asegurándose de que los usuarios sigan las políticas establecidas para controlar y gestionar los activos corporativos.

Como analista de nivel de entrada, es esencial mantener los sistemas y datos de una organización tan seguros como sea posible garantizando que el acceso de los usuarios se limite **únicamente** a lo que los empleados necesitan para hacer su trabajo (*Principio de Menor Privilegio*). El objetivo principal del IAM es reducir el riesgo general.

> [!CAUTION]
> **El Peligro de las Cuentas Compartidas:** Por ejemplo, si todos en una empresa utilizan el mismo inicio de sesión de administrador genérico, no hay forma técnica de rastrear quién tiene acceso a qué datos. En caso de una brecha de seguridad, separar la actividad legítima de los usuarios corporativos de la actividad maliciosa del actor de amenazas sería forensemente imposible.

Hay cuatro componentes principales del IAM:
1. **Identificación:** Es cuando un usuario afirma quién es proporcionando un nombre de usuario, una tarjeta de acceso física o datos biométricos como una huella digital.
2. **Autenticación:** Es el proceso de verificación para probar matemáticamente esa identidad afirmada, como ingresar una contraseña o un PIN secreto.
3. **Autorización:** Se lleva a cabo *después* de que se ha confirmado la identidad del usuario y se relaciona con su nivel de permisos de acceso, lo cual depende de su rol en la organización (*Control de Acceso Basado en Roles / RBAC*).
4. **Responsabilidad (*Accountability* / Auditoría):** Se refiere al monitoreo y registro inmutable de las acciones del usuario (como guardar *logs* de los intentos de inicio de sesión exitosos y fallidos) para probar legalmente que los sistemas se utilizaron de manera adecuada.

## 6. Evaluación y Pruebas de Seguridad (Security Assessment and Testing)
Este dominio se enfoca en realizar pruebas a los controles de seguridad, recopilar y analizar datos, y llevar a cabo auditorías estrictas para monitorear riesgos, amenazas y vulnerabilidades.

Probar los controles de seguridad puede ayudar a una organización a identificar nuevas y mejores formas de mitigar intrusiones. Esto implica examinar si los controles instalados realmente logran los objetivos corporativos. Un analista SOC utilizaría los informes de evaluación (*Security Assessment Reports*) para mejorar los controles existentes.
*   **Ejemplo:** Implementar como nuevo control el uso obligatorio de Autenticación Multifactor (MFA) en toda la empresa tras descubrir en una auditoría que las contraseñas eran demasiado débiles.

## 7. Operaciones de Seguridad (Security Operations)
El dominio de operaciones de seguridad (el corazón táctico del SOC) se enfoca en llevar a cabo investigaciones y ejecutar respuestas de mitigación en tiempo real.

Las investigaciones comienzan en el instante en que se identifica un incidente de seguridad (ej. una alerta crítica en el SIEM). Este proceso requiere un alto sentido de urgencia para minimizar la propagación del riesgo. Si hay un ciberataque activo, mitigar el ataque y aislarlo de la red para evitar que escale es esencial.

> [!NOTE]
> **Respuesta a Incidentes y Análisis Forense:** Una vez que la amenaza activa ha sido neutralizada y contenida, comenzará la recolección estricta de evidencia digital y física bajo Cadena de Custodia. Se debe realizar una autopsia forense para identificar exactamente **cuándo, cómo y por qué** ocurrió la brecha, lo que permite al equipo de seguridad tapar los agujeros y prevenir futuros ataques.

## 8. Seguridad en el Desarrollo de Software (Software Development Security)
El octavo y último dominio de seguridad se enfoca en utilizar prácticas de programación y codificación segura (*Secure Coding*).

Como recordarás, las prácticas de codificación segura son pautas estrictas para crear aplicaciones y servicios invulnerables. El Ciclo de Vida del Desarrollo de Software (SDLC) es un proceso acelerado utilizado por los equipos de ingeniería (*DevOps*) para construir productos rápidamente.

En el mundo moderno (*DevSecOps*), la seguridad ya no es un paso de auditoría al final del producto, sino que se integra completamente en cada fase del desarrollo:
*   Realizar revisiones de diseño seguro durante la fase inicial de arquitectura.
*   Realizar revisiones automatizadas de código seguro durante las fases de programación y pruebas.
*   Realizar pruebas de penetración (*Penetration Testing* o *Hacking Ético*) durante la fase de implementación y despliegue final.

Esto mantiene el software seguro, protege los datos confidenciales de los clientes, y mitiga riesgos catastróficos para la organización.

Estar íntimamente familiarizado con estos ocho dominios te ayudará a comprender cómo se entrelaza la ciberseguridad corporativa. ¡A continuación, discutiremos más a fondo sobre amenazas, *ransomware* y las tres capas misteriosas de la web!
