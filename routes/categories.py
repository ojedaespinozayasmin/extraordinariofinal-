from flask import jsonify
from models.category import Category

def register_routes(app):
    @app.route('/categories', methods=['GET'])
    def get_categories():
        """Lista todas las categorías
        ---
        responses:
          200:
            description: Lista de categorías
            examples:
              application/json: [{"id": 1, "name": "Programming"}]
        """
        categories = Category.query.all()
        return jsonify([c.to_dict() for c in categories])

    @app.route('/categories/<int:id>/courses', methods=['GET'])
    def get_courses_by_category(id):
        """Obtiene los cursos de una categoría
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
        category = Category.query.get_or_404(id)
        return jsonify([c.to_dict() for c in category.courses])

    @app.route('/categories/<int:id>/courses/count', methods=['GET'])
    def count_courses_in_category(id):
        """Cuenta los cursos de una categoría
        ---
        parameters:
          - name: id
            in: path
            required: true
            type: integer
        responses:
          200:
            description: Conteo de cursos
        """
        category = Category.query.get_or_404(id)
        return jsonify({'category': category.name, 'total_courses': len(category.courses)})
