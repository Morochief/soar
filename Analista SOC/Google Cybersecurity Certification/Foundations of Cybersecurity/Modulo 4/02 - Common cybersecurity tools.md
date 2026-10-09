# Common cybersecurity tools

## La Evidencia: Los Registros (*Logs*)
Antes de discutir las herramientas defensivas, hablemos brevemente de los **registros (*logs*)**, ya que son la materia prima, la sangre, que alimenta a todas esas herramientas.

Un *log* es simplemente un registro en texto de los eventos que ocurren dentro de un sistema (por ejemplo, a qué hora un empleado inició sesión, qué archivo abrió o a qué IP de internet se conectó). En ciberseguridad, los *logs* son tu evidencia forense absoluta. Son lo que te permite rastrear los pasos de un atacante.

## El Cerebro del SOC: Herramientas SIEM
La primera herramienta, y el software en el que pasarás el 90% de tu carrera, es el **SIEM** (Gestión de Información y Eventos de Seguridad).

Una herramienta SIEM (pronunciada comúnmente como *"sim"*) es una aplicación masiva que recolecta, centraliza y analiza todos los *logs* de miles de computadoras, servidores y *firewalls* de la organización al mismo tiempo.

Imagina tener que leer millones de líneas de texto plano manualmente en cientos de computadoras para determinar si hay una amenaza. Sería imposible. Las herramientas SIEM reducen la cantidad de datos que un analista debe revisar al procesar todos esos *logs* en tiempo real, cruzarlos con inteligencia de amenazas y lanzarte **alertas automatizadas** si detectan un patrón de ataque.

### SIEMs Populares en la Industria
- **Splunk:** Es una plataforma monstruosa de análisis de datos y el SIEM más famoso del mundo. *Splunk Enterprise* a menudo se aloja en los propios servidores físicos de la corporación (*self-hosted*).
- **Chronicle (Google SecOps):** Es el SIEM moderno de Google. A diferencia del Splunk tradicional, Chronicle es **nativo de la nube** (*cloud-native*), utilizando la misma infraestructura que el buscador de Google para rastrear *logs* a velocidades impensables.

## Herramientas Adicionales del SOC

### Playbooks (Manuales de Respuesta)
Un *Playbook* es literalmente un manual de instrucciones o receta paso a paso que proporciona detalles sobre cómo responder a un incidente. 
En medio de un ciberataque masivo, el pánico es tu peor enemigo. Los *playbooks* eliminan el pánico guiando a los analistas rígidamente sobre cómo manejar la amenaza antes, durante y después del ataque, garantizando que el equipo técnico cumpla con las leyes y las políticas.

### Analizadores de Protocolos de Red (*Packet Sniffers*)
Un *packet sniffer* o Analizador de Red, es una herramienta táctica diseñada para interceptar, capturar y analizar el tráfico crudo que viaja por los cables o el Wi-Fi de tu red. Te permiten "pinchar" la red para ver exactamente qué se están diciendo las computadoras.
Los reyes indiscutibles de la industria en este rubro son **tcpdump** (una herramienta de comandos para la terminal de Linux) y **Wireshark** (la versión gráfica estándar para Windows y Linux).

---

## Puntos Clave (Key Takeaways)
- El **Log** es la evidencia (ej. "El usuario X se logueó a las 03:00 AM").
- El **SIEM** es el motor que lee millones de logs y te lanza una **Alerta** roja en pantalla si ese *log* es peligroso. Ejemplos: Splunk y Chronicle.
- Los **Playbooks** son las recetas de respuesta a incidentes. Te dicen paso a paso a quién llamar y qué cable desconectar.
- **Wireshark** y **tcpdump** son interceptores de red. Permiten al analista husmear dentro de los paquetes de datos que viajan por el cable de red.
