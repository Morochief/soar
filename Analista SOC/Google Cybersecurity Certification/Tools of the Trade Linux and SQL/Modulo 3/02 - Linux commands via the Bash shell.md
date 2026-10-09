# Linux commands via the Bash shell

¡Te damos la bienvenida de nuevo! Antes de adentrarnos en comandos específicos de Linux, exploraremos en mayor detalle los aspectos fundamentales de la comunicación con el sistema operativo a través del *shell*.

---

## Introducción del Instructor

Ser capaz de utilizar comandos de Linux es una competencia técnica esencial para todo profesional en ciberseguridad. Como analista de seguridad, trabajarás frecuentemente con registros del servidor (*server logs*) y necesitarás saber cómo navegar, administrar y analizar archivos de forma remota sin contar con una interfaz gráfica de usuario (*GUI*). 

Además, deberás verificar y configurar accesos para usuarios y grupos, así como otorgar autorizaciones y definir permisos de archivos. Por ello, el desarrollo de habilidades en la línea de comandos es crucial para tu desempeño diario.

---

## Desarrollo Temático: Fundamentos y Sintaxis en Bash

Cuando estudiamos la arquitectura de Linux, aprendimos que el *shell* es uno de los componentes principales del sistema operativo y que existen diversos tipos de *shells*. En esta sección utilizaremos el **Bash shell**, que es el *shell* predeterminado en la mayoría de las distribuciones de Linux. Afortunadamente, los comandos clave de Linux que aprenderás son prácticamente idénticos entre diferentes *shells*.

### Escribir y Estructurar Comandos en Bash

Comunicarte con el sistema operativo es similar a mantener una conversación: tú ingresas un comando y el sistema responde con una solución o resultado. Un **comando** es una instrucción directa que le ordena a la computadora realizar una acción específica.

1. **El Indicador de Consola (*Prompt*):**
   Al abrir la consola, verás el símbolo de dólar (`$`) justo antes del cursor. Este símbolo representa tu indicador (*prompt*) para ingresar una nueva instrucción.
2. **Propósito de los Comandos:**
   * Algunos comandos le piden al sistema buscar un recurso específico (como un archivo).
   * Otros le ordenan iniciar un programa o aplicación.
   * Otros imprimen una cadena de texto (*string*) en pantalla (como el comando `echo`).

### Uso de Argumentos (*Arguments*)

A menudo, un comando por sí solo no está completo si requiere información adicional para ejecutarse. Aquí es donde entran los **argumentos**.

> [!NOTE]
> **¿Qué es un argumento?** 
> Un **argumento** (*argument*) es la información específica o el parámetro que un comando necesita para completar su tarea. Algunos comandos pueden recibir múltiples argumentos simultáneamente.

Por ejemplo, si deseamos usar `echo` para mostrar un mensaje en pantalla, debemos proporcionar la cadena de texto como argumento:

```bash
echo "You are doing great!"
```

En este ejemplo:
* `echo` es el **comando**.
* `"You are doing great!"` es el **argumento** (una cadena de texto).

Al presionar `ENTER`, la consola procesa el comando y devuelve la salida esperada:
```text
You are doing great!
```

### Sensibilidad a Mayúsculas y Minúsculas (*Case Sensitivity*)

> [!IMPORTANT]
> **Regla de Oro en Linux:**
> En Linux, **todos los comandos, argumentos, nombres de archivos y nombres de directorios son estrictamente sensibles a mayúsculas y minúsculas (*case sensitive*)**. Por ejemplo, los comandos `echo`, `Echo` y `ECHO` no son equivalentes; solo `echo` en minúsculas será reconocido por el sistema.

---

## Puntos Clave (Key Takeaways)

* **Competencia Esencial:** La gestión de archivos, la revisión de *logs* y el control de accesos sin interfaz gráfica (GUI) requieren un dominio fluido de la línea de comandos.
* **Estándar Bash:** El *Bash shell* es el estándar en la mayoría de las distribuciones de Linux y comparte comandos fundamentales con otros *shells*.
* **Comando vs. Argumento:** Un *comando* es la acción deseada y un *argumento* es la información específica requerida para llevar a cabo dicha acción.
* **Sensibilidad a Mayúsculas (*Case Sensitivity*):** Linux distingue estrictamente entre mayúsculas y minúsculas en comandos, argumentos, archivos y carpetas.
