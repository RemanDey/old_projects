import numpy as np
from matplotlib import pyplot as plt

SAMPLE_RATE = 4410  
DURATION = 5  

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq

    y = np.sin((2 * np.pi) * frequencies)
    return x, y


x, y = generate_sine_wave(1, SAMPLE_RATE, DURATION)

nicetone=generate_sine_wave(400, SAMPLE_RATE, DURATION)
noisetone=generate_sine_wave(4000, SAMPLE_RATE, DURATION)
noisetone=noisetone*3
mixedtone_tuple=noisetone+nicetone
mixedtone= np.array(mixedtone_tuple)

normalizedtone = np.int16((mixedtone / mixedtone.max()) * 32767)

plt.plot(mixedtone[:100])
plt.show()