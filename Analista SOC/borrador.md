**INDEL**

**Informe vCISO**

TECH12397

# Declaratoria de confidencialidad

El presente documento y todo su contenido es de carácter confidencial. **TECHNOMA SAECA** autoriza expresamente a los funcionarios de **Grupo Riquelme (INDEL)** que tengan injerencia directa en la evaluación de este documento, como también a los miembros activos de su Comité de Seguridad, a acceder al contenido de este documento con el propósito exclusivo de la evaluar el contenido del mismo por **TECHNOMA SAECA**. Las personas que accedan al contenido del presente documento aplicarán al menos las mismas buenas prácticas de cuidado de información confidencial que mantienen para la información confidencial de sus propias organizaciones, comprometiéndose a no usar el documento ni su contenido para ningún otro propósito que el establecido en esta declaratoria, ni compartirlo de forma completa ni parcial con personas no autorizadas.

**Glosario**

**CIS Controls (Controles CIS):** Un conjunto priorizado de salvaguardas y mejores prácticas de ciberseguridad industrial desarrolladas por el Center for Internet Security. Su objetivo es proporcionar un estándar de defensa práctico y efectivo frente a los vectores de ataque más comunes en la actualidad.

**CSAT (Cybersecurity Assessment Tool):** Herramienta metodológica oficial utilizada para evaluar, documentar y reportar el nivel de madurez y el estado de implementación de las salvaguardas del marco CIS Controls dentro de una organización.

**Hardening (Endurecimiento de Sistemas):** Proceso técnico continuo de configurar de forma segura los sistemas de TI (servidores, redes, terminales), deshabilitando puertos innecesarios, servicios redundantes, cuentas por defecto y protocolos inseguros para reducir la superficie de ataque inicial.

**End-of-Life (EoL) / Obsolescencia:** Estado de ciclo de vida en el cual un fabricante tecnológico cesa formalmente el soporte, desarrollo y distribución de actualizaciones de software, parches de seguridad o asistencia técnica para un activo, dejándolo expuesto permanentemente a fallas que no se pueden corregir de manera oficial.

**Severidades (CVSS \- Common Vulnerability Scoring System):** Estándar industrial abierto y universal para evaluar la gravedad de las vulnerabilidades informáticas. Las puntuaciones varían de 0.0 a 10.0, donde: **bajo (0.1–3.9), medio (4.0–6.9), alto (7.0–8.9) y crítico (9.0–10.0)**.

**WebShell:** Script o programa malicioso implantado por un atacante en un servidor web vulnerable. Este proporciona una interfaz de administración de consola remota que permite ejecutar comandos de forma ilegítima dentro del sistema operativo del servidor.

**RCE (Ejecución Remota de Código):** Tipo de vulnerabilidad crítica de seguridad que permite a un actor de amenazas ejecutar comandos de forma no autorizada en un servidor o dispositivo remoto, comúnmente sin requerir privilegios administrativos ni credenciales previas de acceso.

# Informe de Análisis de Brechas (GAP Analysis): Controles CIS v8 IG1 - Industrial Delights S.A.E.

## **Resumen**

### **1. Resumen Ejecutivo: La Paradoja de la Autopercepción vs. Realidad Técnica**

Industrial Delights S.A.E. (Indel S.A.E.), el pilar agroindustrial del Grupo Riquelme y responsable de la marca Mazzei, se encuentra en una coyuntura crítica. Su reciente transición a Sociedad Anónima Emisora de Capital Abierto (S.A.E.) y su posicionamiento como "Exportador del Año 2023" imponen una responsabilidad fiduciaria que trasciende la eficiencia operativa; exigen una gobernanza de ciberseguridad robusta y verificable ante el mercado de valores (BVPASA).

El diagnóstico actual revela una discrepancia sistémica entre la autoevaluación CIS CSAT y la realidad técnica detectada en la planta de Villa Elisa. Mientras la organización reporta niveles de implementación cercanos al 100%, los hallazgos en infraestructura evidencian una "seguridad ilusoria".

