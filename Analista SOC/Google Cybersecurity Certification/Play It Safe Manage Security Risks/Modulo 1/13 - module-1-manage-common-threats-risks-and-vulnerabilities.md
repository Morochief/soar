# Lectura: Manage common threats, risks, and vulnerabilities

Anteriormente, aprendiste que la ciberseguridad corporativa implica proteger a las organizaciones y a las personas de amenazas, riesgos y vulnerabilidades. Comprender el panorama actual de amenazas brinda a las organizaciones la capacidad de crear políticas y procesos diseñados para prevenir y mitigar estos problemas. En esta lectura, explorarás más a fondo cómo gestionar el riesgo y algunas tácticas y técnicas comunes de los actores de amenazas.

## 1. Gestión de Riesgos (Risk Management)
Un objetivo principal de las organizaciones es proteger sus activos. Un activo (*asset*) es un elemento percibido como valioso para una organización. 
Los **activos digitales** incluyen información personal de empleados o clientes (Números de Seguro Social, Fechas de nacimiento, Cuentas bancarias). Los **activos físicos** incluyen quioscos de pago, servidores, computadoras y los propios espacios de oficina.

Algunas estrategias corporativas comunes utilizadas para gestionar los riesgos son:
*   **Aceptación (*Acceptance*):** Aceptar un riesgo para evitar interrumpir la continuidad del negocio (cuando el costo de mitigarlo es mayor que el daño potencial).
*   **Evitación (*Avoidance*):** Crear un plan para evitar por completo el riesgo (ej. cerrar una sucursal en un país hostil).
*   **Transferencia (*Transference*):** Transferir el riesgo a un tercero para que lo gestione (ej. contratar un Seguro de Ciberseguridad o mover los servidores a AWS).
*   **Mitigación (*Mitigation*):** Disminuir el impacto de un riesgo conocido (ej. instalar un Firewall).

Además, las organizaciones implementan marcos de trabajo (*Frameworks*) ampliamente aceptados, como el **NIST RMF** y **HITRUST** (Health Information Trust Alliance), para proteger los activos.

## 2. Amenazas (Threats)
Una amenaza es cualquier circunstancia o evento que pueda impactar negativamente los activos corporativos. Tu trabajo como analista es defender los activos de las amenazas internas y externas. Las amenazas comunes incluyen:
*   **Amenazas internas (*Insider threats*):** Miembros del personal o proveedores externos que abusan de su acceso autorizado para obtener datos que pueden dañar a la organización.
*   **Amenazas persistentes avanzadas (*APTs*):** Un actor de amenazas (usualmente patrocinado por un Estado-Nación) que mantiene acceso no autorizado y silencioso a un sistema durante un período prolongado de tiempo para espiar o robar propiedad intelectual.

## 3. Riesgos (Risks)
Un riesgo es cualquier cosa que pueda afectar la Confidencialidad, Integridad o Disponibilidad (**CIA**) de un activo. Factores que afectan la probabilidad de un riesgo:
*   **Riesgo externo:** Amenazas desde fuera de la organización (Hackers rusos intentando infiltrarse).
*   **Riesgo interno:** Un empleado actual, ex-empleado o socio de confianza que representa un peligro.
*   **Sistemas heredados (*Legacy systems*):** Sistemas antiguos (servidores obsoletos o máquinas expendedoras conectadas a la red) que ya no reciben actualizaciones pero siguen operando.
*   **Riesgo multiparte (*Multiparty risk*):** Subcontratar trabajo a proveedores externos les otorga acceso a propiedad intelectual y secretos comerciales. Si ellos son hackeados, tú eres hackeado (*Supply Chain Attack*).
*   **Cumplimiento/Licencias de software:** Software que no está actualizado, o parches críticos que no se instalan a tiempo.

> [!NOTE]
> **El Top 10 de OWASP:** El Proyecto Abierto de Seguridad de Aplicaciones Web (**OWASP**) publica periódicamente el *Top 10* de los riesgos de seguridad más críticos para aplicaciones web. La reciente actualización incluye riesgos como: diseño inseguro, fallas en la integridad del software, y falsificación de solicitudes del lado del servidor (SSRF). Esto demuestra que debes mantenerte actualizado constantemente.

## 4. Vulnerabilidades Famosas (Vulnerabilities)
Una vulnerabilidad es una debilidad táctica. Por lo tanto, las organizaciones deben inspeccionar regularmente las debilidades dentro de sus sistemas (Gestión de Vulnerabilidades). Algunas de las vulnerabilidades más críticas de los últimos años incluyen:
*   **ProxyLogon:** Una vulnerabilidad pre-autenticada que afecta al servidor Microsoft Exchange. Permite a un actor de amenazas desplegar código malicioso de forma remota.
*   **ZeroLogon:** Una vulnerabilidad en el protocolo de autenticación *Netlogon* de Microsoft.
*   **Log4Shell:** Una pesadilla mundial en la librería de Java. Permite a los atacantes ejecutar código malicioso remoto en computadoras ajenas o filtrar información confidencial tomando el control total del servidor.
*   **PetitPotam:** Afecta al sistema *NTLM* de Windows. Es una técnica de robo que permite a un atacante en la red local (LAN) forzar una autenticación.
*   **Fallas en el registro de seguridad (*Security logging failures*):** Una configuración deficiente de los logs del SIEM, lo que resulta en que los atacantes exploten vulnerabilidades de forma 100% invisible para el equipo SOC.
*   **SSRF (Server-side request forgery):** Permite a los atacantes manipular una aplicación web para acceder y robar bases de datos en los servidores internos (*backend*).

> [!IMPORTANT]
> **Gestión de Vulnerabilidades:** Como analista de Nivel 1, podrías trabajar escaneando sistemas para identificar estas vulnerabilidades. Aunque existan los parches de seguridad, si el departamento de TI no los aplica físicamente a los servidores, las intrusiones ocurrirán. Cuanto antes una organización parcheé un sistema, menor será su ventana de exposición al riesgo.

### Puntos Clave (*Key Takeaways*)
*   Las estrategias para enfrentar el riesgo son 4: Aceptación, Evitación, Transferencia y Mitigación.
*   El **NIST NVD** (Base de Datos Nacional de Vulnerabilidades) y el catálogo de vulnerabilidades explotadas de **CISA** son recursos gratuitos vitales para buscar vulnerabilidades públicas y estar al día con los parches críticos.
