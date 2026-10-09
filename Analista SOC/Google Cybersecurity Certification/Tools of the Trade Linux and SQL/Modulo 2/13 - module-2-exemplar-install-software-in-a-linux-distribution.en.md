# Exemplar: Install software in a Linux distribution

En esta actividad práctica de laboratorio, utilizaste la Herramienta de Paquetes Avanzada (**APT** - *Advanced Package Tool*) y el comando `sudo` para instalar y desinstalar aplicaciones dentro de una consola Bash de Linux [cite: 24].

Si bien la instalación de aplicaciones en Linux puede parecer una tarea compleja, el gestor de paquetes APT simplifica la mayor parte de este proceso, permitiéndote administrar aplicaciones de manera rápida, confiable y segura en entornos Linux [cite: 24].

Para este ejercicio práctico se utilizaron como ejemplo **Suricata** y **tcpdump**, dos aplicaciones fundamentales en seguridad de redes dedicadas a la captura y análisis de tráfico [cite: 24]. La máquina virtual accedida en este laboratorio ejecuta una distribución de Linux basada en **Debian**, la cual trabaja de forma nativa con el gestor APT [cite: 24]. El uso de máquinas virtuales evita daños al sistema operativo anfitrión en caso de un uso inadecuado de herramientas y brinda la capacidad de revertir cambios a un estado previo [cite: 24].

---

## Introducción del Equipo de Ciberseguridad de Google

Como analista de ciberseguridad, la gestión de paquetes e instalación de software en sistemas Linux es una habilidad operativa que aplicarás con alta frecuencia [cite: 24]. Saber instalar, verificar y remover herramientas de análisis de red es un requisito indispensable para configurar puestos de trabajo, servidores de monitoreo y entornos de análisis de incidentes [cite: 24].

---

## Desarrollo Temático: Instalación y Gestión de Software en Linux (Guía de Ejercicio Práctico)

### Escenario Operativo
Tu rol como analista de seguridad requiere que tengas instaladas en tu sistema las aplicaciones de seguridad de red **Suricata** (un sistema de detección de intrusiones o *IDS*) y **tcpdump** (una herramienta de captura de paquetes por línea de comandos) [cite: 24].

En este escenario, debes instalar, desinstalar y reinstalar estas aplicaciones desde la consola Bash de Linux, confirmando en cada paso su correcta instalación [cite: 24].

---

### Tarea 1: Verificar que APT está Instalado
Primero, debes comprobar que la herramienta APT está disponible en el sistema [cite: 24]. La forma más simple de verificarlo es ejecutar el comando `apt` en la consola Bash [cite: 24]. La consola se identifica por el símbolo de dólar (`$`) seguido del cursor de entrada [cite: 24].

*   **Comando a ejecutar:**
    ```bash
    apt
    ```

*   **Resultado esperado:**
    Cuando APT está instalado, muestra información básica de uso, la versión del sistema y una descripción del comando [cite: 24]:
    ```text
    apt 1.8.2.3 (amd64)
    Usage: apt [options] command

    apt is a commandline package manager and provides commands for
    searching and managing as well as querying information about packages.
    It provides the same functionality as the specialized APT tools,
    like apt-get and apt-cache, but enables options more suitable for
    interactive use by default.
    ...
    ```

> [!NOTE]
> APT se encuentra preinstalado por defecto en sistemas derivados de Debian [cite: 24]. En otras distribuciones (como Red Hat o CentOS), se emplean gestores distintos como `YUM` o `DNF` [cite: 24].

---

### Tarea 2: Instalar y Desinstalar la Aplicación Suricata

#### 1. Instalar Suricata usando APT
Ejecuta el siguiente comando para iniciar la instalación [cite: 24]:
```bash
sudo apt install suricata
```

> [!IMPORTANT]
> Los comandos `apt install` y `apt remove` deben antecederse con `sudo` (*superuser do*), ya que se requieren privilegios elevados de administrador para instalar o remover software en sistemas Linux [cite: 24].

