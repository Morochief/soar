# Procedimiento Operativo Estándar (SOP)
## Despliegue de Nodos Remotos de Security Onion (Sensores / Search Nodes) vía ZeroTier Overlay Network

**Versión:** 2.0 (Flujo de Instalación Definitivo con SaltStack Integrado)  
**Autor / Equipo:** SOC & SecOps  
**Revisado:** Implementación en Producción (`soc-onion` y `secops-vascol`)

---

## 1. Arquitectura y Topología de Red

Cuando se despliega un nodo distribuido de Security Onion (Sensor o Search Node) en un cliente remoto o en otra sucursal, la comunicación entre el nodo (Minion/Salt) y el Manager central debe ser directa, cifrada y resistente a reescrituras automáticas de configuración.

En lugar de exponer puertos críticos a Internet pública o configurar complejas VPNs IPSec sitio a sitio, se utiliza una **Overlay Network (SD-WAN)** mediante **ZeroTier**.

```
+------------------------------------+                  +------------------------------------+
|     SECURITY ONION MANAGER         |                  |        CLIENTE REMOTO              |
|        (soc-onion)                 |                  |      (secops-vascol)               |
|                                    |                  |                                    |
|  LAN Interna: 172.17.10.25         |                  |  LAN Cliente: 192.168.225.26       |
|  ZeroTier IP: 10.92.248.203        |<================>|  ZeroTier IP: 10.92.248.156        |
|  ZT Network:  743993800f52cd35     |    Túnel Cifrado |  ZT Network:  743993800f52cd35     |
|  Servicios:   Salt Master (4505/6) |      ZeroTier    |  Rol:         SEARCHNODE + SYSLOG  |
|               NGINX / SOC (443)    |   (Puerto 19993) |                                    |
+------------------------------------+                  +-----------------+------------------+
                                                                          ^
                                                                          | Syslog UDP/514
                                                                          | (Tráfico Perimetral)
                                                        +-----------------+------------------+
                                                        |      FIREWALL SUCURSAL             |
                                                        |   FortiGate 60F ("VASCOL")         |
                                                        |   IP LAN: 192.168.110.1            |
                                                        |   S/N: FGT60FTK2209H6JM            |
                                                        +------------------------------------+
```

---

## 2. Parámetros del Entorno de Referencia

| Componente | Hostname / Dispositivo | IP Red Local | IP ZeroTier | Rol / Función |
| :--- | :--- | :--- | :--- | :--- |
| **Manager Central** | `soc-onion` | `172.17.10.25` | `10.92.248.203` | Standalone Master / Fleet / Grid Manager |
| **Nodo Remoto** | `secops-vascol` | `192.168.225.26` | `10.92.248.156` | Search Node (Almacenamiento) + Sensor Syslog Branch |
| **Firewall Perimetral**| FortiGate 60F (`VASCOL`)| `192.168.110.1` | N/A (Red Sucursal) | Emisor Syslog (Tráfico de red, NAT, DNS, Bloqueos) |
| **Red ZeroTier ID** | Overlay SD-WAN | `743993800f52cd35` | Puerto ZT Manager: `19993` | Túnel encriptado punto a punto |

---

## 3. Fase I: Preparación del Manager Central (`soc-onion`)

> [!IMPORTANT]
> **El Conflicto Crítico de Puertos (Zeek vs ZeroTier):**
> Por defecto, ZeroTier utiliza los puertos UDP/TCP **9993** y **9994**. Sin embargo, Security Onion tiene el motor de captura de tráfico **Zeek** escuchando en los puertos `9993` y `9994`. Si no se cambia el puerto de ZeroTier en el Manager, el servicio `zerotier-one` fallará con error `EXCEPTION (255)`.

### 1.1 Instalar ZeroTier en el Manager
```bash
curl -s https://install.zerotier.com | sudo bash
```

