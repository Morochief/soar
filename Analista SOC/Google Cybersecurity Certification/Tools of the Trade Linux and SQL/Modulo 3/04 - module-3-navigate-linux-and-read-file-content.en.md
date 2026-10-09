# Reading: Navigate Linux and read file content

En esta lectura revisarás cómo navegar por el sistema de archivos utilizando comandos de Linux en Bash [cite: 20]. Explorarás a profundidad la organización del Estándar de Jerarquía del Sistema de Archivos (**FHS** - *Filesystem Hierarchy Standard*), repasarás varios comandos comunes de Linux para la navegación y lectura de archivos, y aprenderás un par de comandos nuevos indispensables [cite: 20].

---

## Introducción del Equipo de Ciberseguridad de Google

Para un analista de ciberseguridad, la capacidad de navegar con rapidez por el sistema de archivos y leer eficientemente el contenido de logs y configuraciones sin depender de una interfaz gráfica es una habilidad fundamental [cite: 20]. La mayoría de las investigaciones de incidentes, auditorías de servidores y análisis forenses se llevan a cabo mediante la terminal, por lo que dominar la estructura del FHS y sus comandos asociados optimizará directamente tu flujo de trabajo en el SOC [cite: 20].

---

## Desarrollo Temático: Estructura del FHS y Comandos de Consola

### Estándar de Jerarquía del Sistema de Archivos (FHS)
El **FHS** es el componente de Linux que define la organización de datos, estructurando la disposición de directorios, contenidos y dispositivos de almacenamiento en el sistema operativo [cite: 20].

En el FHS, la ubicación de cualquier elemento se describe mediante una **ruta de archivo** (*file path*) [cite: 20]. Los distintos niveles dentro de la jerarquía se separan mediante una barra diagonal (`/`) [cite: 20].

#### 1. Directorio Raíz (*Root directory*)
El directorio raíz es el nivel más alto en la jerarquía de Linux y se representa siempre con una sola barra diagonal (`/`) [cite: 20]. Todos los subdirectorios del sistema se ramifican a partir del directorio raíz hacia múltiples niveles según sea necesario [cite: 20].

#### 2. Directorios Estándar del FHS
Directamente debajo del directorio raíz se ubican las carpetas estándar del sistema [cite: 20]:

* **`/home`:** Almacena los directorios personales de cada usuario registrado en el sistema [cite: 20].
* **`/bin`:** Proviene de *"binary"* y contiene archivos binarios y ejecutables (archivos con secuencias de instrucciones necesarias para ejecutar programas y funciones) [cite: 20].
* **`/etc`:** Guarda los archivos de configuración críticos del sistema operativo y de las aplicaciones [cite: 20].
* **`/tmp`:** Almacena archivos temporales [cite: 20]. 

> [!WARNING]
> **Nota de Seguridad sobre `/tmp`:** El directorio `/tmp` es frecuentemente utilizado por atacantes para alojar *scripts* o cargas maliciosas (*payloads*), ya que cualquier usuario en el sistema tiene permisos para modificar e interactuar con los datos almacenados allí [cite: 20].

* **`/mnt`:** Proviene de *"mount"* y se utiliza para montar dispositivos de almacenamiento secundarios o medios extraíbles, como unidades USB y discos duros [cite: 20].

> [!TIP]
> **Consejo Profesional:** Puedes ejecutar el comando `man hier` en la terminal para obtener una descripción detallada sobre la jerarquía FHS y todos sus directorios estándar [cite: 20].

#### 3. Subdirectorios Específicos de Usuario y Tipos de Rutas
Dentro de `/home` se encuentran los subdirectorios dedicados a cada usuario (por ejemplo, `/home/analyst` o `/home/analyst2`), donde cada uno almacena sus archivos y carpetas personales (como `projects`, `logs` o `reports`) [cite: 20].

> [!NOTE]
> **El Símbolo Tilde (`~`):** Cuando una ruta se dirige a una ubicación dentro del directorio personal del usuario actual, dicha carpeta personal se puede representar con el símbolo tilde (`~`) [cite: 20]. Por ejemplo, `/home/analyst/logs` se puede abreviar como `~/logs` [cite: 20].

Para navegar entre directorios, puedes hacer uso de dos tipos de rutas [cite: 20]:
* **Ruta Absoluta (*Absolute file path*):** Ruta completa que inicia de manera explícita desde la raíz (`/`) [cite: 20]. Ejemplo: `/home/analyst/projects` [cite: 20].
* **Ruta Relativa (*Relative file path*):** Ruta que parte del directorio de trabajo actual del usuario [cite: 20]. Utiliza un punto (`.`) para hacer referencia al directorio actual y dos puntos (`..`) para representar al directorio padre [cite: 20]. Ejemplo: `../projects` [cite: 20].

---

### Comandos Clave para la Navegación del Sistema de Archivos

