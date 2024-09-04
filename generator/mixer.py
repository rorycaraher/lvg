import os
import random
import subprocess
from datetime import datetime
import ffmpeg

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
stems_dir = "/Users/rca/nltl/lvg-bucket/mp3/first-principles"
output_dir = "./output"
output_file = os.path.join(output_dir, f"combined_{timestamp}.mp3")

def choose_stems(directory, num_files=3):
    # List all WAV files in the directory
    stems = [f for f in os.listdir(directory) if f.endswith('.mp3')]
    
    # Select random files
    selected_files = random.sample(stems, num_files)
    selected_file_paths = [os.path.join(directory, file) for file in selected_files]
    
    return selected_file_paths

random_volumes = [round(random.uniform(0.5, 1), 1) for _ in range(3)]

# Define input MP3 files
input_files = choose_stems(stems_dir)


# Apply volume filters to each input file
streams = []
for i, input_file in enumerate(input_files):
    stream = (
        ffmpeg.input(input_file)
        .filter('volume', random_volumes[i])
    )
    streams.append(stream)

# Combine the inputs using amix
combined = (
    ffmpeg.filter(streams, 'amix', inputs=len(streams), duration='longest')
    .output(f'output/output-from-lib-{timestamp}.mp3', acodec='libmp3lame', audio_bitrate='192k')
)

# Run the ffmpeg command
ffmpeg.run(combined)
