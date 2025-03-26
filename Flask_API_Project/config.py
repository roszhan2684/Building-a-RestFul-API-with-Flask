# # config.py
# import os

# class Config:
#     # Security Keys
#     SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
#     JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret')

#     # MySQL Configuration
#     MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
#     MYSQL_USER = os.getenv('MYSQL_USER', 'root')
#     MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '2684')  # ✅ Actual password
#     MYSQL_DB = os.getenv('MYSQL_DB', 'roszhan_api')       # ✅ Your DB

#     # Upload settings
#     UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
#     MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2MB
#     ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
# config.py
import os

class Config:
    SECRET_KEY = 'your_secret_key'
    JWT_SECRET_KEY = 'your_jwt_secret'
    
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''        # ← EMPTY string since there's no password
    MYSQL_DB = 'roszhan_api'

    UPLOAD_FOLDER = os.path.join(os.getcwd(),'app' ,'uploads')
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