## **Declaración de postura de riesgo**

La ausencia total de validación independiente (0%) otorga un valor probatorio nulo a los controles declarados. Esta negligencia no solo compromete la continuidad de una planta 100% eléctrica —donde un incidente de red se traduce directamente en una parada de producción y pérdida de materia prima—, sino que genera una responsabilidad legal para el Directorio al presentar estados de cumplimiento que no se corresponden con la superficie de riesgo real.

Indel S.A.E. no puede permitirse "volar a ciegas". La falta de mecanismos de verificación anula la confianza técnica, dejando la propiedad intelectual de las fórmulas BE FIT y la estabilidad operativa de su cadena de suministro expuestas a interrupciones críticas. El siguiente apartado detalla esta brecha mediante métricas de madurez contrastadas.

## **Riesgos de gobierno TIC y continuidad del negocio**

La calificación de riesgo arrojada para Indel S.A.E. es **Extrema**. Es imperativo señalar que los controles C16 (Seguridad de Software) y C18 (Penetration Testing) figuran como "0" o "No Assessed", lo cual es inaceptable para una empresa de capital abierto que gestiona integraciones críticas con Molino Cereales y Cadena Real.

Los hallazgos técnicos correlacionados con el marco CIS v8 exponen la fragilidad de la cadena de suministro alimentaria del Grupo Riquelme:

### **Riesgo de Interrupción de operaciones comerciales por ransomware [Controles CIS C04 / CIS C08 / CIS C07]:**

La ausencia de configuraciones seguras (hardening con credenciales por defecto en cámaras e impresoras) y la falta de aislamiento en consolas de gestión de red (MikroTik .113, UniFi .147) permiten que un adversario o código malicioso se propague lateralmente hacia los servidores de bases de datos centrales (Microsoft SQL Server 2022 en la IP .199). La inhabilitación o cifrado de estos sistemas paralizaría de forma inmediata la facturación, los inventarios y la distribución de productos hacia los 25.000 puntos de venta de Mazzei, además de detener la maquinaria automatizada de la planta de Villa Elisa.

### **Exfiltración de información sensible, fuga de datos y extorsión pública [Controles CIS C03 / CIS C09]:**

Se identificaron vectores de Ejecución Remota de Código (RCE con severidades críticas de hasta 9.8 en el componente gSOAP 2.7 y 8.8 en Microsoft SQL Server 2022). Un actor de amenazas puede vulnerar estas plataformas de producción para extraer datos confidenciales, secretos industriales, recetas patentadas y fórmulas de la línea BE FIT antes de activar mecanismos de extorsión pública, generando pérdidas financieras millonarias y daño irreversible a la reputación corporativa.

### **Responsabilidad legal y de gobierno por omisión de validación [Control CIS C18]:**

Operar con un 0% en Pruebas de Penetración y carecer de validación independiente para los controles reportados al 100% significa que la administración asume una protección conceptual sin sustento técnico comprobado. Ante una brecha de seguridad, esta discrepancia entre lo declarado y la realidad operativa puede interpretarse como una omisión fiduciaria de información relevante frente a accionistas, auditorías externas y los entes reguladores de la BVPASA.

### **Monitoreo y Defensa de Red [Controles CIS C13]:**

Con un 0% de implementación en visibilidad y monitoreo de tráfico de red, la organización carece de capacidades para detectar anomalías, balizas de mando y control (C2) o desplazamientos laterales en tiempo real dentro del perímetro de manufactura y administración.

## **Gobernanza y madurez de controles**

### **2. Análisis Cuantitativo CIS CSAT y Benchmarking de Madurez**

Para una empresa emisora, el contraste entre la autopercepción y el promedio de la industria es el indicador principal de su resiliencia tecnológica. La siguiente tabla expone el abismo entre lo declarado por Indel S.A.E. y la validación externa:

