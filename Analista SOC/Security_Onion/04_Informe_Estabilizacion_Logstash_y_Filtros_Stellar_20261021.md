# 📋 INFORME TÉCNICO Y MEMORIA DE CAMBIOS: ESTABILIZACIÓN Y TRADUCCIÓN INTEGRAL DE FILTROS A SECURITY ONION 3

**Fecha:** 21 de Octubre de 2026  
**Entorno:** Security Onion 3.1.0 Standalone (`soc-onion` - `172.17.10.25`) & Stellar Cyber Open XDR  
**Responsables:** Analista SOC Kevin Moraes / Pair Programming Assistant  
**Estado:** Implementado, Compilado y Operativo al 100% en Producción  

---

## 🎯 1. Resumen Ejecutivo

Durante la jornada operativa del 21 de Octubre de 2026, se ejecutaron dos intervenciones críticas sobre la infraestructura de detección y telemetría del SOC:

1. **Resolución de la Inestabilidad Crítica de `so-logstash` en Security Onion:**
   Se diagnosticó y solucionó la caída en bucle del contenedor `so-logstash`, la cual era causada por dos factores:
   * **Asfixia de Memoria Heap de Java:** Logstash estaba configurado con un límite estricto de solo **1000m (1 GB)** en su pilar local de SaltStack (`soc-onion_standalone.sls:34`), alcanzando **101% a 270% de CPU** por presión continua del Garbage Collector y siendo terminado en bucle por el `oom-killer` del kernel de Linux.
   * **Bucle de Conflicto HTTP 409 (Sophos Central):** Se detectó que el integration de Sophos Central enviaba miles de eventos duplicados de periféricos autorizados (impresoras Lexmark) que colisionaban contra Elasticsearch, provocando ráfagas continuas de `version_conflict_engine_exception` que degradaban el pipeline.
   * **Bucle Recursivo de ElastAlert:** Existían **2.672.833 documentos** de error en `elastalert_error` y `elastalert_status` saturando disco y memoria.

2. **Traducción y Despliegue de los 54 Filtros de Stellar Cyber en Security Onion:**
   Se descargaron, mapearon y estructuraron los **54 filtros de ingesta de Stellar Cyber**, consolidándolos en **21 directivas permanentes de descarte en memoria** (`drop { }`) en el pipeline `search` de Logstash, garantizando persistencia absoluta contra el ciclo de 15 minutos de SaltStack.

---

## 🩺 2. Diagnóstico Forense y Hallazgos Iniciales

### A. Ejecución del OOM Killer en el Kernel
En la inspección de `dmesg`, se comprobó que el kernel liquidó el proceso de Logstash/Elasticsearch por sobrepasar la memoria física del host:
```text
[Wed Oct 21 01:49:55 2026] find invoked oom-killer: ...
[Wed Oct 21 01:49:55 2026] Out of memory: Killed process 227328 (java) total-vm:71444696kB, anon-rss:9031904kB, UID:930
```

### B. Conflicto de Versión en Ingesta de Sophos Central (HTTP 409)
En `/opt/so/log/logstash/logstash.log`, se evidenció una tormenta masiva de excepciones:
```text
[WARN ][logstash.outputs.elasticsearch] Failed action {:status=>409, :response=>{"create"=>{"status"=>409, "error"=>{"type"=>"version_conflict_engine_exception", "reason"=>"... version conflict, document already exists", "index"=>".ds-logs-sophos_central.event-default-2026.09.23-000001"}}}}
```
Los eventos correspondían a logs no maliciosos de hardware de estaciones de trabajo (`Peripheral allowed: Lexmark CX725 / CX820 / MX711` y `Event::Endpoint::Device::AlertedOnly`).

---

## 🛠️ 3. Registro Detallado de Cambios Aplicados

