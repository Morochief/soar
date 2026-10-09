# Lab: Complete a SQL join

En esta actividad práctica de laboratorio, aprenderás a combinar información de múltiples tablas en una base de datos relacional mediante la cláusula `JOIN` de **SQL** (*Structured Query Language*). Practicarás el uso de uniones internas (`INNER JOIN`) y uniones externas (`LEFT JOIN` y `RIGHT JOIN`) en el entorno de MariaDB.

Como analista de ciberseguridad, frecuentemente necesitarás correlacionar datos dispersos en diferentes tablas (por ejemplo, vincular identificadores de hardware con nombres de usuarios o cruzar cuentas de empleados con registros de inicio de sesión) para reconstruir incidentes de seguridad e identificar activos o cuentas no asignadas.

---

## Introducción del Equipo de Ciberseguridad de Google

Una base de datos relacional organiza los datos en tablas interconectadas por columnas compartidas o claves (*keys*). Cuando investigas un incidente de seguridad, una sola tabla rara vez ofrece la visión completa. Utilizar las combinaciones en SQL te permite puentea la información entre tablas, correlacionando por ejemplo el hardware comprometido con la identidad del empleado responsable o los registros de eventos con la estructura organizacional.

---

## Conceptos Clave de Uniones en SQL (SQL Joins)

### 1. Conexión Compartida (*Shared Connection / Key*)
Para unir dos tablas, SQL requiere una columna común existente en ambas tablas (por ejemplo, `device_id` o `username`).

### 2. Notación de Punto (*Dot Notation*)
Cuando ambas tablas contienen una columna con el mismo nombre, debes especificar a cuál tabla pertenece mediante la sintaxis `Tabla.Columna` (ej. `machines.device_id` y `employees.device_id`) para evitar errores de ambigüedad.

### 3. Tipos de Uniones (*Types of Joins*)

* **`INNER JOIN` (Unión Interna):** Devuelve únicamente las filas que coinciden en ambas tablas. Las filas sin correspondencia en alguna de las dos tablas se omiten del resultado.
* **`LEFT JOIN` (Unión Izquierda):** Mantiene **todas** las filas de la tabla izquierda (la especificada después de `FROM`), incluso si no tienen coincidencia en la tabla derecha. Si no hay coincidencia, las columnas de la tabla derecha mostrarán `NULL`.
* **`RIGHT JOIN` (Unión Derecha):** Mantiene **todas** las filas de la tabla derecha (la especificada después de `JOIN`), incluso si no tienen coincidencia en la tabla izquierda. Si no hay coincidencia, las columnas de la tabla izquierda mostrarán `NULL`.

> [!TIP]
> **Preferencia Profesional por `LEFT JOIN`:**
> En la industria de la ciberseguridad, la mayoría de los analistas utiliza casi exclusivamente `LEFT JOIN`. Como leemos de izquierda a derecha, resulta más intuitivo pensar: *"Quiero la lista principal (Tabla A) y traeré lo que coincida de la lista secundaria (Tabla B)"*. Puedes lograr exactamente el mismo resultado de un `RIGHT JOIN` simplemente invirtiendo el orden de las tablas en `FROM` y aplicando un `LEFT JOIN`.

---

## Desarrollo Temático: Guía Paso a Paso del Laboratorio Práctico

### Escenario Operativo
Estás investigando un incidente de seguridad reciente que comprometió varios equipos. Tu objetivo es correlacionar los dispositivos con sus usuarios correspondientes, identificar máquinas sin asignar o empleados sin equipos asociados, y listar todos los intentos de inicio de sesión vinculados a los empleados de la empresa.

---

### Tarea 1: Vincular Empleados con sus Máquinas (`INNER JOIN`)

Para averiguar qué empleados utilizan qué dispositivos, debes combinar las tablas `machines` y `employees` utilizando la columna común `device_id`.

