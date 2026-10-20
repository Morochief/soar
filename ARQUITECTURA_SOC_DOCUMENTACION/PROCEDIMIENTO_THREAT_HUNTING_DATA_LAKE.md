# 🎯 PROCEDIMIENTO ESTÁNDAR: THREAT HUNTING DIRECTO EN DATA LAKE DE STELLAR CYBER

> **Capa RAG**: `PROCEDIMIENTO_ARQ` / `MEMORIA_SOC`  
> **Herramienta Oficial**: [`stellar_threat_hunter.py`](file:///g:/Hermes%20+%20Antigravity/soar/stellar_threat_hunter.py)  
> **Objetivo**: Permitir al analista y a la IA buscar y correlacionar eventos crudos en vivo directamente contra el Data Lake de Stellar Cyber (Interflow, Syslog, WinEventLog, Firewall, Cortex XDR) usando sintaxis Lucene nativa y agregaciones forenses sin esperas ni pasos manuales.

---

## ⚡ Comandos Rápidos de Caza (Threat Hunting)

### 1. Caza por IP (Bidireccional: Origen o Destino)
Busca cualquier conexión, log de firewall o evento de Windows donde participe la IP:
```powershell
python stellar_threat_hunter.py --ip 172.16.202.24 --limit 10
```

### 2. Caza por Usuario (Active Directory / Host)
Busca inicios de sesión, intentos de autenticación Kerberos/NTLM o tráfico asociado al usuario:
```powershell
python stellar_threat_hunter.py --user egonzalez --limit 15
```

### 3. Expresiones Lucene Avanzadas
Combina puertos, protocolos, acciones de firewall y clases de mensaje:
```powershell
# Buscar tráfico denegado en puertos SMB o RDP
python stellar_threat_hunter.py --query "action:deny AND (dstport:445 OR dstport:3389)"

# Caza en logs de Windows para procesos PowerShell o CMD
python stellar_threat_hunter.py --query "process_name:*powershell.exe*" --index winevent

# Caza de tráfico saliente por puertos no estándar
python stellar_threat_hunter.py --query "msg_class:interflow_traffic AND NOT dstport:(80 OR 443 OR 53)"
```

### 4. Agregaciones Forenses y Estadísticas (Top Talkers)
Extrae los principales orígenes, destinos o puertos sin tener que leer todos los logs:
```powershell
# Top puertos con bloqueos en Firewall
python stellar_threat_hunter.py --query "action:deny" --top-ports

# Top IPs de origen generando conexiones
python stellar_threat_hunter.py --query "msg_class:interflow_traffic" --top-srcip

# Top IPs de destino de un host sospechoso
python stellar_threat_hunter.py --ip 192.168.169.133 --top-dstip
```

---

## 🏗️ Arquitectura Técnica y Filtros de Índices

* **Endpoint**: `https://{STELLAR_HOST}/connect/api/data/*{index_filter}*{date}*{tenantid}*/_search`
* **Índices Soportados (`--index`)**:
  - `*` (Búsqueda global cruzada)
  - `adr` (Interflow de red y flujos de tráfico enriquecido)
  - `winevent` / `wineventlog` (Logs de seguridad de Windows de agentes Winlogbeat/Elastic)
  - `syslog` (Eventos recibidos vía Syslog de Firewalls, Switches y Linux)
  - `audit` (Auditoría de plataforma, cambios de configuración y logins)
  - `ade` (Alertas y detecciones de Machine Learning)
