# Security Onion 3: Memoria Institucional y Guía Operativa

Este documento centraliza el conocimiento operativo, los hallazgos críticos de arquitectura descubiertos en el SOC, y la guía de comandos esenciales para la administración de un entorno Security Onion distribuido.

---

## Parte 1: Memoria Institucional y Hallazgos Críticos

### Hallazgo #1: Purga Automática de Logs por Falta de Espacio (Julio 2026)
**Contexto**: Durante una investigación de un posible C&C, se detectó la desaparición de eventos críticos de red (Zeek, Syslog) pocas horas después de su ingesta, quedando el SOC completamente ciego ante auditorías retrospectivas mayores a 24 horas.

**Diagnóstico Técnico**: 
La partición `/nsm` del nodo Manager cuenta con **solo 125 GB**, lo cual está muy por debajo de los requisitos exigidos por la documentación oficial de SO3 (Múltiples Terabytes, Sec. 5.5). 

Al migrar a la v3, el sistema configuró una barrera de supervivencia llamada `LOG_SIZE_LIMIT` (establecida en **62 GB** para este entorno). Cuando el tráfico pesado (como los metadatos de Zeek) satura estos 62 GB, un *cronjob* de emergencia de Security Onion despierta y decapita los índices activos del día para salvar la base de datos de un colapso total.

**Evidencia Forense**: 
El archivo `/opt/so/log/elasticsearch/so-elasticsearch-indices-delete.log` muestra un ciclo de auto-destrucción diario:
```text
Used disk space exceeds LOG_SIZE_LIMIT (62 GB) - There is only one backing index (.ds-logs-zeek-so-2026.07.07-000001).  Deleting logs-zeek-so data stream...
```
*(Nota: Las alertas de Suricata sobreviven a la purga porque ocupan apenas ~80 MB diarios, pero todo el contexto de red desaparece).*

### Hallazgo #2: Bloqueo de Shards por Límite de Watermark de Disco (85%) al Ingresar Nuevos Clientes (Septiembre 2026)
**Contexto**: Al enrolar el nuevo cliente VALORES (`valores-ndr`), la consola Web (Hunt) comenzó a arrojar el error:
`The search query encountered a failure within the Elasticsearch cluster. Check SOC logs for details.`

**Diagnóstico Técnico**:
El cluster de Elasticsearch entró en estado **`RED`** con `unassigned_primary_shards: 1`. 
Al auditar con `_cluster/allocation/explain`, se detectó que el índice recién creado para el FortiGate de VALORES (`.ds-logs-fortinet_fortigate.log-default-...`) fue rechazado por el decider `disk_threshold`:
```text
the node is above the high watermark cluster setting [cluster.routing.allocation.disk.watermark.high=85%], having less than the minimum required [18.6gb] free space, actual free: [16.8gb], actual used: [86.4%]
```
El Manager estaba al 86.4% de disco debido a la acumulación de metadatos de Zeek de la oficina interna (`securityonion`), donde 3 índices sumaban más de 50 GB.

**Resolución Aplicada**:
Se auditó la composición del índice más pesado y antiguo (`.ds-logs-zeek-so-2026.09.27-000007`, 21.1 GB), certificando que el 99.99% (26.2 millones de eventos) pertenecía al tráfico local de la oficina y tenía más de 72 horas.
Se ejecutó la purga selectiva:
```bash
sudo so-elasticsearch-query '.ds-logs-zeek-so-2026.09.27-000007' -X DELETE
sudo so-elasticsearch-query '_cluster/reroute?retry_failed=true' -X POST
```
**Resultado**: Se recuperaron **21.1 GB en 3 segundos**, el disco bajó a menos del 70%, el shard de FortiGate fue asignado automáticamente y la salud del cluster se restableció a **`YELLOW`** (`unassigned_primary_shards: 0`), normalizando la consola Web.

