---
name: security-onion-daily
description: Genera el informe diario ejecutivo (/daily) de Security Onion 3, resumiendo salud del Grid, casos abiertos, amenazas Suricata filtradas y bloqueos perimetrales.
---

# Security Onion Daily Executive Summary

Cuando el usuario solicite un informe diario, estado del día, resumen de guardia o el comando `/daily` / `/daily-onion`, ejecuta:

```bash
python soar/tools_so3/daily_onion_summary.py
```

Presenta el resultado de forma ejecutiva destacando:
1. Salud de los recursos (Disco `/nsm`, RAM, estado del cluster Elasticsearch).
2. Casos nuevos generados automáticamente en `so-case`.
3. Amenazas NIDS relevantes detectadas en red por Suricata (con ruido de AnyDesk/Telegram filtrado).
4. Top atacantes bloqueados por los firewalls.
5. Recomendaciones puntuales para la guardia del SOC.
