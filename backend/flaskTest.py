from flask import Flask, request, jsonify
import sqlite3
from sqlite3 import Error
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def create_connection(database_file):
    conn = None
    try:
        conn = sqlite3.connect(database_file)
        print(f"Connected to SQLite version {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
        return None

def fetch_data(conn):
    cursor = conn.cursor()

    try:
        # Example SELECT query
        cursor.execute("SELECT * FROM users")
        
        columns = [column[0] for column in cursor.description]

        rows = cursor.fetchall()

        df = pd.DataFrame(rows, columns=columns)
        return df.to_dict(orient='records')
    except Error as e:
        print(e)
        return None
    finally:
        cursor.close()

@app.route('/get_data', methods=['GET'])
def get_data():
    conn = create_connection(r"F:\SQlite\sqlite-tools-win-x64-3440200\test.db")

    if conn:
        data = fetch_data(conn)
        conn.close()
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
