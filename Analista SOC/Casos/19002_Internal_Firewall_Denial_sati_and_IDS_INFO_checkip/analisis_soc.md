# Informe Técnico de Análisis Forense Digital e Incident Response (DFIR)

### 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `#FortiGate` `#SSLVPN` `#SATI` `#InternalFWAction` `#Policy0` `#Suricata` `#ETINFO` `#CheckIP` `#AmazonAWS` `#DNS` `#FalsePositive`

He detectado **5 eventos individuales e independientes** en tu volcado JSON, divididos en dos vectores operacionales benignos concurrentes:
1. **Eventos 1, 2 y 3 (Anomalías de Denegación en Firewall - FortiGate):** 3 alertas de Machine Learning `internal_fw_action` (Anomaly IDs `HeEu06ABI3UnQyDOS0XS`, `YOJA06ABI3UnQyDOw-RH`, `NuNF06ABI3UnQyDOW2jg`) detonadas en el firewall perimetral `FG-Technoma` (`FG120GTK24022543`) por consultas DNS (puerto 53 UDP) desde el pool SSL-VPN (`10.212.134.203`, usuario `sati`) hacia el Controlador de Dominio interno `10.11.1.1` (`ad.technoma.local`), descartadas por la regla implícita `policyid=0`.
2. **Eventos 4 y 5 (Alertas IDS Informativas de DNS - Suricata / Maltrace):** 2 alertas de correlación de exploits (`exploit_attempt_priv_priv` y `exploit_attempt_priv_pub`, Anomaly IDs `XeNH06ABI3UnQyDOm6ad` y `XuNH06ABI3UnQyDOnKY2`) disparadas por la firma informativa `ET INFO External IP Lookup Domain in DNS Lookup (checkip .amazonaws .com)` (SID `2054140`) tras una resolución DNS legítima iniciada en la estación `192.168.169.37` (`nb-wbustamante`) hacia `10.11.1.1` y reenviada recursivamente hacia `8.8.8.8` (Google Public DNS).

A continuación se desarrolla el análisis secuencial e individual de cada evento, culminando en la correlación unificada y el Cierre Maestro del caso.

---

### Análisis Evento 1 (ID: 5af9a241-0a8c-4c22-8e33-571f2ca6b543...)

### 🎯 Resumen Ejecutivo del Evento 1 (Formato Nativo Stellar)
* **Alerta Detectada:** Internal Firewall Denial Anomaly (Score `71`, Severidad `60`, Fidelidad `98.18`).
* **Activos Involucrados:** Host cliente VPN `10.212.134.203` (interfaz `ssl.root`, usuario `sati`, proveedor de soporte Odoo) y Controlador de Dominio `10.11.1.1` (`ad.technoma.local`).
* **Comportamiento Anómalo:** Detección de una tasa anómala de `436` paquetes descartados en un intervalo de 5 minutos (frente a una línea base típica de `57`) en el firewall `FG-Technoma`.
* **Causalidad Probable:** Consultas DNS (puerto 53 UDP) generadas por la estación remota conectada por SSL-VPN debido al mecanismo de failover del cliente DNS de Windows, descartadas por la directiva implícita `policyid=0` al no existir regla que permita resolución DNS directa desde el túnel hacia la red de servidores Citrix.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local UTC-3) | Evento Detectado | Actual | Typical | Host Origen | Host Destino | Observación Forense |
|---|---|---|---|---|---|---|---|
| 2026-09-24T11:30:07.000Z | 2026-09-24 08:30:07 | `fw_action` (deny) | 436 | 57 | `10.212.134.203` (`ssl.root`, `sati`) | `10.11.1.1:53` (`ad.technoma.local`) | Bloqueo por regla implícita `policyid=0` en FG-Technoma. Tráfico estrictamente limitado a DNS UDP 53. |

### 🔬 Desglose Técnico y Disección Forense
* **Identidad y Contexto:**
  - Origen: `10.212.134.203` (Pool DHCP de FortiClient SSL-VPN `ssl.root`).
  - Usuario autenticado: `sati` (Cuenta de soporte técnico del sistema Odoo).
  - Destino: `10.11.1.1` (Servidor DNS / Active Directory `ad.technoma.local`).
  - Servicio: `DNS` (`proto: 17` / UDP, `dstport: 53`).
  - Acción firewall: `action: "deny"` (`policyid=0`, descarte por defecto).

