# Informe de Análisis SOC - Lote Interflow (4 Eventos)
**ID del Caso:** `19478_Internal_Firewall_Denial_NB-JTORALES_DNS_VPN`  
**Fecha de Análisis:** 2026-09-24 12:28:00 (UTC-03:00)  
**Analista Responsable:** Nivel 1 SOC / DFIR  
**Tenant / Organización:** `Technoma` (`cf73a415c8794884a0c35b458b7c73ae`)  
**Dispositivo / Firewall:** `FG-Technoma` (`FG120GTK24022543`)  
**Sensor:** `technoma-sensor` (`4e3eab0649114a80a089a5d5a078994d`)  

---

## 1. Declaración de Cantidad y Desglose del Lote
Se procesaron **4 eventos de seguridad nativos de Interflow** correlacionados de anomalía de denegación de firewall interno (`internal_fw_action` / `fw_action`):

1. **`_seq_no: 19478` (`internal_fw_action`):** 2.159 paquetes DNS denegados desde `192.168.169.64` (`NB-JTORALES`) hacia `192.168.3.214:53` a través de la interfaz VPN IPsec `ROGGIO_PRI` (12:01:18).
2. **`_seq_no: 19491` (`internal_fw_action`):** 3.173 paquetes DNS denegados desde `192.168.169.64` hacia `192.168.3.1:53` a través de la interfaz VPN IPsec `ROGGIO_PRI` (12:05:00).
3. **`_seq_no: 19572` (`internal_fw_action`):** 3.007 paquetes DNS denegados desde `192.168.169.64` hacia `192.168.3.214:53` a través de la interfaz VPN IPsec `ROGGIO_PRI` (12:09:59).
4. **`_seq_no: 19590` (`internal_fw_action`):** 3.426 paquetes DNS denegados desde `192.168.169.64` hacia `192.168.100.1:53` a través de la interfaz VPN IPsec `CASA-ASTI` (12:14:59).

---

## 2. Análisis Técnico Detallado
- **Host de Origen:** `192.168.169.64` (`NB-JTORALES`, asignado al usuario corporativo `josetorales`, autenticado en dominio mediante Kerberos, Windows 10/11 en la interfaz `WiFi_Corp`).
- **Destinos:** Servidores DNS remotos en subredes privadas asociadas a túneles VPN IPsec: `192.168.3.214` y `192.168.3.1` (interfaz `ROGGIO_PRI`), y `192.168.100.1` (interfaz `CASA-ASTI`).
- **Servicio y Protocolo:** DNS estándar sobre puerto `53` UDP (`proto=17`).
- **Acción del Firewall:** Acción `deny` estricta bajo la política implícita `policyid=0` del firewall FortiGate `FG-Technoma`.
- **Volumen y Tráfico Transferido:** 11.765 intentos de conexión bloqueados en una ventana de 20 minutos; `sentbyte=0`, `rcvdbyte=0` (bloqueo total sin paso de datos).
- **Diagnóstico:** El endpoint `NB-JTORALES` conserva en su configuración de red o adaptadores virtuales DNS servers residuales pertenecientes a túneles VPN remotos (`ROGGIO_PRI` y `CASA-ASTI`). Al operar dentro de la red corporativa inalámbrica (`WiFi_Corp`), el mecanismo nativo de Windows (Smart Multi-Homed Name Resolution) reintenta periódica y masivamente consultas DNS contra todos los servidores configurados. Debido a que el firewall FortiGate no cuenta con reglas que autoricen el enrutamiento de DNS desde la red Wi-Fi hacia dichas interfaces VPN, el tráfico fue descartado de manera inmediata por la política por defecto (`policyid=0`). No existe ataque, escaneo malicioso ni actividad de comando y control; se trata de una anomalía estadística provocada por una configuración desactualizada de adaptadores DNS en el endpoint.

---

## 3. Evaluación de Impacto y Tríada CIA
- **Confidencialidad (0/10):** Sin fuga de información; 0 bytes transferidos a través del firewall.
- **Integridad (0/10):** No hubo alteración de configuraciones ni compromiso del host.
- **Disponibilidad (0/10):** La red y los túneles VPN operaron con total normalidad.
- **Puntuación de Riesgo Global:** **0.0 / 10** (Insignificante / Tráfico Bloqueado por Política de Firewall).

---

## 4. Veredicto Final y Recomendación
- **Veredicto:** **Falso Positivo** (Ruido Operativo / Denegación Legítima de Firewall por Configuración de DNS en Cliente).
- **Acciones:**
  1. Proceder al cierre del clúster de 4 eventos en Stellar Cyber como Falso Positivo.
  2. Notificar al área de soporte técnico / Help Desk para depurar la lista de servidores DNS estáticos o adaptadores virtuales en el equipo `NB-JTORALES` (`josetorales`).

---

## 5. Instrucción de Cierre en Stellar Cyber
* **Estado:** `Closed`
* **Resolution Tag:** `False Positive`
* **Comentario de Cierre (Condensado):**
> Alerta descartada como **Falso Positivo**. El clúster de 4 eventos corresponde a denegaciones legítimas de firewall (`internal_fw_action`) aplicadas por el equipo FortiGate `FG-Technoma` mediante la política implícita `policyid=0`. El host corporativo `NB-JTORALES` (`192.168.169.64`, usuario `josetorales`) en la red `WiFi_Corp` intentó realizar consultas masivas de resolución DNS (UDP 53) hacia servidores DNS remotos (`192.168.3.214`, `192.168.3.1` y `192.168.100.1`) vinculados a túneles IPsec (`ROGGIO_PRI` y `CASA-ASTI`), producto del mecanismo de reintentos multi-homed de Windows. La totalidad del tráfico fue bloqueado efectivamente (0 bytes transferidos), sin representar escaneo hostil, exfiltración ni afectación a la tríada CIA.
