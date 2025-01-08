import ctypes
import numpy as np
import matplotlib.pyplot as plt
import math

# Load the shared library (adjust path to the correct location)
lib = ctypes.CDLL('./verify.so')  # Use './myfunctions.dll' on Windows

# Define argument and return types for the C functions
lib.solution.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.c_int]
lib.solution.restype = None

lib.derivative.argtypes = [ctypes.c_float, ctypes.c_float]
lib.derivative.restype = ctypes.c_float

# Set the initial values and parameters
x = ctypes.c_float(1.0001)  # Initial value of x
y = ctypes.c_float(-4.10)  # Initial value of y
n = 5000  # Number of iterations

# Create arrays to store the results for plotting
x_vals = []
y_vals = []
exp_vals = []

# Run the solution function and store results for plotting
for i in range(n):
    # Append current values to the lists
    x_vals.append(x.value)
    y_vals.append(y.value)
    
    # Calculate the exponential value of x (e^x)
    exp_vals.append((0.5)*np.log((4/3)*(1-1/(x.value)**2)))
    
    # Call the C solution function
    lib.solution(ctypes.byref(x), ctypes.byref(y), 1)

# Plot both y(x) and exp(x)
sim_line, = plt.plot(x_vals, y_vals, label="Numeric", color='b')
theory_line, = plt.plot(x_vals, exp_vals, label="theory", color='r', linestyle='--')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(handles=[sim_line, theory_line])
plt.grid(True)
plt.show()
