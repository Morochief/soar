# 📜 CHEATSHEET OPERATIVO: SECURITY ONION 3.1.0 (SO3) — GRID DISTRIBUIDA

> **OBJETIVO:**  
> Registro permanente de comandos de administración, diagnóstico y gestión de filtros para la Grid de Security Onion (`172.17.10.25`).  
> Todos los comandos deben ejecutarse con privilegios `sudo`.

---

## 🔍 1. Diagnóstico de Salud de la Grid y Contenedores

| Comando | Propósito |
| :--- | :--- |
| `sudo so-status` | Muestra el estado de salud de todos los contenedores de Security Onion (`running`, `healthy`). |
| `sudo docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Image}}"` | Lista detallada de contenedores Docker activos, tiempos de uptime y tags de imagen (`so-*:3.1.0`). |
| `sudo salt-key -L` | Lista todos los nodos de la Grid y verifica el estado de las llaves aceptadas (`ndr_sensor`, `secops-vascol_sensor`, etc.). |
| `sudo so-version` | Muestra la versión exacta instalada de Security Onion y parches activos. |

---

## 🛡️ 2. Fuentes de la Verdad de Filtros y SaltStack (Persistencia e IaC)

> ⚠️ **REGLA DE ORO: EL CICLO DE 15 MINUTOS (HIGHSTATE DRIFT RECONCILIATION)**  
> En SO3 distribuido, **NUNCA modificar archivos directamente en `/opt/so/conf/` ni dentro de contenedores Docker**.  
> Cada 15 minutos corre un job de SaltStack que detecta discrepancias de configuración y **sobreescribe cualquier cambio manual**.  
> Para que un filtro sea permanente y sobreviva a los ciclos de Salt, debe escribirse en el árbol maestro `/opt/so/saltstack/local/` (que tiene prioridad de merge sobre `/opt/so/saltstack/default/`).

| Tipo de Filtro | Archivo Fuente de la Verdad (Persistente) | Destino Compilado en Sensores |
| :--- | :--- | :--- |
| **Supresiones Suricata (IDS)** | `/opt/so/saltstack/local/salt/suricata/files/threshold.conf` | `/opt/so/conf/suricata/threshold.conf` |
| **Filtros de Captura BPF (Pillar)**| `/opt/so/saltstack/local/pillar/bpf/soc_bpf.sls` | `/opt/so/conf/suricata/bpf` y `/opt/so/conf/zeek/bpf` |
| **Pillar de Sensores** | `/opt/so/saltstack/local/pillar/minions/<minion>.sls` | Configuración específica de interfaces (`bond0`), CPU y PCAP. |

> **CONFIRMACIÓN TÉCNICA EN VIVO:**  
> En `/opt/so/saltstack/default/pillar/top.sls`, las líneas 94-95, 143-144, 196-197 y 218-219 incluyen de forma nativa:  
> `- bpf.soc_bpf` y `- bpf.adv_bpf` para todos los roles de la Grid.  
> Por tanto, **el pilar `soc_bpf.sls` es 100% oficial y persistente ante el ciclo de 15 minutos**.

### Esquema YAML Oficial de BPF en SO3 (`/opt/so/saltstack/local/pillar/bpf/soc_bpf.sls`):
```yaml
bpf:
  suricata:
    - "not (host 192.168.16.6 and port 53)"
    - "not (net 192.168.169.0/24 and tcp port 7680)"
  zeek:
    - "not (host 192.168.16.6 and port 53)"
    - "not (net 192.168.169.0/24 and tcp port 7680)"
  pcap:
    - "not (host 192.168.16.6 and port 53)"
```

### Mecanismo de Compilación Jinja2 Descubierto (`suricata.map.jinja`):
SaltStack utiliza `salt['pillar.get']('bpf', merge=True)`.  
Une la lista con `SURICATABPF|join(" ")` y la valida con:
`/opt/so/saltstack/default/salt/common/tools/sbin/so-bpf-compile <interfaz> <expresion_bpf>`  
Si el código de retorno es `0` (sintaxis TCPDump válida), compila el socket filter y lo distribuye a los contenedores de los sensores (`ndr_sensor`, etc.).

---

## ⚙️ 3. Comandos de Inspección Forense Ejecutados

