### Analisis en Profundidad (Estilo Mentor DFIR)
**Tags:** Network Traffic Analysis, DNS Tunneling, Exfiltration, Cloud Infrastructure

---

### Analisis Evento 1
**ID:** 325f6ebf...
**Alerta:** DNS Tunneling Anomaly (dns_tunnel)

#### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
- **Origen:** El host `nb-agsilvero.technoma.local` (`192.168.169.99`) genero multiples consultas DNS.
- **Destino:** Servidor DNS interno `ad.technoma.local` (`10.11.1.1`).
- **Contexto:** Se detecto una volumetria inusual de trafico DNS (366 bytes vs los 29 tipicos) y alta entropia consultando subdominios extremadamente largos bajo el dominio raiz `powerplatform.com`.
- **Accion requerida:** Confirmar si los subdominios largos son un canal real de exfiltracion (DNS Tunneling) o trafico estructural de un servicio Cloud.

#### Linea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Ratio | Observacion Forense |
|---|---|---|---|---|---|---|
| 2026-07-16 14:49:08 | 2026-07-16 11:49:08 | dns_tunnel | 366 Bytes | 29 Bytes | 12x | Consultas a *.powerplatform.com |

#### Desglose Tecnico y Diseccion Forense
- El motor ML evalua la entropia (89) y longitud de las consultas como `5bbcc1a171964832b76a345a31a53a.eb.tenant.api.powerplatform.com`.
- Estas consultas resuelven, mediante una extensa cadena de CNAMEs (`ppapigw.br-cm001.gateway.prod.cm.powerapps.com...`), hacia direcciones IP legitimas de Microsoft Azure (ej. `4.203.146.0`).
- El dominio `powerplatform.com` pertenece a Microsoft y es la infraestructura backend para Power Apps, Power Automate y Power BI. El subdominio largo no es un payload codificado (Base64/Hex de datos robados), sino un identificador de tenant o GUID de entorno de Microsoft 365.

**Payload / Evidencia Principal:**
```json
{
  "payload_type": "DNS Query (A)",
  "payload_value": "5bbcc1a171964832b76a345a31a53a.eb.tenant.api.powerplatform.com",
  "payload_hash": "N/A",
  "payload_firma": "N/A",
  "payload_accion": "DNS Resolution CNAME Chain",
  "payload_destino": "10.11.1.1"
}
```

**Diagnostico e Hipotesis:**
| Hipotesis Formulada | Resultado de Evaluacion |
|---|---|
| Exfiltracion via DNS Tunneling (Iodine/DNSCat) | Descartado. Resoluciones apuntan a infraestructura oficial de Microsoft, no a un servidor C2 atacante. |
| Trafico legitimo de API Cloud | Confirmado. Comportamiento estructural de los servicios en la nube de Microsoft (Power Platform). |

#### Por que es (o no es) una Amenaza?
No es una amenaza. El motor ML alerta basandose unicamente en las matematicas del string (longitud y distribucion de caracteres aleatorios) sin comprender que proveedores cloud como Microsoft utilizan GUIDs largos en sus URLs para enrutar trafico a recursos especificos (tenants) de forma dinamica.

---

### Analisis Evento 2
**ID:** e0dd9e0f...
**Alerta:** DNS Tunneling Anomaly (dns_tunnel)

#### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
- **Origen:** El host `nb-agsilvero.technoma.local` (`192.168.169.99`).
- **Destino:** Servidor DNS interno `ad.technoma.local` (`10.11.1.1`).
- **Contexto:** Similar al Evento 1, pero esta vez con 470 bytes consultando `global.consent.azure-apim.net`.
- **Accion requerida:** Evaluar si es una continuacion del mismo comportamiento o una herramienta diferente.

#### Linea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Ratio | Observacion Forense |
|---|---|---|---|---|---|---|
| 2026-07-16 14:49:58 | 2026-07-16 11:49:58 | dns_tunnel | 470 Bytes | 29.15 Bytes | 16x | Consultas a azure-apim.net |

#### Desglose Tecnico y Diseccion Forense
- La maquina realiza resoluciones DNS para `global.consent.azure-apim.net` y `msmanaged-na...`.
- `azure-apim.net` es el dominio nativo de Azure API Management.
- Resolvio a IPs como `23.97.96.32` que pertenecen al bloque de Microsoft Azure.
- El evento ocurrio menos de 1 minuto despues del primer evento de Power Platform, lo que indica que ambos son parte de la misma sesion del usuario autenticandose o usando una aplicacion en la nube de Microsoft (el "consent" hace referencia a tokens OAuth/SAML).

**Payload / Evidencia Principal:**
```json
{
  "payload_type": "DNS Query (A)",
  "payload_value": "global.consent.azure-apim.net",
  "payload_hash": "N/A",
  "payload_firma": "N/A",
  "payload_accion": "DNS Resolution",
  "payload_destino": "10.11.1.1"
}
```

**Diagnostico e Hipotesis:**
| Hipotesis Formulada | Resultado de Evaluacion |
|---|---|
| DNS Tunneling / Exfiltracion | Descartado. |
| Autenticacion/Consumo de APIs Azure | Confirmado. |

#### Por que es (o no es) una Amenaza?
Es completamente inofensivo. Al igual que el evento anterior, las resoluciones hacia la infraestructura de API de Azure (`azure-apim.net`) implican grandes cadenas CNAME de Traffic Manager (`trafficmanager.net`) para balanceo de carga global, lo que eleva la cantidad de bytes en la respuesta DNS engañando al ML.

