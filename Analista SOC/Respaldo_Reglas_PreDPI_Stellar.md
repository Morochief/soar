# Respaldo de Reglas Pre-DPI - Sensor Profile: profile-modular-sensor-technoma

**Fecha de Respaldo:** 14 de Octubre de 2026  
**Analista:** Kevin Moraes  
**Sensor Afectado:** `technoma-sensor` (`192.168.15.70`)  
**Perfil:** `profile-modular-sensor-technoma`  
**Ubicación en UI:** `System | Data Source Management | Sensors | Sensor Profiles | profile-modular-sensor-technoma | Traffic Filtering | Pre-DPI Filters`  
**Acción Configurada:** `Drop`

---

## 1. Configuración Original Completa (15 Items de Respaldo)

Copiar y pegar estas líneas en caso de requerir restaurar el estado previo de las reglas del sensor:

```text
host 192.168.15.27
src host 10.2.1.3 and tcp 1500
src host 10.2.1.6 and tcp 1500
src host 10.2.1.4 and tcp 1500
dst 172.17.10.203
src net 172.17.10.0/24 and dst 10.11.1.1
src net 172.17.10.0/24 and dst 10.11.1.2
host 172.17.10.203
dst 192.168.15.27
dst port 10050
dst port 10051
src host 10.11.1.1 and dst host 10.11.1.2 and port 53
src host 10.11.1.2 and dst host 10.11.1.1 and port 53
src host 192.168.15.23 and dst port 53
src port 53 and dst host 192.168.15.23
```

---

## 2. Diagnóstico Técnico de Sintaxis (Por qué fallaba pcap_compile)

Conforme a la documentación oficial de `libpcap` (`pcap_compile(3PCAP)`) y la base de conocimiento de Stellar Cyber:
1. `pcap_compile()` evalúa de forma atómica la concatenación `OR` de todas las líneas.
2. Si una sola línea contiene un error léxico o de tipo (como `tcp 1500` en lugar de `tcp port 1500`, o `dst 172.17.10.203` sin especificar `host`), la función retorna `PCAP_ERROR (-1)`.
3. Al fallar la compilación, el daemon `aella_flow` descarta el filtro completo y opera en modo permisivo (*accept all packets*), permitiendo que todo el tráfico continúe ingresando a Interflow.

---

## 3. Configuración Mínima de Prueba (Aislamiento Quirúrgico Zabbix / Grafana)

Para aislar y comprobar si el motor Pre-DPI funciona sin interferencia de sintaxis ajena, la configuración debe tener **únicamente** las reglas bidireccionales del host Grafana:

```text
src host 192.168.15.23 and dst port 53
src port 53 and dst host 192.168.15.23
```
*(Total Items: 2)*

---

## 4. Versión Corregida de Todo el Conjunto (Por si se decide restaurar todo en limpio)

Si más adelante se quiere volver a cargar todo el conjunto histórico pero con la sintaxis 100% válida para evitar `PCAP_ERROR`:

```text
host 192.168.15.27
src host 10.2.1.3 and tcp port 1500
src host 10.2.1.6 and tcp port 1500
src host 10.2.1.4 and tcp port 1500
dst host 172.17.10.203
src net 172.17.10.0/24 and dst host 10.11.1.1
src net 172.17.10.0/24 and dst host 10.11.1.2
host 172.17.10.203
dst host 192.168.15.27
dst port 10050
dst port 10051
src host 10.11.1.1 and dst host 10.11.1.2 and port 53
src host 10.11.1.2 and dst host 10.11.1.1 and port 53
src host 192.168.15.23 and dst port 53
src port 53 and dst host 192.168.15.23
```