### 1.2 Configurar ZeroTier en el puerto alternativo (19993)
```bash
# 1. Definir puerto en local.conf
sudo bash -c 'cat <<EOF > /var/lib/zerotier-one/local.conf
{
  "settings": {
    "primaryPort": 19993
  }
}
EOF'

# 2. Configurar el override de arranque en systemd
sudo mkdir -p /etc/systemd/system/zerotier-one.service.d
sudo bash -c 'cat <<EOF > /etc/systemd/system/zerotier-one.service.d/override.conf
[Service]
ExecStart=
ExecStart=/usr/sbin/zerotier-one -p19993
EOF'

# 3. Informar al CLI el puerto asignado
sudo bash -c 'echo "19993" > /var/lib/zerotier-one/zerotier-one.port'

# 4. Recargar systemd y reiniciar ZeroTier
sudo systemctl daemon-reload
sudo systemctl reset-failed zerotier-one
sudo systemctl restart zerotier-one
```

### 1.3 Unir el Manager a la Red ZeroTier y fijar IP
```bash
sudo zerotier-cli -p19993 join 743993800f52cd35
```
1. En la consola web de **ZeroTier Central**, marca **Auth** en el Node ID del Manager.
2. Asigna la IP fija deseada (ejemplo: `10.92.248.203`).
3. Verifica el estado en el Manager:
   ```bash
   sudo zerotier-cli -p19993 listnetworks
   ```

### 1.4 [PROACTIVO / OBLIGATORIO] Registrar la IP ZeroTier en NGINX de forma permanente
> [!NOTE]
> Para evitar que el servidor web NGINX del Manager rechace a los clientes remotos con una redirección HTTP 307 a la IP local inalcanzable, configuramos la IP de ZeroTier en el Pillar de NGINX **desde el primer momento**.

En la terminal del Manager, ejecutar:
```bash
# Agregar la IP ZeroTier en alt_names del Pillar del Manager
sudo python3 -c "
path = '/opt/so/saltstack/local/pillar/minions/soc-onion_standalone.sls'
with open(path, 'r') as f:
    content = f.read()

target = 'nginx:\n    enabled: true'
replacement = '''nginx:
    enabled: true
    ssl:
        alt_names:
            - \'10.92.248.203\''''

if 'alt_names' not in content:
    new_content = content.replace(target, replacement)
    with open(path, 'w') as f:
        f.write(new_content)
    print('[+] Pillar de NGINX actualizado con alt_names exitosamente.')
else:
    print('[i] alt_names ya configurado.')
"

# Compilar los certificados y la configuración de NGINX
sudo salt-call saltutil.refresh_pillar
sudo salt-call state.apply nginx
```
*(Esto agrega la IP de ZeroTier a la lista de nombres válidos de NGINX y a los certificados SSL sin alterar las IPs de los sensores de la red interna).*

---

## 4. Fase II: Configuración del Servidor Remoto en el Cliente (`secops-vascol`)

> [!NOTE]
> La instalación de ZeroTier se realiza **directamente en el servidor Linux** donde correrá Security Onion (no en la máquina Windows).

### 2.1 Conectarse por SSH al servidor del cliente
```bash
ssh soc@192.168.225.26
```

### 2.2 Instalar y unir ZeroTier
```bash
curl -s https://install.zerotier.com | sudo bash
sudo zerotier-cli join 743993800f52cd35
```

### 2.3 Autorización en consola ZeroTier
* En **ZeroTier Central**, marca la casilla **Auth** para el nuevo Node ID del cliente.
* Verifica en el cliente la IP asignada (ejemplo: `10.92.248.156`):
  ```bash
  sudo zerotier-cli listnetworks
  ```

---

## 5. Fase III: Apertura de Firewall en el Manager Central

> [!WARNING]
> El Manager bloquea todo tráfico entrante por defecto. Se deben abrir los puertos para la IP de ZeroTier del cliente antes de ejecutar el setup.

En la terminal del **Manager Central (`soc-onion`)**, ejecutar reemplazando por la IP ZeroTier del nuevo nodo:

### 3.1 Autorizar acceso Web / API (Puerto 443 HTTPS)
```bash
sudo so-firewall includehost analyst 10.92.248.156
sudo so-firewall apply
```

