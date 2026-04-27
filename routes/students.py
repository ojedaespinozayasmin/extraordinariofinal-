from flask import jsonify
from models.student import Student

def register_routes(app):
    @app.route('/students', methods=['GET'])
    def get_students():
        """Lista todos los alumnos
        ---
        responses:
          200:
            description: Lista de alumnos
        """
        students = Student.query.all()
        return jsonify([s.to_dict() for s in students])

    @app.route('/students/<int:id>/courses', methods=['GET'])
    def get_courses_of_student(id):
        """Lista los cursos de un alumno
        ---
        parameters:
          - name: id
            in: path
            required: true
            type: integer
        responses:
          200:
            description: Lista de cursos
        """
        student = Student.query.get_or_404(id)
        return jsonify([c.to_dict() for c in student.courses])
