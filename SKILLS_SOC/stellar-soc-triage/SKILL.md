---
name: stellar-soc-triage
description: Procedimiento formal de triaje de alertas en 7 etapas para analistas SOC utilizando Stellar Cyber OpenXDR, formato nativo y justificacion humanizada de cierre.
risk: low
source: workspace
date_added: '2026-09-17'
---

# Procedimiento de Triaje de Alertas SOC (7 Etapas) - Stellar Cyber OpenXDR

## Cuando utilizar este skill
- Al analizar volcados de alertas o telemetria cruda en formato JSON de Stellar Cyber, Interflow, EDR (Sophos, Cortex) o Firewalls (FortiGate).
- Al realizar el triaje operativo de tickets o incidentes en el Cockpit SOC.
- Al redactar justificaciones tecnicas humanizadas de resolucion y cierre para auditorias en Stellar Cyber.
- Al evaluar priorizacion de incidentes, impacto en la triada CIA y clasificacion en los 4 cuadrantes de veredicto.

## Metodologia de Triaje en 7 Etapas

### Etapa 1: Ingestion y Centralizacion
- Capturar la totalidad de los eventos correlacionados en el lago Interflow sin descartar logs.
- Declarar explicitamente el volumen de eventos crudos analizados en el lote.

### Etapa 2: Categorizacion Estrategica
- Mapear la amenaza a la taxonomia correspondiente y a la matriz MITRE ATT&CK (Tactica y Tecnica con ID formal).
- Identificar la clase de activo afectado (DC, Mail Server, Servidor Web DMZ, Endpoint usuario).

### Etapa 3: Priorizacion Dinamica (5 Factores)
1. Criticidad del Activo (DC o Servidor de Base de Datos vs Laptop de usuario).
2. Etapa del Ataque (Reconocimiento temprano vs Ejecucion / Persistencia vs Exfiltracion activa).
3. Cruce CTI (Reputacion en VirusTotal, AbuseIPDB, URLScan, CISA KEV).
4. Score de Anomalia vs Baseline (Puntuacion ML del sensor vs comportamiento historico).
5. Contexto de Negocio y Horario (Horario laboral vs madrugada o ventana de mantenimiento).

### Etapa 4: Investigacion y Evidencia Forense
- Extraer IOCs concretos: IPs, puertos, FQDNs, URLs, hashes SHA256/MD5, comandos CLI.
- Analizar ventana temporal de comportamiento (+/- 30 minutos).
- Revisar historial de alertas en el host para identificar falsos positivos tipificados en la Memoria Institucional.
- Determinar alcance lateral (evento aislado mono-host vs campana multi-host).

### Etapa 5: Determinacion y Veredicto (Los 4 Cuadrantes)
Clasificar estrictamente en uno de los 4 veredictos:
1. True Positive (TP): Actividad maliciosa confirmada -> Escalar a IR / Contencion activa.
2. False Positive (FP): Alerta sobre actividad benigna o ruido operacional -> Cerrar caso y proponer tuning.
3. Benign True Positive (BTP): Comportamiento real pero autorizado (HealthMailbox, respaldos, escaneos acordados) -> Cerrar caso y evaluar exclusion.
4. Unclear (Indeterminado): Evidencia insuficiente -> Retener caso o solicitar telemetria adicional.

Evaluar impacto en la Triada CIA (C0-C3, I0-I3, A0-A3) y asignar porcentaje de Confianza Analitica (0-100%).

### Etapa 6: Escalacion y Respuesta (SLA L1 15 min)
- Ruteo segun niveles: Tier 1 (Cierre o escalacion inicial), Tier 2 (DFIR / Aislamiento EDR), Tier 3 / CERT-PY (Incidentes criticos mayores).
- Asignar el Playbook oficial de Technoma correspondiente de los 28 disponibles.

### Etapa 7: Documentacion y Mejora Continua
- Emitir la recomendacion tecnica concreta de tuning de deteccion (regla de supresion o whitelist en Stellar Cyber) para mitigar la fatiga de alertas.
- Generar la linea de registro para la bitacora de Excel.

---

## Formato Estricto de Respuesta

Toda respuesta de analisis debe presentar obligatoriamente los tres bloques estructurados:

### Bloque 1: Resumen Ejecutivo del Caso (Formato Nativo Stellar)
- Resumen General
- Origen de la Amenaza
- Impacto en el Destino
- Mitigacion y Estado

### Bloque 2: Triaje Forense Estructurado (Metodologia de 7 Etapas)
- Etapa 1 a Etapa 7 detalladas con datos de telemetria.

### Bloque 3: Instruccion para Cierre en Stellar Cyber (Cierre Humanizado)
- Estado: Closed / Resolved
- Resolution Tag: False Positive / Benign / True Positive
- Comentario de Cierre Maestro: Parrafo redactado en lenguaje natural analitico, profesional y claro, justificando tecnicamente el motivo del cierre ante auditorias.
- Datos para Bitacora de Excel (18 Columnas): Presentar la tabla de apoyo visual (columnas A a R) y el bloque de código ````tsv```` listo para copiar con 1 solo clic y pegar directamente en Excel/Google Sheets.
