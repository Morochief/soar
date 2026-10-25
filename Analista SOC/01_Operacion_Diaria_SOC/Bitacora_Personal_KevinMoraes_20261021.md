# Bitácora Técnica de Ingeniería SOC - 21 de Octubre de 2026

- **Fecha:** 21 de Octubre de 2026
- **Autor / Ingeniero:** Kevin Moraes
- **Servidor Objetivo:** `soc-onion` (`172.17.10.25`)
- **Tema:** Unificación y Despliegue de Filtros de Log en Security Onion, Resolución de Conflictos HTTP 409 y Supresión de Ruido en ElastAlert2.

---

## 1. Resumen Ejecutivo de la Jornada

Durante esta jornada se llevaron a cabo trabajos de consolidación de reglas de filtrado de logs entre el SOAR, la plataforma Stellar Cyber y Security Onion 3, así como la corrección de errores recurrentes en el motor de detección de ElastAlert2.

---

## 2. Acciones y Modificaciones Realizadas en `soar/`

### A. Sincronización y Despliegue de Filtros de Ingesta
- **Archivos creados/modificados:**
  - `apply_so_fix.py`
  - `apply_all_stellar_filters_to_so.py`
  - `apply_complete_54_stellar_filters_to_so.py`
- **Objetivo:** Automatizar la inyección de los 54 filtros de descarte y prefiltrado homologados desde Stellar Cyber directamente hacia las pipelines de Logstash en Security Onion (`/opt/so/conf/logstash/pipelines/`).
- **Impacto:** Reducción drástica del volumen de ingesta de eventos no relevantes (ruido de broadcast, traps internos no analíticos y pings de salud), optimizando el ancho de banda y la capacidad de almacenamiento en Elasticsearch.

### B. Diagnóstico y Corrección de Excepciones HTTP 409 en ElastAlert2
- **Archivos creados/modificados:**
  - `get_elastalert_error_sample.py`
  - `locate_failing_rule.py`
  - `get_elastalert_top_failing_rules.py`
  - `read_elastalert_defaults.py`
  - `apply_elastalert_fix.py`
  - `sed_elastalert.py`
  - `silence_409_permanent.py`
- **Problema Detectado:** ElastAlert2 arrojaba de forma continua excepciones `HTTP 409 Conflict` al intentar escribir en los índices de estado (`elastalert_status*`), saturando `/opt/so/log/elastalert/` y degradando el rendimiento del contenedor `so-elastalert`.
- **Causa Raíz:** Colisiones de concurrencia en la escritura de documentos de control entre múltiples hilos de evaluación de reglas.
- **Solución Implementada:**
  - Se configuró la directiva `silence_errors_in_log` en los archivos de configuración por defecto de ElastAlert.
  - Se ajustó el mapeo de los índices de control y se aplicó la persistencia mediante scripts de parcheo para evitar la sobrescritura tras reinicios.

---

## 3. Estado al Cierre del Día 21/10/2026
- Filtros de Stellar Cyber desplegados y operativos en Logstash.
- Reducción del registro de errores en ElastAlert2.
- Detección de una anomalía subsiguiente: reinicios periódicos del contenedor `so-logstash`, quedando programada su investigación a fondo para el día 22.
