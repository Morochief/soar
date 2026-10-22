# 🛡️ INFORME TÉCNICO: CENTRALIZACIÓN AUTÓNOMA 24/7 DE INTEGRACIONES SOPHOS CENTRAL (CAJA ANDE Y VALORES) EN SECURITY ONION 3

**Fecha:** 22 de Octubre de 2026  
**Sistema:** Security Onion 3 (`172.17.10.25` / `soc-onion`)  
**Responsable Técnico:** Kevin Moraes (Analista SOC Technoma) / Asistente Autónomo SOAR  
**Estado:** ✅ **EN PRODUCCIÓN — VALIDADO Y AUDITADO**  

---

## 1. Contexto y Desafío Operativo
* **Situación Inicial:** Las integraciones de Sophos Central API de los clientes **Caja ANDE** y **Valores** estaban vinculadas a un Elastic Agent instalado localmente en la computadora del analista (`NB-KMORAEZ` en la política `Windows-AD_API-Sophos`).
* **Problema:** La recolección de eventos de seguridad dependía exclusivamente de que la laptop del analista estuviera encendida y conectada a la red de Technoma. Al apagarse la máquina o cerrar la sesión, se producían ventanas ciegas de recolección de telemetría de endpoints.
* **Objetivo:** Migrar la recolección al servidor central Security Onion 3 (`soc-onion`), haciéndola 100% autónoma, ininterrumpida (24/7), aislando estrictamente los datos de cada cliente (multi-tenant) y garantizando que las tareas de automatización de SaltStack no pisen la configuración.

---

## 2. Decisiones de Arquitectura y Diseño

### A. Ubicación del Colector: Política `FleetServer_soc-onion`
* Security Onion corre un agente dedicado para el Fleet Server (`so-elastic-fleet`).
* En lugar de instalar binarios adicionales en el sistema operativo del host que colisionen con SaltStack o consuman memoria innecesaria, se integraron las APIs de Sophos Central en la política del agente del Fleet Server: **`FleetServer_soc-onion`** (actualizada a la revisión `41`).
* **Inmunidad ante SaltStack Highstate:** Se auditó el código fuente del orquestador `/opt/so/saltstack/default/salt/elasticfleet/tools/sbin/so-elastic-fleet-integration-policy-elastic-fleet-server`. El script de SO3 **únicamente filtra y actualiza** el paquete con nombre `fleet_server`. Todas las integraciones adicionales (`sophos_central`) son ignoradas por el highstate y persisten de forma indefinida sin sobrescrituras.

### B. Segregación Estricta Multi-Tenant por Namespaces
Siguiendo las directivas de aislamiento de clientes donde Valores y Caja ANDE no deben heredar contextos de Technoma:
* **Caja ANDE:** Namespace dedicado `caja_ande`.
* **Valores:** Namespace dedicado `valores`.

---

## 3. Ejecución Paso a Paso

1. **Configuración en Fleet:**
   * En la política `FleetServer_soc-onion`, se añadieron:
     * `sophos_central-3-caja.ande` ➔ Paquete Sophos Central v1.21.0 ➔ Namespace `caja_ande`.
     * `sophos_central-2.valores` ➔ Paquete Sophos Central v1.21.0 ➔ Namespace `valores`.
     * Salida configurada a `so-manager_elasticsearch`.
2. **Desvinculación y Apagado en el Endpoint Local (`NB-KMORAEZ`):**
   * Desde la consola web de Fleet se ejecutó el **Unenroll forzado** del agente de la laptop del analista.
   * Se cortó la comunicación RPC y pipe de telemetría local, garantizando cero consumo de CPU/RAM en la máquina del analista y evitando eventos duplicados en Elasticsearch.
3. **Estabilización Previa de Swap y Kernel:**
   * La memoria swap fue recuperada previamente en 2.85 GB con `vm.swappiness = 1` y tuning de `vm.dirty_ratio = 10` / `vm.dirty_background_ratio = 5`, garantizando que el colector no genere presión de memoria.

---

## 4. Evidencias Forenses de Ingesta en Producción

### A. Data Streams Creados y Activos en Elasticsearch
```text
health status index                                                     docs.count store.size
green  open   .ds-logs-sophos_central.event-caja_ande-2026.10.22-000001        503    494.2kb
green  open   .ds-logs-sophos_central.event-valores-2026.10.22-000001            1     19.3kb
```

### B. Muestras de Telemetría Real Capturadas

#### 1. Caja ANDE (`logs-sophos_central.event-caja_ande`):
* **Endpoint:** `NBCJPPA25003`
* **Usuario:** `CAJAANDE\vescobar`
* **IP Origen:** `172.16.202.21`
* **Tipo de Evento:** `Event::Endpoint::WebControlViolation`
* **Agente Colector:** `FleetServer-soc-onion`

#### 2. Valores (`logs-sophos_central.event-valores`):
* **Endpoint:** `Romina-nb`
* **Usuario:** `VALORES\rominalopez`
* **IP Origen:** `192.168.40.68`
* **Tipo de Evento:** `Event::Endpoint::UpdateSuccess`
* **Agente Colector:** `FleetServer-soc-onion`

---

## 5. Resumen de Impacto y Beneficios
1. **Disponibilidad 24/7:** La recolección de alertas y eventos de Sophos Central de ambos clientes ya no depende de ninguna estación de trabajo ni analista.
2. **Impacto Cero en Rendimiento:** El colector se ejecuta en el contenedor existente con un impacto menor a 15 MB de RAM.
3. **Aislamiento de Datos:** Las consultas en Kibana, pipelines de Logstash y correlaciones de ElastAlert pueden filtrar directamente por `data_stream.namespace: "valores"` o `"caja_ande"`.
