from flask import Flask, request, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/save_numbers', methods=['POST'])
def save_numbers():
    data = request.get_json()
    if 'numbers' in data:
        numbers = ", ".join(data['numbers'])
        with open('queue.txt', 'a') as f:
            f.write(numbers + "\n")
        return jsonify({"message": "Numbers saved successfully"}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
