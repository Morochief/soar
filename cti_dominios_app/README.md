# 🛡️ CTI & Domain Risk Analyzer (Command Center GUI)

Aplicación local e independiente con **Interfaz Gráfica Web** para ejecutar el pipeline de Threat Intelligence de Dominios y cálculo de Score de Riesgo (1–100), sin depender de que la instancia de n8n esté activa.

---

## 🚀 Cómo iniciar la aplicación

Solo tienes que hacer **doble clic** en:
📂 `iniciar_gui.bat`

O por terminal:
```powershell
cd soar\cti_dominios_app
python app.py
```

Se abrirá automáticamente en tu navegador predeterminado en `http://127.0.0.1:5050`.

---

## ✨ Características de la Interfaz

1. **Barra de Estado de APIs:**
   * Muestra en tiempo real con puntos verdes si tus claves de **Shodan**, **AbuseIPDB**, **GreyNoise**, **Abuse.ch** y **MXToolbox** están cargadas desde `soar/.env`.
2. **Caja de Entrada Inteligente:**
   * Permite pegar múltiples empresas u organismos (uno por línea).
   * Soporta **dominios directos** (`bcp.gov.py`, `technoma.com.py`, etc.).
   * Genera **acrónimos automáticos** (ej: *Banco Central del Paraguay* -> *BCP*).
   * Explora TLDs regionales y gubernamentales (`.gov.py`, `.gob.py`, `.com.py`, etc.).
   * Fallback dual de DNS (`www.` para portales gubernamentales).
3. **Métricas en Vivo:**
   * Contadores ejecutivos: Total procesadas, Dominios analizados, Riesgo Crítico, Alto, Medio y Bajo.
4. **Tabla de Resultados y Libro Mayor:**
   * Enlaces directos a las URLs.
   * Badges de colores por nivel de score (1–100).
   * Badges azules con las normas ISO detectadas en la web (ISO 27001, 9001, etc.).
   * Acordeón interactivo **"Ver desglose"** para auditar punto por punto el aporte de cada plataforma.
5. **Exportación Integrada:**
   * Botón para **Descargar JSON** con exactamente la misma estructura que genera n8n.
   * Botón para **Descargar Workflow de n8n** (`workflow_n8n_listo_para_importar.json`).

---

## 🔄 Compatibilidad con n8n

Cuando tu servicio de n8n vuelva a estar en línea:
* El archivo `workflow_n8n_listo_para_importar.json` contiene los **41 nodos limpios** (sin Brave, con resolución `www.` y soporte de acrónimos).
* Solo tienes que abrir n8n ➔ **Import from File** ➔ seleccionar ese archivo.
* No tienes que reprogramar ni ajustar nada: los dos proyectos usan exactamente las mismas fórmulas y pesos.