#### Payload / Evidencia Principal:
```json
{
  "payload_type": "FortiGate Traffic Log - Firewall Implicit Deny",
  "payload_value": "srcip=10.212.134.203, dstip=10.11.1.1, dstport=53, proto=17, action=deny, policyid=0, user=sati, service=DNS",
  "payload_hash": "N/A (Tráfico de red en tránsito)",
  "payload_firma": "FG-Technoma (FG120GTK24022543) - Syslog Logid 0000000013",
  "payload_accion": "Descarte de paquete UDP/53 por política cero",
  "payload_destino": "10.11.1.1:53 (ad.technoma.local)"
}
```

---

### Análisis Evento 2 (ID: 6508ee6b-2421-4604-92aa-2f2a4bbf4c69...)

### 🎯 Resumen Ejecutivo del Evento 2 (Formato Nativo Stellar)
* **Alerta Detectada:** Internal Firewall Denial Anomaly (Score `71`, Severidad `60`, Fidelidad `99.84`).
* **Activos Involucrados:** `10.212.134.203` (`sati`) hacia `10.11.1.1:53` a través de `FG-Technoma`.
* **Comportamiento Anómalo:** Incremento a `789` paquetes DNS descartados en un intervalo de 5 minutos (frente a 57 típicos) registrado a las 08:50:14 local.
* **Causalidad Probable:** Reintentos cíclicos de resolución DNS por parte del sistema operativo del cliente VPN `sati` al persistir la indisponibilidad de respuesta DNS interna.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local UTC-3) | Evento Detectado | Actual | Typical | Host Origen | Host Destino | Observación Forense |
|---|---|---|---|---|---|---|---|
| 2026-09-24T11:50:14.000Z | 2026-09-24 08:50:14 | `fw_action` (deny) | 789 | 57 | `10.212.134.203` (`ssl.root`, `sati`) | `10.11.1.1:53` | Reintentos de resolución DNS de la estación VPN bloqueados por `policyid=0`. |

---

### Análisis Evento 3 (ID: 527f9712-ed5e-414f-b73c-7c234e1e781c...)

### 🎯 Resumen Ejecutivo del Evento 3 (Formato Nativo Stellar)
* **Alerta Detectada:** Internal Firewall Denial Anomaly (Score `71`, Severidad `60`, Fidelidad `99.57`).
* **Activos Involucrados:** `10.212.134.203` (`sati`) hacia `10.11.1.1:53` a través de `FG-Technoma`.
* **Comportamiento Anómalo:** Persistencia de descartes (`549` paquetes en 5 minutos) registrado a las 08:55:03 local.
* **Causalidad Probable:** Continuación de la ráfaga de consultas DNS de la sesión VPN de `sati`. Idéntico comportamiento operacional benigno.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local UTC-3) | Evento Detectado | Actual | Typical | Host Origen | Host Destino | Observación Forense |
|---|---|---|---|---|---|---|---|
| 2026-09-24T11:55:02.000Z | 2026-09-24 08:55:03 | `fw_action` (deny) | 549 | 57 | `10.212.134.203` (`ssl.root`, `sati`) | `10.11.1.1:53` | Tercera ventana de descarte de consultas DNS en firewall. Sin tráfico hacia puertos críticos. |

---

### Análisis Evento 4 (ID: 97b5cfe4-09de-4cfa-a447-23b0578157f2...)

### 🎯 Resumen Ejecutivo del Evento 4 (Formato Nativo Stellar)
* **Alerta Detectada:** Private to Private Exploit Anomaly (Score `50`, Severidad `75`, Fidelidad `22.00`).
* **Activos Involucrados:** Estación de trabajo `192.168.169.37` (`nb-wbustamante.technoma.local`, VLAN 1101) consultando al servidor DNS `10.11.1.1` (`ad.technoma.local`).
* **Comportamiento Anómalo:** Disparo de firma IDS de Suricata `ET INFO External IP Lookup Domain in DNS Lookup (checkip .amazonaws .com)` (SID `2054140`) clasificada anómalamente como exploit interno tras 16 días de silencio (`days_silent: 16`).
* **Causalidad Probable:** Consulta DNS estándar para resolver `checkip.amazonaws.com`. El dominio es un servicio público y legítimo provisto por Amazon AWS utilizado ampliamente por navegadores, clientes de soporte remoto (AnyDesk) o utilitarios administrativos para determinar la IP pública de salida.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local UTC-3) | Evento Detectado | Dominio Consultado | Signature ID | Host Origen | Host Destino | Observación Forense |
|---|---|---|---|---|---|---|---|
| 2026-09-24T11:57:54.000Z | 2026-09-24 08:57:54 | IDS Alert (`ids-event`) | `checkip.amazonaws.com` | `2054140` | `192.168.169.37` | `10.11.1.1:53` | Solicitud DNS tipo A legítima. Regla ET INFO de severidad meramente informativa (`classtype: external-ip-check`). |

