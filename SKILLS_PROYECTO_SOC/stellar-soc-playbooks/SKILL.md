---
name: stellar-soc-playbooks
description: Standard operating procedure (SOP) for Stellar Cyber XDR analysis, triage, and human-in-the-loop (HITL) incident response. Recommends the exact operational playbook (NIST SP 800-61 Rev.3 & MITRE ATT&CK) and waits for operator authorization before providing actionable containment steps.
metadata:
  origin: technoma-soc-elite
---

# Stellar Cyber XDR & SOC Playbooks Skill (HITL Guided Remediation)

Skill especializada para el análisis de incidentes en **Stellar Cyber OpenXDR** y la aplicación de los **28 Playbooks Operativos de Technoma SOC** basados en el marco **NIST SP 800-61 Rev.3 (Abril 2025) / CSF 2.0** y mapeo a técnicas **MITRE ATT&CK**.

---

## 🛡️ Filosofía Fundamental: Human-in-the-Loop (HITL)
1. **Detección y Recomendación Automática:** Al recibir telemetría de Interflow o datos de un caso, el agente **DEBE SIEMPRE** identificar y **recomendar el Playbook específico** que aplique a la amenaza.
2. **Barrera de Contención y Ejecución (Zero Action without Authorization):** El agente **NUNCA** emitirá comandos destructivos ni asumirá contención activa por su cuenta.
3. **Paso a Paso Bajo Autorización Expresa:** Los pasos técnicos de mitigación, aislamiento de red en EDR o comandos perimetrales **SOLO se desglosan en detalle cuando el analista otorgue su autorización explícita** ("autorizado", "proceder", "aplicar", "dame los pasos").

---

## 📋 Catálogo de los 28 Playbooks Operativos (Clasificación por Enfoque)

### 🔴 ENFOQUE REACTIVO: Triaje de Intrusión, Respuesta y Contención Activa
*Se activan tras una detección de amenaza activa, ejecución de malware o violación perimetral en curso.*

| Código | Playbook Operativo | Severidad | Mapeo MITRE ATT&CK |
| :---: | :--- | :---: | :--- |
| **PB-1.1** | Infecciones por Ransomware | P1 (Crítica) | T1486, T1566, T1133 |
| **PB-1.2** | Infecciones por Malware General | P2 (Alta) | T1566, T1204, T1059 |
| **PB-2.1** | Denegación de Servicio (DoS/DDoS) | P1 (Crítica) | T1498, T1499 |
| **PB-2.2** | Comportamiento Malicioso en la Red | P2 (Alta) | T1071, T1573 |
| **PB-2.3** | Ataques de Fuerza Bruta | P3 (Media) | T1110 |
| **PB-2.4a** | Inyección SQL (SQLi) | P2 (Alta) | T1190 |
| **PB-2.4b** | Cross-Site Scripting (XSS) | P2 (Alta) | T1059.007 |
| **PB-3.4** | Phishing y URLs Maliciosas | P2 (Alta) | T1566, T1566.001 |
| **PB-4.1** | Fuga de Información (Data Leak) | P1 (Crítica) | T1567, T1530 |
| **PB-5.1** | Servidor Web Comprometido y Defacement | P1 (Crítica) | T1491, T1505.003 |
| **PB-5.5** | Compromiso de Cuenta | P1 (Crítica) | T1078, T1550 |
| **PB-5.6a** | Comunicación con Servidor C2 (Command & Control) | P1 (Crítica) | T1071, T1573 |
| **PB-5.6b** | Escalada de Privilegios | P2 (Alta) | T1068, T1548 |
| **PB-5.6c** | Exfiltración de Datos (Genérico) | P2 (Alta) | T1041, T1048 |
| **PB-5.6d** | Exfiltración por Túnel ICMP | P2 (Alta) | T1048.003 |
| **PB-5.6e** | Sistema Comprometido (Tunelización DNS) | P2 (Alta) | T1071.004 |
| **PB-5.6f** | Ataque Interno de Denegación de Servicio (DoS) | P2 (Alta) | T1499 |

### 🟢 ENFOQUE PROACTIVO: Postura, Higiene de Red, Threat Hunting & Salud
*Se activan para prevenir brechas, corregir servicios expuestos o auditar telemetría antes de que ocurra una intrusión.*

| Código | Playbook Operativo | Severidad | Mapeo MITRE ATT&CK |
| :---: | :--- | :---: | :--- |
| **PB-2.4c** | Escaneo de Puertos y Vulnerabilidades | P3 (Media) | T1595, T1190 |
| **PB-3.2** | Gestión de Estafas (Scam) y Abuso de Marca | P3 (Media) | T1583, T1584 |
| **PB-5.2** | Configuración Débil y Servicios Vulnerables | P3 (Media) | T1133, T1021 |
| **PB-5.3** | Compromiso de Terceros (Supply Chain) | P1 (Crítica) | T1195 |
| **PB-5.4** | Tráfico No Cifrado con Credenciales en Texto Plano | P2 (Alta) | T1040, T1557 |
| **PB-5.6.1**| Detección y Respuesta a Movimiento Lateral (Hunting) | P1 (Crítica) | T1021, T1570 |
| **PB-6.1** | Agente Stellar Cyber no envía telemetría | P2 (Alta) | T1562.001 |
| **PB-6.2** | Sensor de Red Offline o sin tráfico | P2 (Alta) | T1562.001 |
| **PB-6.3** | Picos Anómalos de Ingesta / Licencia | P3 (Media) | N/A |
| **PB-6.4** | Brecha de Cobertura de Endpoint (Shadow IT) | P3 (Media) | T1562.001 |
| **PB-7.1** | Intentos Fallidos de Login (Auditoría SMB/RDP) | P3 (Media) | T1110, T1110.004 |