### 3.2 Autorizar el Rol del Minion (Salt 4505/4506, Elastic, Grid)
* **Si el nodo es SEARCHNODE:**
  ```bash
  sudo so-firewall-minion --role=SEARCHNODE --ip=10.92.248.156
  ```

* **Si el nodo es SENSOR:**
  ```bash
  sudo so-firewall-minion --role=SENSOR --ip=10.92.248.156
  ```

---

## 6. Fase IV: Validación de Conectividad Previa

Desde el **Nodo Remoto (`secops-vascol`)**, confirmar que el Manager responde:
```bash
curl -k https://10.92.248.203
```
*Si devuelve código HTTP 200 o HTML de NGINX, la red y el firewall están listos.*

---

## 7. Fase V: Ejecución de `sosetup` en el Nodo Remoto

En el servidor del cliente (`secops-vascol`), iniciar el instalador de Security Onion:
```bash
sudo sosetup
```

### Opciones durante el Asistente:
1. **Deployment Type:** Elegir `Existing Grid`.
2. **Node Role:** Seleccionar `Search Node` o `Sensor` según corresponda.
3. **Manager IP / Hostname:** Ingresar la IP ZeroTier del Manager:
   ```
   10.92.248.203
   ```
4. **Manager Credentials:** Ingresar el usuario administrador y contraseña de la interfaz Web de Security Onion.
5. **Confirmar:** Dejar que el asistente descargue los paquetes y complete la inicialización.
6. Presionar `TAB` y luego `ENTER` sobre `<Ok>` al finalizar.

---

## 8. Fase VI: Aceptación y Configuración Permanente (Post-Instalación Inmediata)

### 8.1 Aceptar el nodo en la Web del Manager
1. Abrir la interfaz web de Security Onion: `https://172.17.10.25` (o `https://10.92.248.203`).
2. Ir a: **Administration** -> **Grid Members**.
3. En **Pending Members**, ubicar el nuevo nodo (`secops-vascol`).
4. Hacer clic en **Review** y luego en **Accept**.

*(Opcional: puedes monitorear el progreso del despliegue en el Manager con `sudo salt-run jobs.active` y en el nodo con `sudo journalctl -u salt-minion -f`).*

---

### 8.2 [PASO CRÍTICO OBLIGATORIO] Fijar `url_base` en el Pillar del Cliente
> [!CAUTION]
> **¿Por qué este paso es obligatorio?**  
> Security Onion ejecuta un **Highstate** cada 15 minutos de forma automática. Si configuras la IP a mano en `sensoroni.json`, el Highstate la borrará a los 15 minutos y el nodo desaparecerá del Grid Web.  
> Al escribir la IP en el Pillar del cliente, el cambio se vuelve **permanente e inmune al Highstate**.

Una vez aceptado el nodo, ejecutar **en el Manager Central**:

```bash
# 1. Agregar el override de url_base en la libreta privada del nuevo nodo
sudo bash -c 'cat <<EOF >> /opt/so/saltstack/local/pillar/minions/secops-vascol_searchnode.sls

global:
  url_base: "10.92.248.203"
EOF'

# 2. Refrescar el caché de Pillar en el cliente
sudo salt 'secops-vascol*' saltutil.refresh_pillar

# 3. Compilar el estado de Sensoroni para que use la IP de ZeroTier
sudo salt 'secops-vascol*' state.apply sensoroni

# 4. Reiniciar el contenedor de Sensoroni en el cliente
sudo salt 'secops-vascol*' cmd.run 'docker restart so-sensoroni'
```

---

### 8.3 [PASO OBLIGATORIO PARA SEARCH NODES] Configurar el Cluster de Elasticsearch (Puerto 9300)

