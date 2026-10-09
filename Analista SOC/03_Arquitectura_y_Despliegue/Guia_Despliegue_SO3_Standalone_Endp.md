# Guía de Migración y Despliegue: Security Onion 3 (Standalone + Endpoints)

**Objetivo:** Proporcionar a Cómputo/Infraestructura los requerimientos para desplegar Security Onion 3 en arquitectura **Standalone** (Todo en uno), integrando tanto telemetría de red como **monitoreo de Endpoints (Elastic Agent / Sysmon)**.

---

## 1. Estrategia de Migración (EoL 2.4)
> [!WARNING] 
> **Fin de Ciclo de Vida (EoL):** Security Onion 2.4 dejará de tener soporte oficial el **1 de Octubre de 2026**.

> [!TIP]
> **¡BUENAS NOTICIAS PARA INFRAESTRUCTURA!** 
> Dado que el servidor actual 2.4 ya corre sobre **Oracle Linux 9**, **NO es obligatorio formatear ni provisionar nuevo hardware**. La migración se puede realizar en el mismo equipo (In-Place Upgrade) ejecutando los scripts nativos de SO:
> 1. Asegurar backup válido en `/nsm/backup`
> 2. `sudo soup` *(Para llegar a la última versión 2.4.211)*
> 3. `sudo soupto3` *(Descarga el actualizador a la versión 3)*
> 4. `sudo soup` *(Ejecuta la migración a la v3)*
> 
> *Nota: Al agregar monitorización de Endpoints (Elastic Agents), el hardware actual probablemente colapsará. Cómputo **debe** escalar el hardware de este mismo equipo según los requerimientos debajo (Especialmente agregando discos SSD/NVMe).*

---

## 2. Requerimientos de Hardware (Impacto por Endpoints)
Al incorporar telemetría de cientos o miles de Endpoints (logs de Windows, Sysmon, EDR), el consumo de memoria e indexación se dispara. 

| Componente | Requerimiento Base | Requerimiento con Endpoints | Notas |
| :--- | :--- | :--- | :--- |
| **CPU** | 4 Cores | **8 a 16 Cores** | Mayor necesidad de procesamiento para ingesta de Logstash. |
| **Memoria RAM** | 24 GB | **64 GB a 128 GB+** | Elasticsearch consumirá agresivamente RAM para indexar los logs de los endpoints. |
| **Almacenamiento** | 200 GB | **1 TB a 5 TB+** | Requisito obligatorio: **Discos SSD/NVMe**. Los discos mecánicos (HDD) colapsarán por el IOPS. |
| **Tarjetas de Red**| 2 Interfaces | 2 Interfaces | NIC 1 (Management) y NIC 2 (Sniffing SPAN). |

---

## 3. Reglas de Firewall Perimetral e Interno

### 3.1. Tráfico Saliente a Internet (TCP/443)
Salida HTTPS para descargar contenedores, actualizaciones y firmas (Emerging Threats, Snort, Elastic GeoIP). 
*Dominios requeridos:* `github.com`, `ghcr.io`, `securityonion.net`, `emergingthreatspro.com`, `elastic.co`.

### 3.2. Tráfico Interno (LAN hacia el Servidor SOC)
Como ahora se desplegarán agentes en las computadoras/servidores de la empresa, **el firewall interno debe permitir que todos los endpoints corporativos (Windows/Linux/Mac) alcancen la IP de Management del servidor Standalone**.

| Origen | Destino | Puertos TCP Permitidos | Uso (Elastic Agent) |
| :--- | :--- | :--- | :--- |
| **Redes de Endpoints (LAN/VPN)** | **IP Management SOC** | `443`, `5055`, `8220`, `8443` | Descarga de binarios del agente, políticas de administración y envío masivo de logs hacia Logstash/Elasticsearch. |

> [!CAUTION]
> **Aislamiento de Red:** Asegurarse de que los puertos 5055, 8220 y 8443 **solo** sean accesibles desde las redes internas corporativas o VPNs, nunca exponerlos directamente a internet.

---

## 4. Guía y Pasos de Instalación
1. Descargar la ISO de [Github Releases](https://github.com/Security-Onion-Solutions/securityonion/releases).
2. Bootear y correr el instalador.
3. Al reiniciar, ejecutar `sudo so-setup` y elegir la opción **Standalone**.
4. Configurar IP de Management y seleccionar la interfaz de Monitoreo/SPAN.
5. **(Fase Endpoints):** Una vez finalizada la instalación, el equipo SOC generará los instaladores del Elastic Agent desde la consola web para que Infraestructura/Mesa de Ayuda los despliegue en los equipos de usuario vía GPO, SCCM o Intune.
