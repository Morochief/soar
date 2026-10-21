# 🖥️ FICHA TÉCNICA: CONSOLA WEB NATIVA `so-soc`, `so-sensoroni` Y `so-nginx`

> **Componente:** Frontend, Interfaz de Analista, Grid Management y Reverse Proxy Seguro  
> **Servicios SO3:** `so-soc`, `so-sensoroni`, `so-nginx`  
> **Repositorio Local Upstream:** `G:\Hermes + Antigravity\sensoroni-docs` y `securityonion-docs`  
> **Puertos de Red:** `443/TCP` (HTTPS Público de Acceso al SOC), `80/TCP` (Redirección HTTP a HTTPS)  
> **Ubicación en SO3:** `/opt/so/conf/soc/`, `/opt/so/conf/nginx/` y `/opt/so/saltstack/salt/`  

---

## 1. Identificación y Propósito en Security Onion

* **Proyectos Base:**
  * **`so-nginx`:** Servidor HTTP y reverse proxy endurecido (TLS 1.2/1.3, CSP estricto).
  * **`so-soc`:** La interfaz de usuario principal de Security Onion (reemplazo moderno de Sguil/Squert de versiones antiguas).
  * **`so-sensoroni`:** Daemon en Go para gestión remota de comandos, interrogación de sensores y control de estado del clúster (Grid).
* **Propósito:**
  * Es la **única puerta de entrada web** para los analistas de seguridad.
  * Agrupa en una experiencia centralizada:
    1. **Alerts:** Vista unificada de incidentes generados por Suricata, Wazuh y ElastAlert.
    2. **Hunt:** Motor de búsqueda interactivo sobre Elasticsearch/OpenSearch.
    3. **PCAP:** Extracción de paquetes en formato `.pcap` en un clic conectándose a Stenographer.
    4. **Cases:** Sistema de seguimiento de tickets e investigación forense.
    5. **Administration / Grid:** Vista de hardware y salud de todos los nodos gestionados por SaltStack.

---

## 2. Comandos Operativos y Diagnóstico

```bash
# Verificar estado de los servicios web:
sudo so-soc-status
sudo so-nginx-status

# Inspeccionar logs de acceso web o errores de proxy:
sudo docker logs --tail 50 -f so-nginx
sudo docker logs --tail 50 -f so-soc

# Reiniciar la interfaz web:
sudo so-soc-restart
sudo so-nginx-restart
```
