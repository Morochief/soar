# 📋 INFORME TÉCNICO EJECUTIVO: CAUSA RAÍZ DE EXCESO DE CUOTA Y SATURACIÓN DNS
### Auditoría Forense de Ingesta, Análisis de Tráfico y Plan de Remediación (Playbook 6.3)

---

| Metadato | Detalle Operativo |
| :--- | :--- |
| **Fecha de Emisión** | 10 de Octubre de 2026 |
| **Referencia Playbook** | **Playbook 6.3** — *Agente o cliente supera capacidad de ingesta* |
| **Severidad de Negocio** | **CRÍTICA** (Incumplimiento de Licencia de Plataforma) |
| **Alerta Stellar Cyber** | `Violation: System is out of compliance due to continuous daily usage violations for over 21 days` |
| **Autor / Analista** | Kevin Moraes — Analista SOC / Detección y Respuesta |
| **Clasificación** | Uso Interno Exclusivo — Technoma SOC & NOC |
| **Ubicación en Repositorio** | `G:\SOC\soar\Analista SOC\Reportes\Informe_Ejecutivo_Causa_Raiz_Ingesta_DNS_Grafana.md` |

---

## 1. Resumen Ejecutivo (Executive Summary)

Durante los últimos 21 días, la plataforma **Stellar Cyber OpenXDR** del tenant Technoma ha estado operando fuera de cumplimiento de licencia debido a una ingesta diaria continua de **14.1 GB a 16.7 GB diarios** (superando la cuota contratada).

Tras una auditoría forense sobre los 12 millones de eventos diarios, se determinó que **el 60% de todas las resoluciones DNS corporativas (1,631,994 eventos en 24 horas)** proviene de un solo equipo interno:
* **Host Culpable:** `192.168.15.23` (Servidor de Grafana del NOC en VLAN-15).
* **Destino Saturado:** `10.11.1.1` (`ad.technoma.local` — Controlador de Dominio / DNS de Technoma).
* **Causa Raíz:** Los dashboards de monitoreo del NOC actualizan múltiples paneles cada 1 a 5 segundos consultando al servidor Zabbix mediante FQDN (`zbx.technoma.com.py`). Al no tener caché DNS local el sistema operativo Linux/Go, dispara una doble consulta (**IPv4 'A'** e **IPv6 'AAAA'**) a razón de **~19 consultas por segundo ininterrumpidas (24/7)**.
* **Impacto en Licencia:** Esta máquina sola consume **~2.88 GB diarios**, acumulando más de **60 GB ingeridos en el período de infracción**.
* **Remediación Requerida:** 2 minutos de configuración en el servidor Grafana (creación de entrada estática en `/etc/hosts` o cambio de URL a IP interna directa), lo cual erradica 1.63M de eventos sin degradar en lo más mínimo la seguridad del SOC.

---

## 2. Evidencia Forense en Interflow (The Smoking Gun)

### 2.1. Métricas de la Consulta en Stellar Cyber
* **Filtro Aplicado:** `srcip: 192.168.15.23 AND dstport: 53`
* **Índice Interrogado:** `Traffic` / `aella-adr-*`
* **Ventana de Tiempo:** Últimas 24 horas.
* **Total de Eventos Detectados:** **`1,631,994 Resultados`**

```text
Distribución Temporal en Tabla (Muestreo segundo a segundo):
-------------------------------------------------------------------------------------------------------
Timestamp               Source Host       Destination Host     Tenant      Query FQDN             Tipo
-------------------------------------------------------------------------------------------------------
2026-10-10 11:38:39     192.168.15.23     ad.technoma.local    technoma    zbx.technoma.com.py    AAAA
2026-10-10 11:38:39     192.168.15.23     ad.technoma.local    technoma    zbx.technoma.com.py    AAAA
2026-10-10 11:38:39     192.168.15.23     ad.technoma.local    technoma    zbx.technoma.com.py    AAAA
2026-10-10 11:38:39     192.168.15.23     ad.technoma.local    technoma    zbx.technoma.com.py    AAAA
2026-10-10 11:38:32     192.168.15.23     ad.technoma.local    technoma    zbx.technoma.com.py    AAAA
2026-10-10 11:38:31     192.168.15.23     ad.technoma.local    technoma    zbx.technoma.com.py    AAAA
2026-10-10 11:38:29     192.168.15.23     ad.technoma.local    technoma    zbx.technoma.com.py    AAAA
2026-10-10 11:38:28     192.168.15.23     ad.technoma.local    technoma    zbx.technoma.com.py    AAAA
-------------------------------------------------------------------------------------------------------
```

### 2.2. Desglose del Registro Raw Interflow (`_id: GNJEJqEBI3UnQyDOJnY5`)
```json
{
  "srcip": "192.168.15.23",
  "srcip_host": "192.168.15.23",
  "dstip": "10.11.1.1",
  "dstip_host": "ad.technoma.local",
  "dstport": 53,
  "proto": 17,
  "vlan": 1101,
  "port_name": "ethernet1",
  "domain_list": ["zbx.technoma.com.py"],
  "metadata": {
    "request": {
      "query": "zbx.technoma.com.py",
      "query_type": "AAAA",
      "effective_tld": "technoma.com.py"
    },
    "response": {
      "resolved_ips": [],
      "reply_code": "No Error",
      "answers": [
        {
          "name": "technoma.com.py",
          "host": "ad.technoma.local",
          "host_type": "SOA"
        }
      ]
    }
  }
}
```

