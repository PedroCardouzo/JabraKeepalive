import numpy as np
import sounddevice as sd

# Settings
samplerate = 44100
volume = 0.0005  # very very low

# Generate high-frequency random signal
duration = 5.0  # seconds
t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
high_freq = 18000  # 18kHz, almost inaudible
wave = (np.sin(2 * np.pi * high_freq * t) * volume).astype(np.float32)

# Callback to stream continuously
def callback(outdata, frames, time_info, status):
    size = len(wave)
    start = (callback.frame * frames) % size
    end = start + frames
    if end <= size:
        outdata[:] = wave[start:end, np.newaxis]
    else:
        part1 = wave[start:]
        part2 = wave[:end - size]
        outdata[:] = np.concatenate((part1, part2))[:, np.newaxis]
    callback.frame += 1

callback.frame = 0

# Open audio stream
with sd.OutputStream(channels=1, callback=callback, samplerate=samplerate):
    print("Keepalive running (ultra high frequency)... Press Ctrl+C to exit.")
    try:
        while True:
            sd.sleep(1000)
    except KeyboardInterrupt:
        print("Exiting.")
