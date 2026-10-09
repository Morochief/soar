# Informe de Análisis SOC - Lote Interflow (4 Eventos)
**ID del Caso:** `19004_VPN_Policy_289_and_Firefox_Portal_10.212.134.204`  
**Fecha de Análisis:** 2026-09-24 10:55:00 (UTC-03:00)  
**Analista Responsable:** Nivel 1 SOC / DFIR  
**Tenant / Organización:** `Technoma` (`cf73a415c8794884a0c35b458b7c73ae`)  
**Firewall / Sensor:** `FG-Technoma` (`FG120GTK24022543`) / `technoma-sensor` (`4e3eab0649114a80a089a5d5a078994d`)  
**IP / Activos Evaluados:** `10.212.134.204` (Pool SSL-VPN `ssl.root` / `nb-jraguero.technoma.local` / `federicoobregon`), `10.186.73.251` (`VMEDIA-2`)  

---

## 1. Declaración de Cantidad y Desglose del Lote
El lote procesado contiene exactamente **4 eventos de seguridad** nativos de Interflow:

1. **Evento 1 (`_seq_no: 19004`):** `internal_fw_policy_id` (Internal Firewall Policy Anomaly). Conexión permitida por la regla `FG-Technoma_289` (`SSLVPN_TO_ITTI_VOIP`) desde `10.212.134.204` hacia `10.186.73.251:8089` generada por el usuario autenticado `federicoobregon` (`VPN_POSVENTA`).
2. **Evento 2 (`_seq_no: 19125`):** `new_registered_domain`. Consulta DNS a las 10:00:10 (-03:00) desde `10.212.134.204` (`nb-jraguero`) hacia el DC `10.11.1.1` por `firefox-portal-detection.com`.
3. **Evento 3 (`_seq_no: 19190`):** `new_registered_domain`. Consulta DNS a las 10:14:11 (-03:00) desde el mismo host por `firefox-portal-detection.com`.
4. **Evento 4 (`_seq_no: 19242`):** `new_registered_domain`. Consulta DNS a las 10:36:44 (-03:00) desde el mismo host por `firefox-portal-detection.com`.

---

## 2. Análisis Técnico Detallado

### Evento 1: Disparo de Política de Firewall tras Inactividad de 37 Días
- **Regla / Módulo:** `new_ml` (`internal_fw_policy_id`)
- **Táctica / Técnica:** `XTA0002` (XDR NBA) / `XT2002` (XDR Firewall Anomaly) - Kill Chain: `Exploration`
- **Usuario Autenticado:** `federicoobregon` (Grupo: `VPN_POSVENTA`, Directorio: `LDAP_Tech`)
- **Origen:** `10.212.134.204:65345` (Túnel VPN SSL `ssl.root`)
- **Destino:** `10.186.73.251:8089` (Interfaz `VMEDIA-2`, servicio `tcp/8089`)
- **Política FortiGate:** Regla ID `289` (`SSLVPN_TO_ITTI_VOIP`, UUID `559febf6-23a3-51f1-86f1-91c963e9e2da`)
- **Acción del Firewall:** `close` (Permitido vía SNAT `172.22.22.246`, 14 paquetes, 4.8 KB transferidos en 1 segundo).
- **Diagnóstico:** El detector de Machine Learning de Stellar Cyber generó la anomalía debido exclusivamente a que la política de firewall número 289 no había registrado tráfico en los últimos 37 días (`days_silent: 37`). La conexión fue efectuada por un usuario legítimo del departamento de posventa autenticado mediante LDAP institucional, accediendo a un servidor VoIP corporativo autorizado. No existe intrusión ni actividad no autorizada.

### Eventos 2, 3 y 4: Verificación Periódica de Portal Cautivo de Firefox
- **Regla / Módulo:** `sa` (`new_registered_domain`)
- **Táctica / Técnica:** `XTA0002` (XDR NBA) / `XT2008` (XDR New Domain) - Kill Chain: `Initial Attempts`
- **Origen:** `10.212.134.204` (`nb-jraguero.technoma.local`)
- **Destino:** `10.11.1.1:53` (`ad.technoma.local`)
- **Dominio Consultado:** `firefox-portal-detection.com`
- **IPs de Respuesta:** `151.101.65.91`, `151.101.1.91`, `151.101.193.91`, `151.101.129.91` (Fastly CDN de Mozilla)
- **Diagnóstico (Fast-Track Regla 5):** Comprobaciones periódicas estándar del navegador Mozilla Firefox para verificar la existencia de un portal cautivo. Las tres consultas se espacian entre las 10:00 y las 10:36 (hora local), siendo un comportamiento predecible y benigno del software cliente en la máquina del usuario `nb-jraguero`.

---

## 3. Evaluación de Impacto y Tríada CIA
- **Confidencialidad (0/10):** Sin filtración de datos corporativos ni accesos indebidos.
- **Integridad (0/10):** No se observan modificaciones no autorizadas en sistemas ni transferencias anómalas.
- **Disponibilidad (0/10):** El servicio VoIP y los servidores DNS funcionaron de acuerdo con los parámetros de diseño.
- **Puntuación de Riesgo Global:** **0.0 / 10** (Insignificante / Tráfico Operacional Normal).

---

## 4. Veredicto y Recomendaciones
- **Veredicto:** **Falso Positivo** (Uso Legítimo de Regla de Firewall Autorizada y Detección de Portal Cautivo de Firefox).
- **Acciones Recomendadas:**
  1. Cerrar los 4 eventos en Stellar Cyber como Falso Positivo / Ruido Operativo.
  2. La política ID 289 (`SSLVPN_TO_ITTI_VOIP`) es una regla válida para el grupo `VPN_POSVENTA`; el aprendizaje de Stellar Cyber incorporará este tráfico en su línea base en los ciclos subsiguientes.
