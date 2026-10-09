# Exemplar: Examine alerts, logs, and rules with Suricata

> [!NOTE]
> Este es el documento ejemplar (Exemplar) del laboratorio práctico del Módulo 4 del Curso 6 (Sound the Alarm: Detection and Response). Muestra cómo leer, comprender y ejecutar reglas personalizadas de Suricata y cómo examinar los registros (*logs*) que genera, como `fast.log` y `eve.json`.

## Resumen de la Actividad (*Activity overview*)
**Suricata** es una herramienta de código abierto de prevención y detección de intrusiones (IDS/IPS) y análisis de red. Monitorea interfaces de red y aplica reglas (*rules* o *signatures*) a los paquetes.

En este laboratorio, simularás ser un analista de seguridad monitoreando tráfico de red. Examinarás reglas personalizadas y usarás Suricata contra un archivo de captura de paquetes (`sample.pcap`) para desencadenar alertas, que luego examinarás en sus respectivos archivos de registro.

### Archivos clave:
*   `sample.pcap`: Datos de tráfico de red de ejemplo.
*   `custom.rules`: Archivo de reglas donde se define qué debe alertar Suricata.
*   `fast.log`: Registro rápido de alertas (formato obsoleto pero útil para verificaciones rápidas).
*   `eve.json`: El registro principal, estándar y predeterminado de Suricata (formato JSON), ideal para procesar con otras aplicaciones.

---

## Tarea 1: Examinar una regla personalizada en Suricata (*Examine a custom rule in Suricata*)
Usando el comando `cat custom.rules`, podemos ver la regla principal de este ejercicio:
```text
alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"GET on wire"; flow:established,to_server; content:"GET"; http_method; sid:12345; rev:3;)
```
Esta regla se compone de tres partes:
1.  **Acción (*Action*)**: `alert` instruye al IDS a generar una alerta si hay coincidencia. (Otras acciones comunes son `drop`, `pass` y `reject`).
2.  **Encabezado (*Header*)**: `http $HOME_NET any -> $EXTERNAL_NET any` indica que la regla aplica al protocolo HTTP, para tráfico proveniente de cualquier puerto en la red local (`$HOME_NET`) dirigido hacia cualquier puerto en redes externas (`$EXTERNAL_NET`).
3.  **Opciones de regla (*Rule options*)**: Todo lo que está entre paréntesis `()`.
    *   `msg:"GET on wire"`: El texto de la alerta que se imprimirá.
    *   `flow:established,to_server`: Paquetes del cliente al servidor en una conexión establecida.
    *   `content:"GET"; http_method`: Busca la palabra "GET" dentro de la porción *http.method*.
    *   `sid:12345; rev:3`: ID único de la firma (SID) y número de revisión.

---

## Tarea 2: Desencadenar una regla personalizada en Suricata (*Trigger a custom rule in Suricata*)
Para correr Suricata contra el tráfico de prueba y nuestra regla, ejecutamos:
```bash
sudo suricata -r sample.pcap -S custom.rules -k none
```
*   `-r`: Archivo de entrada (.pcap).
*   `-S`: Archivo de reglas.
*   `-k none`: Desactiva la comprobación de suma de comprobación (*checksum*).

Al revisar la carpeta de registros con `ls -l /var/log/suricata`, notarás que se han creado nuevos archivos. Podemos revisar `fast.log`:
```bash
cat /var/log/suricata/fast.log
```
*   *Cada línea de `fast.log` corresponde a una alerta con la marca de tiempo, el mensaje de la regla y la IP de origen y destino.*

---

## Tarea 3: Examinar la salida eve.json (*Examine eve.json output*)
El archivo `eve.json` contiene la telemetría detallada en formato JSON. Como `cat /var/log/suricata/eve.json` muestra datos en bruto muy densos, utilizamos la herramienta `jq` para analizarlos:

```bash
jq . /var/log/suricata/eve.json | less
```
*(Nota: Usa la tecla `Q` para salir de `less`).*

**Pregunta 1: ¿Cuál es el valor de la propiedad *severity* (gravedad) de la primera alerta devuelta por el comando jq?**
*   **Respuesta:** `3`

Para extraer campos específicos (como *timestamp*, *flow_id*, *signature*, *proto*, y dirección IP de destino), podemos usar:
```bash
jq -c "[.timestamp,.flow_id,.alert.signature,.proto,.dest_ip]" /var/log/suricata/eve.json
```

**Pregunta 2: ¿Cuál es la dirección IP de destino (*destination IP*) listada para el último evento en el archivo 'eve.json'?**
*   **Respuesta:** `142.250.1.102`

**Pregunta 3: ¿Cuál es la firma de la alerta (*alert signature*) para la primera entrada de alerta en el archivo 'eve.json'?**
*   **Respuesta:** `GET on wire`

Si deseas ver todos los registros asociados a un flujo de red en particular, puedes filtrar por `flow_id` (reemplazando la `X` con el número del flujo):
```bash
jq "select(.flow_id==X)" /var/log/suricata/eve.json
```
*(El `flow_id` es un identificador único que Suricata asigna a una secuencia de paquetes que comparten características comunes, ideal para correlacionar eventos).*
