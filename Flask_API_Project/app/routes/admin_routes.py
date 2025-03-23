# flask_api_project/app/routes/admin_routes.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.crud_service import (
    get_all_items, get_item_by_id, add_item as add_item_service,
    update_item as update_item_service, delete_item as delete_item_service
)

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/items', methods=['GET'])
@jwt_required()
def get_items():
    items = get_all_items()
    return jsonify(items), 200

@admin_bp.route('/items', methods=['POST'])
@jwt_required()
def add_item():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'message': 'Item name is required'}), 400

    item_id = add_item_service(name, description)
    return jsonify({'message': 'Item added', 'item_id': item_id}), 201

@admin_bp.route('/items/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'message': 'Item name is required'}), 400

    success = update_item_service(item_id, name, description)
    if not success:
        return jsonify({'message': 'Update failed'}), 500

    return jsonify({'message': 'Item updated'}), 200

@admin_bp.route('/items/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    success = delete_item_service(item_id)
    if not success:
        return jsonify({'message': 'Delete failed'}), 500

    return jsonify({'message': 'Item deleted'}), 200
