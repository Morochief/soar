# Guía de Migración y Despliegue: Security Onion 3

**Objetivo:** Proporcionar al departamento de Cómputo/Infraestructura los requerimientos exactos para desplegar la nueva plataforma Security Onion 3 en arquitectura **Standalone** (Todo en uno), enfocada en análisis de red.

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
> *Nota: Los requerimientos de hardware a continuación solo aplican en caso de que Cómputo decida, de forma opcional, aprovechar la ventana de mantenimiento para montar el sistema en un hardware más robusto.*

---

## 2. Requerimientos de Hardware
Para una arquitectura **Standalone** (Management, Base de Datos, Motor de Búsqueda y Sensor de Red integrados en el mismo equipo), se exigen los siguientes recursos base:

| Componente | Requerimiento Mínimo | Notas |
| :--- | :--- | :--- |
| **CPU** | 4 Cores (x86-64) | *No se soportan arquitecturas ARM.* |
| **Memoria RAM** | 24 GB | *Elasticsearch y Logstash consumen RAM intensivamente.* |
| **Almacenamiento** | 200 GB | *Recomendado SSD/NVMe. Considerar más espacio según la retención de logs deseada (PCAP).* |
| **Tarjetas de Red (NICs)** | 2 Interfaces | - **NIC 1 (Management):** Con IP fija, salida a internet y acceso para analistas.<br>- **NIC 2 (Sniffing):** Conectada al puerto SPAN/Mirror del Switch (Sin IP asignada). |

---

## 3. Reglas de Firewall Perimetral
El nodo Standalone requiere salida a Internet para descargar actualizaciones, contenedores y firmas de amenazas (Snort/Emerging Threats). 

Se debe habilitar tráfico **Saliente (Outbound) TCP/443 (HTTPS)** desde la IP de *Management* hacia los siguientes dominios:
- `raw.githubusercontent.com` *(Llave pública de Security Onion)*
- `sigs.securityonion.net` *(Firmas de contenedores)*
- `ghcr.io` y `pkg-containers.githubusercontent.com` *(Descarga de contenedores)*
- `rules.emergingthreatspro.com` y `rules.emergingthreats.net` *(Firmas IDS)*
- `github.com` y `objects.githubusercontent.com` *(Actualizaciones de reglas Sigma/Strelka)*
- `repo.securityonion.net`, `repo-alt.securityonion.net`, `so-repo-east.s3.us-east-005.backblazeb2.com` *(Repositorios base)*
- `geoip.elastic.co` y `storage.googleapis.com` *(Actualización de bases de datos de geolocalización)*
- `www.snort.org` *(Firmas de Snort/Talos)*

> [!NOTE]
> **Tráfico Entrante (Inbound):** Al ser Standalone y no utilizar agentes de endpoint en esta fase, Cómputo solo debe permitir el acceso entrante por **TCP/443 (HTTPS)** y **TCP/22 (SSH)** desde la VLAN o VPN de los Analistas SOC hacia la IP de *Management*.

---

## 4. Guía y Pasos de Instalación

### Fase 1: Descarga e Instalación del SO Base
1. Descargar la imagen ISO oficial más reciente desde Github: [Security Onion 3 Releases](https://github.com/Security-Onion-Solutions/securityonion/releases)
2. Bootear la ISO en la Máquina Virtual/Servidor físico.
3. Seguir el instalador basado en texto (similar a la instalación de CentOS/Oracle Linux).

### Fase 2: Configuración de Red (Setup inicial)
1. Al reiniciar, el sistema solicitará iniciar sesión con el usuario creado durante la instalación.
2. Ejecutar el asistente de configuración si no se inicia automáticamente (o escribir `sudo so-setup`).
3. Seleccionar el tipo de despliegue: **Standalone**.
4. Configurar las interfaces de red:
   - **Management Interface:** Asignar IP Estática, Subred, Gateway y DNS.
   - **Monitor/Sniffing Interface:** Seleccionar la segunda tarjeta de red que recibirá el tráfico SPAN.
5. Crear la cuenta de administrador para la Consola Web (SOC).

### Fase 3: Post-Instalación
1. Una vez que el asistente (Salt) termine de levantar todos los contenedores (puede tardar de 15 a 30 minutos dependiendo del hardware), Cómputo deberá notificar al equipo SOC.
2. El equipo SOC ingresará vía navegador web a `https://<IP_DE_MANAGEMENT>` utilizando las credenciales de administrador para comenzar con la personalización de reglas y umbrales.

---

## 5. Referencias Oficiales
- [Documentación Oficial de Security Onion 3](https://docs.securityonion.net/en/2.4/introduction.html)
- [Guía de Hardware](https://docs.securityonion.net/en/2.4/hardware.html)
- [Requerimientos de Firewall](https://docs.securityonion.net/en/2.4/firewall.html)
