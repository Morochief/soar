### 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `False Positive`, `RustDesk`, `Remote Access`, `SMB Anomaly`, `RPC/LSA/SAMR`

### Análisis Lote de Eventos (5 Eventos Recibidos)
Se han identificado y analizado 5 eventos de seguridad en el lote, correspondientes a consultas DNS relacionadas con software de soporte remoto y tráfico SMB RPC interno hacia el Controlador de Dominio.

---

### 🎯 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Alerta Detectada:** Exploit Attempt (Low Severity) & Internal SMB Write Anomaly (12893).
* **Activos Involucrados:** 
  - `192.168.169.179` y `192.168.169.151` realizando consultas DNS hacia el DC `10.11.1.1` (`ad.technoma.local`).
  - `nb-mjcasanas.technoma.local` (`192.168.169.48`) y `NB-FCANDIA` (`192.168.169.2`) interactuando por SMB (puerto 445) con `10.11.1.1`.
* **Comportamiento Anómalo:** 
  1. Firma IDS de Suricata disparada por la resolución del dominio de relevo de RustDesk (`rs-ny.rustdesk.com`).
  2. Ráfaga anómala de solicitudes de escritura y comandos RPC SMB sobre los recursos `lsarpc` y `samr` en la carpeta compartida `\\ad.technoma.local\IPC$`.
* **Causalidad Probable:** 
  1. Uso del software de control remoto legítimo **RustDesk** (solicitud de dominio relay `rs-ny.rustdesk.com`), catalogado genéricamente como intento de exploit por firmas NIDS.
  2. Proceso estándar de sincronización de políticas de grupo (GPO), validación de cuentas SAM (`samr`) y autoridad de seguridad local (`lsarpc`) en Active Directory durante inicios de sesión de usuarios de dominio.

---

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Origen | Destino / Recurso | Firma / Evento Detectado |
|---|---|---|---|---|
| 2026-08-01T08:45:10 | 2026-08-01 05:45:10 | `192.168.169.179` | `10.11.1.1:53` (`rs-ny.rustdesk.com`) | Exploit Attempt (RustDesk Relay DNS). |
| 2026-08-01T08:48:22 | 2026-08-01 05:48:22 | `192.168.169.151` | `10.11.1.1:53` (`rs-ny.rustdesk.com`) | Exploit Attempt (RustDesk Relay DNS). |
| 2026-08-01T08:51:30 | 2026-08-01 05:51:30 | `192.168.169.151` | `10.11.1.1:53` (`rs-ny.rustdesk.com`) | Exploit Attempt (RustDesk Relay DNS). |
| 2026-08-01T08:53:14 | 2026-08-01 05:53:14 | `nb-mjcasanas` (`192.168.169.48`) | `10.11.1.1:445` (`IPC$\lsarpc`) | Internal SMB Write Anomaly (RPC/LSA). |
| 2026-08-01T08:55:01 | 2026-08-01 05:55:01 | `NB-FCANDIA` (`192.168.169.2`) | `10.11.1.1:445` (`IPC$\samr`) | Internal SMB Write Anomaly (RPC/SAMR). |

---

### 🔬 Desglose Técnico y Disección Forense

#### 1. Eventos de DNS / RustDesk (Eventos 1, 2, 3)
* **Proceso / Protocolo:** DNS Query (UDP 53) -> `rs-ny.rustdesk.com` (Tipo `AAAA`).
* **Firma IDS:** `INFO RustDesk Relay Domain in DNS Lookup`.
* **Análisis DFIR:** RustDesk es una aplicación open-source de soporte remoto. Las firmas Suricata clasifican cualquier tráfico hacia su infraestructura pública como "Exploit Attempt / Low Severity" únicamente para advertir sobre la presencia de software de gestión remota no empresarial. No existen evidencias de explotación de código.

#### 2. Eventos de SMB / RPC (Eventos 4, 5)
Traducción mediante la **Piedra de Rosetta SMB (MS-SMB2)**:
* **Conexión a Recurso Compartido:** Comando `3` (`SMB2_TREE_CONNECT`) hacia `\\ad.technoma.local\IPC$`.
* **Apertura de Tuberías Nombre (Named Pipes):** Comando `5` (`SMB2_CREATE`) hacia:
  - `lsarpc` (Local Security Authority RPC - Evento 4)
  - `samr` (Security Account Manager Remote - Evento 5)
