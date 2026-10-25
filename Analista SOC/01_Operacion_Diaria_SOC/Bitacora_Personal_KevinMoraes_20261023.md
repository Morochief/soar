# Bitácora Técnica de Ingeniería SOC - Security Onion 3

- **Fecha:** 23 de Octubre de 2026
- **Autor / Ingeniero:** Kevin Moraes
- **Servidor Objetivo:** `soc-onion` (`172.17.10.25`) - Security Onion Standalone (Manager + Search + Sensor)
- **Tema:** Resolución del fallo crítico de `soup` en descarga de imágenes pesadas (`so-elasticsearch`, `so-elastic-fleet-package-registry`) y proceso de upgrade a Security Onion 3.3.0.

---

## 1. El Problema Detectado

Durante la ejecución del comando de actualización oficial:
```bash
sudo soup -y
```

El proceso fallaba de manera consistente al momento de sincronizar las imágenes Docker grandes hacia el registro local (`soc-onion:5000`), específicamente en:
1. `ghcr.io/security-onion-solutions/so-elastic-fleet-package-registry:3.3.0` (~1.8 GB)
2. `ghcr.io/security-onion-solutions/so-elasticsearch:9.4.5` (~1.5 GB)

El log `/root/soup.log` arrojaba:
```text
#1 [internal] pushing soc-onion:5000/security-onion-solutions/so-elastic-fleet-package-registry
#1 ERROR: copy ... failed to copy: stream error: stream ID 3; PROTOCOL_ERROR; received from peer
Unable to copy so-elastic-fleet-package-registry:3.3.0 to embedded registry
Soup failed with error 1: Unhandled error
```

---

## 2. Diagnóstico y Causa Raíz

En Security Onion 3, el script `/usr/sbin/so-image-common` implementa la copia de imágenes desde GitHub Container Registry (`ghcr.io`) hacia el registro local embebido del Manager utilizando el plugin de Docker Buildx:
```bash
docker buildx imagetools create --tag $HOSTNAME:5000/$IMAGEREPO/$image "$VERIFIED_REF"
```

### ¿Por qué fallaba?
- El binario de `docker-buildx` está compilado en **Go**.
- El cliente HTTP de Go negocia por defecto **HTTP/2 multiplexado** para comunicarse con el daemon del registro Docker en `localhost:5000`.
- Cuando se transmiten streams de capas pesadas (>500 MB), la implementación de HTTP/2 en containerd/registry local corta el stream antes de terminar de escribir todos los bytes esperados por el Content-Length (`client disconnected during blob PUT`, `PROTOCOL_ERROR`).
- Al cortarse el stream, quedan chunks corruptos en `/nsm/docker-registry/docker/registry/v2/repositories/.../_uploads/`, lo que bloquea los reintentos posteriores.
- **Falta de Fallback en el código oficial:** Security Onion Solutions no previó un mecanismo alternativo en caso de que `buildx imagetools` falle, provocando la terminación abrupta (`exit 1`) de `soup`.

---

## 3. La Solución Aplicada (Elegible para Pull Request en GitHub)

Se atacó el problema en dos niveles complementarios:

### A. Solución de Protocolo de Red Go (Fix Limpio)
Para evitar que el cliente de Go sufra el bug de multiplexación de HTTP/2 en subidas pesadas en localhost, se configuró la variable de entorno del runtime de Go:
```bash
export GODEBUG=http2client=0
```
- **Efecto:** Fuerza al cliente de `buildx` a utilizar **HTTP/1.1 persistente**, donde la transferencia de blobs grandes se realiza de forma directa y secuencial sin abortos de stream.
- **Implementación en el servidor:**
  1. Se añadió a `/etc/environment`.
  2. Se añadió al inicio de `/usr/sbin/soup` y `/usr/sbin/so-image-common`.

