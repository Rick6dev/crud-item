from  flask_sqlalchemy  import SQLAlchemy

db =SQLAlchemy();

class Item(db.Model):
    id_item =db.Column(db.Integer,primary_key=True)
    nombre_item=db.Column(db.String(),nullable=False)
    descripcion_item =db.Column(db.String(),nullable=False)

    def __repr__(self):
        return f'<Item {self.nombre_item}>'