**Ajuste Definitivo de Retención Heurística (ILM a 1 Día para Zeek)**:
Para evitar que el sensor local de Technoma (`securityonion`, emisor de ~26 millones de eventos/día) vuelva a asfixiar el cluster y bloquear los logs de clientes como VALORES o VASCOL, se modificó la política oficial `so-zeek-logs` en Elasticsearch reduciendo la fase `delete` a `min_age: 1d`:
```bash
sudo so-elasticsearch-query '_ilm/policy/so-zeek-logs' -X PUT -d '{
  "policy": {
    "phases": {
      "hot": {
        "min_age": "0ms",
        "actions": {
          "set_priority": { "priority": 100 },
          "rollover": { "max_age": "1d", "max_primary_shard_size": "50gb" }
        }
      },
      "delete": {
        "min_age": "1d",
        "actions": { "delete": { "delete_searchable_snapshot": true } }
      }
    }
  }
}'
```
*Garantía de Aislamiento*: Esta política únicamente gobierna el data stream `logs-zeek-so`. Las alertas de seguridad (Suricata), los logs de auditoría Syslog y los eventos perimetrales de FortiGate residen en data streams separados con sus propias políticas ILM independientes, preservando la visibilidad extendida de los clientes.


### Glosario Técnico (SO3 / Elasticsearch)
> [!NOTE]
> Términos indispensables para comprender cómo funciona el motor de datos bajo el capó de SO3.

* **Data Stream (Flujo de Datos)**: En SO3, ya no se usan los clásicos índices diarios (ej. `logstash-2023-01-01`). Ahora se usan *Data Streams* (ej. `logs-zeek-so`). Son una abstracción: para Kibana es un solo flujo infinito de datos, por lo que no necesitas preocuparte de qué día estás consultando.
* **Backing Index (Índice de Respaldo)**: Son los índices físicos ocultos que viven detrás de un Data Stream. Tienen nombres autogenerados como `.ds-logs-zeek-so-2026.07.08-000001`. Cuando se llenan, se genera el `000002`. Cuando SO3 se queda sin espacio, borra estos *Backing Indices*.
* **ILM (Index Lifecycle Management)**: Es el "cerebro" dentro de Elasticsearch que gobierna la retención. Decide automáticamente cuándo un índice se rota (*rollover*), cuándo se comprime (*warm/cold phase*) y cuándo debe borrarse (*delete phase*) según políticas de edad o tamaño (ej. borrar tras 30 días).
* **LOG_SIZE_LIMIT**: Una regla estricta añadida por los creadores de Security Onion. El sistema operativo escanea constantemente el disco `/nsm` y calcula un porcentaje seguro. Si los *Backing Indices* rompen ese límite en Gigabytes, SO3 ejecuta el servicio `MetadataDeleteIndexService` (una especie de francotirador) que borra los datos indiscriminadamente para proteger el sistema de corromperse.

---

## Parte 2: Guía Rápida de Comandos SOC (Cheat Sheet)

Esta sección contiene los comandos fundamentales de administración, orquestación y diagnóstico que todo Operador SOC necesita. Todos los comandos deben ejecutarse con privilegios de `root` (usando `sudo`) desde la consola del **Manager**.

### Datos de Conexión e Infraestructura por Cliente

#### Manager Central (Datacenter SOC)
* **Host:** `soc-onion`
* **IP:** `172.17.10.25`
* **Acceso:** `ssh soc-admin@172.17.10.25`

#### Cliente VASCOL
* **Nodo:** `secops-vascol`
* **IP de Gestión:** `192.168.15.71`
* **Acceso:** `ssh admin@192.168.15.71`
* **Contraseña:** `LMs0cZXhgds*`
* **Rol:** `SENSOR` (Re-desplegado por Liderazgo SOC como Sensor NDR dedicado; ingesta Syslog FortiGate `192.168.110.1` hacia el Manager, eliminando shards distribuidos sobre WAN/ZeroTier).
* **Documentación Detallada:** [informe_tecnico_despliegue_secops_vascol.md](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/03_Arquitectura_y_Despliegue/informe_tecnico_despliegue_secops_vascol.md)