### 🔬 Desglose Técnico y Disección Forense
* **Detalle de la Regla de Suricata / Emerging Threats:**
  - Mensaje de la regla: `ET INFO External IP Lookup Domain in DNS Lookup (checkip .amazonaws .com)`
  - Clasificación: `classtype: external-ip-check`
  - Severidad asignada por el autor de la firma: `Informational` (Stellar Cyber le asigna score 50 por rareza temporal ML de 16 días).
  - Consulta: `checkip.amazonaws.com` (Tipo A, `NOERROR`).
  - Respuestas obtenidas: CNAME `checkip.check-ip.aws.a2z.com` resolviendo a IPs oficiales de AWS (`52.4.57.244`, `54.145.222.151`, etc.).

---

### Análisis Evento 5 (ID: 7da45111-169d-4765-8ad2-05e8a985016c...)

### 🎯 Resumen Ejecutivo del Evento 5 (Formato Nativo Stellar)
* **Alerta Detectada:** Private to Public Exploit Anomaly (Score `43`, Severidad `60`, Fidelidad `22.00`).
* **Activos Involucrados:** Servidor DNS institucional `10.11.1.1` (`ad.technoma.local`) y servidor DNS público `8.8.8.8` (Google Public DNS).
* **Comportamiento Anómalo:** Mismo disparo de firma IDS `ET INFO External IP Lookup Domain in DNS Lookup (checkip .amazonaws .com)` (SID `2054140`) sobre la consulta externa de resolución recursiva.
* **Causalidad Probable:** El Controlador de Dominio `10.11.1.1`, al recibir la petición del Evento 4 y no poseer el registro en su caché local, ejecutó el reenvío recursivo (forwarder) hacia los DNS de Google (`8.8.8.8`), detonando el sensor IDS perimetral.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local UTC-3) | Evento Detectado | Dominio Consultado | Signature ID | Host Origen | Host Destino | Observación Forense |
|---|---|---|---|---|---|---|---|
| 2026-09-24T11:57:54.000Z | 2026-09-24 08:57:54 | IDS Alert (`ids-event`) | `checkip.amazonaws.com` | `2054140` | `10.11.1.1` | `8.8.8.8:53` | Reenvío recursivo de DNS hacia Google. Tráfico de red habitual y legítimo. |

---

### 🔗 Correlación Integral del Lote
El lote presentado integra dos patrones operacionales completamente benignos y bien conocidos en la infraestructura:
1. **Patrón 1 (Eventos 1 a 3):** Conexión SSL-VPN activa del usuario `sati` (proveedor de soporte Odoo) en `10.212.134.203`. La máquina intenta resolver nombres contra el DNS interno `10.11.1.1` en el puerto 53 UDP, resultando bloqueada por la directiva por defecto (`policyid=0`) de FortiGate. No existen conexiones hacia SMB (445), RDP (3389) ni ningún otro puerto.
2. **Patrón 2 (Eventos 4 y 5):** Consulta DNS de verificación de IP pública (`checkip.amazonaws.com`) originada en el endpoint `192.168.169.37` (`nb-wbustamante`) hacia el DNS interno `10.11.1.1` (Evento 4), el cual reenvió la petición hacia `8.8.8.8` (Evento 5). El sensor IDS de Suricata inspeccionó el payload y activó la firma `ET INFO` (SID 2054140), catalogada como exploit únicamente por el algoritmo de anomalía temporal (`days_silent: 16`).

Ambos flujos corresponden a **Falsos Positivos / Ruido Operacional** plenamente justificados.

---

### 🧠 ¿Por qué es (o no es) una Amenaza?
* **Bloqueos de FortiGate:** No representan un ataque de denegación de servicio ni escaneo. Son paquetes UDP/53 aislados descartados silenciosamente por la política de seguridad del firewall.
* **Alertas IDS de Suricata:** La regla activada no corresponde a un exploit, malware ni Command & Control. Es una regla de tipo `ET INFO` diseñada con fines de auditoría para detectar cuando un dispositivo consulta su dirección IP pública en Internet (`checkip.amazonaws.com`, propiedad de Amazon). El tráfico fue resuelto correctamente y no hubo descarga de binarios ni comunicación maliciosa.

---

