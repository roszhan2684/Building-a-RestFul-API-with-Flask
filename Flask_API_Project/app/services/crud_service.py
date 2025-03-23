# app/services/crud_service.py

import pymysql.cursors

def get_all_items():
    from .. import mysql
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    cursor.close()
    return items

def get_item_by_id(item_id):
    from .. import mysql
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
    item = cursor.fetchone()
    cursor.close()
    return item

def add_item(name, description):
    from .. import mysql
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (name, description))
    mysql.connection.commit()
    cursor.close()
    return cursor.lastrowid

def update_item(item_id, name, description):
    from .. import mysql
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE items SET name = %s, description = %s WHERE id = %s", (name, description, item_id))
    mysql.connection.commit()
    cursor.close()
    return True

def delete_item(item_id):
    from .. import mysql
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
    mysql.connection.commit()
    cursor.close()
    return True