#### Cliente VALORES
* **Nodo Sensor NDR:** `valores-ndr`
* **Minion ID en Salt:** `ndr_sensor`
* **IP de Gestión (MGMT):** `192.168.40.232` (`eth0`)
* **Interfaz de Captura (Mirror SPAN):** `eth1` (`Wired connection 1` - Sin IP, Modo Promiscuo/NOARP)
* **Gateway:** `192.168.40.254` | **DNS:** `192.168.40.1` | **Dominio:** `VALORES.local`
* **Acceso SSH Sensor:** `ssh root@192.168.40.232` (Pass: `tempoPass26`)
* **Rol:** `SENSOR` (NDR dedicado: Zeek, Suricata, Stenographer; sin Elasticsearch local).
* **Scanner de Vulnerabilidades SOC:** `192.168.40.231` (Kali Linux - Usuario: `vulnscan` / Pass: `temporal26`)
* **Documentación Detallada:** [guia_despliegue_sensor_ndr_valores.md](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/03_Arquitectura_y_Despliegue/guia_despliegue_sensor_ndr_valores.md)

### 1. Orquestación y Conectividad (SaltStack)
Security Onion utiliza SaltStack para que el Manager controle a los Sensores de forma centralizada.

* **Validar conexión de toda la grilla:** `sudo salt '*' test.ping`
* **Forzar sincronización de configuración (Highstate):** `sudo salt '*' state.highstate`
* **Ejecutar un comando remoto en un sensor específico:** `sudo salt 'securityonion_sensor' cmd.run 'COMANDO_A_EJECUTAR'`

### 2. Diagnóstico de Salud (Contenedores)
En la v3, todos los servicios (Zeek, Suricata, Elasticsearch) corren como contenedores Docker.

* **Ver estado de los servicios (Local):** `sudo so-status`
* **Ver los logs de error de un contenedor específico:** `sudo docker logs <nombre_del_contenedor> --tail 50`
* **Reiniciar un contenedor específico:** `sudo docker restart <nombre_del_contenedor>`

### 3. Actualizaciones y Mantenimiento (SOUP)
SOUP (Security Onion UPdater) es la herramienta oficial para aplicar parches.

* **Actualizar el nodo local (Manager):** `sudo soup`
* **Comprobar si un nodo requiere reinicio:** `sudo so-status` (Mirar la línea `OS Uptime`).
* **Reiniciar un nodo remotamente desde el Manager:** `sudo salt '*sensor*' cmd.run 'reboot'`

### 4. Redes y Firewall (so-firewall)
En SO3 el firewall es estricto y bloquea todo por defecto.

* **Permitir acceso a una IP o rango nuevo:**
  ```bash
  # Para la interfaz Web / Consola Analyst / Open XDR (puertos 80, 443):
  sudo so-firewall includehost analyst TU_IP_O_CIDR

  # Para la API de Elasticsearch / OpenSearch (puerto 9200):
  sudo so-firewall includehost elasticsearch_rest TU_IP_O_CIDR

  # Para agentes de endpoint (Fleet / Elastic Agent, puerto 8220):
  sudo so-firewall includehost fleet TU_IP_O_CIDR

  # Para ingesta de Syslog perimetral (puertos 514, 5514, 5515):
  sudo so-firewall includehost syslog IP_DEL_FIREWALL
  sudo so-firewall apply

  # Si el firewall emite en puertos alternativos (ej. FortiGate en 5514/5515 UDP):
  # Añadir los puertos a /opt/so/saltstack/default/salt/firewall/defaults.yaml bajo 'syslog: udp:'
  # Luego propagar con: sudo salt '*' state.apply firewall
  ```
* **Archivo de definición de hostgroups:** `/opt/so/saltstack/local/pillar/firewall/soc_firewall.sls` y `/opt/so/saltstack/pillar/firewall/hostgroups.sls`
* **Definición de puertos oficiales (portgroups):** `/opt/so/saltstack/default/salt/firewall/defaults.yaml`
* **Eliminar acceso a una IP vieja:** `sudo so-firewall removehost IP_VIEJA`

### 5. Rendimiento de Linux (Básicos)
* **Ver uso de CPU y RAM en tiempo real:** `top` (Presiona `M` para ordenar por Memoria RAM).
* **Ver espacio en los discos:** `df -h`
* **Verificar si el sistema mató contenedores por falta de RAM (OOM Killer):** `dmesg -T | grep -i oom`

### 6. Mantenimiento de Elasticsearch (Disco y Shards)
En Security Onion 3, los comandos de Elasticsearch se envían con el wrapper oficial `so-elasticsearch-query`.

