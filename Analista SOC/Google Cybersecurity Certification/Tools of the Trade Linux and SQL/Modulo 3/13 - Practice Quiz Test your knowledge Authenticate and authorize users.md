# Practice Quiz: Test your knowledge: Authenticate and authorize users

**1. ¿Qué es la autorización? (*What is authorization?*)**
- [ ] El concepto de otorgar únicamente el acceso mínimo y la autorización requerida para completar una tarea o función (*The concept of granting only the minimal access and authorization required to complete a task or function*)
- [ ] El proceso mediante el cual un usuario demuestra que es quien dice ser en el sistema (*The process of a user proving that they are who they say they are in the system*)
- [x] El concepto de otorgar acceso a recursos específicos en un sistema (*The concept of granting access to specific resources in a system*)
- [ ] El proceso de otorgar temporalmente permisos elevados a usuarios específicos (*The process of temporarily granting elevated permissions to specific users*)

---

**2. Un analista de seguridad está actualizando los permisos en un directorio llamado `projects`. Los permisos actuales son `drwxrw-r--`. Quiere agregar permisos de ejecución para el grupo. ¿Qué ingresa en la línea de comandos? (*A security analyst is updating permissions on a directory named `projects`. The current permissions are `drwxrw-r--`. They want to add execute permissions for the group. What do they enter on the command line?*)**
- [ ] `chmod g-x projects` (*`chmod g-x projects`*)
- [ ] `chmod x+x projects` (*`chmod x+x projects`*)
- [x] `chmod g+x projects` (*`chmod g+x projects`*)
- [ ] `chmod u-x projects` (*`chmod u-x projects`*)

---

**3. Un profesional de la seguridad ingresa `chmod g+w access.txt` en la línea de comandos. ¿Qué le indica este comando que haga al sistema operativo? (*A security professional enters `chmod g+w access.txt` into the command line. What does this command tell the operating system to do?*)**
- [x] Agregar permisos de escritura al grupo para el archivo `access.txt` (*Add write permissions to the group for the `access.txt` file*)
- [ ] Quitar permisos de escritura al usuario para el archivo `access.txt` (*Remove write permissions from the user for the `access.txt` file*)
- [ ] Quitar permisos de escritura al grupo para el archivo `access.txt` (*Remove write permissions from the group for the `access.txt` file*)
- [ ] Agregar permisos de escritura al usuario para el archivo `access.txt` (*Add write permissions to the user for the `access.txt` file*)

---

**4. ¿Cuáles de los siguientes comandos típicamente deben usarse con `sudo`? Selecciona tres respuestas. (*Which of the following commands typically must be used with `sudo`? Select three answers.*)**
- [ ] `chmod` (*`chmod`*)
- [x] `useradd` (*`useradd`*)
- [x] `userdel` (*`userdel`*)
- [x] `chown` (*`chown`*)

---

**5. ¿Cuáles de las siguientes afirmaciones describen correctamente la cadena de permisos de archivo `-rw-rw-rw-`? Selecciona dos respuestas. (*Which of the following statements correctly describe the file permissions string `-rw-rw-rw-`? Select two answers.*)**
- [x] El usuario tiene permisos de escritura. (*The user has write permissions.*)
- [ ] El usuario y el grupo tienen permisos de ejecución. (*The user and group have execute permissions.*)
- [x] El grupo tiene permisos de lectura. (*The group has read permissions.*)
- [ ] El tipo de archivo es un directorio. (*The file type is a directory.*)
