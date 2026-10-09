# Reporte de Incidente: Intento de Spear Phishing (Ticket #90540)

## Resumen Ejecutivo
- **Usuario Afectado:** Gisselle Aquino (`gisselleaquino@technoma.com.py`)
- **Remitente Malicioso:** `solana@evalartemail.com` (Solana Vargas)
- **Asunto:** `Re: pregunta rápida - Gisselle`
- **Estado del Incidente:** Resuelto (Riesgo Mitigado)
- **Brecha de Seguridad:** **NO HUBO BRECHA**. La cadena de ataque fue neutralizada en la fase de entrega/reconocimiento gracias a la correcta y veloz acción de la usuaria.

## 1. Análisis de Infraestructura Atacante (Origen y Threat Intel)
Los registros de auditoría exportados de Google Workspace, cruzados con fuentes de inteligencia de amenazas (OSINT), revelan la siguiente telemetría respecto al servidor origen del ataque:
- **Dirección IP (IPv6):** `2a01:111:f403:c408::3`
- **ISP / ASN:** Microsoft Limited (AS8075 - Data Center / Web Hosting)
- **Hostname:** `mail-centralindiaazlp170110003.outbound.protection.outlook.com`
- **Geolocalización:** Pune, Maharashtra, India (IN)
- **Dominio Asociado:** `evalartemail.com` 
- **Reputación de IP:** Registra **48 reportes previos de abuso** por actividades de SPAM.
  > *[!] Análisis de Táctica:* El atacante está utilizando infraestructura legítima de **Microsoft Office 365 (Exchange Online)** ubicada en un Data Center de la India. Esta técnica se utiliza comúnmente para evadir los filtros antispam iniciales de Google, ya que los correos viajan firmados y con alta reputación inherente a los servidores corporativos de Microsoft.
  > *Nota: En la investigación paralela se detectaron intentos similares ("Cinco empresas para Technoma") desde el dominio `autonomousleadco.info`, operando con la misma táctica.*

## 2. Línea de Tiempo del Incidente (2 de Julio de 2026)
A continuación, se detalla la cronología exacta de los hechos basada en los eventos crudos registrados en el tenant de Google Workspace de Technoma:

| Hora (UTC-3) | Evento Registrado (Workspace) | IP Origen | Análisis Forense (Explicación del Analista) |
| :--- | :--- | :--- | :--- |
| **15:02:30** | `Se ha recibido` | `2a01:111:f403:c408::3` (India) | El servidor de Google recibe el correo fraudulento y lo clasifica inicialmente como "Limpio", depositándolo en el buzón. |
| **15:10:35** | `Abrir` | `190.104.178.146` (Paraguay) | La usuaria interactúa con el correo y procede a abrirlo en su cliente/navegador. |
| **15:11:02** | `Ver` | `190.104.178.146` (Paraguay) | La usuaria permanece leyendo el contenido del mensaje durante aproximadamente 30 segundos. |
| **15:11:16** | `Los usuarios lo han clasificado como spam` | N/A | **[ACCIÓN DEFENSIVA]** Gisselle detecta la suplantación de identidad y reporta proactivamente el correo como SPAM dentro de la plataforma. |
| **23:35:17** | `Eliminar` | N/A | La usuaria elimina permanentemente el correo de su bandeja/papelera, erradicando el elemento malicioso. |

## 3. Threat Hunting & Telemetría Interna (Security Onion)
Para descartar cualquier riesgo oculto de ejecución de *malware* secundario o compromiso de credenciales por un posible click involuntario en algún enlace, se ejecutó una cacería de amenazas (Threat Hunting) en el SIEM corporativo (Security Onion) sobre el equipo de la usuaria afectada.