* **Identificar Shards No Asignados (UNASSIGNED) y su Causa:**
  ```bash
  sudo so-elasticsearch-query '_cat/shards?h=index,shard,prirep,state,unassigned.reason&s=state' | grep UNASSIGNED
  ```
* **Llevar Cluster Standalone a GREEN (Eliminar Réplicas Huérfanas de ElastAlert/Templates):**
  En despliegues con un solo nodo de datos (`Standalone`), cualquier índice con `number_of_replicas: 1` mantendrá el cluster en `yellow` y la Web en `Pending`. Se corrige fijando réplicas en 0:
  ```bash
  # Para un índice específico (ej. elastalert_status):
  sudo so-elasticsearch-query 'elastalert_status/_settings' -X PUT -d '{"index": {"number_of_replicas": 0}}'

  # Para todos los índices del nodo Standalone:
  sudo so-elasticsearch-query '*/_settings' -X PUT -d '{"index": {"number_of_replicas": 0}}'
  ```
* **Subir el límite de pánico del disco (Watermark) temporalmente (Ej: 95%):**
  ```bash
  sudo so-elasticsearch-query _cluster/settings -X PUT -d '{ "persistent": { "cluster.routing.allocation.disk.watermark.low": "90%", "cluster.routing.allocation.disk.watermark.high": "95%", "cluster.routing.allocation.disk.watermark.flood_stage": "97%", "cluster.info.update.interval": "1m" } }'
  ```
* **Romper los candados de Solo-Lectura de todos los índices:**
  ```bash
  sudo so-elasticsearch-query "_all/_settings" -X PUT -d '{"index.blocks.read_only_allow_delete": null}'
  ```


### 7. Troubleshooting de Elastic Agent (Windows)
* **Reiniciar el servicio a la fuerza (Abrir PowerShell como Administrador):** `Restart-Service "Elastic Agent" -Force`
* **Verificar el estado exacto de la conexión interna:** `& "C:\Program Files\Elastic\Agent\elastic-agent.exe" status`

### 8. Auditoría Forense de Retención y Purgado de Índices (ILM/Disco)
* **Listar los índices activos actualmente:** `sudo so-elasticsearch-query "_cat/indices?v&s=index"`
* **Revisar el historial de operaciones de borrado del ILM:** `sudo so-elasticsearch-query ".ilm-history-*/_search?q=action:delete&sort=@timestamp:desc&size=5" | grep -i "index"`
* **Consultar el límite real asignado para Logs (LOG_SIZE_LIMIT):** `cat /opt/so/log/elasticsearch/so-elasticsearch-indices-delete.log`

### 9. Procedimiento Estandarizado de Despliegue de Sensores Distribuidos (Playbook Rápido)
Para garantizar que futuros despliegues en nuevos clientes se ejecuten sin fricción, seguir estrictamente este orden:

0. **Calibración Previa de Red en el Sensor (Lección Aprendida Crítica):**
   * **Regla de Oro:** Un puerto Mirror/SPAN **NUNCA** debe tener dirección IP ni DHCP asignado. Debe operar en modo promiscuo y `NOARP` (evidencia forense validada en `securityonion_sensor`: `ens33` UP sin IP).
   * Si la tarjeta mirror tiene IP por DHCP, secuestrará la ruta por defecto (`default gateway`) y `so-setup` abortará con `[ERROR] Main IP mismatch`.
   * **Comandos de preparación antes de instalar:**
     ```bash
     # Fijar IP estática y Gateway en la tarjeta de Gestión (ej. eth0):
     nmcli con mod eth0 ipv4.addresses <IP_MGMT>/24 ipv4.gateway <GATEWAY> ipv4.dns "<DNS1> <DNS2>" ipv4.method manual
     nmcli con up eth0

     # Deshabilitar IP en la tarjeta de Monitoreo / Mirror (ej. eth1 / Wired connection 1):
     nmcli con mod "Wired connection 1" ipv4.method disabled ipv6.method disabled
     nmcli con down "Wired connection 1" && nmcli con up "Wired connection 1"

     # Validar que la ruta por defecto salga por la IP de gestión:
     ip route get 172.17.10.25
     ```