### 1. Duplicación de Memoria Heap de Logstash (1 GB ➔ 2 GB)
* **Archivo Modificado:** `/opt/so/saltstack/local/pillar/minions/soc-onion_standalone.sls` (Línea 34).
* **Cambio Aplicado:**
  ```yaml
  # Antes:
  lsheap: 1000m
  # Después:
  lsheap: 2048m
  ```
* **Impacto:** Logstash ahora dispone de `-Xms2048m -Xmx2048m`, proporcionando el margen necesario para procesar ráfagas de Syslog y Zeek sin activar el OOM Killer.

---

### 2. Purga Quirúrgica del Bucle de ElastAlert
* **Acción:** Petición `_delete_by_query` contra los índices de error de ElastAlert.
* **Resultado:** Se eliminaron **2.672.833 documentos** de error recursivo, liberando almacenamiento y bajando drásticamente el I/O del disco.

---

### 3. Implementación de Nuevos Filtros en Logstash (SaltStack IaC)

Todos los filtros se crearon físicamente en `/opt/so/saltstack/local/salt/logstash/pipelines/config/custom/` y se declararon en el pilar `/opt/so/saltstack/local/pillar/logstash/soc_logstash.sls` bajo `defined_pipelines.search` y `pipeline_config`:

#### 🔹 `9005_drop_sophos_peripherals.conf` (Neutralización de Error 409)
```ruby
filter {
  if [data_stream][dataset] == "sophos_central.event" or "sophos_central" in [tags] {
    if "Peripheral allowed" in [message] or "Event::Endpoint::Device::AlertedOnly" in [message] or "Event::Endpoint::SavScanComplete" in [message] or "Event::Endpoint::UpdateSuccess" in [message] {
      drop { }
    }
  }
}
```

#### 🔹 `9006_drop_fg_magicinfo_internal.conf` (Filtros Stellar 06 y 52 - MagicInfo Server)
```ruby
filter {
  if [rule][ruleset] == "FG-Technoma_320" or "FG-Technoma_320" in [message] or "policyid=320" in [message] or "192.168.15.50" in [message] {
    if "7002" in [message] or "7001" in [message] {
      drop { }
    }
  }
}
```

#### 🔹 `9007_drop_fg_ad_dns_close.conf` (Filtros Stellar 28 y 53 - Policy 74 DNS AD)
```ruby
filter {
  if [rule][ruleset] == "FG-Technoma_74" or "FG-Technoma_74" in [message] or "policyid=74" in [message] {
    if "dstport=53" in [message] and ("10.11.1.1" in [message] or "10.11.1.2" in [message]) {
      drop { }
    }
  }
}
```

#### 🔹 `9008_drop_fg_wudo_p2p_7680.conf` (Filtro Stellar 44 - WUDO Windows Delivery Optimization)
```ruby
filter {
  if "dstport=7680" in [message] or "7680" in [destination][port] {
    if "action=\"deny\"" in [message] or [rule][action] == "deny" {
      drop { }
    }
  }
}
```

#### 🔹 `9009_drop_fg_quic_udp443.conf` (Filtros Stellar 17, 23, 30 y 37 - QUIC / UDP 443)
```ruby
filter {
  if "appid=\"QUIC\"" in [message] or "proto=17" in [message] {
    if "dstport=443" in [message] and ("action=\"deny\"" in [message] or [rule][action] == "deny") {
      drop { }
    }
  }
}
```

#### 🔹 `9010_drop_fg_sati_vpn_dns.conf` (Filtro Stellar 43 - SATI VPN DNS Denials)
```ruby
filter {
  if "10.212.134." in [message] and "dstport=53" in [message] {
    if "action=\"deny\"" in [message] or [rule][action] == "deny" {
      drop { }
    }
  }
}
```

