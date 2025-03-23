# flask_api_project/app/models.py
import MySQLdb.cursors

def get_user_by_username(username):
    from . import mysql
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user = cursor.fetchone()
    cursor.close()
    return user

def insert_user(username, hashed_password):
    from . import mysql
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
    mysql.connection.commit()
    cursor.close()

def get_all_items():
    from . import mysql
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    cursor.close()
    return items

def update_item_by_id(item_id, name, type_):
    from . import mysql
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE items SET name=%s, type=%s WHERE id=%s', (name, type_, item_id))
    mysql.connection.commit()
    cursor.close()

def delete_item_by_id(item_id):
    from . import mysql
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM items WHERE id=%s', (item_id,))
    mysql.connection.commit()
    cursor.close()
