# Reading: Resources for completing Linux labs

En este curso participarás en actividades prácticas de laboratorio donde tendrás la oportunidad de ejercitar comandos de Linux directamente en la terminal[cite: 25]. Para llevar a cabo estos ejercicios interactivos, utilizarás una plataforma llamada Qwiklabs[cite: 25]. Esta lectura te guiará detalladamente en el funcionamiento de la plataforma, el uso de su consola y los accesos directos por teclado más útiles para trabajar en la línea de comandos[cite: 25].

> [!NOTE]
> **Requisito de Edad y Acceso a Qwiklabs:** Qwiklabs actualizó sus términos de servicio para incluir un requisito de edad mínima de 18 años para cumplir con las regulaciones de EE. UU. y la UE[cite: 25]. Si no tienes acceso a Qwiklabs, aún puedes completar el certificado y obtener tu insignia revisando las instrucciones de laboratorio, los modelos de ejemplo (*exemplars*) y participando en las demás actividades del programa[cite: 25].

---

## Introducción del Equipo de Ciberseguridad de Google

La práctica en entornos reales simulados es un pilar fundamental para consolidar tus competencias en ciberseguridad[cite: 25]. Dominar la interfaz de Qwiklabs y agilizar tu navegación en la terminal te permitirá ejecutar comandos con fluidez, inspeccionar sistemas eficientemente y concentrarte en el análisis técnico sin distracciones operativas[cite: 25].

---

## Desarrollo Temático: Guía Operativa de Qwiklabs

A continuación se detallan los componentes principales y los pasos para interactuar dentro del entorno interactivo de laboratorio[cite: 25]:

### 1. Iniciar un Laboratorio (*Start Lab*)
*   **Botón Start Lab:** En la página del laboratorio, debes hacer clic en **Start Lab** para desplegar una terminal temporal[cite: 25]. Al hacerlo, las instrucciones del laboratorio se moverán hacia el lado derecho de la pantalla[cite: 25].
*   **Ejecución:** Lee las instrucciones detenidamente y completa las tareas requeridas ingresando los comandos correspondientes en la terminal[cite: 25].
*   *Nota:* La terminal puede tardar unos momentos en cargarse por completo[cite: 25].

### 2. Cuadro de Diálogo de Control del Laboratorio
Una vez que haces clic en *Start Lab*, se abre el cuadro de diálogo de control del laboratorio[cite: 25]. Este panel contiene tres elementos fundamentales[cite: 25]:
*   El botón para finalizar el laboratorio (**End Lab**)[cite: 25].
*   El temporizador (*timer*)[cite: 25].
*   El botón para abrir la consola de Linux (**Open Linux Console**)[cite: 25].

> [!NOTE]
> Puedes ocultar o mostrar el cuadro de diálogo haciendo clic en el ícono correspondiente del panel[cite: 25].

### 3. El Temporizador (*Timer*)
El temporizador se inicia automáticamente una vez que la terminal se ha cargado[cite: 25]. Mantiene el registro del tiempo restante para completar la actividad y realiza una cuenta regresiva hasta llegar a `00:00:00`[cite: 25]. Cuando el tiempo expira, la terminal temporal y todos sus recursos asociados se eliminan automáticamente[cite: 25].

Tendrás tiempo suficiente para completar cada práctica; sin embargo, se aconseja mantener el enfoque en las tareas para administrar el tiempo eficientemente[cite: 25].

### 4. Abrir la Consola de Linux (*Open Linux Console*)
Al hacer clic en el botón **Open Linux Console**, la terminal se abrirá en una ventana nueva del navegador[cite: 25]. Esta opción es ideal si prefieres trabajar con una vista de pantalla completa de la terminal[cite: 25]. Puedes cerrar esta ventana en cualquier momento sin que esto finalice el laboratorio, pudiendo continuar tu trabajo en la pestaña original[cite: 25].

### 5. Verificación de Progreso (*Check Progress*)
Para validar tu avance, haz clic en **Check my progress** al finalizar cada tarea[cite: 25]. Si aún no has completado una tarea de manera correcta, recibirás pistas e indicaciones sobre los pasos faltantes para lograrlo[cite: 25]. Puedes hacer clic en este botón siempre que desees verificar el estado de una tarea[cite: 25].

