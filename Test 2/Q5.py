# import sympy as sp
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Define symbolic variables and functions
# t = sp.Symbol('t')
# tau = sp.Symbol('tau')
# u = sp.Heaviside

# Define the functions as numpy arrays
t_values = np.linspace(-10, 10, 9000000)  # Increase the number of samples
x_values = (t_values + 6)*(np.heaviside(t_values + 6, 1) - np.heaviside(t_values + 3, 1)) + \
           3*(np.heaviside(t_values + 3, 1) - np.heaviside(t_values + 1, 1)) + \
           (np.heaviside(t_values + 1, 1) - np.heaviside(t_values, 1))*(-t_values + 1) + \
           (np.heaviside(t_values, 1) - np.heaviside(t_values - 2, 1)) + \
           (np.heaviside(t_values - 2, 1) - np.heaviside(t_values - 3, 1))*(-t_values + 3)

p_values = 2*(np.heaviside(t_values - 2, 1) - np.heaviside(t_values - 3, 1)) + \
           (np.heaviside(t_values - 3, 1) - np.heaviside(t_values - 4, 1))

# Perform the convolution using scipy
y_values = signal.convolve(x_values, p_values, mode='full') * (t_values[1] - t_values[0])

# Trim the convolution result to match the original time domain
start_index = (len(y_values) - len(t_values)) // 2
y_values = y_values[start_index:start_index + len(t_values)]

index = np.where(t_values >= 4)[0][0]  
"""
y[5] has been giving me problems, 
I am getting y[5] = 2, should be y[5] == 3
             y[2] = 6 (Joshua's Question is saying that this is correct)
The Correct Values i got using this method are:
y[4] == 3
y[-1] ==6.4999
y[3] == 3.5
"""
print('Done with Convolution')
print(y_values[index])
# # Plot the functions
# plt.figure(figsize=(12, 8))

# # Plot x(t)
# plt.subplot(3, 1, 1)
# plt.plot(t_values, x_values, label='x(t)')
# plt.title('Function x(t)')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.legend()

# # Plot p(t)
# plt.subplot(3, 1, 2)
# plt.plot(t_values, p_values, label='p(t)')
# plt.title('Function p(t)')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.legend()

# # Plot the convolution result y(t)
# plt.subplot(3, 1, 3)
# plt.plot(t_values, y_values, label='y(t) = x(t) * p(t)')
# plt.title('Convolution of x(t) and p(t)')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.legend()

# plt.tight_layout()
# plt.show()
# # Plot the results
# # plt.figure(figsize=(12, 6))
# # plt.plot(t_values, y_values, label='Numerical Convolution')
# # plt.title('Numerical Convolution of x and p')
# # plt.xlabel('Time (s)')
# # plt.ylabel('Amplitude')
# # plt.legend()
# # plt.show()