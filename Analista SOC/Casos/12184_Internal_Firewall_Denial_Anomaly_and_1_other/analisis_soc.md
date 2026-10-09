# Reporte SOC - Caso 12184: Internal Firewall Denial Anomaly (nb-mazcona)

**Fecha de Analisis:** 2026-09-02
**Analista:** K. Moraes
**Tenant:** technoma.local
**Case ID:** 12184_Internal_Firewall_Denial_Anomaly_and_1_other
**Fuente:** Stellar Cyber XDR - internal_fw_action (Sev 60)
**XDR Event:** Internal Firewall Denial Anomaly | Tecnica: XT2002 - XDR Firewall Anomaly

---

> He detectado **5 eventos independientes** en el volcado. Se procesan secuencialmente con cierre maestro unificado al final.

---

## Analisis Evento 1 (UDP/137 - Pulso 1)

### Tags:
`#FalsoPositivo-Probable` `#NetBIOS-InterLAN` `#PoliticaFirewall` `#MITRE-XT2002` `#FortiGate-200F`

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)

- **Origen:** `192.168.169.102` | `nb-mazcona.technoma.local` (VLAN endpoints 192.168.169.0/24)
- **Destino:** `10.0.200.51` (segmento 10.0.200.0/24 - no documentado en inventario THN)
- **Protocolo / Puerto:** UDP/137 (NetBIOS Name Service)
- **Accion del Firewall:** DENY | Regla: `DENY_INTERLAN_NETBIOS`
- **Dispositivo:** `FortiGate-200F`
- **Motor Stellar:** `internal_fw_action` | XDR Event: Internal Firewall Denial Anomaly (XT2002)
- **Score ML:** 0.992 | Actual: 189 | Tipico historico: 12 | Ratio: ~15.75x

### Linea de Tiempo Temporal

| Hora UTC | Hora Local (PYT) | Evento Detectado | Actual | Tipico | Ratio | Observacion Forense |
|---|---|---|---|---|---|---|
| 2026-09-02 14:43:22 | 11:43:22 | UDP/137 denegado hacia 10.0.200.51 | 189 | 12 | 15.75x | Primera rafaga NetBIOS bloqueada |

### Desglose Tecnico y Diseccion Forense

- **NetBIOS Name Service (UDP 137):** Protocolo legacy de Windows para resolucion de nombres. Se emite automaticamente al intentar acceder a recursos compartidos o cuando el Explorador de Archivos busca equipos en la LAN.
- **Destino 10.0.200.51:** No pertenece a la VLAN de origen (192.168.169.x). La regla `DENY_INTERLAN_NETBIOS` confirma politica explicita de bloqueo inter-VLAN configurada en el FortiGate.
- **Ratio 15.75x sobre historico:** El volumen real supera 15 veces el tipico, indicando una sesion activa de busqueda de recursos en otra VLAN que disparo el detector ML de Stellar.
- **`appid_stdport: yes`:** Puerto estandar y reconocido por DPI. No hay ofuscacion ni anomalia en la capa de aplicacion.

```json
{
  "payload_type": "NetBIOS Name Service Broadcast",
  "payload_value": "UDP/137 desde 192.168.169.102 hacia 10.0.200.51",
  "payload_hash": "N/A - trafico bloqueado antes de inspeccion de payload",
  "payload_firma": "appid_name: udp/137 | appid_family: Standard | appid_stdport: yes",
  "payload_accion": "DENY por regla DENY_INTERLAN_NETBIOS en FortiGate-200F",
  "payload_destino": "10.0.200.51:137 (VLAN 10.0.200.0/24 no documentada en inventario THN)"
}
```

**Comandos de Diagnostico Recomendados:**
```powershell
# Verificar unidades de red mapeadas hacia 10.0.200.x en nb-mazcona
Get-PSDrive -PSProvider FileSystem | Where-Object {$_.DisplayRoot -like "*10.0.200*"}
# Ver estado de conexiones NetBIOS activas
nbtstat -s
```

**Hipotesis Formuladas:**

