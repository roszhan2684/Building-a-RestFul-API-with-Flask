# flask_api_project/app/file_handler.py
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required
import os
from werkzeug.utils import secure_filename

file_bp = Blueprint('file', __name__)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@file_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

        if len(file.read()) > current_app.config['MAX_CONTENT_LENGTH']:
            return jsonify({'error': 'File size exceeds limit'}), 400

        file.seek(0)  # reset file pointer after size check
        file.save(filepath)
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200
    else:
        return jsonify({'error': 'Invalid file type'}), 400