### B. Implementación de Fallback Robusto en Código (`so-image-common`)
En caso de que `buildx imagetools` falle por cualquier motivo de red o timeout, se integró el fallback automático a `docker push` directo (que ya verifica layers existentes):
```bash
docker buildx imagetools create --tag $HOSTNAME:5000/$IMAGEREPO/$image "$VERIFIED_REF" >> "$LOG_FILE" 2>&1 || \
docker push $HOSTNAME:5000/$IMAGEREPO/$image >> "$LOG_FILE" 2>&1 || {
  echo "Unable to copy $image to embedded registry" >> "$LOG_FILE" 2>&1
  exit 1
}
```

---

## 4. Resultados Comprobados en Producción

1. **`so-elastic-fleet-package-registry:3.3.0`**: Se copió con éxito al registro local en **0.9s**.
2. **`so-elasticsearch:9.4.5`**: Se copió con éxito al registro local en **1.0s**.
3. **El resto de las 22 imágenes Docker oficiales** (`so-kibana`, `so-logstash`, `so-soc`, `so-suricata`, `so-zeek`, etc.) completaron su descarga y push sin un solo fallo.
4. El proceso `soup` avanzó limpiamente hacia la descarga del agente `elastic-agent_SO-9.4.5.tar.gz` y la fase de actualización de componentes.

---

## 5. Segundo Incidente Detectado y Resuelto: Bloqueo de Paquetes Fleet por Watermark de Disco en Elasticsearch

Durante la fase de actualización de paquetes de Elastic Fleet (`/usr/sbin/so-elastic-fleet-package-upgrade`), la ejecución se detuvo y comenzó a reintentar indefinidamente reportando el fallo en 10 paquetes:
```text
[ERROR] Command '/usr/sbin/so-elastic-fleet-package-upgrade' failed with return code: 1
ERROR: Failed to upgrade 10 package(s):
 - elastic_agent
 - elasticsearch
 - filestream
 - osquery_manager
 - redis
 - system
 - tcp
 - udp
 - windows
 - winlog
```

### Diagnóstico Técnico:
Inspeccionando los logs internos del contenedor `so-kibana`, se identificó una excepción de clúster de Elasticsearch:
```text
cluster_block_exception: index [.kibana_ingest_8.18.8_001] blocked by: 
[TOO_MANY_REQUESTS/12/disk usage exceeded flood-stage watermark, index has read-only-allow-delete block]
```
- **Causa:** La partición de captura y almacenamiento `/nsm` se encontraba al **93% de ocupación**. Por diseño preventivo, Elasticsearch activa un bloqueo de **solo lectura estricto** (`read_only_allow_delete`) al superar el umbral crítico por defecto (~90-95%).
- Al bloquearse los índices internos de Kibana (`.kibana_ingest_*` y `.kibana_task_manager_*`), el motor de Fleet quedaba inhabilitado para persistir los metadatos de las nuevas versiones de los paquetes.

### Remediación Aplicada en Tiempo Real:
1. **Elevación de umbrales (Watermarks) en el clúster:**
   Se configuraron nuevos límites tolerantes para permitir que el upgrade concluya sin interrupciones:
   ```bash
   sudo so-elasticsearch-query '_cluster/settings' -XPUT -d '{
     "persistent": {
       "cluster.routing.allocation.disk.watermark.low": "94%",
       "cluster.routing.allocation.disk.watermark.high": "96%",
       "cluster.routing.allocation.disk.watermark.flood_stage": "98%"
     }
   }'
   ```
2. **Desbloqueo global de índices del sistema:**
   Se removió la bandera de solo lectura sobre todos los índices de Kibana y del clúster:
   ```bash
   sudo so-elasticsearch-query '.kibana*/_settings?expand_wildcards=all' -XPUT -d '{"index.blocks.read_only_allow_delete": null}'
   sudo so-elasticsearch-query '_all/_settings?expand_wildcards=all' -XPUT -d '{"index.blocks.read_only_allow_delete": null}'
   ```

### Resultado:
Inmediatamente Kibana pasó de estado *degraded* a *available*, procesando exitosamente los objetos guardados e instalando las integraciones (`winlog`, `elasticsearch@1.22.0`, `filestream@2.5.0`, `osquery_manager@1.33.0`, etc.) sin volver a bloquearse.

