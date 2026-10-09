### 🔍 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `SMB`, `NTLM`, `10.11.1.5`, `melissasosa`, `False Positive`.

### 📊 Resumen Ejecutivo del Caso
* **Threat Name:** `exploit_attempt_priv_priv`
* **Actor / Usuario:** `melissasosa` (`192.168.169.82`)
* **Destinations:** `10.11.1.5` (adm-fs.technoma.local - File Server) puerto `445`
* **Description:** Múltiples alertas del IDS por tráfico NTLM (`NTLM Session Setup Request - Auth`, `Negotiate`, `Challenge`) hacia el servidor de archivos (adm-fs).

### 🧠 ¿Por qué es (o no es) una Amenaza?
Es un **Falso Positivo de Ciberataque (Ruido Administrativo)**.
Las alertas se originan por un usuario legítimo (`melissasosa`) accediendo a la carpeta compartida `\\10.11.1.5\DocsAdministracion`. El IDS levanta alertas por los paquetes del protocolo NTLM/SMB, etiquetándolos erróneamente como "Exploit Attempt" y Lateral Movement. Esto es tráfico estándar en redes Windows cuando un cliente negocia autenticación para un file share.

### 🎯 Veredicto y Confianza Analítica
```json
{
  "Veredicto": "Falso Positivo (Tráfico SMB/NTLM Legítimo)",
  "Confianza": "100%",
  "Justificacion": "El tráfico es claramente el protocolo de autenticación NTLM hacia un servidor de archivos (adm-fs) accediendo a una ruta compartida esperada para el perfil de la usuaria."
}
```

### 📝 Datos para Bitácora de Excel
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-24 | Antigravity | technoma | 12597 | modular_sensor | N/A | Low | Lateral Movement | FP Acceso Legítimo a File Server | 192.168.169.82, 10.11.1.5 | Alertas de IDS por negociación NTLM generadas cuando la usuaria melissasosa accedió al share \DocsAdministracion. | Logs NTLM / SMB | Ninguna. | Cerrado | N/A | NO | N/A | PB-FP-01 |

### 🏁 Instrucción para Cierre en Stellar Cyber
**Estado:** Closed
**Resolution Tag:** False Positive
**Comentario:** Falso Positivo Analítico. Las alertas etiquetadas como "Exploit Attempt" corresponden a firmas IDS genéricas que capturaron la secuencia de negociación normal de autenticación NTLM (`Negotiate`, `Challenge`, `Auth`). Este tráfico fue generado por la estación de trabajo de la usuaria `melissasosa` (`192.168.169.82`) conectándose de manera legítima al recurso compartido `\\10.11.1.5\DocsAdministracion` en el File Server corporativo (`adm-fs`). No hay indicios de movimiento lateral no autorizado ni explotación. Se cierra el caso sin requerir acciones adicionales.
