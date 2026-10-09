# Reading: Learn more about the TCP/IP model

En esta lectura complementaria, profundizarás en lo que has aprendido sobre el modelo de Protocolo de Control de Transmisión/Protocolo de Internet (*Transmission Control Protocol/Internet Protocol* o **TCP/IP**), analizarás las diferencias fundamentales entre el modelo de Interconexión de Sistemas Abiertos (*Open Systems Interconnection* o **OSI**) y el modelo TCP/IP, y comprenderás cómo se relacionan entre sí [cite: 25]. Finalmente, repasarás cada capa del modelo TCP/IP y revisarás los protocolos más comunes que operan en cada una de ellas [cite: 25].

---

## Introducción del Equipo de Google

Como profesional de la ciberseguridad, es de suma importancia que comprendas a fondo el modelo TCP/IP debido a que describe con precisión las funciones operativas de diversos protocolos de red [cite: 25]. El modelo TCP/IP se fundamenta en la suite de protocolos TCP/IP, la cual engloba todas las subreglas de comunicación que dan soporte al protocolo principal [cite: 25]. 

Para reiterar lo aprendido en lecciones anteriores, un protocolo de red (*network protocol*), también conocido como protocolo de internet, es un conjunto de estándares y reglas que se utilizan para gestionar el enrutamiento y direccionamiento de los paquetes de datos (*data packets*) mientras viajan entre los diferentes dispositivos de una infraestructura [cite: 25]. A lo largo de este documento, aprenderás en qué capas específicas de comunicación operan estos protocolos [cite: 25]. 

> [!NOTE]
> Aunque los dos modelos de referencia más utilizados en la industria global son el TCP/IP y el OSI, los ejemplos analizados de forma práctica en este certificado se alinearán con el modelo TCP/IP, por ser el estándar de implementación real en el internet moderno [cite: 25].

---

## El Modelo TCP/IP

El modelo TCP/IP es un marco de trabajo (*framework*) conceptual utilizado para visualizar y estructurar cómo se organizan, empaquetan y transmiten los datos a través de una red informática [cite: 25]. Este modelo ayuda a los ingenieros de redes y a los analistas de seguridad de un Centro de Operaciones de Seguridad (**SOC**) a conceptualizar los procesos internos del tráfico y a comunicarse con precisión para señalar dónde están ocurriendo interrupciones lógicas o amenazas de seguridad [cite: 25].

El modelo TCP/IP consta de **cuatro capas esenciales**: la capa de acceso a la red, la capa de internet, la capa de transporte y la capa de aplicación [cite: 25]. Al realizar tareas de mitigación y resolución de problemas (*troubleshooting*) en la infraestructura, los profesionales de la ciberseguridad pueden determinar qué capas específicas fueron impactadas por un ataque informático basándose en los procesos técnicos involucrados en el incidente [cite: 25].

### 1. Capa de acceso a la red (*Network access layer*)
La **capa de acceso a la red**, a veces denominada capa de enlace de datos (*data link layer*), gestiona de forma directa la creación de los paquetes de datos y su transmisión física a través de los nodos del sistema [cite: 25]. Esta capa se corresponde directamente con el hardware físico involucrado en las transmisiones de datos [cite: 25].
*   **Componentes físicos:** Los *hubs*, módems, cables de red y el cableado estructurado se consideran elementos integrales de esta capa [cite: 25].
*   **Protocolo ARP (*Address Resolution Protocol*):** El protocolo de resolución de direcciones forma parte medular de la capa de acceso a la red [cite: 25]. Debido a que las direcciones MAC (*MAC addresses*) son los identificadores físicos obligatorios para localizar hosts dentro de una misma red local, se requiere el uso de **ARP** para mapear y traducir las direcciones IP lógicas a sus correspondientes direcciones MAC físicas para habilitar la comunicación interna [cite: 25].

### 2. Capa de internet (*Internet layer*)
La **capa de internet**, a veces llamada capa de red (*network layer*), es la responsable directa de garantizar la entrega exitosa de los paquetes hacia el host de destino, el cual potencialmente puede residir en una red geográfica completamente diferente [cite: 25]. Se encarga de asegurar que las direcciones IP queden incrustadas en los encabezados (*headers*) de los paquetes de datos para indicar la ubicación exacta del emisor y del receptor [cite: 25]. 