> [!IMPORTANT]
> **¿Por qué este paso es necesario en Search Nodes?**  
> Si el nodo remoto tiene el rol de **Search Node**, almacena y busca datos en Elasticsearch. Elasticsearch requiere comunicarse de forma bidireccional con el Manager en el puerto de transporte **9300**.  
> Por defecto, los contenedores Docker de Elasticsearch mapean los hostnames con las IPs de red local (`172.17.10.25` y `192.168.225.26`). Para que el cluster se una a través de ZeroTier, se debe registrar el mapeo en el Pillar de Elasticsearch y autorizar el puerto 9300 en el firewall del cliente.

Ejecutar en el **Manager Central (`soc-onion`)**:

```bash
# 1. Asignar 2 GB de RAM a Elasticsearch en el Search Node (para evitar OOM con shards)
sudo sed -i "s/esheap: '600m'/esheap: '2g'/g" /opt/so/saltstack/local/pillar/minions/secops-vascol_searchnode.sls

# 2. Agregar la IP ZeroTier del Manager al grupo 'standalone' del Firewall
sudo python3 -c "
path = '/opt/so/saltstack/local/pillar/firewall/soc_firewall.sls'
with open(path, 'r') as f:
    content = f.read()

target = '    standalone:\n    - 172.17.10.25'
replacement = '    standalone:\n    - 172.17.10.25\n    - 10.92.248.203'

if '10.92.248.203' not in content:
    new_content = content.replace(target, replacement)
    with open(path, 'w') as f:
        f.write(new_content)
    print('[+] Firewall Pillar actualizado con éxito.')
"

# 3. Definir las IPs de ZeroTier en el Pillar de Elasticsearch (adv_elasticsearch.sls)
sudo bash -c 'cat <<EOF > /opt/so/saltstack/local/pillar/elasticsearch/adv_elasticsearch.sls
elasticsearch:
  nodes:
    searchnode:
      secops-vascol:
        ip: 10.92.248.156
    standalone:
      soc-onion:
        ip: 10.92.248.203
EOF'

# 4. Refrescar los Pillars en ambos servidores
sudo salt-call saltutil.refresh_pillar
sudo salt 'secops-vascol*' saltutil.refresh_pillar

# 5. Aplicar Firewall nativo en el cliente (genera DOCKER-USER automáticamente)
sudo salt 'secops-vascol*' state.apply firewall

# 6. Aplicar Elasticsearch en el cliente y en el Manager
sudo salt 'secops-vascol*' state.apply elasticsearch
sudo salt-call state.apply elasticsearch
```

#### Verificación del Cluster:
En cualquiera de los dos servidores, ejecutar:
```bash
sudo so-elasticsearch-query '_cat/nodes?v'
```
**Salida esperada (Ambos nodos unidos):**
```text
ip            heap.percent ram.percent cpu load_1m load_5m load_15m node.role master name
10.92.248.156           86          98  47    2.26    1.13     0.46 dhit      -      secops-vascol
10.92.248.203           45          98  37    4.03    3.07     2.27 dhimrt    *      soc-onion
```

---

---

### 8.4 [PASO RECOMENDADO] Enrutamiento Transparente hacia Servicios de Fleet y Logstash (NAT / MASQUERADE)

> [!TIP]
> **¿Por qué este paso previene errores en Elastic Agent y Filebeat?**  
> El agente de Elastic (`elastic-agent`) y Filebeat son aprovisionados centralmente por Fleet con la IP interna del Manager (`172.17.10.25:5055` para ingesta de Logstash y `http://172.17.10.25:8443` para descarga de actualizaciones).  
> Para evitar que fallen con *timeout* al buscar la IP local inalcanzable, se configuran dos reglas en la tabla `nat` de iptables en el nodo cliente:
> 1. **DNAT:** Redirige cualquier petición saliente hacia la IP LAN del Manager (`172.17.10.25`) hacia su IP ZeroTier (`10.92.248.203`).
> 2. **MASQUERADE:** Enmascara la IP de origen con la IP de ZeroTier del cliente (`10.92.248.156`), permitiendo que el tráfico fluya limpiamente a través del túnel sin ser descartado.