**Tabla Comparativa: Implementación Reportada vs. Promedio de la Industria**

| Control CIS (v8) | Descripción | % Imp. Indel S.A.E. | % Promedio Industria | Gap de Validación |
| :---: | :--- | :---: | :---: | :--- |
| C01 | Inventario de Activos | 100% | 33% | 0% Validado |
| C02 | Inventario de Software | 100% | 31% | 0% Validado |
| C04 | Configuración Segura | 100% | 39% | 0% Validado |
| C07 | Gestión de Vulnerabilidades | 6% | 39% | Deficiencia Crítica |
| C08 | Gestión de Logs | 100% | 36% | 0% Validado |
| C12 | Gestión de Infraestructura | 100% | 41% | 0% Validado |
| C13 | Monitoreo de Red | 0% | 33% | Ausencia Total |
| C16 | Seguridad de Software App | 0% | 20% | Riesgo Inexcusable |
| C18 | Pruebas de Penetración | 0% | 30% | No Evaluado |

### **Análisis del Gap de Validación y Cumplimiento**

La calificación de riesgo es Extrema. Es imperativo señalar que los controles C16 (Seguridad de Software) y C18 (Penetration Testing) figuran como "0" o "No Assessed", lo cual es inaceptable para una empresa de capital abierto que gestiona integraciones críticas con Molino Cereales y Cadena Real.

La anomalía en el Control C07 (6% vs 39%) confirma que Indel S.A.E. carece de un ciclo de vida para la mitigación de vulnerabilidades. Al no existir validación externa, el 100% reportado en otros dominios es puramente declarativo y carece de sustento técnico, lo que podría interpretarse como una omisión de información relevante para los inversionistas y entes reguladores.

### **Brecha actual frente a la higiene cibernética básica**

Las métricas globales reflejan un rezago sustancial en los pilares formales de gobernanza:

| Nº | Pilar de Gobernanza | Estado Diagnosticado en Indel S.A.E. |
| :---: | :--- | :--- |
| **1** | **Falta de Definición Normativa** | Múltiples subcontroles de seguridad operan en estado "Sin Política Formal", careciendo de directrices aprobadas por el Directorio. |
| **2** | **Informalidad Generalizada** | Las prácticas de administración de contraseñas y accesos se gestionan bajo acuerdos verbales del equipo técnico del momento, sin documentación de respaldo. |
| **3** | **Inexistencia de Aprobación Corporativa** | Las salvaguardas declaradas no cuentan con actas de aprobación institucional que otorguen obligatoriedad normativa y alcance fiduciario. |
| **4** | **Fatiga y Operación Manual** | Las tareas de verificación técnica y control de infraestructura se ejecutan de manera manual, saturando al equipo interno e impidiendo la detección temprana de intrusiones. |

### **Análisis de controles críticos CIS**

