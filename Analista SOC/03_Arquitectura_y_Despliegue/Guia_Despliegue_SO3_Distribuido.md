# Guía de Migración y Despliegue: Security Onion 3 (Arquitectura Distribuida)

**Objetivo:** Proporcionar a Cómputo/Infraestructura los requerimientos para desplegar un clúster de Security Onion 3 en formato **Distribuido**, separando los roles de administración, indexación y recolección de tráfico en múltiples Máquinas Virtuales/Servidores.

---

## 1. Estrategia de Migración (EoL 2.4)
> [!WARNING] 
> **Fin de Ciclo de Vida (EoL):** Security Onion 2.4 dejará de tener soporte oficial el **1 de Octubre de 2026**.

> [!TIP]
> **¡BUENAS NOTICIAS PARA INFRAESTRUCTURA!** 
> Dado que el servidor actual 2.4 ya corre sobre **Oracle Linux 9**, **NO es obligatorio formatear ni provisionar nuevo hardware**. La migración se puede realizar en el mismo equipo (In-Place Upgrade) ejecutando los scripts nativos de SO:
> 1. Asegurar backup válido en `/nsm/backup`
> 2. `sudo soup` *(Para llegar a la última versión 2.4.211)*
> 3. `sudo soupto3` *(Descarga el actualizador a la versión 3)*
> 4. `sudo soup` *(Ejecuta la migración a la v3)*
> 
> *Nota: Los requerimientos de hardware a continuación solo aplican en caso de que Cómputo decida, de forma opcional, aprovechar la ventana de mantenimiento para separar la arquitectura (pasar de Standalone a Distribuido).*

---

## 2. Requerimientos de Hardware (Nodos Separados)
En una arquitectura distribuida básica, se recomienda desplegar al menos un *Manager* (Administración y BD), un *Search Node* (Indexador) y un *Sensor* (Analizador de tráfico).

| Rol del Nodo | CPU (Mínimo) | RAM (Mínimo) | Almacenamiento | Tarjetas de Red (NICs) | Función Principal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Manager** | 4 Cores | 16 GB | 200 GB | 1 (Management) | Consola Central (SOC), orquestación de la grilla (Salt), base de datos principal. |
| **Search Node** | 4 Cores | 16 GB | 200 GB+ | 1 (Management) | Clusterización de Elasticsearch para almacenar y buscar en petabytes de logs (PCAP y alertas). |
| **Sensor** | 4 Cores | 12 GB | 200 GB | 2 (Mgmt + Sniffing) | Recibe el tráfico SPAN del switch y ejecuta Suricata/Zeek/Strelka para generar alertas. |

---

## 3. Reglas de Firewall Perimetral e Interno

Al ser una arquitectura distribuida, el tráfico entre los componentes del clúster (Grid) es vital. Se requieren habilitar tanto puertos de internet como puertos de la red LAN/VLAN.

### 3.1. Tráfico Saliente a Internet (TCP/443)
Todos los nodos (o al menos el Manager si actúa como proxy) necesitan salida a internet hacia:
- `raw.githubusercontent.com`, `ghcr.io`, `pkg-containers.githubusercontent.com`, `github.com`, `objects.githubusercontent.com`
- `sigs.securityonion.net`, `repo.securityonion.net`, `repo-alt.securityonion.net`
- `rules.emergingthreatspro.com`, `rules.emergingthreats.net`, `www.snort.org`
- `geoip.elastic.co`, `storage.googleapis.com`

### 3.2. Tráfico Interno (Node-to-Node)
El Firewall interno (o las ACLs de los switches/hypervisor) debe permitir el siguiente tráfico **estricto** entre las IPs de Management de cada nodo:

| Origen | Destino | Puertos TCP Permitidos | Uso |
| :--- | :--- | :--- | :--- |
| **Sensores / Search Nodes** | **Manager** | `443`, `4505`, `4506`, `5000`, `5055`, `8086`, `8220`, `8443` | Orquestación Salt, Registro Docker, Actualizaciones, Métricas |
| **Search Nodes** | **Manager** | `9696` | Logstash a Redis central |
| **Nodos Elastic** *(Search + Manager)* | **Nodos Elastic** *(Search + Manager)* | `9200`, `9300` | Comunicación de clúster de Elasticsearch (Node-to-node) y Logstash |

> [!NOTE]
> **Tráfico Entrante para Analistas:** El departamento de TI solo necesita exponer el **TCP/443 (HTTPS)** del nodo **Manager** hacia la red de los analistas SOC. No es necesario exponer la interfaz web de los Sensores o Search Nodes.

---

## 4. Secuencia de Instalación
En un entorno distribuido, el orden de despliegue es **crítico**. Cómputo debe seguir esta secuencia:

1. **Instalar el Manager:**
   - Montar la ISO, configurar red con IP Fija.
   - Correr `sudo so-setup` y elegir tipo de despliegue **Manager**.
   - Crear las credenciales de administrador y anotar la clave secreta que entregará SaltStack al final.

2. **Instalar el/los Search Node(s):**
   - Montar la ISO, asignar red.
   - Correr `sudo so-setup` y elegir tipo de despliegue **Search Node**.
   - El sistema pedirá la IP del Manager y la contraseña secreta para unirse a la grilla (Grid).

3. **Instalar el/los Sensor(es):**
   - Montar la ISO, asignar red (Mgmt) y conectar el puerto SPAN a la interfaz de monitoreo sin IP.
   - Correr `sudo so-setup` y elegir tipo de despliegue **Sensor**.
   - El sistema pedirá la IP del Manager y la contraseña secreta para unirse a la grilla.

---

## 5. Referencias Oficiales
- [Arquitectura Distribuida](https://docs.securityonion.net/en/2.4/architecture.html)
- [Guía de Hardware](https://docs.securityonion.net/en/2.4/hardware.html)
- [Requerimientos de Puertos y Firewall Interno](https://docs.securityonion.net/en/2.4/firewall.html)
