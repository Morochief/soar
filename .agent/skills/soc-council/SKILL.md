---
name: soc_council
description: "Invoca un concilio de múltiples subagentes de Antigravity (Red Team, Blue Team, Threat Intel) para debatir un falso positivo complejo, analizar un archivo o investigar un incidente de seguridad en paralelo."
---

# Skill: SOC Council (Debate de IAs)

Esta skill se activa cuando el usuario solicita "consultar al concilio", necesita una "segunda opinión" técnica, o si el análisis inicial presenta alta ambigüedad sobre si una alerta es maliciosa o un falso positivo.

## Mecanismo de Funcionamiento (Subagentes Nativos)
Antigravity no necesita APIs externas (OpenAI/Anthropic). Utiliza su propia capacidad nativa de invocar subagentes (threads independientes que corren en paralelo) usando la herramienta `define_subagent` e `invoke_subagent`.

### Paso 1: Definición de los Miembros del Concilio
Si no los has definido antes en la conversación, debes usar la herramienta `define_subagent` tres veces para crear a los expertos:

1. **Nombre:** `council_red_team`
   **System Prompt:** "Eres un atacante ético (Red Team) extremadamente paranoico. Tu trabajo es analizar la evidencia provista y buscar cualquier vector de ataque oculto, técnicas de ofuscación (Living off the Land), o explicar cómo un adversario real explotaría este escenario. Siempre asume compromiso."

2. **Nombre:** `council_blue_team`
   **System Prompt:** "Eres un ingeniero defensivo (Blue Team) y sysadmin. Tu trabajo es buscar razones legítimas por las cuales un sistema generaría estos logs. Te enfocas en falsos positivos, fallos de software, parches de SO y ruido de red administrativo. Siempre asume benignidad."

3. **Nombre:** `council_threat_intel`
   **System Prompt:** "Eres un analista de Inteligencia de Amenazas (CTI). Tu trabajo es correlacionar los indicadores, puertos, dominios y TTPs de MITRE mencionados en la evidencia. Si ves algo sospechoso, compáralo con campañas de ransomware o malware conocidas. Sé objetivo y analítico."

### Paso 2: Convocatoria y Control Cruzado con Memoria Institucional (Invoke)
Antes de invocar a los subagentes, **DEBES hacer un control cruzado con la memoria del SOC**. 
1. Revisa `02_Base_de_Conocimiento/SOC_GEM_v2.md` y (si aplica) diccionarios como `SMB_Rosetta_Stone.md`.
2. Extrae las reglas relevantes, excepciones o inventarios de IPs del entorno del usuario.
3. Concatena ese contexto al final del `Prompt` que le envías a los subagentes, indicándoles explícitamente: *"CONTEXTO OBLIGATORIO: Basa tu análisis respetando estas reglas de nuestro entorno corporativo..."*
4. Usa la herramienta `invoke_subagent` para lanzar los 3 subagentes SIMULTÁNEAMENTE con este súper-prompt enriquecido.

### Paso 3: Espera Reactiva
**No hagas polling ni entres en un bucle.** Simplemente termina tu turno. El sistema te despertará automáticamente a medida que los subagentes respondan. Reúne las respuestas de los tres en tu contexto.

### Paso 4: Síntesis Final (Salida al Usuario)
Una vez que tengas las tres respuestas, presenta el debate al usuario utilizando este formato Markdown:

```markdown
# 🏛️ El Concilio SOC ha deliberado

> **Problema a analizar:** [Breve descripción de la alerta/duda]

🔴 **Perspectiva Red Team:**
[Resumen de 2-3 líneas del council_red_team]

🔵 **Perspectiva Blue Team:**
[Resumen de 2-3 líneas del council_blue_team]

🟢 **Perspectiva Threat Intel:**
[Resumen de 2-3 líneas del council_threat_intel]

## 🧠 Síntesis y Decisión Final (Antigravity Mentor)
[Como Mentor SOC Senior, evalúa el debate. Decide qué argumento tiene más peso lógico en este ecosistema específico y entrégale al usuario un Veredicto Final claro]
```