Al instalar una aplicación con APT, el sistema muestra el detalle de los componentes e instala automáticamente las **dependencias** (software adicional necesario para el funcionamiento de la aplicación principal) [cite: 24]. Cuando la consola solicite confirmación para continuar, presiona la tecla `ENTER` para aceptar la respuesta predeterminada (`Yes`) [cite: 24].

#### 2. Verificar la Instalación de Suricata
Ejecuta el comando principal de la aplicación para confirmar que responde adecuadamente [cite: 24]:
```bash
suricata
```
Si la instalación fue exitosa, el sistema desplegará la versión instalada (`Suricata 4.1.2`) junto con las opciones de uso de la herramienta [cite: 24].

#### 3. Desinstalar la Aplicación Suricata
Para remover la aplicación del sistema, ejecuta [cite: 24]:
```bash
sudo apt remove suricata
```
Presiona `ENTER` para confirmar cuando el sistema solicite autorización [cite: 24].

#### 4. Confirmar la Desinstalación
Ejecuta nuevamente el comando para comprobar que ya no se encuentra disponible [cite: 24]:
```bash
suricata
```
*   **Resultado esperado (Error):**
    ```text
    -bash: /usr/bin/suricata: No such file or directory
    ```
    Este mensaje confirma que el ejecutable de Suricata ha sido removido del sistema [cite: 24].

---

### Tarea 3: Instalar la Aplicación tcpdump
`tcpdump` es una herramienta de línea de comandos esencial para capturar e inspeccionar tráfico de red en tiempo real [cite: 24].

*   **Comando para instalar tcpdump:**
    ```bash
    sudo apt install tcpdump
    ```

---

### Tarea 4: Listar las Aplicaciones Instaladas
Es importante que un analista sepa validar qué programas y versiones específicas están presentes en el sistema [cite: 24].

1.  **Listar todos los paquetes instalados:**
    ```bash
    apt list --installed
    ```
2.  **Verificar el resultado:**
    La consola generará una lista extensa de software [cite: 24]. Al buscar dentro del listado, observarás la presencia de `tcpdump` [cite: 24]:
    ```text
    tcpdump/oldstable,now 4.9.3-1~deb10u2 amd64 [installed]
    ```
    Suricata no aparecerá en la lista porque fue desinstalada previamente en la Tarea 2 [cite: 24].

---

### Tarea 5: Reinstalar la Aplicación Suricata
En esta fase final, reinstalarás Suricata para mantener ambas herramientas de seguridad operativas en la máquina virtual [cite: 24].

1.  **Reinstalar Suricata:**
    ```bash
    sudo apt install suricata
    ```
2.  **Listar aplicaciones instaladas:**
    ```bash
    apt list --installed
    ```
3.  **Confirmación final:**
    La salida de la lista debe incluir ahora ambas aplicaciones [cite: 24]:
    ```text
    suricata/oldstable,now 1:4.1.2-2+deb10u1 amd64 [installed]
    tcpdump/oldstable,now 4.9.3-1~deb10u2 amd64 [installed]
    ```

---

## Puntos Clave (Key Takeaways)

*   **Gestión Eficiente con APT:** El gestor de paquetes APT automatiza la resolución e instalación de dependencias en distribuciones Linux basadas en Debian [cite: 24].
*   **Privilegios Elevados (`sudo`):** Las tareas administrativas de instalación y desinstalación de paquetes exigen privilegios de superusuario (`sudo`) [cite: 24].
*   **Verificación de Estado:** Es crucial validar la presencia y versión del software utilizando comandos directos o `apt list --installed` [cite: 24].
*   **Herramientas Clave del SOC:** Suricata (detección de intrusiones) y `tcpdump` (captura de paquetes) son aplicaciones de seguridad imprescindibles en el arsenal de un analista de ciberseguridad [cite: 24].
