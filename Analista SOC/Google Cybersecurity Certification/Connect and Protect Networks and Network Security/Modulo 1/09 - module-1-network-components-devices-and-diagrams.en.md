# Network components, devices, and diagrams

En esta lectura complementaria, repasarás los dispositivos de red, sus conexiones e investigarás un diagrama de red simple similar a los utilizados diariamente por los profesionales de la seguridad de redes [cite: 26]. Una comprensión fundamental de la arquitectura de red —a veces denominada diseño de red (*network design*)— te ayudará a medida que aprendes sobre las vulnerabilidades de seguridad inherentes a todas las redes y cómo los actores maliciosos intentan explotarlas [cite: 26]. ¡Comencemos! [cite: 26]

---

## Introducción de los Expertos de Google

Para un analista de seguridad, la red representa el campo de batalla principal donde se transportan los datos de la organización [cite: 26]. Comprender los componentes individuales y saber interpretar un mapa o diagrama de infraestructura te permitirá identificar puntos ciegos lógicos, evaluar configuraciones de seguridad defectuosas e interrumpir los vectores de ataque antes de que comprometan los activos críticos del negocio [cite: 26].

---

## Desarrollo Temático: Componentes e Infraestructura de Red

### Dispositivos de red (*Network devices*)
Los dispositivos de red mantienen la información y los servicios disponibles para los usuarios [cite: 26]. Estos componentes se interconectan mediante conexiones cableadas e inalámbricas [cite: 26]. Una vez que establecen una conexión estable a la red, los dispositivos envían paquetes de datos (*data packets*) [cite: 26]. 

Los paquetes de datos proporcionan información esencial sobre el origen (fuente) y el destino final de la información [cite: 26]. Así es precisamente como se envía y recibe la información a través de los diferentes componentes de un sistema [cite: 26].

> [!NOTE]
> La **red** es la infraestructura general que permite que los dispositivos se comuniquen entre sí [cite: 26]. Los **dispositivos de red** son vehículos especializados (como *routers* y *switches*) encargados de gestionar minuciosamente qué se envía y se recibe a través de la red [cite: 26]. Adicionalmente, las terminales de uso común, como computadoras y teléfonos, se conectan a la red general a través de estos dispositivos especializados [cite: 26].

A nivel de diseño de infraestructura, un *router* típico se conecta al internet exterior a través de un módem suministrado por el Proveedor de Servicios de Internet (**ISP** - *Internet Service Provider*) [cite: 26]. Un *firewall* se sitúa estratégicamente como un dispositivo de seguridad para monitorear todo el tráfico entrante y saliente [cite: 26]. Luego, el *router* dirige el tráfico hacia las estaciones internas de la red doméstica o corporativa (computadoras, *laptops*, teléfonos inteligentes, tabletas e impresoras) [cite: 26]. 

Si la red incorpora un servidor de archivos (*file server*), todos los dispositivos autorizados en esa red pueden acceder a los archivos centralizados en él [cite: 26]. Asimismo, se puede integrar un *switch* de forma opcional para conectar más dispositivos proporcionando puertos adicionales y conexiones Ethernet físicas [cite: 26]. En entornos avanzados, es común conectar dos *routers* al mismo *switch* con fines de balanceo de carga (*load balancing*), optimizando el rendimiento y la tolerancia a fallos del sistema [cite: 26].

### Dispositivos y computadoras de escritorio (*Devices and desktop computers*)
La mayoría de los usuarios de internet están familiarizados con las terminales cotidianas como computadoras personales, computadoras portátiles, teléfonos móviles y tabletas [cite: 26]. 
*   Cada dispositivo y computadora de escritorio posee una dirección MAC (*MAC address*) única y una dirección IP (*IP address*) que lo identifica inequívocamente en la red [cite: 26].
*   Cuentan con una interfaz de red (*network interface*) diseñada para enviar y recibir paquetes de datos [cite: 26].
*   Tienen la capacidad de conectarse a la infraestructura mediante un cable físico físico (*hard wire*) o a través de una conexión inalámbrica [cite: 26].

