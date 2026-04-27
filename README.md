

# 🎓 API Académica - Manual de Uso

¡Hola! Bienvenido a mi proyecto. Aquí te explico de forma sencilla qué hace esta API y cómo puedes usarla sin complicaciones.

---

## 📌 ¿Qué es esto?

Es un sistema que desarrollé para gestionar información escolar de forma práctica. Básicamente, sirve para organizar:

*   📂 **Categorías** (Áreas de estudio)
*   📚 **Cursos** (Las materias)
*   👨‍🎓 **Alumnos** (Los estudiantes)

Y lo mejor: conecta todo automáticamente. Sabe qué curso pertenece a qué categoría y qué alumnos están inscritos en cada clase.

---

## 🛠 ¿Qué necesitas para que funcione?

Solo asegúrate de tener instalado:

*   **Python** (Versión 3.9 o superior)
*   **Git** (Para descargar el código)

Todo lo demás se instala automático con los archivos del proyecto.

---

## 🚀 ¿Cómo lo instalo y lo echo a andar?

Sigue estos pasos sencillos en tu terminal:

### 1️⃣ Descargar el proyecto
```bash
git clone https://github.comojedaespinozayasminextraordinario2.git
cd flask_academy_api
```

### 2️⃣ Instalar lo necesario
```bash
pip install -r requirements.txt
```

### 3️⃣ Crear la base de datos
Ejecuta el script `schema.sql` para crear las tablas y luego `seed.sql` para que se llenen automáticamente con datos de ejemplo (Categorías, Cursos y Alumnos listos para probar).

### 4️⃣ ¡Encender el servidor!
```bash
python app.py
```

Listo ✅. El sistema ya está corriendo en tu computadora.

---

## 📝 ¿Cómo lo uso?

Todo se controla mediante direcciones web (endpoints). Aquí te dejo las principales:

### 📂 Ver Categorías y Cursos
*   `GET /categories` -> Ve todas las áreas de estudio.
*   `GET /categories/1/courses` -> Ve los cursos que hay dentro de una categoría.
*   `GET /categories/1/courses/count` -> Mira cuántos cursos hay en total.

### 📚 Ver Información de Clases
*   `GET /courses` -> Lista de todos los cursos disponibles.
*   `GET /courses/1/students` -> Quiénes están inscritos en ese curso.

### 👨‍🎓 Ver Alumnos
*   `GET /students` -> Todos los alumnos registrados.
*   `GET /students/1/courses` -> En qué cursos está inscrito un alumno.

### 📋 Ver Inscripciones (El punto clave)
*   `GET /enrollments`
    *   Aquí ves un resumen claro: **Alumno** y la lista de **Cursos** que lleva.

---

## 📄 ¿Dónde veo la documentación?

Super fácil. Abrí tu navegador y escribe:

🌐 **`http://localhost:8000/docs`**

Ahí vas a encontrar toda la interfaz gráfica de **Swagger** para probar cada opción sin escribir código, solo dándole clic a "Try it out".

---

## 📂 ¿Qué archivos trae este proyecto?

*   **`app.py`**: El código principal de la aplicación.
*   **`schema.sql`**: Aquí está la estructura de la base de datos.
*   **`seed.sql`**: Los datos de prueba para empezar a usarla rápido.
*   **`requirements.txt`**: La lista de programas necesarios.
*   **`README.md`**: Este instructivo que estás leyendo 😉.

---

## ✅ Notas importantes

*   El proyecto usa el **puerto 8000** para evitar conflictos con otros programas.


---
