# Reporte de Guardia SOC — Sábado 10/10/2026
**Fecha:** 10/10/2026  
**Modalidad:** Home Office / Cobertura de Guardia  
**Analista:** Kevin Moraes  
**Tenants:** Technoma, CAJA ANDE  
**Estado:** Cerrado  

---

## 🎯 Resumen Ejecutivo de la Guardia
* **Monitoreo de Consolas:** Monitoreo continuo de consolas sobre Tenants Technoma y CAJA ANDE en Stellar Cyber, Cortex XDR y Sophos Central. Descarte de falsos positivos de rutina. Sin incidentes activos durante el periodo.
* **Auditoría Forense de Ingesta y Cuota Stellar Cyber:**
  * Se auditó el exceso de consumo del clúster (~16.0 GB/día vs. límite recomendado).
  * Aislamiento de causas raíz: FortiGate Syslog generando 8.22 GB/día (2.9M de eventos) por sesiones LAN de alta frecuencia, y bucle DNS de Grafana hacia `zbx.technoma.com.py` consumiendo 2.90 GB/día (1.75M de consultas innecesarias).
  * Emisión de informes técnicos: *Informe Ejecutivo de Causa Raíz Ingesta DNS Grafana* y *Plan Maestro de Reducción Quirúrgica de Ingesta* (~6.5 GB/día objetivo).
* **Auditoría de Seguridad de Log Filters (Cero Puntos Ciegos):**
  * Revisión de los 65 filtros activos de la plataforma para asegurar que ninguna regla oculte amenazas, balizamiento C2 o movimiento lateral.
  * Emisión del documento técnico: *Auditoría de Seguridad de Log Filters y Riesgos de Ceguera SOC*.
* **Estandarización:**
  * Redacción de la *Guía Técnica Oficial de Filtrado Quirúrgico de Logs* y *Guía Operativa de Triaje y Threat Hunting*.
