import sympy as sp

# Define the symbols
t, omega = sp.symbols('t omega')

# Define the signal 100t * e^(-0.43t) * u(t)
u = sp.Heaviside(t)  # Defining a  Unit step function
signal = 100 * t * sp.exp(-0.43 * t) * u
FT = sp.fourier_transform(signal, t, omega) #### Get the Fourier Transform of this function

# Find the magnitude of the Fourier Transform
magnitude = sp.Abs(FT)

# Substitute omega = 1.69 into the magnitude expressions
magnitude_at_1_66 = magnitude.subs(omega, 1.69)

# Print the results
print(f'Magnitude of the spectrum at 1.66 Hz: {sp.simplify(magnitude_at_1_66)}')
