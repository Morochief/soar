# Graded Quiz: Module 3 challenge

**1. ¿Qué línea de código devuelve el número de caracteres de la cadena asignada a la variable `username`?**
*(Which line of code returns the number of characters in the string assigned to the username variable?)*
- [ ] `print(str(username))`
- [ ] `print(username.str())`
- [x] `print(len(username))` *(print(len(username)))*
- [ ] `print(username.len())`

**2. ¿Qué línea de código devuelve una copia de la cadena "bmoreno" como "BMORENO"?**
*(Which line of code returns a copy of the string "bmoreno" as "BMORENO"?)*
- [x] `print("bmoreno".upper())` *(print("bmoreno".upper()))*
- [ ] `print("bmoreno"(upper))`
- [ ] `print(upper."bmoreno"())`
- [ ] `print(upper("bmoreno"))`

**3. ¿Cuál es el índice del carácter "c" en la cadena "encryption"?**
*(What is the index of the character "c" in the string "encryption"?)*
- [ ] 3
- [ ] 1
- [x] 2 *(2)*
- [ ] 4
> [!NOTE]
> En Python, los índices comienzan en `0`. En "encryption": e=0, n=1, c=2.

**4. ¿Cuál es el resultado (output) del siguiente código?**
*(What is the output of the following code?)*
```python
username_list = ["elarson", "bmoreno", "tshah"] 
device_id_list = ["us2c0R5", "2R78TBR", "bt3MIEz"]
print(username_list + device_id_list)
```
- [ ] Un mensaje de error *(An error message)*
- [ ] `["us2c0R5", "2R78TBR", "bt3MIEz", "elarson", "bmoreno", "tshah"]`
- [x] `["elarson", "bmoreno", "tshah", "us2c0R5", "2R78TBR", "bt3MIEz"]` *(["elarson", "bmoreno", "tshah", "us2c0R5", "2R78TBR", "bt3MIEz"])*
- [ ] `["elarson", "us2c0R5", "bmoreno", "2R78TBR", "tshah", "bt3MIEz"]`

**5. Una variable llamada `my_list` contiene la lista `[1,2,3,4]`. ¿Qué línea de código agrega el elemento `5` al final de la lista utilizando `.insert()`?**
*(A variable named my_list contains the list [1,2,3,4]. Which line of code adds the element 5 to the end of the list?)*
- [ ] `my_list.insert(5)`
- [x] `my_list.insert(4,5)` *(my_list.insert(4,5))*
- [ ] `my_list.insert(5,4)`
- [ ] `my_list.insert(5,5)`

**6. Completa el espacio en blanco: Un(a) _____ es un conjunto de reglas para resolver un problema.**
*(Fill in the blank: A(n) _____ is a set of rules to solve a problem.)*
- [ ] append *(append)*
- [x] algoritmo *(algorithm)*
- [ ] expresión regular *(regular expression)*
- [ ] índice *(index)*

**7. ¿Cuáles de las siguientes cadenas devolvería Python como coincidencias (matches completos) para el patrón de expresión regular de `"\w"`? (Selecciona todas las que correspondan)**
*(Which of the following strings would Python return as matches to the regular expression pattern of "\w"? Select all that apply.)*
- [x] `"2"`
- [ ] `"1B"`
- [x] `"W"`
- [ ] `"security"`
> [!NOTE]
> El patrón `\w` coincide con **un solo** carácter alfanumérico. Para que coincidiera con "1B" o "security", el patrón tendría que ser `\w+`. Por lo tanto, Python solo devolvería como coincidencias completas las opciones que tienen longitud de 1.

**8. ¿Qué módulo necesitas importar para usar expresiones regulares en Python?**
*(What module do you need to import to use regular expressions in Python?)*
- [ ] `csv`
- [ ] `time`
- [x] `re` *(re)*
- [ ] `os`

**9. ¿Qué método agrega la entrada al final de una lista?**
*(Which method adds input to the end of a list?)*
- [x] `.append()` *(.append())*
- [ ] `.lower()`
- [ ] `.index()`
- [ ] `.insert()`

**10. Necesitas tomar un corte (*slice*) de un ID de red. Específicamente, debes extraer los caracteres con índices del 6 al 10 (ambos inclusive). ¿Cuál de los siguientes fragmentos de código hará esto correctamente?**
*(You need to take a slice from a network ID. Specifically, you must extract the characters with indices of 6 through 10. Which of the following code snippets will correctly do this?)*
```python
network_id = "l693m585n528"
```
- [ ] `network_id[5:10]`
- [x] `network_id[6:11]` *(network_id[6:11])*
- [ ] `network_id[7:11]`
- [ ] `network_id[6:10]`
