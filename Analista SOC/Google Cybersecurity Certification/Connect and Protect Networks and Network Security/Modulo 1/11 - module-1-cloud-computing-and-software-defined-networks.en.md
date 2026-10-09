# Reading: Cloud computing and software-defined networks

En esta sección del curso, has estado aprendiendo la arquitectura básica de las redes informáticas [cite: 26]. Analizamos cómo los dispositivos físicos de red, como las estaciones de trabajo, los servidores, los routers y los switches se conectan entre sí para dar vida a una infraestructura [cite: 26]. Estas redes pueden cubrir áreas geográficas pequeñas, como es el caso de una red de área local (**LAN**), o pueden extenderse por una región masiva, como una ciudad, estado o país, constituyendo una red de área amplia (**WAN**) [cite: 26]. También introdujimos el concepto de las redes en la nube y cómo la computación en la nube ha crecido exponencialmente en los últimos años [cite: 26].

En esta lectura complementaria, examinaremos con mayor profundidad los conceptos de la computación y las redes en la nube (*cloud networking*) [cite: 26]. También aprenderás sobre las redes híbridas y las redes definidas por software, así como los beneficios operativos que ofrecen [cite: 26]. Esta lectura también cubrirá las ventajas de alojar infraestructuras en la nube y por qué el alojamiento en la nube (*cloud-hosting*) es altamente beneficioso para las grandes organizaciones [cite: 26].

---

## Introducción de los Expertos de Google

Para un analista de seguridad moderno, la nube ya no es una opción de infraestructura, sino el estándar de la industria [cite: 26]. Comprender cómo se procesan los datos de forma remota y cómo se virtualizan los componentes físicos te otorgará las competencias necesarias para auditar perímetros elásticos, configurar herramientas de detección avanzada y mitigar riesgos en arquitecturas dinámicas que cambian en cuestión de segundos [cite: 26].

---

## Desarrollo Temático: Procesos de Computación e Infraestructura Virtual

### Procesos de computación en la nube (*Computing processes in the cloud*)
Las redes tradicionales se denominan **redes locales (*on-premise networks*)**, lo que significa que todos los dispositivos utilizados para las operaciones de red se mantienen resguardados en una ubicación física propiedad de la empresa, como en un edificio de oficinas, por ejemplo [cite: 26]. 

Por el contrario, la **computación en la nube (*cloud computing*)** se refiere a la práctica de utilizar servidores remotos, aplicaciones y servicios de red que están alojados en el internet, en lugar de estar confinados en una ubicación física propiedad de la organización [cite: 26].

Un **Proveedor de Servicios en la Nube (*Cloud Service Provider - CSP*)** es una empresa que ofrece servicios de computación en la nube [cite: 26]. Estas corporaciones son dueñas de centros de datos (*data centers*) masivos distribuidos en ubicaciones estratégicas alrededor de todo el mundo que albergan millones de servidores [cite: 26]. Los centros de datos brindan servicios tecnológicos, tales como almacenamiento y procesamiento (*compute*), a una escala tan gigantesca que pueden vender sus servicios a otras compañías a cambio de una tarifa [cite: 26]. Las empresas clientes pagan exclusivamente por el almacenamiento y los servicios que necesitan, consumiéndolos de forma directa a través de la Interfaz de Programación de Aplicaciones (**API**) o la consola web del CSP [cite: 26].

> [!NOTE]
> Los CSPs clasifican sus servicios en tres grandes modelos o categorías principales [cite: 26]:
> *   **Software como servicio (*Software as a service - SaaS*):** Se refiere a suites de aplicaciones completas operadas y mantenidas de forma directa por el CSP que una compañía puede utilizar de manera remota sin necesidad de instalar o alojar el software en su propia infraestructura [cite: 26].
> *   **Infraestructura como servicio (*Infrastructure as a service - IaaS*):** Se refiere al uso de componentes informáticos virtuales ofrecidos por el CSP [cite: 26]. Esto incluye contenedores virtuales (*virtual containers*) y almacenamiento que se configuran de forma remota a través de la API o la consola web del proveedor [cite: 26]. Los servicios de almacenamiento y procesamiento en la nube pueden utilizarse para operar aplicaciones existentes y otras cargas de trabajo tecnológicas sin requerir modificaciones significativas, o bien, dichas aplicaciones pueden modificarse para aprovechar las características únicas de disponibilidad, rendimiento y seguridad del proveedor [cite: 26].
> *   **Plataforma como servicio (*Platform as a service - PaaS*):** Se refiere a un conjunto de herramientas y entornos que los desarrolladores de software pueden utilizar para diseñar, implementar y probar aplicaciones personalizadas para su empresa [cite: 26]. Estas aplicaciones a medida se diseñan y se acceden directamente en la nube, respondiendo a necesidades de negocio específicas de la organización [cite: 26].

### Entornos de nube híbrida (*Hybrid cloud environments*)
Cuando las organizaciones deciden utilizar los servicios de un CSP además de mantener sus propias computadoras, redes y almacenamiento locales, esta infraestructura se denomina **entorno de nube híbrida (*hybrid cloud environment*)** [cite: 26]. 

Por otra parte, cuando una organización contrata y combina los servicios de más de un CSP de forma simultánea, se le conoce como un **entorno multi-nube (*multi-cloud environment*)** [cite: 26]. La gran mayoría de las organizaciones implementan entornos de nube híbrida para reducir sustancialmente sus costos operativos mientras mantienen un control estricto y directo sobre sus recursos de red más confidenciales [cite: 26].

