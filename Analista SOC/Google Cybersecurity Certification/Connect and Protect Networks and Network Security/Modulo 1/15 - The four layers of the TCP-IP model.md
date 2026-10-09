# The four layers of the TCP/IP model

¡Hola de nuevo! Una vez que hemos analizado la estructura de una red y cómo se llevan a cabo las comunicaciones, es momento de aprender una de las herramientas más valiosas que tienen los defensores digitales para comprender el flujo de información y anticipar incidentes.

---

## Introducción del Instructor

Mi nombre es **Chris** y soy el Director de Seguridad de la Información (*Chief Information Security Officer* o CISO) en **Google Fiber**. En esta sesión, exploraremos el modelo TCP/IP como un mapa conceptual dinámico. Comprender cómo este *framework* organiza la actividad de la red te permitirá, como analista de seguridad, monitorear el tráfico y proteger a tu organización frente a una gran variedad de riesgos, peligros y amenazas.

---

## Desarrollo Temático: Las Cuatro Capas del Modelo TCP/IP

El modelo TCP/IP es un marco de trabajo (*framework*) que se utiliza de manera estandarizada para visualizar cómo se organizan, estructuran y transmiten los datos a través de una red informática. 

Este modelo se divide de forma jerárquica en **cuatro capas** operativas esenciales. Examinemos detalladamente cada una de ellas, desde la base física hasta la interacción con el usuario:

### Capa 1: Capa de acceso a la red (*Network access layer*)
La primera capa es la **capa de acceso a la red**. Esta sección se encarga específicamente de la creación de los paquetes de datos (*data packets*) y de su transmisión física o inalámbrica a través de los nodos de la infraestructura. 
*   **Componentes asociados:** Incluye todos los dispositivos de hardware que se encuentran interconectados mediante cables físicos, así como los *switches* que tienen la tarea de dirigir los datos directamente hacia su destino local.

### Capa 2: Capa de internet (*Internet layer*)
La segunda capa es la **capa de internet**. Este es el nivel lógico donde las direcciones IP (*IP addresses*) se acoplan o adjuntan formalmente a los paquetes de datos para indicar de manera inequívoca la ubicación tanto del emisor (remitente) como del receptor (destinatario).
*   **Enfoque operativo:** La capa de internet se concentra en cómo las distintas redes independientes se conectan e interactúan entre sí. Por ejemplo, aquí es donde los paquetes de datos procesan la información de enrutamiento que determina si deben permanecer dentro de la red de área local (*LAN*) o si deben ser enviados hacia una red remota exterior, como el internet público.

### Capa 3: Capa de transporte (*Transport layer*)
La tercera capa es la **capa de transporte**, la cual incorpora protocolos especializados para controlar de manera minuciosa el flujo del tráfico de datos a lo largo de la red. 
*   **Flujo y control:** Estos protocolos tienen la facultad de permitir o denegar la comunicación con otros dispositivos e integran metadatos críticos sobre el estado actual de la conexión. 
*   **Control de errores:** Entre las actividades nucleares de esta capa se encuentra el *control de errores*, un mecanismo indispensable que asegura que los datos fluyan de manera suave, continua y sin pérdidas a través de la red.

### Capa 4: Capa de aplicación (*Application layer*)
Finalmente, en la parte superior de la jerarquía se ubica la **capa de aplicación**. En este nivel, los protocolos determinan con precisión de qué manera los paquetes de datos van a interactuar con los programas y los dispositivos receptores finales.
*   **Servicios integrados:** Las funciones operativas que se organizan y gestionan dentro de la capa de aplicación abarcan servicios cotidianos y empresariales críticos, tales como las transferencias de archivos (protocolo FTP) y los servicios de correo electrónico.

> [!IMPORTANT]
> Para un profesional del SOC, saber identificar en qué capa opera un protocolo o dispositivo es fundamental. Cuando surge un problema o una intrusión, esta estructura jerárquica permite aislar la falla de forma sistemática: desde validar si un cable está desconectado en la Capa de Acceso a la Red, hasta rastrear una vulnerabilidad de software en la Capa de Aplicación.

Ahora que posees una comprensión sólida sobre el modelo TCP/IP y sus cuatro capas esenciales, estamos listos para continuar profundizando en sus mecanismos de seguridad. ¡Nos vemos en el próximo video!

---

## Puntos Clave (Key Takeaways)

*   **Propósito del Framework:** El modelo TCP/IP funciona como un mapa visual y conceptual que permite a los profesionales de la seguridad comprender cómo se empaquetan, direccionan y transportan los datos de un extremo a otro de la red.
*   **Capa de Acceso a la Red (L1):** Gobierna los aspectos físicos y de hardware de la comunicación, encargándose de la creación física de los paquetes y su transferencia mediante cables y *switches*.
*   **Capa de Internet (L2):** Introduce el direccionamiento lógico adjuntando las direcciones IP a los paquetes, decidiendo si el tráfico permanece localizado en la *LAN* o se enruta hacia el internet.
*   **Capa de Transporte (L3):** Regula el flujo del tráfico, administra los estados de conexión entre dispositivos e implementa el control de errores para garantizar transmisiones fluidas.
*   **Capa de Aplicación (L4):** Define la interfaz y los protocolos con los que interactúan los servicios de software finales, gestionando flujos comunes como el correo electrónico y la transferencia de archivos de usuario.
