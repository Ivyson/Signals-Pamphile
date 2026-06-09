import sympy as sm

# Define the symbols
t, omega = sm.symbols('t omega')

# Define the signal 100t * e^(-0.43t) * u(t)
u = sm.Heaviside(t)  # Defining a  Unit step function
signal = 100 * t * sm.exp(-0.43 * t) * u
FT = sm.fourier_transform(signal, t, omega) #### Get the Fourier Transform of this function

# Find the magnitude of the Fourier Transform
magnitude = sm.Abs(FT)

# Substitute omega = 1.69 into the magnitude expressions
magnitude_at_1_66 = magnitude.subs(omega, 1.69)

# Print the results
print(f'Magnitude of the spectrum at 1.66 Hz: {sm.simplify(magnitude_at_1_66)}')
