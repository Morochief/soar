# Lectura: Categorías y Tipos de Controles de Seguridad (Control Categories)

Dentro del ámbito de la ciberseguridad, las salvaguardas que implementamos para proteger los activos no son homogéneas; se dividen en estructuras organizadas según su naturaleza y su función operativa. En esta lectura de los expertos de Google, analizaremos en profundidad las categorías y los tipos de controles de seguridad que utilizarás día a día como analista para construir una estrategia sólida de defensa en profundidad (*defense in depth*).

---

## 1. Categorías Principales de Controles

Los controles de ciberseguridad se agrupan en tres categorías fundamentales según el ecosistema sobre el cual actúan:

### Controles Administrativos o Gerenciales (*Administrative/Managerial controls*)
Abordan directamente el **componente humano** de la ciberseguridad. Estos controles incluyen las políticas, directrices y procedimientos formales que definen cómo una organización gestiona sus datos y delimitan con claridad las responsabilidades de los empleados para la protección de la empresa. Aunque son de base política, su cumplimiento y ejecución efectiva a menudo requieren apoyarse en controles técnicos o físicos.

### Controles Técnicos (*Technical controls*)
Consisten en soluciones lógicas basadas en hardware y software para proteger los activos de información. Son herramientas automatizadas esenciales para que los analistas detecten, bloqueen y mitiguen actividades anómalas en la infraestructura digital. Los ejemplos clave incluyen *firewalls*, sistemas de detección de intrusos (**IDS**), sistemas de prevención de intrusos (**IPS**), herramientas *antivirus* (**AV**) y mecanismos de cifrado (*encryption*).

### Controles Físicos u Operacionales (*Physical/Operational controls*)
Son medidas tangibles implementadas para limitar el acceso físico directo a los activos protegidos por parte de personal no autorizado. Salvaguardan el entorno de hardware crítico y abarcan elementos como cerraduras de puertas, candados en gabinetes, cámaras de videovigilancia y lectores de tarjetas de identificación (*badge readers*).

---

## 2. Tipos de Controles según su Función

Independientemente de su categoría, los controles se clasifican según el momento y el objetivo con el que actúan frente a un incidente de seguridad:

> [!NOTE]
> *   **Preventivos (*Preventative*):** Diseñados proactivamente para evitar que ocurra un incidente de seguridad en primera instancia.
> *   **Correctivos (*Corrective*):** Utilizados de forma reactiva para restaurar, reparar o recuperar un activo después de que ha ocurrido un incidente.
> *   **Detectivos (*Detective*):** Implementados de manera continua para identificar si un incidente de seguridad ha ocurrido o se encuentra actualmente en curso.
> *   **Disuasorios (*Deterrent*):** Diseñados específicamente para desalentar, intimidar o persuadir a los atacantes, incrementando la dificultad percibida del ataque.

---

## 3. Tablas Detalladas de Controles

### Controles Administrativos o Gerenciales
| Nombre del Control | Tipo de Control | Propósito del Control |
| :--- | :--- | :--- |
| **Menor Privilegio** (*Least Privilege*) | Preventivo | Reducir el riesgo y el impacto general de un atacante interno malicioso o de cuentas comprometidas. |
| **Planes de Recuperación ante Desastres** (*Disaster recovery plans*) | Correctivo | Garantizar y proporcionar la continuidad del negocio (*business continuity*) ante fallas críticas. |
| **Políticas de Contraseñas** (*Password policies*) | Preventivo | Reducir la probabilidad de compromiso de cuentas mediante técnicas de ataque de fuerza bruta o de diccionario. |
| **Políticas de Control de Acceso** (*Access control policies*) | Preventivo | Reforzar la confidencialidad e integridad definiendo qué grupos o roles específicos pueden acceder o modificar datos. |
| **Políticas de Gestión de Cuentas** (*Account management*) | Preventivo | Gestionar el ciclo de vida de las cuentas, reducir la superficie de ataque y limitar el impacto general de ex-empleados descontentos o el uso de cuentas por defecto. |
| **Separación de Funciones** (*Separation of duties*) | Preventivo | Reducir el riesgo y el impacto operativo derivado de fraudes internos o abusos de privilegios. |

