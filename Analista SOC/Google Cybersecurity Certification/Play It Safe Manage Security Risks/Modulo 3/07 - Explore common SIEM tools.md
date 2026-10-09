# Explore common SIEM tools

¡Hola de nuevo! En sesiones anteriores, analizamos cómo las herramientas SIEM ayudan a los analistas de seguridad a monitorear sistemas y detectar amenazas de seguridad. En este video, cubriremos algunas de las herramientas SIEM líderes en la industria que con alta probabilidad encontrarás en tu trayectoria profesional como analista de seguridad.

---

## Tipos de Implementación de Herramientas SIEM

Antes de profundizar en las marcas del mercado, es fundamental discutir los diferentes tipos de arquitecturas SIEM que las organizaciones pueden elegir según sus necesidades únicas de seguridad y presupuesto:

### 1. SIEM Alojado Localmente (*Self-hosted SIEM*)
Estas herramientas requieren que las organizaciones instalen, operen y mantengan la aplicación utilizando su propia infraestructura física, como su propia capacidad de servidores locales. 
*   **Gestión Interna:** Estas aplicaciones son gestionadas y mantenidas directamente por el departamento de IT de la propia organización, en lugar de un proveedor externo o tercerizado (*third-party vendor*).
*   **Caso de Uso Ideal:** Son ideales cuando una organización está obligada por regulaciones estrictas a mantener el control físico absoluto sobre sus datos confidenciales.

### 2. SIEM Alojado en la Nube (*Cloud-hosted SIEM*)
A diferencia del modelo local, estas herramientas son mantenidas y gestionadas por los propios proveedores de la solución SIEM, volviéndose accesibles de forma segura a través de Internet.
*   **Caso de Uso Ideal:** Es la opción perfecta para organizaciones que no desean invertir capital ni tiempo en la creación, administración y mantenimiento de su propia infraestructura física.

### 3. Solución Híbrida (*Hybrid SIEM*)
Una organización puede optar por utilizar una combinación integrada de herramientas SIEM tanto alojadas localmente (*self-hosted*) como en la nube (*cloud-hosted*).
*   **Caso de Uso Ideal:** Las empresas eligen soluciones híbridas para aprovechar los beneficios masivos de flexibilidad de la nube mientras conservan el control físico e interno sobre ciertos repositorios de datos altamente confidenciales.

---

## Herramientas SIEM Líderes en la Industria

Plataformas como **Splunk Enterprise**, **Splunk Cloud** y **Google Chronicle** son herramientas SIEM comunes que muchas organizaciones utilizan hoy en día para proteger sus datos y sistemas críticos.

### Ecosistema Splunk
Splunk es, en su base, una plataforma avanzada de análisis de datos, y su línea de productos proporciona soluciones SIEM robustas:
*   **Splunk Enterprise:** Es una herramienta de tipo autohospedada (*self-hosted*) que se utiliza para retener, analizar y buscar en los datos de registros (*logs*) de la organización, proveyendo información de seguridad y alertas automatizadas en tiempo real.
*   **Splunk Cloud:** Es una herramienta alojada en la nube (*cloud-hosted*) que se utiliza para recopilar, buscar y monitorear datos de registros. Es de extrema utilidad para empresas que operan en entornos híbridos o exclusivamente en la nube (*cloud-only*), donde una parte o la totalidad de los servicios corporativos residen en internet.

### Google Chronicle
Chronicle es la apuesta de Google para la analítica de seguridad a hiperescala:
*   **Nativo de la Nube (*Cloud-native*):** Chronicle es una herramienta diseñada desde cero para retener, analizar y realizar búsquedas masivas de datos. Ofrece funciones integradas de monitoreo de *logs*, análisis de datos y recolección de telemetría.

> [!IMPORTANT]
> **Diferencia Técnica Clave:** Al igual que las herramientas alojadas en la nube (*cloud-hosted*), las herramientas nativas de la nube (*cloud-native*) son mantenidas y gestionadas por el proveedor externo. Sin embargo, las soluciones *cloud-native* están específicamente diseñadas arquitectónicamente para **aprovechar al máximo todas las capacidades de la computación en la nube**, tales como la alta disponibilidad instantánea, la flexibilidad elástica y la escalabilidad masiva ante peticiones de datos volumétricos.

---

## La Importancia de la Diversidad de Herramientas

Debido a que los actores de amenazas (*threat actors*) mejoran y sofistican frecuentemente sus estrategias para comprometer la Confidencialidad, Integridad y Disponibilidad (**tríada CIA**) de sus objetivos, es de vital importancia que las organizaciones utilicen una variedad diversificada de herramientas de seguridad para defenderse contra los ataques.

Las soluciones SIEM que acabamos de discutir son solo algunos ejemplos del abanico de herramientas disponibles para los equipos de seguridad SOC. Más adelante en este programa de certificación, tendrás la emocionante oportunidad práctica de utilizar tanto **Splunk Cloud** como **Google Chronicle** en entornos de laboratorio para cazar incidentes simulados.

---

## Puntos Clave (Key Takeaways)

*   **Arquitecturas SIEM:** Las empresas eligen su modelo SIEM (*self-hosted*, *cloud-hosted* o *hybrid*) basándose en el balance entre el control físico de sus datos confidenciales y los costos de infraestructura informática.
*   **Splunk Enterprise vs. Cloud:** Splunk Enterprise ofrece una solución robusta local para búsquedas en tiempo real, mientras que Splunk Cloud facilita la gestión de *logs* en infraestructuras híbridas o *cloud-only*.
*   **Poder Cloud-Native:** Google Chronicle representa la evolución *cloud-native*, aprovechando de forma nativa la escalabilidad, la flexibilidad y la alta disponibilidad de la nube para analizar peticiones masivas de datos de seguridad.
*   **Defensa Diversificada:** Ante la constante evolución de las tácticas de los atacantes para vulnerar la tríada CIA, las organizaciones deben desplegar múltiples capas defensivas integrando herramientas SIEM optimizadas.
