# Compendio Técnico de Release Notes de Stellar Cyber (Versiones 6.4.0 a 7.0.0s)
*Compilado y Documentado para Hermes SOAR & Operaciones de Inteligencia SOC*  
*Fecha de Registro: 17 de Octubre de 2026*

---

## 📌 Introducción y Propósito Operativo

Este documento consolida la totalidad de cambios, nuevas capacidades, ajustes de comportamiento, mejoras de APIs, resoluciones de bugs y arquitecturas de Inteligencia Artificial introducidas en Stellar Cyber desde la versión **6.4.0** hasta la **7.0.0s** (Octubre 2026).

Su propósito es servir de **guía técnica permanente** para:
1. **Maximizar la eficiencia del agente IA y SOAR** en la interacción automatizada con la consola Open XDR.
2. **Optimizar la gestión de cuota e ingesta** mediante Log Filters y Parser Studio.
3. **Prevenir fallos de integración** adaptando scripts y mixins a los cambios de API y tipos de datos del vendor.
4. **Habilitar integración nativa vía MCP Server (Model Context Protocol)** y parsers de agentes de IA.

---

## 🚀 1. Stellar Cyber 7.0.0s (Release Principal - Agosto a Octubre 2026)

### A. Hitos y Capacidades Principales (Highlights)
* **Alert & Case Auto-Triage con Colas de Casos (ASOC-152)**:
  * Resúmenes automáticos por IA y triaje por cola de casos.
  * Nueva cola predeterminada **AI Analyst** dedicada para casos críticos.
  * Servicio desacoplado de colas que notifica directamente al motor de Autonomous SOC ante cambios de estado de casos.
* **Métricas de Casos (Case Metrics - AELDEV-66747)**:
  * Plantillas de inicio rápido o temporizadores custom (MTTA, MTTR, SLAs de guardia) integrables como columnas en las colas de casos y en la vista detallada de caso.
* **Evidencias Forenses Detalladas de Sandbox en Malware (AELDEV-72819)**:
  * Reporte profundo de sandbox (Sophos/Stellar) con procesos, artefactos de archivos, registros y conexiones de red directamente visibles en el panel de la alerta para validar veredictos sin saltar de consola.
* **Evolución Mayor de Parser Studio (AELDEV-71125, AELDEV-70204, AELDEV-70203)**:
  * Métrica de ingesta rodante de 7 días (`7d Ingestion`) por parser y workflow automatizado **Disable Inactive Parsers** para apagar parsers huérfanos que consumen RAM del sensor.
  * Creación de parsers desde cero (*from scratch*) y descarga de configuraciones de parsers modulares para portabilidad cross-tenant.
* **APIs Públicas del System Action Center (AELDEV-68354)**:
  * Creación y gestión programática de acciones automáticas (bloqueos, webhooks, aislamientos) vía REST API sin depender de clics manuales en la UI.
* **Printable Payload en Alertas IDS (AELDEV-72713)**:
  * Incorporación del campo `ids.payload_details.payload_printable` en Interflow. El paquete activador de la firma IDS se presenta en texto claro legible inline.
* **Nuevas Detecciones Basadas en Contexto**:
  * *Active Directory Pass-the-Ticket* (`AELDEV-59279`): Cruza peticiones TGS sin previo TGT para la cuenta.
  * *M365 Sign-In from Never-Before-Seen ASN* (`AELDEV-68306`): Con ventana de entrenamiento y supresión scoped por tenant.
  * *SSH Brute Force Aborted Sessions* (`AELDEV-68309`): Evalúa sesiones SSH cortadas en estado `Aborted` comúnmente omitidas en scans masivos.
* **Acciones de Respuesta Extendidas**:
  * Bloqueo y desbloqueo directo de **URLs y Dominios en Firewalls FortiGate** (`AELDEV-67465`).
  * Acciones de respuesta sobre Microsoft Defender for Endpoint (`AELDEV-67002`).
  * Contención de Malops multidispotivo en Cybereason (`AELDEV-68264`).

