# ARQUITECTURA DE SUITE DE INVESTIGACIÓN AUTOMATIZADA: THREAT HUNTING 360°

**Diseño de Flujo y Matriz de Decisión para el Analista SOC (Kevin Moraes)**  
**Integración:** Consola Threat Hunting GUI (`terminal_cti_mixin.py`), Bot Telegram (`telegram_soc_bot.py`) y CLI (`soar_cli.py`).

---

## 1. Visión General: El Botón "Auto-Investigar 360°"

Actualmente en la consola gráfica tenés más de 15 botones individuales (`DNS`, `PTR`, `WHOIS`, `Ping`, `CURL`, `Grep Casos`, `Tri-Scan CTI`, `Anti-Spoofing`, `Desemmascarar Origen`, `DNS Twist`, `MxToolbox`, `AbuseIPDB`, `VirusTotal`, `URLScan`, `NVD CVE`).

El objetivo es tener un **Orquestador Inteligente de Disparo Único** que detecte automáticamente el tipo de observable ingresado en el campo `🎯 Objetivo:` y dispare en cadena y en paralelo exactamente la batería de herramientas que corresponde, sintetizando el veredicto sin que tengas que apretar 5 botones distintos.

```
                         [ INGRESO DE OBSERVABLE ]
                                     │
                    ┌────────────────┴────────────────┐
                    ▼                                 ▼
           [ ES UNA IP ]                      [ ES UN DOMINIO / URL ]
                    │                                 │
         ┌──────────┴──────────┐           ┌──────────┴──────────┐
         ▼                     ▼           ▼                     ▼
     [ PRIVADA ]           [ PÚBLICA ]  [ PAAS / SAAS ]     [ DOMINIO PROPIO ]
     (LAN / VPN)           (Internet)   (Netlify/Vercel)    (Corporativo/Atacante)
```

---

## 2. Flujo de Investigación Automatizado: Rama IP

### Caso 2.1: IP Privada (RFC 1918: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`)
> **Regla de Oro:** NUNCA consultar VirusTotal, AbuseIPDB ni URLScan con una IP privada (filtración de topología interna y consumo inútil de cuota de API).

* **Batería de Herramientas que se dispara:**
  1. `PTR Local / NetBIOS`: Resolución de hostname interno (`Resolve-DnsName -Type PTR`).
  2. `Grep Casos / Bitácora`: Búsqueda de apariciones previas en incidentes y tickets locales.
  3. `Stellar Cyber Data Lake Search`:
     - Últimas 24h de conexiones entrantes y salientes (`srcip` o `dstip`).
     - MAC address, Asset ID, sistema operativo y usuario asociado en Stellar/Cortex.
     - Detección de puertos activos y protocolos usados (ej. 445 SMB, 5985 WinRM, 3389 RDP).
  4. `Ping / Port Sweep Rápido`: Verificación de si el host interno está activo y escuchando en puertos de administración.

### Caso 2.2: IP Pública (Internet)
* **Batería de Herramientas que se dispara:**
  1. `PTR Inverso & WHOIS / ASN`: Identificar proveedor de hosting (AWS, Cloudflare, DigitalOcean, Copaco, Tigo, etc.).
  2. `AbuseIPDB API`:
     - Score de abuso (0% a 100%), cantidad de reportes y categorías de ataque (SSH brute-force, web scan, spam).
  3. `VirusTotal API`:
     - Detecciones en 92 motores AV, tags de malware asociados y Passive DNS (dominios que resolvieron a esa IP).
  4. `DNSBL (Spamhaus ZEN)`:
     - Verificación instantánea si la IP está en listas negras de spam o botnets.
  5. `Stellar Cyber Correlación Interna`:
     - ¿Quién de nuestra red habló con esta IP? (Hosts internos, puertos, bytes transferidos, firmas IDS asociadas).
  6. `CURL Headers (si responde en puerto 80/443)`:
     - Extracción de cabeceras HTTP Server, X-Powered-By y códigos de estado.

---

## 3. Flujo de Investigación Automatizado: Rama Dominio / URL

