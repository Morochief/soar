# IP addresses and network communication

¡Hola de nuevo! Continuamos avanzando con entusiasmo en el Módulo 1. Una vez que hemos analizado cómo se estructuran las capas del modelo de red, es momento de estudiar los identificadores lógicos y físicos que permiten que la información encuentre su destino exacto a través del internet global [cite: 17, 26].

---

## Introducción del Instructor

Mi nombre es **Chris** y soy el Director de Seguridad de la Información (*Chief Information Security Officer* o CISO) en **Google Fiber** [cite: 25]. A lo largo de mi trayectoria en la administración de redes, he visto cómo el correcto direccionamiento es el núcleo perimetral de la ciberseguridad [cite: 24, 26]. En esta clase, analizaremos el rol indispensable de las direcciones IP y MAC en la comunicación de red [cite: 26].

---

## Desarrollo Temático: Direccionamiento en Redes Informáticas

### ¿Qué es una Dirección IP?
Una dirección de Protocolo de Internet o **dirección IP (*IP address*)** es una cadena única de caracteres que identifica de forma inequívoca la ubicación de un dispositivo en el internet exterior [cite: 26]. 

Para comprenderlo de forma sencilla, cada dispositivo conectado a internet posee una dirección IP única, operando de manera muy similar a cómo cada casa en una calle tiene su propia dirección postal física para recibir correspondencia [cite: 26].

### Evolución de los Estándares: IPv4 vs. IPv6
En el ecosistema tecnológico actual, coexisten dos tipos fundamentales de direcciones IP [cite: 26]:

*   **IP Versión 4 (IPv4):** Se escriben como un conjunto de cuatro números (de 1, 2 o 3 dígitos cada uno) separados formalmente por puntos decimales (ej. `192.168.1.1`) [cite: 26]. En los inicios del internet, todas las conexiones dependían exclusivamente de IPv4 [cite: 26]. Sin embargo, a medida que el uso de la tecnología se masificó a nivel mundial, las direcciones IPv4 disponibles comenzaron a agotarse, lo que impulsó el desarrollo de un nuevo estándar [cite: 26].
*   **IP Versión 6 (IPv6):** Están compuestas técnicamente por 32 caracteres (organizados en notación hexadecimal) [cite: 26]. La gran longitud y estructura de las direcciones IPv6 permite interconectar una cantidad exponencialmente mayor de dispositivos a internet, evitando que la industria se quede sin direcciones tan rápido como sucedió con IPv4 [cite: 26].

---

## Segmentación del Tráfico: Direcciones Públicas y Privadas

Las direcciones IP también se clasifican según su visibilidad y alcance dentro y fuera de la organización [cite: 26]:

### 1. Direcciones IP Públicas (*Public IP addresses*)
Tu Proveedor de Servicios de Internet (ISP) se encarga de asignar una dirección IP pública que está directamente vinculada a tu ubicación geográfica real [cite: 26]. Cuando las comunicaciones de red salen de tus dispositivos hacia el internet, absolutamente todas comparten la misma dirección de cara al exterior [cite: 26].

> [!NOTE]
> **La analogía de los compañeros de casa:** Así como todos los compañeros de cuarto en un mismo hogar comparten exactamente la misma dirección postal en sus sobres, todos los dispositivos conectados a una misma red local comparten la misma dirección IP pública hacia el mundo exterior [cite: 26].

### 2. Direcciones IP Privadas (*Private IP addresses*)
Las direcciones IP privadas solo son visibles para otros dispositivos que residen dentro de la misma red local (*LAN*) [cite: 26]. Esto significa que todas las computadoras y terminales de tu red interna pueden comunicarse entre sí utilizando direcciones IP únicas y dedicadas que el resto del internet no puede ver ni acceder de forma directa, añadiendo una capa base de aislamiento perimetral [cite: 26].

---

## Direccionamiento Físico: La Dirección MAC y la Tabla del Switch

Existe otro tipo de identificador crítico en las comunicaciones de red que opera a nivel físico: la **dirección MAC (*MAC address*)** [cite: 26]. Una dirección MAC es un identificador alfanumérico único e inmutable grabado de fábrica que se asigna a cada interfaz o dispositivo físico en una red [cite: 26].

> [!IMPORTANT]
> Cuando un *switch* local recibe un paquete de datos, lee el encabezado para identificar la dirección MAC del dispositivo de destino legítimo y la mapea de forma inmediata con un puerto físico específico [cite: 26]. Posteriormente, el *switch* almacena esta relación técnica dentro de su **tabla de direcciones MAC (*MAC address table*)** [cite: 26].

Puedes visualizar la tabla de direcciones MAC como una agenda de contactos inteligente que el *switch* consulta de forma continua en milisegundos para dirigir los paquetes de datos exclusivamente al dispositivo que le corresponde, optimizando el rendimiento y bloqueando la interceptación de datos en la red local [cite: 26].

---

## Puntos Clave (Key Takeaways)

*   **Identificación Lógica (IP):** Una dirección IP es la cadena única de caracteres encargada de identificar de forma lógica la ubicación de un dispositivo a través de internet [cite: 26].
*   **Mitigación de Agotamiento (IPv6):** Ante el agotamiento inminente de los bloques numéricos de IPv4, el estándar IPv6 introduce una estructura de 32 caracteres hexadecimales para soportar de manera escalable miles de millones de nuevos dispositivos conectados [cite: 26].
*   **Perímetro Público vs. Privado:** El tráfico externo se consolida bajo una única IP pública asignada por el ISP, mientras que los activos internos se comunican de manera aislada y confidencial mediante direcciones IP privadas invisibles para el internet exterior [cite: 26].
*   **Identificación Física (MAC):** La dirección MAC actúa como el identificador alfanumérico físico único e imborrable de cada tarjeta de red en la infraestructura [cite: 26].
*   **Conmutación Eficiente:** Los *switches* interceptan y examinan las direcciones MAC de destino para poblar su *MAC address table*, actuando como un libro de direcciones interno para enrutar los paquetes de datos de forma directa y segura al puerto legítimo [cite: 26].
