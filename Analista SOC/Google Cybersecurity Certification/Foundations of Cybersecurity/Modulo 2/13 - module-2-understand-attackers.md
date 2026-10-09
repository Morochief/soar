# Lectura: Understand attackers

Anteriormente, introdujimos el concepto de actores de amenazas (*threat actors*). Como recordatorio, un actor de amenazas es cualquier persona, grupo o nación que presenta un riesgo de ciberseguridad. En esta lectura, clasificaremos los diferentes tipos de atacantes según sus habilidades, sus motivaciones e intenciones.

## Tipos de Actores de Amenazas

### 1. Amenazas Persistentes Avanzadas (*APTs - Advanced Persistent Threats*)
Las APT son el nivel más alto de cibercriminales. Tienen un presupuesto masivo y una experiencia técnica extremadamente sofisticada (a menudo patrocinados por gobiernos o naciones-estado). Las APT investigan a sus objetivos (corporaciones mundiales o ministerios gubernamentales) durante meses con anticipación y **logran permanecer ocultos dentro de la red enemiga durante años** sin ser detectados. Sus motivaciones incluyen:
- Destruir infraestructura crítica nacional, como redes eléctricas (SCADA), agua o recursos naturales.
- Espionaje corporativo o gubernamental para robar secretos comerciales y militares.

### 2. Amenazas Internas (*Insider threats*)
El atacante ya está adentro. Las amenazas internas son empleados, contratistas o ex-empleados que **abusan de su acceso legal y autorizado** a la red para robar datos o dañar a la organización. Sus motivaciones incluyen:
- Sabotaje (por ejemplo, un administrador de TI despedido que borra los servidores por venganza).
- Corrupción o sobornos de empresas rivales.
- Fugas deliberadas de datos confidenciales.

### 3. Hacktivistas (*Hacktivists*)
Los hacktivistas son actores de amenazas impulsados puramente por una **agenda política o ideológica**. Abusan de la tecnología no para robar dinero, sino para lograr impacto mediático mediante:
- Manifestaciones digitales (como ataques de Denegación de Servicio - DDoS).
- Desfigurar páginas web gubernamentales (*Defacement*) para dejar propaganda.
- Exponer información clasificada que consideran de interés público.

---

## Tipos de Hackers según su Ética (Los "Sombreros")

Históricamente, la industria clasifica la ética de un hacker usando la analogía de los sombreros del viejo oeste:

- **Hackers autorizados (Sombrero Blanco / *White Hats*):** También llamados hackers éticos. Firman contratos legales (NDA) y siguen un código de ética para hackear a su propia empresa con el fin de encontrar debilidades antes de que los criminales lo hagan (*Pentesting*).
- **Hackers semi-autorizados (Sombrero Gris / *Gray Hats*):** Actúan en una zona gris legal. Hackean empresas sin pedir permiso para buscar vulnerabilidades por pura curiosidad o para reportarlas, pero no roban ni destruyen nada.
- **Hackers no autorizados (Sombrero Negro / *Black Hats*):** Son criminales maliciosos sin ética. Hackean sistemas ilegalmente con el único objetivo de destruir, robar datos y obtener ganancias financieras millonarias (ej. operadores de *Ransomware*).

### Otros perfiles en el ecosistema

- **Script Kiddies (Atacantes novatos):** Son individuos sin habilidades técnicas profundas. En lugar de escribir su propio código, descargan *malware* y herramientas ya pre-hechas por otros (*scripts*) para explotar debilidades, generalmente solo por diversión o vandalismo.
- **Mercenarios / Hackers a sueldo:** No tienen una bandera ideológica. Trabajan para el mejor postor, realizando tanto tareas legales como ilegales puramente por dinero.
- **Vigilantes:** Hackers que atacan a los criminales cibernéticos para "hacer justicia" por mano propia (hackeando de vuelta a los servidores de un cartel de *ransomware*, por ejemplo).

## Puntos Clave (Key Takeaways)
- Un analista SOC debe perfilar a su enemigo. Saber si estás lidiando con un **Script Kiddie** o con una **APT** cambia completamente el plan de Respuesta a Incidentes de la corporación.
- **APT:** Equipos altamente entrenados, patrocinados por el Estado, que buscan persistencia sigilosa a largo plazo, no dinero rápido.
- **Insider Threat:** El riesgo más difícil de detectar, porque el atacante utiliza credenciales legítimas (ej: un empleado resentido).
