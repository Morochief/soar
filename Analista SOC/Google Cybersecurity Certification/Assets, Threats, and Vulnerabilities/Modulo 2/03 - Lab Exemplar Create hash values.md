# Laboratorio: Create hash values

## Resumen de la Actividad
Como analista de seguridad, deberás implementar controles de seguridad para proteger a las organizaciones contra una gran variedad de amenazas.

Ahí es donde entran en juego los **hashes**. Anteriormente, aprendiste que una función hash es un algoritmo que produce un código que no se puede descifrar ni revertir. Las funciones hash se utilizan para identificar de forma única el contenido de un archivo (como si fuera su huella digital), de modo que puedas comprobar si ha sido modificado. Este código proporciona un identificador único conocido como **valor hash** o *digest*.

Por ejemplo, un programa malicioso puede imitar a un programa original. Si tan solo una línea de código es diferente a la del programa original, el algoritmo producirá un valor hash completamente distinto. Los equipos de seguridad pueden entonces identificar que el programa ha sido alterado y trabajar para mitigar el riesgo.

Hay muchas herramientas disponibles para comparar hashes en varios escenarios, pero para un analista de seguridad es importante saber cómo comparar hashes manualmente utilizando la terminal.

En esta actividad de laboratorio, crearemos valores hash para dos archivos y utilizaremos comandos de Linux para examinar manualmente las diferencias.

---

## Escenario
En este escenario, debes investigar si dos archivos son idénticos o diferentes. 

Así es como realizarás esta tarea: 
1.  Primero, mostrarás el contenido de dos archivos y crearás valores hash para cada uno. 
2.  Luego, examinarás los hashes y los compararás para determinar la integridad de los datos.

*(Nota: El laboratorio comienza en tu directorio de inicio, `/home/analyst`, como el directorio de trabajo actual. Este directorio contiene dos archivos, `file1.txt` y `file2.txt`.)*

---

## Tarea 1: Generar hashes para archivos
En esta tarea, necesitas mostrar el contenido de cada uno de estos archivos. Luego generarás un valor hash para cada archivo y enviarás esos valores a nuevos archivos, los cuales usarás para examinar las diferencias.

Usa el comando `ls` para listar el contenido del directorio:
```bash
ls
```
> Se listan los dos archivos: `file1.txt` y `file2.txt`.

Usa el comando `cat` para mostrar el contenido del archivo `file1.txt`:
```bash
cat file1.txt
```

Usa el comando `cat` para mostrar el contenido del archivo `file2.txt`:
```bash
cat file2.txt
```

**Revisa la salida de los contenidos de los dos archivos:**
> `X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*`

¿Acaso los contenidos de los dos archivos parecen idénticos cuando usas el comando `cat`?
*   **Sí.** Los contenidos de los dos archivos parecen exactamente idénticos al ojo humano (se trata de la famosa cadena de texto EICAR para probar antivirus).

Aunque el contenido de ambos archivos parece idéntico al mostrarlos en pantalla, necesitas generar el hash de cada archivo para determinar criptográficamente si los archivos son en realidad distintos.

Usa el comando `sha256sum` para generar el hash del archivo `file1.txt`:
```bash
sha256sum file1.txt 
```

Ahora repite el mismo paso para el archivo `file2.txt`:
```bash
sha256sum file2.txt
```

**Revisa los hashes generados:**
> `131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267  file1.txt`
> `2558ba9a4cad1e69804ce03aa2a029526179a91a5e38cb723320e83af9ca017b  file2.txt`

¿Ambos archivos producen el mismo valor hash?
*   **No.** El valor hash generado para `file1.txt` es radicalmente diferente al hash generado para `file2.txt`, lo que indica matemáticamente que los contenidos de los archivos *no son idénticos*, a pesar de que a simple vista lo parecían. Un espacio oculto o un salto de línea bastan para cambiar completamente el hash.

---

## Tarea 2: Comparar hashes
En esta tarea, escribirás los hashes resultantes en dos archivos de texto separados y luego usarás un comando de comparación para encontrar la diferencia exacta.

Usa el comando `sha256sum` para generar el hash de `file1.txt`, y usa el operador de redirección `>>` para enviar la salida a un nuevo archivo llamado `file1hash`:
```bash
sha256sum file1.txt >> file1hash
```

Realiza el mismo paso para el archivo `file2.txt`, enviando la salida al archivo `file2hash`:
```bash
sha256sum file2.txt >> file2hash
```

Ahora deberías tener dos hashes escritos en archivos separados. Puedes usar el comando `cat` para mostrarlos en la terminal y compararlos manualmente:
```bash
cat file1hash
cat file2hash
```

> [!NOTE]
> Aunque el contenido de `file1.txt` y `file2.txt` parecía idéntico anteriormente, los hashes escritos en los nuevos archivos son completamente distintos.

Ahora, puedes usar el comando `cmp` (*compare*) para comparar los dos archivos byte por byte. Si se encuentra una diferencia, el comando reporta el byte exacto y el número de línea donde se detectó el primer desvío.

Usa el comando `cmp` para resaltar las diferencias:
```bash
cmp file1hash file2hash
```

**Revisa la salida (Output):**
> `file1hash file2hash differ: char1, line 1`

La salida del comando `cmp` indica que los hashes difieren ya desde el primer carácter de la primera línea.

---

## Conclusión
¡Gran trabajo! En este laboratorio practicaste cómo:
1.  Calcular (computar) hashes de algoritmos SHA-256 usando el comando `sha256sum`.
2.  Escribir (redireccionar) la salida de comandos a nuevos archivos usando `>>`.
3.  Mostrar los hashes usando el comando `cat`.
4.  Comparar la estructura de archivos usando el comando `cmp`.

Estas son herramientas invaluables que utilizarás diariamente en tu SOC para validar la **Integridad de los datos** (*Data Integrity*) durante las investigaciones de malware y los incidentes de seguridad.