### Firewalls
Un **firewall** es un dispositivo de seguridad de red que monitorea de manera continua el tráfico hacia o desde tu red [cite: 26]. Actúa directamente como tu primera línea de defensa perimetral [cite: 26]. 

> [!IMPORTANT]
> Los *firewalls* tienen la facultad de restringir o bloquear tráfico de red específico entrante y saliente basándose en reglas de seguridad (*security rules*) previamente configuradas por la organización [cite: 26]. Con frecuencia se ubican entre la red interna segura y controlada y los recursos de red externos no confiables, como el internet público [cite: 26]. Sin embargo, recuerda que los *firewalls* son solo una línea de defensa dentro del amplio panorama de la ciberseguridad [cite: 26].

### Servidores (*Servers*)
Los servidores proveen información y servicios esenciales para los dispositivos conectados a la red [cite: 26]. Los dispositivos que realizan solicitudes a un servidor se denominan **clientes (*clients*)** [cite: 26]. Este flujo operativo da forma al denominado **modelo cliente-servidor (*client-server model*)** [cite: 26].

En este esquema, los clientes envían solicitudes al servidor requiriendo información o servicios específicos, y el servidor procesa y ejecuta dichas solicitudes para satisfacer al cliente [cite: 26]. Algunos ejemplos comunes en la industria incluyen:
*   **Servidores DNS:** Realizan búsquedas y resoluciones de nombres de dominio para sitios de internet [cite: 26].
*   **Servidores de archivos (*File servers*):** Almacenan y recuperan archivos desde una base de datos centralizada [cite: 26].
*   **Servidores de correo corporativo:** Organizan y gestionan el flujo de mensajería electrónica para una empresa [cite: 26].

### Hubs y switches
Tanto los *hubs* como los *switches* se encargan de dirigir el tráfico de datos dentro de una red local [cite: 26]. Un **hub** (concentrador) es un dispositivo que proporciona un punto común de conexión para todos los equipos directamente conectados a él [cite: 26]. Los *hubs* poseen la característica de repetir de forma indiscriminada toda la información entrante hacia absolutamente todos sus puertos de salida [cite: 26].

Desde una perspectiva estricta de seguridad, esta replicación masiva vuelve a los *hubs* sumamente vulnerables a la interceptación o escucha no autorizada de datos (*eavesdropping*) [cite: 26]. Por esta razón, los *hubs* ya no se utilizan en las redes modernas; la gran mayoría de las organizaciones los han sustituido por *switches* [cite: 26]. Su uso actual queda relegado a configuraciones de red muy limitadas o laboratorios pequeños, como oficinas en casa [cite: 26].

Por el contrario, los **switches** son la opción preferida para la mayoría de las infraestructuras corporativas [cite: 26]. Un *switch* reenvía paquetes únicamente entre los dispositivos que están conectados de forma directa a él [cite: 26]. Analizan detalladamente la dirección de destino de cada paquete de datos y lo transmiten exclusivamente al dispositivo intencionado [cite: 26].

Para lograr esto, los *switches* mantienen internamente una **tabla de direcciones MAC (*MAC address table*)** que empareja las direcciones físicas de los dispositivos de la red con los números de puerto físico del propio *switch*, enrutando los paquetes entrantes según corresponda [cite: 26]. En el modelo de referencia TCP/IP, los *switches* operan principalmente dentro de la **capa de enlace de datos (*data link layer*)** [cite: 26]. Su implementación mejora significativamente tanto el rendimiento operativo como la seguridad de la red [cite: 26].

### Routers
Los **routers** conectan múltiples redes entre sí y dirigen el tráfico basándose en la dirección IP de la red de destino [cite: 26]. Permiten que dispositivos situados en redes completamente diferentes e independientes se comuniquen entre sí [cite: 26]. Dentro del modelo TCP/IP, los *routers* forman parte de la **capa de red (*network layer*)** [cite: 26].