### B. Cambios de Comportamiento Críticos (Behavior Changes)
* **AELDEV-67525**: En respuestas de error de la API (5xx), el identificador pasa de ser `requestId` a **`request_id`** (snake_case estándar).
* **AELDEV-67820**: Los endpoints públicos de sensores bajo `/data_sensors` ahora exigen privilegios RBAC explícitos (retornan HTTP 403 Forbidden si el perfil API carece de permisos de interfaz equivalentes).
* **AELDEV-28743**: El endpoint `/tenant_groups` ya no devuelve la imagen en base64 en `tgrp_logo`; ahora se consulta bajo demanda en `/tenant_group/{id}/logo`.

### C. Detección y Machine Learning
* **AELDEV-67555**: Agrupación automática de casos usando campos `correlation_info` emitidos por reglas ATH (ej. UPN común o identificador unificado).
* **AELDEV-71314**: Mejora en el scoring de fidelidad para *Successful Login After Brute Force* originado en IPs privadas (ajustado para IPs que carecen de ASN).
* **AELDEV-70538**: Supresión y deduplicación inteligente de alertas recurrentes de ESET Inspect por máquina y regla en lugar de `eset.eialarmid`.

### D. Plataforma, Sensores y Conectores
* **DATA-3502 (Crucial para Agentes IA)**: Introducción de parser nativo para **telemetría de Claude Code / AI Coding Assistants vía OpenTelemetry sobre HTTP en puerto 6210**. Normaliza prompts, herramientas invocadas, ejecuciones de comandos, consumo de tokens y llamadas API.
* **DATA-3634 (Crucial para Log Filters)**: **Fix mayor en Log Filters**. Se corrigió el fallo donde comparaciones numéricas de igualdad `==` o `!=` en reglas de filtro nunca hacían match debido a discrepancia de tipo string vs integer (los logs pasaban de largo). Con este fix, reglas de puerto o severidad numérica aplican descarte estricto.
* **AELDEV-73161**: El campo `Log Source` en Log Filters fue clarificado con la etiqueta **(Log Forwarder only)** para evitar confusiones en conectores o agentes Windows.
* **AELDEV-72988**: Comando CLI en sensores Linux `show support vm-resource-check` para auditar en segundos CPU steal time, presión de I/O y reclamo de memoria por parte del hipervisor (VMware/KVM).
* **AELDEV-70760**: El responder de FortiGate ahora cierra sesión administrativa explícita tras cada acción de bloqueo/desbloqueo, eliminando el agotamiento de sesiones administrativas en el firewall.

---

## 🤖 2. Stellar Cyber 6.6.0 (Julio 2026)

### A. Autonomous SOC y Model Context Protocol (MCP)
* **Consolidación del Stellar Cyber MCP Server**:
  * Implementación oficial de la capa de integración bajo el estándar **Model Context Protocol (MCP)**.
  * Permite a agentes de IA externos (como Claude Code, Hermes o clientes locales) interactuar de forma segura y gobernada con Stellar Cyber mediante tokens API scoped.
  * **Operaciones Soportadas vía MCP**: Búsqueda y listado de casos, lectura de alertas y observables, correlaciones MITRE ATT&CK, actualización de estado/campos de casos y consultas contextuales tenant-aware.
* **AI Assistance en Casos Auto-Triaged**:
  * Ventana de diálogo interactivo con IA dentro del caso para consultar en lenguaje natural el porqué del veredicto, verificar las señales del Verdict Signal Check (VSC) y lanzar hipótesis forenses sobre los datos del caso.
* **Visibilidad de Veredicto en Vistas Principales**:
  * Incorporación de las columnas de veredicto de Auto-Triage directamente en la **Alert Table** y en **Threat Hunting**, permitiendo filtrar y descartar masivamente eventos benignos.
* **Panel de Respuesta Rápida en Auto-Triage**:
  * Posibilidad de ejecutar contención o mitigación en alertas de phishing o compromiso directamente desde la vista del motor de triaje sin entrar a cada caso individual.

### B. Sistema y Plataforma
* **Platform Health Monitoring (EAP)**: Monitoreo centralizado de salud de procesadores y clúster dentro del System Action Center.
* **Conectores y Normalizaciones**: Mejoras en conectores de Active Directory sobre LDAPS y Universal Webhook Responder con enriquecimiento contextual.