Ejecutar en el **Nodo Remoto (`secops-vascol`)**:
```bash
# 1. Redirigir destino a la IP ZeroTier del Manager (PREROUTING para Docker y OUTPUT para procesos locales)
sudo iptables -t nat -A PREROUTING -d 172.17.10.25 -j DNAT --to-destination 10.92.248.203
sudo iptables -t nat -A OUTPUT -d 172.17.10.25 -j DNAT --to-destination 10.92.248.203

# 2. Enmascarar origen con la IP de la interfaz ZeroTier
sudo iptables -t nat -A POSTROUTING -d 10.92.248.203 -j MASQUERADE

# 4. Crear script y servicio Systemd para persistencia garantizada en cada arranque
sudo bash -c 'cat << "EOF" > /usr/local/bin/so-zt-nat.sh
#!/usr/bin/env bash
/usr/sbin/iptables -t nat -C PREROUTING -d 172.17.10.25 -j DNAT --to-destination 10.92.248.203 2>/dev/null || /usr/sbin/iptables -t nat -A PREROUTING -d 172.17.10.25 -j DNAT --to-destination 10.92.248.203
/usr/sbin/iptables -t nat -C OUTPUT -d 172.17.10.25 -j DNAT --to-destination 10.92.248.203 2>/dev/null || /usr/sbin/iptables -t nat -A OUTPUT -d 172.17.10.25 -j DNAT --to-destination 10.92.248.203
/usr/sbin/iptables -t nat -C POSTROUTING -d 10.92.248.203 -j MASQUERADE 2>/dev/null || /usr/sbin/iptables -t nat -A POSTROUTING -d 10.92.248.203 -j MASQUERADE
EOF'

sudo chmod +x /usr/local/bin/so-zt-nat.sh

sudo bash -c 'cat <<EOF > /etc/systemd/system/so-zt-nat.service
[Unit]
Description=Security Onion ZeroTier DNAT Redirect
After=network.target zerotier-one.service

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/local/bin/so-zt-nat.sh

[Install]
WantedBy=multi-user.target
EOF'

sudo systemctl daemon-reload
sudo systemctl enable --now so-zt-nat.service

# 5. [GARANTÍA ANTI-HIGHSTATE] Ejecutar en crontab cada minuto por si SaltStack resetea iptables
(sudo crontab -l 2>/dev/null; echo "* * * * * /usr/local/bin/so-zt-nat.sh >/dev/null 2>&1") | sudo crontab -
```

---

### 8.5 Verificación de Éxito en Vivo

1. **Sensoroni (Heartbeat hacia el Manager):**
   ```bash
   sudo salt 'secops-vascol*' cmd.run 'tail -n 10 /opt/so/log/sensoroni/sensoroni.log'
   ```
   *(Debe mostrar respuestas `"status":"200 OK"` periódicas).*

2. **Elasticsearch Cluster (Salud del Cluster):**
   ```bash
   sudo so-elasticsearch-query '_cluster/health?pretty'
   ```
   *(Debe mostrar `"status" : "green"` con `"number_of_nodes" : 2` y 100% de shards activos).*

3. **Conexión Directa de Logstash (5055) y Fleet Registry (8443):**
   ```bash
   nc -zv 172.17.10.25 5055
   curl -I http://172.17.10.25:8443/artifacts/beats/elastic-agent/elastic-agent-9.3.3+build202604082258-linux-x86_64.tar.gz
   ```
   *(Ambos deben responder instantáneamente con `Connected` y `HTTP/1.1 200 OK`).*

4. **Consola Web Grid:**
   Recargar la consola Web con `Ctrl + F5` en `https://172.17.10.25/#/grid`. El nodo `secops-vascol` debe figurar activo, con todos sus servicios en verde permanentemente.

---

## 9. Inventario Maestro de Persistencia contra Highstates (Los 7 Pilares Definitivos)

Security Onion ejecuta automáticamente la tarea programada `highstate_schedule` **cada 15 minutos**. Cualquier edición manual directa sobre archivos en `/opt/so/conf/` (como `sensoroni.json`, `nginx.conf` o reglas manuales de iptables en la cadena `INPUT`) **será sobreescrita y eliminada**.

