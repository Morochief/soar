# Guía Maestra de Filtrado Integral — Stellar Cyber OpenXDR v7.0.0s
### Pre-DPI Filters, Traffic Filters (Post-DPI) y Log Filters

**Clasificación:** Uso Interno Exclusivo — Equipo SOC & N2 / Ingeniería de Detección  
**Versión de Plataforma:** Stellar Cyber OpenXDR v7.0.0s  
**Última Actualización:** Octubre 2026  
**Objetivo:** Manual técnico de referencia operativo para la creación, parametrización, optimización y auditoría de **Pre-DPI Filters**, **Traffic Filters** y **Log Filters**, orientado a la supresión de ruido operacional, tuning de sensores y control estricto de cuota de ingesta (Playbook 6.3).

---

## 1. Arquitectura Integral y Flujo de Filtrado en el Sensor

En Stellar Cyber v7.0.0s, el sensor implementa un pipeline de procesamiento por etapas. Cada etapa tiene una función específica para reducir la carga de CPU/RAM del sensor y evitar la saturación de ancho de banda, almacenamiento y licencias en el Procesador de Datos (**Data Processor - DP**).

```text
                                        PIPELINE DE PROCESAMIENTO DEL SENSOR
   +-------------+       +------+     +---------------------------------------------------------------------------------+
   | Data Source | ----> | Data | --> |                                SENSOR STELLAR CYBER                             |
   | (SPAN/TAP/  |       +------+     |                                                                                 |
   | Syslog/Win) |                    |  +----------+       +----------------+       +------------+       +-------------------+ |
   +-------------+                    |  | Receiver | ----> | Pre-DPI filter | ----> | DPI engine | ----> | Post-DPI filter   | |
                                      |  +----------+       +----------------+       +------------+       | (Traffic Filter)  | |
                                      |                            |                        |             +-------------------+ |
                                      |                            | (DROP Temprano         |                       |           |
                                      |                            v  a nivel Kernel BPF)   |                       v           |
                                      |                         [ DROP ]                    v               [ Transmisión al DP ]
                                      |                                                [ Interflow ]        (Metadatos L7       |
                                      |                                                                      y Alertas)         |
                                      +---------------------------------------------------------------------------------+
                                                                                                                    |
                                                                                                                    v
                                                                                                       +--------------------------+
                                                                                                       |   DATA PROCESSOR (DP)    |
                                                                                                       | - Enriquecimiento Geo/CTI|
                                                                                                       | - Machine Learning       |
                                                                                                       | - CONSUMO DE LICENCIA    |
                                                                                                       +--------------------------+
```

### Tabla Comparativa de los 3 Mecanismos de Filtrado

| Nivel de Filtrado | Tipo de Tráfico / Entrada | Punto de Evaluación en el Pipeline | Tecnología / Sintaxis | Impacto en Rendimiento del Sensor |
| :--- | :--- | :--- | :--- | :--- |
| **Pre-DPI Filter** | Tráfico de red bruto (SPAN / Mirror / TAP). | **Antes** de que el motor DPI inspeccione los paquetes (`Receiver -> Pre-DPI`). | Sintaxis BPF (*tcpdump* / *libpcap*). Expresiones L2-L4 (`and`, `or`, `not`). | **Máximo Ahorro de CPU y RAM.** Evita que el motor DPI gaste ciclos decodificando protocolos de paquetes que serán descartados. |
| **Post-DPI Filter (Traffic Filter)** | Tráfico de red inspeccionado. | **Después** de que el motor DPI procesa los paquetes y extrae metadatos. | Reglas por aplicación (`appid_name`), protocolos L7 y firmas de aplicación. | Menor ahorro de CPU (el sensor ya inspeccionó el paquete), pero permite filtrar por nombres de aplicación o comportamientos L7. |
| **Log Filter** | Logs de eventos de texto (Syslog de Firewalls, Switches, Windows Events, Conectores). | Módulo **Log Forwarder** y agente de Windows antes de transmitir al DP. | Motor de reglas nativo de Stellar Cyber (Campos normalizados, Operadores y Valores). | Reduce el tráfico de red WAN hacia el DP y ahorra 100% de almacenamiento y cuota de licencia para eventos descartados. |

---

## 2. Pre-DPI Filters: Filtrado de Red a Nivel de Kernel (Deep Dive)

### 2.1. ¿Por qué utilizar Pre-DPI Filters?
A diferencia de los Traffic Filters convencionales (Post-DPI) que analizan la totalidad de los paquetes antes de aplicar reglas, los **Pre-DPI Filters** descartan o aceptan el tráfico de red **antes de que ingrese al motor Deep Packet Inspection (DPI)**. 

Esto permite:
1. Eliminar cuellos de botella en sensores de alto rendimiento (10 Gbps / 40 Gbps).
2. Evitar que ráfagas de tráfico benigno masivo (ej. backups locales, sincronización de bases de datos, replicación DNS entre DCs) consuman la CPU del colector.
3. Prevenir la generación de falsos positivos de anomalías de red en Interflow (como *DNS Tunneling Anomaly* en replicaciones legítimas de Active Directory).

### 2.2. Terminología y Estructura en Stellar Cyber