```bash
# 1. Rastrear de dónde se genera threshold.conf (buscando una regla activa)
sudo grep -rn "2025707" /opt/so/ 2>/dev/null

# 2. Ver la plantilla maestra de supresiones IDS de Suricata
sudo cat /opt/so/saltstack/local/salt/suricata/files/threshold.conf

# 3. Ver los BPF activos en los motores de captura
sudo cat /opt/so/conf/suricata/bpf
sudo cat /opt/so/conf/zeek/bpf

# 4. Ver los pilares y configuración de BPF de SaltStack
sudo cat /opt/so/saltstack/local/pillar/bpf/soc_bpf.sls
sudo cat /opt/so/saltstack/local/pillar/bpf/adv_bpf.sls
sudo cat /opt/so/saltstack/default/salt/bpf/soc_bpf.yaml
```

---

## 🚀 4. Comandos de Aplicación y Sincronización en la Grid

```bash
# 1. Compilar y sincronizar cambios de Suricata (Thresholds y Reglas) en todos los nodos
sudo so-rule-update
sudo salt '*' state.apply suricata

# 2. Sincronizar cambios en Zeek en todos los nodos
sudo salt '*' state.apply zeek

# 3. Compilar BPF en toda la Grid
sudo /opt/so/saltstack/default/salt/common/tools/sbin/so-bpf-compile
sudo salt '*' state.apply bpf

# 4. Reiniciar Logstash para aplicar filtros de Syslog (FortiGate)
sudo so-logstash-restart
```

---

## 🔬 4. Comandos Forenses y Búsqueda en el Sistema de Archivos

```bash
# Rastrear dónde está definida una regla o firma (ejemplo SID 2025707)
sudo grep -rn "2025707" /opt/so/ 2>/dev/null

# Ver qué interfaces de sniffing tiene asignadas el sensor NDR
sudo cat /opt/so/saltstack/local/pillar/minions/ndr_sensor.sls

# Inspeccionar logs del orquestador SaltStack en tiempo real
sudo tail -f /opt/so/log/salt/master
```

---

## 📡 5. Validación de Telemetría Previa al Filtrado (Pre-BPF / Pre-Threshold)

Antes de silenciar o descartar tráfico mediante BPF o reglas de supresión, se debe constatar si los paquetes están ingresando por la interfaz y si generan alertas o logs.

### A. Inspección de tráfico en vivo (Captura SPAN/Mirroring)
```bash
# Escuchar en vivo si la IP y puerto llegan por el SPAN (se detiene tras 5 paquetes)
sudo tcpdump -nn -i any host 192.168.16.6 and port 53 -c 5

# Escuchar en interfaz específica del sensor (ejemplo bond0)
sudo tcpdump -nn -i bond0 host 192.168.16.6 and port 53 -c 10
```

### B. Inspección de contenedores y logs activos en disco (Zeek & Suricata)
En Security Onion 3, tanto Zeek como Suricata corren en contenedores dedicados (`so-zeek`, `so-suricata`). Para inspeccionar sus rutas y logs:

```bash
# Ver contenido de carpetas NSM montadas en el host:
sudo ls -la /nsm/zeek/
sudo ls -la /nsm/suricata/

# Inspeccionar logs directamente dentro del contenedor de Zeek:
sudo docker exec so-zeek ls -la /nsm/zeek/logs/
sudo docker exec so-zeek tail -n 20 /nsm/zeek/logs/current/dns.log 2>/dev/null

# Inspeccionar logs de alertas de Suricata:
sudo docker exec so-suricata tail -n 20 /nsm/suricata/eve.json
```

### C. Consulta directa por API a Elasticsearch Central
Permite verificar de forma instantánea si una IP generó eventos indexados en toda la Grid:

```bash
# 1. Ubicación real de credenciales de Elasticsearch en SO 3:
# Archivo: /opt/so/saltstack/local/pillar/elasticsearch/auth.sls (Usuario: so_elastic)

# 2. Extraer credencial y consultar conteo de eventos de una IP en Elasticsearch:
ES_PASS=$(sudo grep -A 2 "so_elastic_user:" /opt/so/saltstack/local/pillar/elasticsearch/auth.sls | grep "pass:" | awk '{print $2}' | tr -d '"')
curl -s -k -u "so_elastic:$ES_PASS" "https://127.0.0.1:9200/*/_count?q=192.168.16.6"

# 3. Auditoría distribuida en TODOS los sensores de la Grid a la vez (SaltStack):
sudo salt '*' cmd.run 'grep "192.168.16.6" /nsm/zeek/spool/logger/dns.log 2>/dev/null || grep "192.168.16.6" /nsm/zeek/logs/current/dns.log 2>/dev/null || echo "Sin trafico en este sensor"'

# 4. Inspeccionar el mensaje crudo del evento más reciente (Detectar Syslog de Firewalls):
curl -s -k -u "so_elastic:$ES_PASS" "https://127.0.0.1:9200/*/_search?q=192.168.16.6&size=1" | python3 -m json.tool | grep -A 10 -B 2 -E '"message"|"syslog"'
```

