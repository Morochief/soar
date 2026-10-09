# Informe de Análisis SOC - Lote Interflow (5 Eventos)
**ID del Caso:** `19360_Internal_Firewall_Denial_sati_SSLVPN_DNS_ad2`  
**Fecha de Análisis:** 2026-09-24 12:33:00 (UTC-03:00)  
**Analista Responsable:** Nivel 1 SOC / DFIR  
**Tenant / Organización:** `Technoma` (`cf73a415c8794884a0c35b458b7c73ae`)  
**Dispositivo / Firewall:** `FG-Technoma` (`FG120GTK24022543`)  
**Sensor:** `technoma-sensor` (`4e3eab0649114a80a089a5d5a078994d`)  

---

## 1. Declaración de Cantidad y Desglose del Lote
Se procesaron **5 eventos de seguridad nativos de Interflow** correlacionados de anomalía de denegación de firewall interno (`internal_fw_action` / `fw_action`):

1. **`_seq_no: 19360` (`internal_fw_action`):** 549 peticiones DNS (UDP 53) bloqueadas desde `10.212.134.200` (`sati`, interfaz `ssl.root`) hacia `10.11.1.2` (`ad2.technoma.local`, interfaz `Citrix Servers`) por la regla `policyid=0` (11:25:58).
2. **`_seq_no: 19373` (`internal_fw_action`):** 204 peticiones DNS bloqueadas desde `10.212.134.200` hacia `10.11.1.2` por la regla `policyid=0` (11:30:31).
3. **`_seq_no: 19430` (`internal_fw_action`):** 368 peticiones DNS bloqueadas desde `10.212.134.200` hacia `10.11.1.2` por la regla `policyid=0` (11:45:02).
4. **`_seq_no: 19476` (`internal_fw_action`):** 212 peticiones DNS bloqueadas desde `10.212.134.200` hacia `10.11.1.2` por la regla `policyid=0` (11:59:59).
5. **`_seq_no: 19622` (`internal_fw_action`):** 520 peticiones DNS bloqueadas desde `10.212.134.200` hacia `10.11.1.2` por la regla `policyid=0` (12:20:09).

---

## 2. Análisis Técnico Detallado
- **Host de Origen:** `10.212.134.200` (IP asignada en el pool de clientes SSL-VPN FortiClient al usuario corporativo `sati`, interfaz virtual `ssl.root`).
- **Destino:** `10.11.1.2` (`ad2.technoma.local` - Controlador de Dominio y servidor DNS secundario, interfaz de destino `Citrix Servers`).
- **Servicio y Puerto:** UDP `53` (`proto=17`, DNS).
- **Acción del Firewall:** Acción `deny` estricta bajo la regla implícita por defecto `policyid=0` del firewall FortiGate `FG-Technoma`.
- **Métricas de Tráfico:** `sentbyte=0`, `rcvdbyte=0`, `duration=0` (bloqueo total al ingreso de los paquetes).
- **Diagnóstico:** El cliente VPN FortiClient utilizado por el usuario `sati` contiene en su configuración de red el servidor DNS secundario `10.11.1.2`. Sin embargo, la matriz de políticas del firewall FortiGate para el túnel SSL-VPN no dispone de una regla que autorice consultas DNS hacia `10.11.1.2` a través de la interfaz `Citrix Servers`. En consecuencia, la totalidad de las 1.853 peticiones generadas por el endpoint remoto fueron descartadas inmediatamente por la regla de descarte implícito (`policyid=0`). Los reintentos automáticos del cliente DNS superaron el umbral basal de ~22-29 denegaciones por intervalo de 5 minutos, activando la alarma estadística de Machine Learning. Tráfico benigno, esperado y plenamente contenido.

---

## 3. Evaluación de Impacto y Tríada CIA
- **Confidencialidad (0/10):** Sin compromiso de información confidencial; cero bytes transferidos.
- **Integridad (0/10):** No hubo alteración de registros DNS ni compromiso del servidor `ad2`.
- **Disponibilidad (0/10):** El servicio DNS y el túnel VPN continuaron operando con normalidad.
- **Puntuación de Riesgo Global:** **0.0 / 10** (Insignificante / Tráfico Bloqueado por Firewall).

---

## 4. Veredicto Final y Recomendación
- **Veredicto:** **Falso Positivo** (Ruido Operativo / Denegación de Firewall para usuario SSL-VPN `sati` hacia DNS secundario `ad2`).
- **Acciones:**
  1. Proceder al cierre del clúster de 5 eventos en Stellar Cyber como Falso Positivo.
  2. Notificar al área de redes / seguridad perimetral para evaluar si corresponde habilitar la política que permita DNS a `10.11.1.2` desde `ssl.root`, o bien configurar el túnel para entregar exclusivamente `10.11.1.1` como servidor DNS primario a los clientes VPN.

---

## 5. Instrucción de Cierre en Stellar Cyber
* **Estado:** `Closed`
* **Resolution Tag:** `False Positive`
* **Comentario de Cierre (Condensado):**
> Alerta descartada como **Falso Positivo**. El clúster de 5 eventos corresponde a denegaciones legítimas de firewall (`internal_fw_action`) aplicadas por el equipo FortiGate `FG-Technoma` mediante la política implícita `policyid=0`. El usuario remoto `sati` (`10.212.134.200`), conectado a través del túnel SSL-VPN (`ssl.root`), generó consultas de resolución DNS (UDP 53) hacia el Controlador de Dominio secundario `ad2.technoma.local` (`10.11.1.2`), el cual no se encuentra habilitado en las políticas de enrutamiento para dicha interfaz. El tráfico fue bloqueado en su totalidad por diseño de seguridad (0 bytes transferidos), descartando actividad hostil o impacto en la red.