| Término | Definición Técnica | Uso en Stellar Cyber | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Expression (Expresión)** | Sentencia válida en sintaxis *tcpdump* / *libpcap* que define una o más condiciones. | Se combinan múltiples condiciones dentro de una expresión usando `and`, `or` y `not`. | `src host 10.0.0.1 and src port 443` |
| **Rule (Regla)** | Conjunto de una o más expresiones con una directiva de acción (**Accept** o **Drop**). | Múltiples reglas en un filtro se unen implícitamente o explícitamente mediante el operador `or`. | `(src host 10.0.0.1 and src port 443) or (dst host 192.168.1.1)` |

### 2.3. Reglas Críticas de Sintaxis (Lo que NO debes romper)

> [!CAUTION]
> **REGLA DE ORO DE LOS OPERADORES EN MINÚSCULAS:**  
> Los operadores lógicos **DEBEN ESCRIBIRSE ESTRICTAMENTE EN MINÚSCULAS**: `and`, `or`, `not`.  
> Si se escriben en mayúsculas (`AND`, `OR`, `NOT`), **el filtro fallará silenciosamente y no surtirá ningún efecto**.

1. **Lógica de Múltiples Líneas (Recomendado por Legibilidad):**
   * En Stellar Cyber puedes escribir cada regla en su propia línea.
   * La plataforma inserta **automáticamente un operador `or` implícito** entre cada línea:
     ```text
     src host 10.0.0.1 and (src port 80 or src port 443)
     src host 10.0.0.2
     ```
2. **Lógica de Línea Única:**
   * Si prefieres escribir todo en una sola línea, debes encerrar cada regla entre paréntesis y unir explícitamente con `or`:
     ```text
     (src host 10.0.0.1 and (src port 80 or src port 443)) or (src host 10.0.0.2)
     ```
3. **Uso de Negaciones (`not` y `and not`):**
   * Usa `not` al inicio de una regla para invertir toda la condición (ej. `not port 22`).
   * Usa `and not` dentro de una expresión para coincidir con la primera condición pero excluir la segunda:
     ```text
     src host 10.0.0.5 and not port 22
     ```

### 2.4. Comportamiento Direccional y Naturaleza Sin Estado (Stateless)

Los filtros Pre-DPI operan a nivel de paquetes individuales sin estado (*Stateless*). Esto implica consideraciones críticas según el tipo de tráfico:

#### A. Tráfico de Paso / Espejado (Pass-Through Traffic)
* Las directivas `src` y `dst` para `host`, `ip` o `port` funcionan con normalidad, evaluando el origen o destino del paquete.
* **Sesiones Bidireccionales:** Como el tráfico de red es bidireccional (petición y respuesta), si deseas descartar o aceptar una comunicación completa (ej. consultas DNS entre una subred y un servidor), **debes contemplar ambas direcciones**:
  ```text
  src net 10.1.1.0/24 and dst host 192.168.1.12 and port 53
  src host 192.168.1.12 and dst net 10.1.1.0/24 and port 53
  ```
  *(Al escribirlas en líneas separadas, Stellar Cyber aplica un `or` automático entre ambas).*  
  *Atajo equivalente:* Omitir `src`/`dst` y usar `net` y `host` directamente:
  ```text
  net 10.1.1.0/24 and host 192.168.1.12 and port 53
  ```

#### B. Tráfico Iniciado por el Propio Sensor (Sensor-Initiated Traffic)
* `src { host | ip | port }` y `dst { host | ip | port }` **no tienen efecto**.
* Debes usar directamente `host`, `ip` o `port` sin calificadores direccionales.

#### C. La Trampa del Tráfico DHCP (DHCP Gotcha)
* **Problema:** Las reglas que filtran por IP o subred (ej. `net 10.99.10.0/24`) **NO filtran el tráfico DHCP**, debido a que el cliente cuando solicita dirección IP por broadcast aún no posee IP asignada (`0.0.0.0`).
* **Solución Mandatoria:** Filtrar DHCP siempre por **puertos UDP**:
  ```text
  udp port 67 or udp port 68
  ```
  *(El puerto 67 transporta tráfico hacia el servidor DHCP y el 68 hacia el cliente).*

### 2.5. Catálogo de Expresiones Comunes para Pre-DPI

| Objetivo de Filtrado | Expresión Pre-DPI (Sintaxis tcpdump) | Explicación Técnica |
| :--- | :--- | :--- |
| **Host Específico (Bidireccional)** | `host 192.168.1.112` | Coincide con todo el tráfico donde esta IP sea origen o destino. |
| **Host Origen** | `src host 10.36.22.54` | Solo paquetes generados por este host. |
| **Host Destino** | `dst host 192.168.1.1` | Solo paquetes que viajen hacia este host. |
| **Subred Completa (CIDR)** | `net 192.168.1.0/24` | Coincide con cualquier paquete dentro del prefijo de red /24. |
| **Puerto Específico** | `port 443` | Tráfico TCP o UDP en puerto 443 (origen o destino). |
| **Puerto Destino** | `dst port 22` | Paquetes dirigidos al puerto SSH 22. |
| **Protocolo L4 Exclusivo** | `tcp` o `udp` o `icmp` | Filtra exclusivamente por protocolo de capa de transporte. |
| **DHCP Completo** | `udp port 67 or udp port 68` | Captura o descarta toda la negociación DORA de DHCP. |
| **Exclusión de Puerto** | `src host 10.0.0.5 and not port 22` | Todo el tráfico del host 10.0.0.5 excepto sus conexiones SSH. |
| **Regla Multilínea Compleja** | `net 192.168.1.0/24 and tcp`<br/>`src host 10.0.0.5 and not port 22`<br/>`dst host 172.16.0.1` | Evalúa cada línea como una regla independiente unida por `or`. |

