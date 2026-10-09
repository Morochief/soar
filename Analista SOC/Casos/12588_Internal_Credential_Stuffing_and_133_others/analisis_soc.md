### 🔍 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `CredentialStuffing`, `4768`, `HealthMailbox`, `VM-MARANDU`, `False Positive`.

### 📊 Resumen Ejecutivo del Caso
* **Threat Name:** `internal_cloud_account_login_failure` / `internal_user_login_fail`
* **Source:** `172.16.201.4` (VM-MARANDU)
* **Destination:** `172.16.201.8` (VMBASE8 - DC Secundario)
* **Description:** Fallos de autenticación Kerberos (EventID 4768) automatizados y repetitivos para usuarios `HealthMailbox*@cajaande.gov.py`.

### 🧠 ¿Por qué es (o no es) una Amenaza?
Es un **Falso Positivo (Ruido de Deuda Técnica)**. Según la memoria institucional del SOC (`SOC_GEM_v2.md`), el servidor `VM-MARANDU` (172.16.201.4) presenta un problema crónico de configuración relacionado con la plataforma Exchange/Correo, intentando autenticar continuamente cuentas obsoletas de monitoreo de salud (HealthMailboxes) contra el DC Secundario (`VMBASE8`). Stellar Cyber agrupa esta alta tasa de fallos de autenticación nativos como un ataque de "Credential Stuffing" o "Brute Force" interno.

### 🎯 Veredicto y Confianza Analítica
```json
{
  "Veredicto": "Falso Positivo (Fallo de Autenticación de Servicios Internos)",
  "Confianza": "100%",
  "Justificacion": "El comportamiento está explícitamente documentado como deuda técnica de VM-MARANDU relacionada con HealthMailboxes obsoletas."
}
```

### 📝 Datos para Bitácora de Excel
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-24 | Antigravity | CAJAANDE | 12588 | windows_security | N/A | Medium | Credential Access | FP Credential Stuffing HealthMailbox | 172.16.201.4, 172.16.201.8 | Fallos repetitivos 4768 de HealthMailboxes desde VM-MARANDU. | Logs Windows 4768. | Revisar config Exchange en VM-MARANDU. | Cerrado | N/A | NO | N/A | PB-FP-01 |

### 🏁 Instrucción para Cierre en Stellar Cyber
**Estado:** Closed
**Resolution Tag:** False Positive
**Comentario:** Falso Positivo Analítico (Ruido de Infraestructura). El caso corresponde a múltiples eventos 4768 (Fallos de autenticación Kerberos) generados por cuentas de servicio del tipo "HealthMailbox" originados desde el servidor VM-MARANDU (172.16.201.4) hacia el Controlador de Dominio VMBASE8 (172.16.201.8). Este incidente está plenamente documentado en la base de conocimientos como una deuda técnica derivada de cuentas de monitoreo de Exchange obsoletas o mal configuradas. No constituye un ataque de fuerza bruta ni un intento de "Credential Stuffing" por parte de un adversario. Se reitera sugerencia al equipo de infraestructura para sanear dichas cuentas.