### D. Búsqueda en Security Onion Web (Hunt / Lucene)
Acceder a `https://172.17.10.25` -> **Hunt**:
- **Filtrar DNS de la IP:** `source.ip: 192.168.16.6 and destination.port: 53`
- **Filtrar todo el tráfico de la IP:** `ip: 192.168.16.6`
- **Filtrar alertas específicas de Suricata:** `event.module: "suricata" and source.ip: 192.168.16.6`
- **Filtrar mensajes de FortiGate:** `message: "FG-Technoma" and message: "192.168.16.6"`

---

## 🚑 6. Rescate de Recursos y Mantenimiento de Emergencia (Elasticsearch, Swap y Disco)

### Diagnóstico de Colapso de Cluster
* **Causa de caída recurrente de Elasticsearch:** 
  1. **Swap al 100%:** Linux OOM-Killer asesina el proceso JVM de Elasticsearch (`java`) cuando se saturan los 8.6 GB de swap.
  2. **Partición `/nsm` > 85% - 90% (Floodstage Watermark):** Elasticsearch bloquea todos los índices a solo lectura (`read-only`) para evitar corrupción de datos.

### A. Acceso a Logs de Error de Cada Componente en SO3

| Componente | Comando Docker en Vivo | Ruta de Logs en Disco (Host) |
| :--- | :--- | :--- |
| **Elasticsearch** | `sudo docker logs --tail 50 -f so-elasticsearch` | `/nsm/elasticsearch/logs/` |
| **Logstash** | `sudo docker logs --tail 50 -f so-logstash` | `/nsm/logstash/logs/` |
| **ElastAlert** | `sudo docker logs --tail 50 -f so-elastalert` | Montado en memoria del contenedor |
| **Suricata** | `sudo docker logs --tail 50 -f so-suricata` | `/nsm/suricata/suricata.log` |
| **Zeek** | `sudo docker logs --tail 50 -f so-zeek` | `/nsm/zeek/spool/logger/stderr.log` |
| **Kibana** | `sudo docker logs --tail 50 -f so-kibana` | `/nsm/kibana/logs/` |
| **SaltStack Master** | `sudo tail -f /opt/so/log/salt/master` | `/opt/so/log/salt/master` |

### Destrabar Procesos Huérfanos de SaltStack (`--force`)
Si al reiniciar un componente el script se queda esperando porque otro job de Salt quedó trabado en segundo plano (`state.highstate` / `state.apply`), usar el modificador `--force` para limpiar los PIDs huérfanos y forzar la regeneración del contenedor:
```bash
sudo so-elasticsearch-restart --force
sudo so-logstash-restart --force
sudo so-elastalert-restart --force
```

### B. Diagnóstico y Desglose de Memoria RAM y Swap por Contenedor

Permite ver exactamente cuántos gigas y qué porcentaje consume cada servicio de Security Onion:

```bash
# 1. Ver estado general de memoria física, caché y swap disponible:
free -h

# 2. Ver los 6 contenedores principales que consumen el 75% de la RAM del servidor:
sudo docker stats --no-stream --format "table {{.Name}}\t{{.MemUsage}}\t{{.MemPerc}}" | grep -E 'elasticsearch|logstash|kibana|soc|zeek|suricata|NAME'

# 3. Listar TODOS los 23 contenedores ordenados por consumo real de memoria (GiB/MiB):
sudo docker stats --no-stream --format "table {{.Name}}\t{{.MemUsage}}\t{{.MemPerc}}" | sort -k 2 -h -r

# 4. Monitoreo continuo en vivo (se actualiza segundo a segundo, salir con Ctrl+C):
sudo docker stats --format "table {{.Name}}\t{{.MemUsage}}\t{{.MemPerc}}\t{{.CPUPerc}}"
```

> [!NOTE]
> **Régimen Nominal Normal en Standalone:**  
> En un nodo Standalone con 23 contenedores activos, es **completamente normal** un uso de 20 a 24 GB de RAM (85-90%). Elasticsearch pre-asigna ~10 GB para su Heap Java por arquitectura. El indicador de salud crítico es que el **Swap tenga siempre margen libre (>3 GB)** y no esté al 100%.


### C. Procedimiento Paso a Paso de Purga de Índices Basura en Elasticsearch

1. **Obtener la clave administrativa de `so_elastic`:**
   ```bash
   ES_PASS=$(sudo grep -A 2 "so_elastic_user:" /opt/so/saltstack/local/pillar/elasticsearch/auth.sls | grep "pass:" | awk '{print $2}' | tr -d '"')
   ```

