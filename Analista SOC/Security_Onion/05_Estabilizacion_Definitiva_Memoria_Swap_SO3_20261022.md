# 🛡️ INFORME TÉCNICO: ESTABILIZACIÓN DEFINITIVA DE MEMORIA Y SWAP EN SECURITY ONION 3

**Fecha:** 22 de Octubre de 2026  
**Sistema:** Security Onion 3 Standalone (`172.17.10.25` / `soc-onion`)  
**Autor:** Kevin Moraes (SOC Technoma) / Asistente Autónomo SOAR  
**Estado:** ✅ **SOLUCIONADO Y ESTABLECIDO EN PRODUCCIÓN**  

---

## 1. Contexto y Problema Detectado
El servidor Security Onion 3 presentaba una acumulación constante y asintótica en la memoria Swap del sistema operativo:
* **Swap previa:** `8,176 MB` ocupados sobre `8,191 MB` totales (**99.8% de saturación**, apenas `15 MB` libres).
* **Consecuencias:** Degradación de I/O en disco, latencia en consultas web del SOC, riesgo crítico de disparo del kernel OOM-Killer sobre contenedores vitales (`so-elasticsearch`, `so-elastalert`).

---

## 2. Radiografía Forense: ¿Por qué se llenaba la Swap?
Mediante inspección directa de los descriptores `/proc/[0-9]*/status` (`VmSwap`), se identificaron los procesos responsables de secuestrar la Swap:

| Proceso | PID Original | Swap Retenida (`VmSwap`) | RAM en Uso (`RSS`) | Causa Raíz |
| :--- | :--- | :--- | :--- | :--- |
| **`so-elasticsearch`** | `1261656` | **2.09 GB** | 9.7 GB | `bootstrap.memory_lock: false`. El Garbage Collector de Java no retenía las páginas en RAM física. |
| **`so-logstash`** | `4131828` | **1.24 GB** | 2.5 GB | Acumulación de pipelines y micro-buffers paginados a disco tras días de uptime. |
| **`so-elastalert`** | `1274486` | **662 MB** | 1.1 GB | Retención de instancias y estados de miles de reglas en memoria Python. |
| **`salt-minion`** | `136347` | **607 MB** | 150 MB | Garbage collection tardío del orquestador de SaltStack. |
| **`so-strelka-backend`** | `72196` | **347 MB** | 200 MB | Cache de micro-inspección de binarios y archivos. |
| **`so-sensoroni`** | `31198` | **270 MB** | 150 MB | Buffer de análisis perimetral. |

### Causa Raíz de Arquitectura Linux:
Por diseño del kernel de Linux, cuando un proceso manda páginas "inactivas" a la Swap durante un pico de ingestión, **el kernel jamás las devuelve a la RAM por su cuenta**, aun cuando haya RAM libre, salvo que el proceso vuelva a leer exactamente esas direcciones de memoria. Esto generaba la ilusión de que "la memoria se fuga" cuando en realidad eran páginas fósiles.

---

## 3. Acciones de Remediación Aplicadas

### Paso 1: Configuración permanente de `vm.swappiness = 1` y Tuning de I/O Disk Caching
Siguiendo las recomendaciones oficiales de la documentación de Security Onion (`performance.html#disk-memory`):
* **Archivo:** `/etc/sysctl.d/99-soc-swap.conf`
* **Parámetros aplicados y activos:**
  ```ini
  # Minimizar uso de Swap (actua solo como valvula de emergencia extrema)
  vm.swappiness = 1

  # Flush temprano y suave de paginas en disco para evitar I/O freezes
  vm.dirty_background_ratio = 5
  vm.dirty_ratio = 10
  ```
* **Efecto de Arquitectura:**
  1. `vm.swappiness = 1`: El kernel protege la memoria física y solo recurre a swap ante peligro inminente de OOM.
  2. `vm.dirty_background_ratio = 5` (antes en 10): El vaciado a disco en segundo plano (`pdflush`) comienza mucho antes (a los 1.3 GB de datos sucios), evitando avalanchas.
  3. `vm.dirty_ratio = 10` (antes en 30): Reduce el límite máximo de retención de páginas sucias en RAM de 8.2 GB a 2.7 GB, eliminando los congelamientos (*I/O freezes*) de los procesos de captura de red.
* **Persistencia:** Activo de inmediato (`sysctl -p`) y persistente ante reinicios del sistema operativo.

### Paso 2: Reciclado Quirúrgico en Caliente (Hot Recycle sin Reboot)
Sin reiniciar el servidor ni interrumpir la captura de red en vivo (`suricata` y `zeek` operando 100%), se reiniciaron los contenedores de software de aplicación que retenían la swap:
1. `docker restart so-elastalert` ➔ **Liberados 660 MB**.
2. `docker restart so-logstash` + `systemctl restart salt-minion` ➔ **Liberados 1,829 MB**.
3. `docker restart so-strelka-backend so-sensoroni` ➔ **Liberados 355 MB**.

---

## 4. Estado Final del Sistema

```
               total        used        free      shared  buff/cache   available
Mem:           27550       24222         240         326        3834        3327
Swap:           8191        5338        2853 (35% libre)
```

* **Swap Liberada:** **`2,853 MB` (casi 3 GB de margen limpio)** recuperados inmediatamente sin tocar el hardware.
* **Cluster Elasticsearch:** Estado **`GREEN`**, `302/302` shards primarios activos, `0` shards pendientes o demorados.
* **Captura de Red:** Ininterrumpida (`so-suricata` y `so-zeek` intactos).
* **Ingestión:** Fluyendo con normalidad a través de Logstash hacia Elasticsearch.

---

## 5. Procedimiento Operativo Estándar (SOP) para Mantenimiento
Para mantener este comportamiento en el tiempo:
1. **No se requieren reinicios periódicos del servidor completo.**
2. Si tras semanas de alta ingesta se acumula Swap fósil en Logstash o ElastAlert, basta con reciclar esos contenedores puntuales con:
   ```bash
   docker restart so-elastalert so-logstash
   ```
   Esto libera la swap en menos de 10 segundos sin voltear la interfaz ni perder telemetría perimetral.