### 2.6. Ruta de Configuración de Pre-DPI en Stellar Cyber v7.0
1. Navegar a: **`System | DATA MANAGEMENT | Sensors | Sensor Profiles`**.
2. Presionar **`Add Modular Sensor Profile`** o **`Add Standard Sensor Profile`** (o editar un perfil existente haciendo clic en el lápiz).
3. Habilitar el módulo **Network Traffic**.
4. Habilitar la casilla **Traffic Filtering** $\rightarrow$ Configurar **Pre-DPI Filter**.
5. Seleccionar la Acción: **`Drop`** (para descartar antes de DPI) o **`Accept`** (para procesar únicamente lo especificado).
6. Escribir las expresiones en el área de texto (una por línea para mayor claridad).
7. Guardar el perfil. El sensor compila la expresión BPF en su interfaz de red de inmediato.

---

## 3. Anatomía de la Interfaz: Modal "Add a Log Filter"

La interfaz modal de configuración para la creación y edición de Log Filters de eventos de texto se ubica en:
> **`System | DATA SOURCE MANAGEMENT | Data Filters | Log Filters`** $\rightarrow$ Botón **`+ Add`** (o **`Create`**).

```text
+---------------------------------------------------------------------------------------------+
| Add a Log Filter                                                                        [X] |
+---------------------------------------------------------------------------------------------+
| Log Filter Name *                                                                           |
| [ Ingrese un nombre identificador único para el filtro                                    ] |
|                                                                                             |
| Tenant *                                                                                    |
| [ All Tenants | CAJAANDE | technoma | Valores                                            v] |
|                                                                                             |
| Log Source (Log Forwarder only)                                                             |
| [ Seleccione origen específico (ej. fortinet_firewall) o dejar vacío                     v] |
+---------------------------------------------------------------------------------------------+
| Rules                                                                                       |
| + Add Condition                                                                   Clear All |
|                                                                                             |
| +-----------------------------------------------------------------------------------------+ |
| | Field               Field Type           Operator                      [Icono Basurero] | |
| | [ action         v] [ string          v] [ is                        v]                 | |
| |                                                                                         | |
| | Values (OR)                                                                             | |
| | [ deny, close                                                                         ] | |
| +-----------------------------------------------------------------------------------------+ |
|                                                                                             |
| Total Items: 1 (Máximo: 10)                                                                 |
+---------------------------------------------------------------------------------------------+
|                                                                      [ Cancel ] [ Submit ]  |
+---------------------------------------------------------------------------------------------+
```

### Componentes del Formulario Modal:

1. **Log Filter Name (Obligatorio):**
   * Nombre único y auto-descriptivo. 
   * **Recomendación Stellar Cyber:** Usar nombres únicos en toda la organización para evitar colisiones al seleccionarlos en diferentes perfiles de sensores.
   * *Nomenclatura Estándar SOC:* `Drop_<Tenant>_<Tecnologia>_<Motivo>` (ej. `Drop_Technoma_FW_Port7680_Deny`).
2. **Tenant (Obligatorio):**
   * Selector del ámbito del filtro:
     * `All tenants`: Disponible para ser vinculado en cualquier perfil de sensor o conector de la plataforma.
     * `CAJAANDE` / `technoma` / `Valores`: Restringe el filtro exclusivamente al tenant seleccionado.
3. **Log Source (Log Forwarder only) (Opcional):**
   * Define el origen específico del log al que aplicará la regla dentro del colector. El valor real coincide con el campo `msg_origin.source` en Interflow.
   * **REGLA MANDATORIA:** Si el filtro se va a usar para **Windows Server Sensors** o **Conectores**, este campo **DEBE QUEDAR EN BLANCO (EMPTY)**. Si se selecciona un origen aquí, el agente de Windows ignorará la regla.
4. **Rules (+ Add Condition):**
   * Permite agregar de 1 a 10 condiciones por filtro.
   * Cuenta con botón **`Clear All`** para reiniciar las condiciones cargadas.
   * Cada tarjeta de condición contiene: **Field**, **Field Type**, **Operator**, **Values (OR)** y el botón de borrado individual.

---

## 4. Catálogo Oficial de Campos Nativos (`Rules | Field`)

A continuación se detalla la totalidad de los campos indexables disponibles en el menú desplegable de Stellar Cyber v7.0.0s agrupados por categoría técnica:

### 4.1. Red, Sesión y Firewall (Core Networking)
* `action`: Acción aplicada por el firewall o dispositivo (ej. `deny`, `drop`, `accept`, `close`, `client-rst`).
* `appid_name`: Nombre de la aplicación detectada (ej. `DNS`, `SSL`, `HTTP`, `WUDO`, `SSH`).
* `asset_view`: Vista o contexto del activo en la topología.
* `computer_name`: Nombre NetBIOS / Hostname del equipo emisor.
* `domain_list`: Dominios relacionados a la conexión.
* `dstip`: Dirección IP destino (admite formato individual o subred CIDR).
* `dstport`: Puerto de capa de transporte de destino (1-65535).
* `duration`: Duración de la sesión o flujo.
* `end_reason`: Motivo de terminación de la sesión de red.
* `fw_policy_id`: Identificador de la regla o política del firewall que procesó el paquete.
* `group`: Grupo lógico de asignación del dispositivo.
* `handler`: Módulo o parser que gestionó el registro.
* `inbytes_delta`: Delta de bytes de entrada en el intervalo del flujo.
* `inpkts_delta`: Delta de paquetes de entrada en el intervalo del flujo.
* `inpkts_total`: Total acumulado de paquetes entrantes en la sesión.
* `outbytes_delta`: Delta de bytes de salida en el intervalo del flujo.
* `outpkts_delta`: Delta de paquetes de salida en el intervalo del flujo.
* `outpkts_total`: Total acumulado de paquetes salientes en la sesión.
* `parser_err_msg`: Mensaje de error arrojado por el parser en caso de incompatibilidad sintáctica.
* `parser_raw_msg`: Registro de log en crudo capturado antes de normalización.
* `process_id`: Identificador de proceso del sistema operativo (PID).
* `process_user`: Usuario que ejecuta el proceso generador del evento.
* `proto`: Protocolo de transporte L4 (ej. `tcp`, `udp`, `icmp`).
* `srcip`: Dirección IP de origen (admite formato individual o subred CIDR).
* `srcport`: Puerto de capa de transporte de origen.
* `state`: Estado de la conexión o sesión.
* `threat`: Nombre o identificación de la amenaza detectada por el equipo de borde.
* `timestamp`: Marca de tiempo del registro.
* `url`: Cadena URL completa solicitada.
* `vlan`: Etiqueta numérica de VLAN de red (802.1Q).

### 4.2. Archivos e Integridad (FIM & Hashes)
* `file_name`: Nombre del archivo involucrado.
* `file_path`: Ruta completa en el sistema de archivos local.
* `file_size`: Tamaño del archivo en bytes.
* `fileid`: Identificador interno único del archivo.
* `md5`: Hash criptográfico MD5 del archivo.
* `sha256`: Hash criptográfico SHA256 del archivo.

### 4.3. Identidad y Cuentas de Usuario (IAM / Identity)
* `user.domain`: Dominio corporativo o Active Directory al que pertenece el usuario.
* `user.id`: Identificador numérico o SID del usuario.
* `user.identifier`: Identificador secundario o UPN (User Principal Name).
* `user.name`: Nombre de inicio de sesión de la cuenta (ej. `HealthMailbox*`, `SVC_Backup`).
* `user.type`: Clasificación de cuenta (ej. `User`, `Service`, `Admin`, `Machine`).

### 4.4. Cifrado y Metadatos TLS/SSL
* `tls.client_alpns`: Extensiones ALPN negociadas por el cliente.
* `tls.fingerprint`: Huella digital del certificado digital SSL/TLS.
* `tls.from_proto`: Protocolo subyacente que originó la negociación TLS.
* `tls.issuerdn`: Distinguished Name (DN) de la Autoridad Emisora del certificado (CA).
* `tls.ja3.hash`: Hash MD5 del fingerprint JA3 del cliente.
* `tls.ja3.string`: Cadena JA3 raw de negociación del cliente.
* `tls.ja3s.hash`: Hash MD5 del fingerprint JA3S del servidor.
* `tls.ja3s.string`: Cadena JA3S raw de negociación del servidor.
* `tls.ja4`: Huella moderna JA4 de red.
* `tls.notafter`: Fecha de expiración del certificado.
* `tls.notbefore`: Fecha de inicio de validez del certificado.
* `tls.serial`: Número de serie del certificado digital.
* `tls.server_alpns`: Extensiones ALPN confirmadas por el servidor.
* `tls.session_resumed`: Indicador booleano de si la sesión SSL/TLS fue reanudada.
* `tls.sni`: Server Name Indication (nombre del host solicitado en texto plano).
* `tls.subject`: Subject del certificado digital del servidor.
* `tls.subjectaltname`: Nombres alternativos del sujeto (SAN) incluidos en el certificado.
* `tls.version`: Versión del protocolo de cifrado (ej. `TLSv1.2`, `TLSv1.3`).

### 4.5. Sistema de Detección de Intrusos (IDS / IPS / Suricata)
* `ids.action`: Acción tomada por el motor IDS local (`allowed`, `blocked`, `alert`).
* `ids.category`: Categoría Suricata de la firma (ej. `Potentially Bad Traffic`).
* `ids.created_ts`: Timestamp de generación de la alerta IDS.
* `ids.cve`: Identificador CVE asociado a la firma de detección.
* `ids.gid`: Generator ID de la regla Suricata.
* `ids.rev`: Número de revisión de la firma.
* `ids.severity`: Severidad declarada por la firma IDS (1=Alta, 2=Media, 3=Baja).
* `ids.signature`: Nombre de la firma de detección de intrusión.
* `ids.signature_id`: Identificador numérico único de la firma (SID de Suricata/Emerging Threats).
* `ids.source.ip` / `ids.source.port`: IP y puerto origen según el motor de firmas.
* `ids.target.ip` / `ids.target.port`: IP y puerto objetivo según el motor de firmas.
* `ids.metadata.*`:
  * `affected_product`, `attack_target`, `confidence`, `created_at`, `cve`, `deployment`, `malware_family`, `mitre_tactic_id`, `mitre_tactic_name`, `mitre_technique_id`, `mitre_technique_name`, `performance_impact`, `reviewed_at`, `signature_severity`, `tag`, `tls_state`, `updated_at`.
