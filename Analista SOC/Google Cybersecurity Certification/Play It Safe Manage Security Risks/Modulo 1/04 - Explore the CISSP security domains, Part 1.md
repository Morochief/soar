# Explore the CISSP security domains, Part 1

¡Bienvenido de nuevo! Como recordarás del primer curso, existen ocho dominios (o categorías) de seguridad identificados por la certificación **CISSP**. 

Los equipos de seguridad (*Blue Teams*) los utilizan metódicamente para organizar las tareas diarias, identificar brechas que podrían causar consecuencias catastróficas para una organización, y establecer su **postura de seguridad** general. Recuerda que la *postura de seguridad* se refiere a la capacidad real de una organización para gestionar la defensa de sus activos críticos y reaccionar ante cambios o ataques.

En esta clase, desglosaremos el enfoque de los primeros cuatro dominios:

## 1. Seguridad y Gestión de Riesgos (Security and Risk Management)
Este es el dominio fundamental. Sus áreas de enfoque clave incluyen:
*   **Definición de objetivos de seguridad:** Permite a las organizaciones reducir proactivamente los riesgos contra activos críticos (como la información personal identificable o PII).
*   **Mitigación de riesgos (*Risk mitigation*):** Significa tener los procedimientos y reglas correctas en su lugar (*Playbooks*) para reducir rápidamente el impacto de un incidente, como una brecha de datos.
*   **Cumplimiento (*Compliance*):** Es el método principal utilizado para desarrollar políticas de seguridad internas que respeten los requisitos legales y los estándares independientes corporativos.
*   **Continuidad del negocio (*Business continuity*):** Se relaciona con la capacidad corporativa de mantener la productividad diaria operativa estableciendo planes de recuperación ante desastres (DRP).
*   **Regulaciones legales y Ética:** Aunque las leyes varían a nivel mundial, como profesional de seguridad corporativo, esto significa seguir estrictamente las reglas éticas para minimizar negligencias, abusos o fraudes internos.

## 2. Seguridad de Activos (Asset Security)
Este dominio se enfoca de lleno en proteger los activos, tanto físicos como digitales. Está íntimamente relacionado con el **almacenamiento, mantenimiento, retención y destrucción** del ciclo de vida de los datos corporativos.

Esto significa que activos sensibles como la PII y SPII deben manejarse de forma ultrasegura, ya sea que estén almacenados en un disco duro, transferidos por la red, o recopilados físicamente en papel. Las organizaciones deben tener políticas estrictas que dicten cómo se destruyen los datos confidenciales.

> [!NOTE]
> **Ejemplo de Destrucción de Datos:** Como analista SOC, es posible que debas supervisar la destrucción física de discos duros viejos (usando trituradoras industriales) para asegurarte de que se eliminen correctamente. Esto garantiza que un actor de amenazas jamás pueda hurgar en la basura corporativa (*Dumpster Diving*) y acceder a esos datos privados.

## 3. Arquitectura e Ingeniería de Seguridad (Security Architecture and Engineering)
Este dominio se centra en optimizar la seguridad de los datos garantizando que existan **herramientas, sistemas y procesos efectivos** (la arquitectura técnica) para proteger a la organización contra ataques dirigidos.

Uno de los conceptos centrales de esta arquitectura es la **responsabilidad compartida** (*shared responsibility*). Esto significa que *todos* los individuos dentro de una empresa (desde la recepcionista hasta el directivo) deben asumir un rol activo para reducir el riesgo. Al tener políticas que capaciten y alienten a los usuarios a reconocer correos maliciosos y reportar problemas de seguridad de inmediato, el equipo de respuesta a incidentes (IR) puede manejar las intrusiones de forma mucho más rápida y efectiva.

## 4. Seguridad de Redes y Comunicaciones (Communication and Network Security)
Este dominio se enfoca en gestionar y asegurar la infraestructura física de las redes corporativas y las comunicaciones inalámbricas (Wi-Fi). Las redes seguras mantienen a salvo los datos, ya sea en los servidores locales (*on-premise*), en la nube pública, o cuando los empleados se conectan de forma remota mediante VPN.

> [!WARNING]
> **El Riesgo del Trabajo Remoto:** Los empleados que trabajan de forma remota en espacios públicos (como aeropuertos o cafeterías) están expuestos a graves vulnerabilidades si utilizan conexiones Bluetooth inseguras o redes Wi-Fi públicas sin cifrar. Para mitigar esto proactivamente, los miembros del equipo de seguridad pueden bloquear administrativamente el acceso a esos canales de comunicación inseguros a nivel de dispositivo (MDM), disuadiendo comportamientos que podrían ser explotados por los atacantes.

Ahora que hemos revisado el enfoque estratégico de nuestros primeros cuatro dominios, ¡pasemos a discutir los últimos cuatro!