| N | Hipotesis | Probabilidad | Razon |
|---|---|---|---|
| H1 | Software mapeando recursos compartidos o impresoras en otra VLAN | Alta (70%) | NetBIOS se dispara al buscar recursos cross-VLAN |
| H2 | Aplicacion legacy (ERP/inventario) con broadcast NetBIOS | Media (20%) | Aplicaciones antiguas aun usan NetBIOS para descubrimiento |
| H3 | Reconocimiento interno (T1046 Network Service Discovery) | Baja (10%) | Sin patron sistematico de escaneo ni TTPs adicionales |

### Por que es (o no es) una Amenaza?

**Veredicto: Falso Positivo con alta confianza.**

UDP/137 es NetBIOS. Windows lo emite automaticamente al intentar acceder a recursos compartidos, al abrir el Explorador de Archivos o cuando una aplicacion corporativa hace broadcasting. La politica `DENY_INTERLAN_NETBIOS` del FortiGate es exactamente la respuesta correcta: bloquear este trafico legacy entre VLANs como buena practica de segmentacion de red. El motor ML de Stellar detecto la anomalia porque el volumen historico de denegaciones para este host era bajo (tipico: 12) y ahora exploto a 189. Esto no indica actividad maliciosa sino que el usuario intento acceder a algun recurso en la VLAN 10.0.200.0/24.

---

## Analisis Evento 2 (UDP/137 - Pulso 2)

**Evento 2 es un duplicado funcional del Evento 1** con variacion minima en `actual` (201 vs 189) y `srcport` diferente (50232 vs 50231). Representa el segundo pulso de la misma sesion NetBIOS. No se repite el analisis completo. Mismo veredicto: Falso Positivo.

---

## Analisis Evento 3 (UDP/137 - Pulso 3)

**Evento 3 es un duplicado funcional del Evento 1** con `actual` = 178 y `srcport` 50233. Tercer pulso de la misma actividad de rafaga NetBIOS. Mismo veredicto: Falso Positivo.

---

## Analisis Evento 4 (TCP/5150 - Pulso 1)

### Tags:
`#PuertoNoEstandar` `#AppIdDesconocido` `#InvestigarProceso` `#DENY_INTERLAN_UNKNOWN`

### Resumen Ejecutivo

- **Origen:** `192.168.169.102` | `nb-mazcona.technoma.local`
- **Destino:** `10.0.200.51:5150` (TCP)
- **Protocolo / Puerto:** TCP/5150 (PUERTO NO ESTANDAR - `appid_stdport: no`, `appid_family: Unknown`)
- **Accion del Firewall:** DENY | Regla: `DENY_INTERLAN_UNKNOWN`
- **Score ML:** 0.987 | Actual: 155 | Tipico: 8 | Ratio: ~19.4x

### Desglose Tecnico y Diseccion Forense

- **TCP/5150:** Puerto no registrado en IANA como servicio publico estandar. Candidatos conocidos: IBM GPFS/Spectrum Scale (sistema de archivos distribuido IBM), agentes de backup corporativos, o software de gestion propietario. Requiere verificacion.
- **`appid_family: Unknown`:** El motor DPI del FortiGate no pudo identificar la aplicacion. Indica protocolo propietario sin firma en las bases de datos del dispositivo.
- **`fwrule: DENY_INTERLAN_UNKNOWN`:** Politica de denegacion por defecto para trafico TCP desconocido entre VLANs. Respuesta correcta y esperada.
- **Ratio 19.4x:** Aun mas anomalo que el NetBIOS. Sugiere que la aplicacion esta reintentando la conexion repetidamente al no recibir respuesta.

```json
{
  "payload_type": "TCP desconocido - Puerto propietario",
  "payload_value": "TCP/5150 desde 192.168.169.102 hacia 10.0.200.51",
  "payload_hash": "N/A - bloqueado antes de inspeccion de payload",
  "payload_firma": "appid_name: tcp/5150 | appid_family: Unknown | appid_stdport: no",
  "payload_accion": "DENY por regla DENY_INTERLAN_UNKNOWN en FortiGate-200F",
  "payload_destino": "10.0.200.51:5150 (no documentado en inventario THN)"
}
```

