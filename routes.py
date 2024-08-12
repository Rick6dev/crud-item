from flask import Blueprint,request,jsonify
from models import db,Item

bp=Blueprint('api',__name__);


@bp.route('/items',methods=['POST'])
def create_item():
    data =request.json
    new_item =Item(nombre_item=data['nombre_item'],descripcion_item=data['descripcion_item']);
    db.session.add(new_item);
    db.session.commit();
    return jsonify({'id_item':new_item.id_item}),201

@bp.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id_item, 'nombre': item.nombre_item,'descripcion':item.descripcion_item} for item in items])

@bp.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.json
    item = Item.query.get_or_404(id)
    item.nombre = data['nombre_item']
    db.session.commit()
    return jsonify({'id': item.id_item})

@bp.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'result': True})