Para garantizar que un nodo remoto funcione de por vida sin degradarse tras un Highstate o reinicio, se configuraron los siguientes 7 puntos de anclaje definitivos:

| # | Componente / Servicio | Archivo Maestro (Pillar o Config) | Clave / Configuración Exacta | Comando de Aplicación Oficial | ¿Por qué es inmune al Highstate? |
| :-: | :--- | :--- | :--- | :--- | :--- |
| **1** | **NGINX / SSL Multi-IP** *(Manager)* | `/opt/so/saltstack/local/pillar/minions/soc-onion_standalone.sls` | ```yaml\nnginx:\n  enabled: true\n  ssl:\n    alt_names:\n      - '10.92.248.203'\n``` | `sudo salt-call state.apply nginx` | Salt compila los certificados SSL con SAN y agrega la IP ZeroTier a `server_name` en NGINX automáticamente. |
| **2** | **Sensoroni Heartbeat** *(Cliente)* | `/opt/so/saltstack/local/pillar/minions/secops-vascol_searchnode.sls` | ```yaml\nglobal:\n  url_base: "10.92.248.203"\n``` | `sudo salt 'secops-vascol*' saltutil.refresh_pillar`<br>`sudo salt 'secops-vascol*' state.apply sensoroni` | El Highstate del cliente lee su Pillar privado y compila `sensoroni.json` siempre con la IP ZeroTier. |
| **3** | **Memoria Heap Elasticsearch** *(Cliente)* | `/opt/so/saltstack/local/pillar/minions/secops-vascol_searchnode.sls` | ```yaml\nesheap: '2g'\n``` | `sudo salt 'secops-vascol*' state.apply elasticsearch` | Evita que el contenedor caiga por OOM al almacenar shards (reemplaza los 600m por defecto). |
| **4** | **Cluster Elasticsearch (9300)** *(Ambos)* | `/opt/so/saltstack/local/pillar/elasticsearch/adv_elasticsearch.sls` | ```yaml\nelasticsearch:\n  nodes:\n    searchnode:\n      secops-vascol:\n        ip: 10.92.248.156\n    standalone:\n      soc-onion:\n        ip: 10.92.248.203\n``` | `sudo salt-call state.apply elasticsearch`<br>`sudo salt 'secops-vascol*' state.apply elasticsearch` | Los contenedores Docker de ambos nodos resuelven el transporte 9300 por ZeroTier en lugar de las IPs locales. |
| **5** | **Firewall Nativo SO** *(Manager y Cliente)* | `/opt/so/saltstack/local/pillar/firewall/soc_firewall.sls` | ```yaml\nassigned_hostgroups:\n  standalone:\n    - 172.17.10.25\n    - 10.92.248.203\n  searchnode:\n    - 10.92.248.156\n``` | `sudo so-firewall includehost analyst 10.92.248.156`<br>`sudo so-firewall-minion --role=SEARCHNODE --ip=10.92.248.156`<br>`sudo salt 'secops-vascol*' state.apply firewall` | Al ejecutar `state.apply firewall`, Salt lee estos grupos y genera automáticamente las reglas en `DOCKER-USER` (9300, 443, 4505/6). |
| **6** | **Redirección DNAT + MASQUERADE** *(Cliente)* | `/usr/local/bin/so-zt-nat.sh`<br>`/etc/systemd/system/so-zt-nat.service`<br>`crontab -l` | ```bash\niptables -t nat -A OUTPUT -d 172.17.10.25 -j DNAT --to-destination 10.92.248.203\niptables -t nat -A POSTROUTING -d 10.92.248.203 -j MASQUERADE\n``` | `systemctl enable --now so-zt-nat.service`<br>`* * * * * /usr/local/bin/so-zt-nat.sh` | El script verifica con `-C` para no duplicar. Si un Highstate resetea la tabla NAT, el crontab reinserta las reglas en menos de 60 segundos. |
| **7** | **Ingesta Syslog Perimetral** *(Red Local Cliente)* | `/opt/so/saltstack/local/pillar/firewall/soc_firewall.sls` | ```yaml\nassigned_hostgroups:\n  syslog:\n    - 192.168.110.1\n``` | `sudo so-firewall includehost syslog 192.168.110.1`<br>`sudo salt 'secops-vascol_searchnode' state.apply firewall` | Abre el puerto 514 UDP/TCP en `secops-vascol` para recibir logs del FortiGate sin depender de comandos manuales de iptables. |

