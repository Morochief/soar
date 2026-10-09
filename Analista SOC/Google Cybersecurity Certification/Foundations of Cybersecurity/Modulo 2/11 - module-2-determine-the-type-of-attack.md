# Lectura: Determine the type of attack

Anteriormente, aprendimos sobre los ocho dominios de seguridad de la certificación **CISSP** (*Certified Information Systems Security Professional*). Los dominios nos ayudan a comprender mejor cómo los deberes de un analista se organizan en categorías y a entender cómo la corporación maneja los riesgos. 

En esta lectura, clasificaremos los métodos de ataque según el dominio CISSP al que afectan principalmente.

## Clasificación de Tipos de Ataques

### Ataque de Contraseña (*Password attack*)
Un ataque de contraseña es un intento (ya sea automatizado o manual) de acceder a dispositivos, sistemas o bases de datos adivinando o descifrando las credenciales legítimas. Ejemplos comunes que veremos más adelante:
- **Fuerza bruta** (*Brute force*)
- **Tablas Rainbow** (*Rainbow table*)

> **Clasificación CISSP:** Los ataques de contraseñas caen principalmente bajo el dominio de **Seguridad de Redes y Comunicaciones**.

### Ataque de Ingeniería Social (*Social engineering attack*)
La ingeniería social es la manipulación que explota la psicología y el error humano (no el error del código) para obtener información privada. Ejemplos de esta categoría:
- *Phishing, Smishing, Vishing*
- *Spear phishing* y *Whaling*
- Fraude del CEO (*Business Email Compromise - BEC*)
- Ataques *Watering hole* y *USB baiting*

> **Clasificación CISSP:** Dado que involucran fallas en la educación de los empleados y en las políticas, estos ataques caen dentro del dominio de **Gestión de Riesgos y Seguridad** (*Security and Risk Management*).

### Ataque Físico (*Physical attack*)
Un ataque físico es un incidente de seguridad que afecta el entorno tangible, traspasando las barreras arquitectónicas de la empresa. Formas comunes de ataques físicos:
- Conexión de un **cable USB malicioso** modificado.
- Conexión de una unidad flash maliciosa (*Rubber Ducky*).
- Clonación de tarjetas magnéticas de acceso (*Card cloning and skimming*).

> **Clasificación CISSP:** Los ataques físicos comprometen hardware tangible, por lo que pertenecen al dominio de **Seguridad de Activos** (*Asset Security*).

### Inteligencia Artificial Adversaria (*Adversarial artificial intelligence*)
Es una técnica de última generación que manipula los algoritmos de Inteligencia Artificial (IA) y *Machine Learning* de las herramientas defensivas para engañarlas o usarlas en su contra, permitiendo ataques altamente eficientes e indetectables.

> **Clasificación CISSP:** Cae bajo los dominios de **Seguridad de Redes y Comunicaciones** y **Gestión de Identidad y Acceso** (*IAM*).

### Ataque a la Cadena de Suministro (*Supply-chain attack*)
Un ataque a la cadena de suministro no ataca a la corporación directamente. En su lugar, el cibercriminal **ataca a un proveedor externo más débil** (un tercero que fabrica un software o hardware que la corporación utiliza) e infecta el producto desde su origen. 
Cuando la corporación compra e instala el software legítimo del proveedor, se infecta automáticamente. Estos ataques son catastróficos porque infectan a miles de empresas a nivel mundial simultáneamente.

> **Clasificación CISSP:** Debido a su gigantesco alcance, impactan múltiples dominios simultáneamente: **Gestión de Riesgos**, **Arquitectura e Ingeniería**, y **Operaciones de Seguridad** (*SOC*).

### Ataque Criptográfico (*Cryptographic attack*)
Un ataque criptográfico busca romper los algoritmos matemáticos que aseguran y cifran las comunicaciones privadas entre un remitente y un destinatario. Formas avanzadas de ataques criptográficos:
- Ataque de Cumpleaños (*Birthday attack*)
- Ataque de Colisión (*Collision attack*)
- Ataque de Degradación (*Downgrade attack*)

> **Clasificación CISSP:** Al enfocarse en interceptar comunicaciones seguras, pertenecen al dominio de **Seguridad de Redes y Comunicaciones**.

---

## Puntos Clave (Key Takeaways)
- Clasificar los ciberataques dentro del marco **CISSP** permite al analista saber exactamente a qué área (*Dominio*) debe acudir para buscar soluciones y mitigar el riesgo de raíz.
- **NIST:** El Instituto Nacional de Estándares y Tecnología (*NIST*) de EE.UU. mantiene un glosario oficial exhaustivo que es considerado "la biblia" para buscar las definiciones oficiales de cualquier término técnico de ciberseguridad.