### Redes definidas por software (*Software-defined networks*)
Los CSPs ofrecen herramientas de redes virtuales que replican con exactitud las funciones de los dispositivos físicos que analizamos previamente [cite: 26]. Las **Redes Definidas por Software (*Software-Defined Networks - SDNs*)** están compuestas por servicios y dispositivos de red virtuales [cite: 26]. Del mismo modo que los proveedores de la nube suministran computadoras virtuales, muchas SDNs proporcionan *switches* virtuales, *routers* virtuales, *firewalls* virtuales y más [cite: 26]. 

En la actualidad, la mayoría de los dispositivos de hardware de red modernos también admiten la virtualización de funciones de red y el enrutamiento definido por software [cite: 26]. Esto significa que incluso los *switches* y *routers* físicos utilizan software especializado para realizar el enrutamiento de paquetes (*packet routing*) [cite: 26]. En el caso específico de las redes en la nube, las herramientas SDN se ejecutan y alojan en servidores de alto rendimiento ubicados directamente dentro del centro de datos del CSP [cite: 26].

---

## Beneficios de la Computación en la Nube y las SDNs

Tres de las razones fundamentales por las cuales la computación en la nube resulta extraordinariamente atractiva para los negocios son su **confiabilidad**, la **reducción de costos** y su **alta escalabilidad** [cite: 26].

### 1. Confiabilidad (*Reliability*)
La confiabilidad en la computación en la nube se fundamenta en el nivel de disponibilidad que poseen los recursos y servicios de la nube, qué tan seguras son sus conexiones cifradas y con qué frecuencia los servicios se mantienen ejecutándose de manera efectiva [cite: 26]. La infraestructura en la nube permite que tanto los empleados como los clientes accedan a los recursos y datos que necesitan de manera consistente y con interrupciones mínimas [cite: 26].

### 2. Costo (*Cost*)
Tradicionalmente, las compañías debían financiar y proveer su propia infraestructura de red local, al menos para gestionar sus conexiones a internet [cite: 26]. Esto implicaba costos iniciales (*upfront costs*) potencialmente masivos para la adquisición de hardware de nivel empresarial [cite: 26]. 

Sin embargo, debido a que los CSPs operan centros de datos a gran escala, tienen la capacidad de ofrecer dispositivos y servicios virtuales a una fracción del costo que requerirían las empresas para instalar, parchar, actualizar y administrar de forma autónoma esos componentes físicos y su software asociado [cite: 26].

### 3. Escalabilidad (*Scalability*)
Otro desafío histórico que enfrentan las empresas con la computación tradicional es la escalabilidad [cite: 26]. Cuando una organización experimenta un incremento repentino en sus necesidades comerciales o picos de tráfico, puede verse obligada a comprar más equipos físicos y licencias de software para mantener el ritmo operativo [cite: 26]. 

Pero, ¿qué sucede si la demanda comercial disminuye drásticamente poco tiempo después? La empresa se quedaría con hardware ocioso sin un volumen de negocio que justifique el gasto incurrcesado [cite: 26]. 

> [!IMPORTANT]
> Los CSPs eliminan por completo este riesgo financiero al permitir consumir servicios bajo un **modelo de utilidad elástica (*elastic utility model*)** según sea necesario [cite: 26]. Esto significa que las empresas pagan única y exclusivamente por lo que necesitan, en el momento exacto en que lo necesitan [cite: 26].

Los cambios en la infraestructura se pueden realizar de manera inmediata a través de las APIs o la consola web del CSP, un proceso muchísimo más rápido que si los técnicos de red tuvieran que cotizar, comprar, cablear y configurar hardware físico nuevo [cite: 26]. 

Por ejemplo, si un analista de seguridad detecta una anomalía y necesita proteger la red corporativa contra una amenaza inminente, puede configurar rápidamente **Firewalls de Aplicaciones Web (*Web Application Firewalls - WAFs*)**, **Sistemas de Detección/Prevención de Intrusiones (*IDS/IPS*)** o *firewalls* que operan en las capas L3/L4 del modelo de red en el momento en que sea necesario, garantizando un rendimiento óptimo y un entorno de red altamente seguro [cite: 26].

---

## Puntos Clave (Key Takeaways)

*   **Modelo de Infraestructura CSP:** Los Proveedores de Servicios en la Nube poseen centros de datos globales masivos con millones de servidores para entregar almacenamiento, procesamiento y herramientas de red a través de internet [cite: 26].
*   **Modelos de Servicio Avanzados:** La computación en la nube distribuye sus capacidades lógicas a través de los tres esquemas estándar de la industria: *SaaS* (software remoto), *IaaS* (componentes y almacenamiento virtual) y *PaaS* (entornos de desarrollo de aplicaciones) [cite: 26].
*   **Entornos de Adopción Híbridos:** Las organizaciones combinan hardware *on-premise* con recursos de un CSP (nube híbrida) o de múltiples proveedores (multi-nube) para optimizar costos sin perder el control sobre sus datos confidenciales [cite: 26].
*   **Agilidad Mediante SDNs:** Las Redes Definidas por Software reemplazan el hardware físico rígido por *switches*, *routers* y *firewalls* virtuales, habilitando configuraciones dinámicas y eficientes programadas por software para mejorar el monitoreo [cite: 26].
*   **Tríada de Beneficios de Negocio:** La adopción de la nube transforma la gestión tecnológica al robustecer la confiabilidad del servicio, disminuir drásticamente los costos operativos y habilitar una escalabilidad elástica inmediata ante amenazas o demandas de tráfico [cite: 26].
