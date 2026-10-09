### 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `False Positive`, `Cisco Umbrella`, `Sinkhole`, `Pruebas IT`, `DNS Filtering`

### Análisis Evento 1

### 🎯 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Alerta Detectada:** Emerging Threat (SocGholish_Malware_2025_03)
* **Activos Involucrados:** `172.17.10.124` (LAB-SERVER) -> `blacksaltys.com` (IP: `146.112.61.104` Cisco OpenDNS)
* **Comportamiento Anómalo:** Endpoint interno intenta acceder a un dominio catalogado como malicioso y generador de SocGholish, resolviendo a una IP externa específica por el puerto 80.
* **Causalidad Probable:** Pruebas de filtrado web por parte del departamento de IT, redirigidas al Sinkhole de Cisco Umbrella.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Observación Forense |
|---|---|---|---|---|---|
| 2026-07-25T08:13:06 | 2026-07-25 05:13:06 | Emerging Threat | 1 | N/A | Flujo interceptado por Cisco OpenDNS. |

### 🔬 Desglose Técnico y Disección Forense
* **Flujo de Tráfico:** Origen privado `172.17.10.124` (desde la interfaz LAN `LAB-SERVER` en el firewall FortiGate `FG-Technoma`) hacia el destino `146.112.61.104` en el puerto `80`.
* **Amenaza Identificada:** El dominio `blacksaltys.com` tiene reputación de `SocGholish_Malware_2025_03`.
* **Geolocalización Destino:** La IP destino pertenece a Cisco OpenDNS, LLC en Estados Unidos.

**Payload / Evidencia Principal:**
```json
{
  "payload_type": "FortiGate Traffic Log",
  "payload_value": "srcip=172.17.10.124 dstip=146.112.61.104 dstport=80 action=close policyname=Serv-a-Internet",
  "payload_hash": "N/A",
  "payload_firma": "SocGholish_Malware_2025_03",
  "payload_accion": "Navegación Web (Prueba de filtrado)",
  "payload_destino": "Cisco Umbrella Sinkhole"
}
```

### 🧠 ¿Por qué es (o no es) una Amenaza?
**No es una amenaza (Falso Positivo Operativo).** Tal como indica nuestra memoria institucional (`SOC_GEM_v2.md`), la IP `146.112.61.104` es el Sinkhole de Cisco Umbrella. Cuando el equipo de IT realiza pruebas de seguridad desde la red de laboratorio (`LAB-SERVER`, ej: `172.17.10.124`) intentando resolver dominios maliciosos, el DNS de Cisco lo bloquea y redirige el tráfico hacia su IP de Sinkhole para mostrar la página de bloqueo. Stellar Cyber analiza la resolución final e infiere que se estableció conexión con infraestructura maliciosa, cuando en realidad es el mecanismo de defensa en acción.

---

### Análisis Evento 2

**El Evento 2 es un duplicado exacto del Evento 1**, correspondiente a una segunda prueba de conexión (Hora: 10:30:23 UTC) desde el mismo origen `172.17.10.124` hacia el mismo dominio interceptado por el sinkhole de Cisco OpenDNS `146.112.61.104`.

---

### Análisis Evento 3

**El Evento 3 es un duplicado exacto del Evento 1 y 2**, correspondiendo a una tercera iteración de la misma prueba (Hora: 11:54:23 UTC) manteniendo idénticas variables (IPs, firewall FortiGate y reputación de la amenaza).

---

### Cierre Maestro Unificado

### 🛡️ Análisis de Impacto CIA Triad
```json
{
  "Confidentiality": "Sin impacto. El tráfico fue capturado por el sinkhole de Cisco Umbrella.",
  "Integrity": "Sin impacto.",
  "Availability": "Sin impacto."
}
```

### ⚖️ Veredicto y Confianza Analítica
```json
{
  "Veredicto": "False Positive",
  "Confianza": "100%",
  "Motivo": "Comportamiento documentado de Pruebas IT en red de laboratorio, interceptado exitosamente por DNS Filtering (Umbrella Sinkhole)."
}
```

### 📉 Indicador de Fatiga de Alertas
```json
{
  "Fatiga": "Media",
  "Razón": "Las pruebas de seguridad de IT generan ruido si el SIEM no tiene la IP del Sinkhole excluida en sus listas de Threat Intel."
}
```

### 📘 Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
|---|---|
| Detección y Análisis | Validación de IP destino contra rangos conocidos de Cisco Umbrella Sinkhole. |
| Erradicación y Recuperación | N/A (Tráfico bloqueado y redirigido por diseño). |
| Actividad Post-Incidente | Cierre administrativo. |

### 📚 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
|---|---|---|
| PB-002 | Manejo de Falsos Positivos | Identificación de IPs de infraestructura de seguridad (Sinkholes) operando correctamente. |

### 🏷️ Resolution Tag para Stellar Cyber
`False Positive` - IT Authorized Testing.

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
`25/07/2026 11:37 | Analista | technoma | 12634 | Stellar Cyber | - | Media | Emerging Threat | Pruebas IT hacia dominios maliciosos (Sinkhole Cisco) | 172.17.10.124 | Falso positivo por pruebas de IT en red LAB-SERVER. Las peticiones a dominios SocGholish fueron redirigidas correctamente al Sinkhole de Cisco Umbrella (146.112.61.104). | Logs FortiGate | Ninguna | Cerrado | - | No | - | PB-002`

### 💻 Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario final:** Falso positivo operativo. Las alertas corresponden a pruebas de seguridad realizadas por el equipo de IT desde la red de servidores de laboratorio (172.17.10.124). Las consultas a dominios catalogados como maliciosos (blacksaltys.com) fueron correctamente bloqueadas y redirigidas por la protección DNS hacia la IP del Sinkhole de Cisco Umbrella (146.112.61.104). El mecanismo de protección actuó según lo esperado.

> [!TIP]
> Proponer al equipo de ingeniería SOC agregar la IP `146.112.61.104` a la lista de "Safe Destinations" o "Known Sinkholes" dentro de Stellar Cyber, para evitar que el Threat Intel engine dispare la alerta de "Emerging Threat" cuando el destino sea esta IP específica.

### 🔬 Desglose Ultra Quirúrgico
* **Red/Enrutamiento:** Endpoint en la interfaz `LAB-SERVER` intenta cruzar hacia la WAN. El firewall FortiGate (`FG-Technoma`) registra la conexión (policy: `Serv-a-Internet`) y la permite, pero el destino IP real es una red de Cisco.
* **Transporte/Conexión:** Intercambio TCP mínimo sobre puerto 80 (4-5 paquetes, pocos bytes), consistente con una redirección HTTP rápida a una block page.
* **Aplicación/DPI:** DNS resolution manipulada previamente. El endpoint pidió `blacksaltys.com`, pero Cisco Umbrella devolvió `146.112.61.104`.
* **Resumen Quirúrgico Final:** La cadena defensiva operó a la perfección. La solicitud maliciosa fue mitigada por Cisco Umbrella a nivel de resolución de nombres, hundiendo el tráfico web en su Sinkhole. Stellar Cyber, al correlacionar pasivamente el FQDN `blacksaltys.com` y la IP externa con su base de datos (SocGholish), genera la alerta de inteligencia de amenazas, desconociendo que la IP final es en realidad el contenedor seguro de Cisco.
