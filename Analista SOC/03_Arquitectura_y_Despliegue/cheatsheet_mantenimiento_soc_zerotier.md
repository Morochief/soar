# 🛠️ Cheat Sheet Maestro: Operaciones, Mantenimiento y Consultas
## Security Onion Grid Distribuido sobre ZeroTier Overlay Network

**Versión:** 1.0 (Producción)  
**Entorno:** Manager Central (`soc-onion`) ⇄ Search Node Remoto (`secops-vascol`)  
**Túnel:** ZeroTier Network `743993800f52cd35` (Puerto 19993)

---

## 📌 1. Ficha Rápida de Identificadores y Parámetros

| Parámetro | Manager Central (`soc-onion`) | Search Node Cliente (`secops-vascol`) |
| :--- | :--- | :--- |
| **IP Red Local (LAN)** | `172.17.10.25` | `192.168.225.26` |
| **IP ZeroTier (Overlay)** | **`10.92.248.203`** | **`10.92.248.156`** |
| **Rol en SO** | Standalone / Master | Search Node (Data + Ingesta Syslog) |
| **Puerto ZeroTier** | `19993` (Alternativo por Zeek) | `9993` (Estándar) |
| **Puertos Críticos** | `443` (Web/API), `4505/6` (Salt), `9300` (ES), `5055` (Logstash), `8220` (Fleet), `8443` (Artifacts) | `9300` (ES Transporte), `4505/6` (Salt Minion), `514` (Syslog UDP/TCP) |
| **Emisores Perimetrales** | N/A | FortiGate 60F (`192.168.110.1`, devname `VASCOL`) |

---

## ⚡ 2. Chequeo de Salud Express (Health Check en 30 Segundos)

### En el Manager Central (`soc-onion`):
```bash
# 1. Estado de todos los contenedores Docker de Security Onion
sudo so-status

# 2. Salud del clúster de Elasticsearch (Debe responder status: green)
sudo so-elasticsearch-query '_cluster/health?pretty'

# 3. Verificar túnel ZeroTier (Debe decir OK y mostrar la IP 10.92.248.203)
sudo zerotier-cli -p19993 listnetworks

# 4. Probar si el cliente remoto responde en el puerto de Elasticsearch
nc -zv -w 2 10.92.248.156 9300
```

### En el Search Node Remoto (`secops-vascol`):
```bash
# 1. Estado de servicios locales de Security Onion
sudo so-status

# 2. Estado de Elastic Agent y Fleet (Debe decir HEALTHY Running / Connected)
sudo /opt/Elastic/Agent/elastic-agent status

# 3. Comprobar que el DNAT redirige hacia el Manager en 0.01s
nc -zv -w 2 172.17.10.25 8443
nc -zv -w 2 172.17.10.25 5055

# 4. Comprobar ingesta Syslog sin bloqueos (Debe retornar 0 drops en puerto 514)
sudo tail -n 50 /var/log/messages | grep "DPT=514"
sudo tcpdump -nn -c 3 -i any udp port 514
```

---

## 🌐 3. Comandos de ZeroTier (Gestión de Túnel SD-WAN)

> [!WARNING]
> En el Manager `soc-onion`, ZeroTier corre en el puerto **19993**. Siempre debe usarse `-p19993`.

```bash
# MANAGER: Ver estado del servicio
sudo zerotier-cli -p19993 status

# MANAGER: Ver redes conectadas y estado de autenticación (OK / ACCESS_DENIED)
sudo zerotier-cli -p19993 listnetworks

# MANAGER: Ver clientes remotos conectados directamente al Manager
sudo zerotier-cli -p19993 listpeers | grep -E "10.92.248|DIRECT"

# CLIENTE: Ver redes conectadas
sudo zerotier-cli listnetworks

# AMBOS: Reinicio limpio en caso de corte o bloqueo de red
sudo systemctl restart zerotier-one
```

---