1. **Habilitación en Firewall del Manager (`soc-onion`):**
   ```bash
   sudo so-firewall includehost sensor <IP_GESTION_CLIENTE>
   sudo so-firewall apply
   ```

2. **Matriz Oficial de Conectividad y Puertos (Sensor <-> Manager):**

   | Protocolo | Puerto Destino | Sentido | Servicio / Función Oficial |
   | :--- | :--- | :--- | :--- |
   | **ICMP** | N/A | Saliente | Diagnóstico y monitoreo de conectividad (Echo / Ping) |
   | **TCP** | `80` | Saliente | Redirección HTTP y verificación web inicial |
   | **TCP** | `443` | Bidireccional | HTTPS / Grid API (Descarga de certificados y configuración) |
   | **TCP** | `22` | Entrante (Mgr -> Sensor) | SSH Administración y soporte remoto del SOC al sensor |
   | **TCP** | `4505` | Saliente | SaltStack Publisher (Recepción de comandos y tareas del cluster) |
   | **TCP** | `4506` | Saliente | SaltStack Return (Devolución de telemetría y ejecución de Salt) |
   | **TCP** | `5000` | Saliente | Docker Registry interno (Descarga de contenedores oficiales) |
   | **TCP** | `5055` | Saliente | Salt API / Health Check de la grilla |
   | **TCP** | `8086` | Saliente | InfluxDB (Telemetría de métricas y salud del sensor - Telegraf) |
   | **TCP** | `8220` | Saliente | Logstash Pipeline / Fleet (Transmisión de eventos Zeek y Suricata) |
   | **TCP** | `8443` | Saliente | Elasticsearch / OpenSearch API (Indexación directa de alertas) |
   | **TCP** | `9200` | Saliente | Elasticsearch / OpenSearch REST API |

   *Script de validación rápida desde el sensor:*
   ```bash
   for p in 80 443 4505 4506 5000 5055 8086 8220 8443 9200; do nc -zv -w 2 172.17.10.25 $p; done
   ```
   *(Nota crítica: El puerto `8086/TCP` hacia InfluxDB es indispensable para que Telegraf transmita el estado de los contenedores y recursos; si está bloqueado en el firewall perimetral, `Process Status` figurará como `unknown` y la tabla de contenedores permanecerá vacía).*


3. **Ejecución del Asistente en el Sensor:**
   * **Ruta y comando obligatorio:**
     ```bash
     cd /root/SecurityOnion/setup
     ./so-setup iso
     ```
   * **Flujo interactivo:** `Install` -> `DISTRIBUTED` -> `Existing Deployment` -> `SENSOR`.
   * **Reconfigurar Gestión:** Responder **`<No>`** (la red ya quedó calibrada en el paso 0).
   * **Interfaz de Captura / Sniffing:** Seleccionar la interfaz sin IP (ej. `eth1`).
   * **Manager IP:** `172.17.10.25`.

4. **Autorización en el Manager (`soc-onion`):**
   ```bash
   sudo salt-key -L
   sudo salt-key -a <minion_id> -y
   sudo salt '<minion_id>' test.ping
   ```

5. **Creación de Pillars Privados y Despliegue de Contenedores (Highstate):**
   * El compilador exige la existencia de `<minion_id>.sls` y `adv_<minion_id>.sls` en `/opt/so/saltstack/local/pillar/minions/`:
   ```bash
   # 1. Crear adv_<minion_id>.sls vacío y configurar <minion_id>.sls con mainint, mainip e interface bond0:
   sudo touch /opt/so/saltstack/local/pillar/minions/adv_<minion_id>.sls
   sudo chown socore:socore /opt/so/saltstack/local/pillar/minions/*<minion_id>*.sls
   sudo chmod 640 /opt/so/saltstack/local/pillar/minions/*<minion_id>*.sls

   # 2. Inyectar startup_states para evitar fallo en enable_startup_states (Lección Aprendida #5):
   sudo salt '<minion_id>' cmd.run 'echo "startup_states: highstate" >> /etc/salt/minion'

   # 3. Refrescar variables y compilar el despliegue de motores Docker (100% de éxito garantizado):
   sudo salt '<minion_id>' saltutil.refresh_pillar
   sudo salt '<minion_id>' state.highstate
   ```
