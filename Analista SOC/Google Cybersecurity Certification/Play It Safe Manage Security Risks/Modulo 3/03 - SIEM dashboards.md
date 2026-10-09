# SIEM dashboards

Anteriormente, exploramos cómo se utilizan las herramientas SIEM para recopilar y analizar datos de *logs*. Sin embargo, esta es solo una de las muchas maneras en que estas plataformas se aprovechan en ciberseguridad. Las herramientas SIEM también se utilizan para crear cuadros de mando corporativos o *dashboards*.

En esta sesión, analizaremos cómo la representación visual de los datos acelera drásticamente la capacidad de detección y respuesta de un analista en un Centro de Operaciones de Seguridad (**SOC**).

---

## Introducción del Instructor

En esta clase, tu instructor de Google te presentará la importancia de los *dashboards* dentro de un SIEM. Aprenderás que contar con millones de líneas de registros no es suficiente si no se pueden visualizar de forma clara; los componentes gráficos transforman los datos puros en inteligencia de amenazas inmediata.

---

## El Concepto de un Dashboard: De lo Cotidiano a la Seguridad

Es muy probable que ya hayas interactuado con *dashboards* en aplicaciones de tu teléfono móvil u otros dispositivos cotidianos. Su función principal es presentar información detallada sobre tu cuenta o ubicación en un formato que sea sumamente fácil de entender a primera vista.

Un excelente ejemplo de esto son las aplicaciones del clima. Estas plataformas despliegan datos complejos como la temperatura, las precipitaciones, la velocidad del viento y el pronóstico extendido utilizando cuadros, gráficos y otros elementos visuales interactivos. Este formato tan visual facilita la identificación rápida de patrones y tendencias meteorológicas, permitiéndote estar preparado y planificar tu día en consecuencia.

> [!NOTE]
> De la misma manera en que las aplicaciones del clima ayudan a las personas a tomar decisiones rápidas e informadas basadas en datos lógicos, los **dashboards de SIEM** permiten a los analistas de seguridad acceder de forma veloz y sencilla a la información de ciberseguridad de su organización a través de tablas, diagramas y gráficos personalizados.

---

## Monitoreo de Amenazas en la Práctica (Caso de Estudio)

Para entender el valor real de un *dashboard*, imaginemos el siguiente escenario operativo: un analista de nivel inicial (*entry-level*) recibe una alerta en tiempo real sobre un intento de inicio de sesión sospechoso (*suspicious login attempt*). 

El analista accede de inmediato a su *dashboard* de SIEM para recopilar un contexto profundo sobre esta alerta y descubre los siguientes hallazgos críticos:
*   Se han registrado **500 intentos de inicio de sesión** en la cuenta de una empleada llamada Ymara en un lapso de tan solo cinco minutos.
*   Dichos intentos de inicio de sesión provienen de ubicaciones geográficas completamente inusuales y ajenas a la actividad normal de Ymara.
*   La actividad se está ejecutando fuera de sus horarios laborales habituales.

Al utilizar un *dashboard* interactivo, el analista de seguridad pudo revisar rápidamente representaciones visuales de la línea de tiempo de los accesos, la geolocalización de las IPs y el minuto exacto de la actividad. Esto le permitió correlacionar los eventos al instante y determinar con absoluta certeza que se trataba de una actividad sospechosa y un posible ataque de fuerza bruta en curso.

---

## Métricas y Personalización para Stakeholders

Además de proporcionar un resumen exhaustivo y centralizado de los datos relacionados con la ciberseguridad de la infraestructura, los *dashboards* de SIEM también proveen a las distintas partes interesadas (*stakeholders*) una variedad de indicadores técnicos denominados **métricas** (*metrics*).

> [!IMPORTANT]
> Las **métricas** (*metrics*) son atributos técnicos clave —tales como el tiempo de respuesta (*response time*), la disponibilidad (*availability*) y la tasa de fallas (*failure rate*)— que se utilizan de forma cuantitativa para evaluar el rendimiento general y la salud de una aplicación de software o un sistema.

Los *dashboards* de SIEM poseen una gran flexibilidad y pueden ser completamente personalizados (*customized*) para mostrar métricas específicas u otros flujos de datos que sean relevantes para los diferentes miembros de la organización. 

*   **Vista del Analista SOC:** Un analista puede configurar un panel orientado a monitorear las operaciones comerciales del día a día, visualizando elementos operativos como el volumen total de tráfico de red entrante y saliente.
*   **Vista Gerencial:** Los directores de seguridad o CISO pueden acceder a paneles macro que muestran el nivel de cumplimiento normativo (*compliance*) o la cantidad de incidentes mitigados con éxito en el mes.

El uso estratégico de estos paneles visuales consolida las capacidades del equipo técnico para ayudar a las organizaciones a mantener y robustecer su postura de seguridad (*security posture*).

---

## Puntos Clave (Key Takeaways)

*   **Visualización Efectiva:** Los *dashboards* de SIEM traducen grandes volúmenes de texto procedentes de los *logs* en representaciones gráficas (tablas, gráficos, diagramas) legibles a primera vista.
*   **Aceleración de Respuesta:** Permitir el análisis correlacionado de líneas de tiempo, geolocalizaciones y picos de tráfico empodera a los analistas para confirmar actividades sospechosas de forma veloz.
*   **Monitoreo mediante Métricas:** El seguimiento de variables técnicas clave como la tasa de fallas y la disponibilidad es vital para evaluar el rendimiento de las defensas informáticas.
*   **Sintonía a la Medida:** La capacidad de personalización (*customization*) de las herramientas SIEM garantiza que tanto los analistas operativos como los *stakeholders* ejecutivos reciban la telemetría precisa que sus roles demandan.