## 🔍 4. Elasticsearch & Shards: Comandos Esenciales de Monitoreo

Todos estos comandos se ejecutan desde el **Manager Central (`soc-onion`)**:

```bash
# 1. Ver los nodos que componen el clúster, roles y consumo de RAM/Heap
sudo so-elasticsearch-query '_cat/nodes?v'

# 2. Ver distribución de shards y almacenamiento usado por cada nodo
sudo so-elasticsearch-query '_cat/allocation?v'

# 3. Ver si existen shards sin asignar o con fallas (Debe devolver 0 líneas)
sudo so-elasticsearch-query '_cat/shards?h=index,shard,prirep,state,unassigned.reason&v' | grep UNASSIGNED

# 4. Ver los 15 índices con mayor volumen de documentos
sudo so-elasticsearch-query '_cat/indices?v&s=docs.count:desc' | head -n 15

# 5. Contar total de logs recibidos hoy desde secops-vascol en syslog
sudo so-elasticsearch-query '.ds-logs-system.syslog-*/_count?q=host.name:secops-vascol&pretty'

# 6. Ver el último log crudo recibido del cliente secops-vascol
sudo so-elasticsearch-query '.ds-logs-system.syslog-*/_search?q=host.name:secops-vascol&size=1&sort=@timestamp:desc&pretty'

# 7. Forzar reintento de asignación si algún shard quedara bloqueado
sudo so-elasticsearch-query '_cluster/reroute?retry_failed=true' -X POST
```

---

## 🧂 5. SaltStack: Control y Compilación Permanente (Anti-Highstate)

Se ejecutan en el **Manager Central (`soc-onion`)**:

```bash
# 1. Probar conectividad Salt con todos los nodos (Debe devolver True)
sudo salt '*' test.ping

# 2. Ver si hay tareas o Highstates ejecutándose en este momento
sudo salt-run jobs.active

# 3. Consultar qué valor de Pillar tiene cargado un nodo sin entrar en él
sudo salt 'secops-vascol*' pillar.get global:url_base
sudo salt 'secops-vascol*' pillar.get elasticsearch:nodes
sudo salt 'secops-vascol*' pillar.get esheap

# 4. Refrescar la base de datos de Pillars en todos los servidores
sudo salt-call saltutil.refresh_pillar
sudo salt '*' saltutil.refresh_pillar

# 5. Reaplicar estados específicos (sin reiniciar todo el servidor):
#    - Aplicar configuración de Sensoroni en el cliente:
sudo salt 'secops-vascol*' state.apply sensoroni

#    - Aplicar configuración de Elasticsearch en el cliente:
sudo salt 'secops-vascol*' state.apply elasticsearch

#    - Aplicar firewall nativo en el cliente (regenera DOCKER-USER):
sudo salt 'secops-vascol*' state.apply firewall

#    - Aplicar certificados y configuración de NGINX en el Manager:
sudo salt-call state.apply nginx
```

---

## 🤖 6. Elastic Agent y Fleet (Supervisión de Endpoints)

Se ejecutan en el **Search Node Remoto (`secops-vascol`)**:

```bash
# 1. Ver estado completo del agente y componentes (filebeat, osquery, metricbeat)
sudo /opt/Elastic/Agent/elastic-agent status

# 2. Ver la versión en ejecución del binario y del daemon supervisor
sudo /opt/Elastic/Agent/elastic-agent version

# 3. Monitorear logs activos del agente en vivo
sudo tail -f /opt/Elastic/Agent/data/elastic-agent-*/logs/elastic-agent-*.ndjson

# 4. Ver si hay conexiones activas hacia Fleet (8220) o descargas (8443)
sudo ss -tp | grep -E "8220|8443"

# 5. Reiniciar el agente de Elastic
sudo systemctl restart elastic-agent

# 6. Inspeccionar el archivo de estado encriptado del agente
sudo ls -lh /opt/Elastic/Agent/data/elastic-agent-*/state.enc
```