Asimismo, la capa de internet determina qué reglas son responsables de entregar los paquetes de datos y supervisa su trayecto inter-redes [cite: 25]. Entre los protocolos más comunes que operan en este nivel se destacan [cite: 25]:
*   **Protocolo de Internet (*Internet Protocol - IP*):** Envía los paquetes de datos hacia el destino correcto y se apoya en los protocolos de la capa superior (TCP/UDP) para entregarlos al servicio o aplicación correspondiente [cite: 25]. Los paquetes IP hacen posible la comunicación entre dos redes independientes mediante el enrutamiento desde la red emisora a la receptora [cite: 25].
*   **Protocolo de Mensajes de Control de Internet (*Internet Control Message Protocol - ICMP*):** El protocolo **ICMP** se encarga de compartir información sobre errores y actualizaciones de estado de los paquetes de datos [cite: 25]. Es una herramienta extraordinariamente útil para detectar, diagnosticar y solucionar fallas de red [cite: 25]. ICMP reporta telemetría sobre paquetes que fueron descartados (*dropped*) o que desaparecieron en tránsito, problemas de conectividad física o lógica, y redirecciones de tráfico hacia otros *routers* [cite: 25].

### 3. Capa de transporte (*Transport layer*)
La **capa de transporte** es la encargada de asegurar la entrega e intercambio de datos entre dos sistemas o redes independientes, incorporando mecanismos para controlar el flujo y la velocidad del tráfico [cite: 25]. **TCP** y **UDP** son los dos protocolos de transporte principales que se ejecutan en este nivel [cite: 25]:

#### Protocolo de Control de Transmisión (*Transmission Control Protocol - TCP*)
El **TCP** es un protocolo de comunicación orientado a la conexión (*connection-oriented*) que permite a dos dispositivos establecer un enlace lógico estable para transmitir flujos continuos de datos [cite: 25]. Garantiza de forma matemática que los datos se transmitan de manera confiable y sin alteraciones al servicio de destino [cite: 25]. 
*   **Encabezados y Puertos:** TCP inserta el número de puerto (*port number*) del servicio de destino legítimo dentro de su propio encabezado (*TCP header*) de control [cite: 25]. En particular, TCP se encarga de retransmitir automáticamente cualquier fragmento de datos que se haya perdido, corrompido o llegado incompleto durante el trayecto [cite: 25].

#### Protocolo de Datagramas de Usuario (*User Datagram Protocol - UDP*)
El **UDP** es un protocolo no orientado a la conexión (*connectionless*), lo que significa que no establece un enlace previo ni realiza un saludo de manos (*handshake*) entre los dispositivos antes de iniciar la transmisión de datos [cite: 25]. 
*   **Optimización del Rendimiento:** Es utilizado por aplicaciones de software que no requieren una confiabilidad absoluta en la recepción de cada paquete y donde no se realiza un rastreo exhaustivo del flujo como en TCP [cite: 25]. Debido a que UDP prescinde de la sobrecarga de gestionar conexiones de red complejas, se implementa principalmente en aplicaciones altamente sensibles al rendimiento que operan en tiempo real, tales como el streaming de video y las llamadas de voz sobre IP (VoIP) [cite: 25].

### 4. Capa de aplicación (*Application layer*)
La **capa de aplicación** en el modelo TCP/IP condensa y realiza funciones equivalentes a las capas de aplicación, presentación y sesión del modelo de referencia OSI [cite: 25]. Esta capa es la responsable directa de generar solicitudes de red o de procesar y responder a las peticiones entrantes [cite: 25]. 