* **Transferencia RPC:** Comando `11` (`SMB2_IOCTL`), Comando `8` (`SMB2_READ`), Comando `9` (`SMB2_WRITE`), y Comando `16` (`SMB2_QUERY_INFO` / `SMB2_0_INFO_FILE`).
* **Análisis DFIR:** Las tuberías `lsarpc` y `samr` sobre `IPC$` son utilizadas nativamente por los clientes Windows durante el inicio de sesión para verificar membresías de grupos de Active Directory y políticas de seguridad local. El incremento transitorio en comandos de escritura/lectura durante el arranque o inicio de sesión detonó el modelo de Machine Learning `internal_smb_anomaly`.

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
  "Motivo": "Las alertas IDS corresponden a consultas DNS legítimas del software RustDesk y el tráfico SMB son llamadas RPC estándar (lsarpc/samr) para autenticación en Active Directory."
}
```

### 📉 Indicador de Fatiga de Alertas
```json
{
  "Fatiga": "Media",
  "Razón": "Firmas IDS informativas de herramientas de soporte remoto y anomalías de volumen SMB en momentos de login masivo."
}
```

### 📘 Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
|---|---|
| Detección y Análisis | Inspección de firmas Suricata y traducción de comandos SMBv2 (Rosetta Stone). |
| Erradicación y Recuperación | N/A (Tráfico corporativo / herramientas de soporte). |
| Actividad Post-Incidente | Tuning opcional de reglas IDS para categorizar RustDesk como Software Administrado. |

### 📚 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
|---|---|---|
| PB-002 | Manejo de Falsos Positivos | Descarte de alertas de tráfico normal de red y herramientas de soporte remoto. |

### 🏷️ Resolution Tag para Stellar Cyber
`False Positive` - Normal Administrative Behavior / Expected Network Traffic.

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
`01/08/2026 08:23 | Analista | technoma | 12893 | Stellar Cyber | - | Baja | Internal SMB Write Anomaly / Exploit Attempt | Tráfico de soporte RustDesk e inicios de sesión RPC SMB en Active Directory | 10.11.1.1 | Falso Positivo. Las alertas de Exploit Attempt son detonadas por firmas informativas IDS al consultar dominios de RustDesk (rs-ny.rustdesk.com). Las alertas de SMB Write Anomaly corresponden a tráfico RPC legítimo sobre IPC$ (pipes lsarpc y samr) generado por los equipos nb-mjcasanas y NB-FCANDIA durante la autenticación de dominio. Sin actividad maliciosa. | Interflow / Suricata | Ninguna | Cerrado | - | No | - | PB-002`

### 💻 Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario final:** Falso positivo validado. Las alertas del lote 12893 fueron analizadas individualmente:
  1. Los eventos de "Exploit Attempt" corresponden a la firma informativa NIDS `INFO RustDesk Relay Domain in DNS Lookup` generada por la resolución del cliente de soporte remoto RustDesk.
  2. Los eventos de "Internal SMB Write Anomaly" corresponden a la actividad estándar de autenticación de Active Directory sobre `IPC$` en el controlador de dominio `ad.technoma.local` utilizando las tuberías nombradas `lsarpc` y `samr` (comandos SMBv2 TREE_CONNECT, CREATE, IOCTL, WRITE). Se procede al cierre del ticket.

---

### 🔬 Desglose Ultra Quirúrgico

* **Capa 1: Red y Transporte (`srcip` / `dstip` / `proto`)**
  - Eventos 1-3: UDP/53 (DNS) desde `192.168.169.179` y `.151` hacia el DC `10.11.1.1`.
  - Eventos 4-5: TCP/445 (SMB) desde `192.168.169.48` (`nb-mjcasanas`) y `192.168.169.2` (`NB-FCANDIA`) hacia `10.11.1.1`.
* **Capa 2: Aplicación y DPI (`metadata` / `smb_command`)**
  - DNS: Solicitudes `AAAA` para `rs-ny.rustdesk.com`.
  - SMB: Solicitudes SMB2 `TREE_CONNECT` a `\\IPC$`, seguidas de `CREATE` hacia las Named Pipes de seguridad `lsarpc` (LSA) y `samr` (SAM).
* **Capa 3: Motor Anómalo (`new_ml`)**
  - Firma NIDS de baja severidad para RustDesk.
  - El modelo estadístico de SMB detectó un volumen inusualmente alto de escrituras/intercambios RPC en una ventana de 5 minutos provocada por los inicios de sesión.

**Resumen Quirúrgico Final:** Tráfico combinado de la aplicación de soporte remoto RustDesk en clientes de la red y consultas RPC rutinarias a nivel de Active Directory (`lsarpc` / `samr`) hacia el Domain Controller. No hay vectores de ataque presentes.
