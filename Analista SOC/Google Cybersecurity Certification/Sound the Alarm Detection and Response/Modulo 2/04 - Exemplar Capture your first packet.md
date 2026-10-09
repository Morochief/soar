# Exemplar: Capture your first packet

> [!NOTE]
> Este es el documento ejemplar (Exemplar) del laboratorio práctico del Módulo 2 del Curso 6 (Sound the Alarm: Detection and Response). Muestra los comandos correctos para usar `tcpdump` en la captura y filtrado de tráfico en un entorno Linux.

## Resumen de la Actividad (*Activity overview*)
Como analista de seguridad, es fundamental saber cómo capturar y filtrar el tráfico de red en un entorno Linux utilizando herramientas de línea de comandos. En este laboratorio, se utiliza `tcpdump` para capturar tráfico en vivo, guardarlo en un archivo `.pcap` y luego examinar su contenido.

### Objetivos:
1. Identificar las interfaces de red disponibles.
2. Inspeccionar el tráfico en vivo.
3. Capturar tráfico de red en un archivo.
4. Filtrar los datos del paquete capturado.

---

## Tarea 1: Identificar interfaces de red (*Identify network interfaces*)
Para capturar tráfico, primero debes saber qué interfaces están disponibles en la máquina.
1. Utiliza `ifconfig` para enumerar las interfaces:
   ```bash
   sudo ifconfig
   ```
   *La interfaz de red principal suele ser `eth0`.*

2. También puedes usar una bandera de `tcpdump` para listar las interfaces disponibles:
   ```bash
   sudo tcpdump -D
   ```

---

## Tarea 2: Inspeccionar el tráfico de red con tcpdump (*Inspect network traffic*)
Ejecuta el siguiente comando para filtrar datos en vivo desde la interfaz `eth0`:
```bash
sudo tcpdump -i eth0 -v -c5
```

**Desglose del comando:**
*   `-i eth0`: Captura datos específicamente desde la interfaz `eth0`.
*   `-v`: Muestra datos detallados del paquete (modo verboso / *verbose*).
*   `-c5`: Captura exactamente 5 paquetes y luego se detiene.

---

## Tarea 3: Capturar tráfico en un archivo (*Capture network traffic*)
Para guardar una muestra pequeña que contenga solo tráfico web (TCP puerto 80) en un archivo `.pcap`:
```bash
sudo tcpdump -i eth0 -nn -c9 port 80 -w capture.pcap &
```

**Desglose del comando:**
*   `-nn`: No intenta resolver direcciones IP ni puertos a nombres. (Buena práctica de seguridad para evitar alertar a los actores de amenazas mediante búsquedas DNS).
*   `-c9`: Captura 9 paquetes.
*   `port 80`: Filtra solo el tráfico del puerto 80 (HTTP predeterminado).
*   `-w capture.pcap`: Escribe (*write*) los datos capturados en el archivo especificado.
*   `&`: Ejecuta el comando en segundo plano (*background*).

Para generar tráfico y que `tcpdump` lo capture, se utiliza `curl`:
```bash
curl opensource.google.com
```

Puedes verificar que el archivo se creó con:
```bash
ls -l capture.pcap
```

---

## Tarea 4: Filtrar los datos capturados (*Filter the captured packet data*)
Para leer los datos del archivo capturado sin necesidad de capturar en vivo:
```bash
sudo tcpdump -nn -r capture.pcap -v
```
*   `-r`: Lee (*read*) los datos de captura del archivo nombrado.

Para ver los datos en formato hexadecimal y ASCII (útil para buscar anomalías o *malware*):
```bash
sudo tcpdump -nn -r capture.pcap -X
```
*   `-X`: Muestra el formato de salida en hexadecimal y ASCII.

---

## Pon a prueba tu comprensión (*Test your understanding*)

**Pregunta 1: ¿Qué comando usarías para capturar 3 paquetes en cualquier interfaz con la opción verbosa?**
*   **Respuesta:** `sudo tcpdump -c3 -i any -v`

**Pregunta 2: ¿Qué indica la opción `-i`?**
*   **Respuesta:** La interfaz de red a monitorear (*The network interface to monitor*).

**Pregunta 3: ¿Qué tipo de información incluye la opción `-v`?**
*   **Respuesta:** Información verbosa/detallada (*Verbose information*).

**Pregunta 4: ¿Qué comando tcpdump puedes utilizar para identificar las interfaces que están disponibles para realizar una captura de paquetes?**
*   **Respuesta:** `sudo tcpdump -D`
