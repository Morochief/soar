# Exemplar: Examine input and output in the shell

En esta actividad práctica de laboratorio, utilizaste el comando `echo` para examinar cómo se reciben las entradas (*input*) y cómo se devuelven las salidas (*output*) en la consola [cite: 24]. Posteriormente, utilizaste el comando `expr` para realizar cálculos matemáticos básicos directamente desde la línea de comandos de Linux [cite: 24].

Entender la dinámica de entrada y salida es un pilar fundamental para comunicarse con el sistema operativo Linux a través del *shell* [cite: 24]. Como analista de seguridad, necesitarás ingresar comandos con precisión y saber reconocer cuándo la consola devuelve una salida esperada o un mensaje de error [cite: 24].

---

## Introducción del Equipo de Ciberseguridad de Google

Dominar el flujo de entrada, procesamiento y salida en la línea de comandos te permitirá comunicarte eficientemente con los sistemas operativos bajo tu supervisión [cite: 24]. Ya sea calculando volumen de alertas, filtrando eventos de seguridad o limpiando tu espacio de trabajo para evitar distracciones, estos comandos fundamentales forman la base de tu arsenal operativo en el SOC [cite: 24].

---

## Desarrollo Temático: Exploración Práctica de Entrada y Salida

### Escenario Operativo
Como profesional de la seguridad, es vital que te sientas cómodo interactuando con la computadora mediante el *shell* [cite: 24]. En este ejercicio, ingresas cadenas de texto específicas para recibir la respuesta del sistema y ejecutas cálculos matemáticos para que el sistema operativo devuelva los resultados [cite: 24].

---

### Tarea 1: Generar Salida con el Comando `echo`
El comando `echo` en el *shell* Bash imprime en pantalla la cadena de texto (*string*) especificada [cite: 24].

1. **Ingresar texto simple:**
   ```bash
   echo hello
   ```
   * **Entrada (*Input*):** `echo hello` [cite: 24]
   * **Salida (*Output*):** `hello` [cite: 24]

2. **Ingresar texto con comillas:**
   ```bash
   echo "hello"
   ```
   * **Salida (*Output*):** `hello` [cite: 24]

> [!NOTE]
> Las comillas son opcionales en este caso simple, pero le indican al *shell* que agrupe una serie de caracteres [cite: 24]. Esto es especialmente útil cuando necesitas pasar una cadena que contiene caracteres especiales que de otro modo podrían ser malinterpretados por el comando [cite: 24].

3. **Imprimir tu nombre en la consola:**
   ```bash
   echo "Tu Nombre"
   ```
   El nombre ingresado dentro de la cadena se devolverá como la salida estándar en pantalla [cite: 24].

---

### Tarea 2: Generar Salida con el Comando `expr`
El comando `expr` (*expression*) evalúa y realiza cálculos matemáticos enteros básicos desde la línea de comandos [cite: 24].

#### Ejemplo de Ciberseguridad 1: Cálculo de Falsos Positivos
Imagina que el sistema SIEM te muestra que has recibido **32 alertas**, pero tras inspeccionarlas descubres que solo **8 requerían acción real** [cite: 24]. Deseas calcular cuántas alertas correspondieron a falsos positivos (*false positives*) para enviar retroalimentación al equipo que configura las reglas de detección [cite: 24].

Para ello, restamos el número de alertas que requirieron acción del total de alertas [cite: 24]:
```bash
expr 32 - 8
```
* **Resultado devuelto:** `24` [cite: 24]

> [!IMPORTANT]
> El comando `expr` exige de forma obligatoria que **todos los términos y operadores estén separados por espacios** [cite: 24]. Por ejemplo, debes escribir `expr 32 - 8` y no `expr 32-8` [cite: 24].

#### Ejemplo de Ciberseguridad 2: Estimación de Intentos de Inicio de Sesión
Necesitas calcular el promedio de intentos de inicio de sesión (*login attempts*) esperados en el transcurso de un año completo [cite: 24]. De acuerdo con la telemetría recopilada, sabes que se han registrado un promedio de **3,500 intentos de inicio de sesión por mes** [cite: 24].

Para obtener el total anual, multiplicamos el promedio mensual por 12 meses [cite: 24]:
```bash
expr 3500 * 12
```
* **Resultado devuelto:** `42000` [cite: 24]

---

### Tarea 3: Limpiar la Consola Bash (`clear`)
Cuando trabajas en un entorno de línea de comandos, la pantalla puede llenarse rápidamente de entradas y salidas previas [cite: 24]. Esto genera saturación visual y dificulta concentrarse en la tarea actual [cite: 24].

El comando `clear` limpia la ventana del *shell* de todo el texto acumulado y posiciona el cursor en la esquina superior izquierda de la pantalla [cite: 24]:
```bash
clear
```

---

### Tarea Opcional: Cálculos Matemáticos Adicionales
Los operadores matemáticos soportados por `expr` son:
* **Suma:** `+` [cite: 24]
* **Resta:** `-` [cite: 24]
* **Multiplicación:** `*` [cite: 24]
* **División:** `/` [cite: 24]

> [!NOTE]
> **Limitaciones de `expr`:** El comando `expr` solo realiza cálculos matemáticos con números enteros (*integers*) [cite: 24]. No acepta puntos decimales ni devuelve resultados fraccionarios [cite: 24]. Todos los resultados se redondean hacia abajo al número entero más cercano [cite: 24]. Recuerda siempre separar términos y operadores con espacios (ej. `expr 25 + 15`) [cite: 24].

---

## Puntos Clave (Key Takeaways)

* **Generación de Salida en Pantalla:** El comando `echo` imprime directamente cadenas de texto en la consola, utilizando comillas opcionales o necesarias para agrupar caracteres especiales [cite: 24].
* **Evaluación de Expresiones (`expr`):** Permite resolver cálculos matemáticos con números enteros (suma, resta, multiplicación, división), siendo crucial separar cada término y operador con espacios [cite: 24].
* **Higiene de la Terminal (`clear`):** Mantiene la consola limpia y organizada para permitir una mayor concentración durante el análisis de logs y comandos [cite: 24].
* **Flujo Operativo Básico:** Un analista de ciberseguridad debe dominar el ciclo de entrada de comandos y la verificación de salidas o errores para operar con eficacia sobre entornos Linux [cite: 24].
