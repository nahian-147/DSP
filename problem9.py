import numpy as np
import imageio
import time
from cmath import pi, exp

def Radix2_FFT(f):
    N = len(f)
    if N<=1:
        return f
    
    even = Radix2_FFT(f[0::2])
    odd = Radix2_FFT(f[1::2])
    
    fft = np.zeros(N).astype(np.complex64)
    
    for i in range(N//2):
        fft[i] = even[i] + exp((-2j*pi*i)/N) * odd[i]
        fft[i + N//2] = even[i] - exp((-2j*pi*i)/N) * odd[i]
        
    return fft
x = [1,2,3,4]
fft = Radix2_FFT(x)
print(fft)

print(np.fft.fft(x))