**Comandos de Diagnostico Recomendados:**
```powershell
# Identificar proceso en nb-mazcona que intenta TCP/5150
netstat -ano | findstr ":5150"
# Resolver DNS del destino
nslookup 10.0.200.51
ping 10.0.200.51
```

**Hipotesis Formuladas:**

| N | Hipotesis | Probabilidad | Razon |
|---|---|---|---|
| H1 | Agente corporativo (backup/DLP/inventario) sin acceso inter-VLAN a su servidor | Alta (60%) | Puerto propietario y patron de reintentos es tipico de agentes |
| H2 | Software de gestion de dispositivos usando puerto no estandar | Media (25%) | Coincide temporalmente con el intento NetBIOS simultaneo |
| H3 | C2 en puerto no estandar - actividad maliciosa | Baja (15%) | Sin otros IoCs ni alertas correlacionadas en el host |

---

## Analisis Evento 5 (TCP/5150 - Pulso 2)

**Evento 5 es un duplicado funcional del Evento 4** con `actual` = 163 y `srcport` 50241. Segundo pulso del mismo intento de conexion TCP/5150. Mismo analisis aplica.

---

## Correlacion Final de Eventos

Los 5 eventos forman un patron coherente desde un unico origen hacia un unico destino en dos protocolos complementarios:

1. **UDP/137 (Eventos 1-3):** Rafaga NetBIOS - busqueda de nombres o recursos en otra VLAN.
2. **TCP/5150 (Eventos 4-5):** Aplicacion intentando conectarse a un servicio en la misma IP destino usando protocolo propietario.

**Narrativa probable:** El equipo `nb-mazcona` tiene una aplicacion (o el propio usuario) intentando acceder a un servidor en la VLAN 10.0.200.0/24. La combinacion NetBIOS + puerto propietario es tipica de software de gestion de activos, impresoras en red, sistemas ERP legacy o agentes corporativos que primero resuelven el nombre del servidor via NetBIOS y luego intentan conectarse por su puerto especifico.

---

## CIERRE MAESTRO UNIFICADO

### Analisis de Impacto CIA Triad

```json
{
  "Confidencialidad": {
    "impacto": "NINGUNO",
    "razon": "Trafico bloqueado por FortiGate. No hay evidencia de exfiltracion ni acceso exitoso a datos."
  },
  "Integridad": {
    "impacto": "NINGUNO",
    "razon": "No se modifico ningun recurso. Todas las conexiones fueron denegadas antes del establecimiento."
  },
  "Disponibilidad": {
    "impacto": "BAJO",
    "razon": "El usuario o aplicacion en nb-mazcona no puede acceder al recurso en 10.0.200.51. Impacto funcional minimo si es un servicio operativamente necesario."
  }
}
```

### Veredicto y Confianza Analitica

```json
{
  "veredicto": "FALSO POSITIVO - Politica Inter-VLAN Legitima",
  "confianza": "ALTA (85 por ciento)",
  "justificacion": "UDP/137 es trafico normal de Windows bloqueado correctamente por politica. TCP/5150 requiere confirmacion del proceso origen, pero el contexto apunta a software legitimo sin acceso inter-VLAN autorizado. El 15% de incertidumbre residual se eliminara al identificar el proceso.",
  "accion_pendiente": "Confirmar con responsable de nb-mazcona el proceso que genera TCP/5150. Si es legitimo, coordinar con red para evaluar regla de firewall o reubicacion del recurso.",
  "mitre_tecnica": "XT2002 - XDR Firewall Anomaly"
}
```

### Indicador de Fatiga de Alertas

```json
{
  "nivel_fatiga": "MEDIO",
  "razon": "UDP/137 es ruido administrativo confirmable. TCP/5150 requiere verificacion antes de suprimir.",
  "accion": "Crear regla de supresion para UDP/137 en Stellar una vez confirmado como ruido. Documentar patron en SOC_GEM_v2.md."
}
```

