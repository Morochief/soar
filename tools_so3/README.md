# Herramientas y Scripts de Automatización Security Onion 3 (SO3)

Este directorio contiene las utilidades y scripts operacionales diseñados específicamente para interactuar, diagnosticar y configurar la infraestructura de **Security Onion 3 (Standalone: 172.17.10.25)** sin interferir con las utilidades de Stellar Cyber.

---

## 🛠️ Inventario de Herramientas

| Script | Descripción | Uso Operacional |
| :--- | :--- | :--- |
| `so3_client.py` | Wrapper SSH & Sudo con soporte UTF-8, SFTP temporal y gestión de conexiones. | Módulo base reutilizable por todas las herramientas. |
| `check_status.py` | Comprobación de salud de los 23 contenedores (`so-status`). | Monitoreo rápido del estado del grid. |
| `check_logstash.py` | Diagnóstico de `so-logstash`, memoria/heap (`lsheap`), reinicios y logs en tiempo real. | Inspección de pipeline y fallos de ingestión. |
| `check_bpf.py` | Muestra y valida las reglas BPF Pre-DPI activas en Suricata y Zeek, y compila contra `bond0`. | Verificación de filtros de paquetes crudos. |
| `check_filters.py` | Lista los 21 filtros Logstash en disco y comprueba su inclusión en el Pillar de SaltStack. | Auditoría de reglas de descarte de ruido. |
| `audit_filter_effectiveness.py` | **Auditoría Matemática de Efectividad**: Compara volumen indexado histórico vs. tiempo real para validar que el ruido cayó a 0 eventos. | Validación formal de descarte y detección de fugas. |
| `manage_cases.py` | **Gestor y Creador Automatizado de Casos**: Permite crear, listar y escalar incidentes automáticamente en `so-case` con historial (`so-casehistory`). | Orquestación SOAR y paridad con Stellar Cyber. |

---

## 🚀 Ejemplos de Ejecución Directa

```bash
# 1. Comprobar salud de los contenedores
python soar/tools_so3/check_status.py

# 2. Diagnosticar Logstash y heap de memoria
python soar/tools_so3/check_logstash.py

# 3. Validar filtros Pre-DPI (BPF) de Suricata y Zeek
python soar/tools_so3/check_bpf.py

# 4. Verificar filtros personalizados de Logstash
python soar/tools_so3/check_filters.py

# 5. Auditar efectividad matemática de filtros y BPF (Antes vs. Ahora)
python soar/tools_so3/audit_filter_effectiveness.py

# 6. Listar y Crear Casos Automatizados en Security Onion
python soar/tools_so3/manage_cases.py --list
python soar/tools_so3/manage_cases.py --create --title "Ataque Detectado" --desc "Detalle forense" --severity critical
```