---

### CIERRE MAESTRO UNIFICADO

#### Analisis de Impacto CIA Triad
```json
{
  "Confidencialidad": "Ninguna. No hay exfiltracion real, el volumen de bytes se debe al tamaño de las respuestas DNS (CNAMEs) legitimas.",
  "Integridad": "Ninguna.",
  "Disponibilidad": "Ninguna."
}
```

#### Veredicto y Confianza Analitica
```json
{
  "Veredicto": "Falso Positivo",
  "Confianza": "Alta",
  "Justificacion": "Trafico DNS nativo de la plataforma Microsoft 365 / Azure."
}
```

#### Indicador de Fatiga de Alertas
```json
{
  "Clasificacion": "Ruido Estadistico (ML)",
  "Recomendacion": "Excluir de las detecciones de DNS Tunneling los dominios powerplatform.com y azure-apim.net."
}
```

#### Fase del Ciclo NIST 800-61
| Fase NIST | Accion Tecnica |
|---|---|
| Preparacion | Motor ML entrenado para detectar alta entropia en queries DNS. |
| Deteccion y Analisis | Validacion de los dominios raiz (`powerplatform.com` y `azure-apim.net`) confirmando que corresponden a infraestructura Microsoft. |
| Contencion | No requerida. |
| Erradicacion | No requerida. |
| Recuperacion | No requerida. |
| Actividades Post-Incidente | Documentar el comportamiento cloud en la memoria SOC y cerrar alerta. |

#### Playbook Asignado
| ID | Nombre | Justificacion Estrategica |
|---|---|---|
| PB-001 | Falso Positivo / Ruido | Navegacion o uso de apps Cloud oficiales de la empresa. |

#### Resolution Tag para Stellar Cyber
- **Etiqueta:** Falso Positivo
- **Descripcion:** Resoluciones DNS a infraestructura Microsoft Azure/Power Platform.

#### Datos para Bitacora de Excel (UNA SOLA LINEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Deteccion | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripcion | Evidencia | Solicitud de Accion | Estado | URL | Generacion de Ticket | TICKET | Playbook |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 16/07/2026 14:49 | Antigravity | technoma | 12265 | Stellar Cyber | N/A | 46 | DNS Tunneling Anomaly | Falso Positivo - Microsoft Cloud | nb-agsilvero.technoma.local | ML detono alertas por alta entropia y longitud de resoluciones DNS hacia powerplatform.com y azure-apim.net (Azure/Power Apps). | Logs DNS Interflow | Ninguna | Cerrado | N/A | No | N/A | PB-001 |

#### Instruccion para Cierre en Stellar Cyber
**Estado:** Closed
**Resolution Tag:** False Positive
**Comentario final:**
Se investiga la alerta de DNS Tunneling (Exfiltration). El analisis detallado de la captura de red demuestra que no existe ningun tunel activo ni exfiltracion encubierta. El motor de Machine Learning genero un falso positivo al evaluar matematicamente la longitud y entropia de las consultas DNS generadas por el equipo `nb-agsilvero`. Dichas consultas se dirigian a `powerplatform.com` y `azure-apim.net`, dominios oficiales de la infraestructura Cloud de Microsoft (Power Apps, Azure API Management). El volumen de bytes inusual (366 y 470) es resultado de las extensas cadenas de resolucion CNAME (Traffic Manager) y el uso de GUIDs en los URLs de los tenants, comportamiento estandar de plataformas de nube. Se cierra la alerta sin accion requerida.

> [!TIP]
> Dado que el motor de ML de Stellar Cyber seguirá marcando a los dominios estructurados con GUIDs (como Azure y AWS) como Tunneling, se recomienda ejecutar el procedimiento de `update_soc_memory` para documentar estos dominios y crear una nueva plantilla de cierre llamada "IDS Falso Positivo - DNS Tunneling por Servicios Cloud".

#### Desglose Ultra Quirurgico
- **Capa de Red/Enrutamiento:** Origen `192.168.169.99` conectando via vlan 1101 con el servidor DNS local `10.11.1.1` en el puerto destino `53`.
- **Capa de Aplicacion/DPI:** El sensor analiza los paquetes `appid_name: dns`. Descompone el mensaje y extrae `metadata.request.query` y el `effective_tld`.
- **Metadatos TLS/SSL:** No aplica al ser DNS sin cifrar (puerto 53 tradicional).
- **Motor ML:** El modelo que detecta `dns_tunnel` observa el volumen de bytes enviados y recibidos durante una resolucion (`outbytes` y `inbytes`), la entropia en los strings (como `5bbcc1a171964832b76a345a31a53a` = 94 de entropia) y el numero de queries en 5 minutos.
- **Resumen Quirurgico Final:** El usuario accede a una aplicacion corporativa alojada en Microsoft PowerApps, lo que detona un torrente de resoluciones DNS en segundo plano para alcanzar las APIs de Azure correspondientes a ese tenant. El sensor captura estos requests y sus gigantescas respuestas CNAME de balanceo global. El ML se espanta al ver tanto texto largo y entropico que no parece lenguaje humano, marcandolo como un intento matematico de tunelizacion (T1048), cuando en la realidad es un trafico de capa 7 ordinario hacia Azure.