### Caso 3.1: Subdominio en Plataforma PaaS / Multi-Inquilino Pública
*(Detectado automáticamente si el dominio raíz es: `netlify.app`, `vercel.app`, `github.io`, `pages.dev`, `firebaseapp.com`, `azureedge.net`, `s3.amazonaws.com`, etc.)*
* **Comportamiento Quirúrgico:**
  - **OMITIR:** Barrido pasivo de subdominios en el dominio raíz (evita falsos positivos contra la infraestructura de Netlify/Vercel).
  - **OMITIR:** Análisis SPF/DMARC en el subdominio (las plataformas PaaS no gestionan correo saliente desde subdominios efímeros).
* **Batería de Herramientas que se dispara:**
  1. `Resolución A / AAAA`: Extraer las IPs de balanceo/CDN del proveedor.
  2. `URLScan.io API`: Búsqueda histórica de capturas, veredicto y estado actual del sitio (200 OK vs 404 Takedown).
  3. `VirusTotal & ANY.RUN CTI`: Consultar historial de muestras de malware o phishing asociadas a ese subdominio.
  4. `Stellar Cyber DNS Interflow`: Buscar qué notebooks internas resolvieron este subdominio y en qué fechas.

### Caso 3.2: Dominio Propio / Desconocido (Posible Infraestructura C2 o Phishing Privado)
* **Batería de Herramientas que se dispara de una vez:**
  1. `Desemmascarar Origen (Bypass Cloudflare)`:
     - Detección de fugas en registros MX (`_dc-mx`), SPF `ip4:` y barrido de subdominios sin proxy (`mail.`, `direct.`, `cpanel.`, `origin.`).
  2. `Anti-Spoofing (SPF, DMARC, MX)`:
     - Evaluación de protección contra suplantación de identidad para campañas de correo.
  3. `DNS Twist / Typosquatting`:
     - Si es un dominio corporativo similar a Technoma o clientes, comprobar homóglifos o lookalikes registrados por atacantes.
  4. `Tri-Scan CTI (VT + URLScan + AbuseIPDB)`:
     - Consulta combinada de reputación global.
  5. `Stellar Cyber Data Lake`:
     - Comprobación de solicitudes DNS en toda la red corporativa.

---

## 4. Matriz Rápida: ¿Qué combinación usar según el evento?

| Tipo de Alerta o Evento | Combinación Óptima de Herramientas | Resultado Esperado |
| :--- | :--- | :--- |
| **Alerta IDS: Escaneo de Puertos / Fuerza Bruta (ej. Nmap, MySQL 3306)** | `IP Flow` ➔ `PTR Local` ➔ `Grep Casos` ➔ `Stellar Logins` | Saber si es un host interno (ej. pentest de Saucedo) o un atacante perimetral externo. |
| **Alerta IDS: Consulta DNS Sospechosa / Phishing (ej. Netlify, .su, .top)** | `Dominio Flow` ➔ `URLScan.io` ➔ `VirusTotal` ➔ `Stellar ADR (Tráfico Web)` | Saber si la landing sigue viva o cayó, y si el usuario local transfirió credenciales por POST. |
| **Correo Sospechoso / Reporte de Phishing de Usuario (.eml)** | `Analizador Cabeceras` ➔ `Anti-Spoofing (SPF/DMARC)` ➔ `MxToolbox` ➔ `URLScan` | Verificar si el remitente fue falsificado (spoofing) y si los enlaces del correo son maliciosos. |
| **Alerta C2 / Beaconing / Conexión Saliente Rara** | `Desemmascarar Origen` ➔ `AbuseIPDB` ➔ `WHOIS` ➔ `Pivotes OSINT (Shodan/ViewDNS)` | Encontrar la IP real del servidor de control del atacante detrás de proxies/Cloudflare. |
| **Alerta de Vulnerabilidad / CVE en Endpoint** | `NVD CVE` ➔ `Cortex XDR Process Query` | Medir CVSS, vector de ataque y si hay procesos vulnerables ejecutándose en el endpoint. |

---

## 5. Implementación en la Interfaz (Siguiente Paso)
Se agregará en la primera fila de la Consola Threat Hunting un botón principal:
`🚀 AUTO-INVESTIGAR 360°`
Al hacer clic con cualquier texto en el campo objetivo:
1. Identifica automáticamente si es `IP Privada`, `IP Pública`, `Subdominio PaaS`, `Dominio Raíz`, `URL` o `Hash SHA256`.
2. Dispara el flujo exacto correspondiente.
3. Genera un **Reporte Ejecutivo Integrado** en la consola con dictamen final: `BENIGNO`, `SOSPECHOSO` o `CRÍTICO`.