---

### 🏛️ PLAYBOOKS CERT-PY (Respuesta Forense, Escalación & Notificaciones Externas)
*Directrices oficiales del CSIRT Nacional para gestión formal, takedown perimetral, denuncias y comunicación con ISPs:*

| Código | Playbook CERT-PY | Severidad | Propósito Operativo / Forense |
| :---: | :--- | :---: | :--- |
| **CERT-01** | Ransomware (Gestión de Rescate & Decryptors) | P1 | Identificación vía ID-Ransomware / NoMoreRansom, escalación y análisis RDP/Phishing. |
| **CERT-02** | Acceso Indebido a Cuenta / Datos / Sistemas | P1 | Takedown de dumps de bases de datos, notificación O365 y revocación de credenciales. |
| **CERT-03** | Servidor Web Comprometido (Defacement / WebShell) | P1 | Aislamiento web, contacto con proveedor de hosting (`OrgAbuseEmail`) y erradicación. |
| **CERT-04** | SPAM / Correo Malicioso / Phishing Mail | P2 | Extracción de cabeceras RFC 822 (MXToolbox), reporte a Open-Relays y CSIRT de origen. |
| **CERT-05** | Phishing Web (Takedown & SafeBrowsing) | P2 | Verificación con proxy evasivo (`hide.me`), reporte a PhishTank, Google y nic.py. |
| **CERT-06** | Escaneo y/o Fuerza Bruta (Notificación ISP) | P3 | Verificación en bases de IoCs y notificación formal con extractos de logs al ISP. |
| **CERT-07** | Denegación de Servicio (DoS / DDoS) | P1 | Coordinación upstream con carriers para mitigación de tráfico amplificado NTP/DNS. |
| **CERT-08** | Malware (Análisis Dinámico Sandbox) | P2 | Ejecución controlada en Any.Run/FLOSS, extracción de hashes C2 y notificación técnica. |
| **CERT-09** | Equipo Comprometido (Alertas de Sinkholing) | P2 | Procesamiento de feeds Shadowserver, adquisición de memoria RAM e imagen forense. |
| **CERT-10** | Servicio Vulnerable / Exposición Crítica | P3 | Notificación formal a directores TIC por RDP expuesto a Internet o fallos de versión. |

---

## 🔄 Protocolo de Triaje Obligatorio

Cuando se presente un caso o alerta de Stellar Cyber:

### Paso 1: Análisis Forense de la Telemetría
- Analizar observables (IPs, dominios, procesos, hashes, usuarios).
- Cruzar con la **Memoria Institucional** (activos conocidos, falsos positivos documentados).
- Determinar si el comportamiento es Falso Positivo (FP), True Positive (TP) o Benign.

### Paso 2: Recomendación del Playbook (Identificación de Naturaleza Operativa)
Indicar siempre en la salida:
```markdown
### 📘 Playbook Sugerido (Recomendación Automática)
* **Procedimiento:** [Código y Nombre del Playbook, ej. PB-3.4 Phishing y URLs Maliciosas]
* **Enfoque Operativo:** [🔴 Reactivo (Respuesta & Contención)  |  🟢 Proactivo (Postura & Higiene / Hunting)]
* **Prioridad / Severidad:** [P1, P2 o P3]
* **Mapeo MITRE ATT&CK:** [Técnica, ej. T1566.001]
* **Objetivo Táctico:** [Breve síntesis de qué previene o mitiga este playbook]
* **Estado HITL:** ⏳ *En espera de autorización del operador ("autorizo", "procede", "dame los pasos") para detallar y ejecutar los pasos de remediación.*
```

### Paso 3: Ejecución de Remediación (Solo si el Operador Autoriza)
Una vez que el usuario diga "autorizo", "procede", "dame los pasos" o similar:
Desplegar la guía táctica paso a paso extraída de los playbooks oficiales:
1. **Fase 1: Validación y Clasificación** (Queries exactas a ejecutar en Stellar Cyber / Interflow).
2. **Fase 2: Contención Inmediata** (Aislamiento de host en consola EDR, bloqueo perimetral en firewall FortiGate, o revocación de credenciales).
3. **Fase 3: Erradicación y Análisis Causa Raíz** (Análisis forense de memoria, logs de eventos o sandbox).
4. **Fase 4: Cierre Formal y Plantilla de Notificación** (Texto listo para copiar y pegar en el sistema de tickets con veredicto justificado).
