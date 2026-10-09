# Guía de Migración y Despliegue: Security Onion 3 (Distribuido + Endpoints)

**Objetivo:** Proporcionar a Cómputo/Infraestructura los requerimientos para desplegar un clúster de Security Onion 3 **Distribuido** de alta capacidad, preparado para recibir telemetría tanto de Red (SPAN) como de miles de Endpoints (Elastic Agent).

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
> *Nota: Al migrar hacia una arquitectura distribuida y soportar Endpoints, Infraestructura tendrá que provisionar el hardware adicional para los nuevos Nodos (Search Nodes, Sensores).*

---

## 2. Requerimientos de Hardware (Nodos Separados)
Para soportar endpoints, se recomienda la adición de un nodo "Fleet" (para gestionar agentes) o "Receiver" (para ingestar logs masivos), además de escalar fuertemente los Search Nodes.

| Rol del Nodo | CPU (Mínimo) | RAM (Mínimo) | Almacenamiento | Función Principal |
| :--- | :--- | :--- | :--- | :--- |
| **Manager** | 4 Cores | 16 GB | 200 GB | Consola SOC, Base de Datos, Orquestación. |
| **Search Node** | **8 a 16 Cores** | **64 GB a 128 GB+** | **1 TB a 5 TB (SSD/NVMe)** | Clúster de Elasticsearch (Altísimo consumo de IOPS y RAM por los endpoints). |
| **Sensor (Red)** | 4 Cores | 12 GB | 200 GB (NIC dedicada) | Analizador de tráfico SPAN/Mirror. |
| **Fleet Node (Endpoints)** | 4 Cores | 4 GB a 8 GB | 200 GB | Servidor frontal que gestiona las políticas de los Elastic Agents y recibe sus logs. |

---

## 3. Reglas de Firewall Perimetral e Interno

### 3.1. Tráfico Saliente a Internet (TCP/443)
Todos los nodos necesitan salida a internet hacia Github, repositorios de Elastic, Emerging Threats y Security Onion Solutions (`raw.githubusercontent.com`, `ghcr.io`, `geoip.elastic.co`, etc.).

### 3.2. Tráfico Interno (Nodos y Endpoints)
El despliegue de agentes modifica drásticamente las rutas internas. Se deben aplicar estas ACLs:

| Origen | Destino | Puertos TCP Permitidos | Uso |
| :--- | :--- | :--- | :--- |
| **Todos los Nodos (Grid)** | **Manager** | `443`, `4505`, `4506`, `5000`, `5055`, `8086`, `8220`, `8443` | Orquestación, Registro Docker, Actualizaciones |
| **Search Nodes** | **Manager** | `9696` | Logstash a Redis central |
| **Nodos Elastic** | **Nodos Elastic** | `9200`, `9300` | Comunicación interna del clúster de Elasticsearch |
| **Fleet Node** | **Manager / Search** | `5056`, `9200` | Envío de logs desde el Fleet Node hacia el clúster de Elasticsearch. |
| **Todos los Endpoints de la Empresa (LAN/VPN)** | **Fleet Node** (o Manager si no hay Fleet) | `5055`, `8220`, `8443` | Comunicación directa de las PCs de los usuarios hacia el servidor de agentes para descargar políticas y enviar logs. |

> [!CAUTION]
> **Riesgo Operativo:** Es fundamental que el puerto `8220` (Fleet) esté alcanzable por **toda** la red corporativa donde se instalarán los agentes, pero protegido de accesos externos desde Internet.

---

## 4. Secuencia de Instalación
La instalación debe ser estrictamente secuencial:

1. **Instalar el Manager** (`sudo so-setup` -> Manager). Anotar la contraseña secreta de la grilla.
2. **Instalar el/los Search Node(s)** uniéndolos a la IP del Manager.
3. **Instalar el Sensor de Red** conectando el puerto de Sniffing.
4. **Instalar el Fleet Node** (opcional, para alivianar al Manager del tráfico de endpoints).
5. **Despliegue de Agentes:** El equipo SOC generará los instaladores para que Infraestructura los distribuya vía GPO o SCCM hacia los endpoints.