- **Usuario de Red (AD):** `giselleaquino`
- **IP Local (WiFi_Corp):** `192.168.169.124`
- **Hallazgos:** Durante y posterior a la ventana de tiempo crítica (15:10 a 15:15 hs), los logs de auditoría del Firewall (FortiGate) no registraron ninguna conexión saliente hacia puertos no estándar, dominios de Comando y Control (C2), ni tráfico anómalo asociado a la descarga de *payloads*. 
- **Conclusión Técnica:** El comportamiento de red del equipo se mantuvo exclusivamente dentro de los parámetros de tráfico legítimo de Directorio Activo (SMB/LDAP). 

## 4. Conclusión y Acciones de Contención Ejecutadas
Acorde al Playbook de Respuesta a Incidentes para la categoría de *(SPAM) Correo malicioso o no deseado*:

1. **Contención aplicada:** Se recomienda/aplicó el bloqueo global de los dominios emisores (`evalartemail.com` y `autonomousleadco.info`) a nivel de pasarela Antispam / Google Workspace.
2. **Cierre:** Al no haber materialización del daño en la infraestructura, sumado a la contención técnica ya mencionada, el incidente cumple con las condiciones del procedimiento para darse por cerrado y resuelto de manera exitosa.

## 5. Inteligencia de Amenazas Extendida (Investigación Secundaria)
Como parte del análisis proactivo, se investigó el segundo dominio asociado a esta campaña de Phishing (`autonomousleadco.info`), arrojando los siguientes resultados de infraestructura atacante alterna:
- **Dirección IP (IPv4):** `209.85.220.41`
- **ISP / ASN:** Google LLC (AS15169 - Data Center)
- **Hostname:** `mail-sor-f41.google.com`
- **Reputación de IP:** Registra **357 reportes de abuso** recientes en bases de datos comunitarias (AbuseIPDB), específicamente asociados a campañas de Spam, Phishing y suplantación de marcas (ej: McAfee).
- **Señuelo Web (Web Server):** A diferencia del primer dominio, `autonomousleadco.info` posee un servidor web activo configurado con un redireccionamiento HTTP 301 (oculto tras los WAF de Cloudflare) que desvía el tráfico hacia el dominio `https://www.highticket.agency/`.
  > *[!] Análisis de Táctica:* Para este segundo vector, el actor de amenazas no usó Microsoft, sino que contrató licenciamiento empresarial de **Google Workspace**. Al enviar correos desde `smtp.google.com`, aprovechan la "lista blanca" implícita de IPs corporativas de Google, sorteando nuevamente los filtros de seguridad del receptor bajo el amparo de firmas SPF/DKIM legítimas.

## 6. Anexo: Evidencias de Ejecución (OSINT)
Para respaldar la investigación, a continuación se adjuntan las salidas en crudo de los comandos ejecutados desde la terminal del Analista SOC para la extracción de metadatos de los dominios atacantes.

### Dominio 1: evalartemail.com (Microsoft 365)
**Comando:** `Resolve-DnsName -Type TXT evalartemail.com`
```text
Name                                     Type   TTL   Section    Strings                                  
----                                     ----   ---   -------    -------                                  
evalartemail.com                         TXT    59    Answer     {v=spf1 include:spf.protection.outlook.com -all} 
```

**Comando:** `nslookup 2a01:111:f403:c408::3`
```text
Nombre:  mail-centralindiaazlp170110003.outbound.protection.outlook.com
Address:  2a01:111:f403:c408::3
```

**Comando:** `curl.exe -I -k https://evalartemail.com`
```text
curl: (6) Could not resolve host: evalartemail.com
```
*(Nota del Analista: El dominio no posee registro 'A' ni servidor web configurado; su único propósito es la emisión unidireccional de correos maliciosos).*

### Dominio 2: autonomousleadco.info (Google Workspace)
**Comando:** `Resolve-DnsName -Type TXT autonomousleadco.info`
```text
Name                                     Type   TTL   Section    Strings                                  
----                                     ----   ---   -------    -------                                  
autonomousleadco.info                    TXT    300   Answer     {v=spf1 include:_spf.google.com ~all}    
```

