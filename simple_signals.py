from scipy.fftpack import fft, ifft
import numpy as np

x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

y = fft(x)
y_i = ifft(y)

print y_i
