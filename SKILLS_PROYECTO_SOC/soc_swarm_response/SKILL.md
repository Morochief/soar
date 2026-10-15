---
name: soc_swarm_response
description: Activa el protocolo de "Enjambre SOC". Genera múltiples subagentes en paralelo para investigar un IoC o un endpoint comprometido en Security Onion, Stellar Cyber y plataformas de Threat Intel simultáneamente.
---

# SOC Swarm Response (Protocolo de Enjambre)

## Contexto
Utiliza esta skill cuando el usuario esté investigando un incidente crítico, un IoC sospechoso (IP, dominio, hash) o un endpoint posiblemente comprometido, y necesite recolectar inteligencia y logs de múltiples plataformas lo más rápido posible sin perder el foco en la respuesta.

## Flujo de Trabajo del Enjambre

Cuando se active esta skill, DEBES utilizar la herramienta `invoke_subagent` para lanzar inmediatamente los siguientes subagentes en paralelo. 

### 1. Subagente 1 (Security Onion Hunter)
* **Role:** Security Onion Hunter
* **TypeName:** research
* **Prompt Sugerido:** "Busca en el historial de Security Onion (utilizando scripts locales de hunting como `so_hunter.py`) cualquier rastro, conexión o log de red relacionado con el IoC. Entrega un resumen de los flujos de tráfico y el timeline de actividad."

### 2. Subagente 2 (Threat Intel Analyst)
* **Role:** Threat Intel Analyst
* **TypeName:** research
* **Prompt Sugerido:** "Investiga la reputación, malware asociado y reportes previos del IoC. Utiliza herramientas como `otx_fetcher.py` para AlienVault OTX o realiza búsquedas web profundas. Resume la campaña maliciosa asociada."

### 3. Subagente 3 (Stellar Cyber / SIEM Analyst)
* **Role:** SIEM Analyst
* **TypeName:** research
* **Prompt Sugerido:** "Busca alertas L7, eventos anómalos o correlaciones del IoC en Stellar Cyber (usando scripts como `stellar_hunter.py` u otra API disponible). Reporta cualquier detección avanzada de IA."

## Reglas para el Agente Principal (Tú)
1. **No bloquees el hilo:** Tras invocar a los subagentes, informa al usuario inmediatamente que el *Enjambre SOC* ha sido desplegado y que están trabajando en segundo plano.
2. **Foco en Contención:** Mientras los subagentes buscan data, tú debes guiar al analista humano en las tareas críticas (aislamiento del host en Cortex XDR, bloqueos de IP en el FortiGate).
3. **Síntesis Ejecutiva:** Cuando los subagentes comiencen a enviarte sus reportes por mensaje, consolida los hallazgos. No le tires el texto crudo al usuario; armá un "Reporte de Enjambre" que cruce los datos de red (SO) con la inteligencia (OTX) y las alertas (Stellar).