**Comando:** `nslookup 209.85.220.41`
```text
Nombre:  mail-sor-f41.google.com
Address:  209.85.220.41
```

**Comando:** `curl.exe -I -k https://autonomousleadco.info`
```text
HTTP/1.1 301 Moved Permanently
Location: https://www.highticket.agency/
Server: cloudflare
```
*(Nota del Analista: A diferencia del anterior, este dominio funciona como un "Señuelo Web" activo que redirecciona el tráfico hacia una supuesta agencia, ocultando su infraestructura real detrás de los proxies de Cloudflare).*

### Dominio 3 (Destino final de redirección): highticket.agency
> *Este dominio no envió ningún correo a Technoma. Fue descubierto como destino oculto de la redirección HTTP 301 de `autonomousleadco.info` y se investigó para determinar si alojaba malware o un panel de robo de credenciales.*

**Justificación del análisis:** El simple `301 Moved Permanently` detectado en el paso anterior no era suficiente para clasificar el incidente. Un sitio de phishing puede usar redirecciones como capa de evasión (mostrar algo inocente al scanner, y servir malware al usuario real). Por eso se ejecutó un segundo comando `curl` con parámetro `-sL` para seguir la cadena de redireccionamientos y leer el código fuente real de la página de destino de forma segura desde la terminal, sin exponer el navegador.

**Nota sobre la alerta de Cortex XDR (Alert ID: 127599):** Este comando generó una segunda alerta en Cortex XDR (`curl.exe` conectándose a `www.highticket.agency`). Dicha alerta es un **Verdadero Positivo Benigno (BTP)**: la herramienta funcionó correctamente al detectar un LOLBin (`curl.exe`) conectándose a un dominio nunca antes visto en la red. La ejecución fue autorizada por el Analista SOC en el marco de la investigación del ticket #90540.

**Comando:** `Resolve-DnsName -Type A highticket.agency`
```text
highticket.agency    A    300    Answer    198.202.211.1
```

**Comando:** `Resolve-DnsName -Type TXT highticket.agency`
```text
highticket.agency    TXT    300    {v=spf1 include:spf.protection.outlook.com -all}
highticket.agency    TXT    300    {google-site-verification=Idtq5VWvMtiab2q9wjOI4HcSOUEs62xziwGQQYPit-Y}
highticket.agency    TXT    300    {facebook-domain-verification=3xmqw8tu5rqoy4f65lgug14b39g7o6}
highticket.agency    TXT    300    {MS=ms67470828}
```

**Comando:** `Resolve-DnsName -Type MX highticket.agency`
```text
highticket.agency    MX    300    highticket-agency.mail.protection.outlook.com
```

**Comando:** `curl.exe -I -k https://www.highticket.agency/`
```text
HTTP/1.1 200 OK
Date: Fri, 03 Jul 2026 09:53:20 GMT
Content-Type: text/html; charset=utf-8
Server: cloudflare
Strict-Transport-Security: max-age=31536000
```

**Comando:** `curl.exe -sL -k https://www.highticket.agency/ | findstr /i "<title>"`
```text
<title>HighTicket Agency — AI-Powered B2B Prospecting Engine</title>
```
*(Nota del Analista: El análisis del código fuente de la página de destino final descarta la presencia de un portal de robo de credenciales. Se trata de una agencia de marketing B2B construida en Webflow, con verificaciones de dominio en Google, Facebook y Microsoft. La infraestructura de correo de este dominio matriz también opera sobre Microsoft 365. Se confirmó que la campaña de `autonomousleadco.info` es Spear-SPAM comercial de esta agencia, y no Phishing destructivo. Ver Sección 7 para clasificación definitiva).*

## 7. Clasificación Definitiva de los Incidentes (Veredictos)
Es imperativo destacar que la profundidad del análisis forense revela que **estamos ante dos eventos aislados y de naturaleza distinta**, los cuales no pertenecen a la misma campaña, a pesar de que ambos evadieron los filtros iniciales usando infraestructuras de alta reputación:

1. **Incidente A (`evalartemail.com` - Microsoft 365):** Al tratarse de un dominio fantasma sin redirecciones comerciales ni sitio web activo, su perfil técnico táctico se alinea fuertemente con una campaña clásica de **Phishing (Credential Harvesting)**. El objetivo principal de este actor era engañar a la usuaria ("Re: pregunta rápida") para robar sus credenciales corporativas mediante un enlace fraudulento.
2. **Incidente B (`autonomousleadco.info` - Google Workspace):** La investigación OSINT descubrió que este dominio es una fachada que redirige a "HighTicket Agency" (una agencia de marketing B2B). Este evento se clasifica estrictamente como **Spear-SPAM (Marketing Engañoso Abusivo)**. Utilizan ingeniería social al borde de la ilegalidad para forzar la apertura de correos y vender servicios de "generación de leads", pero sin fines destructivos ni robo de contraseñas.

**Resumen:** Technoma fue blanco de un intento de robo de credenciales y, en paralelo, de una campaña de SPAM comercial ultra-agresivo. Ambos vectores fueron detectados oportunamente y mitigados con éxito sin ocasionar brechas de seguridad.

## 8. Investigación WHOIS (Paso 5 del Playbook — Responsables del Dominio)
De acuerdo al Playbook de Incidentes *(SPAM) Correo malicioso o no deseado*, **Paso 5**, se procedió a identificar a los responsables del dominio origen del Incidente A para su notificación.

### Dominio `evalartemail.com`
**Comando:** `whois evalartemail.com`

| Campo | Valor | Relevancia Forense |
|:---|:---|:---|
| **Fecha de creación** | 2026-02-10 (hace ~5 meses) | ⚠️ Dominio creado recientemente, patrón típico de dominios creados ad-hoc para ataques |
| **Registrador** | Dynadot Inc. (IANA ID: 472) | Responsable técnico del dominio |
| **Abuse Contact** | `abuse@dynadot.com` / +1.6502620100 | 🎯 **Destinatario del reporte según Playbook (Plantilla 03)** |
| **Titular real** | REDACTED FOR PRIVACY | El atacante contrató privacidad para ocultar su identidad |
| **Organización de privacidad** | Super Privacy Service LTD c/o Dynadot | Servicio usado deliberadamente para anonimizar la titularidad |
| **Name Servers** | ClouDNS (pns61-64) | DNS externo adicional para facilitar cambios rápidos si es detectado |
| **DNSSEC** | Unsigned | Sin firma de seguridad DNS |

### Dominio `autonomousleadco.info`
**Comando:** `whois -h whois.nic.info autonomousleadco.info` (vía RDAP)

| Campo | Valor | Relevancia Forense |
|:---|:---|:---|
| **Fecha de creación** | 2026-03-06 (hace ~4 meses) | ⚠️ Dominio creado recientemente — patrón idéntico al Incidente A |
| **Registrador** | Spaceship, Inc. (IANA ID: 3862) | Responsable técnico del dominio |
| **Abuse Contact** | `abuse@spaceship.com` / +1.6613102107 | 🎯 **Destinatario del reporte según Playbook (Plantilla 03)** |
| **Titular real** | REDACTED — "Withheld for Privacy ehf" | Servicio de privacidad con sede en **Islandia**, deliberadamente elegido por sus leyes de privacidad estrictas |
| **Name Servers** | `joaquin.ns.cloudflare.com` / `evelyn.ns.cloudflare.com` | Cloudflare como escudo DNS — consistente con la redirección HTTP 301 detectada |
| **DNSSEC** | Unsigned | Sin firma de seguridad DNS |

---

### 🔎 Análisis Comparativo de Ambos Dominios

