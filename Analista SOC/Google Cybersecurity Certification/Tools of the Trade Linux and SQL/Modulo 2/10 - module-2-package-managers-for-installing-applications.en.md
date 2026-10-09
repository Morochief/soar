# Reading: Package managers for installing applications

En lecciones anteriores, aprendiste sobre las distribuciones de Linux y cómo diferentes distribuciones derivan de distintas fuentes, como las distribuciones basadas en Debian o Red Hat Enterprise Linux [cite: 26]. También se te introdujo al concepto de los gestores de paquetes (*package managers*) y aprendiste que las aplicaciones en Linux comúnmente se distribuyen a través de ellos [cite: 26]. En esta lectura, aplicarás este conocimiento para profundizar en el funcionamiento de los gestores de paquetes [cite: 26].

---

## Introducción del Equipo de Ciberseguridad de Google

Para un analista de ciberseguridad, comprender cómo se instalan, actualizan y remueven las aplicaciones en Linux es fundamental [cite: 26]. Las herramientas de seguridad y el software del sistema dependen de una correcta gestión de paquetes para garantizar que los entornos contengan las últimas correcciones de errores (*bug fixes*) y parches de seguridad (*security patches*), elementos clave para mantener la postura defensiva de una organización [cite: 26].

---

## Desarrollo Temático: Administración de Software en Linux

### Introducción a los Gestores de Paquetes
Un **paquete (*package*)** es una pieza de software que se puede combinar con otros paquetes para formar una aplicación completa [cite: 26]. Algunos paquetes son lo suficientemente grandes como para constituir aplicaciones por sí mismos [cite: 26].

Los paquetes contienen todos los archivos necesarios para la instalación de una aplicación [cite: 26]. Entre estos archivos se incluyen las **dependencias (*dependencies*)**, que son archivos complementarios indispensables para ejecutar una aplicación de forma correcta [cite: 26].

Un **gestor de paquetes (*package manager*)** es una herramienta que ayuda a los usuarios a instalar, administrar, actualizar y eliminar paquetes o aplicaciones, resolviendo automáticamente los problemas de dependencias entre componentes [cite: 26]. Linux utiliza múltiples gestores de paquetes según la familia de distribución [cite: 26].

> [!IMPORTANT]
> **Seguridad y Actualizaciones:** Es fundamental utilizar siempre la versión más reciente de un paquete cuando sea posible [cite: 26]. Las versiones más recientes incluyen los parches de seguridad y correcciones de errores más actualizados, lo que ayuda a mantener el sistema protegido contra vulnerabilidades conocidas [cite: 26].

---

### Tipos de Gestores de Paquetes
Muchas distribuciones de Linux comúnmente utilizadas derivan de una misma distribución madre [cite: 26]. Por ejemplo, **KALI LINUX™**, **Ubuntu** y **Parrot** provienen de Debian, mientras que **CentOS** deriva de Red Hat [cite: 26].

Este conocimiento es muy útil al instalar aplicaciones, ya que ciertos gestores de paquetes funcionan exclusivamente con familias de distribuciones específicas [cite: 26]:
*   **Gestor de paquetes de Red Hat (*Red Hat Package Manager - RPM*):** Se utiliza en distribuciones de Linux derivadas de Red Hat y maneja archivos con la extensión `.rpm` (por ejemplo, `Paquete-Version-Lanzamiento_Arquitectura.rpm`) [cite: 26].
*   **dpkg:** Se utiliza en distribuciones derivadas de Debian (como Kali, Ubuntu y Parrot) y maneja archivos con la extensión `.deb` (por ejemplo, `Paquete_Version-Lanzamiento_Arquitectura.deb`) [cite: 26].

---

### Herramientas de Gestión de Paquetes (*Package Management Tools*)
Además de los gestores de paquetes de bajo nivel como RPM y `dpkg`, existen **herramientas de gestión de paquetes** de alto nivel que permiten interactuar fácilmente con los paquetes a través de la consola (*shell*) [cite: 26]. Estas herramientas se utilizan frecuentemente porque permiten realizar tareas básicas, como la instalación de un nuevo paquete desde repositorios remotos, de forma mucho más ágil y automatizada [cite: 26].

Dos herramientas destacadas en la industria son [cite: 26]:

#### 1. Herramienta de Paquetes Avanzada (*Advanced Package Tool - APT*)
**APT** es la herramienta utilizada en distribuciones derivadas de Debian (como Ubuntu, Kali Linux y Parrot) [cite: 26]. Se ejecuta desde la interfaz de línea de comandos (CLI) para gestionar, buscar, actualizar e instalar paquetes y sus dependencias de forma automatizada [cite: 26].

#### 2. Yellowdog Updater Modified (*YUM*)
**YUM** es la herramienta utilizada en distribuciones derivadas de Red Hat (como CentOS o RHEL) [cite: 26]. Se ejecuta desde la línea de comandos para administrar, buscar e instalar paquetes funcionando directamente con archivos `.rpm` [cite: 26].

---

## Puntos Clave (Key Takeaways)

*   **Definición de Paquete:** Un paquete es un conjunto de archivos de software que incluye las dependencias necesarias para la correcta instalación y funcionamiento de una aplicación [cite: 26].
*   **Gestión y Parches de Seguridad:** Los gestores de paquetes administran el ciclo de vida del software; mantener las aplicaciones actualizadas a la versión más reciente garantiza la aplicación de parches de seguridad esenciales [cite: 26].
*   **Ecosistema Debian:** Las distribuciones derivadas de Debian (Kali, Ubuntu, Parrot) emplean gestores como `dpkg` (archivos `.deb`) y herramientas de alto nivel como **APT** (*Advanced Package Tool*) [cite: 26].
*   **Ecosistema Red Hat:** Las distribuciones derivadas de Red Hat (RHEL, CentOS, AlmaLinux) emplean el gestor **RPM** (archivos `.rpm`) y herramientas como **YUM** (*Yellowdog Updater Modified*) [cite: 26].
