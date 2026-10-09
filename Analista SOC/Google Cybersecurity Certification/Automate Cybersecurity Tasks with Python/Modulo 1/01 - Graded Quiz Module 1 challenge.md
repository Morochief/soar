# Graded Quiz: Module 1 challenge

**1. Completa el espacio en blanco: La automatización es _____.**
*(Fill in the blank: Automation is _____.)*
- [x] el uso de tecnología para reducir el esfuerzo humano y manual para realizar tareas comunes y repetitivas *(the use of technology to reduce human and manual effort to perform common and repetitive tasks)*
- [ ] el uso de esfuerzo humano y manual para reducir el consumo de energía tecnológica
- [ ] el reemplazo de tecnología existente
- [ ] la combinación de tecnología y esfuerzo manual para completar una tarea

**2. El propósito del siguiente código es imprimir un mensaje de "Intentando conexión" mientras el valor de la variable `count` sea menor que 10. El valor de `count` debería aumentar en 1 con cada iteración del bucle. ¿Qué tiene de malo el código? (Selecciona todas las respuestas que correspondan)**
*(The purpose of the following code is to print an "Attempting connection" message while the value of the count variable is less than 10... What is wrong with the code? Select all that apply.)*
```python
count = 1 
while count < 10: 
print("Attempting Connection") 
count = count + 1 
```
- [ ] La línea con `while count < 10:` no está indentada (sangría).
- [ ] La línea con `count = 1` no está indentada.
- [x] La línea con `print("Attempting connection")` no está indentada. *(The line with print("Attempting connection") is not indented.)*
- [x] La línea con `count = count + 1` no está indentada. *(The line with count = count + 1 is not indented.)*

**3. Completa el espacio en blanco: Los datos de tipo cadena (String) _____.**
*(Fill in the blank: String data _____.)*
- [x] deben ir entre comillas *(must be placed in quotation marks)*
- [ ] deben ir entre corchetes
- [ ] deben incluir un punto decimal
- [ ] deben ir entre paréntesis

**4. ¿Qué línea de código en Python crearía un valor booleano de `True`?**
*(Which line of Python code would create a Boolean value of True?)*
- [ ] `print(["Boolean"])` (Esto imprime una lista)
- [ ] `print("True")` (Esto imprime un String)
- [ ] `print(25<24)` (Esto evalúa a False)
- [x] `print(10<100)` *(print(10<100))*

**5. ¿Qué línea de código asigna la cadena "dtanaka" a una variable llamada `username`?**
*(Which line of code assigns the string "dtanaka" to a variable called username?)*
- [x] `username = "dtanaka"` *(username = "dtanaka")*
- [ ] `username = dtanaka`
- [ ] `"dtanaka" = username`
- [ ] `username("dtanaka")`

**6. ¿Qué código puedes utilizar para devolver el tipo de dato del valor almacenado en la variable `input`?**
*(What code can you use to return the data type of the value stored in the input variable?)*
- [ ] `print("type")`
- [x] `type(input)` *(type(input))*
- [ ] `type("string")`
- [ ] `print(input)`

**7. Estás comprobando si la cadena almacenada en una variable `device_id` coincide con el ID de dispositivo correcto, la cadena "15hgu3769". Cuando coincida, deseas imprimir "Login successful!". ¿Qué declaración condicional tiene la sintaxis correcta necesaria para hacer esto?**
*(Which conditional statement has the correct syntax needed to do this?)*
- [ ] `if "device_id" = "15hgu3769"` \n `print("Login successful!")`
- [x] `if device_id == "15hgu3769":` \n `  print("Login successful!")`
- [ ] `if device_id != "15hgu3769"` \n `  print("Login successful!")`
- [ ] `if "device_id == 15hgu3769"` \n `print("Login successful!")`

**8. Completa el espacio en blanco: Una instrucción `else` _____.**
*(Fill in the blank: An else statement _____.)*
- [ ] contiene su propia condición única
- [x] se ejecuta cuando la condición de la instrucción `if` que la precede se evalúa como Falsa (`False`) *(executes when the condition in the if statement preceding it evaluates to False)*
- [ ] se ejecuta cuando la condición de la instrucción `if` que la precede se evalúa como Verdadera (`True`)
- [ ] se requiere después de cada instrucción `if`

**9. ¿Qué instrucción iterativa (*loop*) puedes usar si deseas imprimir "Security alert" cinco veces?**
*(What iterative statement can you use if you want to print "Security alert" five times?)*
- [ ] `for i in range(6):` \n `  print("Security alert")`
- [ ] `for i in [0, 5]:` \n `  print("Security alert")`
- [ ] `for i in range(1,5):` \n `  print("Security alert")`
- [x] `for i in range(5):` \n `  print("Security alert")`

**10. Deseas imprimir todos los números pares entre 0 y 10 (es decir, 0, 2, 4, 6, 8 y 10). ¿Cuál debería ser tu próxima línea de código?**
*(You want to print all even numbers between 0 and 10... What should your next line of code be?)*
```python
count = 0
while count <= 10:
  print(count)
```
- [ ] `if count < 10:`
- [x] `count = count + 2` *(count = count + 2)*
- [ ] `count = count + 1`
- [ ] `count = 1`
