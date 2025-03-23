# Flask RESTful API - Mid Project

## Title:
Building a RESTful API with Flask - Error Handling, Authentication, and File Handling with Public and Admin Routes

## Team Members:
- Roszhan Raj Meenakshi Sundhresan
- Member 2 Name
- Member 3 Name

## Features Implemented:
- JWT Authentication (Login/Register)
- Public and Admin Routes
- File Upload (with validation)
- MySQL Database Integration
- Error Handling for 400, 401, 404, 500
- CRUD Operations for Items

## Technologies Used:
- Flask
- Flask-JWT-Extended
- Flask-MySQLdb
- Python
- MySQL

## Setup Instructions:

1. **Clone the Repository**
```bash
git clone <your-repo-link>
cd flask_api_project
```

2. **Create Virtual Environment and Install Requirements**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

3. **Configure MySQL Database**
Create a database named `flaskapi` and run `schema.sql` in your MySQL client.

4. **Set Environment Variables (Optional)**
Create a `.env` file and add:
```
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=flaskapi
```

5. **Run the Application**
```bash
python run.py
```

6. **Test Endpoints with POSTMAN**
- `/register`, `/login` - Auth
- `/admin-only` - JWT protected
- `/upload` - File upload
- `/public-items` - Public access
- `/items` - CRUD

## Deliverables
- ✅ GitHub Repo with Source Code
- ✅ `requirements.txt`
- ✅ Screenshot of Postman
- ✅ Demo Video showing login and file upload endpoints

---

Feel free to reach out with questions or issues!

Happy Coding! 🚀