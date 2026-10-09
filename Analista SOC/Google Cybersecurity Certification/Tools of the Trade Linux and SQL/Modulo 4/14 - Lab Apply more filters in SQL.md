# Lab: Apply more filters in SQL

En esta actividad práctica de laboratorio, aprenderás a aplicar operadores de comparación numéricos, de fecha y de hora en consultas SQL sobre una base de datos MariaDB. Dominarás el uso de los operadores `=`, `>`, `<`, `<>`, `>=`, `<=` y la cláusula `BETWEEN ... AND ...`.

Como analista de ciberseguridad, filtrar datos numéricos y temporales es crucial durante la investigación de incidentes de seguridad. Te permite acotar las búsquedas a eventos ocurridos en ventanas de tiempo específicas, identificar inicios de sesión fuera del horario laboral habitual o examinar eventos por su identificador único (*event_id*).

---

## Introducción del Equipo de Ciberseguridad de Google

Al investigar un incidente de seguridad, rara vez trabajarás con conjuntos de datos pequeños. Lo habitual es analizar miles o millones de registros de acceso (*logs*). Utilizar operadores de filtrado avanzado en fechas, horas e identificadores te permite reducir drásticamente el volumen de datos a inspeccionar y concentrarte en la ventana exacta en la que se produjo la anomalía o la brecha.

---

## Resumen de Operadores de Comparación en SQL

| Operador | Significado | Ejemplos de Uso |
| :---: | :--- | :--- |
| `=` | Igual a | `WHERE login_date = '2022-05-09'` |
| `>` | Mayor que | `WHERE login_date > '2022-05-09'` |
| `<` | Menor que | `WHERE login_time < '07:00:00'` |
| `<>` o `!=` | Diferente de | `WHERE country <> 'USA'` |
| `>=` | Mayor o igual que | `WHERE event_id >= 100` |
| `<=` | Menor o igual que | `WHERE event_id <= 150` |
| `BETWEEN ... AND ...` | Entre un rango inclusivo | `WHERE login_date BETWEEN '2022-05-09' AND '2022-05-11'` |

> [!IMPORTANT]
> **Reglas de Formato para Tipos de Datos:**
> * **Fechas y Horas:** Se deben encerrar entre comillas simples utilizando el formato estándar ISO: `'AAAA-MM-DD'` para fechas y `'HH:MM:SS'` para horas.
> * **Valores Numéricos:** Los números (como `event_id`) **no** llevan comillas.

---

## Desarrollo Temático: Guía Paso a Paso del Laboratorio Práctico

### Escenario Operativo
Estás investigando un incidente de seguridad reciente en la organización. Debes analizar los intentos de inicio de sesión registrados en la tabla `log_in_attempts` filtrando por fechas, horas e identificadores de eventos para esclarecer el incidente.

---

### Tarea 1: Obtener Intentos de Inicio de Sesión Posteriores a una Fecha

Para comenzar la investigación, debes reunir información sobre los inicios de sesión realizados después del 9 de mayo de 2022.

1. **Selecciona todos los registros con `login_date` posterior a `'2022-05-09'`:**
   ```sql
   SELECT * FROM log_in_attempts WHERE login_date > '2022-05-09';
   ```

#### Pregunta de Evaluación - Tarea 1 (Parte 1)

**¿Cuántos intentos de inicio de sesión se realizaron después del 2022-05-09? (*How many login attempts were made after 2022-05-09?*)**
- [ ] 111
- [ ] 185
- [ ] 134
- [x] 125

2. **Amplía el rango para incluir también los eventos ocurridos el propio día `'2022-05-09'` utilizando el operador `>=`:**
   ```sql
   SELECT * FROM log_in_attempts WHERE login_date >= '2022-05-09';
   ```

#### Pregunta de Evaluación - Tarea 1 (Parte 2)

**¿Cuántos intentos de inicio de sesión se realizaron el 2022-05-09 o después? (*How many login attempts were made on or after 2022-05-09?*)**
- [ ] 186
- [ ] 143
- [x] 165
- [ ] 190

---

### Tarea 2: Obtener Inicios de Sesión en un Rango de Fechas (`BETWEEN ... AND ...`)

