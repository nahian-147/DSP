from scipy import signal as sig
import numpy as np 

x = [1, 1, 2, 3]
y = [1, 1, 2, 3]
cor = []

for l in range(-max(len(x), len(y)), max(len(x), len(y))):
    sigma = 0
    for n in range(len(x)):
        if n - l < len(y) and n - l >= 0:
            sigma += x[n] * y[n - l]
        else:
            sigma += 0
    cor.append(sigma)

cor_xy = []

for item in cor:
    if not item == 0:
        cor_xy.append(item)

cor_xy = np.array(cor_xy)
print(cor_xy)
print(sig.correlate(x, y))
