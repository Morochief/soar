# Practice Quiz: Test your knowledge: SQL queries

**1. ¿Cuál de las siguientes es una consulta SQL válida? (*Which of the following is a valid SQL query?*)**
- [ ] `SELECT COLUMNS FROM employees;`
- [ ] `FROM employees, SELECT *;`
- [x] `SELECT * FROM employees;`
- [ ] `SELECT ALL FROM employees;`

---

**2. ¿Qué es el filtrado en SQL? (*What is filtering in SQL?*)**
- [x] Seleccionar datos que coincidan con una condición determinada (*Selecting data that match a certain condition*)
- [ ] Eliminar datos innecesarios de la base de datos (*Removing unnecessary data from the database*)
- [ ] Cambiar una tabla para que coincida con una condición (*Changing a table to match a condition*)
- [ ] Eliminar registros no válidos (*Removing invalid records*)

---

**3. ¿Qué patrón coincide con cualquier cadena de texto que comience con el carácter 'A'? (*Which pattern matches with any string that starts with the character 'A'?*)**
- [ ] `'%A'`
- [x] `'A%'`
- [ ] `'A'`
- [ ] `'%A%'`

---

**4. Un analista de seguridad quiere filtrar la tabla `log_in_attempts` para obtener los registros donde el valor en la columna `country` sea 'Canada'. ¿Cuál es una consulta válida para esto? (*A security analyst wants to filter the log_in_attempts table for records where the value in the country column is 'Canada'. What is a valid query for this?*)**
- [ ] ```sql
      SELECT *
      FROM log_in_attempts
      WHERE country = Canada;
      ```
- [ ] ```sql
      SELECT WHERE country = 'Canada'
      FROM log_in_attempts;
      ```
- [ ] ```sql
      WHERE country = 'Canada'
      SELECT *
      FROM log_in_attempts;
      ```
- [x] ```sql
      SELECT *
      FROM log_in_attempts
      WHERE country = 'Canada';
      ```
