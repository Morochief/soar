# Practice Quiz: Test your knowledge: Overview of intrusion detection systems (IDS)

**1. A security analyst uses a network protocol analyzer to capture HTTP traffic to analyze patterns. What type of data are they using?**
*   **Network telemetry**
*   False positive
*   Host-based
*   Signature-based

> **Justificación:** La telemetría de red (Network telemetry) consiste en datos capturados del tráfico de red, como capturas de paquetes HTTP, que se utilizan para el análisis de patrones.

***

**2. A security analyst creates a Suricata signature to identify and detect security threats based on the direction of network traffic. Which of the following rule options should they use?**
*   Message
*   Content
*   Rev
*   **Flow**

> **Justificación:** La opción `flow` dentro de las reglas de Suricata permite especificar la dirección del tráfico de red (por ejemplo, `to_server` o `from_server`).

***

**3. Which statement accurately describes the difference between a network-based intrusion detection system (NIDS) and a host-based intrusion detection system (HIDS)?**
*   A NIDS uses signature analysis to detect threats; a HIDS uses agents.
*   **A NIDS is installed on a network; a HIDS is installed on individual devices.**
*   A NIDS only detects known threats; a HIDS detects unknown threats.
*   A NIDS is installed on individual devices; a HIDS is installed on a network.

> **Justificación:** Un NIDS monitorea el tráfico de toda una red en puntos estratégicos, mientras que un HIDS se instala como un agente en dispositivos (hosts) individuales para monitorear su actividad interna.

***

**4. Fill in the blank: The _____ component of an IDS signature includes network traffic information.**
*   signature ID
*   rule options
*   **header**
*   action

> **Justificación:** El encabezado (*header*) de una firma IDS define la información del tráfico de red, incluyendo el protocolo, las direcciones IP de origen/destino, los puertos y la dirección del flujo.
