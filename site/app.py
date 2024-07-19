from flask import Flask, request, jsonify, send_from_directory
import os
import sqlalchemy
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

# Database connection setup
def init_db_connection():
    db_user = "db_user"
    db_name = "level_values_db"
    db_connection_name = os.getenv("DB_CONNECTION_NAME")

    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="postgresql+pg8000",
            username=db_user,
            database=db_name,
            query={
                "unix_sock": f"/cloudsql/{db_connection_name}/.s.PGSQL.5432"
            }
        )
    )
    return pool

db = init_db_connection()
app.run(debug=True)
