from flask import jsonify
from models.course import Course

def register_routes(app):
    @app.route('/courses', methods=['GET'])
    def get_courses():
        """Lista todos los cursos
        ---
        responses:
          200:
            description: Lista de cursos
        """
        courses = Course.query.all()
        return jsonify([c.to_dict() for c in courses])

    @app.route('/courses/<int:id>/students', methods=['GET'])
    def get_students_in_course(id):
        """Lista los alumnos inscritos en un curso
        ---
        parameters:
          - name: id
            in: path
            required: true
            type: integer
        responses:
          200:
            description: Lista de alumnos
        """
        course = Course.query.get_or_404(id)
        return jsonify([s.to_dict() for s in course.students])
