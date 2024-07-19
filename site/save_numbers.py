from flask import Flask, request, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

import re

@app.route('/save_numbers', methods=['POST'])
def save_numbers():
    data = request.get_json()
    if 'numbers' in data:
        numbers = data['numbers']
        if all(re.match(r'^[a-zA-Z_][a-zA-Z0-9_-]*$', number) for number in numbers):
            numbers_str = ", ".join(numbers)
            with open('queue.txt', 'a') as f:
                f.write(numbers_str + "\n")
            return jsonify({"message": "Numbers saved successfully"}), 200
        else:
            return jsonify({"error": "Invalid number format"}), 400
    else:
        return jsonify({"error": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