---

## 🛡️ 7. Redirección Transparente (DNAT/MASQUERADE) y Firewall

### En el Cliente Remoto (`secops-vascol`):
```bash
# 1. Ver si las reglas de redirección están activas en la tabla NAT
sudo iptables -t nat -S | grep 10.92.248.203

# 2. Si las reglas no están, re-ejecutar el script de persistencia
sudo /usr/local/bin/so-zt-nat.sh

# 3. Comprobar el servicio systemd de arranque
sudo systemctl status so-zt-nat.service

# 4. Verificar la tarea en crontab que auto-corrige cada 60 segundos
sudo crontab -l | grep so-zt-nat
```

### En el Manager Central (`soc-onion`):
```bash
# 1. Autorizar una nueva IP en el puerto 443 Web/API
sudo so-firewall includehost analyst <NUEVA_IP>
sudo so-firewall apply

# 2. Autorizar un nuevo minion remoto con su rol
sudo so-firewall-minion --role=SEARCHNODE --ip=<NUEVA_IP_ZT>

# 3. Ver reglas de firewall generadas por Security Onion
sudo iptables -S DOCKER-USER | grep 9300

# 4. GESTIÓN SYSLOG (SO 2.4): Autorizar IP emisora de logs de red (FortiGate / Switches)
#    Nota: 'so-allow' está deprecado en SO 2.4; usar 'so-firewall' en el Manager:
sudo so-firewall includehost syslog 192.168.110.1

# 5. Aplicar la regla de firewall en el Minion Search Node remoto vía Salt:
sudo salt 'secops-vascol_searchnode' state.apply firewall
```

---

## 🔎 8. Consultas KQL / Lucene Listas para Copiar y Pegar (Hunt / Kibana)

Usa estas consultas en la barra de búsqueda de **Hunt** (`/#/hunt`) o **Kibana**:

| Objetivo de Búsqueda | Sintaxis KQL / Filtro |
| :--- | :--- |
| **Ingesta de Firewall FortiGate (Sucursal VASCOL)** | `data_stream.dataset: "syslog.syslog"` o `message: "*VASCOL*"` |
| **Tráfico FortiGate capturado en el Search Node** | `host.name: "secops-vascol" AND data_stream.dataset: "syslog.syslog"` |
| **Filtrar por dispositivo perimetral (Serial FGT60F)** | `message: "*FGT60FTK2209H6JM*"` |
| **Auditoría Interna del OS Linux (secops-vascol)** | `host.name: "secops-vascol" AND data_stream.dataset: "system.syslog"` |
| **Aislar todo el tráfico de este cliente (Global)** | `host.name: "secops-vascol"` |
| **Ver solo auditoría de comandos (sudo)** | `host.name: "secops-vascol" AND process.name: "sudo"` |
| **Ver logins y sesiones SSH** | `host.name: "secops-vascol" AND process.name: ("sshd" or "systemd-logind")` |
| **Buscar errores o caídas en el nodo** | `host.name: "secops-vascol" AND log.level: ("error" or "fatal")` |
| **Ver el evento de prueba inyectado** | `process.name: "SOC_TEST"` o `message: "*Prueba de ingesta*"` |
| **Excluir a este cliente del tablero** | `NOT host.name: "secops-vascol"` |
| **Filtrar por la IP de túnel del cliente** | `metadata.input.beats.host.ip: "10.92.248.156"` |

---

## 🚨 9. Protocolo de Rescate Rápido (Si algo falla, corre esto)

### Escenario A: "El nodo secops-vascol desapareció del Grid Web"
* **Causa:** El Highstate pisó `url_base` o el contenedor de Sensoroni se detuvo.
* **Solución (En el Manager):**
  ```bash
  sudo salt 'secops-vascol*' state.apply sensoroni
  sudo salt 'secops-vascol*' cmd.run 'docker restart so-sensoroni'
  sudo salt 'secops-vascol*' cmd.run 'tail -n 5 /opt/so/log/sensoroni/sensoroni.log'
  ```