Al ejecutarse la comprobación con `/usr/sbin/so-elastic-fleet-package-upgrade`:
> `Successfully upgraded all packages.`

---

## 6. Estado Final de la Infraestructura post-Upgrade

1. **Versión del Sistema (`/etc/soversion`):** `3.3.0`
2. **Salud General de Contenedores (`so-status`):**
   - **23/23 contenedores en estado `running` / `healthy`**:
     - `so-dockerregistry`, `so-elastalert`, `so-elastic-fleet`, `so-elastic-fleet-package-registry`
     - `so-elasticsearch` (9.4.5), `so-influxdb`, `so-kibana`, `so-kratos`
     - `so-logstash`, `so-nginx`, `so-postgres`, `so-redis`
     - `so-sensoroni`, `so-soc`, `so-strelka` (backend, coordinator, filestream, frontend, gatekeeper, manager)
     - `so-suricata`, `so-telegraf`, `so-zeek`
   - Mensaje oficial de salud: `✔ This onion is ready to make your adversaries cry!`

---

## 7. Verificación de Compatibilidad de CPU (Release Notes 3.3.0)
- Las notas de la versión 3.3.0 advierten sobre el requerimiento de soporte para microarquitectura **`x86_64-v3`** en las imágenes de Elastic 9.x.
- Se verificó que el procesador del host `soc-onion` cuenta con el set completo de instrucciones (`AVX`, `AVX2`, `BMI1`, `BMI2`, `FMA`), garantizando compatibilidad nativa plena sin riesgo de caídas de binarios.

---

## 8. Diagnóstico de Alertas en la Interfaz Web de SOC Grid

### A. Métrica "Zeek Loss: 98.1%"
- **Diagnóstico:** Falso positivo transitorio en la interfaz web de SOC. Durante el upgrade, los workers de Zeek se detuvieron temporalmente para cargar la versión 8.0.10. El dashboard promedió los minutos de reinicio como paquetes perdidos.
- **Validación técnica:** Inspección de `/nsm/zeek/logs/current/capture_loss.log` confirmó que los 5 workers operan actualmente con:
  `{"peer":"worker-1-x", "gaps":0, "acks":0, "percent_lost":0.0}` (0.0% de pérdida real).

### B. Versión mostrada en Grid para el nodo `secops-vascol` (3.1.0 vs 3.3.0)
- **Diagnóstico:** El sensor `secops-vascol` (`192.168.225.26`) tenía actualizados en disco la versión `/etc/soversion` (`3.3.0`) y casi todos sus contenedores en `3.3.0` (`so-zeek`, `so-suricata`, `so-strelka`, `so-telegraf`), pero el contenedor agente de comunicación con la interfaz de SOC (`so-sensoroni`) continuaba corriendo la imagen remanente `so-soc:3.1.0`. Por esta razón, el agente seguía identificando al nodo ante la consola web con la versión `3.1.0`.
- **Causa Raíz:** En los sensores satélites puros, el estado Salt encargado de recrear ese contenedor es `sensoroni` (y no `soc`). Durante el upgrade global, `sensoroni` no había alcanzado a recrearse en ese nodo.
- **Acción ejecutada:** 
  Se disparó la actualización del estado Salt específico hacia el minion:
  ```bash
  sudo salt 'secops-vascol_sensor' state.apply sensoroni
  ```
- **Resultado:**
  Salt reemplazó el contenedor viejo con éxito:
  `Replaced container 'so-sensoroni'. Container has a new image (soc-onion:5000/security-onion-solutions/so-soc:3.3.0)`.
  Todos los contenedores de `secops-vascol` quedaron al 100% en la versión `3.3.0` sincronizados con el Manager.


---

## 9. Análisis Forense de Filtros de Log en Puerto 7002 — Validación de Ausencia de Ceguera SOC

