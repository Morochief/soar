# Resumen Ejecutivo: Capacitación Check Point – Estrategia y Portafolio

## 1. Estrategia Comercial y Nuevo Modelo de Negocio (MSSP)
El mensaje central de la capacitación es que Check Point dejó de ser solo una "caja de hardware de $70,000 dólares" para convertirse en un ecosistema flexible y altamente competitivo.
*   **Modelo de Servicio a la Medida (MSSP):** Para mercados sensibles al precio (Bolivia, Paraguay, Uruguay), Check Point introdujo un modelo donde el partner (nosotros) se vuelve la marca. Usamos un Tenant Maestro (MCP) para habilitar "Tenants Hijos" a los clientes. El precio base arranca desde $20,000 USD cobrados como servicio. 
*   **PoC (Prueba de Concepto) Agresiva:** Se habilita un escaneo gratis de 15 días de la *Superficie de Ataque Externa*. Como detecta 3 a 4 veces más brechas reales (fugas de datos) que la competencia, la venta del servicio gestionado (MDR/SOC) se cierra sola.
*   **Operativa en el Portal de Partners:** Toda cotización nace en *PartnerMAP*. Es crítico hacer el *Deal Registration* para proteger el negocio y garantizar los márgenes de descuento. Al cerrar la venta, se genera un *Activation Token* que libera las licencias en la nube (Infinity Portal).

## 2. Gestión del Riesgo Externo (Cyberint) y Validaciones Reales
Check Point no es un NDR (Network Detection), sino una plataforma proactiva impulsada por la compra de **Cyberint**.
*   **Superando a FortiRecon:** No escanean simplemente puertos. Tienen *Agentic Exposures* (Pentesting continuo y automatizado). Si el sistema reporta exposiciones, es porque las atacó y confirmó que son explotables, eliminando las suposiciones y los falsos positivos de la competencia.
*   **Intelligence Data Leak & Takedown:** Revisan la Deep/Dark web en tiempo real (Raw Intelligence) buscando credenciales robadas y código filtrado. Además, incluyen el proceso legal y automatizado de **Takedown** para tirar abajo páginas falsas (phishing) o apps clonadas en cuestión de horas.
*   **BAS vs Pentesting:** Posicionan su tecnología de simulación de ataques (BAS) como una evaluación constante 24/7 de las defensas (para ver si el firewall o EDR reaccionan bien), complementando el clásico pentesting anual hecho por humanos.

## 3. Consolidación de la Fuerza de Trabajo (SASE, EDR, Mobile, Email)
Check Point busca que reemplacemos toda la "fragmentación" de otras marcas por una sola suite consolidada en la nube:
*   **Harmony SASE (Ex Perimeter 81):** Tras la compra de Perimeter 81 por $490M, reemplazan las viejas VPNs por una red global ultrarrápida. Combina SD-WAN con Zero Trust (ZTNA), permitiendo despliegues en minutos, logrando una conexión a las apps internas sin latencia y apoyándose en Proveedores de Identidad (IdP como Entra ID/Okta).
*   **Harmony Email (Ex Avanan):** El principal golpe contra Microsoft y Cisco (IronPort). Mientras Cisco requiere desviar el correo y fragmentar licencias, Check Point usa un modelo *Inline por API*. El correo se frena y analiza con IA *antes* de llegar a la bandeja del usuario en Office 365.
*   **Harmony Endpoint y Mobile:** El EDR de Check Point no solo reacciona, es *Prevention-First*. Tiene análisis forense automático y "Rollback" contra Ransomware (restaura archivos cifrados sin pagar rescate). *Harmony Mobile* protege dispositivos corporativos y BYOD contra redes públicas maliciosas y robo de credenciales vía SMS/WhatsApp.

## 4. IA Security y Seguridad de Aplicaciones (WAF)
La Inteligencia Artificial es el pilar central del futuro de Check Point, dividida en cómo protegen las apps y cómo facilitan la gestión.
*   **WAF de Software (CloudGuard y open-appsec):** Se burlaron del modelo de Radware (que cobra licencias dobles por firmas y capacidad). El WAF de Check Point usa IA, no requiere calibración manual y es ideal para Kubernetes y aplicaciones web modernas, reduciendo falsos positivos al mínimo.
*   **Workforce AI Security:** Licenciamiento por usuario para controlar lo que los empleados hacen en ChatGPT o Gemini, evitando la fuga de datos (DLP) al bloquear *copiar y pegar* información confidencial en prompts de IA.
*   **MCP Servers:** La joya de la automatización. Check Point liberó servidores *Model Context Protocol* que actúan como traductores. Permiten que cualquier asistente de IA administre firewalls y redes en la nube pidiéndoselo en lenguaje natural, reduciendo drásticamente los tiempos operativos.

## 5. El Negocio del Soporte y las Certificaciones
La capacitación dejó claro que nuestro nivel técnico impacta directamente en la rentabilidad de los negocios que cerremos:
*   **Soporte Directo vs. Colaborativo:** Si no tenemos ingenieros capacitados, el cliente le compra el *Soporte Directo* a Check Point (más caro y nosotros no participamos de la posventa). Si calificamos, vendemos *Soporte Colaborativo*; nosotros damos el Nivel 1 y 2, obtenemos un costo bajísimo de fábrica, le agregamos nuestro margen y blindamos la relación con el cliente.
*   **CCSA y CCSE:** Para acceder a ese Soporte Colaborativo y subir de nivel de Partner (para más descuentos), Check Point nos exige tener ingenieros certificados en **CCSA** (Administración) y **CCSE** (Expertos en Troubleshooting). Es imperativo invertir en la certificación del equipo para maximizar la rentabilidad.

***
> **Resumen Comercial (El 'Elevator Pitch'):**
> "La oportunidad más grande que vimos es empaquetar la tecnología de Check Point como un Servicio Gestionado (MSSP) utilizando las Pruebas de Concepto gratis de Cyberint para demostrarle al cliente vulnerabilidades y fugas de datos reales que la competencia (como Fortinet) no detecta, rompiendo la barrera de precio inicial al cobrarlo como suscripción operativa."
