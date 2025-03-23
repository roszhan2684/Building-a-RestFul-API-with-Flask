from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_mysqldb import MySQL
from .auth import auth as auth_bp
from .file_handler import file_bp
from .utils.error_handlers import register_error_handlers
from .routes.public_routes import public_bp
from .routes.admin_routes import admin_bp

mysql = MySQL()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    mysql.init_app(app)
    jwt.init_app(app)

    # Register blueprints with route prefixes
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(file_bp, url_prefix='/file')
    app.register_blueprint(public_bp, url_prefix='/public')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # Register error handlers
    register_error_handlers(app)

    # ✅ Add a Root Route so 127.0.0.1:5000/ doesn't show "Not Found"
    @app.route('/')
    def home():
        return jsonify({'message': 'Welcome to Flask API!'}), 200

    return app