* `ids.payload_details.app_proto`: Protocolo de aplicación determinado por el motor IDS.
* `ids.payload_details.dns.*`:
  * `flags`, `id`, `opcode`, `queries.rrname`, `queries.rrtype`, `query.id`, `query.opcode`, `query.rrname`, `query.rrtype`, `query.tx_id`, `query.type`, `rcode`, `rd`, `tx_id`, `type`, `version`.
* `ids.payload_details.flow.*`:
  * Métricas de bytes y paquetes saltados (*bypassed*) y transferidos entre cliente y servidor (`bytes_toclient`, `bytes_toserver`, `dest_ip`, `dest_port`, `pkts_toclient`, `pkts_toserver`, `src_ip`, `src_port`, `start`).
* `ids.payload_details.http.*`:
  * Detalles de sesión web (`content_range.*`, `hostname`, `http_content_type`, `http_method`, `http_port`, `http_refer`, `http_user_agent`, `length`, `protocol`, `redirect`, `resp_content_length`, `status`, `url`).

### 4.6. Gestión de Vulnerabilidades (Vulnerability Engine)
* `vuln_count`, `vuln_score`: Contadores y puntajes globales del escáner.
* `vulnerabilities.*` / `vulnerability.*`:
  * `count`, `cpe`, `cve`, `cvss_v2_score`, `description`, `host_id`, `hostname`, `offline`, `plugin.cvss3_base_score`, `plugin.cvss3_temporal_score`, `plugin.cvss_base_score`, `plugin.cvss_temporal_score`, `plugin.vpr.drivers.cvss3_impact_score`, `plugin.vpr.score`, `plugin_family`, `plugin_id`, `plugin_name`, `risk_factor`, `score`, `severity`, `severity_index`, `snoozed`, `synopsis`, `vuln_index`.

---

## 5. Tipos de Datos (Field Types) y Operadores Admitidos

Stellar Cyber categoriza estrictamente los campos en **5 tipos de datos**. Los operadores disponibles en el formulario varían dinámicamente según el tipo seleccionado:

| Field Type | Operadores Disponibles | Sintaxis y Comportamiento de Valores |
| :--- | :--- | :--- |
| **`ip`** | `matches`<br/>`does not match`<br/>`field exists`<br/>`field does not exist` | Admite direcciones IP individuales (ej. `192.168.15.31`) o **subredes CIDR completas** (ej. `10.212.134.0/24`, `192.168.0.0/16`). |
| **`string`** | `is`<br/>`is not`<br/>`contains`<br/>`does not contain`<br/>`field exists`<br/>`field does not exist` | Admite una lista de valores separados por coma o tecla Enter. La evaluación interna entre los valores de la lista es **OR** (ej. `deny, drop, blocked`). |
| **`number`** | `is`<br/>`is not`<br/>`greater than`<br/>`less than`<br/>`greater than or equal to`<br/>`less than or equal to`<br/>`field exists`<br/>`field does not exist` | Valores numéricos enteros o decimales. Para simular rangos inclusivos/exclusivos, use combinaciones de operadores lógicos. |
| **`date`** | `is`<br/>`is not`<br/>`contains`<br/>`does not contain`<br/>`field exists`<br/>`field does not exist` | Formato estándar de fecha ISO / epoch. |
| **`boolean`** | `is`<br/>`is not`<br/>`field exists`<br/>`field does not exist` | Valores booleanos nativos (`true` / `false`). |

---

## 6. Lógica de Evaluación, Restricciones y Límites Operativos

### 6.1. Reglas Lógicas de Combinación (AND vs. OR)
* **Dentro de un mismo Log Filter:**
  * Todas las condiciones agregadas (`+ Add Condition`) se evalúan estrictamente con lógica **AND**.
  * Un log solo se descarta si **satisface el 100% de las condiciones definidas**.
  * *Excepción:* Si dentro de una misma condición de tipo `string` o `ip` ingresas múltiples valores, esos valores particulares se evalúan entre sí con lógica **OR**.
* **Entre Múltiples Log Filters aplicados a un Perfil:**
  * La relación entre distintos Log Filters es **OR**.
  * Si un evento cumple las condiciones del *Filtro 1* **O** del *Filtro 2*, el evento es descartado inmediatamente.

### 6.2. Límites y Cuotas por Perfil (Límites Duros de Plataforma)

| Componente | Límite Máximo | Comportamiento y Recomendaciones |
| :--- | :---: | :--- |
| **Condiciones por Filtro** | **10 reglas** | Máximo de líneas `+ Add Condition` por cada Log Filter individual. |
| **Filtros por Conector** | **10 filtros** | Los conectores únicamente admiten filtros de exclusión (**Exclude**). |
| **Filtros por Perfil de Sensor Modular** | **10 filtros** | Asignados en `Log Forwarder \| Data Filtering`. |
| **Filtros por Perfil de Sensor Estándar** | **10 filtros** | Asignados en `Feature Customization \| Sensor \| Log Forwarder`. |
| **Filtros para Agente Windows (Exclude)** | **100 filtros** | Panel *Exclude Event Filters* en la pestaña Windows del perfil. |
| **Filtros para Agente Windows (Include)** | **100 filtros** | Panel *Include Event Filters* en la pestaña Windows del perfil. |