| Control CIS v8 | Concepto Operativo | Beneficio para el Negocio | Diagnóstico en Indel S.A.E. |
| :--- | :--- | :--- | :--- |
| **CIS C18: Pruebas de Penetración** | Simulación periódica de ciberataques reales mediante especialistas éticos independientes. | Certifica ante el Directorio y la BVPASA que las defensas tecnológicas resisten adversarios reales. | **0% de madurez (Promedio: 30%).** Inexistencia de evaluaciones ofensivas; la postura de seguridad es puramente teórica. |
| **CIS C04: Configuración Segura (Hardening)** | Deshabilitación de servicios innecesarios, puertos inseguros y contraseñas de fábrica en todos los activos. | Neutraliza los puntos de entrada más comunes de cibercriminales y bloquea la elevación de privilegios. | **Deficiencia Crítica.** Cámaras Hikvision operan con `admin/12345` e impresoras Ricoh con clave en blanco. |
| **CIS C08: Gestión de Registros (Logs)** | Centralización, custodia y correlación de eventos de seguridad de firewalls, servidores y bases de datos. | Brinda trazabilidad forense histórica y capacidad de alerta temprana ante ataques silenciosos. | **0% Validado.** Aunque se reporta 100% de implementación, no existe auditoría independiente que garantice la integridad de los registros. |
| **CIS C07: Gestión de Vulnerabilidades** | Detección automatizada, priorización y remediación de fallos de seguridad en software y sistemas. | Cierra las ventanas de exposición frente a exploits públicos que puedan detener la manufactura. | **6% de madurez (Promedio: 39%).** Presencia de fallos RCE críticos no mitigados en SQL Server 2022 y componentes web. |
| **CIS C13: Monitoreo y Defensa de Red** | Inspección continua del tráfico de red para alertar y bloquear anomalías y movimientos laterales. | Evita que un atacante que comprometa un dispositivo periférico alcance los servidores de producción. | **0% de madurez (Promedio: 33%).** Ausencia total de visibilidad sobre el tráfico interno de la planta y oficinas. |
| **CIS C06: Control de Accesos** | Asignación de privilegios mínimos y autenticación multifactor (MFA) para consolas administrativas. | Protege las consolas de gestión de red contra accesos no autorizados internos o remotos. | **Vulnerable por Exposición.** Interfaces MikroTik, UniFi y FortiClient EMS accesibles desde segmentos generales. |

## **Visibilidad de activos y servicios expuestos**

### **3. Mapeo de Brechas Técnicas a Salvaguardas CIS (IG1)**

Los hallazgos técnicos correlacionados con el marco CIS v8 exponen la fragilidad de la cadena de suministro alimentaria del Grupo Riquelme.

### **CIS C01, C12 y C13: Gestión de Activos y Visibilidad de Red**

Se detectó una exposición crítica de interfaces administrativas que deberían estar estrictamente segmentadas. La visibilidad de estos activos permite movimientos laterales que podrían paralizar la planta:

### **CIS C04: Configuraciones Seguras (Hardening)**

La ausencia de una política de "Zero Default Passwords" es alarmante. Se ha verificado acceso a dispositivos críticos mediante credenciales de fábrica:

| Control / Categoría | Detalle del Hallazgo Técnico |
| :--- | :--- |
| **Gestión de Red Expuesta** | MikroTik RouterOS (.113) y UniFi Network Controller (.147:8080) accesibles desde segmentos generales. |
| **Activos Críticos Omitidos** | El servidor FortiClient Endpoint Management Server (.120) es un objetivo de alto valor para el despliegue de malware y se encuentra expuesto sin capas de protección adicionales. |
| **Telefonía Legacy** | Unidades Cisco SPA2102 (.22 y .88), dispositivos en estado End-of-Life, introducen riesgos de seguridad no remediables en la infraestructura de voz. |
| **Video-Vigilancia** | Cámaras Hikvision/HiLook en las IPs 192.168.102.48, 192.168.102.154 y 192.168.102.251 operan con combinaciones admin/12345 o admin/admin. |
| **Infraestructura de Impresión** | Equipos Ricoh Web Image Monitor en las IPs 192.168.102.138, 192.168.102.157 y 192.168.102.240 permiten acceso administrativo con usuario admin y contraseña en blanco. |

## **Riesgo operacional y panorama de amenazas**

### **CIS C07: Gestión Continua de Vulnerabilidades**

El escaneo identificó vectores de Ejecución Remota de Código (RCE) que comprometen la integridad de los datos de producción:

| Hallazgos de Software | Detalle Técnico y Severidad |
| :--- | :--- |
| **1. Microsoft SQL Server 2022 (.199)** | Vulnerable a CVE-2023-38169 y CVE-2021-1636 (Score 8.8). Un compromiso aquí alteraría la logística de los 25.000 puntos de venta de Mazzei. |
| **2. CastPortal (Nginx .21)** | El portal de producción expone interfaces que requieren auditoría inmediata para evitar intrusiones en la capa de aplicaciones. |
| **3. Componente gSOAP 2.7 (10.0.0.4:81)** | Crítico (Score 9.8) con exploits públicos para CVE-2021-21783. |
| **4. Ubiquiti Infrastructure** | Servidores lighttpd 1.4.54 (.13, .16) afectados por CVE-2022-22707. |
| **Impacto de negocio** | |
| La interrupción de la infraestructura de red en Indel S.A.E. no es solo un problema de TI; es un riesgo de negocio que puede detener una planta cuya operatividad depende de sistemas eléctricos y automatizados. La Alta Dirección debe actuar para proteger la reputación de Mazzei y la estabilidad del Grupo Riquelme. | |

## **Vulnerabilidades y riesgo de explotación**

La concentración de vulnerabilidades críticas en sistemas transaccionales y de gestión de red plantea un vector directo de compromiso de la infraestructura productiva:

| Identificador | Vector de Explotación y Activo Afectado | Severidad (CVSS) | Impacto Técnico Estimado |
| :---: | :--- | :---: | :--- |
| **VULN-01** | **Microsoft SQL Server 2022 (IP: 192.168.102.199)**<br>Vulnerabilidades CVE-2023-38169 y CVE-2021-1636 | **8.8 (Alta)** | Ejecución de comandos no autenticados y manipulación directa de registros transaccionales, inventarios y despachos de Mazzei. |
| **VULN-02** | **Componente gSOAP v2.7 (IP: 10.0.0.4, Puerto 81/tcp)**<br>Exploit público disponible para CVE-2021-21783 | **9.8 (Crítica)** | Ejecución Remota de Código (RCE) que permite el control absoluto del servidor e implantación de consolas WebShell. |
| **VULN-03** | **CastPortal Nginx (IP: 192.168.102.21)**<br>Interfaces de producción expuestas sin auditoría de aplicaciones | **Alta** | Punto de entrada a la red interna y evasión de controles perimetrales a través de la capa web de manufactura. |
| **VULN-04** | **Servidores lighttpd 1.4.54 Ubiquiti (IPs: .13, .16)**<br>Vulnerabilidad conocida CVE-2022-22707 | **7.5 (Alta)** | Denegación de servicio o desbordamiento de búfer en equipamiento de conectividad de planta. |

## **Plan de acción y remediación**

### **4. Plan de Acción y Remediación Estratégica (Roadmap Big 4)**

Este plan de 90 días está diseñado para migrar de una postura reactiva a una de cumplimiento validado, protegiendo la ventaja competitiva de la manufactura limpia y eléctrica.

### **Fase I: Endurecimiento Inmediato (0-30 días)**

| Nº | Acción de Remediación | Detalle Técnico |
| :---: | :--- | :--- |
| **1** | **Remediación de Credenciales** | Rotar inmediatamente las contraseñas por defecto en cámaras (.48, .154, .251) e impresoras Ricoh (.138, .157, .240). |
| **2** | **Aislamiento de Interfaces** | Implementar listas de control de acceso (ACLs) para restringir el acceso a MikroTik (.113), UniFi (.147) y FortiClient EMS (.120) únicamente desde una VLAN de gestión autenticada. |

### **Fase II: Mitigación de Vulnerabilidades Críticas (30-60 días)**

| Nº | Acción de Remediación | Detalle Técnico |
| :---: | :--- | :--- |
| **1** | **Ciclo de Parcheo de Base de Datos** | Priorizar la actualización de Microsoft SQL Server 2022 (.199) y la actualización/reemplazo del componente gSOAP en la IP 10.0.0.4 para neutralizar riesgos de RCE. |
| **2** | **Seguridad de Aplicaciones** | Realizar un escaneo profundo de vulnerabilidades sobre el CastPortal (.21) para asegurar que la interfaz de producción no sea un punto de entrada a la red interna. |

### **Fase III: Validación y Monitoreo Continuo (60-90 días)**

