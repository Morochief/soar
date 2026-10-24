# 🏗️ GUÍA DE ARQUITECTURA DE SECURITY ONION 3.0 & DIMENSIONAMIENTO DE RECURSOS

> **CLASIFICACIÓN:** USO INTERNO SOC TECHNOMA — BASE DE CONOCIMIENTO  
> **FECHA DE ACTUALIZACIÓN:** 22 de Octubre de 2026  
> **APLICABLE A:** Nodo `soc-onion` (172.17.10.25) & Diseño de Red SO3  

---

## 📌 1. Resumen Ejecutivo del Comportamiento de Hardware

En el nodo central de Security Onion (`soc-onion`), la visualización habitual de un consumo de **Memoria RAM entre 85% y 92%** es un comportamiento **esperado y saludable** bajo la arquitectura **Standalone**.

Esto se debe a la coexistencia simultánea de:
1. **JVM Heap de Elasticsearch:** Reserva fija del 50% de la RAM del host (~14 GB).
2. **JVM Heap de Logstash:** Reserva fija (~4 GB) para los pipelines de entrada y salida de eventos.
3. **Firmas en Memoria de Suricata:** Más de **52.500 reglas IDS activas** cargadas en memoria viva (~4 GB).
4. **Buffer/Cache de Linux (`buff/cache`):** El kernel utiliza toda la memoria restante para optimizar la lectura/escritura de índices de disco de Elasticsearch.

---

## 📐 2. Modelos de Arquitectura en Security Onion 3.0

Security Onion 3.0 clasifica sus despliegues según la distribución de carga y los roles de cada nodo:

### 2.1. Standalone (Arquitectura Actual de Technoma)
* **Descripción:** Todos los componentes se ejecutan en un único host físico o máquina virtual.
* **Flujo de Ingesta:**
  $$\text{Suricata / Zeek / Strelka} \longrightarrow \text{Elastic Agent} \longrightarrow \text{Logstash (Ingreso)} \longrightarrow \text{Redis (Queue)} \longrightarrow \text{Logstash (Parser)} \longrightarrow \text{Elasticsearch}$$
* **Ventajas:** Despliegue simple, mantenimiento centralizado, sin dependencias de red entre nodos.
* **Desventajas:** Cuello de botella en contención de RAM y CPU; no escala para altos volúmenes de tráfico (> 1 Gbps sostenido).
* **Requisito mínimo recomendado:** 32 GB RAM / 8+ CPU Cores / Almacenamiento SSD/NVMe.

```
+---------------------------------------------------------------------------------+
|                               NODO STANDALONE                                   |
|                                                                                 |
|  [Suricata / Zeek] ---> [Elastic Agent] ---> [Logstash] ---> [Redis Queue]      |
|                                                                    |            |
|                                                              [Logstash]         |
|                                                                    |            |
|  [Kibana / SOC UI] <--------------------------------------- [Elasticsearch]     |
+---------------------------------------------------------------------------------+
```

---

### 2.2. Distributed (Arquitectura de Producción Recomendada)
* **Separación de Funciones en 3 Roles:**
  1. **Manager Node:** Ejecuta la interfaz gráfica (SOC UI, Kibana), ElastAlert y la cola central de Redis. Coordina las búsquedas.
  2. **Sensor Nodes (1 o más):** Dedicados exclusivamente a capturar tráfico en puertos TAP/SPAN (Suricata, Zeek, captura PCAP). Envían los logs al Manager vía Elastic Agent.
  3. **Search Nodes (1 o más):** Nodos pesados de datos. Consumen eventos de la cola de Redis del Manager, los parsean vía Logstash y los indexan en su propio cluster de Elasticsearch.
* **Escalabilidad:** Permite agregar Search Nodes a medida que aumenta la retención de días, o Sensor Nodes por cada sede física o VLAN monitoreada.

---

### 2.3. Distributed + Receiver Nodes (Alta Disponibilidad e Ingesta Masiva)
* **Propósito:** Evitar que el Manager Node se sature cuando existen miles de Elastic Agents o decenas de integraciones Syslog/API (Sophos, Fortinet, Windows Event Logs).
* **Mecanismo:** 
  * Los nodos **Receiver** corren instancias de **Logstash + Redis** en modo Activo-Activo.
  * Si el Manager se apaga o entra en mantenimiento, los agentes y sensores desvían su tráfico a los Receivers sin perder un solo evento.
  * Los Search Nodes drenan tanto el Redis del Manager como el Redis de los Receivers.

---

### 2.4. IDH (Intrusion Detection Honeypot)
* **Propósito:** Nodo ligero señuelo colocado en segmentos internos o DMZ.
* **Función:** Emula servicios vulnerables comunes (HTTP, FTP, SSH, MySQL). Cualquier intento de autenticación o escaneo contra un IDH dispara una alerta inmediata de alta severidad hacia el Manager.

---

### 2.5. Heavy Nodes (Desaconsejado para Producción General)
* **Descripción:** Nodos que actúan como sensores y al mismo tiempo almacenan sus propios datos localmente en un Elasticsearch independiente, consultados vía *Cross-Cluster Search*.
* **Limitación:** Tienen un alto consumo de hardware y bajo rendimiento general; la documentación oficial de Security Onion recomienda evitarlos salvo escenarios aislados sin enlace WAN hacia el cluster central.

---

## 🛠️ 3. Matriz Comparativa de Roles y Componentes

| Rol de Nodo | Sensores (Suricata/Zeek) | Ingesta (Logstash/Redis) | Almacenamiento (Elasticsearch) | Consola (SOC UI / Kibana) |
| :--- | :---: | :---: | :---: | :---: |
| **Standalone** *(Actual)* | ✅ SÍ | ✅ SÍ | ✅ SÍ | ✅ SÍ |
| **Manager** | ❌ NO | ✅ SÍ (Redis) | ⚠️ Solo metadata | ✅ SÍ |
| **Sensor Node** | ✅ SÍ | ❌ NO | ❌ NO (solo PCAP local) | ❌ NO |
| **Search Node** | ❌ NO | ✅ SÍ (Parser) | ✅ SÍ (Data Lake) | ❌ NO |
| **Receiver Node** | ❌ NO | ✅ SÍ (Buffer activo) | ❌ NO | ❌ NO |
| **IDH Node** | ⚠️ Honeypot | ❌ NO | ❌ NO | ❌ NO |

---

## ⚙️ 4. Guía Rápida de Monitoreo y Mantenimiento de Salud

### Verificar Estado y Cola de Eventos:
```bash
# Ver estado general de los contenedores
sudo so-status

# Inspeccionar si la cola de Redis tiene eventos atascados
sudo docker exec so-redis redis-cli LLEN "logstash:redis"
```

### Liberar Memoria en Caso de Presión en Cache:
```bash
# Sincronizar escrituras pendientes y purgar cache temporal de Linux
sudo sync; echo 3 | sudo tee /proc/sys/vm/drop_caches

# Ver memoria real disponible
free -h
```

### Parámetros Críticos del Kernel (Ya aplicados permanentemente en `/etc/sysctl.d/99-soc-tuning.conf`):
* `vm.swappiness = 1` *(Evita que el sistema use Swap a menos que la RAM libre sea menor al 1%)*.
* `vm.dirty_background_ratio = 5` *(Obliga al kernel a escribir datos en disco de forma continua)*.
* `vm.dirty_ratio = 10` *(Evita ráfagas masivas de I/O que congelen los servicios)*.
