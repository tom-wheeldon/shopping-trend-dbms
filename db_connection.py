import mysql.connector
from config import DB_CONFIG

def get_db_connection():
    conn = mysql.connector.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database']
    )
    if conn.is_connected():
        print("Connected to the database")
        return conn
    else:
        raise Exception("Connection failed")
