from flask import Flask, request, jsonify, send_from_directory
import os
import sqlalchemy
from flask_cors import CORS
from google.cloud import pubsub_v1, storage
import json
from datetime import datetime
# mixdown stuff
from mixer import mixer

app = Flask(__name__,
            static_url_path='', 
            static_folder='site'
            )
CORS(app)

mixer = mixer.Mixer()
stems_dir = "/Users/rca/nltl/lvg-bucket/mp3/first-principles"
output_dir = "./output"


@app.route('/test_values', methods=['POST'])
def test_values():
    data = request.get_json()
    if 'lvg_values' in data:
        stems = data['lvg_values']['stems']
        volumes = data['lvg_values']['volumes'][0:len(stems)] # only need volume for each stem
        rounded_volumes = [round(i, 3) for i in volumes]
        print(f"Worked! {rounded_volumes}")
        return jsonify({"message": f"Success! {data}"}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400

@app.route('/test_mixdown', methods=['POST'])
def test_mixdown():
    data = request.get_json()
    if 'lvg_values' in data:
        stems = data['lvg_values']['stems']
        volumes = data['lvg_values']['volumes'][0:len(stems)] # only need volume for each stem
        rounded_volumes = [round(i, 3) for i in volumes]
        input_files = mixer.get_stems(stems_dir, stems)
        mixer.create_mixdown(input_files, rounded_volumes)
        return jsonify({"message": f"Success! {data}"}), 200
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