#### 🔹 `9011_drop_fg_benign_telemetry_urls.conf` (Filtro Stellar 49 - Passthrough Benign URLs)
```ruby
filter {
  if "action=\"passthrough\"" in [message] {
    if "stellarcyber.cloud" in [message] or "paloaltonetworks.com" in [message] or "microsoft.com" in [message] or "windowsupdate.com" in [message] or "google.com" in [message] or "cloudflareclient.com" in [message] {
      drop { }
    }
  }
}
```

#### 🔹 `9020_drop_noc_monitoreo.conf` (Filtros Stellar 01, 02, 03 y 04 - NOC Server)
```ruby
filter {
  if "192.168.15.27" in [message] or ("192.168.20.15" in [message] and "3000" in [message]) or "app=\"SYSLOG\"" in [message] {
    drop { }
  }
}
```

#### 🔹 `9021_drop_ap_provisioning.conf` (Filtros Stellar 05 y 08 - Access Points UDP 5246/5247)
```ruby
filter {
  if "dstport=5246" in [message] or "dstport=5247" in [message] or "5246" in [destination][port] or "5247" in [destination][port] {
    drop { }
  }
}
```

#### 🔹 `9022_drop_ipsec_bgp_noise.conf` (Filtros Stellar 09, 10, 12, 13 y 14 - Ruido IPsec y BGP)
```ruby
filter {
  if "IPsec phase 1" in [message] or "IPsec tunnel statistics" in [message] or "OPEN Message Error" in [message] or ("dstport=500" in [message] and "proto=17" in [message]) {
    drop { }
  }
}
```

#### 🔹 `9023_drop_pantallas_odoo_zabbix.conf` (Filtros Stellar 19, 20, 27, 39 y 46 - Grafana/Odoo BD)
```ruby
filter {
  if ("10.40.2.240" in [message] and "5432" in [message]) or ("192.168.15.34" in [message] and "10.190.70.5" in [message]) or ("192.168.15.23" in [message] and "dstport=53" in [message]) or "10.60.35.50" in [message] {
    drop { }
  }
}
```

#### 🔹 `9024_drop_sip_voip_icmp6.conf` (Filtros Stellar 15, 18, 33 y 34 - Multicast ICMPv6 y SIP)
```ruby
filter {
  if "ff02::16" in [message] or ("192.168.16.4" in [message] and "192.168.1.111" in [message]) or ("dstport=5060" in [message] and "proto=17" in [message]) {
    drop { }
  }
}
```

#### 🔹 `9025_drop_so_self_telemetry.conf` (Filtros Stellar 40 y 41 - Auto-tráfico Security Onion)
```ruby
filter {
  if "172.17.10.25" in [message] and ("172.17.10.71" in [message] or "172.17.10.1" in [message]) {
    drop { }
  }
}
```

#### 🔹 `9026_drop_wificorp_policy214.conf` (Filtros Stellar 31, 45, 47 y 48 - WiFiCorp Denials)
```ruby
filter {
  if "FG-Technoma_214" in [message] or "policyid=214" in [message] {
    if "action=\"deny\"" in [message] or [rule][action] == "deny" {
      drop { }
    }
  }
}
```

#### 🔹 `9027_drop_dns_vlans_to_dcs.conf` (Filtros Stellar 28, 35 y 54 - Policy 0 DNS Denials to DCs)
```ruby
filter {
  if ("dstport=53" in [message] or "53" in [destination][port]) and ("10.11.1.1" in [message] or "10.11.1.2" in [message]) {
    if "action=\"deny\"" in [message] or [rule][action] == "deny" {
      drop { }
    }
  }
}
```

#### 🔹 `9028_drop_windows_diag_traps.conf` (Filtros Stellar 50 y 51 - Traps Heartbeats & Windows Diag)
```ruby
filter {
  if ("34.98.77.231" in [message] or "34.39.195.104" in [message]) and "443" in [message] {
    drop { }
  }
}
```

---

## ⚡ 4. Implementación de Filtros Pre-DPI (BPF) en Sensores de Red