### Contexto del Requerimiento
El jefe de operaciones solicitó filtrar los eventos de keep-alive hacia el puerto TCP/7002 en Stellar Cyber, ya que generan un volumen masivo de logs sin valor analítico. Antes de proceder, se requirió una validación técnica completa de que el filtrado **no genera ceguera ni pérdida de capacidad de detección** para el SOC.

### Filtros Activos que Afectan Puerto 7002

| # | Nombre del Filtro | Nivel | Acciones Filtradas | Alcance |
|---|---|---|---|---|
| 1 | `Drop_FW_Accept_Close_TCP_7001_7002_and_8010_Internal_Services` | Stellar Cyber Log Filter | `accept`, `close` | Puertos 7001/7002/8010 hacia IPs 192.168.15.50, .60, 10.11.5.4 |
| 2 | `Filter NOC deny TCP 7002 8000` | Stellar Cyber Log Filter | `deny`, `close`, `timeout`, `client-rst`, `server-rst` | Puertos 7002/8000/38881 |
| 3 | `9006_drop_fg_magicinfo_internal.conf` | Pipeline Logstash (Security Onion) | Todos los eventos de Policy 320 | FortiGate → 192.168.15.50 en 7001/7002 |

**Acción no cubierta por ningún filtro:** `ip-conn` (conexión IP activa/intentada) — responsable de la generación actual de ~1M+ logs diarios residuales.

### Investigación Forense Ejecutada

Se realizaron **8 búsquedas cruzadas** en el Data Lake de Stellar Cyber y en los logs de Zeek de Security Onion para determinar la cobertura real del SOC sobre este tráfico.

#### A. Búsqueda en Stellar Cyber Data Lake (via `stellar_threat_hunter.py`)

| Query Lucene | Resultado | Interpretación |
|---|---|---|
| `dstport:7002 AND msg_class:interflow_traffic` | **0 eventos** | El sensor NDR de Stellar **no captura** este tráfico a nivel de paquete/DPI |
| `dstport:7002 AND msg_class:firewall` | **10,000+ eventos** | Todo el volumen proviene exclusivamente de syslog de FortiGate |
| `dstport:7002` (todos los índices) | **10,000+ eventos** | 100% de clase `firewall`, acción `ip-conn`, destino `192.168.15.50:7002` |
| `dstip:192.168.15.50 AND NOT msg_class:firewall` | **0 eventos** | No existe ninguna fuente de datos NDR/Interflow/IDS para esa IP en Stellar |
| `engid_name:technoma-sensor AND msg_class:ids_event` (top ports) | 443, 53, 445, 8220... | Puerto 7002 **no aparece** en el top de puertos del motor IDS del sensor |

#### B. Búsqueda en Security Onion — Zeek `conn.log` (via Salt en 4 sensores)

| Sensor | Resultado para `id.resp_p: 7002` | Resultado para `192.168.15.50` |
|---|---|---|
| `soc-onion_standalone` | **0 conexiones** | Sin resultados |
| `securityonion_sensor` | **0 conexiones** | Solo broadcasts NetBIOS (port 138) emitidos por la propia IP |
| `secops-vascol_sensor` | **0 conexiones** | Sin resultados |
| `ndr_sensor` (valores-ndr) | **0 conexiones** | Sin resultados |

#### C. Análisis del Payload Crudo del Evento Típico

```json
{
  "msg_class": "firewall",
  "dev_type": "fw_fortigate",
  "action": "ip-conn",
  "fortinet.msg": "Connection Failed",
  "fortinet.policyname": "IOT-to-Magic-Info Paradas",
  "fortinet.policyid": 247,
  "fortinet.srcintf": "HOTEL-COS_ENC-1",
  "fortinet.dstintf": "VLAN-15",
  "fortinet.service": "TCP - 7002",
  "srcip": "10.149.200.5",
  "dstip": "192.168.15.50",
  "dstport": 7002,
  "totalbytes": 0,
  "totalpackets": 0,
  "state": "Closed",
  "threat_score": 0
}
```

