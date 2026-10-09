### 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `False Positive`, `SMB Read Anomaly`, `Active Directory`, `GPO`, `Sysvol`

### Análisis Lote de Eventos

### 🎯 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Alerta Detectada:** Internal SMB Read Anomaly (Reportada erróneamente en el nombre del archivo como Write Anomaly).
* **Activos Involucrados:** Equipos de la red de usuarios `192.168.169.x` (`.11`, `.12`, `.21`) contactando a `ad.technoma.local` (`10.11.1.1`).
* **Comportamiento Anómalo:** Los endpoints generaron un volumen "anómalamente alto" de lecturas SMB hacia el Controlador de Dominio (DC) en la red interna, superando su línea base histórica calculada por Machine Learning.
* **Causalidad Probable:** Comportamiento documentado y benigno. Los equipos están descargando y aplicando Políticas de Grupo (GPOs) y realizando autenticaciones Kerberos/NTLM rutinarias contra el DC.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Origen -> Destino | Observación Forense |
|---|---|---|---|---|
| 2026-07-31T07:50:37 | 2026-07-31 04:50:37 | SMB Read Anomaly | 192.168.169.11 -> 10.11.1.1 | Acceso a `\IPC$` y `lsarpc`. |
| 2026-07-31T09:20:01 | 2026-07-31 06:20:01 | SMB Read Anomaly | 192.168.169.12 -> 10.11.1.1 | Descarga de `\sysvol\...\Groups.xml`. |
| ... | ... | ... | 192.168.169.21 -> 10.11.1.1 | Descarga de `\sysvol\...\gpt.ini`. |

### 🔬 Desglose Técnico y Disección Forense
* **Proceso Actor:** Servicios nativos de Windows (Group Policy Client / LSASS).
* **Rutas SMB Accedidas:**
  * `\\ad.technoma.local\IPC$`
  * `\\ad.technoma.local\sysvol`
* **Archivos Específicos Descargados (Metadata):**
  * `technoma.local\Policies\{AFA96729...}\Machine\Preferences\Groups\Groups.xml`
  * `technoma.local\Policies\{70EEDEE7...}\gpt.ini`
  * Interacciones RPC: `lsarpc` (Local Security Authority).

**Contexto del SIEM (Stellar Cyber):**
La alerta se disparó por el motor de Machine Learning (`new_ml`), el cual detectó que el número de lecturas por minuto (ej. 49 y 90) era superior al típico histórico para esos hosts (ej. 9). Stellar mapea esto a la táctica MITRE de Movimiento Lateral (T1210 - Exploitation of Remote Services).

### 🧠 ¿Por qué es (o no es) una Amenaza?
**No es una amenaza (Falso Positivo).** De acuerdo con nuestra `SOC_GEM_v2.md`, todo el tráfico hacia `ad.technoma.local` a través de los recursos `IPC$`, `sysvol` o `lsarpc` es considerado tráfico administrativo por diseño (Actualización de políticas de grupo, sincronización de AD, resolución de cuentas). No hay explotación de servicios remotos, solo el sistema operativo Windows haciendo su trabajo.

---

### Cierre Maestro Unificado

### 🛡️ Análisis de Impacto CIA Triad
```json
{
  "Confidentiality": "Sin impacto.",
  "Integrity": "Sin impacto.",
  "Availability": "Sin impacto."
}
```

### ⚖️ Veredicto y Confianza Analítica
```json
{
  "Veredicto": "False Positive",
  "Confianza": "100%",
  "Motivo": "La evidencia técnica y los archivos extraídos del PCAP (gpt.ini, Groups.xml) demuestran de forma irrefutable que es tráfico legítimo de Group Policy (GPO)."
}
```

### 📉 Indicador de Fatiga de Alertas
```json
{
  "Fatiga": "Alta",
  "Razón": "El motor de ML para volúmenes de red suele fallar mucho en entornos donde las políticas de dominio se empujan en masa (ej. encendido matutino de PCs)."
}
```

### 📘 Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
|---|---|
| Detección y Análisis | Inspección profunda de los metadatos de los paquetes (DPI) y validación de nombres de archivo transferidos por SMB. |
| Erradicación y Recuperación | N/A (Tráfico legítimo). |
| Actividad Post-Incidente | Ninguna. Ya está documentado en Memoria Institucional. |

### 📚 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
|---|---|---|
| PB-002 | Manejo de Falsos Positivos | Tráfico normal de dominio clasificado erróneamente por algoritmos de detección de anomalías volumétricas. |

### 🏷️ Resolution Tag para Stellar Cyber
`False Positive` - Normal Administrative Behavior.

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
`31/07/2026 08:49 | Analista | technoma | 12844 | Stellar Cyber | - | Baja | Internal SMB Read Anomaly | Volumen inusual de tráfico SMB hacia ad.technoma.local (IPC$ y Sysvol) | 10.11.1.1 | Falso Positivo. Varios equipos (192.168.169.x) generaron alertas volumétricas de SMB Read hacia el DC primario (ad.technoma.local). La inspección de paquetes revela que están descargando políticas GPO legítimas (gpt.ini, Groups.xml) e interactuando con lsarpc. Comportamiento normal documentado en SOC_GEM_v2.md. | Stellar Cyber ML | Ninguna | Cerrado | - | No | - | PB-002`

### 💻 Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario final:** Falso positivo heurístico. Las alertas de `Internal SMB Read Anomaly` detonaron porque varios equipos de la red de usuarios (ej. `.11`, `.12`, `.21`) superaron su umbral histórico de lectura SMB. La revisión del payload y los metadatos confirma que las conexiones iban dirigidas a `ad.technoma.local` hacia los recursos `sysvol` e `IPC$`, descargando archivos estándar de configuración (`gpt.ini`, `Groups.xml`) y comunicándose por `lsarpc`. Esto es tráfico benigno de actualización de Group Policy Objects (GPOs) y autenticación, tal como figura en nuestra base de conocimientos. Se cierra el ticket.

> [!TIP]
> **(Agregado por Mentoría DFIR)** Las anomalías volumétricas en SMB son el pan de cada día en las mañanas cuando todos encienden sus equipos y el servicio *Group Policy Client* hace el "pull" desde los DCs. Para no perder tiempo, ve directo al campo `smb_path_summary` o `metadata.request.filename` del JSON. Si ves rutas `\sysvol\` o `{GUID}\gpt.ini`, es 99% un falso positivo. Si, en cambio, ves escrituras a `C$`, `ADMIN$` o múltiples archivos de ofimática con extensiones cifradas (`.locky`, `.enc`), tienes que escalar a TIER 2 de inmediato.

### 🔬 Desglose Ultra Quirúrgico
* **Red/Enrutamiento:** Tráfico lateral entre VLAN de Usuarios (1101) y Servidores (10.11.1.x).
* **Transporte/Conexión:** TCP 445 (SMB) / TCP 139 (NetBIOS).
* **Aplicación/DPI:** Protocolo SMB v2.
* **Resumen Quirúrgico Final:** Stellar Cyber ML no entiende de "archivos de Windows", solo de "matemáticas". Detectó un Delta > a lo histórico (49 lecturas vs 9 habituales) y disparó la alarma. A nivel perimetral, la telemetría es correcta (sí hubo una anomalía estadística), pero a nivel semántico (lo que significan esos datos) es una simple operación administrativa del sistema operativo.
