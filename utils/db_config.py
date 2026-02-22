import sqlite3
from sqlite3 import Error

def get_db_connection():
    """
    Establish a connection to the SQLite database.
    """
    try:
        connection = sqlite3.connect('disease_prediction.db')
        return connection
    except Error as e:
        print(f"Error connecting to SQLite: {e}")
        return None

def create_table():
    """
    Create the predictions table if it doesn't exist.
    """
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symptoms TEXT,
                predicted_disease TEXT,
                probability REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        connection.commit()
        cursor.close()
        connection.close()