| Nº | Acción de Remediación | Detalle Técnico |
| :---: | :--- | :--- |
| **1** | **Cierre de Brecha de Visibilidad** | Implementar soluciones de monitoreo de tráfico (C13) para detectar anomalías en tiempo real. |
| **2** | **Auditoría de Terceros** | Ejecutar un ejercicio de validación externa para convertir el cumplimiento autodeclarado en cumplimiento técnico certificado, mitigando el riesgo de responsabilidad legal del Directorio ante la BVPASA. |

## **Brecha operativa**

Es imperativo que la dirección de Indel S.A.E. delimite claramente los roles de ciberseguridad en la organización:

| Actor / Rol | Responsabilidad Primaria | Limitación Operativa |
| :--- | :--- | :--- |
| **Equipo de TI Interno** | Garantizar la disponibilidad operativa y continuidad de la planta de Villa Elisa y la logística comercial. | No dispone de dedicación exclusiva ni herramientas para el monitoreo y análisis de amenazas 24/7. |
| **Servicio de vCISO (Technoma)** | Liderar la gobernanza estratégica, diseño de políticas y maduración hacia estándares CIS IG2. | No ejecuta remediaciones de infraestructura, desarrollo de software ni vigilancia operativa de alertas en tiempo real. |
| **SOC 24/7 (Centro de Operaciones)** | Vigilancia táctica continua, detección de intrusiones y contención de incidentes en tiempo real. | Requiere coordinación estrecha con TI interno y alineamiento bajo las directrices del vCISO. |

Con 40 subcontroles operados manualmente y vectores RCE expuestos, resulta ineludible la integración de un servicio de SOC 24/7 administrado que actúe como escudo táctico sobre los servidores productivos y gateways de red.

## **Transición a la fase 2 del servicio vCISO (Gobierno y Madurez IG2) adicionando el servicio administrado SOC**

Bajo la Fase 2 de acompañamiento continuo integrada con el Servicio Administrado de SOC, Technoma asumirá la responsabilidad de:

| Nº | Eje de Trabajo | Objetivo y Alcance Estratégico |
| :---: | :--- | :--- |
| **1** | **Gobernar y Auditar** | Supervisar la efectividad del SOC 24/7, garantizando el cumplimiento de SLAs y tiempos de respuesta ante incidentes en la planta. |
| **2** | **Formalizar Documentación** | Redactar y someter al Directorio las políticas formales de seguridad para cerrar los 41 subcontroles que carecen de marco normativo escrito. |
| **3** | **Madurez CIS IG2** | Implementar autenticación multifactor (MFA) y segmentación avanzada, preparando a Indel S.A.E. para auditorías fiduciarias y cumplimiento BVPASA. |
| **4** | **Pruebas de Penetración Periódicas (CIS C18)** | Coordinar ejercicios anuales de Red Teaming y validación ética independiente para certificar la resiliencia real de los sistemas de producción. |

## **Cierre del informe**

Cierre del Informe: La interrupción de la infraestructura de red en Indel S.A.E. no es solo un problema de TI; es un riesgo de negocio que puede detener una planta cuya operatividad depende de sistemas eléctricos y automatizados. La Alta Dirección debe actuar para proteger la reputación de Mazzei y la estabilidad del Grupo Riquelme.

## **Anexos Técnicos**

### **Resumen de hallazgos controles CIS**

A continuación se detalla el mapa de calor obtenido del relevamiento CIS v8 IG1 para Indel S.A.E. frente al promedio internacional:

