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

## **Cierre del informe**

Cierre del Informe: La interrupción de la infraestructura de red en Indel S.A.E. no es solo un problema de TI; es un riesgo de negocio que puede detener una planta cuya operatividad depende de sistemas eléctricos y automatizados. La Alta Dirección debe actuar para proteger la reputación de Mazzei y la estabilidad del Grupo Riquelme.