2. **Listar los índices más pesados para identificar anomalías:**
   ```bash
   curl -s -k -u "so_elastic:$ES_PASS" "https://127.0.0.1:9200/_cat/indices?v&s=pri.store.size:desc" | head -n 15
   ```

3. **Ejecutar la purga de los índices identificados como basura:**
   ```bash
   # Purgar bucle de errores de ElastAlert (Liberó 7.4 GB):
   curl -s -k -u "so_elastic:$ES_PASS" -X DELETE "https://127.0.0.1:9200/elastalert_error"

   # Purgar acumulador de estados masivos de ElastAlert (Liberó 1.4 GB):
   curl -s -k -u "so_elastic:$ES_PASS" -X DELETE "https://127.0.0.1:9200/elastalert_status"
   ```
   *Respuesta esperada:* `{"acknowledged": true}`

4. **Purga Selectiva de Eventos Específicos sin Borrar Índices (`_delete_by_query`):**
   Permite eliminar retroactivamente eventos ruidosos que ya fueron indexados en el pasado (ejemplo: los 55.409 eventos de la cámara Dahua):
   ```bash
   curl -s -k -u "so_elastic:$ES_PASS" -X POST "https://127.0.0.1:9200/*/_delete_by_query?conflicts=proceed" -H 'Content-Type: application/json' -d'
   {
     "query": {
       "query_string": {
         "query": "192.168.16.6"
       }
     }
   }'
   ```

5. **Verificar la recuperación inmediata de almacenamiento en el sistema:**
   ```bash
   df -h /nsm
   ```

6. **Ajustar Réplicas en Nodos Standalone (Pasar Cluster de Yellow/Pending a Green/OK al 100%):**
   En arquitecturas de 1 solo nodo de datos, los índices que solicitan réplicas quedan con shards no asignados (`unassigned_shards`), manteniendo el cluster en `yellow` y la Web en `Pending`. Ajustar a 0 réplicas pone el cluster en `green` inmediatamente:
   ```bash
   curl -s -k -u "so_elastic:$ES_PASS" -X PUT "https://127.0.0.1:9200/*/_settings" -H 'Content-Type: application/json' -d '{"index": {"number_of_replicas": 0}}'
   curl -s -k -u "so_elastic:$ES_PASS" "https://127.0.0.1:9200/_cluster/health?pretty"
   ```


---

## 🛡️ 7. Registro Oficial de Filtros Aplicados en este Servidor

### Filtro 1: Descarte de Syslog de Cámara Dahua Denegada en FortiGate
* **Problema:** El firewall `FG-Technoma` bombardeaba a Security Onion con miles de logs por minuto informando tráfico DNS denegado de la cámara `192.168.16.6` en la VLAN16.
* **Capa Técnica:** **Capa 3 (Logstash Drop)** — Los filtros BPF de Suricata/Zeek no actúan sobre Syslog.
* **Mecanismo Maestro Oficial de SO3 (SaltStack IaC):**
  Security Onion compila Logstash mediante `defined_pipelines` y aplica `clean: True` al directorio de destino. Si un archivo `.conf` no está registrado en el pilar, SaltStack lo elimina en cada reinicio.
* **1. Archivo Fuente en SaltStack:**
  `/opt/so/saltstack/local/salt/logstash/pipelines/config/custom/9000_drop_fg_dahua.conf`
  ```ruby
  filter {
    if "192.168.16.6" in [message] or "192.168.16.6" in [event][original] {
      drop { }
    }
  }
  ```
* **2. Declaración en el Pilar Local (`soc_logstash.sls`):**
  Archivo: `/opt/so/saltstack/local/pillar/logstash/soc_logstash.sls`
  ```yaml
  logstash:
    defined_pipelines:
      manager:
        - so/0011_input_endgame.conf
        - so/0012_input_elastic_agent.conf.jinja
        - so/0013_input_lumberjack_fleet.conf.jinja
        - custom/9000_drop_fg_dahua.conf
        - so/9999_output_redis.conf.jinja
      search:
        - so/0900_input_redis.conf.jinja
        - custom/9000_drop_fg_dahua.conf
        - so/9805_output_elastic_agent.conf.jinja
        - so/9900_output_endgame.conf.jinja
  ```
* **3. Directorios de Despliegue Activo en el Contenedor:**
  - Manager: `/opt/so/conf/logstash/pipelines/manager/9000_drop_fg_dahua.conf` (descarta antes de Redis).
  - Search: `/opt/so/conf/logstash/pipelines/search/9000_drop_fg_dahua.conf` (descarta antes de Elasticsearch).
