# Components of network layer communication

En la lectura previa sobre el modelo OSI, aprendiste acerca de las siete capas que se utilizan para conceptualizar la manera en que los datos se transmiten a través de internet [cite: 24]. En esta lectura complementaria, profundizarás en las operaciones técnicas que ocurren específicamente en la **capa 3 del modelo OSI: la capa de red (*network layer*)** [cite: 24].

---

## Introducción del Equipo de Google

Aprender a interpretar los componentes de la capa de red es una de las habilidades más críticas para un analista de seguridad dentro del Centro de Operaciones de Seguridad (**SOC**) [cite: 24]. Cada paquete de datos que atraviesa el perímetro corporativo lleva consigo metadatos que revelan su origen, su comportamiento esperado y sus intenciones [cite: 24]. Dominar la anatomía de estos paquetes te permitirá detectar anomalías, identificar suplantaciones de identidad y tomar decisiones defensivas en tiempo real para salvaguardar la infraestructura de tu organización [cite: 24].

---

## Desarrollo Temático: Operaciones en la Capa de Red

Las funciones en la capa de red organizan el direccionamiento lógico y la entrega de los paquetes de datos (*data packets*) a través de la infraestructura, desde el dispositivo emisor o *host* hasta el dispositivo de destino [cite: 24]. Esto incluye guiar y dirigir los paquetes de un *router* a otro a través de internet, hasta que alcancen la dirección de Protocolo de Internet o dirección IP (*IP address*) de la red de destino legítima [cite: 24].

La dirección IP de destino se encuentra resguardada dentro del encabezado (*header*) de cada paquete de datos [cite: 24]. Esta dirección se almacenará en las **tablas de enrutamiento (*routing tables*)** de los *routers* a lo largo de la ruta del paquete para optimizar futuros procesos de entrega [cite: 24].

Todos los paquetes de datos incluyen una dirección IP [cite: 24]. Dependiendo del protocolo de la capa de transporte que se utilice, un paquete de datos también recibe nombres específicos en la industria [cite: 24]:
*   **Paquete IP (*IP packet*):** Cuando se emplean conexiones orientadas a la conexión mediante TCP [cite: 24].
*   **Datagrama (*Datagram*):** Cuando se emplean transmisiones sin conexión mediante UDP [cite: 24].

Un *router* lee la dirección IP contenida en el encabezado de un paquete de datos para dirigirlo de una red a otra [cite: 24]. Sin embargo, la información del encabezado comunica mucho más que la simple dirección de destino; también incluye datos críticos como la dirección IP de origen, el tamaño total del paquete y qué protocolo específico se utilizará para la porción de datos del paquete [cite: 24].

---

## Estructura y Formato de un Paquete IPv4

Un paquete IP versión 4 (IPv4) está constituido por dos grandes secciones: **el encabezado (*header*)** y **los datos (*data*)** [cite: 24].

*   **El encabezado IPv4:** Su formato está estrictamente determinado por el protocolo IPv4 e incluye la información de enrutamiento IP que los dispositivos utilizan para dirigir el paquete [cite: 24]. El tamaño de este encabezado varía de **20 a 60 bytes** [cite: 24]. Los primeros 20 bytes son fijos y contienen datos esenciales como las direcciones IP de origen y destino, la longitud del encabezado y la longitud total del paquete [cite: 24]. Los bytes restantes (de 0 a 40 bytes) corresponden al campo de opciones (*options field*) [cite: 24].
*   **La sección de datos:** La longitud de este segmento puede variar enormemente [cite: 24]. No obstante, el tamaño máximo absoluto de un paquete IPv4 completo es de **65,535 bytes** [cite: 24]. Esta sección almacena el mensaje real que se está transfiriendo por internet, como la información de un sitio web o el texto de un correo electrónico [cite: 24].

### Los 13 Campos del Encabezado IPv4
Existen exactamente 13 campos estructurados dentro del encabezado de un paquete IPv4 que todo analista debe conocer [cite: 24]:

1.  **Versión (*Version - VER*):** Este componente de 4 bits le indica a los dispositivos receptores qué versión del protocolo está utilizando el paquete (en este caso, IPv4) [cite: 24].
2.  **Longitud del Encabezado IP (*IP Header Length - HLEN o IHL*):** Indica el tamaño exacto del encabezado del paquete [cite: 24]. Este valor le permite al sistema receptor saber con precisión dónde termina el encabezado y dónde comienza el segmento de datos reales [cite: 24].
3.  **Tipo de Servicio (*Type of Service - ToS*):** Los *routers* priorizan ciertos paquetes para mantener una calidad de servicio (*Quality of Service* o QoS) óptima en la red [cite: 24]. El campo ToS le proporciona al *router* esta información de prioridad [cite: 24].
4.  **Longitud Total (*Total Length*):** Comunica el tamaño absoluto de todo el paquete IP, sumando el encabezado y los datos [cite: 24]. El límite máximo es de 65,535 bytes [cite: 24].
5.  **Identificación (*Identification*):** Aunque los paquetes pueden medir hasta 65,535 bytes, la mayoría de las redes físicas tienen un límite de transmisión más pequeño [cite: 24]. En estos casos, los paquetes grandes deben dividirse o fragmentarse en paquetes IP más pequeños [cite: 24]. El campo de identificación proporciona un identificador único para todos los fragmentos del paquete original, permitiendo que el receptor los reensamble correctamente al llegar a su destino [cite: 24].
6.  **Banderas (*Flags*):** Suministra información al dispositivo de enrutamiento sobre si el paquete original ha sido fragmentado y si existen más fragmentos en tránsito asociados a ese mismo flujo [cite: 24].
7.  **Desplazamiento de Fragmentación (*Fragmentation Offset*):** Le indica a los *routers* y sistemas receptores el lugar exacto del paquete original al que pertenece ese fragmento específico para su reconstrucción secuencial [cite: 24].
8.  **Tiempo de Vida (*Time to Live - TTL*):** El TTL es un mecanismo de seguridad crítico que evita que los paquetes de datos queden atrapados en bucles de red y sean reenviados por los *routers* de forma indefinida [cite: 24]. Contiene un contador establecido por el emisor que disminuye en uno (-1) cada vez que el paquete pasa por un *router* [cite: 24]. Si el contador llega a cero (0), el *router* descarta (*discards*) el paquete de inmediato y envía un mensaje de error ICMP de tiempo excedido (*ICMP Time Exceeded*) de vuelta al remitente original [cite: 24].
9.  **Protocolo (*Protocol*):** Le comunica al dispositivo receptor qué protocolo específico de la capa superior (como TCP o UDP) se debe utilizar para procesar la porción de datos del paquete [cite: 24].
10. **Suma de Comprobación del Encabezado (*Header Checksum*):** Contiene un valor matemático que se utiliza para detectar si el encabezado IP sufrió alguna corrupción o alteración durante el tránsito [cite: 24]. Si el *router* detecta que el paquete está corrompido, lo descarta inmediatamente [cite: 24].
11. **Dirección IP de Origen (*Source IP Address*):** Es la dirección IPv4 del dispositivo que envió originalmente el paquete [cite: 24].
12. **Dirección IP de Destino (*Destination IP Address*):** Es la dirección IPv4 del dispositivo receptor final al que va dirigido el paquete [cite: 24].
13. **Opciones (*Options*):** Permite aplicar configuraciones de seguridad adicionales al paquete si el valor de HLEN es mayor que cinco, comunicando estas directrices especiales a los dispositivos de enrutamiento [cite: 24].

---

## Diferencias Críticas entre IPv4 e IPv6

Con la masificación global de internet, se volvió evidente que el bloque total de direcciones IPv4 eventualmente se terminaría; este fenómeno se conoce como **agotamiento de direcciones IPv4 (*IPv4 address exhaustion*)** [cite: 24]. Debido a que originalmente no se previó la inmensa cantidad de dispositivos de cómputo que requerirían una dirección IP, se desarrolló el estándar IPv6 para mitigar este agotamiento y resolver problemas arquitectónicos relacionados [cite: 24].