| Indicador | `evalartemail.com` (Inc. A) | `autonomousleadco.info` (Inc. B) |
|:---|:---|:---|
| **Fecha de creación** | 10 Feb 2026 (~5 meses) | 06 Mar 2026 (~4 meses) |
| **Registrador** | Dynadot Inc. | Spaceship, Inc. |
| **Abuse Contact** | abuse@dynadot.com | abuse@spaceship.com |
| **Servicio de privacidad** | Super Privacy Service (EE.UU.) | Withheld for Privacy ehf (Islandia) |
| **DNS externo** | ClouDNS | Cloudflare |
| **DNSSEC** | Unsigned | Unsigned |
| **Sitio web activo** | ❌ No | ✅ Sí (redirige a highticket.agency) |

> **Conclusión del Análisis Comparativo:** Ambos dominios comparten el mismo patrón de comportamiento evasivo: creados recientemente, propietario oculto detrás de servicios de privacidad, DNS administrado por terceros, y DNSSEC no implementado. Esto confirma que, independientemente de si son el mismo actor o actores distintos, ambos emplean tácticas deliberadas de anonimización para dificultar su identificación y eventual acción legal.

---

## 9. Próximos Pasos del Playbook (Pendientes)
Según la fase de **Contención y Recuperación** del Playbook, una vez identificados los responsables, corresponde ejecutar las siguientes acciones en orden:

| # | Acción | Destinatario | Base del Playbook |
|:---|:---|:---|:---|
| 1 | Reportar abuso del dominio `evalartemail.com` | `abuse@dynadot.com` | Paso 5 + Plantilla 03 |
| 2 | Reportar abuso del dominio `autonomousleadco.info` | `abuse@spaceship.com` | Paso 5 + Plantilla 03 |
| 3 | Reportar abuso de infraestructura Microsoft 365 | `abuse@microsoft.com` | Paso 5 — Responsable ISP |
| 4 | Reportar abuso de infraestructura Google Workspace | `https://safebrowsing.google.com/safebrowsing/report_phish/` | Paso 5 — Responsable ISP |
| 5 | Notificar al CSIRT del país de origen (India) | `incident@cert-in.org.in` | Paso 5 — CSIRT responsable |
| 6 | Bloquear ambos dominios en Google Workspace Admin | Admin de Technoma | Contención interna |
| 7 | Cerrar ticket #90540 como Resuelto | Odoo | Paso 9 del Playbook |

---

## 10. Anexo: Correos de Reporte (Playbook Plantilla 03)
A continuación se adjuntan los borradores de los correos de notificación redactados según la Plantilla 03 del Playbook de Incidentes, listos para ser enviados a los responsables de las plataformas abusadas.

### Correo 1 — Registrador de evalartemail.com
**Destinatario:** `abuse@dynadot.com`
**Asunto:** Spam - Phishing - evalartemail.com - solana@evalartemail.com
```text
Hello,

We have detected that a domain registered under your authority is being 
used to send malicious phishing emails targeting our organization:

Domain: evalartemail.com
Registrar: Dynadot Inc.
Malicious account: solana@evalartemail.com
Sending infrastructure: Microsoft Exchange Online (AS8075)
Sending IP (IPv6): 2a01:111:f403:c408::3
Hostname: mail-centralindiaazlp170110003.outbound.protection.outlook.com
Geolocation: Pune, Maharashtra, India

The email was crafted using social engineering tactics ("Re: quick 
question - Gisselle") to impersonate a known contact and trick our 
users into disclosing corporate credentials.

The domain evalartemail.com was created on February 10, 2026, has no 
active web presence, and appears to have been registered exclusively 
for the purpose of sending phishing emails. The domain owner's identity 
is concealed behind a privacy service.

We kindly request that you investigate this matter and take the 
appropriate action, including suspension of the domain if the abuse 
is confirmed.

We would appreciate your collaboration to address this issue or forward 
this report to someone who can.

Best regards,
SOC Analyst — Technoma
```

