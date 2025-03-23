# Building-a-RestFul-API-with-Flask
Web Backend Project
Absolutely! Here's a `README.md` you can use for your Flask API project. It documents setup, usage, endpoints, and more.

---

```markdown
# 🔐 Flask API with JWT Authentication & MySQL

A secure RESTful API built with **Flask**, **MySQL**, and **JWT Authentication** to handle user registration, login, and protected routes.

---

## 📁 Project Structure

```
Flask_API_Project/
│
├── app/
│   ├── __init__.py       # App factory & configuration
│   ├── auth.py           # Authentication routes (register, login)
│   ├── models.py         # Database helper functions
│
├── config.py             # Configuration for Flask & MySQL
├── run.py                # Entry point for running the Flask app
├── uploads/              # Folder to store uploaded files (if needed)
├── venv/                 # Python virtual environment
└── README.md             # You're reading this 🙂
```

---

## 🚀 Features

- ✅ User registration
- ✅ Secure password hashing (via `werkzeug.security`)
- ✅ JWT-based login system
- ✅ MySQL database integration
- ✅ Protected routes support
- ✅ File upload support (config-ready)

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Flask_API_Project.git
cd Flask_API_Project
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> If `requirements.txt` doesn't exist, manually install:
```bash
pip install flask flask-jwt-extended flask-mysqldb werkzeug
```

### 4. Configure MySQL

Make sure MySQL is running. Create the database:

```sql
CREATE DATABASE roszhan_api;

USE roszhan_api;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);
```

> ✅ No password for `root` user? Leave the `MYSQL_PASSWORD` as an empty string in `config.py`.

---

## 🔑 Environment Configuration

Update `config.py`:

```python
class Config:
    SECRET_KEY = 'your_secret_key'
    JWT_SECRET_KEY = 'your_jwt_secret'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''         # Leave blank if no password
    MYSQL_DB = 'roszhan_api'
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
```

---

## ▶️ Running the App

```bash
python run.py
```

The API will be available at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📬 API Endpoints

### 🔹 Register a user
**POST** `/auth/register`

**Body:**
```json
{
  "username": "roszhan",
  "password": "2684"
}
```

---

### 🔹 Login and receive JWT
**POST** `/auth/login`

**Body:**
```json
{
  "username": "roszhan",
  "password": "2684"
}
```

**Response:**
```json
{
  "access_token": "JWT_TOKEN_HERE"
}
```

---

### 🔒 Protected Route (Example)
Add your own protected route like:

```python
from flask_jwt_extended import jwt_required

@app.route('/dashboard')
@jwt_required()
def dashboard():
    return jsonify(message="Welcome to your dashboard!")
```

---

## 🧪 Testing

Use **Postman** or **cURL** to test the endpoints.

---

## 📌 Notes

- All passwords are hashed using `werkzeug.security.generate_password_hash`.
- JWT tokens are returned on successful login.
- Use tokens to access any protected routes using the `Authorization: Bearer <token>` header.

---

## 👨‍💻 Author

**Roszhan Raj Meenakshi Sundhresan**

---

## 🏁 License

This project is licensed under the MIT License.
```

---

Would you like me to generate a `requirements.txt` file too based on your dependencies?
