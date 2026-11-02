import numpy as np
import matplotlib.pyplot as plt

# (a) Generate analog signal with high sampling rate
fs = 1000
t = np.arange(0, 1, 1/fs)
x = np.sin(2 * np.pi * 3 * t)

# (b) Sample the signal at 20 Hz
fs_sample = 20
ts = np.arange(0, 1, 1/fs_sample)
xs = np.sin(2 * np.pi * 3 * ts)

# (c) Quantize the samples to 3-bit levels (8 levels)
bits = 3
L = 2**bits
xmin, xmax = -1, 1

delta = (xmax - xmin) / L
xq = xmin + delta/2 + delta * np.floor((xs - xmin) / delta)
xq = np.clip(xq, xmin + delta/2, xmax - delta/2)

# Plot all three signals
plt.figure(figsize=(12, 9))

plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title("Analog Sine Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(ts, xs)
plt.title("Sampled Signal (20 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, x, label="Original Analog Signal")
plt.stem(ts, xq, linefmt='r-', markerfmt='ro',
         basefmt='k-', label="3-bit Quantized Samples")
plt.title("Analog and Quantized Signals")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()