# Graded Quiz: Module 4 challenge

**1. ¿Qué es la depuración (*debugging*)?**
*(What is debugging?)*
- [ ] La práctica de mejorar la legibilidad del código.
- [ ] La práctica de mejorar la eficiencia del código.
- [ ] La práctica de llamar a una función desde múltiples lugares en un programa más grande.
- [x] La práctica de identificar y corregir errores en el código. *(The practice of identifying and fixing errors in code.)*

**2. Le pides a tu código que divida algo por 0, pero se produce un error. ¿Qué tipo de error es este?**
*(You ask your code to divide something by 0, but an error occurs. What type of error is this?)*
- [ ] Error de sintaxis *(Syntax error)*
- [x] Excepción (`ZeroDivisionError`) *(Exception)*
- [ ] Índice fuera de límites *(Index out of bounds)*
- [ ] Error lógico *(Logic error)*

**3. Al depurar código, ¿cuáles son formas efectivas de determinar qué secciones del código funcionan correctamente? (Selecciona todas las que correspondan)**
*(When debugging code, what are effective ways to determine which sections of code are working properly? Select all that apply.)*
- [ ] Agregar comentarios en el código *(Add comments in the code)*
- [x] Agregar instrucciones `print` (Para ver el estado de las variables). *(Add print statements)*
- [x] Usar un depurador (*debugger*). *(Use a debugger)*
- [ ] Eliminar líneas en blanco del código.

**4. Si deseas leer un archivo llamado "logs.txt", ¿qué línea de código te permite abrir este archivo con fines de lectura y almacenarlo en una variable llamada `file`?**
*(If you want to read a file called "logs.txt", which line of code allows you to open this file for purposes of reading it and store it in a variable called file?)*
- [x] `with open("logs.txt", "r") as file:` *(with open("logs.txt", "r") as file:)*
- [ ] `with open("logs.txt", file, "r"):`
- [ ] `with file.open("logs.txt", "r"):`
- [ ] `with open(file, "r") as logs.txt:`

**5. Has leído un archivo de registro (*log*) en la variable `file_text`. Esta variable contiene una cadena de texto con 50 nombres de usuario de empleados. Para pasarlo a una función, la cadena debe dividirse en una lista de nombres de usuario separados. ¿Cómo conviertes esta cadena en una lista y la almacenas en la variable `usernames`?**
*(How do you convert this string into a list and store it in a variable usernames?)*
- [x] `usernames = file_text.split()` *(usernames = file_text.split())*
- [ ] `usernames = split(usernames, file_text)`
- [ ] `usernames = usernames.split(file_text)`
- [ ] `file_text.split() as usernames`

**6. ¿Qué es el análisis de datos (*parsing*)?**
*(What is parsing?)*
- [ ] El proceso de escribir datos en un nuevo archivo.
- [ ] El proceso de leer datos línea por línea.
- [ ] El proceso de copiar datos a otros archivos.
- [x] El proceso de extraer, analizar y convertir datos en un formato más legible/utilizable. *(The process of converting data into a more readable format)*

**7. Después de haber abierto un archivo de registro como `file`, ¿qué línea de código te ayudará a leer el archivo en una variable llamada `text`?**
*(After you've opened a log file as file, which line of code will help you read the file into a variable called text?)*
- [ ] `text = read(file)`
- [x] `text = file.read()` *(text = file.read())*
- [ ] `text.read(file)`
- [ ] `text = read(file, "r")`

**8. Deseas comprobar si un dispositivo ejecuta un sistema operativo que necesita actualizaciones. Los dispositivos que contienen la subcadena "i71" en su ID necesitan esta actualización. Quieres leer un archivo de registro, convertirlo en cadena, dividirlo en una lista `devices`, y luego separar los que contengan "i71" en una lista `updates_list`. ¿Qué formaría parte de tu código? (Selecciona tres respuestas)**
*(If you want to automate this through Python, what would be part of your code? Select three answers.)*
- [x] Un bucle `for` para iterar a través de todos los elementos en la lista de dispositivos. *(A for loop to iterate through all items in the devices list)*
- [ ] Una variable de contador para realizar un seguimiento del *número* de dispositivos (Falso, porque queremos una lista, no una cantidad).
- [x] Una instrucción `if` que verifique si los elementos en los dispositivos contienen la subcadena "i71". *(An if statement that checks if elements in devices contain the substring "i71")*
- [x] Una función `split()` para dividir la cadena de texto en una lista. *(A split() function to split the string containing the information in the log file into a devices list)*

**9. Analiza la salida de este código y depúralo:**
*(Analyze its output, and then debug it. What is the error related to?)*
```python
device_id = "p35rv47
for char in device_id:
  print(char)
```
- [ ] Una variable mal escrita.
- [ ] Falta un doble signo de igual (==).
- [ ] Faltan dos puntos (:).
- [x] Falta una comilla ("). *(A missing quotation mark ("))*

**10. Analiza la salida de este código y depúralo:**
*(How can you fix the error?)*
```python
list = ["user1", "user2", "user3", "user4"]
for user in list:
  if user != "user3":
    print("Warning: user3 should not access the system.")
```
- [ ] Cambiar "user3" a "user1" en la condicional.
- [x] Cambiar el operador `!=` al operador `==` en la condicional. *(Change the != operator to the == operator in the conditional.)*
- [ ] Cambiar la sangría (indentación).
- [ ] Cambiar "user3" a "user2" en la condicional.
