import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
trapezoid = ctypes.CDLL('./trapezoid.so')

# Define the function signature
trapezoid.trapezoidal_rule.restype = ctypes.c_double
trapezoid.trapezoidal_rule.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]

# Define the function y' = e^x * sin(x) for plotting
def f(x):
    return np.exp(x) * np.sin(x)

# Inputs
a = 0.0  # Lower limit
b = np.pi  # Upper limit
n = 100  # Number of intervals (use smaller n for better visualization)

# Call the C function
result = trapezoid.trapezoidal_rule(ctypes.c_double(a), ctypes.c_double(b), ctypes.c_int(n))

# Generate points for the trapezoids
x = np.linspace(a, b, n + 1)  # Trapezoid boundaries
y = f(x)  # Function values at the boundaries

# Plot the function
x_fine = np.linspace(a, b, 500)  # For smooth curve
y_fine = f(x_fine)
plt.plot(x_fine, y_fine, label=r"$y' = e^x \sin x$", color="blue")

# Plot the trapezoids
for i in range(n):
    plt.fill_between([x[i], x[i + 1]], [y[i], y[i + 1]], color="skyblue", alpha=0.4)

# Highlight the calculated area
plt.fill_between(x, y, color="skyblue", alpha=0.4, label="Trapezoidal Area")

# Labels and legend
plt.title(f"Area under curve (Trapezoidal Rule, n={n})")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

# Print the computed result
print(f"The value of the integral y({b}) is approximately {result}")

