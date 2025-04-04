# flask_api_project/app/utils/error_handlers.py
from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(error='Bad Request'), 400

    @app.errorhandler(401)
    def unauthorized(e):
        return jsonify(error='Unauthorized'), 401

    @app.errorhandler(404)
    def not_found(e):
        return jsonify(error='Not Found'), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify(error='Internal Server Error'), 500