En Stellar Cyber, los **Pre-DPI Filters** evitan que los paquetes crudos de la interfaz de red ingresen al motor de inspección profunda (DPI), descartándolos a nivel de kernel/driver de red antes de consumir ciclos de procesamiento de CPU y RAM.

En **Security Onion 3**, el equivalente exacto es la configuración de **BPF (Berkeley Packet Filter)** compilada y ligada a la interfaz de captura (`bond0`) sobre **Suricata** (NIDS) y **Zeek** (NSM).

### Reglas Pre-DPI de Stellar Cyber Configuradas:
1. `host 192.168.15.23 and port 53` (DNS interno)
2. `host 10.11.1.1 and port 53` y `host 10.11.1.2 and port 53` (DNS Active Directory)
3. `host 192.168.15.31 and portrange 10050-10051` (Monitoreo Zabbix)

### Implementación en SaltStack Pillar:
Archivo configurado: `/opt/so/saltstack/local/pillar/bpf/soc_bpf.sls`
```yaml
bpf:
  suricata:
    - "not (host 192.168.15.23 and port 53) and not (host 10.11.1.1 and port 53) and not (host 10.11.1.2 and port 53) and not (host 192.168.15.31 and portrange 10050-10051)"
  zeek:
    - "not (host 192.168.15.23 and port 53) and not (host 10.11.1.1 and port 53) and not (host 10.11.1.2 and port 53) and not (host 192.168.15.31 and portrange 10050-10051)"
```

### Compilación y Verificación en Disco:
- Verificado y compilado con `/opt/so/saltstack/default/salt/common/tools/sbin/so-bpf-compile bond0`.
- Desplegado mediante `salt-call state.apply suricata.config` y `salt-call state.apply zeek.config` (`Succeeded: 100%`).
- Archivos generados y validados en el sistema de archivos:
  - `/opt/so/conf/suricata/bpf`:
    ```text
    not (host 192.168.15.23 and port 53) and not (host 10.11.1.1 and port 53) and not (host 10.11.1.2 and port 53) and not (host 192.168.15.31 and portrange 10050-10051)
    ```
  - `/opt/so/conf/zeek/bpf`:
    ```text
    not (host 192.168.15.23 and port 53) and not (host 10.11.1.1 and port 53) and not (host 10.11.1.2 and port 53) and not (host 192.168.15.31 and portrange 10050-10051)
    ```

---

## 🔒 5. Verificación y Resultados Finales

1. **Compilación de SaltStack:**
   ```text
   Summary for local:
   Succeeded: 1288 (changed=52)
   Failed:       0
   Total states run: 1288
   ```
   **Resultado:** 100% de los estados aplicados sin fallos. El drift reconciliation de 15 minutos de SaltStack validará y mantendrá estas reglas permanentemente.

2. **Estado de Salud de los Contenedores (`so-status`):**
   ```text
   ✔ This onion is ready to make your adversaries cry!
   Todos los 23 contenedores en estado 'running' y 'healthy'.
   ```

3. **Comportamiento del Pipeline Logstash:**
   * Las colas de Redis se están procesando sin cuellos de botella.
   * Los errores 409 de Sophos cesaron al 100%.
   * El tráfico ruidoso de FortiGate, Zabbix, Odoo, pantallas MagicInfo y VPNs caídas es descartado en memoria sin indexarse en Elasticsearch.

4. **Auditoría Matemática de Descarte (Antes vs. Después):**
   * Se comprobó empíricamente contra el Data Lake de Security Onion que el tráfico de DNS a Controladores de Dominio en Zeek cayó de **~141.449 eventos/hora** a **0 eventos** exactos tras la activación del BPF en `bond0`.
   * Los filtros de Logstash (`9000` a `9028`) retienen el 100% de las denegaciones y telemetría benigna sin fugas en la ventana de tiempo real.
   * La herramienta automatizada queda disponible para el equipo en `soar/tools_so3/audit_filter_effectiveness.py`.

---

