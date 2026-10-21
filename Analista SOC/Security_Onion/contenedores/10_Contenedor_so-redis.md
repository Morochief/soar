# ⚡ FICHA TÉCNICA: BROKER Y BUFFER EN MEMORIA `so-redis`

> **Componente:** Cola intermedia de mensajes en memoria y buffer anti-desbordes  
> **Servicio SO3:** `so-redis`  
> **Repositorio Local Upstream:** `G:\Hermes + Antigravity\redis-doc`  
> **Puerto de Red:** `6379/TCP` (Localhost / Red Docker)  
> **Ubicación en SO3:** `/opt/so/conf/redis/` y `/opt/so/saltstack/salt/redis/`  

---

## 1. Identificación y Propósito en Security Onion

* **Proyecto Base Upstream:** [redis/redis](https://github.com/redis/redis) *(Documentación clonada en `redis-doc`)*.
* **Propósito en SO3:**
  * **Amortiguador de choque (Buffer / Shock Absorber):** En momentos de tormentas de tráfico en la red (escaneos masivos, ataques DDoS, picos de navegación laboral), los sensores generan millones de eventos por segundo que Logstash y Elasticsearch no pueden procesar instantáneamente en disco.
  * `so-filebeat` lee los logs de Zeek y Suricata y los inserta inmediatamente en una lista en memoria en Redis (`LPUSH`).
  * `so-logstash` consume continuamente de esa lista en memoria a su propio ritmo (`RPOP`).
  * **Si Elasticsearch o Logstash se reinician o caen temporalmente, ningún log se pierde**, porque quedan encolados en la memoria RAM de Redis.

---

## 2. Diagnóstico Rápido y Métricas de Ingesta

### A. Verificar si hay atasco en la cola de ingestión (Queue Length):
```bash
# Consultar cuántos eventos están acumulados esperando a ser procesados por Logstash:
sudo docker exec -it so-redis redis-cli llen logstash:beats
```
* **Veredicto del SOC:**
  * `0 a 10,000`: **Normal**. Logstash procesa al ritmo que entra el tráfico.
  * `> 100,000`: **Alerta de congestión**. Logstash está teniendo problemas para parsear o Elasticsearch está bloqueado.

### B. Estadísticas de Memoria de Redis:
```bash
sudo docker exec -it so-redis redis-cli info memory
```

### C. Reiniciar servicio:
```bash
sudo so-redis-restart
```
