import os
from google.cloud import pubsub_v1
import json
import os
from select_random_wavs import select_random_wavs, combine_wavs
import subprocess
from datetime import datetime

# Set up the subscriber
project_id = "live-version-generator"
subscription_id = "level_values-sub"
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message):
    print(f"Received message: {message.data}")
    data = json.loads(message.data)
    if 'numbers' in data:
        numbers = data['numbers']
        directory = "./generator/seeds/amy-01"
        selected_files = select_random_wavs(directory)
        selected_file_paths = [os.path.join(directory, file) for file in selected_files]
        output_dir = "./output"
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        output_file = os.path.join(output_dir, f"combined_{timestamp}.wav")
        
        # Set volumes according to the values from the queue
        temp_files = []
        for file, volume in zip(selected_file_paths, numbers):
            temp_file = f"temp_{os.path.basename(file)}"
            temp_files.append(temp_file)
            subprocess.run([
                "ffmpeg", "-i", file, "-filter:a", f"volume={volume}", temp_file
            ])
        
        ffmpeg_command = ["ffmpeg"]
        for temp_file in temp_files:
            ffmpeg_command.extend(["-i", temp_file])
        
        filter_complex = f"amix=inputs={len(temp_files)}:duration=longest, aecho=0.8:0.9:1000:0.3"
        ffmpeg_command.extend(["-filter_complex", filter_complex, output_file])
        
        subprocess.run(ffmpeg_command)
        for file in temp_files:
            os.remove(file)
        
        print(f"Combined file saved as {output_file}")
    message.ack()

# Listen for messages on the subscription
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}..\n")

try:
    streaming_pull_future.result()
except KeyboardInterrupt:
    streaming_pull_future.cancel()
