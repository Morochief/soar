# Guía de Instalación y Puesta a Punto: Security Onion Desktop 3.3.0 en VirtualBox

Esta guía documenta el procedimiento completo, técnico y validado en laboratorio para el despliegue de **Security Onion Desktop 3.3.0** como estación de trabajo independiente para el analista de SOC (Sandbox / Forensic Workstation), así como la resolución de dependencias de red y compilación de **VirtualBox Guest Additions** sobre el kernel **Oracle Linux 9 (UEK)**.

---

## 1. Arquitectura y Dimensionamiento de la Máquina Virtual

A diferencia de un nodo Sensor o Manager de Security Onion (que consumen entre 16 GB y 24 GB de RAM), el rol **Desktop** es un entorno liviano orientado al analista, diseñado para inspección forense local (PCAP, Wireshark, NetworkMiner, CyberChef) y navegación hacia el Grid.

### Especificaciones Recomendadas en VirtualBox
* **Tipo**: `Linux`
* **Versión**: `Oracle Linux 9.x (64-bit)`
* **Procesadores (vCPU)**: `2 CPUs` (o 4 si se dispone de recursos).
* **Memoria RAM**: `4096 MB` (4 GB) mínimo recomendado; `6144 MB` (6 GB) óptimo.
* **Disco Virtual (VDI)**: `50 GB` a `60 GB` (Almacenamiento dinámico).
* **Adaptador de Red Inicial**: `NAT` (para evitar restricciones de DHCP / 802.1X en redes corporativas durante el setup).

---

## 2. Proceso de Despliegue del Sistema Operativo

1. Iniciar la máquina virtual con la imagen ISO montada (`securityonion-3.3.0-*.iso`).
2. Completar la instalación del sistema operativo base (Oracle Linux 9).
3. En el primer reinicio, iniciar sesión en la consola TTY:
   * **Usuario**: `kevinmoraes` (o el usuario configurado).
   * **Contraseña**: Credencial administrativa definida en la instalación.

---

## 3. Instalación del Entorno Gráfico (Security Onion Desktop)

Security Onion 3.x almacena los scripts de aprovisionamiento en `/root/SecurityOnion/`.

### 3.1. Asegurar Conectividad de Red
Verificar que la interfaz tenga direccionamiento IP asignado:
```bash
ip a
```
*Si la interfaz no tiene IP asignada (por ejemplo en entornos NAT de VirtualBox):*
```bash
sudo nmcli device connect enp0s3
```

### 3.2. Ejecución del Instalador de Escritorio
Lanzar el script nativo de instalación de la interfaz de analista:
```bash
sudo /root/SecurityOnion/so-desktop-install
```

### 3.3. Opciones en el Asistente Interactivo
1. **Join Grid**:
   * Pregunta: `Would you like to join this desktop to an existing grid?`
   * Selección: **`<No>`** (Para mantener la estación independiente sin requerir Salt / certificados del Manager).
2. **Interfaz Gráfica al Arranque**:
   * Pregunta: `Would you still like to have the graphical interface loaded at boot?`
   * Selección: **`<Yes>`** (Habilita el `graphical.target` y el inicio de sesión XFCE).

### 3.4. Reinicio de Confirmación
Al finalizar el script con el mensaje `Desktop Install Complete!`:
```bash
sudo reboot
```

---

## 4. Instalación de VirtualBox Guest Additions (Oracle Linux 9 UEK)

Por defecto, Security Onion aísla el repositorio base de Oracle Linux dejando únicamente sus repositorios internos (`securityonionkernel.repo` y `securityonion.repo`). Para compilar los módulos del kernel de VirtualBox sobre el **Unbreakable Enterprise Kernel (UEK)**, se deben restaurar los repositorios oficiales de Oracle e instalar los headers de compilación.

### 4.1. Insertar el Medio de Guest Additions
En la ventana de VirtualBox de Windows:
* Ir a: **Dispositivos** > **Insertar imagen de CD de las «Guest Additions»...**

### 4.2. Habilitar Repositorios Oficiales de Oracle Linux 9
Abrir una terminal en el Desktop y ejecutar:
```bash
sudo dnf install -y oraclelinux-release-el9
```

### 4.3. Instalar Dependencias de Compilación y Headers del Kernel UEK
Instalar las herramientas de desarrollo esenciales y las cabeceras exactas de la versión del kernel en ejecución:
```bash
sudo dnf install -y gcc make bzip2 perl kernel-uek-devel-$(uname -r)
```

### 4.4. Compilar los Módulos de VirtualBox
Ejecutar la compilación mediante el servicio de VirtualBox:
```bash
sudo /sbin/rcvboxadd setup
```
*(O de forma equivalente ejecutando el script directamente desde el CD montado:)*
```bash
cd /run/media/$USER/VBox_GAs_*
sudo ./VBoxLinuxAdditions.run
```
Verificar que el resultado indique:
```text
Building the VirtualBox Guest Additions kernel modules... [ OK ]
```

### 4.5. Reinicio Final
Aplicar los módulos del kernel:
```bash
sudo reboot
```

---

## 5. Ajustes Post-Instalación en VirtualBox (Host Windows)

Una vez reiniciada la máquina con las Guest Additions activas:
1. **Portapapeles Compartido y Arrastrar y Soltar**:
   * Menú **Dispositivos** > **Portapapeles compartido** > Seleccionar **Bidireccional**.
   * Menú **Dispositivos** > **Arrastrar y soltar** > Seleccionar **Bidireccional**.
2. **Pantalla Completa**:
   * Presionar `Host + F` (por defecto `Ctrl Derecho + F`) o maximizar la ventana para ajuste automático de resolución (DPI adaptativo).

---

## 6. Resumen de Comandos Útiles

| Propósito | Comando |
| :--- | :--- |
| **Verificar Direccionamiento IP** | `ip a` |
| **Instalar Entorno Desktop** | `sudo /root/SecurityOnion/so-desktop-install` |
| **Restaurar Repositorios Oracle Linux** | `sudo dnf install -y oraclelinux-release-el9` |
| **Instalar Headers Kernel UEK** | `sudo dnf install -y kernel-uek-devel-$(uname -r)` |
| **Compilar Módulos Guest Additions** | `sudo /sbin/rcvboxadd setup` |
| **Reiniciar Sistema** | `sudo reboot` |