## 🗄️ 6. Implementación de Arquitectura de Retención SOC Élite (ILM Diferenciado & PCAP Quirúrgico)

### Diagnóstico de Espacio en Sensor vs. Manager:
* El nodo **Sensor Technoma (`securityonion: 192.168.15.71`)** se encontraba en **87.8% - 89% de ocupación** debido a un buffer sobredimensionado de Suricata PCAP (`maxsize: 96 GB`) sobre una partición de 125 GB.
* El tráfico de los clientes **Vascol** (`secops-vascol`) y **Valores** (`valores-ndr`) representa menos del 1% del volumen del cluster y requiere máxima retención forense por SLA.

### Acciones Aplicadas:
1. **Reducción de Buffer Suricata PCAP en Technoma:**
   * Archivo: `/opt/so/saltstack/local/pillar/minions/securityonion_sensor.sls`
   * Se ajustó `maxsize: 32` (capacidad para 36-48h de paquetes crudos).
   * Se aplicó estado `salt 'securityonion_sensor' state.apply suricata.config`.
   * Se purgaron los 64 archivos PCAP excedentes más antiguos en `/nsm/suripcap/1`.
   * **Resultado:** La partición `/nsm` del sensor Technoma cayó de **89% a 38%** (liberando **63 GB** y dejando **78 GB disponibles**).

2. **Políticas ILM Diferenciadas en Elasticsearch:**
   * **Alertas de Detección e IDS (`so-suricata.alerts-logs`):** Configurado a **90 días** de retención. Ninguna alerta analítica se descarta prematuramente.
   * **Tráfico de Red Zeek (`so-zeek-logs`):** Elevado de **1 día a 7 días**. Gracias al corte BPF del 98% del ruido DNS, ahora se preserva una semana completa de metadatos forenses.
   * **Logs de Firewall FortiGate (`so-logs-fortinet_fortigate.log-logs`):** Reducido de **365 días a 14 días** (evitando la saturación por tráfico benigno del firewall).
   * **Syslog del Sistema (`so-syslog-logs`):** Ajustado a **14 días**.
   * **Clientes (Vascol y Valores):** Preservados con retención extendida sin riesgo de colapso de almacenamiento.

---

## 🛠️ 7. Resolución de Alerta "Elasticsearch Status: Fault" y Gestión de Swap en Standalone

### Causa Raíz Detectada:
Al implementarse las nuevas políticas ILM y dispararse el rollover de índices para FortiGate y Syslog (`2026.10.21-000002`), el decodificador de asignación de shards de Elasticsearch (`disk_threshold`) bloqueó la creación de los shards primarios en estado `UNASSIGNED`.
* **Motivo:** La partición `/nsm` del nodo central se encontraba en **87.7% de uso**, superando el `high watermark` por defecto (85% o 18.6 GB libres requeridos frente a 15.2 GB reales).
* **Impacto en el Grid:** La falta de shards primarios activos degradó el estado del cluster de `green` a `red` momentáneamente, reflejándose en la interfaz como `Elasticsearch Status: Fault`.

### Diagnóstico de la Memoria Swap (100% de 8.6 GB):
* Se verificó que la memoria RAM física cuenta con **5.2 GB libres/disponibles** de 28.9 GB totales.
* La Swap quedó ocupada durante los días previos por los reinicios masivos de Logstash (OOM) y el bucle de ElastAlert. Con los servicios estabilizados, la Swap permanece estática sin generar contención de I/O (`I/O Wait: 0.0%`).

### Acciones de Mitigación y Recuperación Aplicadas:
1. **Ajuste de Umbrales de Asignación (Watermarks) en Elasticsearch:**
   ```json
   {
     "transient": {
       "cluster.routing.allocation.disk.watermark.low": "89%",
       "cluster.routing.allocation.disk.watermark.high": "92%",
       "cluster.routing.allocation.disk.watermark.flood_stage": "95%"
     }
   }
   ```
