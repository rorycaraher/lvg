from flask import Flask, request, jsonify, send_from_directory
import os
import sqlalchemy
from flask_cors import CORS
from google.cloud import pubsub_v1, storage
import json

app = Flask(__name__)
CORS(app)

# Initialize Pub/Sub client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('live-version-generator', 'level_values')

@app.route('/save_numbers', methods=['POST'])
def save_numbers():
    data = request.get_json()
    if 'lvg_values' in data:
    #     numbers = data['numbers']
    #     message_json = json.dumps({'numbers': numbers})
    #     message_bytes = message_json.encode('utf-8')
        
    #     # Publish message to Pub/Sub
    #     future = publisher.publish(topic_path, data=message_bytes)
    #     future.result()  # Ensure the message is published
        
        return jsonify({"message": "Numbers pushed to Pub/Sub successfully"}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400


# Database connection setup using Cloud SQL Auth Proxy
def init_db_connection():
    db_user = "db_user"
    db_pass = os.getenv("DB_PASS")
    db_name = "level_values_db"
    db_host = "127.0.0.1"  # Cloud SQL Auth Proxy runs on localhost

    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="postgresql+pg8000",
            username=db_user,
            password=db_pass,
            database=db_name,
            host=db_host,
            port=5432,  # Default port for PostgreSQL
            query={}
        )
    )
    return pool

db = init_db_connection()
app.run(debug=True)