Define con precisión a qué servicios de internet y aplicaciones de software puede acceder un usuario final, determinando cómo interactuarán los paquetes de datos con los programas del sistema receptor [cite: 25]. Los protocolos de la capa de aplicación dependen enteramente de las capas inferiores subyacentes para transportar los datos reales a través de la infraestructura [cite: 25]. Algunos de los estándares más utilizados en esta capa son [cite: 25]:
*   **HTTP / HTTPS (*Hypertext Transfer Protocol*):** Para la navegación y transferencia de hipertexto en la web [cite: 25].
*   **SMTP (*Simple Mail Transfer Protocol*):** Para la transferencia y distribución de correo electrónico [cite: 25].
*   **SSH (*Secure Shell*):** Para el acceso y administración remota y cifrada de sistemas [cite: 25].
*   **FTP (*File Transfer Protocol*):** Para la transferencia e intercambio formal de archivos [cite: 25].
*   **DNS (*Domain Name System*):** Para la resolución y traducción de nombres de dominio legibles a direcciones IP [cite: 25].

---

## Comparativa: Modelo TCP/IP vs. Modelo OSI

El modelo **OSI** organiza visualmente los protocolos de red dividiéndolos en **siete capas** distintas [cite: 25]. Los profesionales de la ciberseguridad utilizan frecuentemente este mapa de referencia de siete niveles para comunicarse entre sí sobre los orígenes potenciales de una falla de red o para aislar vectores de ataque complejos [cite: 25].

| Característica | Modelo TCP/IP | Modelo OSI |
| :--- | :--- | :--- |
| **Complejidad** | Modelo simplificado y práctico [cite: 25]. | Modelo detallado y conceptual [cite: 25]. |
| **Número de Capas** | 4 capas (Acceso a la Red, Internet, Transporte, Aplicación) [cite: 25]. | 7 capas (Física, Enlace de Datos, Red, Transporte, Sesión, Presentación, Aplicación) [cite: 25]. |
| **Capa Superior** | Combina las funciones de interfaz, sesión y formato en la capa de Aplicación [cite: 25]. | Separa estrictamente la Sesión, Presentación y Aplicación en tres niveles independientes [cite: 25]. |
| **Enfoque Industrial** | Es el estándar de implementación real sobre el cual se construyó el internet [cite: 25]. | Se utiliza principalmente como una guía educativa y de referencia teórica de comunicación [cite: 25]. |

A pesar de sus diferencias en el número de capas, existen múltiples similitudes entre ambos esquemas [cite: 25]. Ambos modelos definen estándares rigurosos para la interconexión de sistemas de cómputo y dividen el proceso de comunicación en capas lógicas estructuradas para garantizar el orden operativo [cite: 25]. El modelo TCP/IP puede visualizarse como una versión condensada, optimizada y altamente práctica del modelo OSI [cite: 25].

---

## Puntos Clave (Key Takeaways)

*   **Modelos de Visualización:** Tanto el modelo TCP/IP como el OSI son estructuras conceptuales de referencia diseñadas para ayudar a los analistas a visualizar los procesos de comunicación, identificar flujos y mapear riesgos de datos entre sistemas [cite: 25].
*   **Estructura Jerárquica:** El modelo TCP/IP consta de 4 capas operativas, mientras que el modelo OSI expande la teoría analítica estructurándola en 7 capas diferenciadas [cite: 25].
*   **Capa de Acceso (L1 - ARP):** Administra la interfaz física del hardware y utiliza el protocolo ARP para mapear direcciones IP lógicas con direcciones MAC físicas dentro de la LAN [cite: 25].
*   **Capa de Internet (L2 - IP/ICMP):** Gobierna el direccionamiento y entrega inter-redes mediante paquetes IP, complementándose con el protocolo ICMP para recibir reportes de conectividad y diagnóstico de errores en tránsito [cite: 25].
*   **Capa de Transporte (L3 - TCP/UDP):** Regula la transferencia de datos mediante esquemas confiables orientados a la conexión y retransmisión de errores (TCP) o mediante transmisiones veloces e idóneas para tiempo real sin conexión previa (UDP) [cite: 25].
*   **Capa de Aplicación (L4 - Servicios):** Centraliza la interacción con el software de usuario y los servicios finales de la infraestructura, operando protocolos indispensables para el SOC como HTTP, SMTP, SSH, FTP y DNS [cite: 25].
