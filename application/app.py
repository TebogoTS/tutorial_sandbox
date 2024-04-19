from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Environment variables
db_host = os.getenv('DB_HOST', 'localhost')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', 'password')
db_database = os.getenv('DB_DATABASE', 'people_db')

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )
    return connection

@app.route('/')
def list_people():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM people;')
    people = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(people)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
