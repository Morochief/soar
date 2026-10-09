# Exemplar: Analyze your first packet with Wireshark

> [!NOTE]
> Este es el documento ejemplar (Exemplar) del laboratorio práctico del Módulo 2 del Curso 6 (Sound the Alarm: Detection and Response). Muestra los pasos correctos para analizar tráfico de red usando Wireshark.

## Resumen de la Actividad (*Activity overview*)
Como analista de seguridad, necesitarás analizar el tráfico de red para saber qué tipo de información se envía desde y hacia los sistemas. Herramientas como **Wireshark** (un analizador de protocolos de red / *packet sniffer* con interfaz gráfica) ayudan a examinar paquetes, encontrar patrones y aplicar filtros en investigaciones de seguridad.

En esta actividad, se examina un archivo de captura de paquetes (`.pcap`) que contiene tráfico relacionado con un usuario conectándose a un sitio web (opensource.google.com).

### Objetivos:
1. Identificar direcciones IP de origen y destino.
2. Examinar los protocolos utilizados en la conexión web.
3. Analizar datos de paquetes para ver el tipo de información enviada y recibida.

---

## Tarea 1: Explorar datos con Wireshark (*Explore data with Wireshark*)
Al abrir el archivo `.pcap`, se muestra la interfaz principal con varias columnas:
*   **No.**: El número de índice del paquete.
*   **Time**: La marca de tiempo (*timestamp*).
*   **Source**: IP de origen.
*   **Destination**: IP de destino.
*   **Protocol**: El protocolo contenido en el paquete.
*   **Length**: La longitud total del paquete.
*   **Info**: Información sobre la carga útil (*payload*).

**Pregunta 1: ¿Cuál es el protocolo del primer paquete en la lista donde la columna "info" comienza con las palabras 'Echo (ping) request'?**
*   **Respuesta:** `ICMP`. (Este es el protocolo utilizado para solicitudes *ping*).

---

## Tarea 2: Aplicar un filtro básico e inspeccionar un paquete (*Apply a basic Wireshark filter and inspect a packet*)
Usando la barra de filtros, filtramos por una IP específica:
`ip.addr == 142.250.1.139`

Al hacer doble clic en el primer paquete `TCP` de la lista filtrada, se abre el panel de detalles del paquete (*Packet Details Pane*), estructurado en capas OSI/TCP-IP (Frame, Ethernet II, IPv4, TCP).

**Pregunta 2: ¿Cuál es el puerto de destino TCP de este paquete TCP?**
*   **Respuesta:** `80`. (Es el puerto típico para solicitudes web HTTP iniciales).

---

## Tarea 3: Uso de filtros para seleccionar paquetes (*Use filters to select packets*)
Exploramos filtros adicionales:
*   Tráfico desde un origen: `ip.src == 142.250.1.139`
*   Tráfico hacia un destino: `ip.dst == 142.250.1.139`
*   Tráfico desde/hacia una dirección MAC específica: `eth.addr == 42:01:ac:15:e0:02`

Al revisar el paquete con el filtro de dirección MAC...
**Pregunta 3: ¿Cuál es el protocolo contenido en el subárbol Internet Protocol Version 4 del primer paquete relacionado con la dirección MAC 42:01:ac:15:e0:02?**
*   **Respuesta:** `TCP`.

---

## Tarea 4: Explorar paquetes DNS (*Use filters to explore DNS packets*)
Para filtrar tráfico de resolución de nombres (DNS), filtramos por el puerto UDP 53:
`udp.port == 53`

Revisando el subárbol **Domain Name System (query)** en el apartado *Answers* (Respuestas)...
**Pregunta 4: ¿Cuál de estas direcciones IP se muestra en la sección de Respuestas (*Answers*) ampliada para la consulta DNS de opensource.google.com?**
*   **Respuesta:** `142.250.1.139`.

---

## Tarea 5: Explorar paquetes TCP (*Use filters to explore TCP packets*)
Filtramos el puerto HTTP predeterminado:
`tcp.port == 80`

Al inspeccionar el primer paquete enviado hacia `169.254.169.254`:
**Pregunta 5: ¿Cuál es el valor del Tiempo de vida (*Time to Live / TTL*) del paquete especificado en el subárbol IPv4?**
*   **Respuesta:** `64`.

**Pregunta 6: ¿Cuál es la longitud de la trama (*Frame Length*) especificada en el subárbol Frame?**
*   **Respuesta:** `54 bytes`.

**Pregunta 7: ¿Cuál es la longitud del encabezado (*Header Length*) especificada en el subárbol IPv4?**
*   **Respuesta:** `20 bytes`.

**Pregunta 8: ¿Cuál es la dirección de destino (*Destination Address*) en el subárbol IPv4?**
*   **Respuesta:** `169.254.169.254`.

Finalmente, se puede buscar texto sin formato (*payload*) dentro del tráfico usando `contains`:
`tcp contains "curl"`
Este filtro mostrará paquetes que contengan solicitudes web hechas mediante el comando `curl`.