**Hallazgos clave del payload:**
- `totalbytes: 0` y `totalpackets: 0` → No se transfirieron datos; es un intento de conexión TCP fallido (SYN sin respuesta o RST).
- `msg: "Connection Failed"` → El handshake TCP ni siquiera se completó.
- `policyname: "IOT-to-Magic-Info Paradas"` → Tráfico de dispositivos IoT de señalización digital Samsung MagicInfo en sucursales/paradas.
- `srcintf: "HOTEL-COS_ENC-1"` → Proviene de interfaces de túneles VPN de sucursales remotas.
- `threat_score: 0` → Stellar Cyber no le asigna relevancia de seguridad.

### Conclusión Técnica: NO Existe Ceguera

| Factor de Evaluación | Dictamen |
|---|---|
| **¿El NDR de Stellar ve este tráfico?** | **NO.** El sensor NDR (`technoma-sensor`) no tiene SPAN/mirror de la VLAN 15 ni de las interfaces de túneles VPN de sucursales. Los 0 eventos en `interflow_traffic` y `ids_event` lo confirman. |
| **¿Security Onion (Zeek/Suricata) lo ve?** | **NO.** Ninguno de los 4 sensores registra conexiones al puerto 7002 ni hacia `192.168.15.50` en sus `conn.log` actuales. La VLAN de señalización digital no está reflejada hacia las bocas de captura de red. |
| **¿Filtrar genera pérdida de visibilidad?** | **NO.** No se puede perder visibilidad sobre algo que **ya no se tiene a nivel de paquete**. La única fuente de datos sobre este tráfico es el syslog del FortiGate, y ese syslog reporta conexiones fallidas sin payload (0 bytes, 0 paquetes), sin valor forense ni de detección. |
| **¿Existe riesgo si un IoT se compromete?** | **MITIGADO.** Si un dispositivo IoT en las subredes `10.149.x.x` o `10.180.x.x` se comprometiera, su actividad de movimiento lateral o exfiltración se manifestaría en puertos críticos (445/SMB, 135/RPC, 3389/RDP, 443/HTTPS, 53/DNS) que **sí están cubiertos** tanto por el FortiGate IPS, el NDR, Suricata y Zeek. Un keep-alive fallido a un servidor de pantallas no es un indicador de compromiso. |
| **¿El servicio destino es crítico?** | **NO.** `192.168.15.50:7002` es un servidor VMware (`dsthwvendor: VMware`, MAC `00:50:56:96:bd:13`) corriendo Samsung MagicInfo Server para gestión de contenido de pantallas digitales. No procesa credenciales corporativas, no tiene acceso a datos sensibles y no es un vector de entrada a la red. |

### Recomendación Operativa

1. **Agregar la acción `ip-conn`** al filtro existente `Drop_FW_Accept_Close_TCP_7001_7002_and_8010_Internal_Services` en Stellar Cyber para eliminar los ~1M+ logs diarios residuales que aún consumen cuota de ingesta.
2. **No se requiere compensación** con reglas adicionales de monitoreo, ya que la cobertura NDR/IDS nunca existió para esta VLAN y el tráfico carece de valor de detección.
3. **Mantener** la política de FortiGate `247` activa como control perimetral de acceso (el filtro solo suprime el log en Stellar, no la política de seguridad del firewall).


### Hallazgo Adicional: Riesgo de Movimiento Lateral en VLAN-15 (Segmento Compartido con Zabbix/Grafana)

#### Observación del Analista
Se identificó que `192.168.15.50` (MagicInfo Samsung) reside en la **VLAN-15**, el mismo segmento de red donde se encuentran servidores de infraestructura como Zabbix y Grafana (`192.168.15.70`, entre otros). Esto plantea la pregunta: ¿un compromiso del servidor MagicInfo podría permitir movimiento lateral intra-VLAN sin pasar por el FortiGate?

#### Investigación Realizada