### Escenario B: "El clúster de Elasticsearch se puso en YELLOW o RED"
* **Causa:** El puerto 9300 fue bloqueado o no puede comunicarse por ZeroTier.
* **Solución (En el Manager):**
  ```bash
  sudo salt 'secops-vascol*' state.apply firewall
  sudo salt 'secops-vascol*' state.apply elasticsearch
  sudo so-elasticsearch-query '_cluster/health?pretty'
  ```

### Escenario C: "Elastic Agent en el cliente dice DOWNLOADING (0%) o UPGRADE FAILED"
* **Causa:** Faltan las reglas de DNAT o faltó el archivo `.asc`.
* **Solución (En el Cliente):**
  ```bash
  sudo /usr/local/bin/so-zt-nat.sh
  sudo curl -o /opt/Elastic/Agent/data/elastic-agent-*/downloads/elastic-agent-9.3.3+build202604082258-linux-x86_64.tar.gz.asc http://10.92.248.203:8443/artifacts/beats/elastic-agent/elastic-agent-9.3.3+build202604082258-linux-x86_64.tar.gz.asc
  sudo systemctl restart elastic-agent
  ```

### Escenario D: "El nodo remoto no ingesta los logs del Firewall FortiGate (Dropping UDP 514)"
* **Causa:** El kernel de `secops-vascol` descarta los paquetes (`IPTables-dropped: IN=ens32 ... PROTO=UDP DPT=514`) porque la IP del firewall emisor (`192.168.110.1`) no ha sido autorizada en el hostgroup `syslog` de Security Onion o el estado de Salt no se ha aplicado al minion.
* **Solución (En el Manager Central):**
  ```bash
  # 1. Autorizar la IP en el grupo syslog:
  sudo so-firewall includehost syslog 192.168.110.1

  # 2. Empujar y forzar la regla de firewall al Search Node remoto:
  sudo salt 'secops-vascol_searchnode' state.apply firewall
  ```
* **Verificación:**
  ```bash
  # En el Search Node: confirmar 0 paquetes descartados
  sudo tail -n 20 /var/log/messages | grep "DPT=514"
  # En el Manager: verificar el dataset syslog.syslog en Elasticsearch
  sudo so-elasticsearch-query '.ds-logs-syslog-so-*/_search?q=message:VASCOL&size=1&pretty'
  ```

---

## 📂 10. Mapa de Rutas de Archivos Críticos

```text
MANAGER (soc-onion):
├── /opt/so/saltstack/local/pillar/minions/soc-onion_standalone.sls    <-- alt_names NGINX
├── /opt/so/saltstack/local/pillar/minions/secops-vascol_searchnode.sls <-- url_base y esheap
├── /opt/so/saltstack/local/pillar/elasticsearch/adv_elasticsearch.sls <-- Mapeo IPs 9300
├── /opt/so/saltstack/local/pillar/firewall/soc_firewall.sls          <-- Hostgroups de firewall (syslog, analyst, etc)
├── /var/lib/zerotier-one/local.conf                                  <-- Puerto 19993
└── /opt/so/log/                                                      <-- Logs del sistema

CLIENTE (secops-vascol):
├── /usr/local/bin/so-zt-nat.sh                                       <-- Script DNAT/MASQUERADE
├── /etc/systemd/system/so-zt-nat.service                             <-- Servicio persistencia boot
├── /opt/Elastic/Agent/elastic-agent.yml                              <-- Configuración del agente
├── /opt/Elastic/Agent/data/elastic-agent-9.3.3.../                   <-- Directorio versión activa
├── /etc/sysconfig/iptables                                           <-- Reglas persistidas generadas por Salt
└── /var/log/messages                                                 <-- Auditoría de kernel y drops (IPTables-dropped)
```
