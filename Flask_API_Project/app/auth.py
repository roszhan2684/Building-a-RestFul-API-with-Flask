# flask_api_project/app/auth.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import get_user_by_username, insert_user

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    from . import mysql
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400

    if get_user_by_username(username):
        return jsonify({'message': 'User already exists'}), 400

    hashed_password = generate_password_hash(password)
    insert_user(username, hashed_password)
    return jsonify({'message': 'User registered successfully'}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = get_user_by_username(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=username)
    return jsonify({'token': access_token}), 200

