import os
import random
import subprocess
from datetime import datetime
from generate_sine_waves import list_current_directory

def select_random_wavs(directory, num_files=4):
    # List all WAV files in the directory
    wav_files = [f for f in os.listdir(directory) if f.endswith('.wav')]
    
    # Select random files
    selected_files = random.sample(wav_files, num_files)
    
    return selected_files

def combine_wavs(input_files, output_file):
    temp_files = []
    for file in input_files:
        volume = random.uniform(0.5, 1.0)  # Random volume between 0.5 and 1.0
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
def list_files(directory):
    files = os.listdir(directory)
    for file in files:
        print(file)

def main():
    directory = "./seeds/amy-01"
    print("Listing files in directory:")
    list_files(directory)
    output_dir = "./output"
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    selected_files = select_random_wavs(directory)

    selected_file_paths = [os.path.join(directory, file) for file in selected_files]
    output_file = os.path.join(output_dir, f"combined_hot_{timestamp}.wav")
    with open("queue-example.txt", "a") as f:
        f.write(", ".join([os.path.basename(file) for file in selected_file_paths]) + "\n")
    combine_wavs(selected_file_paths, output_file)
    print(f"Combined file saved as {output_file}")

if __name__ == "__main__":
    print("Listing files in the current directory:")
    list_current_directory()
    main()