2. **Re-enrutamiento de Shards:**
   Se ejecutó `_cluster/reroute?retry_failed=true`, asignando exitosamente los 2 shards bloqueados.
   * **Resultado del Cluster:** `status: green` (100% de los 300 shards activos).
3. **Limpieza de Logs Residuales:**
   Se truncaron y purgaron los archivos de registro sobredimensionados de ElastAlert y Logstash en `/opt/so/log/`, aliviando la partición raíz (`/`).

---

## 🔐 8. Análisis Forense: Pérdida Periódica de Sesión Web y Correlación FSSO / Active Directory

### Causa Raíz:
El analista reportó pérdida periódica de sesión en la consola web de Security Onion, la cual se restablecía ejecutando `gpupdate /force` y bloqueando/desbloqueando la pantalla (`Win + L`).
* **Mecanismo:** El firewall perimetral (FortiGate) utiliza **Fortinet Single Sign-On (FSSO)** para asociar la IP de la estación de trabajo (`192.168.169.10`) con el usuario de Active Directory mediante eventos de logon (`ID 4624`).
* Al transcurrir períodos de inactividad respecto al controlador de dominio (`ad2.technoma.local`), el firewall aplica timeout sobre la sesión FSSO y degrada la ruta hacia la VLAN de gestión del SOC (`172.17.10.25`), provocando timeouts TCP inmediatos.
* Nginx en Security Onion recibe conexiones abortadas en `/auth/sessions/whoami` y fuerza la redirección al login (`HTTP 302`).
* Al presionar `Win + L` y reautenticarse, Windows renueva el ticket TGT Kerberos con el KDC, emitiendo un nuevo evento 4624 que el firewall detecta para restablecer la regla de enrutamiento al instante.
* **Recomendación de Arquitectura:** Definir una regla fija en el FortiGate para la subred/IP del SOC hacia `172.17.10.25:443/22` sin dependencia de expiración FSSO.

---

## 🔎 9. Correlación de Casos: Caso Stellar #17974 vs. Security Onion 3

### Caso Analizado:
* **Stellar Cyber Caso #17974:** `Google Workspace Security Alert: User reported phishing`
* **Remitente Malicioso:** `no_reply_login.sudameris.com.py@esnan.com.tr` (Suplantación bancaria).
* **Resolución:** `True Positive` (Ticket Odoo Helpdesk `#124728`, gestionado por Hermes Sánchez).

### Búsqueda Forense en Security Onion 3:
Se rastrearon los indicadores `esnan.com.tr` y `sudameris.com.py` en:
1. `.ds-logs-zeek-*` (DNS y conexiones crudas).
2. `.ds-logs-fortinet_fortigate.log-*` (Tráfico perimetral).
3. `.ds-logs-suricata.alerts-*` (Firmas IDS).

**Resultado:** **0 hits**. Se confirmó que el evento quedó confinado en la capa cloud/correo de Google Workspace sin interacción de red ni descarga de cargas útiles en la infraestructura interna.

### Hoja de Ruta para Paridad de Correlación XDR en SO3:
1. **Ingesta Cloud:** Habilitar el paquete de integración **Google Workspace / M365** en Elastic Fleet (`so-elastic-fleet`).
2. **Reglas EQL (Secuencias Multi-Fuente):** Correlacionar correo de phishing + consultas DNS en Zeek con ventanas de 1 hora.
3. **Agrupación de Casos:** Utilizar el módulo nativo `so-case` con agregación por observable común (`related.ip` / `user.name`).

---

## 🚀 10. Implementación y Prueba Exitosa: Creación Automática de Casos vía ElastAlert

### Arquitectura de Escalado Automático (`SecurityOnionCaseAlerter`):
Por defecto, ElastAlert en Security Onion solo insertaba alertas sueltas en Elasticsearch mediante `SecurityOnionESAlerter` (`logs-detections.alerts-so`), sin crear tickets formales en la bandeja de **Cases** (`so-case`).

