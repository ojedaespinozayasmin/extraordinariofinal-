from models import db

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'category_id': self.category_id}
