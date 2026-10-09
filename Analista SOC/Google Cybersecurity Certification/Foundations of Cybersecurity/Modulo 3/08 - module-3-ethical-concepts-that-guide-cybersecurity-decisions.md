# Lectura: Ethical concepts that guide cybersecurity decisions

Anteriormente introdujimos el concepto básico de ética en seguridad. Ser ético requiere que los profesionales se mantengan imparciales y defiendan la confidencialidad de los datos privados de los clientes. Tener una brújula moral fuerte te ayudará a navegar escenarios grises en tu día a día en el SOC. 

En esta lectura, aprenderás más conceptos esenciales para tomar decisiones apropiadas sobre cómo responder **legalmente** a los ciberataques.

## La Trampa del "Hack Back" (Contraataques)

### Punto de vista de Estados Unidos (y mayoría de países occidentales)
En EE. UU., lanzar un contraataque cibernético (*hackear de vuelta*) al atacante que acaba de vulnerar tu red es **100% ilegal**. Viola regulaciones federales masivas como la Ley de Abuso y Fraude Informático (CFAA).

En el sector corporativo, **tu trabajo es puramente defender**. 
El acto de contraatacar se percibe legalmente como un acto de *vigilantismo* (justicia por mano propia). Y debido a que los cibercriminales suelen triangular sus ataques robando servidores vulnerables de otros países (ej. el servidor del atacante podría ser en realidad el servidor secuestrado de un hospital pediátrico), tu contraataque podría destruir infraestructura inocente y escalar el daño catastróficamente. 

Peor aún, si el actor de amenazas es patrocinado por un Estado-Nación enemigo, un contraataque lanzado por una corporación privada puede provocar un incidente diplomático internacional. Por estas razones, las únicas entidades autorizadas para ejecutar ciberataques ofensivos (*Hack Backs*) son unidades militares específicas de ciberguerra gubernamental.

### Punto de vista internacional
La Corte Internacional de Justicia (CIJ) establece teóricamente que un grupo podría contraatacar si se cumplen utopías técnicas como:
- Que el contraataque garantice afectar pura y exclusivamente al atacante inicial (imposible de probar en ciberseguridad).
- Que los efectos del ataque puedan revertirse.

En la vida real, las organizaciones nunca contraatacan porque los daños colaterales son imposibles de controlar y los resultados legales son devastadores para el Analista de Seguridad involucrado.

## Principios Éticos Diarios del Analista

Debido a que la venganza (los contraataques) está descartada legalmente, la industria ha creado marcos defensivos preventivos como la Tríada CIA para abordar estos problemas. 

- **Confidencialidad Ética:** Implica un nivel de respeto absoluto por los activos privados. Significa que, aunque poseas credenciales de Administrador Global, éticamente te prohíbes a ti mismo acceder a datos a menos que sea estrictamente necesario para resolver una alerta técnica.
- **Protección de la Privacidad (PII y SPII):** Debes conocer la diferencia. La **PII** (Información de Identificación Personal) es información general (Nombre, Dirección, Teléfono). La **SPII** (PII Sensible) son los datos críticos que requieren controles encriptados muchísimo más estrictos, como los Números de Seguro Social, cuentas bancarias y datos biométricos.
- **Respeto a las Leyes:** Como analista manejando incidentes, estás obligado a ser imparcial, transparente y basarte estrictamente en **evidencia forense (logs)**, nunca en intuiciones. Si descubres que los servidores fueron vulnerados, por ejemplo, bajo la ley HIPAA tienes la obligación ética y legal de impulsar a la gerencia a notificar rápidamente a los pacientes sobre el robo de sus datos de salud (PHI).

---

## Puntos Clave (Key Takeaways)
- El **Hack Back** (contraatacar al enemigo que hackeó tu red corporativa) está estrictamente prohibido por la ley y es causa de despido y juicio penal para el analista y la corporación. Tu rol es Defender y Aislar la amenaza.
- El nivel de protección técnica y ética aumenta cuando la empresa almacena **SPII** (datos críticos financieros o de identidad), comparado con la PII general.
- La toma de decisiones en un incidente de seguridad (Responder, Aislar, Reportar) debe estar guiada por *Frameworks* establecidos (como NIST) para protegerte de la responsabilidad legal.
