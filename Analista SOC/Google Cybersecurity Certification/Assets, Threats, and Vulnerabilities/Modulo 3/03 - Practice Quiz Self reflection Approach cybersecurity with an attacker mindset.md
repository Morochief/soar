# Practice Quiz: Self-reflection: Approach cybersecurity with an attacker mindset

## Resumen de la Actividad
Ahora que has sido introducido a las **superficies de ataque** (*attack surfaces*) y los **vectores de ataque** (*attack vectors*), puedes hacer una pausa y pensar en lo que estás aprendiendo. En esta auto-reflexión, pensarás cómo estos factores pueden ayudar a identificar amenazas y responder a preguntas breves.

> [!NOTE]
> **Repaso de la mentalidad de un atacante**
> Anteriormente, aprendiste que aplicar la mentalidad de un atacante a cualquier situación comienza preguntándote: *"¿Cómo explotaría yo este vector?"* Esto requerirá que consideres dos elementos:
> 1.  **Superficie de ataque:** Incluye todas las vulnerabilidades potenciales que un actor de amenazas podría explotar. (El "qué" es atacable).
> 2.  **Vector de ataque:** Es la vía, camino o método que un atacante utiliza para penetrar las defensas de seguridad de una superficie de ataque. (El "cómo" entra el atacante).
> 
> El proceso paso a paso es: Identificar un objetivo -> Determinar cómo se puede acceder a él -> Evaluar los vectores de ataque explotables -> Encontrar las herramientas y métodos de ataque.

---

## Reflexión

**1. Considera lo que revisaste sobre la aplicación de una mentalidad de atacante en relación a asegurar el entorno de tu hogar:**
*   *¿Cuáles son las superficies de ataque de un hogar? ¿Son físicas o digitales? ¿Cuáles son sus vulnerabilidades? ¿Están actualmente expuestas a riesgos?*
*   *Ahora, escribe de 2 a 3 oraciones que describan características importantes sobre las superficies de ataque de tu hogar.*

**Ejemplo de Respuesta (Nivel Analista SOC):**
Las superficies de ataque de mi hogar son tanto físicas como digitales. Físicamente, incluyen puertas, ventanas y el buzón de correo, cuyas vulnerabilidades podrían ser cerraduras débiles o falta de vigilancia. Digitalmente, la superficie de ataque abarca mi router Wi-Fi, cámaras de seguridad IoT y altavoces inteligentes, los cuales están expuestos a riesgos reales de botnets si mantienen contraseñas predeterminadas de fábrica o si su *firmware* está desactualizado.
*(The attack surfaces of my home are both physical and digital. Physically, they include doors, windows, and mailboxes, whose vulnerabilities could be weak locks or lack of surveillance. Digitally, the attack surface includes my Wi-Fi router, IoT security cameras, and smart speakers, which are exposed to real botnet risks if they use default passwords or if their firmware is outdated.)*

---

**2. A continuación, considera cómo un atacante podría explotar las vulnerabilidades de esa superficie.**
*   *¿Cuáles son los vectores de ataque de esta superficie? ¿Hay múltiples puntos de entrada? ¿Cómo podrían explotarse las vulnerabilidades? ¿Qué defensas existen? ¿Se pueden agregar nuevas defensas?*
*   *Ahora, escribe de 3 a 5 oraciones que expliquen cuáles son esos vectores de ataque y cómo puedes aplicar las estrategias que has aprendido para proteger tu hogar.*

**Ejemplo de Respuesta (Nivel Analista SOC):**
Los vectores de ataque físicos podrían incluir forzar el cerrojo de una puerta o interceptar correspondencia bancaria en el buzón. Digitalmente, los vectores de entrada incluyen ataques de fuerza bruta contra la contraseña del Wi-Fi, o el escaneo y explotación de puertos abiertos en dispositivos IoT vulnerables. Mis defensas actuales incluyen alarmas físicas y cifrado WPA3 en la red inalámbrica. Para reducir los vectores de ataque, aplicaré el principio de defensa en profundidad segmentando mi red (aislando los dispositivos IoT en una red de "Invitados"), desactivando la administración remota (UPnP/WPS) en el router, y adoptando gestores de contraseñas para asegurar que cada dispositivo tenga una clave única y robusta.
*(Physical attack vectors could include picking a door lock or intercepting bank mail. Digitally, entry vectors include brute-force attacks against the Wi-Fi password, or scanning and exploiting open ports on vulnerable IoT devices. My current defenses include physical alarms and WPA3 encryption on the wireless network. To reduce attack vectors, I will apply the principle of defense in depth by segmenting my network (isolating IoT devices on a Guest network), disabling remote administration (UPnP/WPS) on the router, and adopting password managers to ensure every device has a unique, strong password.)*
