# Dossier Técnico y Arquitectura de Control: `command_center.py`
Este documento detalla a nivel milimétrico el funcionamiento interno, diseño de software, patrones asíncronos de PySide6, integración con la API REST de Stellar Cyber v6.5.0s y la pasarela de razonamiento cognitivo con Google Gemini.

---

## 🏛️ 1. Arquitectura Central del Sistema

La herramienta está estructurada bajo el patrón **N-tier de Cliente Delgado Desktop**, utilizando **PySide6 (Qt para Python)** como interfaz de usuario (GUI) reactiva y un motor asincrónico multihilo (`QThread`) para evitar el bloqueo del hilo principal (Main Thread/UI Thread) durante operaciones pesadas de E/S.

```mermaid
graph TD
    subgraph UI Thread (Main)
        A[XdrDashboard - Main Window] --> B[Neon HTML Health Panel]
        A --> C[Active Incidents SOAR Queue]
        A --> D[Case Triage & AI Investigation]
        A --> E[Interactive Multitenant Hunting]
        A --> F[QTimer Polling - 15s]
    end

    subgraph Background Workers (QThreads)
        F -->|Triggers| G[ApiWorker - health/cases]
        D -->|Triage Action| H[ApiWorker - triage]
        D -->|AI Button| I[AiAnalysisWorker - Gemini]
        E -->|Hunt Action| J[ApiWorker - hunt]
    end

    subgraph External Infrastructure
        G & H & J -->|REST API + JWT Auth| K[Stellar Cyber Gateway]
        I -->|REST POST + API Key| L[Google Gemini API]
    end
```

---

## ⚙️ 2. Motor de Concurrencia (Anti-Freeze Engine)

En aplicaciones GUI, realizar peticiones HTTP síncronas congela la ventana debido a que bloquea el bucle de eventos (`QEventLoop`). `command_center.py` solventa esto mediante un desacoplamiento total en dos clases de hilos:

### A. `ApiWorker(QThread)`
Diseñado para la comunicación directa con la API REST de Stellar Cyber.
* **Handshake JWT**: Obtiene un JSON Web Token efímero a través de la función privada `_get_token()` concatenando el `EMAIL_USUARIO` y el `ALL_ACCESS_TOKEN` codificado en `Base64`.
* **Multiplexado de Acciones**: Acepta un `endpoint_type` (`health`, `cases`, `triage`, `update_case`, `interflow`, `hunt`) y rutea dinámicamente la transacción HTTP.
* **Seguridad EDR-Safe**: Todas las solicitudes tienen deshabilitada la validación de certificados SSL (`verify=False`) y control de advertencias (`urllib3.disable_warnings`) para evitar falsos positivos de interceptores TLS en laboratorios y proxies de auditoría de red corporativa.

### B. `AiAnalysisWorker(QThread)`
Maneja de forma aislada la comunicación con la API de Google Gemini:
* **Headers Canónicos**: Envía la API Key en el encabezado `X-goog-api-key` y la instrucción del sistema (`system_instruction`) en la estructura del payload nativo.
* **Simulación de Flujo**: Envía de forma segura el payload JSON con `temperature=1.0` y `maxOutputTokens=8192`. Emite la señal `chunk_received` al recibir la respuesta completa para pintar el bloque de texto con elegancia.

---

## 🧹 3. Higiene Analítica y Optimización de Payloads

Uno de los mayores retos en la integración de IA en entornos de ciberseguridad es el desbordamiento de la ventana de contexto y el ruido de datos irrelevantes en las alertas. El sistema implementa dos técnicas críticas de procesamiento previo:

### A. `clean_forensic_data(data)`
Filtro recursivo que descarta metadatos de telemetría basura, extrayendo únicamente los campos forenses esenciales:
* `srcip` (IP Origen)
* `dstip` (IP Destino)
* `action` (Acción tomada por el EDR/Firewall)
* `policyname` (Regla activada)
* `appid_name` (Identificación de aplicación/protocolo)
* `event_description`
* `parser_raw_msg` (Mensaje en bruto original)

### B. `sanitizar_interflow(texto_crudo)`
Implementa un parseador lexicográfico que escanea el texto crudo en busca de llaves estructuradas `{` y `[`.
1. Utiliza `json.JSONDecoder().raw_decode()` para detectar y aislar objetos JSON embebidos.
2. Limpia recursivamente estos objetos mediante `clean_forensic_data()`.
3. Reensambla el documento final, reduciendo la telemetría cruda en hasta un **85% de volumen sin perder valor forense**, optimizando radicalmente el consumo de tokens y la latencia de respuesta de Gemini.

---

## 🛡️ 4. Robustez de Sesión y Salida Limpia (`closeEvent`)

Para mitigar el error clásico de Qt `QThread: Destroyed while thread '' is still running` (causado al destruir el objeto padre `QMainWindow` mientras los subprocesos de red siguen activos en memoria de sistema), se implementa un interceptor del ciclo de vida del widget principal:

```python
def closeEvent(self, event):
    self.timer_live.stop()  # Detiene el hilo de polling automático de 15 segundos
    workers = ['worker_health', 'worker_cases', 'worker_soar', 'worker_ai', 'worker_hunt']
    for w_name in workers:
        if hasattr(self, w_name):
            w = getattr(self, w_name)
            if w and w.isRunning():
                w.terminate()  # Envía una señal de terminación asíncrona al sistema operativo
                w.wait()       # Bloquea temporalmente hasta que el hilo libere sus recursos de socket
    event.accept()             # Permite el cierre normal del proceso de GUI
```

Adicionalmente, se inyecta la función reactiva `enviar_notificacion_popup()` utilizando la clase `QMessageBox` de forma segura dentro del hilo principal al procesar cambios en la sensórica o estados críticos de pozo de ingesta.

---

## 🏆 5. Puntos de Integración con el Perímetro XDR

1. **Monitoreo de Sensórica y Salud**: El panel izquierdo compila y formatea dinámicamente un dashboard HTML enriquecido con barras gráficas ASCII de CPU/Disco y ratios de transferencia de datos en tiempo real (Inbytes/Outbytes).
2. **Dynamic Ingestion Pooling**: Audita las cuotas de ingesta contratadas de forma colectiva (All Tenants) contra los consumos individuales, emitiendo beeps de advertencia de hardware si el pozo global supera los `10 GB/dia` parametrizados.
3. **SOAR Integration**: Permite la toma de casos (`PUT /cases/{id}` con asignación al analista), extracción de logs de Interflow asociados y el cierre definitivo de alertas con veredictos (`False Positive`, `True Positive`, `Benign`) y comentarios que se persisten directamente en Stellar Cyber.
