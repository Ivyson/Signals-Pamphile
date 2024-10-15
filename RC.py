import numpy as np

# Given parameters
frequency = 1.2e3  # Frequency in Hz
R = 18  # Resistance in Ohms
C = 17.6e-6  # Capacitance in Farads
V_peak_input = 38  # Peak amplitude of the input voltage in Volts

# Angular frequency
omega = 2 * np.pi * frequency

# Transfer function H(jw) for an RC low-pass filter
H_jw = 1 / (1 + 1j * omega * R * C)

# Calculate the peak amplitude of the output voltage
V_peak_output = np.abs(H_jw) * V_peak_input

print(f"The peak amplitude voltage of the output signal is {V_peak_output:.4f} Volts")