#### Hallazgos Técnicos Clave del Registro:
1. **La Consulta `AAAA` (IPv6):** Grafana solicita resolución IPv6. Como `zbx.technoma.com.py` solo opera en IPv4, el servidor DNS devuelve una respuesta vacía con registro `SOA` (`resolved_ips: []`). Esto provoca que la aplicación intente reconsultar inmediatamente, **duplicando el volumen de paquetes**.
2. **El Sensor Afectado:** La captura proviene del puerto espejo físico **`ethernet1`** en la **VLAN 1101** del colector modular `technoma-sensor` (`192.168.15.70`).

---

## 3. Justificación Arquitectónica: ¿Por qué se configuró así?

El equipo de infraestructura/NOC configuró el origen de datos usando el FQDN `zbx.technoma.com.py` siguiendo buenas prácticas de desarrollo:
* **Soporte de Certificados SSL/TLS:** Si Zabbix opera bajo HTTPS, la validación del certificado exige coincidencia del Common Name (CN).
* **Abstracción de Red:** Permite migrar el servidor Zabbix sin tener que reconfigurar decenas de paneles en Grafana.
* **VirtualHosting:** Permite que proxies inversos ruteen el tráfico correctamente mediante el encabezado `Host`.

### El Fallo Operativo Desapercibido:
A diferencia de los sistemas Windows (que integran el servicio de caché `Dnscache`), el runtime de **Go** y las instalaciones estándar de **Linux para servidores carecen de caché DNS local por defecto**. Al configurarse paneles en pantallas del NOC con auto-refresh de 1 a 5 segundos, el servidor se transformó involuntariamente en un cañón de peticiones DNS.

---

## 4. Postura de Ciberseguridad SOC: ¿Por qué NO se descarta en el Sensor?
*(En estricto cumplimiento de la política de Gobernanza SOC `soc-surgical-filtering`)*

El servidor `192.168.15.23` tiene su puerto de servicio 3000 **publicado a Internet mediante DNAT** (`190.128.219.210:3000`) y recibe escaneos constantes externos.

> [!CAUTION]
> **POLÍTICA DE CERO PUNTOS CIEGOS (ZERO BLIND SPOT POLICY):**  
> Si el SOC aplicara un filtro genérico en el sensor (`host 192.168.15.23 and port 53` en Pre-DPI):
> 1. Si un atacante compromete el servidor de Grafana vía vulnerabilidad web, **el SOC quedaría completamente ciego** ante exfiltración encubierta por **DNS Tunneling** (*dnscat2*, *iodine*) o comunicación con servidores de Comando y Control (**C2**).
> 2. **Por ello, la remediación DEBE ejecutarse en origen (en el host), preservando al 100% la capacidad de detección del sensor.**

---

## 5. Plan de Remediación Inmediata (NOC / Infraestructura)

Se solicita al equipo del NOC aplicar **una** de las siguientes opciones en el servidor `192.168.15.23` (tiempo estimado: 2 minutos):

### Opción A (Recomendada — Vía `/etc/hosts` en Linux):
Editar el archivo `/etc/hosts` del servidor de Grafana:
```bash
sudo nano /etc/hosts
```
Agregar la siguiente línea al final:
```text
192.168.15.31    zbx.technoma.com.py
```
Guardar los cambios.
* **Mecanismo:** El sistema operativo resolverá `zbx.technoma.com.py` desde su tabla estática local en 0.0001 ms. Ningún paquete UDP 53 saldrá por la red física hacia el DC.
* **Seguridad Preservada:** Si el servidor intenta resolver cualquier otro dominio o un C2 en Internet, **la consulta saldrá por la red y Stellar Cyber disparará la alerta normalmente**.

### Opción B (Vía Interfaz Web de Grafana):
1. Ingresar a Grafana (`http://192.168.15.23:3000`).
2. Ir a **Configuration | Data Sources** ➔ Seleccionar el datasource de Zabbix.
3. Cambiar el campo **URL** de `http://zbx.technoma.com.py:[puerto]` a la IP directa:
   ```text
   http://192.168.15.31:[puerto]
   ```
4. Presionar **Save & Test**.

---

## 6. Resultados Esperados y Métricas de Éxito

| Métrica | Antes de la Remediación | Después de la Remediación | Reducción / Ahorro |
| :--- | :---: | :---: | :---: |
| **Consultas DNS Diarias (`192.168.15.23`)** | 1,631,994 eventos | **< 100 eventos** | **-99.99%** |
| **Volumen de Ingesta Interflow** | ~16.0 GB / día | **~13.1 GB / día** | **-2.9 GB diarios** |
| **Carga en el DC `ad.technoma.local`** | ~19 queries / seg | **0 queries / seg** | **Alivio total de CPU/Red** |
| **Cumplimiento de Licencia Stellar Cyber** | ❌ Violación (>21 días) | ✅ **Conforme a Cuota** | **Normalización del Contrato** |
| **Visibilidad de Seguridad del SOC** | 100% | **100% (Cero Puntos Ciegos)** | **Sin Pérdida de Detección** |

---

## 7. Verificación Post-Remediación
Tras aplicar el cambio, el analista de guardia ejecutará la query de control en **Threat Hunting | Interflow Search**:
```lucene
srcip: 192.168.15.23 AND dstport: 53
```
* **Criterio de Aceptación:** El contador de resultados en la ventana de 1 hora debe ser **cero (0)**.
