# 🛡️ Technoma SOC — OpenXDR Master Cockpit & Forensic Suite

Suite gráfica y orquestador SOAR/CTI para analistas del Centro de Operaciones de Seguridad (SOC), diseñado para interactuar con **Stellar Cyber OpenXDR**, **Palo Alto Cortex XDR**, **FortiGate**, motores de CTI (VirusTotal, AbuseIPDB, URLScan, NVD) y copilotaje forense asistido por modelos de lenguaje (NVIDIA NIM / Gemini).

---

## 🚀 Componentes Principales

| Módulo / Herramienta | Archivo Principal | Descripción |
| :--- | :--- | :--- |
| **OpenXDR Cockpit Principal** | `command_center.py` | Panel central de mando: gestión de casos, supervisión de sensores, ingesta de pozo, correlación con EDR y disparador de acciones SOAR. |
| **Copiloto IA Forense** | `soc_agent_gui.py` | Asistente forense en tiempo real con pre-extracción de contexto local, dictamen en 4 fases, justificación para consola y fila TSV de 18 columnas. |
| **Generador de Reportes de Abuso** | `abuse_report_dialog.py` | Parser de volcados JSON de Interflow/Syslog para generación y despacho de notificaciones a Abuse Desks con control de duplicados. |
| **Módulo CTI & Feeds de Amenazas** | `feeds_intel_module.py` | Sincronizador de IOCs diarios, análisis de CVEs/KEV de CISA y generación de reportes de inteligencia. |
| **Generador Oficial de Tickets** | `thn_ticket_generator.py` | Formulario oficial FL-THN-POS-01 para reporte de incidentes y generación de expedientes PDF. |
| **Analizador de Cabeceras de Correo** | `email_header_analyzer.py` | Triaje forense de ataques de Phishing, validación de SPF/DKIM/DMARC y bypass de CDN. |

---

## 📦 Requisitos Previos

* **Python 3.10** o superior instalado en el sistema.
* Acceso a API de Stellar Cyber y claves de CTI / IA (opcionales según módulo).

---

## ⚙️ Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### 2. Crear y activar un entorno virtual aislado
En Windows:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

En Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Copia la plantilla de ejemplo y edita tus claves:
```bash
copy .env.example .env     # En Windows
cp .env.example .env       # En Linux
```

Edita `.env` con las credenciales necesarias (`STELLAR_HOST`, `STELLAR_TOKEN`, `NVIDIA_API_KEY`, etc.).

---

## 🖥️ Ejecución

* **Cockpit Completo:** `python command_center.py` o doble clic en `Lanzar_Cockpit_GUI.bat`.
* **Copiloto IA Forense:** `python soc_agent_gui.py` o doble clic en `Iniciar_SOC_Agent_GUI.bat`.
* **Reportes de Abuso:** `python abuse_report_dialog.py` o doble clic en `Lanzar_Reporte_Abuso.bat`.

---

## 🔒 Buenas Prácticas de Seguridad
* **Nunca subir el archivo `.env`** al repositorio ni a servicios en la nube.
* **Nunca subir exportaciones de tickets o volcados con datos confidenciales de clientes** (`*.tsv`, `*.csv`).
* Mantener `.gitignore` actualizado para preservar el aislamiento del entorno virtual (`venv`).
