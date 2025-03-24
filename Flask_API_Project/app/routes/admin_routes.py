# flask_api_project/app/routes/admin_routes.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import get_all_items, update_item_by_id, delete_item_by_id, insert_item
from MySQLdb import DatabaseError

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

    item_id = insert_item(name, description)
    return jsonify({'message': 'Item added', 'item_id': item_id}), 201

@admin_bp.route('/items/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')

        if not name:
            return jsonify({'message': 'Item name is required'}), 400

        success = update_item_by_id(item_id, name, description)
        if not success:
            return jsonify({'message': 'Update failed'}), 500

        return jsonify({'message': 'Item updated'}), 200

    except DatabaseError as e:
            # Log the error for debugging
            print(f"Database error occurred: {e}")
            return jsonify({'message': 'Database error occurred'}), 500
    except Exception as e:
            # Log unexpected errors
            print(f"Unexpected error occurred: {e}")
            return jsonify({'message': 'An unexpected error occurred'}), 500

@admin_bp.route('/items/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    success = delete_item_by_id(item_id)
    if not success:
        return jsonify({'message': 'Delete failed'}), 500

    return jsonify({'message': 'Item deleted'}), 200

@admin_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def homepage():
    return jsonify({'message': 'Welcome to the dashboard'}), 200