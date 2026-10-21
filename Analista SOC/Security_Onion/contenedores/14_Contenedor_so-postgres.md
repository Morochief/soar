# 🐘 FICHA TÉCNICA: BASE DE DATOS ESTRUCTURADA `so-postgres`

> **Componente:** Base de Datos Relacional SQL (RDBMS) para Casos, Alertas, SOC UI y Backend  
> **Servicio SO3:** `so-postgres`  
> **Ubicación en SO3:** `/opt/so/conf/postgres/` y `/opt/so/saltstack/salt/postgres/`  
> **Directorio de Datos en Disco:** `/nsm/postgres/` o `/opt/so/conf/postgres/data/`  
> **Puerto de Red:** `5432/TCP` (Exclusivo para la red Docker interna / Localhost)  

---

## 1. Identificación y Rol Crítico en Security Onion

* **Proyecto Base Upstream:** [PostgreSQL](https://www.postgresql.org/) (`postgres:15-alpine` o `postgres:14-alpine`).
* **¿Por qué SO3 necesita PostgreSQL si ya tiene Elasticsearch?:**
  * **Elasticsearch** es un Data Lake diseñado para búsquedas rápidas sobre texto completo y análisis temporal masivo (millones de logs de red por segundo). **No es una base de datos relacional ACID.**
  * **`so-postgres` almacena el estado transaccional y la gestión operativa del SOC:**
    1. **Módulo de Casos (`so-cases`):** Historial de investigaciones, notas forenses, comentarios de analistas, evidencias adjuntas y estados de tickets.
    2. **Configuraciones de la UI (`so-soc`):** Preferencias de dashboards de los usuarios, configuraciones de visualización y filtros guardados.
    3. **Metadatos del Grid:** Registro de roles de nodos y estado administrativo.

---

## 2. Comandos Operativos y Diagnóstico

### A. Verificar estado del contenedor:
```bash
sudo docker ps --filter "name=so-postgres"
sudo so-postgres-status
```

### B. Probar conexión y salud de la base de datos:
```bash
# Ejecutar pg_isready dentro del contenedor
sudo docker exec -it so-postgres pg_isready -U postgres
```
*(Debe responder: `/var/run/postgresql:5432 - accepting connections`).*

### C. Inspeccionar logs de la base de datos:
```bash
sudo docker logs --tail 50 -f so-postgres
```

### D. Reiniciar base de datos:
```bash
sudo so-postgres-restart
```
