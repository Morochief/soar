# ⚡ AUDITORÍA Y MATRIZ DE COMPLIMIENTO: HIGH PERFORMANCE TUNING EN SECURITY ONION 3

**Fecha:** 22 de Octubre de 2026  
**Sistema:** Security Onion 3 Standalone (`172.17.10.25` / `soc-onion`)  
**Referencia Oficial:** [Security Onion 3 Docs — High Performance Tuning](https://docs.securityonion.net/en/3/main/performance/?h=swap#high-performance-tuning)  
**Autor:** Kevin Moraes (Analista SOC Technoma) / Asistente Autónomo SOAR  
**Estado General:** ✅ **CUMPLIMIENTO DE ALTO RENDIMIENTO VALIDADO EN PRODUCCIÓN**  

---

## 1. Matriz de Cumplimiento Técnico

| Sección de la Documentación Oficial | Parámetros Exigidos | Estado en `soc-onion` | Evidencia Técnica en el Host |
| :--- | :--- | :---: | :--- |
| **Disk/Memory Tuning** | `vm.swappiness = 1`<br>`vm.dirty_background_ratio = 5`<br>`vm.dirty_ratio = 10` | ✅ **Aplicado y Persistente** | Configurado en `/etc/sysctl.d/99-soc-swap.conf`. Protege la RAM física y previene *I/O latency spikes*. |
| **NIC Offloading (SEPTun)** | Desactivar GRO, LRO y Checksumming en la interfaz sniffing | ✅ **Cumplido al 100%** | `ethtool -k bond0` confirma:<br>• `generic-receive-offload: off`<br>• `large-receive-offload: off`<br>• `rx-checksumming: off` |
| **Elastic Pipeline Tuning** | Paralelización masiva de workers en Logstash y colas Redis | ✅ **Optimizado** | `pipeline_x_workers: 12` (1 worker por core de CPU disponible). Heap balanceado: Logstash (`2GB`) y Elasticsearch (`9.4GB`). |
| **CPU Allocation (Zeek & Suricata)** | Distribución equitativa de workers para captura y análisis | ✅ **Optimizado (5+5)** | • Suricata AF-Packet: `5 hilos`<br>• Zeek Load Balancing: `5 workers`<br>• 2 núcleos reservados para el SO y Elastic. |
| **CPU Pinning / NUMA Affinity** | Fijar hilos de sniffing a núcleos físicos de CPU | ℹ️ **No Requerido (Mononodo)** | Arquitectura virtualizada con un único nodo NUMA (`node0: CPUs 0-11`). El scheduler de Linux balancea sin penalización de bus. |

---

## 2. Detalle de Arquitectura por Componente

### A. Memoria y Disco (Subsanación de Saturación de Swap)
* **Condición Original:** Swap al 99.8% debido al valor por defecto del kernel (`swappiness=10` y `dirty_ratio=30`).
* **Ajuste:**
  ```ini
  vm.swappiness = 1
  vm.dirty_background_ratio = 5
  vm.dirty_ratio = 10
  ```
* **Impacto:** Liberación inmediata de 2.85 GB de Swap retenida y flujo suave de escritura en disco SSD/NVMe.

### B. Rendimiento de Captura de Red (SEPTun / Suricata Enterprise Performance Tuning)
Para evitar que la tarjeta de red agrupe paquetes artificialmente antes de que lleguen a los analizadores de protocolos (lo que rompería el análisis de reensamblado TCP de Zeek y firmas de Suricata), la interfaz de captura `bond0` tiene desactivadas las funciones de offloading:
* `rx-checksumming: off [fixed]`
* `generic-receive-offload: off`
* `large-receive-offload: off`

### C. Pipeline y Workers de Procesamiento
* **Capacidad de CPU del Host:** 12 vCPUs dedicadas.
* **Reparto de Carga en Ingesta:**
  * **Suricata IDS:** 5 subprocesos (`af-packet.threads: 5`).
  * **Zeek Protocol Decoders:** 5 procesos (`lb_procs: 5`).
  * **Logstash Pipeline:** 12 hilos paralelos (`pipeline_x_workers: 12`).
  * **Redis Buffer:** `so-redis` operando como cola intermedia para amortiguar picos de tráfico perimetral.

---

## 3. Consideraciones Futuras de Escalamiento
Si la infraestructura se migra a un servidor físico (*Bare-Metal*) con múltiples sockets de CPU y enlaces de 10Gbps/40Gbps:
1. **CPU Pinning:** Se recomienda mapear explícitamente los hilos de Suricata y Zeek a los núcleos del socket NUMA directamente conectado a la tarjeta PCIe de red.
2. **Ampliación de RAM:** Al sobreaprovisionar memoria (>32 GB o 64 GB), se podrá proceder a la desactivación total de swap (`swapoff -a`) como recomienda la guía oficial de Elasticsearch.
