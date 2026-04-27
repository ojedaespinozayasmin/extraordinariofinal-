from flask import jsonify
from models.student import Student

def register_routes(app):
    @app.route('/enrollments', methods=['GET'])
    def get_enrollments():
        """Lista todos los alumnos con sus cursos (ENDPOINT CLAVE)
        ---
        responses:
          200:
            description: Alumnos con sus cursos
            examples:
              application/json: [{"student": "Ana García", "courses": ["Python Basics", "Flask API"]}]
        """
        students = Student.query.all()
        result = []
        for student in students:
            result.append({
                'student': student.name,
                'courses': [c.name for c in student.courses]
            })
        return jsonify(result)