| Verificación | Resultado |
|---|---|
| **Zeek ve VLAN-15** | **SÍ.** `securityonion_sensor` captura tráfico en VLAN 15 — confirmado con **2,010 conexiones** en el `conn.log` actual. VLANs visibles: 6, 10, 15, 16, 17, 18, 20, 33, 301, 302, 304, 1101, 1103, 1104, 1105. |
| **NDR Stellar ve tráfico saliente de .15.50** | **SÍ.** `interflow_traffic` muestra queries DNS de `192.168.15.50` hacia `10.11.1.1:53` (AD) con payload de `cc-ueno-itti.traps.paloaltonetworks.com` (Cortex XDR check-in). El servidor tiene agente Cortex XDR activo. |
| **NDR Stellar ve tráfico entrante a .15.50** | **NO.** `dstip:192.168.15.50 AND msg_class:interflow_traffic` = **0 eventos**. El tráfico de las sucursales IoT (`10.x.x.x`) entra por túneles VPN y el NDR solo captura la interfaz local de la VLAN, no la interfaz del túnel. |
| **Tráfico intra-VLAN-15 host-to-host** | **NO detectado en Stellar** (`srcip:192.168.15.* AND dstip:192.168.15.*` = 0 eventos). El sensor NDR no ve tráfico este-oeste dentro de la VLAN cuando es switcheado localmente (requeriría SPAN del switch de acceso). |
| **Zeek: tráfico unicast de .15.50** | Solo se ven: (1) broadcasts NetBIOS a `192.168.15.255:138` y (2) un broadcast UDP a `255.255.255.255:33221`. **No hay tráfico TCP de .15.50 a otros hosts de la VLAN-15** en Zeek actual. |

#### Análisis de Riesgo

**El riesgo de movimiento lateral desde el MagicInfo (192.168.15.50) es BAJO**, por las siguientes razones:

1. **El tráfico entrante al MagicInfo NO proviene de la VLAN-15 local.** Las conexiones al puerto 7002 vienen de subredes remotas IoT (`10.149.x.x`, `10.180.x.x`) a través de túneles VPN del FortiGate. Un compromiso de un tótem en una sucursal tendría que primero atravesar el túnel VPN y luego pivotar dentro de la VLAN-15, lo cual **sí pasaría por el firewall** y se logearía.

2. **El servidor tiene Cortex XDR activo.** El payload del interflow muestra queries DNS al dominio `cc-ueno-itti.traps.paloaltonetworks.com` — esto confirma que el agente de EDR de Palo Alto está corriendo en el servidor MagicInfo, proporcionando detección de endpoint contra malware, scripts maliciosos y movimiento lateral.

3. **Zeek ve la VLAN-15 pero no registra conexiones TCP internas de .15.50.** Esto indica que el servidor MagicInfo no está estableciendo conexiones activas hacia Zabbix (`.15.70`) ni hacia otros hosts del segmento. Su perfil de comunicación actual es:
   - DNS queries salientes → `10.11.1.1` (AD/DNS)
   - HTTPS saliente → `52.123.128.14` (Microsoft/Azure)
   - Cortex XDR check-in → `34.39.195.104` (Palo Alto Cloud)
   - Broadcasts NetBIOS locales → `192.168.15.255`
   - **Ninguna conexión directa a otros servidores de la VLAN-15**

4. **El tráfico filtrado (acciones `accept`, `close`, `deny`, `ip-conn`) se refiere exclusivamente a conexiones desde IoT remoto** (`10.x.x.x` → `192.168.15.50:7002`), no a tráfico intra-VLAN. Filtrar estos logs no elimina visibilidad sobre movimiento lateral, que se detectaría por:
   - Suricata/Zeek en Security Onion (VLAN-15 está en captura)
   - Cortex XDR en el endpoint
   - FortiGate IPS para tráfico inter-VLAN

#### Conclusión Actualizada

Se confirma que **NO existe riesgo de ceguera** al filtrar los eventos de puerto 7002. Aunque el servidor MagicInfo comparte VLAN con infraestructura de monitoreo (Zabbix/Grafana), las capas de protección restantes (Cortex XDR en endpoint, Zeek/Suricata capturando VLAN-15, FortiGate IPS inter-VLAN) proporcionan cobertura suficiente para detectar cualquier actividad anómala que pudiera originarse desde o hacia ese host.


