### 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `True Positive`, `Policy Violation`, `Unsanctioned Software`, `Gaming Client`, `Firewall Denial`

### Análisis Lote de Eventos

### 🎯 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Alerta Detectada:** Internal Firewall Denial Anomaly (12830) & Cortex XDR BIOC: Rare unsigned binary connected to a globally rare external host (133150, 133151).
* **Activos Involucrados:** `NB-AMUNOZ` (`192.168.169.76`) - Dominio `technoma.local` (Usuario: `albertmunoz`) y `NB-SFERNANDEZ` (`192.168.171.115`).
* **Comportamiento Anómalo:** 
  1. El host `NB-AMUNOZ` ejecutó binarios sin firma localizados en `C:\Call of Duty Modern Warfare 3\` (`TeknoMW3_Client_Launcher.exe` e `iw5mp.exe`) estableciendo conexiones HTTPS hacia la IP `94.242.58.56` (Dominio `teknogods.com`, Suecia).
  2. En paralelo, FortiGate bloqueó repetidamente (226 intentos) tráfico entrante al puerto TCP/7680 (Windows Delivery Optimization) desde `NB-SFERNANDEZ` hacia `NB-AMUNOZ`.
* **Causalidad Probable:** Violación de la Política de Uso Aceptable (AUP). El usuario `albertmunoz` instaló y ejecutó un cliente de videojuego pirata/modificado (**TeknoMW3 - Call of Duty Modern Warfare 3**) en su equipo corporativo. El cliente intentó conectarse a los servidores comunitarios de `teknogods.com` para emparejamiento multijugador. Cortex XDR lo catalogó como "Command and Control" por ser un binario sin firma comunicándose con una IP globalmente infrecuente.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Origen / Proceso | Destino / Puerto | Evento & Firma |
|---|---|---|---|---|
| 2026-07-30T20:10:04 | 2026-07-30 17:10:04 | `NB-SFERNANDEZ` (`192.168.171.115`) | `NB-AMUNOZ` (`192.168.169.76:7680`) | FortiGate Deny (WDO P2P Traffic). |
| 2026-07-30T20:36:33 | 2026-07-30 17:36:33 | `TeknoMW3_Client_Launcher.exe` (PID 32760) | `teknogods.com` (`94.242.58.56:443`) | Cortex XDR BIOC: Rare Unsigned Binary. |
| 2026-07-30T20:37:51 | 2026-07-30 17:37:51 | `iw5mp.exe` (PID 26600) | `teknogods.com` (`94.242.58.56:443`) | Cortex XDR BIOC: Rare Unsigned Binary. |

### 🔬 Desglose Técnico y Disección Forense
* **Usuario:** `TECHNOMA\albertmunoz` (Albert Muñoz).
* **Ruta de Ejecución:** `C:\Call of Duty Modern Warfare 3\TeknoMW3_Client_Launcher.exe` y `iw5mp.exe`.
* **Hashes:** 
  - `TeknoMW3_Client_Launcher.exe` (SHA256: `8ddf64f5e0831de63794a6474b73636ce52768b491fcff658a3304b9679f229b`)
  - `iw5mp.exe` (SHA256: `c2cb2335f1e2dd9f714fc90db429bafd41bdf47b59a27c509fbc27509c8587cd`)
* **Infraestructura Externa:** `teknogods.com` (`94.242.58.56`, ASN 42532 SIA VEESP, Suecia).
* **Puerto Interno 7680:** Corresponde a Windows Delivery Optimization (WUDO/WDO), servicio de Windows para compartir actualizaciones P2P en la red local. El FortiGate bloqueó este tráfico entre VLAN304 y WiFi_Corp por políticas de segmentación estándar.

**Contexto del SIEM y EDR:**
Cortex XDR generó alertas de severidad Media (C2 / Web Protocols) debido a que `TeknoMW3_Client_Launcher.exe` y `iw5mp.exe` son binarios no firmados y no conocidos en el ecosistema corporativo que abren sockets TLS/443 hacia una IP externa sin reputación empresarial. La investigación confirma que **TeknoMW3** es un lanzador no oficial legítimo en el mundo del gaming para habilitar servidores dedicados en Call of Duty MW3, pero su presencia en un entorno de trabajo representa un riesgo de malware/suplantación y falta de cumplimiento de políticas.

### 🧠 ¿Por qué es (o no es) una Amenaza?
**Es un True Positive por Violación de Políticas Corporativas (Software No Autorizado).** No se trata de un ataque C2 persistente conducido por un grupo de ciberdelincuencia o ransomware. Sin embargo, la instalación y ejecución de videojuegos modificados/crackeados en activos corporativos expone a la organización a vulnerabilidades de cadena de suministro, troyanos empaquetados y consumo indebido de recursos de red.

---

### Cierre Maestro Unificado

### 🛡️ Análisis de Impacto CIA Triad
```json
{
  "Confidentiality": "Sin evidencia de fuga de datos corporativos.",
  "Integrity": "Comprometida a nivel de cumplimiento (ejecución de binarios sin firma / crackeados).",
  "Availability": "Sin impacto directo."
}
```

### ⚖️ Veredicto y Confianza Analítica
```json
{
  "Veredicto": "True Positive (Policy Violation / Unsanctioned Software)",
  "Confianza": "100%",
  "Motivo": "Los logs de Cortex XDR identifican de forma explícita el ejecutable C:\\Call of Duty Modern Warfare 3\\TeknoMW3_Client_Launcher.exe y el dominio teknogods.com."
}
```

### 📉 Indicador de Fatiga de Alertas
```json
{
  "Fatiga": "Baja",
  "Razón": "Evento puntual de software no autorizado ejecutado por un usuario final."
}
```

### 📘 Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
|---|---|
| Detección y Análisis | Identificación del proceso no autorizado `TeknoMW3` y destino `teknogods.com`. Descarte de C2 avanzado. |
| Erradicación y Recuperación | Notificación a Soporte/Seguridad para remover la carpeta del juego y apercibir al usuario. |
| Actividad Post-Incidente | Ajuste de políticas EDR/AppLocker para bloquear directorios no estándar como `C:\Call of Duty...`. |

### 📚 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
|---|---|---|
| PB-003 | Software No Autorizado y Violación de AUP | Manejo de aplicaciones no corporativas, juegos y binarios sin firma instalados por usuarios. |

### 🏷️ Resolution Tag para Stellar Cyber
`True Positive` - Policy Violation / Unsanctioned Software.

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
`31/07/2026 13:00 | Analista | technoma | 12830 | Stellar Cyber | - | Media | Internal Firewall Denial Anomaly / Cortex BIOC | Ejecución de juego no autorizado (Call of Duty MW3 / TeknoMW3) | 192.168.169.76 | True Positive (Violación de Política). El usuario albertmunoz en NB-AMUNOZ instaló y ejecutó un cliente de videojuego pirata (TeknoMW3_Client_Launcher.exe / iw5mp.exe en C:\Call of Duty Modern Warfare 3\), conectándose a teknogods.com (Suecia). Cortex XDR lo catalogó como C2 por ser binario sin firma conectándose a IP rara. Adicionalmente FortiGate denegó tráfico P2P WDO (TCP 7680) entre VLANs. No es malware APT, sino uso indebido de equipo corporativo. Se solicita remoción del software. | Cortex XDR / FortiGate | Ninguna | Escalado a IT / RRHH | - | No | - | PB-003`

### 💻 Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed (Derivado a TI / Seguridad Interna)
* **Resolution Tag:** True Positive (Policy Violation)
* **Comentario final:** Eventos validados como Violación de la Política de Uso Aceptable (AUP). Cortex XDR detectó la comunicación del proceso `TeknoMW3_Client_Launcher.exe` y `iw5mp.exe` (ubicados en `C:\Call of Duty Modern Warfare 3\`) hacia `teknogods.com` (`94.242.58.56`). El usuario `albertmunoz` instaló un cliente de videojuego no autorizado en el equipo `NB-AMUNOZ`. Aunque Cortex XDR clasifica la regla BIOC como "Command and Control", el análisis técnico confirma que se trata del tráfico nativo de un juego multijugador modificado. El evento de denegación de FortiGate corresponde a tráfico P2P de actualización de Windows (TCP/7680) bloqueado entre VLANs. Se cierra el ticket en la consola SOC y se remite el hallazgo a Soporte TI para la eliminación del software no autorizado y la desinfección/auditoría del equipo.
