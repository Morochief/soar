# 🛡️ Manual Operativo SOC: Triaje Forense & Arsenal Threat Hunting

> **Entorno de Trabajo:** Stellar Cyber OpenXDR DFIR & Threat Hunting Cockpit  
> **Área:** Detección Perimetral, Triaje CTI, Respuesta a Incidentes (DFIR) & Threat Hunting  
> **Marco Metodológico:** NIST SP 800-61r3, MITRE ATT&CK for Enterprise, Stellar Cyber Interflow  

---

## 📑 Tabla de Contenidos
1. [Propósito del Documento](#1-propósito-del-documento)
2. [Arquitectura del Arsenal Threat Hunting (Tab 5)](#2-arquitectura-del-arsenal-threat-hunting-tab-5)
3. [Matriz Operativa de Herramientas: ¿Cuándo y Cómo Usar Cada Una?](#3-matriz-operativa-de-herramientas-cuándo-y-cómo-usar-cada-una)
4. [Flujo Maestro de Triaje Rápido en 4 Fases (< 2 Minutos)](#4-flujo-maestro-de-triaje-rápido-en-4-fases--2-minutos)
5. [Caso de Estudio Real: Ataque Brute Force en IP `217.60.242.76`](#5-caso-de-estudio-real-ataque-brute-force-en-ip-2176024276)
6. [Guía de Interpretación de Hallazgos Técnicos (FAQ de Red)](#6-guía-de-interpretación-de-hallazgos-técnicos-faq-de-red)
7. [Historial de Optimizaciones Técnicas del Cockpit](#7-historial-de-optimizaciones-técnicas-del-cockpit)

---

## 1. Propósito del Documento

Este manual sirve como **referencia técnica y metodológica** para los analistas de Nivel 1 y Nivel 2 del SOC al operar la pestaña **Threat Hunting / DFIR Cockpit (Tab 5)** del sistema SOAR. 

El objetivo es estandarizar el proceso de investigación perimetral cuando se detectan eventos sospechosos (ataques de fuerza bruta, escaneos de puertos, URLs de phishing, balizas C2 o intentos de explotación de vulnerabilidades), asegurando que cada comando se ejecute con un objetivo claro, sin bloqueos en la interfaz y produciendo evidencia accionable.

---

## 2. Arquitectura del Arsenal Threat Hunting (Tab 5)

La barra de herramientas del Cockpit está segmentada en tres capas funcionales:

```mermaid
flowchart TD
    subgraph CAPA 1: Inteligencia de Amenazas [CTI Intel & Reputación]
        A1["Tri-Scan CTI"]
        A2["AbuseIPDB v2"]
        A3["VirusTotal v3"]
        A4["URLScan.io"]
        A5["NVD CVE"]
    end

    subgraph CAPA 2: Red & Perímetro [Network Recon & Live Probing]
        B1["WHOIS Forense Maestro"]
        B2["DNS Inteligente + DNSBL"]
        B3["PTR Reverso"]
        B4["Ping & Sondeo de Puertos"]
        B5["CURL (Banner Grabbing)"]
    end

    subgraph CAPA 3: Respuesta & Gobernanza [Incident Response & Remediation]
        C1["Grep Casos Históricos"]
        C2["Generador de Reportes de Abuso"]
        C3["Security Onion Pivot"]
        C4["Sandboxes Externas"]
    end

    CAPA 1 --> CAPA 2
    CAPA 2 --> CAPA 3
```

---

## 3. Matriz Operativa de Herramientas: ¿Cuándo y Cómo Usar Cada Una?

| Botón / Herramienta | Tipo de Observable | Tecnología Subyacente | ¿Cuándo DEBO usarlo? | Salida Esperada & Criterio SOC |
| :--- | :--- | :--- | :--- | :--- |
| **Tri-Scan CTI** | IP, Dominio, URL, Hash | Consulta asincrónica en hilos paralelos a **AbuseIPDB**, **VirusTotal** y **URLScan**. | **En el primer segundo del incidente.** Es el disparador universal de triaje inicial. | Tarjeta visual con Veredicto consolidado, porcentaje de abuso, ratio de motores y enlace directo a escaneos. |
| **AbuseIPDB** | IPv4 / IPv6 pública | API v2 con autenticación Bearer y caching local. | Al recibir alertas de firewall por **fuerza bruta (SSH, RDP, Web)** o **escaneo masivo de puertos**. | • **Score > 20%:** Sospechoso.<br>• **Score > 80%:** Atacante activo confirmado.<br>• Muestra ISP, número de reportes acumulados y fecha del último ataque. |
| **VirusTotal** | IP, Dominio, URL o Hash (MD5, SHA1, SHA256) | API v3 REST con consulta de reputación en +90 motores de ciberseguridad. | • Al analizar **hashes de ejecutables o scripts**.<br>• En dominios o URLs sospechosas de phishing o C2.<br>• Para contrastar detecciones de motores EDR. | • **0/90:** Observable limpio / sin firmas.<br>• **≥ 3/90:** Confirmación de amenaza (Malware / Phishing).<br>• Identifica familias de malware y campañas. |
| **WHOIS** | IP o Dominio | Motor forense multi-fuente ([`whois_recon.py`](file:///g:/SOC/soar/whois_recon.py)): RIPEstat, RDAP, BGP Routing, Geolocation y RIRs (LACNIC, RIPE, ARIN, APNIC, AFRINIC). | Cuando necesitas **identificar al propietario legal**, el proveedor de tránsito (BGP ASN) y los **buzones de abuso oficiales** para denuncias. | Desglose completo: Subred `inetnum`, ASN de enrutamiento BGP, Registrador, País de origen y correos electrónicos de abuso (`abuse@...`). |
| **DNS** | IP o Dominio | • **En IPs:** Resolución inversa PTR + Consulta DNSBL contra **Spamhaus ZEN** (`zen.spamhaus.org`).<br>• **En Dominios:** Resolución estructurada de registros **A, AAAA, MX, NS y TXT**. | • Para dominios: verificar hacia qué IPs apunta y qué servidores de correo (`MX`) tiene.<br>• Para IPs: comprobar si figura en listas negras globales o si tiene hostname asignado. | • **Spamhaus Listada:** IP catalogada como fuente activa de spam, malware o botnets.<br>• **TXT:** Permite auditar registros SPF (`v=spf1`) y claves de autenticación. |
| **PTR** | Dirección IP | Resolución DNS inversa estricta (Tipo PTR) vía servidores recursivos globales (`8.8.8.8` / `1.1.1.1`). | Para identificar si la IP tiene un hostname FQDN asignado que delate su función (ej: `mail.servidor.com`, `vpn.banco.com`, `dyn.ip.telecom.com`). | • **Hostname resuelto:** Revela si es servidor corporativo o residencial dinámico.<br>• **NXDOMAIN:** Común en proxies compartidos, WAFs (Cloudflare) y VPS de ataque. |
| **Ping (Conexión)** | IP o Hostname | 1. ICMP Ping rápido (2 paquetes, 1s timeout).<br>2. Sondeo perimetral de puertos TCP comunes: **80 (HTTP), 443 (HTTPS), 22 (SSH), 3389 (RDP), 8080 (Alt-Web)** con timeout estricto de 600ms por socket. | Para determinar si el host atacante **sigue encendido** y qué puertos de servicio tiene expuestos directamente a Internet. | **Completado en menos de 2.5s:**<br>• `ICMP: ALCANZABLE` $\rightarrow$ La máquina responde a red.<br>• `Puerto 22 ABIERTO` $\rightarrow$ Servidor Linux administrable.<br>• `Puerto 3389 ABIERTO` $\rightarrow$ Servidor Windows RDP expuesto. |
| **CURL** | URL o IP pública | Consulta HTTP/HTTPS mediante `curl.exe -I` con limitación estricta de tiempo (`--connect-timeout 3 --max-time 6`). Prueba HTTPS (443) y fallback automático a HTTP (80). | Cuando se sospecha de un **sitio web malicioso, portal clonado o endpoint C2** y se quiere inspeccionar la respuesta del servidor sin descargar el cuerpo de la página. | Extrae las cabeceras HTTP del servidor:<br>• `Server: ...` (Apache, nginx, IIS, Caddy)<br>• `Location: ...` (Detección de redirecciones maliciosas)<br>• Códigos de estado: `200 OK`, `301/302 Redirect`, `403 Forbidden`, `404 Not Found`. |
| **URLScan** | URL, Dominio o IP | Consulta a la API de búsqueda pública de URLScan.io. | Para inspeccionar sitios web sospechosos de phishing **sin interactuar directamente con ellos**, visualizando capturas de pantalla previas y tecnologías cargadas. | • **Con escaneos:** Muestra título de página, IP de hosting, servidor web y enlace a la auditoría visual completa.<br>• **Sin escaneos:** Ficha limpia indicando que la IP no aloja sitios web públicos indexados. |
| **NVD CVE** | Identificador de vulnerabilidad (`CVE-AAAA-NNNNN`) | API 2.0 del National Vulnerability Database (NIST) con cálculo automático de CVSS v3.1 y v2.0. | Cuando un log de firewall o EDR menciona un exploit o intento de vulnerabilidad conocida (ej. `CVE-2024-3400`, `CVE-2023-46805`, `CVE-2021-44228`). | Muestra score CVSS (0.0 a 10.0), severidad normalizada, vector de ataque, debilidad CWE asociada y enlaces a parches oficiales. |
| **Grep Casos** | Cualquier IOC (IP, Dominio, Hash) | Búsqueda recursiva en disco local sobre informes pasados, playbooks, bitácoras y archivos JSON/Markdown del entorno SOAR. | Para responder la pregunta clave: **¿Esta IP o dominio ya nos había atacado antes?** | Lista los archivos de casos anteriores donde apareció el IOC junto con el número de línea y contexto, acelerando la correlación de campañas. |

---

## 4. Flujo Maestro de Triaje Rápido en 4 Fases (< 2 Minutos)

Este es el procedimiento estándar que debe ejecutar el analista frente a cualquier alerta perimetral o IOC sospechoso:

```
                      [LOG O ALERTA DE AMENAZA]
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ FASE 1: REPUTACIÓN Y SEVERIDAD (CTI)                            │
│ 1. Ingresar la IP o dominio en el campo "Objetivo".             │
│ 2. Clic en "Tri-Scan CTI" (o AbuseIPDB + VirusTotal).           │
│    ➜ ¿Score de abuso > 80%?                                     │
│    ➜ ¿Múltiples motores lo marcan como malicioso?               │
│    • SÍ: Confirmado atacante / IOC malicioso. Proceder a Fase 2.│
│    • NO: Verificar si pertenece a infraestructura legítima (CDN)│
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ FASE 2: ATRIBUCIÓN E INFRAESTRUCTURA LEGAL                      │
│ 1. Clic en "WHOIS".                                             │
│    ➜ Identificar Registrante de la Subred (inetnum).            │
│    ➜ Identificar Titular del Sistema Autónomo (BGP ASN).        │
│    ➜ Anotar el buzón oficial de abuso (abuse@...).              │
│ 2. Clic en "DNS".                                               │
│    ➜ ¿Tiene PTR declarado?                                      │
│    ➜ ¿Aparece listado en Spamhaus ZEN DNSBL?                    │
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ FASE 3: AUDITORÍA DE RED Y ESTADO DEL OBJETIVO                  │
│ 1. Clic en "Ping" (Diagnóstico Perimetral).                     │
│    ➜ ¿Responde a ICMP?                                          │
│    ➜ ¿Qué puertos tiene abiertos? (22 SSH, 80/443 Web, 8080)    │
│ 2. Si tiene puerto web abierto: Clic en "CURL".                 │
│    ➜ Inspeccionar cabeceras HTTP y banner del servidor.         │
│ 3. Clic en "Grep Casos".                                        │
│    ➜ ¿Apareció en incidentes de la semana pasada?               │
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ FASE 4: CONTENCIÓN Y ACCIÓN DE RESPUESTA                        │
│ 1. Clic en "Generar Reporte de Abuso".                          │
│    ➜ Valida doble titularidad (Subred + BGP ASN).               │
│    ➜ Genera plantilla formal en inglés con logs técnicos.       │
│    ➜ Envío automático o exportación para el ISP responsable.    │
│ 2. Enviar indicador a Lista Negra en Firewall / Fortigate / XDR.│
│ 3. Documentar y cerrar caso con clasificación de severidad P1-P4│
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. Caso de Estudio Real: Ataque Brute Force en IP `217.60.242.76`

Durante el turno de guardia, el firewall perimetral FortiGate generó la siguiente alerta crítica:
- **Evento:** `Brute force attack PORT_3000`
- **IP Origen:** `217.60.242.76` (Puerto origen 57250)
- **IP Destino:** `190.128.219.210` (Puerto destino 3000)
- **Acción:** `deny` por política `Block_Countries`

### Paso 1: Triaje CTI
- **AbuseIPDB:** Confianza de Abuso **100%**. 197 reportes acumulados por ataques de fuerza bruta en las últimas 24 horas.
- **VirusTotal:** 6/92 motores clasifican la IP como maliciosa.

### Paso 2: Análisis Forense de Propiedad (WHOIS)
Al ejecutar el nuevo motor WHOIS forense se identificó el fenómeno de **Doble Titularidad**:
1. **Titular de la Subred (RIPE RDAP `inetnum: 217.60.242.0/24`):**
   - Organización: `Cat Communication Networks LTD` (Londres, Reino Unido).
   - Buzón de abuso asignado: `abuse@catlabs.llc`.
2. **Titular del Sistema Autónomo BGP (ASN 218970):**
   - Entidad legal anunciante: `Amin NezhadKahnoji` (Emiratos Árabes Unidos).
- **Acción del SOAR:** El módulo de reportes unificó ambas entidades en el asunto:  
  `Brute force attack PORT_3000 - 217.60.242.76 [Cat Communication Networks LTD / Amin NezhadKahnoji]`  
  y dirigió la notificación al buzón legal `abuse@catlabs.llc`.

### Paso 3: Diagnóstico de Red (Ping & CURL)
- **Ping:**
  - ICMP Echo: `ALCANZABLE` (El host sigue activo en Internet).
  - Puerto 80/TCP: `Cerrado / Filtrado`
  - Puerto 443/TCP: `Cerrado / Filtrado` (Explica por qué los curls ciegos a HTTPS se colgaban).
  - **Puerto 22/TCP (SSH): `ABIERTO`** (Servidor Linux activo).
  - **Puerto 8080/TCP (Web Alternativo): `ABIERTO`**.
- **CURL:** Al probar el puerto 8080 (`curl.exe -I http://217.60.242.76:8080`), el servidor respondió de inmediato:  
  `HTTP/1.1 404 Not Found` (Servicio web Go/Node escuchando).

---

## 6. Guía de Interpretación de Hallazgos Técnicos (FAQ de Red)

### ¿Qué significa si el Ping ICMP falla pero los puertos TCP responden?
Muchos servidores cloud (AWS, Azure, DigitalOcean) y firewalls empresariales **bloquean por defecto los paquetes ICMP Echo Request (Ping)** para evitar ser descubiertos en barridos automatizados. Sin embargo, los servicios TCP (como HTTP en el 80/443 o SSH en el 22) siguen abiertos y funcionando. Por eso el nuevo botón **Ping** del Cockpit no se limita al ping clásico: ejecuta un sondeo de sockets TCP perimetrales.

### ¿Qué significa que el registro PTR devuelva NXDOMAIN?
Un error `NXDOMAIN` en la consulta PTR significa que el proveedor de hosting o el propietario de la IP **no ha configurado una zona inversa DNS en su servidor de nombres**. Esto es muy común en:
- Rangos residenciales o de conexiones móviles.
- VPS baratos contratados por atacantes para desplegar bots.
- IPs de proxies compartidos.  
Por el contrario, los servidores de correo legítimos o sedes corporativas **siempre** tienen un registro PTR válido configurado (ej: `mail.dominio.com`).

### ¿Qué hacer si URLScan muestra "Sin escaneos públicos previos"?
URLScan.io indexa únicamente páginas que han sido enviadas para su análisis por analistas de seguridad o rastreadores automatizados. Si una IP atacante se dedica exclusivamente a escanear puertos, lanzar ataques de fuerza bruta por SSH o lanzar exploits por puertos no web, **no tendrá historial en URLScan**. Esto no significa que sea segura; al contrario, refuerza la hipótesis de que se trata de una IP de ataque y no de un sitio web público.

### ¿Cuándo debo enviar un Reporte de Abuso formal?
El envío de denuncias de abuso a proveedores upstream (`abuse@...`) está recomendado cuando:
1. El ataque está dirigido a activos críticos de la organización (fuerza bruta repetitiva, escaneo de vulnerabilidades, intentos de acceso no autorizado).
2. La IP tiene reportes activos recientes y el proveedor es un ISP reconocido (Hetzner, OVH, Linode, AWS, DigitalOcean, RIPE NCC).
3. Se cuenta con el log crudo con fecha, hora en UTC, IP origen, puerto y payload bloqueado.

---

## 7. Historial de Optimizaciones Técnicas del Cockpit

| Versión | Componente | Optimización Realizada |
| :--- | :--- | :--- |
| **v2.8.4** | `command_center.py` | Implementación de timeouts estrictos (`--connect-timeout 3`) en CURL para evitar bloqueos por puertos filtrados. |
| **v2.8.4** | `command_center.py` | Reemplazo de `Test-NetConnection` por sondeo socket asincrónico ultrarrápido (ICMP + TCP 80, 443, 22, 3389, 8080). |
| **v2.8.4** | `command_center.py` | Enrutamiento inteligente en DNS: consulta PTR + Spamhaus ZEN DNSBL para IPs; A, MX, NS y TXT para dominios. |
| **v2.8.4** | `command_center.py` | Interceptación de observables no CVE en el botón NVD CVE mediante diálogo de entrada guiada. |
| **v2.8.4** | `cti_engine.py` | Formateo elegante de estados `not_found` en URLScan y NVD NIST eliminando mensajes crudos de error HTTP 404. |
| **v2.8.4** | `whois_recon.py` | Creación del motor forense multi-fuente que fusiona RIPEstat, RDAP, BGP routing y doble titularidad. |
| **v2.8.4** | `abuse_report_dialog.py` | Concatenación automática de Subred Registrada y BGP ASN Legal Holder en el asunto de los reportes. |