### 6.3. Orden y Performance de Evaluación
* El orden de los filtros en la lista no altera el veredicto final, pero **impacta significativamente en el consumo de CPU y memoria del sensor**.
* **Buena Práctica:** Ordena los filtros colocando en primer lugar los que tengan la mayor probabilidad de descarte (ej. si el filtro de WUDO coincide con el 60% de los logs y el de VPN con el 10%, coloca el de WUDO en la primera posición para evitar que el colector procese comprobaciones innecesarias).

### 6.4. Reglas Especiales de Agentes Windows Server
Cuando se definen listas de inclusión y exclusión simultáneamente en la pestaña Windows:
1. El sensor evalúa primero la lista de **Exclusión (Exclude List)**: si coincide, el evento es **descartado (Dropped)** de inmediato.
2. Si no coincide con la exclusión, pasa a la lista de **Inclusión (Include List)**: si coincide, el evento **se transmite (Passed)**.
3. Si no coincide con la lista de inclusión, el evento **se descarta por defecto**.
4. Si ambas listas están vacías, el filtrado está deshabilitado y se transmiten todos los eventos de Windows configurados.

---

## 7. Procedimientos Paso a Paso para la Creación de Filtros

### Método 1: Creación Directa desde el Event Display (Atajo de Triaje SOC)
Este método es el más rápido y libre de errores tipográficos para el analista N1/N2 durante el análisis de alertas:

1. Ingresa a la consola: **`Threat Hunting`** $\rightarrow$ pestaña **`Interflow Search`**.
2. En el selector superior de **Indices**, elige el índice origen:
   * `Syslog` (para firewalls, proxies, switches, EDR).
   * `Windows Events` (para servidores y controladores de dominio).
   * `Traffic` (para flujos de red Interflow).
   * `IDPS/Malware Sandbox Events` (para firmas de intrusión).
3. Localiza el evento ruidoso en la tabla y presiona el botón **More Info** en la columna *Action*.
4. En el panel lateral desplegado, haz clic en el menú superior **`Response`** $\rightarrow$ selecciona **`Add a Log Filter`**.
5. Stellar Cyber pre-completará automáticamente:
   * El campo **Tenant** con el cliente exacto del evento.
   * El nombre del campo y sus valores según la telemetría real del registro analizado.
6. Asigna un nombre estructurado (ej. `Drop_Technoma_Firewall_WUDO_7680`).
7. Ajusta los operadores y condiciones secundarias según corresponda.
8. Haz clic en **`Submit`**.

### Método 2: Creación Manual desde la Tabla de Administración
1. Dirígete a: **`System | DATA SOURCE MANAGEMENT | Data Filters | Log Filters`**.
2. Presiona el botón **`+ Add`** (esquina superior derecha).
3. Define el nombre del filtro en **Log Filter Name**.
4. Selecciona el **Tenant** (`technoma`, `CAJAANDE`, `Valores` o `All Tenants`).
5. En **Log Source**, elige el origen correspondiente si es para Log Forwarder, o déjalo vacío si es para Windows Server o universal.
6. Pulsa **`+ Add Condition`**, selecciona el campo del catálogo, su tipo de dato, el operador e ingresa el valor deseado.
7. Pulsa **`Submit`**.

---

## 8. Procedimiento de Vinculación y Activación del Filtro

> [!IMPORTANT]
> Un Log Filter recién creado **NO descarta nada por sí solo**. Es una definición pasiva en base de datos. Para que comience a surtir efecto, **debes asociarlo al perfil del sensor o conector respectivo**.

### A. Para Sensores Modulares (Colector Central / `technoma-sensor` 192.168.15.70)
1. Navega a: **`System | DATA SOURCE MANAGEMENT | Sensors | Sensor Profiles`**.
2. Ubica el perfil modular en uso (ej. `profile-modular-sensor-technoma`) y haz clic en el ícono de edición (Lápiz).
3. En el árbol de configuración izquierdo, selecciona: **`Log Forwarder | Data Filtering`**.
4. En la sección de filtros activos, presiona agregar y selecciona tu filtro de la lista.
5. Haz clic en **`Save`** / **`Submit`**. El sensor modular recibirá la orden y actualizará su motor de forwarder sin reiniciar el servicio.

### B. Para Servidores Windows (Agente Windows Server Sensor)
1. Navega a: **`System | DATA SOURCE MANAGEMENT | Sensors | Sensor Profiles`**.
2. Edita el perfil correspondiente a los servidores Windows de la infraestructura.
3. Haz clic en la pestaña **`Windows`**.
4. En el recuadro **`Exclude Event Filters`**, selecciona tu filtro de descarte (asegúrate de que el filtro tenga `Log Source` vacío).
5. Haz clic en **`Save`**.

### C. Para Conectores API (M365, Azure, AWS, Google Workspace)
1. Navega a: **`System | INTEGRATIONS | Connectors`**.
2. Ubica el conector deseado (debe tener función *Collect*) y presiona el ícono de edición.
3. Desplázate hasta el final de la página de configuración general al campo **`Log Filters`**.
4. Selecciona el filtro deseado (soporta hasta 10 filtros de exclusión).
5. Presiona **`Submit`**.

