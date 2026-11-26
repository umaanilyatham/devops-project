
from flask import Flask, jsonify
from db import get_db_connection

# Create Flask application
app = Flask(__name__)

# Sample employee data


# Health check API
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Application is running"})

# Get all employees
@app.route("/employees", methods=["GET"])
def get_employees():
    connection=get_db_connection()
    cursor=connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    employees=cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(employees)

# Start Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
