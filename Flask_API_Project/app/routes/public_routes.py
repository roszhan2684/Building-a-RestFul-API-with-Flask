# flask_api_project/app/routes/public_routes.py
from flask import Blueprint, jsonify

public_bp = Blueprint('public', __name__)

@public_bp.route('/public-items', methods=['GET'])
def public_items():
    items = [
        {"id": 1, "name": "Free eBook", "type": "Resource"},
        {"id": 2, "name": "Upcoming Events", "type": "Announcement"},
        {"id": 3, "name": "API Documentation", "type": "Info"}
    ]
    return jsonify({'public_items': items}), 200

