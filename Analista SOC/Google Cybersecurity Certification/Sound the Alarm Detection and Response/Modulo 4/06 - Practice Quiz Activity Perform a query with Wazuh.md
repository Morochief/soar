# Practice Quiz: Activity: Perform a query with Wazuh

**1. How many events are contained in the buttercup-games* index across all time?**
*   100 - 1,000
*   **Over 100,000**
*   10000
*   10 - 99

> **Justificación:** Según el Paso 4 de la actividad, al realizar la primera búsqueda con el comodín `*` desde el año 2000, los resultados arrojan más de 100,000 eventos ingeridos.

***

**2. Which field identifies the name of a network device or system from which an event originates?**
*   **host**
*   index
*   sourcetype
*   source

> **Justificación:** El campo `host` (o `host.keyword` en el dashboard de Wazuh) especifica el nombre del host o dispositivo de red desde donde se originó el evento (por ejemplo, `mailsv`, `www1`).

***

**3. Which of the following hosts used by Buttercup Games contains log information relevant to financial transactions?**
*   www2
*   www3
*   www1
*   **vendor_sales**

> **Justificación:** Según el Paso 5, el host `vendor_sales` es el que contiene la información sobre las ventas minoristas (retail sales) y transacciones de Buttercup Games.

***

**4. How many failed SSH logins are there for the root account on the mail server?**
*   100
*   One
*   None
*   **More than 100**

> **Justificación:** Al realizar la búsqueda `host.keyword: mailsv AND (fail* OR failed) AND root` en el Paso 7, el sistema devuelve más de 300 eventos de intentos fallidos, lo que encaja con la opción "More than 100".
