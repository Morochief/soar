# Informe de Análisis SOC - Lote Interflow (2 Eventos)
**ID del Caso:** `19343_WUDO_Firewall_Denial_and_Policy_190_NB-EVERA`  
**Fecha de Análisis:** 2026-09-24 12:21:00 (UTC-03:00)  
**Analista Responsable:** Nivel 1 SOC / DFIR  
**Tenant / Organización:** `Technoma` (`cf73a415c8794884a0c35b458b7c73ae`)  
**Sensor / Firewall:** `technoma-sensor` (`4e3eab0649114a80a089a5d5a078994d`) / `FG-Technoma` (`FG120GTK24022543`)  

---

## 1. Declaración de Cantidad y Desglose del Lote
Se procesaron exactamente **2 eventos de seguridad** correlacionados en este lote de alertas nativas de Interflow:

1. **Evento 1 (`_seq_no: 19343`):** `internal_fw_action` (Internal Firewall Denial Anomaly) en FortiGate `FG-Technoma`. Bloqueo de 217 intentos de conexión en el puerto TCP 7680 (Windows Update Delivery Optimization - WUDO) desde `192.168.15.16` (VLAN-15) hacia `192.168.169.102` (`nb-evera.technoma.local`, `WiFi_Corp`).
2. **Evento 2 (`_seq_no: 19424`):** `internal_fw_policy_id` (Internal Firewall Policy Anomaly) en FortiGate `FG-Technoma`. Conexión TCP 7680 hacia `10.179.105.31` (`UPAY-P5-PRI`) originada por `192.168.169.102` (`nb-evera.technoma.local`, usuario `ENRIQUEVERA`), disparando la política 190 (`THN A UPAY P5`) tras 23 días de silencio con resultado `timeout`.

---

## 2. Análisis Individual de Eventos

### Evento 1: Bloqueo de Conexiones P2P WUDO en Firewall (TCP 7680)
- **ID de Alerta:** `49a8d5a6-8225-4f3f-a023-2bf0ad64df2a1790259903645-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=`
- **Regla / Módulo:** `new_ml` (`internal_fw_action`)
- **Táctica / Técnica:** `XTA0002` (XDR NBA) / `XT2002` (XDR Firewall Anomaly) - Kill Chain: `Exploration`
- **Origen:** `192.168.15.16:65013` (VLAN-15, MAC `50:6b:8d:ec:30:fa`)
- **Destino:** `192.168.169.102:7680` (`WiFi_Corp`, `nb-evera.technoma.local`, usuario `ENRIQUEVERA`)
- **Servicio / Protocolo:** `tcp/7680` (Windows Update Delivery Optimization - WUDO) / Protocolo TCP (6)
- **Acción del Firewall:** `deny` vía política `policyid=0` (política implícita de denegación inter-zona)
- **Métrica Anómala:** 217 eventos bloqueados en 5 minutos vs valor típico basal de 22.
- **Diagnóstico:** El protocolo WUDO utiliza el puerto TCP 7680 para distribuir parches de Windows entre equipos locales de manera P2P. El host `192.168.15.16` (cableado en VLAN-15) intentó conectarse al endpoint `192.168.169.102` en `WiFi_Corp`. Al no existir una regla inter-VLAN que lo autorice, el FortiGate descartó el tráfico limpiamente (`policyid=0`), ocasionando ráfagas de reintentos que activaron el umbral estadístico del motor ML.

### Evento 2: Activación de Política 190 tras 23 Días por Intento WUDO Outbound
- **ID de Alerta:** `166b29a7-862c-4593-8309-09bf3cdcdcfc1790261702677-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=`
- **Regla / Módulo:** `new_ml` (`internal_fw_policy_id`)
- **Táctica / Técnica:** `XTA0002` (XDR NBA) / `XT2002` (XDR Firewall Anomaly) - Kill Chain: `Exploration`
- **Origen:** `192.168.169.102:49677` (`WiFi_Corp`, `nb-evera.technoma.local`, usuario `ENRIQUEVERA`)
- **Destino:** `10.179.105.31:7680` (Interfaz `UPAY-P5-PRI`, túnel IPsec VPN)
- **Política FortiGate:** Regla ID `190` (`THN A UPAY P5`, UUID `46a48c78-ca3f-51f0-f325-000011dbfb2b`)
- **Acción del Firewall:** `timeout` (12 segundos de duración, 104 bytes / 2 paquetes enviados sin respuesta recibida)
- **Diagnóstico:** El servicio WUDO en la máquina de `ENRIQUEVERA` intentó localizar peers de actualización en la subred remota `10.179.105.31:7680`. La conexión coincidió con la regla 190 pero expiró por timeout. El detector de Machine Learning alertó el evento exclusivamente porque dicha regla no había registrado tráfico en los últimos 23 días (`days_silent: 23`). Tráfico benigno generado por el subsistema de Windows.

---

## 3. Evaluación de Impacto y Tríada CIA
- **Confidencialidad (0/10):** Sin compromiso ni exposición de información confidencial.
- **Integridad (0/10):** Sin alteración en configuraciones ni ejecución de código malicioso.
- **Disponibilidad (0/10):** Operatividad íntegra; las políticas de firewall cumplieron su función de contención inter-zona.
- **Puntuación de Riesgo Global:** **0.0 / 10** (Insignificante / Ruido Operativo de Red).

---

## 4. Veredicto Final y Recomendación
- **Veredicto:** **Falso Positivo** (Ruido Operacional / Protocolo P2P Windows Update Delivery Optimization - WUDO).
- **Acciones:**
  1. Cerrar ambas alertas en Stellar Cyber como Falso Positivo.
  2. Registrar la excepción analítica en la línea base de Machine Learning para el puerto TCP 7680.

---

## 5. Instrucción de Cierre en Stellar Cyber
* **Estado:** `Closed`
* **Resolution Tag:** `False Positive`
* **Comentario:**
> Alerta descartada como **Falso Positivo**. El análisis técnico confirma que ambos eventos corresponden a tráfico operacional benigno del protocolo nativo **Windows Update Delivery Optimization (WUDO, puerto TCP 7680)** en la estación `nb-evera.technoma.local` (`192.168.169.102`, usuario `ENRIQUEVERA`). Por un lado, la denegación en firewall (`internal_fw_action`) se originó por el bloqueo inter-VLAN legítimo de conexiones P2P desde `192.168.15.16` bajo la regla implícita `policyid=0`. Por otro lado, la anomalía de política (`internal_fw_policy_id`) fue disparada por el motor ML debido a 23 días de inactividad de la regla 190 (`THN A UPAY P5`) tras un reintento WUDO no exitoso (`action=timeout`) hacia `10.179.105.31`. Sin impacto en la tríada CIA ni actividad maliciosa.
