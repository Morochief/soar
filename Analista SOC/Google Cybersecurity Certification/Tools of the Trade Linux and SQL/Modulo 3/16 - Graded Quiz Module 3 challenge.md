# Graded Quiz: Module 3 challenge

**1. ¿Cuáles son los argumentos en `mv Q1users.txt /home/analyst/reports`? Selecciona dos respuestas. (*What are the arguments in `mv Q1users.txt /home/analyst/reports`? Select two answers.*)**
- [x] `/home/analyst/reports` (*`/home/analyst/reports`*)
- [ ] `.txt` (*`.txt`*)
- [ ] `mv` (*`mv`*)
- [x] `Q1users.txt` (*`Q1users.txt`*)

---

**2. ¿Cuál de los siguientes elementos representa el directorio raíz? (*Which of the following items represents the root directory?*)**
- [ ] `*home` (*`*home`*)
- [x] `/` (*`/`*)
- [ ] `*` (*`*`*)
- [ ] `/home` (*`/home`*)

---

**3. Un analista de seguridad ingresa `grep OS updates.txt` en la línea de comandos. ¿Qué le indica este comando que haga al sistema operativo? (*A security analyst enters `grep OS updates.txt` into the command line. What does this tell the operating system to do?*)**
- [ ] Crear un nuevo archivo llamado `updates.txt` en el directorio `OS` (*Create a new file named `updates.txt` in the `OS` directory*)
- [ ] Mover el archivo `updates.txt` al directorio `OS` (*Move the `updates.txt` file to the `OS` directory*)
- [ ] Crear un nuevo directorio llamado `OS` y un nuevo archivo llamado `updates.txt` (*Create a new directory named `OS` and a new file named `updates.txt`*)
- [x] Buscar en el archivo `updates.txt` y devolver todas las líneas que contengan la cadena `OS` (*Search through the `updates.txt` file and return all lines containing the string `OS`*)

---

**4. ¿Cuál de estos comandos crea un archivo nuevo? (*Which of these commands creates a new file?*)**
- [x] `touch` (*`touch`*)
- [ ] `cd` (*`cd`*)
- [ ] `chmod` (*`chmod`*)
- [ ] `mkdir` (*`mkdir`*)

---

**5. ¿Cuáles de los siguientes son tipos de permisos? Selecciona todas las opciones que correspondan. (*Which of the following are types of permissions? Select all that apply.*)**
- [x] Lectura (*Read*)
- [ ] Autorización (*Authorize*)
- [x] Ejecución (*Execute*)
- [x] Escritura (*Write*)

---

**6. Un analista de seguridad está actualizando los permisos en el archivo `access.txt`. Quiere agregar permisos de escritura para el usuario y quitar permisos de lectura para el grupo. ¿Qué ingresa en la línea de comandos? (*A security analyst is updating permissions on the file `access.txt`. They want to add write permissions for the user and remove read permissions for the group. What do they enter on the command line?*)**
- [x] `chmod u+w,g-r access.txt` (*`chmod u-w,g-r access.txt` -> `chmod u+w,g-r access.txt`*)
- [ ] `chmod u+rw,g-rw access.txt` (*`chmod u+rw,g-rw access.txt`*)
- [ ] `chmod u-w,g+r access.txt` (*`chmod u-w,g+r access.txt`*)
- [ ] `chmod access.txt u+w,g-r` (*`chmod access.txt u+w,g-r`*)

---

**7. ¿Qué hace `sudo`? (*What does `sudo` do?*)**
- [ ] Agrega usuarios al sistema (*Adds users to the system*)
- [ ] Elimina usuarios del sistema (*Deletes users from the system*)
- [ ] Cambia el propietario asociado a un archivo determinado (*Changes the owner associated with a particular file*)
- [x] Otorga temporalmente permisos elevados a usuarios específicos (*Temporarily grants elevated permissions to specific users*)

---

**8. ¿Qué debes especificar en el argumento que sigue al comando `cd`? (*What should you specify in the argument following the `cd` command?*)**
- [x] El directorio al que deseas navegar (*The directory you want to navigate to*)
- [ ] Tu directorio actual (*Your current directory*)
- [ ] El archivo que deseas crear (*The file you want to create*)
- [ ] La cadena de texto que deseas buscar (*The string you want to search for*)

---

**9. Un analista de seguridad ingresa `apropos password` en la línea de comandos. ¿Qué le indica este comando que haga al sistema operativo? (*A security analyst enters `apropos password` into the command line. What does this tell the operating system to do?*)**
- [x] Mostrar todos los comandos que contienen la palabra "password" en las descripciones de sus páginas del manual (*Output all the commands that contain the word “password” in their man page descriptions*)
- [ ] Cambiar tu directorio actual a `/password` (*Change your current directory to `/password`*)
- [ ] Mostrar información detallada sobre el comando `password` y cómo funciona (*Display detailed information on the `password` command and how it works*)
- [ ] Mostrar una descripción del comando `password` en una sola línea (*Display a description of the `password` command on a single line*)

---

**10. Dada la siguiente cadena de permisos `drw-rw-r--`, ¿qué representa el cuarto carácter? (*Given the following permissions `drw-rw-r--`, what does the fourth character represent?*)**
- [ ] El grupo tiene permisos de ejecución para este directorio (*The group has execute permissions for this directory*)
- [x] El propietario **no** tiene permisos de ejecución para este directorio (*The owner does not have execute permissions for this directory*)
- [ ] El usuario tiene permisos de ejecución para este directorio (*The user has execute permissions for this directory*)
- [ ] El grupo **no** tiene permisos de ejecución para este directorio (*The group does not have execute permissions for this directory*)
