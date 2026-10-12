---
name: analyze_stellar_alert
description: "Analiza automáticamente volcados JSON de Stellar Cyber/Interflow aplicando triaje forense estructurado en 4 fases, formato nativo Stellar y cierre unificado."
risk: low
source: workspace
date_added: '2026-10-03'
---

# Skill: Analista SOC Experto — Triaje y Análisis de Alertas Stellar Cyber

Esta skill se activa al recibir volcados de texto estructurado o bloques JSON nativos de **Stellar Cyber OpenXDR / Interflow**.

---

## 🎯 Principios de Diseño: Orden, Claridad y Cierre Maestro Unificado

1. **Conteo y Declaración de Lote:**  
   Al recibir múltiples eventos (array `docs`), se debe declarar de inmediato el número total de eventos analizados (ej. *«He analizado un lote de 4 eventos correlacionados en Interflow»*).
2. **Causalidad Consolidada (Fin del Desorden):**  
   ESTÁ PROHIBIDO repetir tablas o JSONs redundantes 10 veces por cada evento similar. Se analiza la **causalidad integral del incidente como un único caso consolidado**, cruzando el tráfico de red, los activos y las firmas disparadas.
3. **Formato Nativo Oficial de Stellar Cyber:**  
   Todo reporte incluye obligatoriamente los 4 bloques canónicos de la plataforma (`Resumen General`, `Origen de la Amenaza`, `Impacto en el Destino`, `Mitigación y Estado`).
4. **Comentario de Cierre Humanizado:**  
   Redactado en un párrafo analítico fluido y continuo (prohibidas las listas numeradas mecánicas del tipo *"1. El primer evento..."*).
5. **Doble Bitácora:**  
   Genera la fila oficial de 18 columnas en TSV (para la bitácora de Excel) y la ficha modular para la Bitácora Personal en Markdown.

---

## 📋 Estructura Estándar de Respuesta (Las 4 Fases Claras)

Toda respuesta debe seguir esta estructura limpia y sin saturación:

### Fase 1: Declaración de Ingesta y Resumen Ejecutivo Nativo Stellar Cyber
* **Conteo:** Total de eventos analizados en el lote.
* **Tabla de Entidades Críticas:** Activo Origen (IP, Host, MAC), Activo Destino (IP, Host/Dominio, Puerto), Protocolo, Firmas IDS / Reglas disparadas, Severidad.
* **Resumen Ejecutivo (Los 4 Puntos Oficiales de Stellar Cyber):**
  * `Resumen General:` Breve síntesis del incidente y la anomalía detectada.
  * `Origen de la Amenaza:` Host, IP y proceso o usuario causante.
  * `Impacto en el Destino:` Qué activos recibieron el tráfico y si hubo compromiso.
  * `Mitigación y Estado:` Estado del caso y acciones de respuesta.

### Fase 2: Triaje y Correlación Forense
* **Disección Técnica y Causalidad:** Explicación analítica clara de por qué el motor de Stellar Cyber / IDS disparó la alerta y qué estaba ocurriendo en realidad (diferenciando ruido operativo de ataque real).
* **IOCs y Firmas Disparadas:** Tabla compacta con SID, nombre de firma, clasificación de severidad y payload/query.
* **Matriz de Impacto CIA:** Evaluación breve (Confidencialidad, Integridad, Disponibilidad).
* **Veredicto y Confianza:** Uno de los 4 cuadrantes estándar (`True Positive`, `False Positive`, `Benign True Positive`, `Unclear`) con porcentaje de confianza analítica (0-100%).
* **Playbook SOC Asignado:** Mapeo al catálogo oficial de Technoma SOC (`PB-X.X`) y técnica MITRE ATT&CK.

### Fase 3: Instrucción de Cierre en Stellar Cyber
* **Estado:** `Closed` / `Resolved`.
* **Resolution Tag:** `False Positive` / `Benign` / `True Positive`.
* **Comentario de Cierre Maestro:** Párrafo técnico humanizado y elegante, listo para copiar y pegar en el modal de cierre de caso de Stellar Cyber.
* **Recomendación de Tuning / Regla de Supresión:** Parámetros exactos de filtro o whitelist en Stellar Cyber para mitigar la fatiga de alertas si se trata de un falso positivo recurrente.

### Fase 4: Exportación de Bitácoras
1. **Bitácora Oficial de Turno (18 Columnas):** Tabla de apoyo visual + bloque de código ````tsv```` de 1 clic para pegar en Excel o Google Sheets.
2. **Ficha para Bitácora Personal Markdown:** Bloque formateado listo para incorporar al archivo `Analista SOC/Bitacora_Personal_Casos_SOC.md`.
