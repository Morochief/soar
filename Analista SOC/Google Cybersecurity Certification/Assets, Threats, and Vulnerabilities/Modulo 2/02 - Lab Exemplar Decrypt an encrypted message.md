# Laboratorio: Decrypt an encrypted message

## Resumen de la Actividad
Anteriormente, aprendiste sobre criptografía y cómo el cifrado (*encryption*) y el descifrado (*decryption*) pueden utilizarse para asegurar la información en línea. También se te presentó el cifrado César (*Caesar cipher*), uno de los algoritmos criptográficos más antiguos utilizados para proteger la privacidad de las personas.

Como analista SOC, es fundamental que comprendas el papel del cifrado para asegurar los datos y que estés familiarizado con los controles de seguridad adecuados para hacerlo.

En esta actividad de laboratorio, serás guiado a través de algunas actividades criptográficas básicas utilizando comandos de Linux (*Bash shell*) para descifrar archivos y revelar mensajes ocultos.

---

## Escenario
En este escenario, **todos los archivos en tu directorio de inicio (*home*) han sido cifrados por un atacante**. Necesitarás utilizar comandos de Linux para romper el cifrado César y descifrar los archivos para poder leer los mensajes ocultos que contienen.

Así es como realizarás esta tarea: 
1.  Primero, explorarás el contenido del directorio de inicio y leerás el contenido de un archivo. 
2.  Luego, encontrarás un archivo oculto y descifrarás el código César que contiene. 
3.  Finalmente, descifrarás el archivo de datos principal utilizando OpenSSL para recuperar tu información y revelar el mensaje secreto.

*(Nota: El laboratorio comienza con la sesión iniciada como el usuario `analyst`, siendo tu directorio de trabajo actual `/home/analyst`.)*

---

## Tarea 1: Leer el contenido de un archivo
El laboratorio comienza en tu directorio de inicio, `/home/analyst`. En esta tarea, necesitas explorar el contenido de tu directorio y leer un archivo para obtener más instrucciones.

Usa el comando `ls` para listar los archivos en el directorio de trabajo actual:
```bash
ls /home/analyst
```
> Se listan dos archivos, `Q1.encrypted` y `README.txt`, y un subdirectorio, `caesar`.

El archivo `README.txt` contiene un mensaje importante. Usa el comando `cat` para ver su contenido:
```bash
cat README.txt
```

**Salida (Output):**
> *Hello, All of your data has been encrypted. To recover your data, you will need to solve a cipher. To get started look for a hidden file in the caesar subdirectory.*

El mensaje advierte que el subdirectorio `caesar` contiene un archivo oculto. En la próxima tarea, deberás encontrar ese archivo y resolver el cifrado César que lo protege.

---

## Tarea 2: Encontrar un archivo oculto
En esta tarea, necesitas encontrar un archivo oculto y descifrar su cifrado César. Esto te dará la llave para la siguiente tarea.

Primero, usa el comando `cd` para cambiar al subdirectorio `caesar`:
```bash
cd caesar
```

Usa el comando `ls -a` para listar todos los archivos, incluyendo los **archivos ocultos** (los cuales empiezan con un punto `.` en Linux):
```bash
ls -a
```
**Salida (Output):**
> `.  ..  .leftShift3`

Usa el comando `cat` para listar el contenido del archivo oculto `.leftShift3`:
```bash
cat .leftShift3
```

El mensaje dentro de `.leftShift3` parece estar mezclado (ofuscado). Esto se debe a que los datos han sido cifrados usando un **Cifrado César**. Este cifrado se puede resolver desplazando cada carácter del alfabeto hacia la izquierda o derecha por un número fijo de espacios (en este caso, *leftShift3* indica 3 espacios a la izquierda. Así, la "d" es una "a", y la "e" es una "b").

Puedes descifrar el Cifrado César en el archivo usando el comando `tr` (Translate):
```bash
cat .leftShift3 | tr "d-za-cD-ZA-C" "a-zA-Z"
```

> [!NOTE]
> **El Comando `tr`**: El comando `tr` traduce o reemplaza texto de un conjunto de caracteres a otro usando un mapeo. El primer parámetro representa el conjunto de entrada y el segundo el conjunto de salida. Al indicarle `"d-za-cD-ZA-C" "a-zA-Z"`, le estamos diciendo a Linux que traduzca el alfabeto desplazado de vuelta a su orden original (A-Z).

**Salida (Output) Descifrada:**
> *In order to recover your files you will need to enter the following command: `openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute`*

¡El archivo oculto nos acaba de revelar el comando exacto para desencriptar el ataque! 
Ahora, regresa a tu directorio de inicio antes de completar la siguiente tarea:
```bash
cd ~
```

---

## Tarea 3: Descifrar un archivo (OpenSSL)
Ahora que has resuelto el cifrado César, necesitas usar el comando revelado en la tarea anterior para descifrar el archivo principal y recuperar tu información.

Ejecuta el comando exacto que descubriste:
```bash
openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute
```

**Desglose del comando:**
*   `openssl`: Invoca la herramienta OpenSSL para revertir el cifrado.
*   `aes-256-cbc`: Indica el cifrado simétrico robusto que se usará.
*   `-pbkdf2`: Añade seguridad adicional a la llave (función de derivación).
*   `-a`: Indica la codificación deseada para la salida.
*   `-d`: Especifica que la acción es **Descifrar** (*decrypt*).
*   `-in`: Especifica el archivo de entrada (input = `Q1.encrypted`).
*   `-out`: Especifica el archivo de salida (output = `Q1.recovered`).
*   `-k`: Especifica la contraseña/llave, que en este ejemplo es `ettubrute`.

Usa el comando `ls` para listar los contenidos de tu directorio de trabajo actual y comprobar si funcionó:
```bash
ls
```
¡El nuevo archivo `Q1.recovered` en el directorio es tu archivo descifrado! Usa el comando `cat` para leer el mensaje de victoria:
```bash
cat Q1.recovered
```

**Salida (Output):**
> *If you are able to read this, then you have successfully decrypted the classic cipher text. You recovered the encryption key that was used to encrypt this file. Great work!*

---

## Conclusión
¡Gran trabajo! Ahora tienes experiencia práctica utilizando comandos de Linux (Bash Shell) para:
1.  Listar archivos ocultos usando `ls -a`.
2.  Descifrar un cifrado César en la terminal usando pipes `|` y el comando `tr`.
3.  Descifrar un archivo con seguridad de grado industrial utilizando `openssl`. 

Este es un hito táctico importante en tu viaje hacia la comprensión real del cifrado y descifrado en el trabajo diario de un analista de seguridad.
