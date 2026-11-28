# Scripts de una sola vez que modifican producción

Estos scripts se usaron **una vez** para cambios puntuales en Security Onion / Stellar
(borrar un índice concreto, parchear salt/logstash/elastalert, silenciar errores 409, etc.).
Antes estaban en la raíz del repo junto a las herramientas de uso diario, y era fácil
volver a ejecutarlos por error.

**No los ejecutes de nuevo sin leerlos antes:** varios tienen objetivos fijos
(por ejemplo `delete_old_zeek_index.py` borra `.ds-logs-zeek-so-2026.10.21-000053`) y
asumen el estado que tenía el servidor ese día.

Quedan aquí como registro histórico, referenciados desde las bitácoras de
`Analista SOC/01_Operacion_Diaria_SOC/`.
