# Lectura: Tools for protecting business operations

Anteriormente te introdujimos a varias habilidades técnicas y herramientas que los analistas de seguridad de *Nivel 1* (*Tier 1*) utilizan a diario. En esta lectura, profundizaremos en cómo los analistas utilizan estas herramientas y procesos formales para mitigar los riesgos de manera metódica y legal.

## El conjunto de herramientas de un analista de Nivel 1
Cada organización proporciona un arsenal (*toolkit*) diferente según su presupuesto y necesidades. Como futuro analista, es vital que comprendas la arquitectura estándar subyacente de estas herramientas para que puedas dominar cualquier variante comercial que te toque usar en tu trabajo.

### Herramientas SIEM (Gestión de Eventos e Información de Seguridad)
Una herramienta SIEM (como Splunk o Sentinel) es una aplicación central que recopila y analiza datos de registros (*logs*) para monitorear actividades críticas en toda la corporación. Dependiendo del volumen de datos, sería imposible que un humano leyera los *logs* por su cuenta. El SIEM procesa terabytes de *logs* en segundos y alerta al analista *solo* cuando detecta vulnerabilidades o ataques.

Las herramientas SIEM proporcionan potentes **paneles visuales** (*dashboards*) que grafican los datos, permitiendo a los equipos de seguridad identificar tendencias rápidamente (ej. un mapa que muestra picos de conexiones provenientes de IPs en Rusia).

Los SIEM se pueden alojar de dos formas:
- **Local (*On-premise*):** El SIEM se instala en los servidores físicos y discos duros que la empresa tiene en su propio edificio. Ofrece control total, pero es carísimo y complejo de mantener.
- **Nube (*Cloud-hosted* / *Cloud-native*):** El SIEM vive en servidores de terceros (como AWS o Google Cloud). Es mucho más fácil de configurar, escalar y mantener, siendo la opción preferida por equipos de seguridad modernos (como Chronicle).

### Analizadores de Protocolos de Red (*Packet Sniffers*)
También conocidos como *rastreadores de paquetes*, son herramientas tácticas diseñadas para interceptar, capturar y desarmar microscópicamente el tráfico de datos que circula por los cables de la red. Esto significa que la herramienta guarda una copia exacta de todo lo que envían y reciben las computadoras. Más adelante usarás Wireshark para practicar esto.

### Los Playbooks de Respuesta
Un *Playbook* es un manual o receta que proporciona detalles milimétricos sobre cómo responder a un incidente de seguridad (ej. "Playbook para Ransomware"). Los playbooks guían a los analistas paso a paso para garantizar que el equipo no actúe por pánico, sino mediante un proceso documentado y auditable.

**Escenario Forense Práctico:**
Imagina que trabajas como analista para una empresa de Respuesta a Incidentes (*Incident Response* o *IR*). Te asignan el caso de un consultorio médico que sufrió un hackeo. Tu trabajo es investigar y proporcionarle evidencia legal a la Compañía de Seguros de Ciberseguridad para determinar si el consultorio tiene derecho a cobrar el seguro.
En este escenario crítico, un error tuyo puede costar millones de dólares. Por eso, al realizar análisis forense, seguirás obligatoriamente dos *Playbooks* universales:

1. **Playbook de Cadena de Custodia (*Chain of Custody*):**
Es el proceso estricto de documentar la posesión y el control de la evidencia física y digital durante toda la investigación. Si confiscas la computadora hackeada, deberás documentar bajo firma de papel: quién te la entregó, a qué hora exacta, dónde se guardó y quién más tiene la llave de esa caja fuerte. **Cada vez que la evidencia se mueve, se debe reportar.** Esto garantiza ante un juez que la evidencia nunca fue manipulada por terceros.

2. **Playbook de Preservación de Evidencias (*Protecting and preserving evidence*):**
Es el proceso de trabajar con pruebas digitales frágiles. Al investigar, aplicarás estrictamente el **Orden de Volatilidad** (*Order of Volatility*), una regla forense inquebrantable que dicta que *siempre* debes capturar primero los datos que estén a punto de desaparecer (datos volátiles). Por ejemplo, tu primera acción será capturar la Memoria RAM de la computadora infectada, porque si la máquina se apaga, el contenido de la RAM se pierde para siempre y la evidencia del atacante desaparece.
Además, la regla de oro de este playbook exige que **jamás investigues sobre el equipo original**. Siempre debes usar software especial para crear una copia bit-a-bit exacta del disco duro (*imagen forense*), guardar el original bajo llave, y jugar únicamente con las copias.

---

## Puntos Clave (Key Takeaways)
- El **SIEM** es la herramienta principal que un analista usa para monitorear toda la red, alojado en servidores locales (*On-premise*) o en la nube (*Cloud*).
- Los **Packet Sniffers** (como Wireshark) son las lupas que usas para leer el tráfico crudo de la red.
- Durante un ataque, tu accionar estará dictado estrictamente por **Playbooks** (manuales corporativos de respuesta).
- En análisis forense, la **Cadena de Custodia** demuestra que no alteraste la evidencia, y el **Orden de Volatilidad** te obliga a salvar la Memoria RAM antes de que alguien apague la computadora.