---

## 🧠 3. Stellar Cyber 6.5.0 (Mayo a Julio 2026)

### A. Capacidades Destacadas
* **Lanzamiento Inicial del MCP Server (Early Access Program)**:
  * Primera versión del servidor Model Context Protocol de Stellar Cyber, abriendo la plataforma para el desarrollo de analistas autónomos externos gobernados por RBAC.
* **Aparición de Parser Studio**:
  * Entorno interactivo para diseñar, clonar, testear en dry-run y desplegar parsers personalizados sin necesidad de reiniciar sensores ni alterar código base.
* **Detección: Successful Login After Brute Force**:
  * Algoritmo de detección que correlaciona ataques distribuidos de fuerza bruta provenientes de múltiples IPs con un inicio de sesión exitoso posterior desde una IP no observada.
* **Cobertura de Auditoría AWS Config**:
  * Ingesta y correlación de cambios de configuración y violaciones de cumplimiento en infraestructura cloud de AWS.
* **Importación y Exportación de Reglas ATH**:
  * Capacidad de exportar e importar paquetes de reglas de Automated Threat Hunting en JSON/YAML entre distintos clústeres y entornos de prueba.

---

## ⚡ 4. Stellar Cyber 6.4.0 (Marzo 2026)

### A. Capacidades Destacadas
* **Intelligent Case Analysis & Narrative Summaries**:
  * Generación automática de síntesis ejecutiva, hipótesis investigativas, líneas de tiempo y recomendaciones de respuesta en casos de alta severidad.
* **Detección de Patrones de SQL Injection por ML**:
  * Análisis de comportamiento sobre tráfico web HTTP identificando intentos iterativos de inyección SQL externos y en movimientos laterales internos.
* **VPN Login Failure Anomaly**:
  * Modelo estadístico de comportamiento anómalo aplicado a concentradores VPN (Fortinet FortiGate, Check Point, Palo Alto Networks GlobalProtect).
* **Dashboard Builder Responsivo**:
  * Reestructuración del sistema de tableros con disposición modular basada en grillas flexibles.

---

## 🛠️ 5. Matriz de Impacto para el Agente Hermes y SOAR Command Center

| Vector / Componente SOAR | Cambio del Vendor | Acción Requerida en Nuestro Código / Procedimientos |
| :--- | :--- | :--- |
| **Manejador de Errores REST** | Cambio `requestId` $\to$ `request_id` (7.0.0s) | En [`soar_app/core/infra.py`](file:///g:/Hermes%20+%20Antigravity/soar/soar_app/core/infra.py), asegurar que `RestSessionManager` soporte ambos campos para logs limpios. |
| **Extracción Forense IDS** | Nuevo campo `ids.payload_details.payload_printable` | Enriquecer la pestaña Hunter y el Worker de Triage (`triage_ops_mixin.py`) para renderizar el payload inline y evitar descargas de PCAP. |
| **Integración de Agente MCP** | Stellar Cyber MCP Server disponible (6.5+) | Configurar en el entorno local el conector MCP de Stellar Cyber con un API Key scoped en Perfil para permitir consultas y cierres automatizados nativos. |
| **Telemetría de AI Agents** | Ingesta nativa Claude Code / OTel en port 6210 | Enviar logs de ejecución de nuestros propios scripts a Stellar Cyber para trazabilidad de operaciones del SOAR. |
| **Log Filtering y Cuota** | Fix en comparadores numéricos `==`/`!=` (DATA-3634) | Los filtros de ingesta desplegados en el sensor modular (ej. puertos 53, 445, 135) ahora operan con máxima rigurosidad y precisión matemática. |
| **Parser Hygiene** | 7d Ingestion y Disable Inactive Parsers | Monitorear el sensor modular de Technoma y desactivar parsers que no reciben tráfico para recuperar memoria en el nodo. |

---
*Fin del Compendio. Archivo mantenido bajo control de cambios en la base de conocimiento local del SOC.*
