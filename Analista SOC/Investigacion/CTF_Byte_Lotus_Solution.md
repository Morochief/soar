# Resolución CTF: Hacker Holidays - The Byte Lotus Hotel

## Resumen del Incidente
Durante la evaluación, se identificó una aplicación web expuesta en el puerto 8080 (`http://10.64.152.252:8080`). La aplicación presentaba una vulnerabilidad de exposición de información crítica debido a una mala configuración en el despliegue, la cual permitía el acceso directo al directorio de control de versiones `.git/`.

## Pasos de Explotación y Recuperación

### 1. Identificación de la Vulnerabilidad
Al realizar consultas al puerto 8080, se detectó que el directorio `.git/` estaba expuesto y con la funcionalidad de listado de directorios (Directory Indexing) habilitada, permitiendo visualizar los archivos de control de versiones.

### 2. Extracción del Repositorio
Debido a la falta de conectividad hacia internet en el entorno (lo que impidió el uso de herramientas de terceros como `git-dumper`), se procedió a realizar una descarga recursiva utilizando herramientas nativas.

Comando ejecutado para espejar el directorio `.git/`:
```bash
mkdir -p repo && cd repo
wget -r -np -nH --cut-dirs=0 -e robots=off http://10.64.152.252:8080/.git/
```

### 3. Limpieza y Restauración del Árbol de Trabajo
Una vez finalizada la descarga de los objetos y referencias de Git, se eliminaron los archivos `.html` residuales generados por `wget` y se forzó la restauración del código fuente.

Comandos ejecutados:
```bash
find .git -name "index.html" -delete
git checkout -f HEAD
```

### 4. Análisis del Código Fuente y Localización de la Bandera
Al restaurar el repositorio, se listaron los archivos obtenidos (`README.md`, `app.js`, `index.html`). Al examinar el contenido de estos archivos, se identificó la bandera en texto claro dentro del archivo `README.md`, el cual contenía notas internas de desarrollo.

Comando ejecutado:
```bash
cat README.md
```

**Bandera Obtenida:**
`THM{byt3_l0tus_n3v3r_f0rg3ts}`

## Conclusión
La falla radica en el despliegue de la aplicación directamente desde el repositorio o en la falta de restricciones a nivel de servidor web para denegar el acceso a carpetas ocultas (`.git/`). Esto permitió la reconstrucción total del código fuente y el compromiso de información confidencial.
