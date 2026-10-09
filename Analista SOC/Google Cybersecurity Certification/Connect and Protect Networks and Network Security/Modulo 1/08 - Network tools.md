# Network tools

¡Te damos la bienvenida! Continuamos avanzando con paso firme en este primer módulo del curso. Una vez comprendido qué es una red, el siguiente paso fundamental para cualquier analista de ciberseguridad es conocer los componentes de hardware y software que la hacen posible.

---

## Introducción del Instructor

Mi nombre es **Chris** y soy el Director de Seguridad de la Información (*Chief Information Security Officer* o CISO) en **Google Fiber**. En esta sesión, analizaremos los dispositivos físicos tradicionales que estructuran una red y cómo la evolución tecnológica nos permite emular sus funciones en entornos virtuales para optimizar la seguridad y los costos.

---

## Dispositivos Físicos de Red

Para gestionar el tráfico de datos, una infraestructura tradicional depende de dispositivos de hardware especializados. Cada uno de ellos posee un nivel diferente de inteligencia operativa y seguridad:

### 1. Hub (*Concentrador*)
Un **hub** es un dispositivo de red básico que retransmite o transmite en directo (*broadcasts*) información a absolutamente todos los dispositivos conectados a la red. 
*   *Analogía:* Puedes imaginar un *hub* como una torre de radio tradicional, la cual emite una señal abierta hacia cualquier receptor que esté sintonizado en la frecuencia correcta, sin importar quién sea.

### 2. Switch (*Conmutador*)
Un **switch** establece conexiones directas entre dispositivos específicos dentro de una misma red local mediante el envío y la recepción de datos orientada exclusivamente a ellos. 

> [!IMPORTANT]
> Un *switch* es sustancialmente más inteligente que un *hub*, ya que solo transfiere los datos al destino legítimo e intencionado. Esta característica selectiva vuelve a los *switches* herramientas mucho más seguras que los *hubs*, permitiéndoles controlar el flujo del tráfico, mitigar el riesgo de intercepción de datos y mejorar drásticamente el rendimiento general de la red.

### 3. Router (*Enrutador*)
Un **router** es un dispositivo de red diseñado específicamente para interconectar múltiples redes diferentes entre sí. 
*   *Flujo de comunicación:* Si una computadora en una red requiere enviar información a una tableta ubicada en otra red distinta, los datos viajan primero desde la computadora hacia el *router*. El *router* lee la dirección de destino final y reenvía los datos al *router* de la red correspondiente. Finalmente, el *router* receptor dirige esa información con precisión hacia la tableta.

### 4. Módem (*Modem*)
Un **módem** es el dispositivo encargado de conectar tu *router* con el proveedor de servicios de internet, trayendo el acceso externo hacia tu red de área local (*LAN*).
*   *Flujo geográfico:* Cuando envías información a un dispositivo en una ubicación geográfica distante, tu computadora transmite los datos al *router*, este los transfiere a través del módem hacia el internet global. En el extremo opuesto, el módem del destinatario legítimo recibe la información, la pasa a su propio *router* y, finalmente, este último la entrega al dispositivo final.

---

## Virtualización y Redes en la Nube

Herramientas de red como los *hubs*, *switches*, *routers* y módems son históricamente dispositivos físicos. Sin embargo, en el panorama tecnológico moderno, muchas de las funciones ejecutadas por este hardware físico pueden ser completadas de forma lógica mediante **herramientas de virtualización (*virtualization tools*)**.

> [!NOTE]
> Las herramientas de virtualización son piezas avanzadas de software que realizan operaciones completas de red. Estas soluciones de software ejecutan las mismas tareas de enrutamiento y conmutación que normalmente completaría un equipo físico, y son ofrecidas de manera nativa por los proveedores de servicios en la nube (*Cloud service providers*).

El uso de estas infraestructuras virtuales proporciona a las organizaciones extraordinarias oportunidades de **ahorro de costos** y una alta **escalabilidad** operativa, conceptos en los que profundizaremos más adelante en el programa.

---

## Puntos Clave (Key Takeaways)

*   **Diferencia Crítica Hub vs. Switch:** Mientras que el *hub* difunde datos a toda la red de forma indiscriminada (siendo un riesgo de seguridad), el *switch* mapea destinos específicos, aislando el tráfico y robusteciendo la seguridad perimetral.
*   **Enrutamiento Inter-redes:** Los *routers* actúan como los puentes lógicos que leen direccionamientos y permiten la comunicación fluida entre redes totalmente independientes.
*   **Acceso LAN a Internet:** El módem cumple la función indispensable de traducir y enlazar la infraestructura local (*LAN*) con el entorno de red de área amplia (*WAN*) del internet.
*   **Evolución hacia el Software:** La virtualización en la nube permite sustituir el hardware físico costoso por funciones de red definidas por software, garantizando implementaciones rápidas, escalables y económicamente eficientes.
