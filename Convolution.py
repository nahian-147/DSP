from scipy import signal as sig
import numpy as np

x = [1, 1, 1, 1, 1, 1.5, 1, 1, 1]
y = [1, 1, 0, 0, 0, 0.9, 1, 1, 1]
conv = []

for l in range(-2 * max(len(x), len(y)), 2 * max(len(x), len(y))):
    sigma = 0
    for n in range(len(x)):
        if -n + l < len(y) and -n + l >= 0:
            sigma += x[n] * y[-n + l]
        else:
            sigma += 0
    conv.append(sigma)

conv_xy = []

for item in conv:
    if not item == 0:
        conv_xy.append(item)

conv_xy = np.array(conv_xy)
print(conv_xy)
print(sig.convolve(x, y))
