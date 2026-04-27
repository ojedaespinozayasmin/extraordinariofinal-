from flask import jsonify
from models.student import Student

def register_routes(app):
    @app.route('/students', methods=['GET'])
    def get_students():
        students = Student.query.all()
        return jsonify([s.to_dict() for s in students])

    @app.route('/students/<int:id>/courses', methods=['GET'])
    def get_courses_of_student(id):
        student = Student.query.get_or_404(id)
        return jsonify([c.to_dict() for c in student.courses])
