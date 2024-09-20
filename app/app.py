from flask import Flask, request, jsonify, send_from_directory
import os
from flask_cors import CORS
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

app.run(debug=True)
