---
name: update_soc_memory
description: "Añade nuevos patrones heurísticos confirmados a la tabla de Memoria Institucional de SOC_GEM_v2.md"
---

# Skill: Actualizador de Memoria Institucional SOC

Esta skill se debe usar cada vez que identifiques un comportamiento repetitivo, un nuevo Falso Positivo validado o un True Positive confirmado que el equipo SOC deba recordar en el futuro.

## INSTRUCCIONES:
1. Revisa el archivo `SOC_GEM_v2.md` para encontrar la tabla de "MEMORIA INSTITUCIONAL (Falsos Positivos & Anomalías de Red Confirmadas)".
2. Añade una nueva fila respetando estrictamente el formato de columnas de la tabla Markdown:
   `| **[Observable/Entidad]** ([Contexto]) | [Ubicación o Función] | [Comportamiento esperado/ruido]. **[Veredicto]**. |`
3. Usa la herramienta de reemplazo de contenido (`multi_replace_file_content` o `replace_file_content`) para insertar la nueva fila en la sección correcta, garantizando que el archivo no se rompa ni se borre otro contenido.
4. Confírmale al usuario que la Memoria ha sido actualizada para que futuras alertas con el mismo patrón sean mitigadas rápidamente.
