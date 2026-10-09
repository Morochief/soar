# Sean: Keep your cool during a data breach

## Mantén la Calma (*Keep your cool*)
Hola, mi nombre es Sean. Soy Gerente Técnico de Programas (*Technical Program Manager*) en Google Workspace. Soy un veterano de la ciberseguridad con 30 años de experiencia en el espacio corporativo a través de seis industrias diferentes.

> [!NOTE]
> Durante tu primera brecha de datos (*data breach*), lo más importante que puedes hacer es **mantener la calma** (*keep your cool*). 

Cuando ocurre un incidente, todos a tu alrededor (gerentes, empleados, directores) se van a volver locos de pánico. Si estás en el equipo de seguridad y estás gestionando el incidente, tienes que ser, legítimamente, la persona más tranquila en la habitación. Sé esa persona que pone la pausa racional en la conversación. Alguien podría gritarte: *"¿Acaso sabes lo que está pasando?"*. Y tú responderás calmadamente: *"Absolutamente sí"*.

## Un Caso Real de Brecha de Datos por Hardware
Creo que la brecha de datos más grande que he tenido comenzó con una simple llamada telefónica. 

Un ingeniero de otra institución financiera compró un servidor usado en eBay. Al conectar y encender ese servidor, descubrió que los discos duros no habían sido formateados ni borrados (*wiped*). **Había veinte millones de registros de tarjetas de crédito en ese servidor en venta al público**. 

Ese evento desencadenó una auditoría y revisión completa: descubrimos que, como estábamos subcontratando centros de datos, no estábamos controlando cómo actuaban nuestros proveedores. Nos dimos cuenta de que no teníamos políticas escritas sobre cómo esos terceros debían borrar criptográficamente o destruir físicamente los servidores y discos que ya no usábamos.

## Prioridad Número Uno: Contener la Brecha
La primera acción que siempre vas a tomar durante un incidente es **contener la brecha** (*contain the breach*). 

> [!IMPORTANT]
> Si tu red todavía está "sangrando" o hemorragiando datos (los *hackers* los están extrayendo activamente), debes seguir tus protocolos progresivos para detener esa fuga de inmediato. Si eso significa apagar un servidor, apagar un centro de datos entero, o cortar la conexión a internet de la empresa, lo haces sin dudarlo. **Detener la pérdida de datos es tu prioridad número uno, no reparar la red ni investigar al culpable.**

Tu trabajo formal como gerente de incidentes (*incident manager*), o como analista de seguridad trabajando en una brecha en progreso, es **primero detener la brecha (Contención) y luego investigar la brecha (Análisis)**.

Por lo tanto, no improvises bajo fuego: **ejecutar la gestión de incidentes siguiendo un plan preestablecido** es la lección técnica más valiosa que un analista *entry-level* puede grabar en su mente.

## Puntos Clave (Key Takeaways)
- La habilidad blanda más importante durante un incidente crítico es **mantener la calma**. El equipo de seguridad SOC es la ancla racional de la empresa.
- Ante un ataque en progreso, **tu prioridad absoluta número uno es la Contención**. Debes aislar y detener la fuga de datos primero (desconectando cables de red, apagando servidores o bloqueando puertos), antes de intentar investigar quién los atacó.
- Un analista SOC nunca improvisa en una crisis; siempre **ejecuta el plan de respuesta a incidentes** (*Incident Response Plan* / *Playbooks*).
- Desechar hardware informático sin aplicar un borrado seguro (*wiping* / *sanitization*) o destrucción física a los discos duros, representa un riesgo crítico de fuga masiva de datos corporativos (SPII).
