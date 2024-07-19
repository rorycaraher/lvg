import numpy as np
import wave
import struct
import os

# Constants
SAMPLE_RATE = 44100  # samples per second
DURATION = 1.0       # seconds
AMPLITUDE = 16000    # amplitude of the wave

# Frequencies of one octave of the chromatic scale starting from middle C (C4)
FREQUENCIES = [
    261.63,  # C4
    277.18,  # C#4/Db4
    293.66,  # D4
    311.13,  # D#4/Eb4
    329.63,  # E4
    349.23,  # F4
    369.99,  # F#4/Gb4
    392.00,  # G4
    415.30,  # G#4/Ab4
    440.00,  # A4
    466.16,  # A#4/Bb4
    493.88   # B4
]

def generate_sine_wave(frequency, duration, sample_rate, amplitude):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return wave

def save_wave(filename, wave_data, sample_rate):
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)  # mono
        wf.setsampwidth(2)  # two bytes per sample
        wf.setframerate(sample_rate)
        for sample in wave_data:
            wf.writeframes(struct.pack('h', int(sample)))

def main():
    output_dir = "./seeds/amy-01"
    os.makedirs(output_dir, exist_ok=True)
    
    for i, freq in enumerate(FREQUENCIES):
        wave_data = generate_sine_wave(freq, DURATION, SAMPLE_RATE, AMPLITUDE)
        filename = os.path.join(output_dir, f"sine_{i+1}_{freq:.2f}Hz.wav")
        save_wave(filename, wave_data, SAMPLE_RATE)
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()
