# Introduction to Linux, SQL, and Python

## Más allá de las herramientas básicas
Como discutimos en la lectura anterior, los analistas de SOC utilizan software empaquetado como SIEM, *playbooks* y analizadores de red (*packet sniffers*) para gestionar las defensas.

Sin embargo, para investigar de verdad, los analistas deben "bajar al barro" y utilizar lenguajes de programación y manipular sistemas operativos directamente desde la terminal.

## ¿Por qué los Analistas deben saber programar?
La programación permite a los analistas crear un conjunto de instrucciones precisas que la computadora ejecutará por ellos. Esto permite completar tareas defensivas repetitivas con una precisión y eficiencia inhumanas, reduciendo a cero el riesgo de "error humano", y ahorrando días enteros de trabajo manual al investigar un ciberataque masivo.

## El Trío de Oro del SOC

### 1. El Sistema Operativo: Linux
Linux es un sistema operativo de código abierto (*open-source*), gratuito y modificable por cualquier persona. Prácticamente toda la infraestructura de la nube y los servidores corporativos del mundo corren sobre Linux.

A diferencia de sistemas operativos diseñados para usuarios comunes (como Windows o macOS), en los servidores corporativos **Linux carece de entorno gráfico y se basa exclusivamente en la Línea de Comandos (Terminal/CLI)**.
Aunque Linux no es un lenguaje de programación *per se*, usarás comandos de texto puramente técnicos para hablar directamente con las entrañas del sistema.

Un uso cotidiano absoluto de la terminal de Linux para un analista es leer *logs* de servidores en vivo. Por ejemplo, podrías escribir comandos en la pantalla negra de Linux para filtrar miles de registros de error de un servidor web en segundos mientras investigas un pico de tráfico de red extraño.

### 2. SQL (*Structured Query Language*)
SQL (Lenguaje de Consulta Estructurado) es el lenguaje estándar utilizado para interactuar y extraer información cruda desde una **base de datos** corporativa.

Una base de datos es una tabla gigantesca y organizada de información. El SIEM de tu empresa almacenará cientos de millones de *logs*. Como analista, usarás consultas SQL diariamente para filtrar todo ese océano de datos en milisegundos y encontrar la aguja en el pajar (ej. *"Muéstrame todos los intentos de contraseña fallidos del usuario Administrador en los últimos 15 minutos"*).

### 3. Python
Los profesionales de ciberseguridad (tanto del Blue Team como del Red Team) aman **Python**. Utilizarás Python para crear pequeños programas de texto (*scripts*) que hagan el trabajo sucio por ti. Te permite automatizar tareas aburridas y repetitivas (como comparar un archivo Excel con direcciones IP sospechosas contra tu base de datos) con una precisión total.

---

> [!NOTE]
> **Adáptate a la industria:**
> Como futuro profesional, debes entender que cada empresa privada tendrá un entorno (*toolkit*) distinto. Lo que buscan los empleadores al pedirte que sepas Linux, SQL y Python, no es que seas un programador experto, sino demostrarles que **comprendes la lógica computacional base** y que puedes adaptarte rápidamente a las herramientas internas de su organización.