### Controles Técnicos
| Nombre del Control | Tipo de Control | Propósito del Control |
| :--- | :--- | :--- |
| **Firewall** | Preventivo | Filtrar el tráfico no deseado o malicioso para evitar que penetre en la red interna de la organización. |
| **IDS / IPS** | Detectivo | Detectar y prevenir tráfico anómalo o malicioso que coincida con una firma técnica o una regla de seguridad. |
| **Cifrado** (*Encryption*) | Disuasorio | Proveer confidencialidad estricta a la información sensible, volviéndola ilegible para terceros no autorizados. |
| **Copias de Seguridad** (*Backups*) | Correctivo | Restaurar y recuperar los datos y sistemas operativos esenciales después de un evento disruptivo. |
| **Gestión de Contraseñas** (*Password management*) | Preventivo | Reducir la fatiga de contraseñas de los usuarios y promover el uso de credenciales robustas y únicas. |
| **Software Antivirus (AV)** | Preventivo | Escanear los sistemas para detectar, aislar y poner en cuarentena amenazas y *malware* conocidos. |
| **Monitoreo Manual e Intervención** | Preventivo | Necesario para identificar y gestionar de forma humana las amenazas, riesgos o vulnerabilidades en sistemas heredados u obsoletos. |

### Controles Físicos u Operacionales
| Nombre del Control | Tipo de Control | Propósito del Control |
| :--- | :--- | :--- |
| **Caja Fuerte con Control de Tiempo** | Disuasorio | Reducir la superficie de ataque física y mitigar el impacto general de robos o amenazas materiales directas. |
| **Iluminación Adecuada** | Disuasorio | Disuadir amenazas físicas externas al limitar y eliminar las zonas ocultas o "escondites". |
| **Televisión de Circuito Cerrado (CCTV)** | Preventivo / Detectivo | Su presencia disuade y reduce el riesgo de intrusiones corporativas, y su grabación aporta análisis forense posterior para informar sobre las condiciones del evento. |
| **Gabinetes bajo Llave (para redes)** | Preventivo | Reforzar la integridad de la infraestructura de red impidiendo que personal no autorizado altere o manipule físicamente los *switches*, *routers* o cableado. |
| **Señalización de Proveedor de Alarma** | Disuasorio | Desalentar intrusiones físicas al hacer que las probabilidades de éxito de un ataque parezcan sumamente bajas. |
| **Cerraduras / Candados** (*Locks*) | Disuasorio / Preventivo | Robustecer la integridad y seguridad perimetral al bloquear el paso físico a áreas restringidas y activos críticos. |
| **Detección y Prevención de Incendios** | Detectivo / Preventivo | Detectar la presencia de fuego o humo en tiempo real dentro de las instalaciones y activar sistemas de mitigación (aspersores) para evitar la pérdida de servidores o inventario. |

---

## Puntos Clave (Key Takeaways)

*   **Defensa en Profundidad:** Las tres categorías de controles (Administrativos, Técnicos y Físicos) deben entrelazarse de forma armónica para crear capas defensivas que un actor de amenazas no pueda vulnerar fácilmente.
*   **Gestión del Error Humano:** Los controles administrativos mitigan el riesgo en el eslabón más débil mediante políticas claras, pero su éxito real depende de la supervisión lógica o técnica de sus reglas.
*   **Automatización de Controles:** El despliegue de herramientas como IDS, *firewalls* y cifrado aporta a los analistas una capacidad operativa automatizada de prevención y detección veloz en la red.
*   **Línea del Tiempo del Incidente:** Clasificar los controles según su tipo (Preventivo, Detectivo, Correctivo y Disuasorio) permite a la organización saber con precisión si está invirtiendo recursos suficientes en prevenir ataques o si su estrategia está desbalanceada hacia la reacción post-incidente.