### 6. Permisos de Copiar y Pegar
La primera vez que intentes utilizar accesos directos por teclado para copiar o pegar (como `CTRL + C`), aparecerá una ventana emergente solicitando autorización para acceder al portapapeles de tu dispositivo (*"cloudskillsboost.google quiere ver el texto e imágenes copiados en el portapapeles"*)[cite: 25]. Haz clic en **Permitir (*Allow*)** para habilitar el uso de estos atajos[cite: 25]. Si decides no otorgar acceso, aún podrás completar la actividad ingresando el texto manualmente[cite: 25].

### 7. Bloques de Código e Inserción en la Terminal
Los pasos de las instrucciones suelen incluir bloques de código[cite: 25]. Puedes hacer clic en el botón de copiar del bloque e insertarlo en la terminal[cite: 25]:
*   Para pegar texto o código en la terminal, haz clic en cualquier parte interna de la consola para activarla[cite: 25]. La terminal se encuentra activa cuando el cursor cambia de un contorno vacío estático a un bloque sólido parpadeante[cite: 25].
*   Una vez activa, utiliza la combinación de teclas **`Ctrl + V`** para pegar el contenido copiado en la ubicación exacta del cursor parpadeante[cite: 25].

### 8. Desplazamiento (*Scrolling*) y Finalización (*End Lab*)
*   **Desplazamiento:** Para desplazarte verticalmente dentro de la terminal, utiliza la rueda de desplazamiento del ratón (*scroll*) o el panel táctil (*touchpad*) de tu computadora[cite: 25].
*   **Finalizar el Laboratorio:** Haz clic en **End Lab** únicamente cuando hayas terminado todas las tareas[cite: 25]. No hagas clic en este botón antes de tiempo, ya que perderás el acceso al entorno y al trabajo realizado durante la sesión[cite: 25].

---

## Consejos Útiles de Navegación y Atajos de Teclado en la Terminal

A continuación se presenta un resumen de los atajos de teclado y comandos de navegación indispensables para operar en la terminal de Linux[cite: 25]. Para utilizarlos, asegúrate de que el cursor esté posicionado dentro de la ventana de la terminal[cite: 25]:

| Atajo / Comando | Función Operativa |
| :--- | :--- |
| **`CTRL + C`** | Interrumpe y finaliza un comando que se encuentra en ejecución[cite: 25]. (En el área de instrucciones de Qwiklabs copia texto, pero dentro de la terminal detiene el comando activo o muestra `^C` en el cursor)[cite: 25]. |
| **`CTRL + V`** | Pega texto dentro de la terminal[cite: 25]. |
| **`clear`** o **`CTRL + L`** | Limpia la pantalla de la terminal[cite: 25]. |
| **`CTRL + A`** | Mueve el cursor al inicio de la línea de comandos[cite: 25]. |
| **`CTRL + E`** | Mueve el cursor al final de la línea de comandos[cite: 25]. |
| **Flecha izquierda** | Desplaza el cursor una posición hacia la izquierda dentro del comando[cite: 25]. |
| **Flecha derecha** | Desplaza el cursor una posición hacia la derecha dentro del comando[cite: 25]. |
| **Flecha arriba** | Muestra el último comando ingresado en el historial de la consola (puede presionarse varias veces para retroceder en el historial)[cite: 25]. |
| **Flecha abajo** | Avanza hacia el siguiente comando en el historial (tras haber usado la flecha arriba)[cite: 25]. |
| **Tecla Tab** | Proporciona sugerencias de autocompletado automático para el texto o comando ingresado[cite: 25]. |

---

## Puntos Clave (Key Takeaways)

*   **Entorno Práctico Qwiklabs:** Proporciona terminales temporales de Linux con tiempo limitado para practicar comandos reales en un entorno controlado[cite: 25].
*   **Interacción de Consola:** Se puede abrir en pantalla completa con el botón *Open Linux Console* y verificar cada tarea de forma interactiva con *Check my progress*[cite: 25].
*   **Portapapeles y Atajos:** Otorgar permisos de portapapeles permite usar `CTRL + V` para pegar fragmentos de código cuando el cursor esté parpadeando como bloque sólido dentro de la terminal[cite: 25].
*   **Eficacia en la Terminal:** Comandos como `clear` (`CTRL + L`), interrupciones con `CTRL + C`, desplazamientos con `CTRL + A`/`CTRL + E`, el historial con las flechas de dirección y el autocompletado con `Tab` optimizan significativamente la productividad en línea de comandos[cite: 25].