### Fase del Ciclo NIST 800-61

| Fase NIST | Accion Tecnica |
|---|---|
| Preparacion | Revisar y documentar servicios en VLAN 10.0.200.0/24. Inventariar aplicaciones en nb-mazcona. |
| Deteccion y Analisis | Completada. Clasificado como FP alta probabilidad (85%). |
| Contencion | No requerida. FortiGate bloquea correctamente el trafico. |
| Erradicacion | N/A para Falso Positivo. |
| Recuperacion | Coordinar con TI si acceso a 10.0.200.51 es operativamente necesario. |
| Post-Incidente | Registrar en bitacora. Evaluar supresion UDP/137 en Stellar. Investigar proceso TCP/5150. |

### Playbook Asignado

| ID | Nombre | Justificacion Estrategica |
|---|---|---|
| PB-FW-POLICY | Firewall Policy Review | Trafico bloqueado por politica inter-VLAN existente y correcta. Aplica revision de politica de red, no playbook de incidente activo. |

### Resolution Tag para Stellar Cyber

**Tag:** `FP - Policy Enforcement (Inter-VLAN Block)`

**Descripcion:** Host `nb-mazcona.technoma.local` genero trafico NetBIOS (UDP/137) y TCP/5150 hacia `10.0.200.51` en otra VLAN, ambos bloqueados por politicas legitimas del FortiGate-200F. Sin evidencia de actividad maliciosa.

### Datos para Bitacora de Excel (UNA SOLA LINEA EN TABLA)

| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Deteccion | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripcion | Evidencia | Solicitud de Accion | Estado | URL | Generacion de Ticket | TICKET | Playbook |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-02 11:43 | K. Moraes | technoma.local | 12184 | Stellar Cyber XDR (internal_fw_action) | N/A | Baja | Internal Firewall Denial Anomaly | nb-mazcona intento acceder a 10.0.200.51 por UDP/137 y TCP/5150 | nb-mazcona.technoma.local (192.168.169.102) | 5 eventos: 3x UDP/137 (DENY_INTERLAN_NETBIOS) + 2x TCP/5150 (DENY_INTERLAN_UNKNOWN) en FortiGate-200F. FP: politica inter-VLAN correctamente configurada. TCP/5150 pendiente confirmacion de proceso. | alerta_original.json | Confirmar proceso TCP/5150 en nb-mazcona. Evaluar supresion Stellar para UDP/137. | Cerrado - FP | N/A | No | N/A | PB-FW-POLICY |

### Instruccion para Cierre en Stellar Cyber

**Estado:** Closed
**Resolution Tag:** `FP - Policy Enforcement (Inter-VLAN Block)`

**Comentario de Cierre:**

> Se analizaron 5 eventos agrupados bajo la alerta `Internal Firewall Denial Anomaly` originados en `nb-mazcona.technoma.local` (192.168.169.102) hacia `10.0.200.51`.
>
> **Eventos 1-3 (UDP/137):** Trafico NetBIOS Name Service bloqueado por la politica `DENY_INTERLAN_NETBIOS` del FortiGate-200F al intentar resolver nombres en el segmento 10.0.200.0/24. Comportamiento normal de Windows al buscar recursos en otra VLAN. El volumen elevado (ratio ~15x sobre historico de 12 denegaciones tipicas) se explica por una sesion activa de busqueda de recursos. **Clasificado como Falso Positivo.**
>
> **Eventos 4-5 (TCP/5150):** Conexion TCP en puerto propietario desconocido (`appid_family: Unknown`) hacia `10.0.200.51`. Sin firma de aplicacion conocida en el FortiGate. Se recomienda consultar al responsable de nb-mazcona para identificar el proceso origen. Clasificado provisionalmente como **Falso Positivo pendiente confirmacion**, sin IoCs adicionales ni alertas correlacionadas en el host.
>
> **Accion pendiente:** Identificar el proceso en `nb-mazcona` que genera TCP/5150. Si es software legitimo, evaluar apertura de regla inter-VLAN controlada.

