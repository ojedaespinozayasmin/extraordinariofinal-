from flask import jsonify
from models.category import Category

def register_routes(app):
    @app.route('/categories', methods=['GET'])
    def get_categories():
        categories = Category.query.all()
        return jsonify([c.to_dict() for c in categories])

    @app.route('/categories/<int:id>/courses', methods=['GET'])
    def get_courses_by_category(id):
        category = Category.query.get_or_404(id)
        return jsonify([c.to_dict() for c in category.courses])

    @app.route('/categories/<int:id>/courses/count', methods=['GET'])
    def count_courses_in_category(id):
        category = Category.query.get_or_404(id)
        return jsonify({'category': category.name, 'total_courses': len(category.courses)})
