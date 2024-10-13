import numpy as np

# Define the sampling points
T_s = 0.05
t = np.array([0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35])

# Define the signal x(t) = 5cos(8 * pi * t)
x = 5 * np.cos(8 * np.pi * t)

# Compute the DFT
X = np.fft.fft(x)

# Print the magnitude of the frequency component X[2]
magnitude_X2 = np.abs(X[2])
print("Magnitude of X[2]:", magnitude_X2)
