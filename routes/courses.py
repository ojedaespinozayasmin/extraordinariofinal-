from flask import jsonify
from models.course import Course
from models.student import Student

def register_routes(app):
    @app.route('/courses', methods=['GET'])
    def get_courses():
        courses = Course.query.all()
        return jsonify([c.to_dict() for c in courses])

    @app.route('/courses/<int:id>/students', methods=['GET'])
    def get_students_in_course(id):
        course = Course.query.get_or_404(id)
        return jsonify([s.to_dict() for s in course.students])
