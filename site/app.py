from flask import Flask, request, jsonify, send_from_directory
from db_connection import init_db_connection
from flask_cors import CORS
from google.cloud import pubsub_v1
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

# Initialize Pub/Sub client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('live-version-generator', 'level_values')

@app.route('/save_numbers', methods=['POST'])
def save_numbers():
    data = request.get_json()
    if 'numbers' in data:
        numbers = data['numbers']
        message_json = json.dumps({'numbers': numbers})
        message_bytes = message_json.encode('utf-8')
        
        # Publish message to Pub/Sub
        future = publisher.publish(topic_path, data=message_bytes)
        future.result()  # Ensure the message is published
        
        return jsonify({"message": "Numbers pushed to Pub/Sub successfully"}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400


db = init_db_connection()
app.run(debug=True)
