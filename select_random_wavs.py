import os
import random
import subprocess

def select_random_wavs(directory, num_files=4):
    # List all WAV files in the directory
    wav_files = [f for f in os.listdir(directory) if f.endswith('.wav')]
    
    # Select random files
    selected_files = random.sample(wav_files, num_files)
    
    return selected_files

def main():
    directory = "./seeds/amy-01"
    selected_files = select_random_wavs(directory)
    
    for file in selected_files:
        file_path = os.path.join(directory, file)
        print(f"Selected {file_path}")
        # Example command to process the file with ffmpeg
        # subprocess.run(["ffmpeg", "-i", file_path, "output_file"])

if __name__ == "__main__":
    main()