1. **Ejecuta un `INNER JOIN` entre las tablas `machines` y `employees`:**
   ```sql
   SELECT * FROM machines 
   INNER JOIN employees ON machines.device_id = employees.device_id;
   ```

> [!NOTE]
> **Análisis de Sintaxis:**
> * `FROM machines`: Especifica la primera tabla (tabla izquierda).
> * `INNER JOIN employees`: Añade la segunda tabla (tabla derecha).
> * `ON machines.device_id = employees.device_id`: Establece la regla de coincidencia exacta sobre la columna `device_id`.

#### Pregunta de Evaluación - Tarea 1

**¿Cuántas filas devolvió la consulta con `INNER JOIN`? (*How many rows did the inner join return?*)**
- [ ] 185
- [ ] 124
- [ ] 85
- [x] 185

---

### Tarea 2: Recuperar Datos Completos con `LEFT JOIN` y `RIGHT JOIN`

Ahora debes identificar tanto los dispositivos que no están asignados a ningún usuario (equipos en inventario o reserva) como a los empleados que no tienen un dispositivo asignado.

1. **Ejecuta un `LEFT JOIN` para conservar todas las máquinas de la tabla `machines`:**
   ```sql
   SELECT * FROM machines 
   LEFT JOIN employees ON machines.device_id = employees.device_id;
   ```

#### Pregunta de Evaluación - Tarea 2 (Parte 1)

**¿Cuál es el valor en la columna `username` para el último registro devuelto? (*What is the value in the username column for the last record returned?*)**
- [ ] cgriffin
- [ ] areyes
- [ ] asundara
- [x] NULL

> [!IMPORTANT]
> **Interpretación de Valores `NULL`:** Un valor `NULL` en las columnas de empleados indica que esa máquina existe en el inventario pero no tiene un usuario asignado en este momento.

2. **Ejecuta un `RIGHT JOIN` para conservar todos los empleados de la tabla `employees`:**
   ```sql
   SELECT * FROM machines 
   RIGHT JOIN employees ON machines.device_id = employees.device_id;
   ```

#### Pregunta de Evaluación - Tarea 2 (Parte 2)

**¿Cuál es el valor en la columna `username` para el último registro devuelto? (*What is the value in the username column for the last record returned?*)**
- [ ] asundara
- [ ] NULL
- [ ] cgriffin
- [x] areyes

---

### Tarea 3: Obtener Datos de Intentos de Inicio de Sesión de Empleados

Para continuar la investigación del incidente de seguridad, debes obtener información de todos los empleados que han realizado intentos de inicio de sesión. Para ello, realizarás un `INNER JOIN` entre `employees` y `log_in_attempts` utilizando la columna común `username`.

1. **Ejecuta la combinación interna entre las tablas `employees` y `log_in_attempts`:**
   ```sql
   SELECT * FROM employees 
   INNER JOIN log_in_attempts ON employees.username = log_in_attempts.username;
   ```

#### Pregunta de Evaluación - Tarea 3

**¿Cuántos registros devuelve este `INNER JOIN`? (*How many records are returned by this inner join?*)**
- [x] 200
- [ ] 175
- [ ] 210
- [ ] 145

---

## Puntos Clave (Key Takeaways)

* **Propósito de los `JOINS`:** Permiten vincular información distribuida en distintas tablas relacionales utilizando una columna común.
* **Uso de `INNER JOIN`:** Ideal para cuando solo interesan los registros que tienen una correspondencia directa y exacta en ambas tablas.
* **Uso de `LEFT JOIN` y `RIGHT JOIN`:** Esenciales para identificar vacíos o discrepancias en los datos (como equipos huérfanos o empleados sin recursos asignados) reflejados con valores `NULL`.
* **Sintaxis de Punto (`Tabla.Columna`):** Es una buena práctica y requisito imprescindible en columnas con el mismo nombre para evitar errores de ambigüedad durante la consulta.
