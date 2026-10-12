# Reporte de Guardia SOC — Domingo 11/10/2026
**Fecha:** 11/10/2026  
**Modalidad:** Home Office / Cobertura de Guardia  
**Analista:** Kevin Moraes  
**Tenants:** Technoma, CAJA ANDE  
**Estado:** En Seguimiento (Caso Zabbix)  

---

## 🎯 Resumen Ejecutivo de la Guardia
* **Monitoreo de Consolas:** Monitoreo continuo de consolas sobre Tenants Technoma y CAJA ANDE en Stellar Cyber, Cortex XDR y Sophos Central. Consolas en estado verde sin alertas críticas abiertas.
* **Remediaciones Quirúrgicas en Producción (Stellar Cyber):**
  * **CCTV Dahua (DHCP Relay):** Corrección del filtro de la cámara (`192.168.16.16`) con esquema numérico IANA `proto: 17` UDP, suprimiendo ráfagas de renovaciones locales al gateway (`192.168.16.1:67`) sin generar puntos ciegos.
  * **Filtro #64 (WUDO Puerto 7680):** Reconfiguración en producción a 5 dimensiones estrictas (`dev_type: fw_fortigate`, `action: deny`, `dstport: 7680`, `proto: 6` TCP, `srcip/dstip: 192.168.169.0/24, 192.168.100.0/24`), eliminando el punto ciego de C2 saliente y escaneos hacia servidores y Domain Controllers.
* **Detección Técnica en Seguimiento:**
  * **Servidor Zabbix (`192.168.15.31`):** Se identificó el ruido y alto volumen de sondeos hacia agentes internos (TCP 10050). Se diseñó la especificación técnica de mitigación de 5 dimensiones, pero **NO se aplicó en producción**; queda formalmente en estado **EN SEGUIMIENTO** para presentar y validar la estrategia con Jefatura del SOC (Ivan Centurión).