Para desplazarte e inspeccionar la estructura del FHS, utilizas principalmente tres comandos [cite: 20]:

#### `pwd` (*Print Working Directory*)
Muestra en pantalla la ruta absoluta del directorio de trabajo actual [cite: 20].
* **Ejemplo:** Si estás en tu carpeta personal siendo el usuario `analyst`, al ingresar `pwd` obtendrás `/home/analyst` [cite: 20].

> [!TIP]
> **Consejo Profesional:** Para verificar con qué cuenta de usuario estás convalidado actualmente, utiliza el comando `whoami` [cite: 20].

#### `ls` (*List*)
Muestra los nombres de los archivos y subdirectorios contenidos en la ubicación actual [cite: 20].
* **Uso con argumentos:** Si deseas listar el contenido de un directorio distinto al actual, puedes agregar la ruta absoluta o relativa como argumento [cite: 20]. Por ejemplo, desde `/home/analyst` puedes listar el contenido de la carpeta de proyectos con `ls projects` o `ls /home/analyst/projects` [cite: 20].

#### `cd` (*Change Directory*)
Permite cambiar la ubicación del directorio de trabajo [cite: 20].
* Puedes navegar a una subcarpeta ingresando su nombre (`cd projects`) o a cualquier directorio del sistema especificando la ruta absoluta (`cd /home/analyst/logs`) [cite: 20].

> [!TIP]
> **Consejo Profesional:** Ejecuta `cd ..` usando rutas relativas para retroceder o subir un nivel en la estructura jerárquica [cite: 20].

---

### Comandos Comunes para Leer el Contenido de Archivos

Al investigar incidentes o auditar la seguridad, requerirás inspeccionar el texto almacenado en los archivos [cite: 20]. Para ello dispones de los siguientes comandos [cite: 20]:

#### `cat` (*Concatenate*)
Imprime en la pantalla todo el contenido completo de un archivo de principio a fin [cite: 20].
* **Sintaxis:** `cat updates.txt` [cite: 20].

#### `head`
Muestra únicamente el comienzo de un archivo (por defecto, las primeras 10 líneas) [cite: 20]. Es ideal para verificar rápidamente la estructura o encabezado de un archivo sin cargarlo entero [cite: 20].
* **Sintaxis:** `head updates.txt` [cite: 20].

> [!TIP]
> **Personalizar líneas devueltas:** Puedes modificar el número de líneas mostradas incluyendo la opción `-n` [cite: 20]. Por ejemplo, para ver solo las primeras 5 líneas escribe: `head -n 5 updates.txt` [cite: 20].

#### `tail`
Realiza el comportamiento opuesto a `head`: despliega únicamente el final de un archivo (por defecto, las últimas 10 líneas) [cite: 20].
* **Sintaxis:** `tail updates.txt` [cite: 20].

> [!TIP]
> **Uso Clave en Ciberseguridad:** `tail` es una herramienta extraordinaria para leer las entradas más recientes registradas al final de un archivo de *log* (*log file*) durante el monitoreo de eventos en tiempo real [cite: 20].

#### `less`
Muestra el contenido de un archivo de manera paginada (pantalla por pantalla), facilitando la navegación cómoda hacia adelante y hacia atrás dentro de archivos voluminosos [cite: 20].
* **Sintaxis:** `less updates.txt` [cite: 20].

Una vez dentro de la interfaz del comando `less`, utilizas los siguientes controles de teclado [cite: 20]:
| Tecla | Acción |
| :--- | :--- |
| **Barra espaciadora** | Avanzar una página completa [cite: 20] |
| **`b`** | Retroceder una página completa [cite: 20] |
| **Flecha abajo** | Avanzar una línea [cite: 20] |
| **Flecha arriba** | Retroceder una línea [cite: 20] |
| **`q`** | Salir de `less` y regresar a la terminal [cite: 20] |

---

## Puntos Clave (Key Takeaways)

* **Organización FHS:** Comprender el Estándar de Jerarquía del Sistema de Archivos permite ubicar de forma predecible directorios críticos como `/etc` (configuraciones), `/tmp` (temporales/amenazas) y `/bin` (ejecutables) [cite: 20].
* **Comandos de Navegación:** Los comandos `pwd` (ubicación), `ls` (listar) y `cd` (cambiar directorio) forman el núcleo de la movilidad en Linux [cite: 20].
* **Técnicas de Lectura de Archivos:** Selecciona la herramienta según el caso de uso: `cat` para archivos pequeños, `head` para inspeccionar encabezados, `tail` para monitorear los registros más recientes en *logs*, y `less` para navegar documentos extensos por páginas [cite: 20].
* **Flexibilidad con Rutas:** Dominar la diferencia entre rutas absolutas (desde `/`) y relativas (`.`, `..`, `~`) agiliza la ejecución de tareas de administración y respuesta a incidentes [cite: 20].