---

## 10. Despliegue y Actualización del Filtro en Stellar Cyber

### Acción Ejecutada
- **Filtro ID:** `6ad394ab3a5c745b75a319be`
- **Nombre:** `Drop_FW_Accept_Close_TCP_7001_7002_and_8010_Internal_Services`
- **Dispositivo:** `fw_fortigate` (Fortinet FortiGate)
- **Perfil Sensor:** `profile-modular-sensor-technoma`

### Modificación Aplicada en Reglas:
Se actualizó el campo `action` sumando la acción `"ip-conn"`, cerrando la fuga de logs:
```json
{
  "dev_type": "fw_fortigate",
  "dev_type_label": "Fortinet FortiGate",
  "rules": {
    "action": {
      "type": "string",
      "op": "==",
      "value": [
        "close",
        "accept",
        "ip-conn"
      ]
    },
    "dstport": {
      "type": "number",
      "op": "==",
      "value": [
        7001,
        7002,
        8010
      ]
    },
    "dstip": {
      "type": "ip",
      "op": "matches",
      "value": [
        "192.168.15.60/32",
        "192.168.15.50/32",
        "10.11.5.4/32"
      ]
    }
  }
}
```

### Impacto Inmediato:
- **Respuesta API:** `HTTP 200 OK`.
- **Efecto:** El colector/sensor de Stellar Cyber (`technoma-sensor`) descarta inmediatamente en la etapa de pre-ingesta los eventos con acción `ip-conn` dirigidos a `192.168.15.50:7002`.
- **Ahorro de Cuota:** Eliminación estimada de **~1,000,000+ eventos diarios** residuales que consumían espacio y procesamiento innecesario en la cuota de licencia de Stellar.
- **Postura de Seguridad:** Intacta y validada forensemente en sección 9.


---

## 11. Auditoría Completa de los 54 Filtros de Stellar Cyber y Demarcación Operativa (NOC vs. SOC)

### A. Auditoría General de Filtros en Stellar Cyber
Se realizó la extracción y auditoría técnica forense del 100% de los 54 filtros de descarte activos en el colector de Stellar Cyber (`profile-modular-sensor-technoma`), documentados íntegramente en `C:\Users\kevinmoraes\Desktop\SOC\soar\AUDITORIA_54_LOG_FILTERS_STELLAR_CYBER.md`.

* **Categorización funcional:**
  1. *Telemetría Cloud, Sistemas Operativos y Antivirus (9 filtros):* Tráfico de Windows Update, Apple APNs, CDNs benignas y heartbeats de Cortex XDR.
  2. *Monitoreo Interno (11 filtros):* Polling periódico de Zabbix (puerto 10050), paneles Grafana (3000), consultas a PostgreSQL de Odoo (5432) y PINGs de Helpdesk.
  3. *Red, Protocolos de Enrutamiento y VPN (8 filtros):* Notificaciones informativas de BGP (179), renegociaciones de IPsec Phase 1/IKE (500) y SNMP (161).
  4. *Señalización Digital e IoT (5 filtros):* Conexiones al puerto 7001/7002 de pantallas MagicInfo y puerto 8010 de Veeam hacia el almacenamiento QNAP (`10.11.5.4`).
  5. *Access Points y Wi-Fi Corporativo (7 filtros):* Túneles de control/datos CAPWAP (5246/5247) y bloqueos normales de estaciones móviles en VLAN aislada.
  6. *Servicios de Directorio Activo y DNS (5 filtros):* Resoluciones DNS salientes de Domain Controllers y denegaciones perimetrales de dispositivos en VLANs sin acceso a los DCs.
  7. *Telefonía y Videollamadas (3 filtros):* Señalización SIP (5060/5080) y tráfico multimedia de Cisco Webex.
  8. *Servidores de Infraestructura SOC (6 filtros):* Tráfico de gestión de Security Onion (`172.17.10.25`, `.71`) para prevenir bucles de syslog.

