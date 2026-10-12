# Auditoría Forense de Seguridad: Análisis de Cegueras en Log Filters — Stellar Cyber

**Para:** Jefatura de Ciberseguridad / Equipo de Ingeniería de Detección & SOC  
**De:** Analista SOC / Ciberseguridad Operativa  
**Fecha:** 10 de Octubre de 2026  
**Clasificación:** Confidencial — Gobernanza SOC & Hardening de Sensores  
**Marco de Referencia:** Directiva de Filtrado Quirúrgico (`soc-surgical-filtering` / Zero Blind Spot Policy)  
**Objetivo:** Evaluación de los 65 filtros de logs activos en Stellar Cyber para identificar reglas que generen puntos ciegos críticos para el SOC (silenciamiento de malware, C2, exfiltración o movimiento lateral).

---

## 1. Resumen Ejecutivo de la Auditoría

De los **65 Log Filters** configurados actualmente en la plataforma, la auditoría automática ha identificado **16 filtros que vulneran las buenas prácticas de detección y generan puntos ciegos severos**:

```
                              ESTADO DE SALUD DE LOS 65 LOG FILTERS
 ┌───────────────────────────────────────┬─────────────────────────┬────────────────────────┐
 │ 🛡️ Filtros Quirúrgicos Válidos        │ 🚨 Cegueras Críticas    │ ⚠️ Riesgos Altos/Med.  │
 │ 49 filtros (75.4%)                    │ 10 filtros (15.4%)      │ 6 filtros (9.2%)       │
 └───────────────────────────────────────┴─────────────────────────┴────────────────────────┘
```

> [!CAUTION]
> ### 🛑 HALLAZGO CRÍTICO PARA EL SOC
> Se descubrió que varios filtros fueron creados con la técnica del **"Hacha"** (silenciar hosts completos o protocolos web enteros) en lugar del **"Bisturí Quirúrgico"** (especificar dispositivo + acción + aplicación benigna).
> **Si un host con silenciamiento total es comprometido por ransomware o malware, el firewall FortiGate descartará los eventos en el sensor y el SOC jamás recibirá la telemetría.**

---

## 2. Los 10 Filtros con Ceguera Crítica (Peligro Inmediato)

### 🔴 1. Silenciamiento Total de Hosts (Sin límite de puerto, servicio ni aplicación)
Estos filtros eliminan **el 100% de la telemetría** del host indicado. Cualquier escaneo, explotación de vulnerabilidad, exfiltración o baliza hacia un C2 queda totalmente invisible para el SIEM/XDR.

| Filtro # | ID de Filtro | Dispositivo | Regla Configurada | Impacto de Seguridad (Punto Ciego) |
| :---: | :---: | :---: | :--- | :--- |
| **#1** | `691caf0998520e1b91eb3860` | `fw_fortigate` | `srcip == 192.168.15.27` | **Ceguera Total de Origen:** Silencia todo lo que la IP `192.168.15.27` transmita hacia cualquier destino del mundo. |
| **#2** | `691cb065fd93619a950d1787` | `fw_fortigate` | `dstip == 192.168.15.27` | **Ceguera Total de Destino:** Silencia cualquier ataque, escaneo o conexión dirigida a `192.168.15.27`. |
| **#57** | `6a5139be27ba4bd1fd69924c` | `fw_fortigate` | `srcip == ['172.17.10.25', '172.17.10.71']` | Silenciamiento total de dos servidores internos corporativos. |
| **#59** | `6a51481127326e7742c519f6` | `fw_fortigate` | `dstip == ['172.17.10.25', '172.17.10.71']` | Silenciamiento total hacia esos dos servidores corporativos. |

---

### 🔴 2. Descarte Ciego de Protocolos Web y Cifrados (HTTPS / QUIC)
Descarta tráfico cifrado saliente sin validar el dominio de destino. Si un actor malicioso establece comunicación por estos puertos, el sensor no reportará nada al XDR.

| Filtro # | ID de Filtro | Dispositivo | Regla Configurada | Impacto de Seguridad (Punto Ciego) |
| :---: | :---: | :---: | :--- | :--- |
| **#60** | `6a514eca27326e7742c51a03` | `fw_fortigate` | `srcip == ['192.168.15.31', '10.2.1.4', '172.17.10.251']` AND `appid_name == ['https', 'HTTPS']` | **Punto Ciego Masivo:** Descarta **TODO el tráfico HTTPS saliente** desde el servidor Zabbix (`192.168.15.31`) y otros 2 servidores hacia Internet o la red interna. Si Zabbix es vulnerado y baja un payload malicioso por 443, no habrá registro en Stellar. |
| **#53** | `69bda3da65e9b18c3281ae56` | `fw_fortigate` | `appid_name == ['QUIC']` | **Descarte Global de QUIC (UDP 443):** Descarta el protocolo en TODA la red. Cualquier malware que use túneles HTTP/3 o QUIC para C2 o exfiltración queda 100% invisible. |

---