### 🛡️ Matriz de Impacto CIA Triad
```json
{
  "confidencialidad": "Ninguno (0/10) - Las consultas hacia servidores internos fueron descartadas por el firewall y la resolución DNS hacia Amazon no involucra datos sensibles.",
  "integridad": "Ninguno (0/10) - No hubo alteración de configuraciones, registros DNS ni archivos en los activos involucrados.",
  "disponibilidad": "Ninguno (0/10) - La infraestructura de red y los servicios de Active Directory/DNS operaron sin afectación."
}
```

### ⚖️ Veredicto y Confianza Analítica (Metodología de 7 Etapas)
```json
{
  "clasificacion": "False Positive",
  "categoria": "Ruido Operacional de Enrutamiento VPN & Firma IDS Informativa (ET INFO)",
  "confianza_analitica": 100,
  "justificacion": "Correlación concluyente: 3 descartes de consultas DNS en firewall por policyid=0 desde túnel SSL-VPN de sati, y 2 eventos IDS por consulta legítima a checkip.amazonaws.com disparando una firma puramente informativa (ET INFO SID 2054140). Cero impacto y comportamiento benigno validado."
}
```

### 📉 Indicador de Fatiga de Alertas
```json
{
  "nivel_fatiga": "Medio-Alto",
  "causa": "Alertas recurrentes de denegación VPN para la cuenta sati y firmas informativas de DNS categorizadas por ML como exploits.",
  "recomendacion_tuning": "1) Deshabilitar la severidad de exploit para la firma ET INFO 2054140 en Suricata o suprimir checkip.amazonaws.com. 2) Evaluar regla de DNS para el pool SSL-VPN en FG-Technoma o ajustar configuración de adaptadores en el cliente VPN."
}
```

### 📘 Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
|---|---|
| **1. Preparación** | Identificación de perfiles de tráfico conocidos en base de conocimiento (`sati` VPN y firmas `ET INFO`). |
| **2. Detección y Análisis** | Verificación de descarte por `policyid=0` en FortiGate y auditoría de payload DNS en Suricata confirmando SID `2054140`. |
| **3. Contención, Erradicación y Recuperación** | No aplica contención. Actividades operacionales normales. |
| **4. Actividad Post-Incidente** | Documentación del cierre consolidado y registro en bitácora oficial. |

### 📚 Playbook Asignado y Escalación CERT-PY
| Control | Detalle |
|---|---|
| **Playbook Operativo SOC** | `PB 3.1 - Triaje de Denegaciones en Firewall y Ruido de Firmas IDS` |
| **Escalación CERT-PY** | **No requerida.** Falso positivo operacional sin evidencia de compromiso ni vectores maliciosos. |

### 🏷️ Resolution Tag para Stellar Cyber
* **Tag:** `False Positive`
* **Sub-etiqueta:** `Operational Noise / Known Benign Traffic`

---

### 📝 Datos para Bitácora de Excel (Apoyo Visual y 1-Clic TSV)

| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-24 08:57:54 | Kevin Moraes | Technoma | HeEu06ABI3UnQyDOS0XS / XeNH06ABI3UnQyDOm6ad | Stellar Cyber ML / FortiGate (FG-Technoma) & Suricata IDS | N/A | Baja | Internal Firewall Denial Anomaly & Exploit Attempt (ET INFO) | Denegación DNS en VPN (sati) y consulta informativa a checkip.amazonaws.com | 10.212.134.203 (sati), 192.168.169.37 (nb-wbustamante) -> 10.11.1.1 (ad), 8.8.8.8 | Lote consolidado de 5 eventos: 3 descartes por regla implícita (policyid=0) de consultas DNS desde túnel SSL-VPN (usuario sati), y 2 eventos IDS por resolución de dominio público de verificación de IP (checkip.amazonaws.com) disparando firma informativa ET INFO (SID 2054140). Actividad operacional benigna. | Acciones 'deny' (policyid=0, UDP 53) en FG-Technoma (FG120GTK24022543). Firma Suricata SID 2054140 (ET INFO checkip.amazonaws.com, classtype: external-ip-check). | No se requiere acción de contención. Cerrar alerta como Falso Positivo / Ruido Operacional. | Cerrado | N/A | No | N/A | PB 3.1 - Triaje de Denegaciones en Firewall y Ruido de Firmas IDS |

