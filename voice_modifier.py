import librosa
import soundfile as sf
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Load the input audio
input_file = "input.wav"
y, sr = librosa.load(input_file, sr=None)

# User input
speed_factor = float(input("Enter speed factor (e.g., 0.5 for slow, 2 for fast): "))
pitch_steps = int(input("Enter pitch shift in semitones (e.g., +5 or -5): "))

# Create label and timestamp
label = f"speed{speed_factor}_pitch{pitch_steps}"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Modify audio
y_speed = librosa.effects.time_stretch(y, rate=speed_factor)
y_pitch = librosa.effects.pitch_shift(y, sr=sr, n_steps=pitch_steps)
y_combined = librosa.effects.pitch_shift(y_speed, sr=sr, n_steps=pitch_steps)

# File names
out_speed = f"output_speed_{label}_{timestamp}.wav"
out_pitch = f"output_pitch_{label}_{timestamp}.wav"
out_combined = f"output_combined_{label}_{timestamp}.wav"
plot_file = f"waveform_{label}_{timestamp}.png"

# Save files
sf.write(out_speed, y_speed, sr)
sf.write(out_pitch, y_pitch, sr)
sf.write(out_combined, y_combined, sr)

# Plot and save figure
plt.figure(figsize=(12, 4))
plt.plot(y[:1000], label='Original')
plt.plot(y_speed[:1000], label='Speed Changed')
plt.plot(y_pitch[:1000], label='Pitch Shifted')
plt.title(f"Waveform Comparison\n{label}")
plt.legend()
plt.tight_layout()
plt.savefig(plot_file)
plt.show()

print("\n✅ Files saved:")
print(f"  - {out_speed}")
print(f"  - {out_pitch}")
print(f"  - {out_combined}")
print(f"  - {plot_file}")
