---
name: google_cyber_transcriber
description: Framework para traducir y formatear transcripciones del Google Cybersecurity Certificate al español.
---

# Google Cybersecurity Transcriber Skill

Esta skill define el framework para procesar las transcripciones en crudo del "Google Cybersecurity Certificate". Cuando el usuario envíe una transcripción, el agente debe aplicar estrictamente las siguientes reglas para generar un documento Markdown altamente profesional, estético y preciso.

## 1. Reglas de Formato (Markdown Estético)
- **Título del Documento:** Usa un encabezado de nivel 1 (`#`) con el título original (o traducido sutilmente) de la transcripción.
- **Flujo de Lectura:** Elimina los timestamps (`00:00`, `01:23`) del cuerpo principal para que el texto fluya como un artículo o capítulo de libro. No presentes el texto como subtítulos fragmentados.
- **Estructura Lógica:** Agrupa las oraciones en párrafos coherentes basándote en el contexto. Utiliza encabezados de nivel 2 y 3 (`##`, `###`) para separar temas de forma natural.
- **Alertas y Notas:** Usa GitHub Alerts (ej. `> [!NOTE]`, `> [!IMPORTANT]`) para resaltar conceptos clave, consejos del instructor o estadísticas importantes (ej. proyecciones de crecimiento laboral).
- **Listas:** Convierte enumeraciones implícitas en listas con viñetas para mejorar la legibilidad.

## 2. Reglas de Traducción y Tono
- **Tono:** Mantén el entusiasmo original de los instructores de Google. El lenguaje debe ser profesional, claro, directo y motivador.
- **Español Preciso (Sin Errores):** Evita calcos sintácticos del inglés. Las oraciones deben sonar naturales en español neutro.
- **Terminología Técnica (Spanglish Controlado):** 
  - Términos de la industria que rara vez se traducen en el ámbito profesional deben mantenerse en inglés (ej. *Framework*, *Incident Response*, *Logs*, *Malware*, *Scripts*, *SQL*, *Linux*).
  - Si un término tiene una traducción aceptada y común (ej. *Network* -> *Red*, *Threats* -> *Amenazas*, *Vulnerabilities* -> *Vulnerabilidades*), úsala.
  - En caso de duda o para conceptos muy específicos, escribe el término en español seguido del término en inglés en cursiva y entre paréntesis la primera vez (ej. *activos (assets)*).

## 3. Estructura Obligatoria del Documento
Todo apunte generado debe seguir esta estructura base:
1. **Encabezado principal:** Título de la clase.
2. **Introducción del Instructor:** Presentación de quién habla y su rol en Google.
3. **Desarrollo Temático:** El cuerpo de la transcripción dividido lógicamente.
4. **Puntos Clave (Key Takeaways):** Un breve resumen final en viñetas destilando lo más importante del texto.

## 4. Conversión de Documentos Adicionales (PDFs, PPTX, etc.)
El curso frecuentemente provee materiales de lectura en formato PDF u otros. Si el usuario te envía un documento y la instrucción "markitdown [archivo]" (o similar), debes convertirlo aplicando un estándar riguroso.

**Estándar de Ejecución de MarkItDown:**
Debido a que `markitdown` se instaló a nivel local del usuario (User Site-Packages) y el ejecutable no se encuentra en la variable de entorno global `PATH` de Windows, intentar ejecutar `markitdown` directamente en la terminal fallará. Tampoco es necesario levantar un entorno virtual (venv) para esta tarea simple, ya que el módulo está disponible para el intérprete base de Python.

Sigue estrictamente estos pasos:
1. **Ejecución Vía Módulo:** Nunca uses `markitdown` directamente. Utiliza el ejecutable de Python invocando el módulo:
   ```powershell
   python -m markitdown "Ruta\Al\Archivo.pdf" -o "Ruta\Al\Archivo.md"
   ```
2. **Espera de Conversión:** Espera a que el proceso en segundo plano finalice y se genere el archivo `.md`.
3. **Traducción y Formateo:** Lee el Markdown generado (el cual estará en inglés y en bruto), tradúcelo completamente al español aplicando las **Reglas de Traducción (Sección 2)** y dale estructura aplicando las **Reglas de Formato (Sección 1)**.
4. **Entrega:** Sobreescribe el archivo `.md` con la versión traducida y maquetada, e infórmale al usuario.

## 5. Procesamiento de Quizzes (HTML/JSON)
Si el usuario te envía un bloque de código HTML (o JSON incrustado) perteneciente a un examen o cuestionario (*Quiz*):
1. Extrae las preguntas y las opciones de respuesta del código fuente.
2. Identifica las **respuestas correctas** utilizando tu base de conocimientos y el contexto de las lecturas/transcripciones anteriores.
3. Debes incluir **tanto la versión en inglés (original) como la traducción al español** de cada pregunta y de TODAS sus opciones. Esto es obligatorio para que el usuario mantenga el contexto exacto del examen. Formato sugerido: "Pregunta en Español (*Pregunta en Inglés*)".
4. Maqueta el resultado en un archivo Markdown, utilizando cajas de verificación (`[x]`) para marcar claramente las opciones correctas y (`[ ]`) para las incorrectas.
5. Guarda el archivo con un título descriptivo que inicie con `Practice Quiz` o `Quiz`.

## 6. Flujo de Trabajo General (Para Textos y Transcripciones)
1. Analiza el texto en crudo proporcionado por el usuario.
2. Traduce mentalmente aplicando las reglas de terminología.
3. Redacta el documento `.md` en la ruta `Google Cybersecurity Certification/` usando el nombre indicado.
4. Asegúrate de que el documento no contenga errores ortográficos ni traducciones literales torpes.

## 7. Enumeración Automática en Vivo (Live Enumeration)
Para mantener el directorio limpio y secuencial, **debes numerar automáticamente cada archivo en el momento de su creación** (ej. `01 - Welcome.md`, `02 - Quiz.md`, `03 - Reading.md`). 

1. Antes de guardar un nuevo documento, revisa rápidamente la carpeta actual del módulo con el comando `Get-ChildItem -Path . -Filter "*.md"` para determinar el último número utilizado.
2. Nombra el nuevo archivo con el prefijo numérico correspondiente sumando +1 al último archivo encontrado (ej. si el último es `04 - ...`, guarda el tuyo como `05 - ...`).
3. Esto elimina la necesidad de correr scripts temporales de enumeración al final del módulo.

## 8. Re-enumeración Forzada (Fallback)
Solo en caso de que el usuario pida explícitamente "re-enumerar" la carpeta porque el orden se rompió:
1. Crea un script temporal `enumerate.ps1`:
   ```powershell
   $i = 0
   Get-ChildItem -Path . -Filter "*.md" | Sort-Object LastWriteTime | ForEach-Object {
       $i++
       $newName = "{0:D2} - {1}" -f $i, ($_.Name -replace '^\d{2} - ', '')
       Rename-Item -Path $_.FullName -NewName $newName
   }
   ```
2. Ejecútalo: `powershell -ExecutionPolicy Bypass -File .\enumerate.ps1`
3. Bórralo e informa al usuario.
