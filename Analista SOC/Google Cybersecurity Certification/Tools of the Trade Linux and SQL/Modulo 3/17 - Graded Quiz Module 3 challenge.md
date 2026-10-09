# Graded Quiz: Module 3 challenge

**1. ¿Cuáles son los argumentos en `mv Q1users.txt /home/analyst/reports`? Selecciona dos respuestas. (*What are the arguments in `mv Q1users.txt /home/analyst/reports`? Select two answers.*)**
- [ ] `mv` (*`mv`*)
- [ ] `.txt` (*`.txt`*)
- [x] `/home/analyst/reports` (*`/home/analyst/reports`*)
- [x] `Q1users.txt` (*`Q1users.txt`*)

---

**2. ¿Qué es el directorio raíz? (*What is the root directory?*)**
- [ ] Un subdirectorio del directorio personal (*A subdirectory of the home directory*)
- [x] El directorio de nivel más alto en Linux (*The highest-level directory in Linux*)
- [ ] El comando para navegar entre directorios (*The command to navigate between directories*)
- [ ] El directorio personal de un usuario específico sin privilegios (*The home directory of a specific user with no privileges*)

---

**3. Un analista de seguridad ingresa `grep OS updates.txt` en la línea de comandos. ¿Qué le indica este comando que haga al sistema operativo? (*A security analyst enters `grep OS updates.txt` into the command line. What does this tell the operating system to do?*)**
- [ ] Crear un nuevo directorio llamado `OS` y un nuevo archivo llamado `updates.txt` (*Create a new directory named `OS` and a new file named `updates.txt`*)
- [ ] Crear un nuevo archivo llamado `updates.txt` en el directorio `OS` (*Create a new file named `updates.txt` in the `OS` directory*)
- [ ] Mover el archivo `updates.txt` al directorio `OS` (*Move the `updates.txt` file to the `OS` directory*)
- [x] Buscar en el archivo `updates.txt` y devolver todas las líneas que contengan la cadena `OS` (*Search through the `updates.txt` file and return all lines containing the string `OS`*)

---

**4. Un analista de seguridad ingresa `touch updates.txt` en la línea de comandos. ¿Qué le indica este comando que haga al sistema operativo? (*A security analyst enters `touch updates.txt` into the command line. What does this tell the operating system to do?*)**
- [ ] Abrir el archivo `updates.txt` (*Open the `updates.txt` file*)
- [ ] Crear un nuevo archivo llamado `updates.txt` y moverlo al directorio raíz (*Create a new file named `updates.txt` and move it to the root directory*)
- [ ] Mover el archivo `updates.txt` fuera de su directorio actual (*Move the `updates.txt` file out of their current directory*)
- [x] Crear un nuevo archivo llamado `updates.txt` en su directorio actual (*Create a new file named `updates.txt` in their current directory*)

---

**5. ¿Qué son lectura, escritura y ejecución? (*What are read, write, and execute?*)**
- [ ] Comandos específicos de Linux utilizados para cambiar los permisos de archivos (*Specific Linux commands used to change file permissions*)
- [ ] Los tres tipos de propietarios para archivos y directorios (*The three types of owners for files and directories*)
- [ ] Diferentes métodos para editar archivos (*Different methods for editing files*)
- [x] Los tres tipos de permisos para usuarios autorizados (*The three types of permissions for authorized users*)

---

**6. Un analista de seguridad ingresa `chmod u+w,g-r access.txt` en la línea de comandos. ¿Qué hace este comando? (*A security analyst enters `chmod u+w,g-r access.txt` into the command line. What does this command do?*)**
- [ ] Agrega permisos de escritura para el grupo y quita permisos de lectura para el usuario en el archivo `access.txt`. (*It adds write permissions for the group and removes read permissions for the user on the access.txt file.*)
- [ ] Quita permisos de escritura y lectura para el usuario y el grupo en el archivo `access.txt`. (*It removes write and read permissions for the user and group on the access.txt file.*)
- [x] Agrega permisos de escritura para el usuario y quita permisos de lectura para el grupo en el archivo `access.txt`. (*It adds write permissions for the user and removes read permissions for the group on the access.txt file.*)
- [ ] Agrega permisos de escritura y lectura para el usuario y el grupo en el archivo `access.txt`. (*It adds write and read permissions for the user and group on the access.txt file.*)

---

**7. ¿Qué hace `sudo`? (*What does `sudo` do?*)**
- [ ] Elimina usuarios del sistema (*Deletes users from the system*)
- [ ] Agrega usuarios al sistema (*Adds users to the system*)
- [ ] Cambia el propietario asociado a un archivo determinado (*Changes the owner associated with a particular file*)
- [x] Otorga temporalmente permisos elevados a usuarios específicos (*Temporarily grants elevated permissions to specific users*)

---

**8. ¿Qué debes especificar en el argumento que sigue al comando `cd`? (*What should you specify in the argument following the `cd` command?*)**
- [ ] La cadena de texto que deseas buscar (*The string you want to search for*)
- [x] El directorio al que deseas navegar (*The directory you want to navigate to*)
- [ ] El archivo que deseas crear (*The file you want to create*)
- [ ] Tu directorio actual (*Your current directory*)

---

**9. ¿Cuál de los siguientes comandos busca una cadena especificada en las descripciones de las páginas del manual? (*Which of the following commands searches the manual page descriptions for a specified string?*)**
- [ ] `cp` (*`cp`*)
- [ ] `man` (*`man`*)
- [ ] `pwd` (*`pwd`*)
- [x] `apropos` (*`apropos`*)

---

**10. Dada la siguiente cadena de permisos `drw-rw-r--`, ¿qué permisos tiene el grupo? Selecciona todas las opciones que correspondan. (*Given the following permissions `drw-rw-r--`, what permissions does the group have? Select all that apply.*)**
- [x] Lectura (*Read*)
- [ ] Uso (*Use*)
- [x] Escritura (*Write*)
- [ ] Ejecución (*Execute*)