### 🔴 3. Silenciamiento de IPs Públicas Completas
| Filtro # | ID de Filtro | Dispositivo | Regla Configurada | Impacto de Seguridad |
| :---: | :---: | :---: | :--- | :--- |
| **#24** | `691e0987fd93619a950d1826` | `fw_fortigate` | `dstip == ['142.251.128.67', '142.251.129.74']` | Silencia IPs públicas sin restringir puerto ni aplicación. |
| **#31** | `691e42924ae91719cb3e4a21` | `fw_fortigate` | `dstip == ['172.224.174.195', '172.224.174.196', '172.224.174.198', '172.224.174.197']` | Silencia bloque de IPs de CDN/Apple sin validar servicio. |
| **#32** | `691e62c1fd93619a950d184f` | `fw_fortigate` | `dstip == ['91.189.91.x', '185.125.190.x']` | Silencia repositorios de Ubuntu completos sin limitar puerto HTTP/HTTPS. |

---

## 3. Filtros con Riesgo Alto (Descartes Globales y Subredes Masivas)

1. **Filtro #5, #6 y #8 (Descartes Globales de Puertos sin Host):**
   * Reglas: `dstport == 5247`, `dstport == [7002, 8000, 38881]`, `dstport == 5246`.
   * **Peligro:** Descartan esos puertos en **toda la infraestructura** sin especificar origen ni destino. Aunque 5246/5247 son puertos de CAPWAP (antenas WiFi), descartarlos globalmente impide detectar escaneos o abusos sobre esos puertos en servidores que no son controladores inalámbricos.
2. **Filtro #64 (Descarte de Denegaciones en Clase B Completa):**
   * Regla: `action == 'deny'` AND `dstport == 7680` AND `srcip == '192.168.0.0/16'`.
   * **Peligro:** Utiliza un bloque CIDR masivo (`/16`). Si hay escaneos o intentos de movimiento lateral bloqueados en ese puerto en subredes no contempladas, se pierden.
3. **Filtro #43 (Subnet Pública Masiva con Protocolo Cifrado):**
   * Regla: `dstip == ['57.144.0.0/14', '142.251.0.0/16']` AND `appid_name == ['QUIC']`.

---

## 4. Plan de Remediación Quirúrgica (Reemplazo de Filtros Peligrosos)

Para evitar puntos ciegos sin disparar la cuota de ingesta, se debe aplicar el **Principio de las 3 Dimensiones** de `soc-surgical-filtering`:

$$\text{Regla Segura} = \text{Dispositivo} + \text{Acción / Origen} + \mathbf{Aplicación\ Benigna\ Concreta\ y\ Puerto}$$

### Plan de Cambios Específicos:

1. **Corregir Filtros #1 y #2 (`192.168.15.27`):**
   * Averiguar qué servicio corre en `192.168.15.27` (ej. si es backup Veeam o NFS).
   * *Corrección:* Modificar el filtro para que descarte **únicamente** el puerto y protocolo benigno (ej. `srcip: 192.168.15.27 AND dstport: 2049 AND appid_name: nfs`), **nunca la IP completa**.
2. **Corregir Filtro #60 (Zabbix HTTPS):**
   * No descartar todo el tráfico HTTPS. Reemplazarlo por una regla que solo descarte las peticiones hacia el FQDN o IP del servidor interno al que Zabbix consulta (ej. `srcip: 192.168.15.31 AND dstip: <IP_DESTINO_INTERNA> AND dstport: 443`).
3. **Eliminar Filtro #53 (QUIC Global):**
   * Eliminar el descarte indiscriminado de QUIC. Si hay aplicaciones específicas que saturan QUIC (ej. YouTube en WiFi), limitarlo exclusivamente a la subnet de invitados o WiFi (`srcip: 192.168.169.0/24 AND appid_name: QUIC AND dstport: 443`).

---

## 5. Nueva Funcionalidad Integrada en el Master Cockpit (`command_center.py`)

Para permitir al analista SOC y a la jefatura auditar estos datos en tiempo real sin requerir scripts en consola, se ha integrado en el Cockpit principal:

1. **Nuevo Botón en la Barra de Control PB 6.3:**  
   `[🔍 Telemetría & Log Filters]`
2. **Centro de Auditoría Forense Interactivo (`ingestion_audit_dialog.py`):**
   * **Pestaña 1 (Desglose de Ingesta Diaria):** KPIs de consumo en GB por sensor, tipo de log, origen y conectores con cálculo automático de porcentajes.
   * **Pestaña 2 (Estado de Conectores Cloud):** Monitoreo en vivo de Google Workspace, Cortex XDR y Sophos (sincronización, estado `ONLINE/OFFLINE`, errores e ingesta diaria).
   * **Pestaña 3 (Auditoría de Log Filters & Cegueras SOC):** Clasificación automática en tiempo real de los 65 filtros por severidad (`CRÍTICA`, `ALTA`, `QUIRÚRGICO`), buscador por texto/IP/puerto y advertencias de puntos ciegos.
   * **Botón de Exportación:** Descarga instantánea de las evidencias completas en formato JSON/TSV.