### Correo 2 — Registrador de autonomousleadco.info
**Destinatario:** `abuse@spaceship.com`
**Asunto:** Spam - Unsolicited Commercial Email - autonomousleadco.info
```text
Hello,

We have detected that a domain registered under your authority is being 
used to send unsolicited commercial emails (Spear-SPAM) targeting our 
organization:

Domain: autonomousleadco.info
Registrar: Spaceship, Inc.
Sending infrastructure: Google Workspace / Gmail (AS15169)
Sending IP (IPv4): 209.85.220.41
Hostname: mail-sor-f41.google.com

The domain redirects all web traffic (HTTP 301) to:
https://www.highticket.agency/

The domain autonomousleadco.info was created on March 6, 2026, uses 
Cloudflare nameservers for obfuscation, and its owner's identity is 
concealed behind a privacy service (Withheld for Privacy ehf, Iceland).

The IP address 209.85.220.41 has been reported 357 times on AbuseIPDB 
for phishing, spoofing, and email spam within the last 30 days.

We kindly request that you investigate this matter and take the 
appropriate action, including suspension of the domain if the abuse 
is confirmed.

We would appreciate your collaboration to address this issue or forward 
this report to someone who can.

Best regards,
SOC Analyst — Technoma
```

### Correo 3 — Plataforma Abusada (Microsoft 365)
**Destinatario:** `abuse@microsoft.com`
**Asunto:** Phishing abuse via Microsoft 365 tenant - evalartemail.com
```text
Hello Microsoft Security Team,

We are reporting an active abuse of Microsoft Exchange Online 
infrastructure for phishing purposes targeting our organization.

Abusive tenant domain: evalartemail.com
Abusive account: solana@evalartemail.com
Sending IP (IPv6): 2a01:111:f403:c408::3
Hostname: mail-centralindiaazlp170110003.outbound.protection.outlook.com
ASN: AS8075 (Microsoft Limited)
Geolocation: Pune, Maharashtra, India
Date of incident: 2026-07-02 at 15:02:30 (UTC-3)
AbuseIPDB reports on sending IP: 48 reports

The attacker leveraged a legitimate Microsoft 365 subscription to send 
phishing emails using social engineering ("Re: quick question") to 
harvest corporate credentials from our users. By using Microsoft's 
trusted infrastructure, the emails bypassed our organization's initial 
spam filters.

We kindly request investigation and suspension of the abusive tenant 
associated with evalartemail.com.

For reporting security issues specific to traffic emanating from 
Microsoft Online Services, we are also submitting this report to:
https://cert.microsoft.com

Best regards,
SOC Analyst — Technoma
```

### Correo 4 — CERT Nacional (India)
**Destinatario:** `incident@cert-in.org.in`
**Asunto:** Phishing campaign originating from India - Microsoft Azure infrastructure
```text
Hello CERT-In Team,

We are reporting a phishing campaign that originated from infrastructure 
located in India and targeted our organization in Paraguay (South America).

Incident details:
- Type: Phishing / Credential Harvesting
- Date: 2026-07-02 at 15:02:30 UTC-3
- Sending IP (IPv6): 2a01:111:f403:c408::3
- ASN: AS8075 (Microsoft Limited — Exchange Online)
- Hostname: mail-centralindiaazlp170110003.outbound.protection.outlook.com
- Geolocation: Pune, Maharashtra, India (IN-MH)
- Malicious domain: evalartemail.com (registered Feb 10, 2026)
- Malicious account: solana@evalartemail.com

The attacker used a Microsoft 365 tenant (evalartemail.com) hosted in 
your jurisdiction to conduct a spear phishing campaign impersonating 
a known contact of our targeted user.

We have already notified Microsoft (abuse@microsoft.com) and the domain 
registrar (abuse@dynadot.com). We are sharing this information with 
your team for awareness and any further investigation you may consider 
appropriate.

We would appreciate your collaboration or any information you may have 
about this threat actor.

Best regards,
SOC Analyst — Technoma
```
