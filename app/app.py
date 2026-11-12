
from flask import Flask, jsonify

# Create Flask application
app = Flask(__name__)

# Sample employee data
employees = [
    {"id": 1, "name": "Anil", "role": "Python Developer"},
    {"id": 2, "name": "Ravi", "role": "DevOps Engineer"}
]

# Health check API
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Application is running"})

# Get all employees
@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)

# Start Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