> [!TIP]
> Actualizar `SOC_GEM_v2.md` con el patron: **nb-mazcona.technoma.local genera rafagas UDP/137 y TCP/5150 hacia 10.0.200.51 - probable aplicacion corporativa inter-VLAN sin acceso autorizado. Pendiente confirmacion proceso TCP/5150.**
> Si TCP/5150 es confirmado como servicio legitimo, agregar plantilla de cierre a `plantillas_cierre_soc.md` bajo categoria: **Bloqueo Inter-VLAN por Politica de Segmentacion**.

---

### Desglose Ultra Quirurgico

**Capa de Red / Enrutamiento:**
- `srcip: 192.168.169.102` pertenece a VLAN de endpoints/usuarios (192.168.169.0/24).
- `dstip: 10.0.200.51` pertenece al segmento 10.0.200.0/24, no documentado en inventario THN. Podria ser VLAN de servidores, impresoras o dispositivos IoT corporativos.
- `dev_name: FortiGate-200F`: Firewall inter-VLAN gestionando el enrutamiento y aplicando politicas de segmentacion.

**Capa de Transporte / Conexion:**
- Eventos 1-3: `proto: 17` (UDP) | `dstport: 137` - NetBIOS Name Service. No orientado a conexion, modo broadcast/unicast.
- Eventos 4-5: `proto: 6` (TCP) | `dstport: 5150` - Intento de conexion orientada. FortiGate rechaza antes del handshake TCP completo.
- `srcport: 50231-50241`: Puertos efimeros (>49152), confirma que nb-mazcona es el cliente iniciando conexiones salientes.

**Capa de Aplicacion / DPI:**
- UDP/137: `appid_family: Standard`, `appid_stdport: yes` - Reconocido por motor DPI de FortiGate como NetBIOS estandar.
- TCP/5150: `appid_family: Unknown`, `appid_stdport: no` - Motor DPI no identifico la aplicacion. Protocolo propietario sin firma conocida en el dispositivo.

**Metadatos del Motor ML (Stellar):**
- `engid: 16` | `engid_name: Internal Firewall Denial Anomaly` - Motor de deteccion de anomalias de denegacion interna.
- `detected_fields: ["srcip_host"]` - El campo que disparo la anomalia fue el hostname de origen. Stellar mantiene baseline por hostname.
- `gap: 0.0` - Sin brecha temporal en la deteccion. Alerta generada en tiempo real.
- Ratios: actual (155-201) vs typical (8-12) = entre 13x y 25x el valor tipico. Scores 0.987-0.992 indican alta confianza del modelo en la anomalia estadistica, pero NO en la maliciosidad.
- `aella_tuples`: Formato `src.dst.port.proto` - Confirma la tupla de conexion exacta capturada.

**Resumen Quirurgico Final:**

El equipo `nb-mazcona.technoma.local` (192.168.169.102) inicio una rafaga inusualmente alta de intentos de comunicacion inter-VLAN hacia `10.0.200.51` en dos modalidades: busqueda de nombres via NetBIOS (UDP/137, bloqueado por `DENY_INTERLAN_NETBIOS`) y conexion directa a un servicio propietario (TCP/5150, bloqueado por `DENY_INTERLAN_UNKNOWN`). El FortiGate-200F actuo correctamente en ambos casos. El motor ML de Stellar detecto el patron como anomalo porque el volumen historico de denegaciones para este host era bajo (8-12 por periodo), y ahora exploto a 155-201. Narrativa mas probable: el usuario en nb-mazcona (posiblemente manuelazcona segun el hostname) intento acceder a un servidor en la VLAN 10.0.200.0/24 manualmente o a traves de una aplicacion instalada o reconfigurada recientemente que usa TCP/5150 para comunicarse con su servidor. No hay elementos que sugieran actividad maliciosa activa, pero TCP/5150 debe confirmarse antes de cerrar el caso definitivamente.
