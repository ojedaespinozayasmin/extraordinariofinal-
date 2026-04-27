from flask import Flask
from flasgger import Swagger
from config import Config
from models import db

# Importar modelos para que SQLAlchemy los reconozca
from models.category import Category
from models.course import Course
from models.student import Student
from models.enrollment import Enrollment

# Importar rutas
from routes.categories import register_routes as register_categories
from routes.courses import register_routes as register_courses
from routes.students import register_routes as register_students
from routes.enrollments import register_routes as register_enrollments

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar extensiones
    db.init_app(app)
    
    # Configurar Swagger
    app.config['SWAGGER'] = {
        'title': 'API Academia',
        'uiversion': 3,
        'specs_route': '/docs'
    }
    Swagger(app)
    
    # Registrar rutas
    register_categories(app)
    register_courses(app)
    register_students(app)
    register_enrollments(app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    
    with app.app_context():
        db.create_all()
        
        # Insertar datos si no hay
        if Category.query.count() == 0:
            # Categorías
            prog = Category(name='Programming')
            data = Category(name='Data Science')
            db.session.add_all([prog, data])
            db.session.commit()
            
            # Cursos
            cursos = [
                Course(name='Python Basics', category_id=1),
                Course(name='Flask API', category_id=1),
                Course(name='Django', category_id=1),
                Course(name='JavaScript', category_id=1),
                Course(name='React', category_id=1),
                Course(name='Machine Learning', category_id=2),
                Course(name='Pandas', category_id=2),
                Course(name='Data Viz', category_id=2),
                Course(name='Statistics', category_id=2),
                Course(name='SQL for Data', category_id=2),
            ]
            db.session.add_all(cursos)
            db.session.commit()
            
            # Alumnos
            alumnos = [
                Student(name='Ana García'), Student(name='Luis Martínez'),
                Student(name='Carla Rodríguez'), Student(name='Jorge López'),
                Student(name='María Fernández'), Student(name='Carlos Sánchez'),
                Student(name='Laura Gómez'), Student(name='Pedro Díaz'),
                Student(name='Sofía Ruiz'), Student(name='Diego Torres'),
            ]
            db.session.add_all(alumnos)
            db.session.commit()
            
            # Inscripciones
            enrollments = [
                Enrollment(student_id=1, course_id=1),
                Enrollment(student_id=1, course_id=2),
                Enrollment(student_id=1, course_id=6),
                Enrollment(student_id=2, course_id=2),
                Enrollment(student_id=2, course_id=3),
                Enrollment(student_id=2, course_id=7),
                Enrollment(student_id=3, course_id=1),
                Enrollment(student_id=3, course_id=4),
                Enrollment(student_id=3, course_id=8),
                Enrollment(student_id=4, course_id=5),
                Enrollment(student_id=4, course_id=9),
                Enrollment(student_id=5, course_id=6),
                Enrollment(student_id=5, course_id=10),
                Enrollment(student_id=6, course_id=2),
                Enrollment(student_id=6, course_id=7),
                Enrollment(student_id=7, course_id=3),
                Enrollment(student_id=7, course_id=8),
                Enrollment(student_id=7, course_id=1),
                Enrollment(student_id=8, course_id=4),
                Enrollment(student_id=8, course_id=9),
                Enrollment(student_id=9, course_id=5),
                Enrollment(student_id=9, course_id=10),
                Enrollment(student_id=10, course_id=1),
                Enrollment(student_id=10, course_id=2),
                Enrollment(student_id=10, course_id=6),
            ]
            db.session.add_all(enrollments)
            db.session.commit()
            print("✅ Datos de prueba insertados")
    
    app.run(debug=True, port=8000, host='0.0.0.0')
