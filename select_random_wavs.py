import os
import random
import subprocess

def select_random_wavs(directory, num_files=4):
    # List all WAV files in the directory
    wav_files = [f for f in os.listdir(directory) if f.endswith('.wav')]
    
    # Select random files
    selected_files = random.sample(wav_files, num_files)
    
    return selected_files

def combine_wavs(input_files, output_file):
    temp_files = []
    for file in input_files:
        volume = random.uniform(0.5, 1.5)  # Random volume between 0.5 and 1.5
        temp_file = f"temp_{os.path.basename(file)}"
        temp_files.append(temp_file)
        subprocess.run([
            "ffmpeg", "-i", file, "-filter:a", f"volume={volume}", temp_file
        ])
    
    with open("input_files.txt", "w") as f:
        for file in temp_files:
            f.write(f"file '{file}'\n")
    
    subprocess.run([
        "ffmpeg", "-f", "concat", "-safe", "0", "-i", "input_files.txt",
        "-filter_complex", "aecho=0.8:0.9:1000:0.3", output_file
    ])
    
    os.remove("input_files.txt")
    for file in temp_files:
        os.remove(file)
def main():
    directory = "./seeds/amy-01"
    selected_files = select_random_wavs(directory)

    selected_file_paths = [os.path.join(directory, file) for file in selected_files]
    output_file = os.path.join(directory, "combined_hot.wav")
    combine_wavs(selected_file_paths, output_file)
    print(f"Combined file saved as {output_file}")

if __name__ == "__main__":
    main()