Las diferencias fundamentales entre ambos protocolos radican en su longitud, formato y características de seguridad [cite: 24]:

### Longitud y Formato
*   **IPv4:** Las direcciones se componen de cuatro números decimales separados por puntos, donde cada número varía de 0 a 255 (ej. `198.51.100.0`) [cite: 24]. En total, abarcan un espacio de **4 bytes** (32 bits), lo que permite un límite de hasta **4,300 millones** de direcciones posibles [cite: 24].
*   **IPv6:** Se estructuran mediante ocho números hexadecimales separados por dos puntos (`:`), donde cada grupo contiene hasta cuatro dígitos hexadecimales [cite: 24]. En total, abarcan **16 bytes** (128 bits), permitiendo una escala masiva de hasta **340 undecillones** de direcciones posibles (un 340 seguido de 36 ceros) [cite: 24]. Un ejemplo de dirección IPv6 sería: `2002:0db8:0000:0000:0000:ff21:0023:1234` [cite: 24].

> [!NOTE]
> **Notación simplificada en IPv6:** Para representar uno o más grupos consecutivos compuestos exclusivamente por ceros, puedes sustituirlos por un doble signo de dos puntos (`::`) [cite: 24]. Siguiendo esta regla, la dirección IPv6 del ejemplo anterior se puede escribir de forma simplificada como: `2002:0db8::ff21:0023:1234` [cite: 24].

### Simplificación del Encabezado
El diseño del encabezado de un paquete IPv6 es sustancialmente más simple y eficiente que el de IPv4 [cite: 24]. Campos complejos de IPv4 como *IHL*, *Identification* y *Flags* fueron completamente eliminados en IPv6 para acelerar el procesamiento en los *routers* [cite: 24]. En su lugar, IPv6 introduce únicamente el campo **Etiqueta de Flujo (*Flow Label*)**, el cual identifica paquetes que requieren un manejo prioritario o especial por parte de los routers de la infraestructura [cite: 24].

### Mejoras de Seguridad Perimetral
A nivel de ciberseguridad, IPv6 introduce ventajas sumamente relevantes en comparación con IPv4 [cite: 24]:
*   Ofrece un enrutamiento mucho más eficiente y optimizado a través de los nodos globales [cite: 24].
*   **Elimina las colisiones de direcciones privadas:** Un problema común en IPv4 que ocurre cuando dos dispositivos dentro de una misma infraestructura intentan utilizar la misma dirección IP de forma simultánea, causando interrupciones operativas [cite: 24].

---

## Puntos Clave (Key Takeaways)

*   **Propósito de la Capa de Red:** Gestiona el enrutamiento y direccionamiento lógico de los paquetes de datos inter-redes desde el host emisor hasta el destinatario final usando tablas de enrutamiento [cite: 24].
*   **Anatomía de Paquetes (IPv4):** Un paquete IPv4 se divide en un encabezado variable (de 20 a 60 bytes) y una carga útil de datos, con un tamaño máximo absoluto de 65,535 bytes [cite: 24].
*   **Telemetría de Control del Encabezado:** Los 13 campos de IPv4 proveen datos esenciales para el SOC, destacando el *TTL* (que destruye paquetes en bucle generando un error ICMP) y el *Header Checksum* (que valida la integridad del encabezado) [cite: 24].
*   **Mitigación mediante IPv6:** Diseñado para solucionar de raíz el agotamiento de direcciones de IPv4, IPv6 expande el espacio de direccionamiento de 4 a 16 bytes, habilitando hasta 340 undecillones de identificadores únicos [cite: 24].
*   **Ventajas Defensivas de IPv6:** Adicionalmente a un encabezado simplificado con el campo *Flow Label*, IPv6 optimiza la velocidad de enrutamiento y neutraliza las colisiones operativas por duplicidad de direcciones IP en la red [cite: 24].
