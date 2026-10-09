# Lectura: Security domains cybersecurity analysts need to know

Como analista, puedes explorar diversas áreas de la ciberseguridad que te interesen. Una forma de explorar esas áreas es comprendiendo los diferentes dominios de seguridad y cómo se utilizan para organizar el trabajo técnico y administrativo de los profesionales. En esta lectura, aprenderás más sobre los ocho dominios de seguridad **CISSP** y cómo se relacionan con el trabajo táctico que harás como analista de seguridad.

## Dominio 1: Seguridad y gestión de riesgos (Security and risk management)
Todas las organizaciones deben desarrollar su postura de seguridad (*security posture*). Esta es la capacidad de una organización para gestionar la defensa de sus activos críticos y reaccionar ante los cambios (o ataques). Los elementos de este dominio que impactan directamente la postura de seguridad incluyen:
*   Metas y objetivos de seguridad
*   Procesos de mitigación de riesgos
*   Cumplimiento normativo (*Compliance*)
*   Planes de Continuidad del Negocio (BCP)
*   Regulaciones legales
*   Ética profesional y organizacional

La **Seguridad de la Información (InfoSec)** también está estrechamente relacionada con este dominio y se refiere a un conjunto de procesos establecidos para asegurar la información. Las áreas de diseño InfoSec incluyen: Gestión de vulnerabilidades, Respuesta a incidentes, Seguridad en la nube (*Cloud Security*), Seguridad de aplicaciones y Seguridad de la infraestructura.
*   *Ejemplo:* Un equipo de seguridad (*Blue Team*) puede necesitar alterar técnicamente cómo se procesa la Información Personal Identificable (PII) en sus bases de datos para adherirse al Reglamento General de Protección de Datos (GDPR) de la Unión Europea.

## Dominio 2: Seguridad de activos (Asset security)
La seguridad de activos implica gestionar el ciclo de vida de los datos, incluyendo el **almacenamiento, mantenimiento, retención y destrucción** de datos físicos y virtuales. Dado que el robo de activos aumenta drásticamente el nivel de riesgo, mantener un inventario exacto es esencial.
*   *Ejemplo:* Los analistas de seguridad pueden necesitar crear copias de seguridad de datos críticos aisladas de la red para garantizar que puedan restaurar el entorno corporativo si un ataque de *Ransomware* encripta la organización.

## Dominio 3: Arquitectura e ingeniería de seguridad (Security architecture and engineering)
Este dominio se enfoca en gestionar la seguridad garantizando que existan herramientas, sistemas y procesos efectivos. Uno de los aspectos más importantes es el concepto de **responsabilidad compartida** (*shared responsibility*), lo que significa que *todos* los individuos asumen un rol activo para reducir el riesgo. Los principios de diseño adicionales incluyen:
*   Modelado de amenazas (*Threat modeling*)
*   Menor privilegio (*Least privilege*)
*   Defensa en profundidad (*Defense in depth*)
*   Fallo seguro (*Fail securely*)
*   Separación de funciones (*Separation of duties*)
*   Mantenerlo simple (*Keep it simple*)
*   Cero confianza (*Zero trust*)
*   Confiar pero verificar (*Trust but verify*)
*   *Ejemplo:* El uso de una herramienta **SIEM** para monitorear banderas rojas (*flags*) relacionadas con inicios de sesión inusuales, lo que podría indicar que un atacante está intentando infiltrarse.

## Dominio 4: Seguridad de redes y comunicaciones (Communication and network security)
Este dominio se enfoca en asegurar las redes físicas y las comunicaciones inalámbricas (incluyendo conexiones locales, remotas y en la nube). Las organizaciones con entornos de trabajo híbridos deben asegurar los datos mientras gestionan conexiones externas seguras (como VPNs) para los trabajadores remotos.

## Dominio 5: Gestión de identidad y acceso (Identity and access management / IAM)
El dominio IAM se enfoca en asegurar que las identidades de los usuarios sean de confianza y autenticadas, y que su acceso a los sistemas esté estrictamente autorizado.

> [!IMPORTANT]
> **El Principio del Menor Privilegio:** IAM utiliza lo que se conoce como el *principio de menor privilegio* (Least Privilege), que es el concepto de otorgar a un usuario únicamente el acceso mínimo y estrictamente necesario para completar su tarea laboral, ni un permiso más. Por ejemplo, garantizar que el soporte al cliente solo pueda ver el número de teléfono del cliente (pero no su tarjeta de crédito) para resolver un ticket, y luego revocar el acceso.

## Dominio 6: Evaluación y pruebas de seguridad (Security assessment and testing)
Se enfoca en identificar proactivamente vulnerabilidades. Las organizaciones suelen contratar probadores de penetración (a menudo llamados **Pen Testers** o *Red Teamers*) para hackear éticamente los sistemas e imitar a un atacante real antes de que ocurra una brecha. También enfatiza la realización de auditorías de seguridad (*Security Audits*) periódicas a los permisos de los usuarios para validar que nadie tenga exceso de privilegios (previniendo el *Privilege Creep*).

## Dominio 7: Operaciones de seguridad (Security operations)
La sala de guerra. Este dominio se enfoca en la investigación táctica de posibles brechas de datos y la implementación de la respuesta a incidentes en tiempo real. Esto incluye el uso de estrategias y herramientas como:
*   Formación y concientización (Entrenamiento de usuarios)
*   Informes y documentación (*Reporting*)
*   Detección y prevención de intrusiones (IDS / IPS)
*   Herramientas SIEM
*   Gestión de registros (*Log Management*)
*   Manuales de respuesta (*Playbooks*)
*   Gestión de incidentes (*Incident Response*)
*   Forense posterior a la brecha (*Post-breach forensics*)
*   Reflexión sobre las lecciones aprendidas (Mejora continua)
*   *Ejemplo:* Un equipo de analistas de seguridad manejando un ataque activo a las 3:00 a.m. aislando segmentos de la red para detener la exfiltración masiva de datos corporativos.

## Dominio 8: Seguridad en el desarrollo de software (Software development security)
Se enfoca en utilizar pautas de programación segura (*Secure Coding*). La seguridad debe incorporarse activamente en *cada* etapa del Ciclo de Vida del Desarrollo de Software (SDLC) para prevenir inyecciones de código. La seguridad no puede ser una idea de último momento; debe realizarse **QA** (Aseguramiento de Calidad) y pruebas dinámicas al código antes de ser lanzado a los clientes.

### Puntos Clave (*Key Takeaways*)
*   Los 8 dominios CISSP categorizan todo el espectro del trabajo de ciberseguridad corporativo, desde el papeleo legal hasta el *Hacking Ético*.
*   El Principio de Menor Privilegio es vital para aislar cuentas comprometidas.
*   Estar familiarizado con la terminología de InfoSec te preparará mejor para leer alertas técnicas del SIEM y comprender exactamente qué dominio de la empresa está bajo ataque.