| Control CIS v8.1 | Descripción y Cobertura Operativa | Cumplimiento Indel S.A.E. | Promedio Industria | Gap de Madurez | Prioridad Estratégica vCISO |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **CIS C18** | Pruebas de Penetración | 0% | 30% | -30% | **Crítica.** Ausencia total de validación independiente. |
| **CIS C16** | Seguridad de Software de Aplicación | 0% | 20% | -20% | **Crítica.** Riesgo inexcusable en portales de producción. |
| **CIS C13** | Monitoreo y Defensa de Red | 0% | 33% | -33% | **Crítica.** Ceguera ante movimientos laterales en planta. |
| **CIS C07** | Gestión de Vulnerabilidades | 6% | 39% | -33% | **Crítica.** Presencia de fallos RCE sin ciclo de mitigación. |
| **CIS C04** | Configuración Segura de Activos | 100% (0% Validado) | 39% | Deficiencia Real | **Crítica.** Vulnerabilidades por credenciales estándar. |
| **CIS C08** | Gestión de Logs de Auditoría | 100% (0% Validado) | 36% | Brecha Probatoria | **Alta.** Falta de verificación de integridad y centralización. |
| **CIS C01** | Inventario de Activos (Hardware) | 100% (0% Validado) | 33% | Brecha Probatoria | **Media.** Requiere auditoría dinámica automatizada. |
| **CIS C02** | Inventario de Software | 100% (0% Validado) | 31% | Brecha Probatoria | **Media.** Falta de control de ciclo de vida de aplicaciones. |
| **CIS C12** | Gestión de Infraestructura de Red | 100% (0% Validado) | 41% | Brecha Probatoria | **Alta.** Interfaces de gestión expuestas sin segmentación. |

### **Detalle de puertos, servicios y vulnerabilidades**

La siguiente matriz consolida los activos y servicios de Indel S.A.E. que requieren intervención técnica inmediata:

| Dirección IP / Activo | Servicio Expuesto / Puerto | Vulnerabilidad / Condición | Severidad (CVSS) | Impacto Técnico Estimado |
| :--- | :---: | :--- | :---: | :--- |
| **192.168.102.199** | Microsoft SQL Server 2022 Puerto 1433/tcp | CVE-2023-38169 / CVE-2021-1636 | **8.8 (Alta)** | Ejecución no autorizada; alteración de datos de distribución de 25.000 puntos de venta. |
| **10.0.0.4:81** | Componente gSOAP v2.7 Puerto 81/tcp | CVE-2021-21783 (Exploits públicos) | **9.8 (Crítica)** | Ejecución Remota de Código (RCE) y control administrativo del servidor de producción. |
| **192.168.102.21** | CastPortal (Nginx) Puerto 80/443/tcp | Exposición de interfaz de manufactura | **Alta** | Vector potencial de intrusión y acceso a la red interna desde la capa web. |
| **192.168.102.13, .16** | Ubiquiti lighttpd v1.4.54 Puerto 80/tcp | CVE-2022-22707 | **7.5 (Alta)** | Fallos de desbordamiento en infraestructura de conectividad inalámbrica. |
| **192.168.102.113** | MikroTik RouterOS Puerto 80/8291/tcp | Gestión accesible desde segmentos generales | **Alta** | Riesgo de interceptación y desconfiguración de tablas de enrutamiento de planta. |
| **192.168.102.147:8080** | UniFi Network Controller Puerto 8080/tcp | Consola de control Wi-Fi expuesta | **Media** | Modificación no autorizada de políticas de acceso inalámbrico. |
| **192.168.102.120** | FortiClient EMS Consola Endpoint | Servidor expuesto sin capas adicionales | **Alta** | Objetivo de alto valor para despliegue no autorizado de malware en terminales. |
| **192.168.102.22, .88** | Cisco SPA2102 Telefonía VoIP | Dispositivos en estado End-of-Life (EoL) | **Media** | Vulnerabilidades no corregibles por cese de soporte del fabricante. |
| **192.168.102.48, .154, .251** | Cámaras Hikvision / HiLook Puerto 80/554/tcp | Credenciales de fábrica (`admin/12345`) | **Crítica** | Sabotaje de videovigilancia física y punto de pivoteo hacia la red interna. |
| **192.168.102.138, .157, .240** | Ricoh Web Image Monitor Puerto 80/tcp | Credenciales de fábrica (usuario `admin`, clave vacía) | **Alta** | Interceptación de documentación confidencial y acceso a configuraciones de red. |