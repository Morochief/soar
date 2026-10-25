# Bitácora Técnica de Ingeniería SOC - 22 de Octubre de 2026

- **Fecha:** 22 de Octubre de 2026
- **Autor / Ingeniero:** Kevin Moraes
- **Servidor Objetivo:** `soc-onion` (`172.17.10.25`)
- **Tema:** Resolución del Reinicio Cíclico de Logstash (15 min), Auditoría y Depuración Selectiva de Espacio en `/nsm` e Inicio del Proceso de Upgrade a Security Onion 3.3.0.

---

## 1. Resumen Ejecutivo de la Jornada

Se resolvió la causa raíz que provocaba la caída y reinicio forzado de `so-logstash` cada 15 minutos exactos debido a una desincronización en el orquestador SaltStack. Paralelamente, se realizó una auditoría forense del almacenamiento en `/nsm` liberando espacio de logs locales caducos sin tocar telemetría de clientes, preparando el terreno para el upgrade mayor de Security Onion.

---

## 2. Acciones y Modificaciones Realizadas en `soar/`

### A. Diagnóstico y Estabilización Definitiva de Logstash
- **Archivos creados/modificados:**
  - `check_messages_earlier.py`, `check_drop_states.py`, `find_drop_9027.py`
  - `check_9027_perms.py`, `cmp_files.py`, `check_stat.py`
  - `check_soc_logstash_pillar.py`, `check_pillar_lines.py`
  - `fix_permanent_restart_cause.py`, `apply_clean_pillar.py`
- **Causa Raíz:** En `/opt/so/saltstack/local/pillar/logstash/soc_logstash.sls` existía una clave obsoleta `pipeline_config:`. Cada 15 minutos el cron `highstate_schedule` ejecutaba SaltStack, provocando un conflicto entre `defined_pipelines` y `pipeline_config`. Esto hacía que Salt detectara un falso cambio de archivo (`File changed`) en las reglas `9027` y `9028`, disparando `docker_container.mod_watch` que mataba y recreaba a `so-logstash`.
- **Solución:** Limpieza de la clave conflictiva en el Pillar y reasignación de permisos `660` (`logstash:socore`). Logstash alcanzó estabilidad operativa ininterrumpida.

### B. Auditoría y Liberación Forense de Espacio en `/nsm`
- **Archivos creados/modificados:**
  - `clean_more_space.py`, `list_es_indices.py`, `check_es_sources.py`
  - `check_agents_breakdown.py`, `check_datasets.py`, `check_hosts_syslog.py`
  - `check_zeek_suricata.py`, `check_data_streams_indices.py`, `delete_old_zeek_index.py`
- **Directiva Estricta Cumplida:** Cero impacto en datos de clientes. Se preservaron intactos los eventos de:
  - **Valores (`valores-ndr` / FortiGate):** 12.6 millones de eventos intactos.
  - **Vascol (`secops-vascol`):** 4.8 millones de eventos intactos.
- **Acción:** Eliminación selectiva de índices Zeek/Suricata antiguos generados por tráfico local de prueba previo, recuperando gigabytes críticos en `/nsm`.

### C. Automatización y Preparación del Upgrade a SO 3.3.0
- **Archivos creados/modificados:**
  - `run_config_backup.py`, `launch_soup.py`, `check_soup_status.py`
  - Scripts de auditoría previa de parámetros CLI y prompts interactivos de `soup`.
- **Acción:** Creación de backups de configuración y lanzamiento del proceso oficial de actualización (`soup -y`) hacia la versión 3.3.0.

---

## 3. Estado al Cierre del Día 22/10/2026
- `so-logstash` completamente estable sin reinicios cíclicos.
- Almacenamiento en `/nsm` optimizado con datos de clientes resguardados.
- Proceso `soup` en ejecución durante la noche/madrugada.
