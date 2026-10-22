# Herramientas y Scripts de Automatización Stellar Cyber

Este directorio contiene las herramientas de auditoría, threat hunting, gestión de casos y filtros de logs diseñadas para interactuar mediante API con la plataforma **Stellar Cyber**.

---

## 🛠️ Inventario de Herramientas

| Script | Descripción |
| :--- | :--- |
| `stellar_cli.py` | CLI principal para interactuar con la API de Stellar Cyber. |
| `stellar_log_filter_manager.py` | Administrador de filtros de logs (creación, edición y descarte de cuota). |
| `stellar_alerts_checker.py` | Consulta y monitoreo de alertas de seguridad recientes. |
| `stellar_case_fetcher.py` | Extractor de incidentes y casos abiertos en Stellar Cyber. |
| `stellar_threat_hunter.py` | Motor de threat hunting automatizado sobre los índices de ingestión. |
| `threat_hunting_auditor.py` | Auditoría de las 20 consultas del panel de Threat Hunting y consumo de cuota. |
| `threat_hunting_exact_auditor.py` | Análisis de consumo exacto de fuentes ruidosas y candidatos a exclusión. |
| `audit_benign_domains.py` | Identificación de dominios benignos de alta frecuencia (Microsoft, Google, etc.). |
| `scan_tags_non_standard.py` | Escaneo y auditoría de tráfico no estándar o anómalo en la red. |
| `verify_cajaande_stdport.py` | Verificación de tráfico estándar vs no estándar para clientes específicos. |