#### Fila Cruda (Copiar con 1 Clic para Excel/Google Sheets):
```tsv
2026-09-24 08:57:54	Kevin Moraes	Technoma	HeEu06ABI3UnQyDOS0XS / XeNH06ABI3UnQyDOm6ad	Stellar Cyber ML / FortiGate (FG-Technoma) & Suricata IDS	N/A	Baja	Internal Firewall Denial Anomaly & Exploit Attempt (ET INFO)	Denegación DNS en VPN (sati) y consulta informativa a checkip.amazonaws.com	10.212.134.203 (sati), 192.168.169.37 (nb-wbustamante) -> 10.11.1.1 (ad), 8.8.8.8	Lote consolidado de 5 eventos: 3 descartes por regla implícita (policyid=0) de consultas DNS desde túnel SSL-VPN (usuario sati), y 2 eventos IDS por resolución de dominio público de verificación de IP (checkip.amazonaws.com) disparando firma informativa ET INFO (SID 2054140). Actividad operacional benigna.	Acciones 'deny' (policyid=0, UDP 53) en FG-Technoma (FG120GTK24022543). Firma Suricata SID 2054140 (ET INFO checkip.amazonaws.com, classtype: external-ip-check).	No se requiere acción de contención. Cerrar alerta como Falso Positivo / Ruido Operacional.	Cerrado	N/A	No	N/A	PB 3.1 - Triaje de Denegaciones en Firewall y Ruido de Firmas IDS
```

---

### 💻 Instrucción para Cierre en Stellar Cyber
* **Estado:** `Closed`
* **Resolution Tag:** `False Positive`
* **Comentario de Cierre (Narrativa Fluida y Profesional):**

> Se procede al cierre formal del lote de 5 alertas de denegación en firewall (`internal_fw_action`) y supuestos intentos de exploit (`exploit_attempt_priv_priv` / `exploit_attempt_priv_pub`) tras determinarse que corresponden íntegramente a **Falsos Positivos por ruido operacional**. 
> 
> En primer lugar, los eventos de firewall registrados en `FG-Technoma` (`FG120GTK24022543`) derivan de consultas DNS rutinarias (puerto 53 UDP) emitidas desde la sesión SSL-VPN del proveedor de soporte Odoo (`10.212.134.203`, usuario `sati`) hacia el Controlador de Dominio `10.11.1.1`, las cuales resultaron descartadas por la política implícita por defecto (`policyid=0`) sin que existan intentos de conexión hacia servicios administrativos o movimiento lateral. En segundo lugar, las alertas de exploit corresponden a la resolución legítima del dominio público de verificación de IP `checkip.amazonaws.com` (propiedad de Amazon AWS) iniciada desde la estación `192.168.169.37` (`nb-wbustamante`) y reenviada por el servidor DNS local hacia `8.8.8.8`. Dicha petición detonó la firma de Suricata `ET INFO External IP Lookup Domain in DNS Lookup` (SID `2054140`), la cual posee carácter estrictamente informativo (`classtype: external-ip-check`) y fue clasificada anómalamente por el motor de correlación tras un período de baja frecuencia histórica. Al corroborarse la ausencia total de indicadores de compromiso y con la tríada CIA indemne, se finaliza el caso satisfactoriamente.

---

### 🔬 Desglose Ultra Quirúrgico
* **Capa de Red y Enrutamiento:**
  - `srcip`: `10.212.134.203` (Segmento VPN `ssl.root`) y `192.168.169.37` (VLAN 1101 de estaciones de trabajo).
  - `dstip`: `10.11.1.1` (`ad.technoma.local`, interfaz LAN de servidores) y `8.8.8.8` (DNS público de Google en Internet).
  - Firewall perimetral `FG-Technoma`: Filtrado estricto aplicando política cero (`rule_id: 0`).

* **Capa de Transporte:**
  - Protocolo `17` (UDP) en puerto de destino `53` (DNS estándar).
  - Sin establecimiento de sesiones TCP ni transporte de cargas útiles complejas.

* **Capa de Aplicación y Firmas IDS:**
  - Formato DNS estándar (queries de tipo A para `checkip.amazonaws.com` con flags `NOERROR`).
  - Motor IDS Suricata: Detección basada en firma `ET INFO` (`2054140`) con impacto operativo nulo.

* **Capa de Machine Learning:**
  - `days_silent: 16`: Disparador heurístico de rareza temporal que elevó una firma informativa a categoría de alerta de exploit.
  - Scores ML de 50 y 43 con fidelidad baja (22%), confirmando la susceptibilidad a falsos positivos en consultas DNS públicas poco frecuentes.

* **Resumen Quirúrgico Final:**
  La telemetría demuestra que el tráfico analizado se compone exclusivamente de consultas de resolución de nombres: por un lado, peticiones DNS de una estación VPN (`sati`) descartadas limpiamente por el firewall sin generar riesgo; y por otro lado, una consulta legítima al servicio público de Amazon AWS para verificación de IP externa, la cual detonó una regla IDS informativa de Suricata. Se certifica la inexistencia de actividad maliciosa y se procede al cierre definitivo.
