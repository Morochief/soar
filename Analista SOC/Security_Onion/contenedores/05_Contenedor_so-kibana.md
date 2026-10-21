# 📊 FICHA TÉCNICA: VISUALIZACIÓN Y ANÁLISIS `so-kibana`

> **Componente:** Plataforma de Visualización, Dashboards y Exploración Analítica (Elastic Stack)  
> **Servicio SO3:** `so-kibana`  
> **Repositorio Local Upstream de Documentación:** `G:\Hermes + Antigravity\elastic-docs-content` (Secciones `explore-analyze/discover/`, `explore-analyze/dashboards/`, `api/kibana/`)  
> **Puerto de Red:** `5601/TCP` (HTTP / Reverse Proxy Nginx)  
> **Ubicación en SO3:** `/opt/so/conf/kibana/` y `/opt/so/saltstack/salt/kibana/`  

---

## 1. Identificación y Propósito en Security Onion

* **Proyecto Base Upstream:** [elastic/kibana](https://github.com/elastic/kibana) *(Documentación oficial centralizada en `elastic-docs-content`)*.
* **Propósito en SO3:**
  * Es la **interfaz clásica y avanzada de exploración de datos** sobre Elasticsearch.
  * Mientras que la consola nativa `so-soc` está orientada a flujos específicos de analistas (Alerts, Hunt, PCAP y Grid Management), **Kibana ofrece libertad total para crear visualizaciones ad-hoc, gráficos de series temporales, diagramas Sankey de tráfico y paneles ejecutivos**.
  * Viene preconfigurado con dashboards nativos de Security Onion para Suricata, Zeek (DNS, HTTP, SSL, SSH), Wazuh, Syslog de Firewalls y estado de sensores.

---

## 2. Flujo de Arquitectura y Acceso en SO3

En SO3, Kibana no está expuesto directamente al público por el puerto `5601`. Se encuentra protegido detrás de la capa de autenticación y proxy inverso:

```mermaid
flowchart LR
    subgraph Usuario ["Analista SOC"]
        BROWSER["Navegador Web (HTTPS :443)"]
    end

    subgraph PerimetroManager ["Nodo Manager SO3"]
        NGINX["so-nginx / Reverse Proxy (:443)"]
        AUTH["Autenticación SO3 (OAuth2 / Session)"]
        KIB["so-kibana (:5601)"]
        ES["so-elasticsearch (:9200)"]
    end

    BROWSER -->|https://manager-ip/kibana| NGINX
    NGINX --> AUTH
    AUTH -->|Tráfico Proxy Autenticado| KIB
    KIB -->|Consultas REST Query DSL| ES
    ES -->> KIB: Documentos e Índices
    KIB -->> BROWSER: Dashboards y Gráficos Renderizados
```

---

## 3. Módulos Clave de Kibana Utilizados por el SOC

Los manuales de `elastic-docs-content` cubren las 4 herramientas esenciales de Kibana en SO3:

1. **Discover (`explore-analyze/discover/`):**
   * Vista forense cruda en tiempo real.
   * Permite filtrar usando **KQL (Kibana Query Language)** o sintaxis Lucene.
   * Ejemplo de búsqueda rápida KQL para investigar una IP:
     ```kql
     source.ip: "192.168.169.143" or destination.ip: "192.168.169.143"
     ```
2. **Dashboard (`explore-analyze/dashboards/`):**
   * Agrupa visualizaciones múltiples en una sola pantalla:
     * *Zeek Hunting Dashboard:* Mapas de calor de DNS, transferencias de archivos sospechosas.
     * *Suricata Alerts Dashboard:* Top firmas por severidad y países de origen.
3. **Visualize Library / Lens:**
   * Constructor gráfico para crear diagramas de barras, tortas, métricas y tablas agregadas por campos ECS (`event.dataset`, `network.transport`, `http.response.status_code`).
4. **Dev Tools / Console:**
   * Consola interactiva para enviar comandos REST directos contra Elasticsearch sin necesidad de usar `curl` desde la terminal:
     ```json
     GET _cat/indices?v
     GET so-*/_search
     {
       "size": 10,
       "query": { "match": { "event.module": "suricata" } }
     }
     ```

---

## 4. Orquestación con SaltStack (`.sls`)

En SO3, SaltStack aprovisiona el contenedor de Kibana, inyecta los certificados TLS y carga automáticamente los **Saved Objects** (dashboards prefabricados de Security Onion) en el índice `.kibana`.

### Ubicación del State: `/opt/so/saltstack/salt/kibana/init.sls`
```yaml
so-kibana:
  docker_container.running:
    - image: {{ salt['pillar.get']('docker:registry', 'localhost:5000') }}/securityonionsolutions/so-kibana:latest
    - restart_policy: always
    - network_mode: host
    - environment:
      - ELASTICSEARCH_HOSTS: "http://127.0.0.1:9200"
      - SERVER_HOST: "127.0.0.1"
      - SERVER_PORT: "5601"
      - SERVER_BASEPATH: "/kibana"
      - SERVER_REWRITERESUBNAME: "false"
    - binds:
      - /opt/so/conf/kibana/kibana.yml:/usr/share/kibana/config/kibana.yml:ro
      - /opt/so/log/kibana:/usr/share/kibana/data:rw
```

---

## 5. Diagnóstico y Comandos de Administración

### A. Verificar estado del contenedor:
```bash
# Ver estado en Docker
sudo docker ps --filter "name=so-kibana"

# Ver estado en el CLI de Security Onion
sudo so-kibana-status
```

### B. Inspeccionar logs de arranque y conexión:
```bash
sudo docker logs --tail 100 -f so-kibana
```
*(Indica si Kibana está esperando a que Elasticsearch pase a estado `YELLOW`/`GREEN` o si hay errores en el índice `.kibana`).*

### C. Recargar Dashboards por defecto de Security Onion:
Si se borran o corrompen los dashboards predefinidos del SOC:
```bash
sudo so-kibana-load
```

### D. Reiniciar servicio:
```bash
sudo so-kibana-restart
```

---

## 6. Puntos Críticos y Resolución de Problemas

1. **Error `Kibana server is not ready yet`:**
   * **Causa más frecuente:** Elasticsearch está caído, en estado `RED`, o la memoria JVM está saturada por un GC (Garbage Collection) largo.
   * **Solución:** Comprobar primero la salud de Elasticsearch:
     ```bash
     curl -s http://localhost:9200/_cluster/health | jq .
     ```
2. **Índice `.kibana` Bloqueado en Solo Lectura:**
   * Si el disco supera el 95% (*Flood-Stage Watermark*), Kibana no permitirá guardar nuevas visualizaciones ni editar dashboards. Se debe liberar espacio en `/nsm` y desbloquear los índices con la API de settings.