---

### Mapeo de Resolución DNS Local (`/etc/hosts`)

Para garantizar que los servicios que resuelven por hostname no dependan de servidores DNS externos:

* **En el Manager (`soc-onion`):**
  ```bash
  echo "10.92.248.156 secops-vascol" | sudo tee -a /etc/hosts
  ```
* **En el Nodo Remoto (`secops-vascol`):**
  ```bash
  echo "10.92.248.203 soc-onion" | sudo tee -a /etc/hosts
  ```

---

## 10. Fase VII: Ingesta y Recolección de Syslog Perimetral en el Nodo Remoto (Firewall FortiGate)

> [!IMPORTANT]
> **Doble Capacidad del Nodo Remoto:**  
> Un Search Node en Security Onion no solo almacena shards distribuidos; también ejecuta Logstash y Elastic Agent localmente. Esto le permite operar simultáneamente como **Colector y Sensor Syslog On-Premise** para los appliances de red de la sucursal (firewalls, routers, switches), evitando saturar los enlaces WAN.

### 10.1 Diagnóstico de Bloqueo Inicial de Syslog
Cuando el administrador configura el Firewall perimetral (FortiGate 60F, IP `192.168.110.1`, devname `VASCOL`) para enviar tráfico syslog UDP al nodo remoto (`192.168.225.26:514`), el kernel de Linux descarta los paquetes por política de denegación predeterminada:
```text
IPTables-dropped: IN=ens32 ... SRC=192.168.110.1 DST=192.168.225.26 PROTO=UDP DPT=514 LEN=1077
```

### 10.2 Autorización Centralizada vía `so-firewall` (Security Onion 2.4)
> [!WARNING]
> En Security Onion 2.4, la herramienta clásica `so-allow` está deprecada para adición de hosts por línea de comandos y remite a `so-firewall`. Además, `so-firewall` **solo existe y debe ejecutarse en el Manager (`soc-onion`)**, jamás en los minions remotos.

1. **En el Manager Central (`soc-onion`), agregar la IP del Firewall al grupo `syslog`:**
   ```bash
   sudo so-firewall includehost syslog 192.168.110.1
   ```
   *Salida esperada:* `INFO - Successfully added IP 192.168.110.1 to hostgroup syslog`.

2. **Identificar la clave del minion remoto:**
   ```bash
   sudo salt-key -L
   ```
   *(Confirmar el nombre exacto del minion: `secops-vascol_searchnode`).*

3. **Empujar el estado de firewall al Search Node remoto:**
   ```bash
   sudo salt 'secops-vascol_searchnode' state.apply firewall
   ```
   *Resultado:* Salt compilará `/etc/sysconfig/iptables` en el Search Node remoto agregando:
   ```text
   +-A INPUT -s 192.168.110.1/32 -p udp -m udp --dport 514 -j ACCEPT
   +-A INPUT -s 192.168.110.1/32 -p tcp -m tcp --dport 514 -j ACCEPT
   ```

### 10.3 Verificación de Ingesta en Tiempo Real
1. **Verificar cese de bloqueos en el Search Node:**
   ```bash
   sudo tail -n 20 /var/log/messages | grep "DPT=514"
   ```
   *(No debe figurar ninguna nueva línea de `IPTables-dropped`).*

2. **Consultar logs de red recibidos en Elasticsearch (Desde el Manager):**
   ```bash
   sudo so-elasticsearch-query '.ds-logs-syslog-so-*/_search?q=host.name:secops-vascol&size=1&sort=@timestamp:desc&pretty'
   ```
   *(Comprobará eventos con `data_stream.dataset: "syslog.syslog"`, originados en `devname="VASCOL"`, `devid="FGT60FTK2209H6JM"`).*