* **Conclusión de Seguridad:** El 100% de los filtros aplica únicamente sobre logs de tráfico de sesión del FortiGate (`type: traffic`). Ningún filtro descarta logs de eventos de seguridad UTM/IPS (`type: utm`), los cuales ingresan sin alteraciones a las plataformas de detección.

---

### B. Análisis del Puerto 8010 (Veeam Backup a Storage QNAP)
Durante la inspección de la regla `#52`, se analizó la naturaleza del puerto TCP `8010`:
* **Flujo identificado:** `10.11.4.2:56632` (`VEEAM-SERVER-BK`, VLAN1104) hacia `10.11.5.4:8010` (`QNAP NAS Storage`, VLAN1105).
* **Política FortiGate:** Policy 150 (`"DMZTechCloud a DMZStorageTechCloud"`).
* **Propósito:** Comunicación interna del servicio de transporte de backups de Veeam contra el repositorio de almacenamiento NAS QNAP. Su inclusión en el filtro evita cientos de miles de logs de sesiones recurrentes de sondeo de disco y transferencia.

---

### C. Por qué Suricata y Zeek son el Complemento Esencial del Firewall
Se definió y formalizó el rol complementario de los motores de inspección de red frente a los logs de firewall:
* **FortiGate (Control de Acceso L3/L4):** Determina permisos de tránsito basados en IP y puerto (quién tiene autorización de pasar).
* **Suricata (NIDS por Firmas L4/L7):** Inspecciona el contenido (payload) contra más de 70,000 firmas de ataques y CVEs en vuelo, alertando en tiempo real si un paquete contiene un exploit conocido.
* **Zeek (NDR y Metadatos Forenses):** Registra el comportamiento de cada sesión, extrayendo metadatos estructurados (DNS, SSL, HTTP, huellas criptográficas JA4/JA4S) sin depender de firmas, lo que permite reconstruir la actividad incluso en escenarios Zero-Day o con tráfico cifrado.

---

### D. Demarcación de Alcance: Cliente del NOC vs. Cliente del SOC (El caso ITTI y MagicInfo)
Se estableció el marco de visibilidad y detección respecto al servidor MagicInfo (`192.168.15.50`):
* **Contexto:** El servidor y servicio pertenecen a **ITTI**, quien es **cliente del NOC (conectividad/operaciones) y no del SOC**. ITTI administra su propio tenant de Cortex XDR (`cc-ueno-itti`) con su propio equipo de seguridad interno, por lo que el SOC de Technoma no tiene visibilidad de su consola de endpoint.
* **Mecanismos de detección del SOC de Technoma:** A pesar de no gestionar el endpoint, el SOC de Technoma mantiene cobertura integral de seguridad sobre el servidor a través de la infraestructura de red propia:
  1. *Perímetro e IPS:* El tráfico remoto pasa obligatoriamente por el `FG-Technoma`. Si un paquete hacia el puerto 7002 contiene un exploit o payload malicioso, el motor IPS del firewall lo intercepta y reporta a Stellar Cyber.
  2. *Inspección de Tráfico de Red:* Los sensores de Security Onion (`securityonion_sensor`, `ndr_sensor`) capturan el tráfico de los switches vía SPAN, permitiendo a Suricata detectar firmas de intrusión y a Zeek registrar metadatos de las conexiones.
  3. *Detección de Movimiento Lateral:* Si el servidor fuera comprometido e intentara interactuar con otros equipos de la red corporativa (como Zabbix `192.168.15.70` o los Domain Controllers `10.11.1.1`), los motores de comportamiento de Zeek y Stellar Cyber detectarán inmediatamente las anomalías de escaneo o conexión interna.
* **Analogía de Demarcación:** ITTI supervisa el interior del vehículo (el sistema operativo y sus procesos vía Cortex XDR), mientras que el SOC de Technoma supervisa la autopista (toda la red, switches y firewall). Cualquier intento de utilizar la red para perpetrar un ataque o propagar una amenaza genera alertas inmediatas en las plataformas del SOC de Technoma.
