from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proyecto_academy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SWAGGER'] = {'title': 'API Academia', 'uiversion': 3, 'specs_route': '/docs'}

db = SQLAlchemy(app)
swagger = Swagger(app)

# Modelos
class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    courses = db.relationship('Course', backref='category', lazy=True)

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    courses = db.relationship('Course', secondary='enrollment', backref='students')

class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)

# Endpoints
@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify([{'id': c.id, 'name': c.name} for c in Category.query.all()])

@app.route('/categories/<int:id>/courses', methods=['GET'])
def get_courses_by_category(id):
    category = Category.query.get_or_404(id)
    return jsonify([{'id': c.id, 'name': c.name} for c in category.courses])

@app.route('/categories/<int:id>/courses/count', methods=['GET'])
def count_courses_in_category(id):
    category = Category.query.get_or_404(id)
    return jsonify({'category': category.name, 'total_courses': len(category.courses)})

@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify([{'id': c.id, 'name': c.name, 'category_id': c.category_id} for c in Course.query.all()])

@app.route('/courses/<int:id>/students', methods=['GET'])
def get_students_in_course(id):
    course = Course.query.get_or_404(id)
    return jsonify([{'id': s.id, 'name': s.name} for s in course.students])

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify([{'id': s.id, 'name': s.name} for s in Student.query.all()])

@app.route('/students/<int:id>/courses', methods=['GET'])
def get_courses_of_student(id):
    student = Student.query.get_or_404(id)
    return jsonify([{'id': c.id, 'name': c.name} for c in student.courses])

@app.route('/enrollments', methods=['GET'])
def get_enrollments():
    result = []
    for student in Student.query.all():
        result.append({
            'student': student.name,
            'courses': [c.name for c in student.courses]
        })
    return jsonify(result)

if __name__ == '__main__':
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