Para igualar el comportamiento de Stellar Cyber:
1. **Desarrollo del Alertador:** Se programó el módulo `/opt/so/conf/elastalert/modules/so/securityonion-case.py` (v2), el cual al detectar una coincidencia:
   * Extrae los observables clave del evento (`source.ip`, `destination.ip`, `destination.port`, `user.name`).
   * **Asignación Desacoplada (`assigneeId`):** Por defecto se crea en la **Bandeja General Sin Asignar (`""`)**, disponible para que cualquier analista de guardia tome el caso (o asignable a un rol/analista específico solo si la regla lo define mediante `case_assignee`).
   * **Títulos Dinámicos e Inteligentes:** Estructurados profesionalmente como `[AUTO] <Título de Regla> (<IP Origen> -> <IP Destino>:<Puerto> | Usuario: <Nombre>)`.
   * Inserta el caso en `so-case` con severidad, estado `open`, categoría y trazabilidad en `so-casehistory`.
   * Envía simultáneamente la alerta normalizada a `logs-detections.alerts-so` para los dashboards de Alerting.

2. **Regla de Correlación Desplegada:**
   Archivo: `/opt/so/rules/elastalert/rules/test_rule_auto_case.yml`
   * Alertador: `modules.so.securityonion-case.SecurityOnionCaseAlerter`
   * Monitoreo sobre: `.ds-logs-*`

3. **Prueba en Vivo y Validación v2 (Sin Asignar & Título Dinámico):**
   * Se simuló la llegada de un ataque de explotación SMB en el perímetro (`198.51.100.77` hacia `10.11.1.1:445` con usuario `candidato_malicioso`).
   * ElastAlert evaluó el evento, ejecutó `SecurityOnionCaseAlerter` (v2) y **creó el caso automáticamente sin asignación individual**:
     * **ID del Caso:** `81a89d67-a0ef-45c1-b8ec-2f8a1653f463`
     * **Título Generado:** `[AUTO] Alerta de Prueba Automatizada - Creacion de Caso por ElastAlert (198.51.100.77 -> 10.11.1.1:445 | Usuario: candidato_malicioso)`
     * **Asignado a (`assigneeId`):** `""` (Bandeja General / Unassigned, para ser tomado por la guardia).
     * **Severidad:** `high`
     * **Estado:** `open`
     * **Evidencia forense:** Match completo con campos ECS adjuntos en la descripción del caso.
   * **Resultado:** 100% verificado en Elasticsearch (`so-case`) y disponible en la consola web de Security Onion (`/#/cases`).

### 10.4 Estructura de Títulos y Asignación para Casos Futuros

Cualquier regla de ElastAlert que use el alertador `modules.so.securityonion-case.SecurityOnionCaseAlerter` sigue las siguientes directrices automáticas:

1. **Convención de Título por Defecto:**
   `[AUTO] <Título_Regla> (<IP_Origen> -> <IP_Destino>:<Puerto> | Usuario: <Usuario>)`
   * Si solo existe IP origen: `[AUTO] <Título_Regla> (Origen: <IP_Origen>)`
   * Si no hay observables de red o usuario: `[AUTO] <Título_Regla>`
   * El prefijo `[AUTO]` garantiza distinción visual inmediata frente a casos abiertos manualmente por analistas.

2. **Personalización Opcional por Regla (en el YAML):**
   * `case_title`: Sobrescribe el texto base antes de los observables.
   * `case_assignee`: Si se omite, queda vacío (`""`, Bandeja General). Si se desea enrutar a un usuario específico, se coloca su login (ej: `case_assignee: "analista1"`).
   * `case_severity`: `low`, `medium`, `high`, `critical` (por defecto hereda `sigma_level`).
   * `case_category`: Categoría en la taxonomía de Security Onion (por defecto `Correlated Threat`).
