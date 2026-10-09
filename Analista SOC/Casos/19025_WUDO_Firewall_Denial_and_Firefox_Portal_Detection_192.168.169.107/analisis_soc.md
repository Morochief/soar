# Informe de Análisis SOC - Lote Interflow (2 Eventos)
**ID del Caso:** `19025_WUDO_Firewall_Denial_and_Firefox_Portal_Detection_192.168.169.107`  
**Fecha de Análisis:** 2026-09-24 09:34:00 (UTC-03:00)  
**Analista Responsable:** Nivel 1 SOC / DFIR  
**Tenant / Organización:** `Technoma` (`cf73a415c8794884a0c35b458b7c73ae`)  
**Sensor / Firewall:** `technoma-sensor` (`4e3eab0649114a80a089a5d5a078994d`) / `FG-Technoma` (`FG120GTK24022543`)  

---

## 1. Declaración de Cantidad y Desglose del Lote
Se procesaron exactamente **2 eventos de seguridad** correlacionados en este lote de alertas nativas de Interflow:

1. **Evento 1 (`_seq_no: 19025`):** `internal_fw_action` (Internal Firewall Denial Anomaly) en FortiGate `FG-Technoma`. Bloqueo de 335 intentos de conexión TCP 7680 (Windows Update Delivery Optimization - WUDO) desde `192.168.15.16` (VLAN-15) hacia `192.168.169.107` (`WiFi_Corp`).
2. **Evento 2 (`_seq_no: 19054`):** `new_registered_domain` (Recently Registered Domains) vía DNS. Consulta desde `192.168.169.107` (`WiFi_Corp`) al DC/DNS `10.11.1.1` por el dominio oficial `firefox-portal-detection.com`.

---

## 2. Análisis Individual de Eventos

### Evento 1: Bloqueo de Conexiones P2P WUDO en Firewall (TCP 7680)
- **ID de Alerta:** `433df633-cf12-4542-8de2-fc52dd51c5ad1790251804238-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=`
- **Regla / Módulo:** `new_ml` (`internal_fw_action`)
- **Táctica / Técnica:** `XTA0002` (XDR NBA) / `XT2002` (XDR Firewall Anomaly) - Kill Chain: `Exploration`
- **Origen:** `192.168.15.16:55519` (VLAN-15, MAC `50:6b:8d:ec:30:fa`)
- **Destino:** `192.168.169.107:7680` (`WiFi_Corp`, Asset `b0fe715a-2224-11f1-818c-26eb39a0cd74`)
- **Servicio / Protocolo:** `tcp/7680` (Windows Update Delivery Optimization - WUDO) / Protocolo TCP (6)
- **Acción del Firewall:** `deny` vía política `policyid=0` (política implícita de denegación inter-zona)
- **Métrica Anómala:** 335 eventos bloqueados en 5 minutos vs valor típico basal de 28.
- **Hallazgo Técnico:** El servicio Windows Update Delivery Optimization utiliza el puerto TCP 7680 para compartir paquetes de parches entre hosts de la red local (distribución P2P). El equipo `192.168.15.16` (cableado en VLAN-15) intentó contactar al equipo `192.168.169.107` (conectado a la red inalámbrica `WiFi_Corp`). La segmentación del firewall bloqueó preventivamente este tráfico inter-VLAN al no existir regla permitida, generando ráfagas de reintentos TCP que dispararon la anomalía estadística.

### Evento 2: Consulta DNS a Dominio Reciente (Captive Portal Detection de Firefox)
- **ID de Alerta:** `3f247baf-254e-4376-a9c3-69dcf1d166ed1790252886544-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=`
- **Regla / Módulo:** `sa` (`new_registered_domain`)
- **Táctica / Técnica:** `XTA0002` (XDR NBA) / `XT2008` (XDR New Domain) - Kill Chain: `Initial Attempts`
- **Origen:** `192.168.169.107:60078` (`WiFi_Corp`, VLAN 1101, MAC `00:09:0f:09:0a:04`)
- **Destino:** `10.11.1.1:53` (`ad.technoma.local`)
- **Consulta Solicitada:** `firefox-portal-detection.com` (Tipo A)
- **Fecha Registro Dominio:** `2026-07-01T15:40:13Z` (< 90 días)
- **Respuestas IP Resueltas:** `151.101.129.91`, `151.101.65.91`, `151.101.193.91`, `151.101.1.91` (Red de distribución Fastly CDN de Mozilla)
- **Indicadores DGA / Reputación:** `is_dga: no`, `dga_score: 0`, `domain_reputation: Good`
- **Hallazgo Técnico (Fast-Track Regla 5):** Aplicación directa del criterio de dominios oficiales recientemente registrados. `firefox-portal-detection.com` es el endpoint canónico de Mozilla Firefox para comprobar si el usuario requiere autenticación en un portal cautivo al conectarse a redes Wi-Fi. Las IPs pertenecen a Fastly. Tráfico 100% benigno y esperado.

---

## 3. Correlación Integral del Host `192.168.169.107`
1. A las 09:00:04 (-03:00), el host `192.168.169.107` se encuentra asociado a la red Wi-Fi corporativa (`WiFi_Corp`, VLAN 1101) y es objeto de solicitudes pasivas de actualización P2P de Windows (WUDO TCP 7680) provenientes de la VLAN-15, las cuales fueron rechazadas correctamente por el firewall.
2. A las 09:25:03 (-03:00), el usuario inicia o reanuda sesión de navegación web utilizando Mozilla Firefox, disparando la sonda de detección de portal cautivo hacia `firefox-portal-detection.com`.
3. No existe actividad de escaneo hostil, comando y control (C2), beaconing malicioso ni persistencia.

---

## 4. Evaluación de Impacto y Tríada CIA
- **Confidencialidad (0/10):** Ningún dato sensible corporativo fue expuesto ni transmitido.
- **Integridad (0/10):** No se alteraron configuraciones ni se ejecutó código malicioso en los endpoints.
- **Disponibilidad (0/10):** Los servicios de red y DNS operaron con normalidad; el bloqueo de WUDO preservó el aislamiento de la red Wi-Fi.
- **Puntuación de Riesgo Global:** **0.0 / 10** (Insignificante / Ruido Operativo).

---

## 5. Veredicto Final y Justificación Humanizada
- **Veredicto:** **Falso Positivo** (Ruido Operativo / Protocolo P2P Windows y Chequeo Legítimo de Navegador).
- **Causa Raíz:**
  1. Descubrimiento P2P nativo de Windows Update (puerto TCP 7680) entre VLANs no enrutadas.
  2. Detección automática de portal cautivo del navegador Mozilla Firefox (`firefox-portal-detection.com`) con registro inferior a 90 días.
- **Acción Inmediata Recomendada:** Cerrar ambas alertas en Stellar Cyber como Falso Positivo. Opcionalmente configurar excepción/tuning en la regla de Newly Registered Domains para `firefox-portal-detection.com` si se desea suprimir el ruido en endpoints con Firefox.
