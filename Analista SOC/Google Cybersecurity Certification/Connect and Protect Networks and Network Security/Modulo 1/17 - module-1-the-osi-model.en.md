# Reading: The OSI model

Hasta ahora en esta sección del curso, has aprendido sobre los componentes de una red, los dispositivos de red y cómo ocurre la comunicación a través de ella [cite: 25]. También estudiaste el modelo TCP/IP para comprender cómo se organiza la comunicación de red en las diferentes capas de internet [cite: 25].

---

## Contexto de los Expertos de Google

Toda la comunicación en una red se organiza mediante protocolos de red [cite: 25]. Anteriormente, aprendiste sobre el Protocolo de Control de Transmisión (*Transmission Control Protocol* o TCP), que establece conexiones entre dos dispositivos, y el Protocolo de Internet (*Internet Protocol* o IP), que se utiliza para el enrutamiento y direccionamiento de paquetes de datos (*data packets*) a medida que viajan entre dispositivos en una red [cite: 25]. Estos protocolos se utilizan en capas de internet específicas dentro del modelo TCP/IP [cite: 25]. 

El modelo TCP/IP de 4 capas es una versión condensada del modelo de Interconexión de Sistemas Abiertos (*Open Systems Interconnection* o OSI), el cual está compuesto por 7 capas [cite: 25]. El modelo OSI te proporcionará una comprensión más profunda de los procesos que ocurren en cada nivel [cite: 25]. Trabajaremos a la inversa, desde la capa siete hasta la capa uno, abarcando desde los procesos que involucran la interacción directa del usuario con la red hasta aquellos que implican la conexión física a internet a través de componentes de red como cables y *switches* [cite: 25]. Esta lectura también repasará las principales diferencias entre los modelos TCP/IP y OSI [cite: 25].

---

## Desarrollo Temático: Modelo TCP/IP vs. Modelo OSI

El modelo TCP/IP es un marco de trabajo (*framework*) utilizado para visualizar cómo se organizan y transmiten los datos a través de una red [cite: 25]. Este modelo ayuda a los ingenieros de redes y a los analistas de seguridad a conceptualizar los procesos en la red y a comunicar dónde ocurren las interrupciones o las amenazas de seguridad [cite: 25]. 

El modelo TCP/IP tiene cuatro capas: la capa de acceso a la red, la capa de internet, la capa de transporte y la capa de aplicación [cite: 25]. Al analizar eventos de red, los profesionales de la seguridad pueden determinar en qué capa o capas ocurrió un ataque basándose en qué procesos estuvieron involucrados en el incidente [cite: 25].

Por otro lado, el modelo OSI es un concepto estandarizado que describe las siete capas que las computadoras utilizan para comunicarse y enviar datos a través de la red [cite: 25]. Los profesionales de redes y ciberseguridad a menudo utilizan este modelo para comunicarse entre sí sobre las fuentes potenciales de problemas o amenazas de seguridad cuando estas ocurren [cite: 25].

> [!NOTE]
> Algunas organizaciones confían en gran medida en el modelo TCP/IP, mientras que otras prefieren utilizar el modelo OSI [cite: 25]. Como analista de seguridad, es importante estar familiarizado con ambos modelos, ya que ambos son útiles para comprender cómo funcionan las redes [cite: 25].

---

## Análisis Profundo de las 7 Capas del Modelo OSI

### Capa 7: Capa de aplicación (*Application layer*)
La capa de aplicación incluye procesos que involucran directamente al usuario cotidiano [cite: 25]. Esta capa engloba todos los protocolos de red que las aplicaciones de software utilizan para conectar a un usuario a internet [cite: 25]. Esta característica es el elemento identificativo de la capa de aplicación: la conexión del usuario a internet mediante aplicaciones y solicitudes [cite: 25].

*   **Navegación Web:** Un ejemplo de comunicación en la capa de aplicación es el uso de un navegador web [cite: 25]. El navegador de internet utiliza HTTP o HTTPS para enviar y recibir información desde el servidor del sitio web [cite: 25].
*   **Correo Electrónico:** La aplicación de correo electrónico utiliza el Protocolo Simple de Transferencia de Correo (*Simple Mail Transfer Protocol* o SMTP) para enviar y recibir información de correos [cite: 25].
*   **Resolución de Nombres:** Los navegadores web utilizan el protocolo del Sistema de Nombres de Dominio (*Domain Name System* o DNS) para traducir los nombres de dominio de los sitios web en direcciones IP, las cuales identifican al servidor web que aloja la información del sitio [cite: 25].

### Capa 6: Capa de presentación (*Presentation layer*)
Las funciones en la capa de presentación involucran la traducción y el cifrado de datos para la red [cite: 25]. Esta capa añade y reemplaza datos con formatos que puedan ser comprendidos por las aplicaciones (capa 7) tanto en el sistema emisor como en el receptor [cite: 25]. Los formatos en el extremo del usuario pueden ser diferentes de los del sistema receptor, por lo que los procesos en la capa de presentación requieren el uso de un formato estandarizado [cite: 25].