> [!TIP]
> **Diferencia Técnica Clave de Datasets:**
> * **`system.syslog`:** Logs internos del sistema operativo Linux (`secops-vascol`), generados por `salt-minion`, `systemd`, `dockerd` y leídos de `/var/log/messages`.
> * **`syslog.syslog`:** Logs de red perimetrales recibidos a través del socket de red UDP/TCP 514 provenientes del firewall FortiGate de la sucursal.

---

## 11. Matriz de Resolución de Problemas (Troubleshooting)

| Síntoma / Error | Causa Raíz | Solución |
| :--- | :--- | :--- |
| `zerotier-one` status `failed (exit-code 255)` en el Manager | Zeek ya está usando los puertos 9993/9994. | Mover ZeroTier al puerto 19993 vía `local.conf` y `override.conf` (Fase I). |
| `zerotier-cli status` -> `404 status invalid JSON response` | El CLI consulta el puerto 9993 donde responde Zeek. | Crear `/var/lib/zerotier-one/zerotier-one.port` con `19993` y usar `-p19993`. |
| `curl: (28) Failed to connect ... port 443: Connection timed out` | `so-firewall` del Manager está bloqueando la IP ZeroTier. | En el Manager: `sudo so-firewall includehost analyst <IP_ZT>` y `sudo so-firewall apply`. |
| Pantalla azul: `Setup is unable to access the manager` | Faltan permisos para los puertos de Salt (4505/4506) del rol seleccionado. | En el Manager: `sudo so-firewall-minion --role=<ROL> --ip=<IP_ZT>`. |
| Sensoroni reporta `307 Temporary Redirect` -> Timeout | NGINX en el Manager no tiene la IP ZeroTier en sus nombres válidos y redirige a la IP local inalcanzable. | Configurar `nginx: ssl: alt_names: ['<IP_ZT>']` en el Pillar del Manager y ejecutar `sudo salt-call state.apply nginx`. |
| El nodo funcionaba pero desapareció al rato del Grid Web | Se modificó `sensoroni.json` con `sed` y el Highstate de los 15 min lo sobreescribió. | Configurar `global: url_base: "<IP_ZT>"` en el archivo Pillar del Minion (`minions/<nombre>.sls`) y aplicar `state.apply sensoroni`. |
| Elasticsearch `503 master_not_discovered_exception` en Search Node | Los contenedores Docker resuelven los nombres a las IPs locales y el puerto 9300 está bloqueado. | Configurar `adv_elasticsearch.sls` con las IPs ZeroTier, permitir el puerto 9300 en el firewall del nodo cliente y aplicar `state.apply elasticsearch`. |
| Elastic Agent timeout en puerto 8443 / Filebeat failover en 5055 | Fleet aprovisiona la IP LAN inalcanzable del Manager para paquetes y Logstash. | En el cliente: Aplicar `DNAT` hacia la IP ZeroTier del Manager y `MASQUERADE` hacia su IP ZeroTier (Fase 8.4). |
| `IPTables-dropped: ... PROTO=UDP DPT=514` en Search Node | El firewall bloquea los logs del FortiGate por falta de autorización en el hostgroup `syslog`. | En el Manager: `sudo so-firewall includehost syslog 192.168.110.1` y luego `sudo salt 'secops-vascol_searchnode' state.apply firewall`. |
| En el Search Node: `so-allow` o `so-firewall: command not found` | Las herramientas de firewall de SO 2.4 residen exclusivamente en el nodo Manager Central. | Ejecutar siempre los comandos de `so-firewall` en `soc-onion` y empujar los cambios con `salt '<minion>' state.apply firewall`. |
| `zerotier-cli listnetworks` muestra `ACCESS_DENIED` | El nodo se conectó a la red pero no fue aprobado. | Entrar a ZeroTier Central y marcar la casilla **Auth**. |
