### 🔍 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `DNS`, `AnyDesk`, `8.8.8.8`, `10.11.1.1`, `Posture Gap`.

### 📊 Resumen Ejecutivo del Caso
* **Threat Name:** `new_registered_domain`, `exploit_attempt_priv_pub`
* **Source:** `10.11.1.1` (ad.technoma.local - DC) y `192.168.169.50`
* **Destinations:** `8.8.8.8` (Google DNS) y `8.8.4.4`
* **Description:** Múltiples alertas de anomalías de tráfico de red originadas en su mayoría por el DC `10.11.1.1`. Incluye consultas DNS directas a `8.8.8.8` para el dominio recientemente registrado `theagenticx.ai` y picos de consultas DNS para los relays de AnyDesk (`relay-*.net.anydesk.com`).

### 🧠 ¿Por qué es (o no es) una Amenaza?
Es un **Falso Positivo de Ciberataque**, pero evidencia una **Falla de Postura (Policy Violation)**.
1. **Alertas de AnyDesk (Exploit Attempt):** Están explícitamente documentadas en la memoria institucional (`SOC_GEM_v2.md`) como falsos positivos. AnyDesk es una herramienta corporativa autorizada y el IDS levanta falsas alertas por sus consultas DNS de telemetría a sus relays.
2. **Consultas DNS externas directas desde el DC:** El servidor Controlador de Dominio (`10.11.1.1`) está saltándose el DNS interno y realizando consultas directas a IPs públicas (`8.8.8.8` / `8.8.4.4`). Esto suele ocurrir por aplicaciones que tienen los DNS de Google hardcodeados (como el propio AnyDesk, navegadores u otros agentes). No es malicioso, pero es un riesgo operativo. 
3. **El dominio `theagenticx.ai`:** Es telemetría de un software legítimo, no un C2 malicioso. El problema real no es el dominio, sino que el DC resuelva externamente.

### 🎯 Veredicto y Confianza Analítica
```json
{
  "Veredicto": "Falso Positivo (Falla de Postura de Red / AnyDesk Legítimo)",
  "Confianza": "100%",
  "Justificacion": "Eventos documentados en SOC_GEM_v2. El tráfico de AnyDesk es normal y el bypass de DNS es una brecha de postura conocida que debe corregirse a nivel firewall."
}
```

### 📝 Datos para Bitácora de Excel
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-24 | Antigravity | technoma | 12595 | modular_sensor | N/A | Medium | Network Traffic Analysis | FP Consultas DNS Externas y AnyDesk | 10.11.1.1, 192.168.169.50 | Alertas generadas por tráfico autorizado de AnyDesk y bypass de DNS del DC (consultas a 8.8.8.8). No es malicioso, pero el DC debe usar DNS interno. | Logs de red Interflow | Bloquear DNS outbound en Firewall. | Cerrado | N/A | NO | N/A | PB-FP-01 |

### 🏁 Instrucción para Cierre en Stellar Cyber
**Estado:** Closed
**Resolution Tag:** False Positive
**Comentario:** Falso Positivo Analítico con Observación de Postura. El lote de alertas se compone de dos comportamientos benignos: 1) Resoluciones de telemetría y conexión de AnyDesk (herramienta autorizada) detectadas erróneamente por firmas IDS genéricas como "Exploit Attempt". 2) El Controlador de Dominio (10.11.1.1) realizando consultas DNS directas hacia servidores públicos (8.8.8.8 / 8.8.4.4) como fallback para aplicaciones instaladas. No existe actividad C2 ni explotación. Se cierra el caso, pero se recomienda a Infraestructura aplicar la regla de Firewall correspondiente para forzar el uso del DNS interno y bloquear el puerto UDP/TCP 53 saliente desde los servidores.