> [!IMPORTANT]
> Algunas funciones de formato que ocurren en la capa 6 incluyen el cifrado, la compresión y la confirmación de que el conjunto de códigos de caracteres puede ser interpretado en el sistema receptor [cite: 25]. Un ejemplo de cifrado que tiene lugar en esta capa es SSL, que cifra los datos entre los servidores web y los navegadores como parte de los sitios web con HTTPS [cite: 25].

### Capa 5: Capa de sesión (*Session layer*)
Una sesión describe el momento en que se establece una conexión entre dos dispositivos [cite: 25]. Una sesión abierta permite que los dispositivos se comuniquen entre sí [cite: 25]. Los protocolos de la capa de sesión mantienen la sesión abierta mientras se transfieren los datos y la terminan una vez que la transmisión se ha completado [cite: 25].

*   **Responsabilidades:** La capa de sesión también es responsable de actividades como la autenticación, la reconexión y el establecimiento de puntos de control (*checkpoints*) durante una transferencia de datos [cite: 25].
*   **Resiliencia:** Si una sesión se interrumpe, los puntos de control aseguran que la transmisión se reanude en el último punto de control de la sesión cuando se restablezca la conexión [cite: 25]. 
*   **Interacción:** Las sesiones incluyen una solicitud y una respuesta entre aplicaciones [cite: 25]. Las funciones en la capa de sesión responden a las solicitudes de servicio de los procesos en la capa de presentación (capa 6) y envían solicitudes de servicios a la capa de transporte (capa 4) [cite: 25].

### Capa 4: Capa de transporte (*Transport layer*)
La capa de transporte es responsable de entregar los datos entre los dispositivos [cite: 25]. Esta capa también maneja la velocidad de la transferencia de datos, el flujo de la transferencia y la división de los datos en segmentos más pequeños para facilitar su transporte [cite: 25].

*   **Segmentación:** Es el proceso de dividir una gran transmisión de datos en piezas más pequeñas que puedan ser procesadas por el sistema receptor [cite: 25]. Estos segmentos deben ser reensamblados en su destino para que puedan ser procesados en la capa de sesión (capa 5) [cite: 25].
*   **Sincronización:** La velocidad y el ritmo de la transmisión también deben coincidir con la velocidad de conexión del sistema de destino [cite: 25]. TCP y UDP son protocolos de la capa de transporte [cite: 25].

### Capa 3: Capa de red (*Network layer*)
La capa de red supervisa la recepción de las tramas (*frames*) provenientes de la capa de enlace de datos (capa 2) y las entrega al destino previsto [cite: 25]. El destino previsto se puede encontrar basándose en la dirección que reside en la trama de los paquetes de datos [cite: 25]. Los paquetes de datos permiten la comunicación entre dos redes [cite: 25]. Estos paquetes incluyen direcciones IP que indican a los *routers* hacia dónde enviarlos, siendo enrutados desde la red emisora hasta la red receptora [cite: 25].

### Capa 2: Capa de enlace de datos (*Data link layer*)
La capa de enlace de datos organiza el envío y la recepción de paquetes de datos dentro de una sola red [cite: 25]. La capa de enlace de datos es el hogar de los *switches* en la red local y de las tarjetas de interfaz de red (*Network Interface Cards* o NIC) en los dispositivos locales [cite: 25]. Protocolos como el Protocolo de Control de Red (*Network Control Protocol* o NCP), el Control de Enlace de Datos de Alto Nivel (*High-level Data Link Control* o HDLC) y el protocolo de Control de Enlace de Datos Síncrono (*Synchronous Data Link Control* o SDLC) se utilizan en esta capa [cite: 25].

### Capa 1: Capa física (*Physical layer*)
Como su nombre indica, la capa física corresponde al hardware físico involucrado en la transmisión de la red [cite: 25]. Los *hubs*, los módems y los cables y el cableado que los conectan se consideran parte de la capa física [cite: 25]. Para viajar a través de un cable Ethernet o coaxial, un paquete de datos debe traducirse en un flujo de unos y ceros (0s y 1s) [cite: 25]. Este flujo de 0s y 1s se envía a través del cableado y los cables físicos, se recibe y luego se pasa a los niveles superiores del modelo OSI [cite: 25].

---

## Puntos Clave (Key Takeaways)

*   **Modelos Conceptuales:** Tanto el modelo TCP/IP como el OSI son modelos conceptuales que ayudan a los profesionales de redes a diseñar procesos y protocolos de red con respecto a la transmisión de datos entre dos o más sistemas [cite: 25].
*   **Estructura OSI:** El modelo OSI contiene siete capas de comunicación [cite: 25]. Los profesionales de redes y seguridad utilizan el modelo OSI para comunicarse entre sí sobre las posibles fuentes de problemas o amenazas de seguridad cuando estas ocurren [cite: 25].
*   **Herramienta de Diagnóstico:** Los ingenieros de redes y los analistas de seguridad utilizan los modelos TCP/IP y OSI para conceptualizar los procesos de la red y comunicar la ubicación exacta de las interrupciones o amenazas [cite: 25].
