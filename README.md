# 🎙️ DSP Voice Modifier Project

This project modifies a recorded voice signal by:
- Changing the **speed**
- Shifting the **pitch**
- And combining both effects

It also plots waveform comparisons of original vs modified audio.

---

## 🛠️ Tools Used
- Python 3
- librosa
- soundfile
- matplotlib

---

## 📂 Project Files

| Filename                          | Description                                 |
|-----------------------------------|---------------------------------------------|
| `input.wav`                       | Original voice input                        |
| `voice_modifier.py`               | Main script to modify voice                 |
| `output_speed_...wav`             | Speed-modified output                       |
| `output_pitch_...wav`             | Pitch-shifted output                        |
| `output_combined_...wav`          | Combined speed & pitch effect               |
| `waveform_...png`                 | Waveform comparison image                   |

---

## 🗣️ Sample Voice Input

> "I am Abbal Baral and I am doing the Digital Signal Processing Project!"

---

## ⚙️ Example Parameters

- `speed_factor = 0.5`, `pitch_steps = -5` → Slow, deep voice
- `speed_factor = 1.5`, `pitch_steps = +3` → Fast, high voice
- `speed_factor = 1.0`, `pitch_steps = -2` → Mild pitch drop

---

## 📈 Output Visualization

Each run also generates a waveform plot showing differences between:
- Original audio
- Speed-modified
- Pitch-shifted

---

## 🧪 Run It Yourself

```bash
python voice_modifier.py
