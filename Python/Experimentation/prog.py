import numpy as np
import pyaudio
import matplotlib.pyplot as plt
from scipy.fft import fft

# Audio settings
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Frequency range and step
f1 = 200   # start frequency (Hz)
f2 = 2000  # end frequency (Hz)
d = 100    # step size (Hz)

# EMA smoothing factor (alpha)
alpha = 0.3  # 0 < alpha <= 1; lower = smoother

# Generate the frequencies to check
freqs_to_check = np.arange(f1, f2 + 1, d)

# Start PyAudio
p = pyaudio.PyAudio()

# Select mode
mode = input("Select mode: [A]uto (default mic) or [M]anual (choose device)? ").strip().lower()

if mode == "m":
    print("\nAvailable audio devices:")
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print(f"{i}: {info['name']} (inputs: {info['maxInputChannels']})")
    DEVICE_INDEX = int(input("Select input device index: "))
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=DEVICE_INDEX,
                    frames_per_buffer=CHUNK)
else:
    print("Using default input device...")
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

# Plot setup
plt.ion()
fig, ax2 = plt.subplots(figsize=(10, 5))

bars = ax2.bar(freqs_to_check, np.zeros_like(freqs_to_check), width=d*0.8)
ax2.set_title(f"Real-time Audio Spectrum (Sampled every {d} Hz, EMA smoothing)")
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Amplitude")
ax2.set_xlim(f1 - d, f2 + d)
ax2.set_ylim(0, 5000)  # positive amplitude only

plt.tight_layout()
print("Listening... press Ctrl+C to stop.")

# Precompute FFT bin indices for the frequencies to check
fft_freqs = np.fft.fftfreq(CHUNK, 1 / RATE)[:CHUNK // 2]
bin_indices = [np.argmin(np.abs(fft_freqs - f)) for f in freqs_to_check]

# Initialize smoothed amplitude array
smoothed_amplitude = np.zeros_like(freqs_to_check, dtype=float)

try:
    while True:
        # Read audio data
        data = np.frombuffer(stream.read(CHUNK, exception_on_overflow=False), dtype=np.int16)

        # FFT
        yf = fft(data)
        amplitude_full = 2.0 / CHUNK * np.abs(yf[:CHUNK // 2])
        amplitude_sampled = amplitude_full[bin_indices]

        # EMA smoothing
        smoothed_amplitude = alpha * amplitude_sampled + (1 - alpha) * smoothed_amplitude

        # Update bars
        for rect, h in zip(bars, smoothed_amplitude):
            rect.set_height(max(h, 0))

        # Refresh plot
        fig.canvas.draw()
        fig.canvas.flush_events()
except KeyboardInterrupt:
    print("Stopping...")

# Cleanup
stream.stop_stream()
stream.close()
p.terminate()
