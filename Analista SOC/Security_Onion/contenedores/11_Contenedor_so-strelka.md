# 🏹 FICHA TÉCNICA: SUITE DE ANÁLISIS DE ARCHIVOS Y MALWARE STRELKA

> **Componente:** Plataforma de extracción profunda de archivos en tiempo real (Threat Hunting / CTI)  
> **Servicios SO3:** `so-strelka-backend`, `so-strelka-coordinator`, `so-strelka-filestream`, `so-strelka-frontend`, `so-strelka-gatekeeper`, `so-strelka-manager`  
> **Repositorio Local Upstream:** `G:\Hermes + Antigravity\strelka-docs` (Target Corporation)  
> **Ubicación en SO3:** `/opt/so/conf/strelka/` y `/opt/so/saltstack/salt/strelka/`  

---

## 1. Identificación y Rol Crítico en Security Onion

* **Proyecto Base Upstream:** [target/strelka](https://github.com/target/strelka).
* **¿Qué hace exactamente en SO3?:**
  * Es el **motor automatizado de inspección y análisis estático de archivos sospechosos** en tránsito por la red.
  * Cuando Zeek detecta que se descarga o transfiere un archivo ejecutable (`.exe`, `.dll`), documento con macros (`.docx`, `.xlsm`), script (`.ps1`, `.bat`, `.vbs`) o archivo comprimido (`.zip`, `.iso`), Zeek extrae la carga útil a disco.
  * **Strelka toma ese archivo y le aplica docenas de escáneres en paralelo:**
    * Extracción de metadatos OLE y macros VBA sospechosas en documentos Office.
    * Descompresión recursiva de archivos ZIP/RAR/TAR/ISO para analizar lo que hay dentro.
    * Extracción de cadenas (**Strings**), hashes (MD5, SHA1, SHA256, SSDEEP, TLSH).
    * Búsqueda de firmas **YARA** para familias de malware conocidas y Ransomware.
    * Análisis de cabeceras PE (Portable Executable) de Windows para detectar empaquetadores (UPX), timestamps falsificados o compiladores sospechosos.
  * Los resultados se envían a Elasticsearch como eventos `so-strelka-*`, permitiendo buscar directamente en Kibana o en el SOC qué ejecutables o documentos entraron a la empresa.

---

## 2. Los 6 Contenedores de la Arquitectura Strelka en SO3

Security Onion despliega Strelka en microservicios contenerizados de alta escala:

| Contenedor SO3 | Función en el Pipeline de Análisis |
| :--- | :--- |
| **`so-strelka-filestream`** | Monitorea la carpeta de extracción de Zeek (`/nsm/zeek/extracted/`) y envía los nuevos archivos al pipeline. |
| **`so-strelka-gatekeeper`** | Validador de entrada y filtro previo: descarta archivos duplicados (por hash previo) o archivos demasiado grandes. |
| **`so-strelka-frontend`** | API de entrada gRPC que recibe las solicitudes de análisis y las encola. |
| **`so-strelka-coordinator`** | Orquestador de tareas basado en Redis / Celery que distribuye las tareas entre los workers. |
| **`so-strelka-backend`** | **El núcleo ejecutor:** Corre los plugins de análisis (YARA, OLE, PEfile, ExifTool, PDF, 7zip, etc.). |
| **`so-strelka-manager`** | Gestor de ciclo de vida del servicio y control de métricas. |

---

## 3. Diagnóstico y Comandos de Administración

```bash
# Ver estado de los 6 contenedores de Strelka:
sudo docker ps --filter "name=so-strelka"

# Estado nativo
sudo so-strelka-status

# Inspeccionar logs del backend (donde corren las reglas YARA y parsers):
sudo docker logs --tail 50 -f so-strelka-backend

# Reiniciar la suite Strelka completa:
sudo so-strelka-restart
```
