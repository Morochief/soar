# Input and output in the shell

¡Hola de nuevo! En esta lección profundizaremos en el funcionamiento del **shell** de Linux y aprenderemos exactamente cómo nos comunicamos con él en el día a día.

---

## Introducción del Instructor

Comunicarte con una computadora es muy similar a mantener una conversación cotidiana con un amigo: una persona realiza una pregunta y la otra responde con una respuesta; si la segunda persona no sabe la respuesta, simplemente indica que la desconoce. Cuando te comunicas con el *shell*, los comandos pueden recibir datos de entrada, generar datos de salida o devolver mensajes de error según el resultado de la instrucción.

---

## Desarrollo Temático: Los Tres Canales de Comunicación del Shell

La interacción con la interfaz de línea de comandos del sistema operativo se canaliza a través de tres flujos fundamentales: **entrada estándar**, **salida estándar** y **error estándar**.

### 1. Entrada Estándar (*Standard Input* / `stdin`)
La **entrada estándar** consiste en la información que el sistema operativo recibe a través de la línea de comandos. Es el equivalente a hacerle una pregunta a un amigo. Esta información se ingresa mediante el teclado hacia el *shell*. Si el *shell* puede interpretar tu solicitud, le pide al **kernel** los recursos necesarios para ejecutar la tarea correspondiente.

Para ilustrar este concepto, utilicemos el comando `echo`, una instrucción de Linux diseñada para imprimir en pantalla una cadena de texto (*string*).

> [!NOTE]
> **Cadena de texto (*String*):** En programación y sistemas operativos, una cadena es un tipo de dato compuesto por una secuencia ordenada de caracteres (letras, números o símbolos).

Si deseamos enviar una entrada estándar al sistema, escribimos el siguiente comando en la consola:
```bash
echo hello
```

### 2. Salida Estándar (*Standard Output* / `stdout`)
La **salida estándar** es la información devuelta por el sistema operativo a través del *shell*. Del mismo modo que un amigo responde a tu pregunta, la salida es la respuesta directa de la computadora al comando ingresado. Es el resultado visible que recibes en pantalla.

Continuando con nuestro ejemplo anterior, al presionar la tecla `ENTER` tras ingresar `echo hello`, el *shell* devuelve de inmediato la salida correspondiente:
```text
hello
```

### 3. Error Estándar (*Standard Error* / `stderr`)
El **error estándar** contiene los mensajes de advertencia o falla devueltos por el sistema operativo a través del *shell* cuando no es posible responder o ejecutar una orden.

> [!IMPORTANT]
> **Causas Comunes de Errores en la Consola:**
> * **Errores de sintaxis o de escritura:** Escribir mal el nombre de un comando o de un parámetro.
> * **Recursos inexistentes:** El sistema no reconoce la orden o no encuentra el archivo/directorio solicitado.
> * **Permisos insuficientes:** El usuario actual no cuenta con las atribuciones necesarias de seguridad para ejecutar la acción.

Si intentamos ingresar `eco hello` en la consola (escribiendo intencionalmente `eco` en lugar de `echo`), al presionar `ENTER` el sistema operativo no sabrá cómo responder y generará inmediatamente un mensaje de error estándar.

---

## Puntos Clave (Key Takeaways)

* **Tres Flujos de Comunicación:** Toda interacción con el *shell* se limita a tres canales: recibir una orden (entrada), devolver un resultado exitoso (salida) o notificar un problema (error).
* **Entrada Estándar (`stdin`):** Información e instrucciones introducidas por el usuario mediante el teclado para ser procesadas por el *kernel*.
* **Salida Estándar (`stdout`):** Respuesta que genera el sistema operativo y proyecta en pantalla tras procesar correctamente una orden (por ejemplo, con el comando `echo`).
* **Error Estándar (`stderr`):** Mensajes que emite el sistema cuando no puede procesar un comando debido a faltas de ortografía, recursos no encontrados o permisos insuficientes.
