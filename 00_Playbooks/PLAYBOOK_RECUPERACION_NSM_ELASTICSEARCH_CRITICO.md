# 🚨 PLAYBOOK DE RECUPERACIÓN DE EMERGENCIA: DESBLOQUEO DE SECURITY ONION Y `/nsm` CRÍTICO

**Propósito:** Guía de acción rápida cuando `/nsm` supera el 90-95%, Elasticsearch se bloquea en modo solo lectura (`read_only_allow_delete: true`) y los servicios del SOC se caen en bucle.  
**Basado en:** Caso real resuelto durante el upgrade a Security Onion 3.3.0 (Octubre 2026).

---

## ⚡ 1. Síntomas de la Falla
* `df -h /nsm` muestra **>90%** o **>95%**.
* `sudo so-status` muestra contenedores reiniciándose o fallando (`so-elasticsearch`, `so-logstash`).
* Los logs de Logstash muestran: `FORBIDDEN/12/index read-only / allow delete (api)`.
* La web de Security Onion / Kibana no carga nuevos eventos ni alertas.

---

## 🛠️ Procedimiento de Rescate Paso a Paso

### PASO 1: Diagnóstico Rápido de Espacio e Índices
```bash
# 1. Verificar espacio de disco en /nsm
df -h /nsm

# 2. Ver qué carpetas de /nsm están consumiendo más espacio
sudo du -xh /nsm --max-depth=1 | sort -h

# 3. Listar los índices más pesados de Elasticsearch
sudo so-elasticsearch-query "_cat/indices?v&s=store.size:desc" | head -30
```

---

### PASO 2: Quitar el Bloqueo de Solo Lectura de Elasticsearch
Cuando el disco llega al 95%, Elasticsearch activa el candado de muerte (*flood-stage watermark*). Para poder borrar índices o recibir datos, hay que levantar el candado manualmente:

```bash
sudo so-elasticsearch-query "_all/_settings" -X PUT -d '{"index.blocks.read_only_allow_delete":null}'
```

---

### PASO 3: Borrado Manual de Índices Viejos Pesados
Identificar índices viejos de Zeek, Syslog o FortiGate que tengan más de 15 o 30 días y eliminarlos con llamada `DELETE`:

```bash
# Ejemplos de borrado de índices antiguos específicos:
sudo so-elasticsearch-query ".ds-logs-zeek-so-2026.10.22-000056" -X DELETE
sudo so-elasticsearch-query ".ds-logs-zeek-so-2026.10.23-000058" -X DELETE
sudo so-elasticsearch-query ".ds-logs-soc-so-2026.09.22-000001" -X DELETE
sudo so-elasticsearch-query ".ds-logs-system.syslog-default-2026.09.22-000001" -X DELETE
sudo so-elasticsearch-query ".ds-logs-fortinet_fortigate.log-default-2026.09.30-000001" -X DELETE
```

> [!TIP]
> También se pueden borrar índices viejos por patrón de comodín:
> ```bash
> # Borrar índices de Zeek de una fecha específica
> sudo so-elasticsearch-query "*zeek*2026.09*" -X DELETE
> ```

---

### PASO 4: Limpieza Profunda de Docker y Docker Registry (Recupera 20-30 GB)
Tras descargas o upgrades de versión (`soup`), el registro local de Docker queda lleno de capas huérfanas:

```bash
# 1. Eliminar temporales de subida de imágenes huérfanas
sudo rm -rf /nsm/docker-registry/docker/registry/v2/repositories/*/_uploads/*

# 2. Ejecutar recolección de basura del Docker Registry
sudo docker exec so-dockerregistry bin/registry garbage-collect /etc/distribution/config.yml -m

# 3. Purgar volúmenes y contenedores huérfanos de Docker en el host
sudo docker system prune -a --volumes -f
```

---

### PASO 5: Reparación de Shards Corruptos o No Asignados (`UNASSIGNED`)
Al apagarse abruptamente o quedarse sin disco, los shards de Elasticsearch suelen quedar desalineados:

```bash
# 1. Verificar si existen shards sin asignar
sudo so-elasticsearch-query "_cat/shards?v" | grep UNASSIGNED

# 2. Forzar la reasignación automática de shards fallidos
sudo so-elasticsearch-query "_cluster/reroute?retry_failed=true&pretty" -X POST

# 3. Si un shard primario específico sigue sin asignar, forzar su asignación:
sudo so-elasticsearch-query "_cluster/allocation/explain?pretty" -X POST -d '{
  "index": "NOMBRE_DEL_INDICE_CON_ERROR",
  "shard": 0,
  "primary": true
}'
```

---

### PASO 6: Reinicio de Servicios y Verificación de Salud
```bash
# 1. Reiniciar Elasticsearch si es necesario
sudo so-elasticsearch-restart

# 2. Verificar que el cluster de Elasticsearch esté en estado GREEN
sudo so-elasticsearch-query "_cluster/health?pretty"

# 3. Comprobar que todos los contenedores de Security Onion estén en OK/healthy
sudo so-status

# 4. Confirmar el nuevo espacio libre en /nsm (Debe estar <80%)
df -h /nsm
```

---

## 📋 Resumen Rápido de "One-Liners" de Emergencia

```bash
# Quitar candado:
sudo so-elasticsearch-query "_all/_settings" -X PUT -d '{"index.blocks.read_only_allow_delete":null}'

# Reroute shards:
sudo so-elasticsearch-query "_cluster/reroute?retry_failed=true&pretty" -X POST

# Garbage collect Docker Registry:
sudo docker exec so-dockerregistry bin/registry garbage-collect /etc/distribution/config.yml -m
```