La dirección IP de la red de destino viene incrustada dentro del encabezado IP (*IP header*) del paquete [cite: 26]. El *router* lee esta información del encabezado y reenvía el paquete al siguiente *router* en la ruta idónea hacia el destino final, repitiéndose este proceso de forma sucesiva hasta que el paquete alcanza la red objetivo [cite: 26]. Adicionalmente, muchos *routers* modernos incluyen funciones de *firewall* integradas que permiten bloquear o admitir tráfico entrante según la información de la transmisión, deteniendo el tráfico malicioso antes de que ingrese a la red privada y dañe la red de área local (*LAN*) [cite: 26].

### Módems y puntos de acceso inalámbrico (*Modems and wireless access points*)
Los **módems** conectan la infraestructura del hogar o de la oficina con el Proveedor de Servicios de Internet (ISP) [cite: 26]. Los ISPs entregan conectividad a internet mediante líneas telefónicas, cables coaxiales o cables de fibra óptica [cite: 26]. El módem recibe las transmisiones o señales analógicas/digitales desde el internet exterior y las convierte a un formato digital compatible con la conexión física de la empresa [cite: 26]. Generalmente, los módems se conectan directamente a un *router*, el cual toma las transmisiones decodificadas y las distribuye hacia la red local [cite: 26].

> [!NOTE]
> Las redes empresariales (*enterprise networks*) utilizadas por grandes organizaciones para conectar a miles de usuarios y dispositivos suelen emplear tecnologías de banda ancha dedicadas de alta velocidad para manejar grandes volúmenes de tráfico, prescindiendo habitualmente del uso de un módem tradicional [cite: 26].

Un **punto de acceso inalámbrico (*Wireless Access Point - WAP*)** envía y recibe señales digitales a través de ondas de radio, creando una red inalámbrica dedicada [cite: 26]. Los dispositivos equipados con adaptadores inalámbricos se conectan al punto de acceso mediante el uso de **Wi-Fi** (el cual se refiere a un conjunto de estándares de la industria utilizados por los componentes de red para comunicarse sin cables) [cite: 26]. Los puntos de acceso inalámbrico y sus clientes asociados emplean protocolos Wi-Fi específicos para transmitir datos mediante ondas de radio, los cuales se envían posteriormente hacia los *routers* y *switches* para ser dirigidos a su destino final [cite: 26].

---

## Uso de Diagramas de Red como Analista de Seguridad

Los **diagramas de red (*network diagrams*)** permiten a los administradores de redes y al personal del SOC visualizar de forma clara la arquitectura y el diseño de la red privada de su organización [cite: 26]. 

Los diagramas de red funcionan como mapas detallados que muestran con precisión qué dispositivos residen en la red y cómo se conectan entre sí [cite: 26]. Utilizan gráficos e íconos representativos pequeños para retratar cada dispositivo de red (computadoras, firewalls, routers) y líneas continuas o punteadas para ilustrar el medio de conexión e interrelación entre ellos [cite: 26]. Al estudiar minuciosamente los diagramas de red, los analistas de seguridad pueden desarrollar, auditar y refinar sus estrategias defensivas para robustecer la seguridad de las arquitecturas de red [cite: 26].

---

## Puntos Clave (Key Takeaways)

*   **Modelo Cliente-Servidor:** En este esquema operativo, el cliente genera solicitudes de información y servicios, y el servidor centralizado se encarga de procesar, validar y ejecutar dichas peticiones [cite: 26].
*   **Dispositivos de Infraestructura:** Una red sólida se compone de una variedad de componentes especializados, incluyendo estaciones de trabajo, servidores, *firewalls*, *routers*, *switches* y módems [cite: 26].
*   **Aislamiento de Tráfico con Switches:** A diferencia de los *hubs* (que replican datos de forma insegura a todos los puertos), los *switches* operan en la capa de enlace de datos utilizando tablas de direcciones MAC para enviar información exclusivamente al destinatario legítimo [cite: 26].
*   **Enrutamiento Inteligente:** Los *routers* funcionan en la capa de red del modelo TCP/IP, leyendo los encabezados IP de los paquetes para dirigir el tráfico de datos entre redes completamente independientes [cite: 26].
*   **Mapas de Red para el SOC:** Los analistas de seguridad utilizan los diagramas de red como herramientas visuales indispensables para mapear la arquitectura interna, identificar perímetros expuestos y optimizar los controles defensivos [cite: 26].
