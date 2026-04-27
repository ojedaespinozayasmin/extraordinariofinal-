from flask import jsonify
from models.student import Student

def register_routes(app):
    @app.route('/enrollments', methods=['GET'])
    def get_enrollments():
        students = Student.query.all()
        result = []
        for student in students:
            result.append({
                'student': student.name,
                'courses': [c.name for c in student.courses]
            })
        return jsonify(result)