* **4. Comando de Compilación y Aplicación:**
  ```bash
  sudo so-logstash-restart
  ```
* **5. Comando de Verificación (Comprobar que el contador no sube más):**
  ```bash
  ES_PASS=$(sudo grep -A 2 "so_elastic_user:" /opt/so/saltstack/local/pillar/elasticsearch/auth.sls | grep "pass:" | awk '{print $2}' | tr -d '"')
  curl -s -k -u "so_elastic:$ES_PASS" "https://127.0.0.1:9200/*/_count?q=192.168.16.6"
  ```

---

## ⚡ 8. Playbook Rápido: Aplicar un Nuevo Filtro Drop en Logstash (Método Oficial Probado)

Cada vez que se identifique una IP o evento ruidoso de firewall/syslog, ejecutar estos pasos exactos:

### 1. Diagnóstico previo (Confirmar que es Syslog)
```bash
ES_PASS=$(sudo grep -A 2 "so_elastic_user:" /opt/so/saltstack/local/pillar/elasticsearch/auth.sls | grep "pass:" | awk '{print $2}' | tr -d '"')
curl -s -k -u "so_elastic:$ES_PASS" "https://127.0.0.1:9200/*/_search?q=<TARGET>&size=1&sort=@timestamp:desc" | python3 -m json.tool | grep -A 8 -B 2 '"message"'
```

### 2. Registrar en el Pilar de SaltStack (`soc_logstash.sls`)
En `/opt/so/saltstack/local/pillar/logstash/soc_logstash.sls`, agregar el archivo en `defined_pipelines.search` y su contenido bajo `pipeline_config`:

```yaml
logstash:
  defined_pipelines:
    manager:
      - so/0011_input_endgame.conf
      - so/0012_input_elastic_agent.conf.jinja
      - so/0013_input_lumberjack_fleet.conf.jinja
      - so/9999_output_redis.conf.jinja
    search:
      - so/0900_input_redis.conf.jinja
      - custom/9000_drop_fg_dahua.conf
      - custom/9001_drop_fg_vpn_ecop.conf
      - custom/<NUMERO>_drop_<NOMBRE>.conf      # <-- Registrar en lista
      - so/9805_output_elastic_agent.conf.jinja
      - so/9900_output_endgame.conf.jinja
  pipeline_config:
    9000_drop_fg_dahua: |
      filter {
        if "192.168.16.6" in [message] or "192.168.16.6" in [event][original] {
          drop { }
        }
      }
    9001_drop_fg_vpn_ecop: |
      filter {
        if "ECOP-MATRIZ-SEC" in [message] or "ECOP-MATRIZ-SEC" in [event][original] {
          drop { }
        }
      }
    <NUMERO>_drop_<NOMBRE>: |                   # <-- Contenido del filtro
      filter {
        if "<TARGET>" in [message] or "<TARGET>" in [event][original] {
          drop { }
        }
      }
```

### 3. Compilar con SaltStack (Crea automáticamente el archivo en search/)
```bash
sudo salt-call state.apply logstash.config
```
*(Debe terminar con `Failed: 0` y `changed > 0`).*

### 4. Reiniciar Logstash y Validar
```bash
# Reiniciar contenedor:
sudo so-logstash-restart --force

# Comprobar que el archivo se generó en el pipeline de search:
sudo ls -la /opt/so/conf/logstash/pipelines/search/

# Comprobar en tiempo real sobre el stream activo de logs (respuesta instantánea en 0.05s):
curl -s -k -u "so_elastic:$ES_PASS" "https://127.0.0.1:9200/logs-zeek-so/_count?q=message:*<TARGET>*"

# (Alternativa global por IP):
curl -s -k -u "so_elastic:$ES_PASS" "https://127.0.0.1:9200/logs-zeek-so/_count?q=<IP>"
```

---

## 🔎 9. Comando de Cacería: Descubrir el Próximo Gran Emisor de Eventos

Para identificar la siguiente fuente de ruido que satura la base de datos:

```bash
# Top 5 IPs con mayor volumen de eventos generados:
ES_PASS=$(sudo grep -A 2 "so_elastic_user:" /opt/so/saltstack/local/pillar/elasticsearch/auth.sls | grep "pass:" | awk '{print $2}' | tr -d '"')
curl -s -k -u "so_elastic:$ES_PASS" "https://127.0.0.1:9200/logs-zeek-so/_search" -H 'Content-Type: application/json' -d'
{
  "size": 0,
  "aggs": {
    "top_ips": {
      "terms": {
        "field": "source.ip",
        "size": 5
      }
    }
  }
}' | python3 -m json.tool | grep -A 3 -B 1 '"key"'
```