Ahora debes acotar la búsqueda para incluir únicamente los intentos realizados entre el 9 de mayo y el 11 de mayo de 2022.

1. **Filtra los registros comprendidos en el rango de fechas utilizando `BETWEEN` y `AND`:**
   ```sql
   SELECT * FROM log_in_attempts WHERE login_date BETWEEN '2022-05-09' AND '2022-05-11';
   ```

#### Pregunta de Evaluación - Tarea 2

**¿Cuántos intentos de inicio de sesión se realizaron entre el 2022-05-09 y el 2022-05-11? (*How many login attempts were made between 2022-05-09 and 2022-05-11?*)**
- [ ] 160
- [ ] 134
- [ ] 157
- [x] 123

---

### Tarea 3: Investigar Inicios de Sesión en Horarios Específicos

El horario laboral habitual de la organización comienza a las `07:00:00`. Debes analizar los inicios de sesión realizados antes de esa hora para detectar actividad fuera de horario.

1. **Selecciona los intentos de inicio de sesión ocurridos antes de las `'07:00:00'`:**
   ```sql
   SELECT * FROM log_in_attempts WHERE login_time < '07:00:00';
   ```

#### Pregunta de Evaluación - Tarea 3 (Parte 1)

**¿Cuál es el nombre de usuario del quinto registro devuelto en esta consulta? (*What is the username of the fifth record returned from this query?*)**
- [ ] bisles
- [x] eraab
- [ ] acook
- [ ] jrafael

2. **Refina la consulta para analizar únicamente el rango entre las `'06:00:00'` y las `'07:00:00'`:**
   ```sql
   SELECT * FROM log_in_attempts WHERE login_time BETWEEN '06:00:00' AND '07:00:00';
   ```

#### Pregunta de Evaluación - Tarea 3 (Parte 2)

**¿A qué hora ocurrió el intento de inicio de sesión más temprano entre las 06:00:00 y las 07:00:00? (*What time was the earliest login attempt between 06:00:00 and 07:00:00?*)**
- [ ] 06:04:34
- [ ] 06:15:41
- [x] 06:01:31
- [ ] 06:03:41

---

### Tarea 4: Investigar Inicios de Sesión por ID de Evento (`event_id`)

Analizarás los registros basándote en su número de identificador de evento (`event_id`). Seleccionarás solo los campos `event_id`, `username` y `login_date`.

1. **Selecciona los registros cuyo `event_id` sea mayor o igual a `100`:**
   ```sql
   SELECT event_id, username, login_date FROM log_in_attempts WHERE event_id >= 100;
   ```

#### Pregunta de Evaluación - Tarea 4 (Parte 1)

**¿Cuál es la fecha de inicio de sesión del tercer resultado devuelto? (*What is the login date of the third result returned by your query?*)**
- [ ] 2022-05-10
- [ ] 2022-05-08
- [x] 2022-05-09
- [ ] 2022-05-11

2. **Acota los resultados para mostrar únicamente los eventos con `event_id` entre `100` y `150`:**
   ```sql
   SELECT event_id, username, login_date FROM log_in_attempts WHERE event_id BETWEEN 100 AND 150;
   ```

#### Pregunta de Evaluación - Tarea 4 (Parte 2)

**¿Cuál es el nombre de usuario del séptimo resultado devuelto por la consulta? (*What is the username of the seventh result returned by your query?*)**
- [x] tmitchel
- [ ] mabadi
- [ ] bisles
- [ ] gesparza

---

## Puntos Clave (Key Takeaways)

* **Operadores Lógicos y de Rango:** `BETWEEN ... AND ...` incluye los valores límite del rango (es inclusivo) y simplifica consultas que requerirían combinar `>=` y `<=`.
* **Formato de Fechas y Horas en SQL:** Las cadenas de fecha (`'YYYY-MM-DD'`) y hora (`'HH:MM:SS'`) requieren siempre comillas simples.
* **Manejo de Datos Numéricos:** Los identificadores o valores de tipo entero (`int`), como `event_id`, no llevan comillas simples en las cláusulas `WHERE`.
* **Investigación de Incidentes:** Filtrar por horas tempranas (ej. `< '07:00:00'`) es una técnica común para detectar accesos no autorizados fuera del horario laboral.