---

## 9. Recetario de Producción para Technoma SOC (Casos Reales Resueltos)

A continuación se presentan las recetas estandarizadas para mitigar los cuatro vectores de ruido identificados en la plataforma:

---

### Receta 1: Descarte de Sondas Exchange `HealthMailbox` (Windows Event ID 4776)
* **Problema:** El servidor `VMBASE8` (`172.16.201.8`) dispara más de 2,000 logs de fallo NTLM cada 10 minutos contra `VM-MARANDU` debido a pruebas de disponibilidad internas de Exchange.
* **Configuración del Log Filter:**
  * **Log Filter Name:** `Drop_Win_Event4776_HealthMailbox`
  * **Tenant:** `technoma`
  * **Log Source:** *(DEJAR VACÍO)*
  * **Condición 1:**
    * *Field:* `event_id` | *Field Type:* `number` | *Operator:* `is` | *Value:* `4776`
  * **Condición 2:**
    * *Field:* `user.name` | *Field Type:* `string` | *Operator:* `contains` | *Value:* `HealthMailbox`
* **Vinculación:** Perfil de Sensor Windows $\rightarrow$ Pestaña **Windows** $\rightarrow$ **Exclude Event Filters**.

---

### Receta 2: Descarte de Bucles de Denegación en Firewall (WUDO Puerto 7680)
* **Problema:** Tráfico P2P de actualizaciones de Windows bloqueado por el firewall entre segmentos internos, generando ráfagas de denegaciones repetitivas en Syslog.
* **Configuración del Log Filter:**
  * **Log Filter Name:** `Drop_FW_Denial_Internal_WUDO_7680`
  * **Tenant:** `technoma`
  * **Log Source:** `fortinet_firewall` (o el source correspondiente del colector)
  * **Condición 1:**
    * *Field:* `action` | *Field Type:* `string` | *Operator:* `is` | *Value:* `deny, drop, blocked`
  * **Condición 2:**
    * *Field:* `dstport` | *Field Type:* `number` | *Operator:* `is` | *Value:* `7680`
  * **Condición 3:**
    * *Field:* `srcip` | *Field Type:* `ip` | *Operator:* `matches` | *Value:* `192.168.0.0/16`
* **Vinculación:** `System | Sensors | Sensor Profiles` $\rightarrow$ Editar `profile-modular-sensor-technoma` $\rightarrow$ **Log Forwarder | Data Filtering**.

---

### Receta 3: Descarte Quirúrgico de Denegaciones DNS desde VPN Proveedores (SATI SSLVPN -> DCs)
* **Problema:** Consultas DNS automáticas/residuales desde clientes de la red SSL-VPN de SATI (`10.212.134.0/24`, usuario `sati`) denegadas masivamente por política perimetral (`policyid=0`) hacia los controladores de dominio internos (`10.11.1.0/24`, puerto 53), disparando anomalías ML de firewall (`internal_fw_action`) y saturando la cuota diaria de ingesta (Playbook 6.3).
* **Configuración del Log Filter Quirúrgico:**
  * **Log Filter Name:** `Drop_FW_Denial_SATI_VPN_DNS_DCs`
  * **Tenant:** `technoma`
  * **Log Source:** `Fortinet Fortigate` (o dejar vacío para captura universal de origen)
  * **Condición 1:**
    * *Field:* `action` | *Field Type:* `string` | *Operator:* `is` | *Value:* `deny`
  * **Condición 2:**
    * *Field:* `dstport` | *Field Type:* `number` | *Operator:* `is` | *Value:* `53`
  * **Condición 3:**
    * *Field:* `srcip` | *Field Type:* `ip` | *Operator:* `matches` | *Value:* `10.212.134.0/24`
  * **Condición 4:**
    * *Field:* `dstip` | *Field Type:* `ip` | *Operator:* `matches` | *Value:* `10.11.1.0/24`
* **Vinculación:** Perfil de Sensor Modular $\rightarrow$ **Log Forwarder | Data Filtering**.

#### Matriz de Evaluación: ¿Qué se pierde y qué NO se pierde?
* **Lo que se Descarta (Lo que no viaja al SIEM):**
  * Únicamente las denegaciones del firewall (`action=deny`) por consultas al puerto 53 (DNS) originadas exclusivamente en la subred VPN `10.212.134.0/24` dirigidas a los DCs `10.11.1.0/24`. Tráfico que ya fue bloqueado y neutralizado por el firewall.
* **Lo que se Conserva 100% Intacto (Cero pérdida de visibilidad de seguridad):**
  * ✅ **Conexiones permitidas:** Cualquier tráfico exitoso (`action=accept`) desde la VPN se ingesta normalmente.
  * ✅ **Otros puertos y servicios:** Si el usuario/atacante intenta RDP (3389), SMB (445), SSH (22), HTTP/S o escaneo de puertos, **se ingesta y alerta normalmente**.
  * ✅ **Otros destinos:** Intentos hacia otras subredes (DMZ, estaciones de trabajo, servidores de base de datos) se ingestan sin alteración.
  * ✅ **Amenazas avanzadas:** Firmas de IPS, Antivirus, NGFW o reputación disparadas por el firewall se transmiten al 100%.
  * ✅ **Auditoría forense:** La evidencia del bloqueo sigue existiendo en el syslog local del firewall FortiGate / FortiAnalyzer.

