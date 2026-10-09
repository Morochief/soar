# Reading: Different types of shells

El dominio y manejo de los entornos de terminal de Linux (*shells*) es una habilidad fundamental e indispensable para todo profesional en ciberseguridad [cite: 24]. Los *shells* se utilizan a diario para ejecutar comandos, administrar sistemas, inspeccionar archivos y automatizar tareas esenciales [cite: 24]. En esta lectura profundizaremos en el concepto del *shell*, cómo facilita la comunicación con el sistema y conoceremos los distintos tipos de *shells* existentes, con especial énfasis en aquel que utilizaremos a lo largo de este curso [cite: 24].

---

## Introducción del Equipo de Ciberseguridad de Google

En el trabajo diario dentro de un Centro de Operaciones de Seguridad (**SOC**), el *shell* constituye tu interfaz principal para interactuar directamente con el sistema operativo [cite: 24]. Comprender las diferencias entre los tipos de *shells* y dominar el uso de la línea de comandos te otorgará la velocidad y precisión necesarias para analizar incidentes, auditar configuraciones y responder ante amenazas de manera efectiva [cite: 24].

---

## Desarrollo Temático: Comunicación y Tipos de Shells en Linux

### Comunicación a través de un Shell
Como se estudió anteriormente, el **shell** es el intérprete de línea de comandos (*command-line interpreter*) [cite: 24]. Puedes visualizarlo como un traductor entre el usuario y el sistema informático [cite: 24]. 

El *shell* permite enviar instrucciones al equipo y recibir sus respuestas en pantalla [cite: 24]. Al ingresar un comando, el *shell* ejecuta múltiples procesos internos para [cite: 24]:
1. Interpretar y validar la sintaxis de la instrucción ingresada [cite: 24].
2. Enviar la orden procesada al **kernel** (el núcleo del sistema operativo) [cite: 24].
3. Recibir la respuesta del *kernel* y devolver el resultado procesado al usuario en la pantalla [cite: 24].

---

### Tipos de Shells en Linux
Existen diversos tipos de *shells* en los sistemas operativos derivados de Unix y Linux [cite: 24]. Entre los más conocidos se encuentran [cite: 24]:

*   **Bourne-Again Shell (`bash`):** El estándar principal y más extendido en Linux [cite: 24].
*   **C Shell (`csh`):** Un *shell* cuya sintaxis se asemeja al lenguaje de programación C [cite: 24].
*   **Korn Shell (`ksh`):** Un *shell* diseñado para combinar características de `sh` y `csh` [cite: 24].
*   **Enhanced C Shell (`tcsh`):** Una versión mejorada e interactiva del C Shell [cite: 24].
*   **Z Shell (`zsh`):** Un *shell* moderno con potentes funciones de autocompletado y personalización [cite: 24].

Todos los *shells* de Linux comparten y ejecutan los comandos estándar del sistema operativo, pero pueden diferir en características secundarias, como el indicador de entrada de línea (*prompt*) [cite: 24]. Por ejemplo, *shells* como `ksh` y `bash` utilizan el símbolo de dólar (`$`) para indicar el punto donde el usuario debe escribir sus comandos [cite: 24]. En cambio, otros *shells* como `zsh` suelen emplear el símbolo de porcentaje (`%`) para esta misma función [cite: 24].

---

### El Shell Bash (`bash`)
**Bash** (*Bourne-Again Shell*) es el *shell* predeterminado en la mayoría de las distribuciones de Linux [cite: 24]. Se considera un entorno sumamente amigable para el usuario (*user-friendly*), ideal tanto para ejecutar comandos básicos del sistema como para desarrollar proyectos complejos de automatización mediante scripts (*shell scripting*) [cite: 24].

> [!IMPORTANT]
> **El Estándar en Ciberseguridad:** **Bash** es el *shell* más popular y ampliamente utilizado en la profesión de ciberseguridad [cite: 24]. A lo largo de este certificado, utilizarás **Bash** de manera continua para aprender, ejercitar y dominar los comandos de Linux [cite: 24].

---

## Puntos Clave (Key Takeaways)

*   **Rol del Shell:** Funciona como un traductor entre el usuario y el sistema operativo, interpretando instrucciones para enviarlas al *kernel* y presentar las respuestas [cite: 24].
*   **Variedad de Entornos:** Existen múltiples tipos de *shells* (`bash`, `csh`, `ksh`, `tcsh`, `zsh`), los cuales comparten los comandos fundamentales de Linux pero pueden variar en su sintaxis e indicadores de consola (*prompt*) [cite: 24].
*   **Indicadores de Consola:** `bash` y `ksh` utilizan convencionalmente el símbolo `$` en el *prompt*, mientras que `zsh` utiliza `%` [cite: 24].
*   **Prevalencia de Bash:** `bash` es el *shell* predeterminado de la mayoría de las distribuciones y el estándar indiscutible en la industria de la ciberseguridad [cite: 24].
