import sqlite3
import sqlalchemy

def open_connection():
    connection = sqlite3.connect('ingredients.db')
    return connection

def close_connection(connection):
    connection.commit()
    connection.close()

def initialize_database():
    conn = open_connection()
    conn.execute('''CREATE TABLE ingredients (name TEXT, quantity REAL, unit TEXT, cost REAL, unit_cost REAL)''')
    close_connection(conn)

initialize_database()