---

### Receta 4: Filtro de Tráfico Pre-DPI (Pre-DPI Filter) para Replicación DNS entre DCs (con Tag VLAN 1101)
* **Fecha de Implementación en Producción:** **01/10/2026**
* **Problema:** Sincronización continua de bases DNS y consultas de endpoints NetBIOS (`NB-*`) en `UDP 53` entre los Controladores de Dominio `10.11.1.1` y `10.11.1.2` capturada por el puerto espejo del sensor modular (`ethernet1` en **VLAN 1101**), disparando cientos de falsos positivos de *DNS Tunneling Anomaly* (Casos #16584, #16562, #43665) y consumiendo cuota de ingesta y CPU en el motor DPI.
* **Naturaleza:** **Pre-DPI Filter** (Descarte en Kernel antes de DPI a nivel de paquetes de red).
* **Configuración en Sensor Profile:**
  * Navegar a: `System | DATA MANAGEMENT | Sensors | Sensor Profiles` $\rightarrow$ Editar `profile-modular-sensor-technoma`.
  * Habilitar **Network Traffic** y **Traffic Filtering**.
  * Seleccionar Acción: **`Drop` traffic matching the following filter expressions**.
  * Expresiones Pre-DPI cargadas en líneas independientes (Ítems 13 y 14):
    * **Línea A (Tráfico con tag 802.1Q VLAN 1101):**
      ```text
      vlan 1101 and host 10.11.1.1 and host 10.11.1.2 and udp port 53
      ```
    * **Línea B (Tráfico nativo / sin etiqueta):**
      ```text
      host 10.11.1.1 and host 10.11.1.2 and udp port 53
      ```
  * Guardar el perfil con **Submit**. El sensor modular descarta esos paquetes en la interfaz SPAN antes de enviarlos al motor de análisis DPI (ahorro del 100% de CPU y erradicación definitiva de falsas alertas de Machine Learning).

---

## 10. Auditoría, Métricas de Descarte y Verificación

Para justificar el trabajo técnico ante auditorías o en reuniones de capacidad y licencias del SOC:

### 10.1. Panel de Métricas en la Tabla de Log Filters
En `System | DATA SOURCE MANAGEMENT | Data Filters | Log Filters`, monitorea las siguientes columnas:
* **`In Use`:** Cantidad de perfiles de sensor o conectores que tienen vinculado activamente el filtro. Si marca `0`, el filtro no está operando.
* **`Hit count`:** Número total de eventos individuales descartados en la ventana de tiempo seleccionada. Al hacer clic se desglosa el recuento por Tenant.
* **`Hit count size`:** **Volumen real de datos ahorrado en MB o GB**. Esta es la métrica clave para documentar el retorno de inversión y el éxito del Playbook 6.3.

### 10.2. Telemetría Interna en Threat Hunting (Sensor Monitoring)
Stellar Cyber envía periódicamente las estadísticas de descarte de cada sensor al índice interno de telemetría:
* **Índice:** `Sensor Monitoring` (`aella-ade-*`)
* **Filtro de Consulta:** `msgtype: 41`
* **Datos Visibles:** Desglose temporal de logs procesados vs. logs descartados por identificador de filtro (`filter_id`).

### 10.3. Comandos de Diagnóstico en CLI del Sensor (Consola SSH)
Si se dispone de acceso por terminal a un sensor modular o estándar:
```bash
# Ver estado general de los filtros activos en el colector
show logfilter

# Ver detalles específicos y el último evento capturado por un filtro determinado
show logfilter <filter-id>
```

---

## 11. Checklist de Verificación para el Analista N2

Antes de dar por concluido un procedimiento de filtrado, verifique:

- [ ] ¿El filtro necesario es **Pre-DPI** (paquetes brutos en SPAN) o **Log Filter** (eventos de texto en Syslog/Windows)?
- [ ] Si es **Pre-DPI Filter**, ¿todos los operadores están estrictamente en minúsculas (`and`, `or`, `not`)?
- [ ] Si es **Pre-DPI Filter**, ¿se contemplaron ambas direcciones para tráfico bidireccional (`src` y `dst` o regla no direccional)?
- [ ] Si es un **Log Filter**, ¿el nombre sigue la convención `Drop_<Tenant>_<Tecnologia>_<Motivo>`?
- [ ] ¿Se seleccionó el Tenant correcto (`technoma`, `CAJAANDE`, `Valores` o `All Tenants`)?
- [ ] Si es para Windows Server o Conectores, ¿se dejó el campo `Log Source` **vacío**?
- [ ] ¿Los campos utilizados en Log Filter son campos crudos/normalizados por el colector y no campos enriquecidos por el DP?
- [ ] ¿Se asoció el filtro al perfil del sensor correspondiente (`Log Forwarder | Data Filtering`, pestaña `Windows` o `Pre-DPI Filter`)?
- [ ] ¿Se verificó en la columna `Hit count` o en la consola del sensor que el contador comience a incrementarse tras 5 a 10 minutos de operación?
- [ ] ¿Se registró la acción técnica en la Bitácora de Turno del SOC con referencia al Playbook 6.3?

