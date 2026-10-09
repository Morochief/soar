# 🛡️ Registro Oficial de IPs Reportadas por Abuso y Ataques Perimetrales

**Analista:** Kevin Moraes  
**Área:** SOC Technoma  
**Propósito:** Control histórico de direcciones IP atacantes notificadas formalmente a los proveedores de infraestructura / hosting (Abuse Desks) y CSIRTs, para evitar reportes duplicados y auditar seguimiento.

---

## 📊 Tabla Maestra de Direcciones IP Notificadas

| # | Dirección IP | Fecha / Hora Reporte | Proveedor / ASN | País Origen | Servicio / Pto | Tipo Incidente | Destinatario (To) | CCO (Bcc) | Asunto Enviado | Estado |
| :-: | :--- | :---: | :--- | :---: | :---: | :---: | :--- | :--- | :--- | :---: |
| **01** | `172.71.232.51` | 09/10/2026 | Cloudflare Inc. (AS13335) | Francia / Edge | HTTPS (443) | Escaneo | `abuse@cloudflare.com` | `Ivan` | `Scan - 172.71.232.51 [Cloudflare Inc.]` | 🟢 Notificado |
| **02** | `172.71.119.91` | 09/10/2026 | Cloudflare Inc. (AS13335) | Francia / Edge | HTTPS (443) | Escaneo | `abuse@cloudflare.com` | `Ivan` | `Scan - 172.71.119.91 [Cloudflare Inc.]` | 🟢 Notificado |
| **03** | `172.71.232.50` | 09/10/2026 | Cloudflare Inc. (AS13335) | Francia / Edge | HTTPS (443) | Escaneo | `abuse@cloudflare.com` | `Ivan` | `Scan - 172.71.232.50 [Cloudflare Inc.]` | 🟢 Notificado |
| **04** | `172.71.127.147` | 09/10/2026 | Cloudflare Inc. (AS13335) | Francia (Paris) | HTTPS (443) | Fuerza Bruta / Scan | `abuse@cloudflare.com` | `Ivan` | `Scan - 172.71.127.147 [Cloudflare Inc.]` | 🟢 Notificado |
| **05** | `104.23.254.12` | 09/10/2026 | Cloudflare Inc. (AS13335) | EE.UU. / Edge | HTTPS (443) | Escaneo | `abuse@cloudflare.com` | `Ivan` | `Scan - 104.23.254.12 [Cloudflare Inc.]` | 🟢 Notificado |
| **06** | `5.61.209.106` | 09/10/2026 | Amarutu Technology Ltd | Seychelles | HTTP (443) | Fuerza Bruta | `abuse@koddos.com` | `Ivan` | `Brute force attack HTTP - 5.61.209.106 [Amarutu Technology Ltd]` | 🟢 Notificado |

---

## 🔍 Detalle Técnico de los Reportes Enviados (09/10/2026)

### 1. `172.71.232.51` — Cloudflare Inc.
* **Fecha de Conexión:** `2026-10-08 20:30` (GMT-3)
* **Objetivo:** DMZ Servers Technoma (`190.104.178.146:443`)
* **Acción Perimetral:** `Deny` (FortiGate Policy 262 - `Block_Countries`)
* **Asunto:** `Scan - 172.71.232.51 [Cloudflare Inc.]`
* **Destinatario:** `abuse@cloudflare.com` | **Bcc:** `Ivan`

### 2. `172.71.119.91` — Cloudflare Inc.
* **Fecha de Conexión:** `2026-10-08 20:29` (GMT-3)
* **Objetivo:** DMZ Servers Technoma (`190.104.178.146:443`)
* **Acción Perimetral:** `Deny` (FortiGate Policy 262 - `Block_Countries`)
* **Asunto:** `Scan - 172.71.119.91 [Cloudflare Inc.]`
* **Destinatario:** `abuse@cloudflare.com` | **Bcc:** `Ivan`

### 3. `172.71.232.50` — Cloudflare Inc.
* **Fecha de Conexión:** `2026-10-08 20:29` (GMT-3)
* **Objetivo:** DMZ Servers Technoma (`190.104.178.146:443`)
* **Acción Perimetral:** `Deny` (FortiGate Policy 262 - `Block_Countries`)
* **Asunto:** `Scan - 172.71.232.50 [Cloudflare Inc.]`
* **Destinatario:** `abuse@cloudflare.com` | **Bcc:** `Ivan`

### 4. `172.71.127.147` — Cloudflare Inc.
* **Fecha de Conexión:** `2026-10-08 20:28:33` (GMT-3)
* **Reputación Stellar/ETPro:** `Brute_Forcer` (Threat Score 36)
* **Objetivo:** DMZ Servers Technoma (`190.104.178.146:443` -> NAT `10.11.3.196:443`)
* **Acción Perimetral:** `Deny` (FortiGate Policy 262 - `Block_Countries` - 5 intentos consecutivos bloqueados)
* **Asunto:** `Scan - 172.71.127.147 [Cloudflare Inc.]`
* **Destinatario:** `abuse@cloudflare.com` | **Bcc:** `Ivan`

### 5. `104.23.254.12` — Cloudflare Inc.
* **Fecha de Conexión:** `2026-10-08 20:27` (GMT-3)
* **Objetivo:** DMZ Servers Technoma (`190.104.178.146:443`)
* **Acción Perimetral:** `Deny` (FortiGate Policy 262 - `Block_Countries`)
* **Asunto:** `Scan - 104.23.254.12 [Cloudflare Inc.]`
* **Destinatario:** `abuse@cloudflare.com` | **Bcc:** `Ivan`

---

## 📌 Guía Rápida para Comprobar si una IP ya fue Reportada
Antes de enviar una nueva notificación de abuso:
1. Buscar la IP en esta tabla mediante `Ctrl + F`.
2. Si ya figura con estado `🟢 Notificado` dentro de las últimas 72 horas, no duplicar el correo salvo que se trate de un ataque de severidad crítica persistente (en cuyo caso usar la **Plantilla 05 de Seguimiento**).
