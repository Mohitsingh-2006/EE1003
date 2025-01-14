import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the C shared library
quadratic_lib = ctypes.CDLL('./quadratic_roots.so')

# Define the function signature in the C library
quadratic_lib.find_roots.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                     ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

# Coefficients of the quadratic equation
a = np.sqrt(2)
b = 7
c = 5 * np.sqrt(2)

# Variables to store the roots (passed by reference)
root1 = ctypes.c_double()
root2 = ctypes.c_double()

# Call the C function to compute roots
quadratic_lib.find_roots(a, b, c, ctypes.byref(root1), ctypes.byref(root2))

# Extract the roots
roots = [root1.value, root2.value]
print("Roots of the quadratic equation (computed in C):", roots)

# Plot the quadratic function
x = np.linspace(-6, 2, 500)  # Range for x-axis
y = a * x**2 + b * x + c      # Quadratic equation

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$\sqrt{2}x^2 + 7x + 5\sqrt{2} = 0$', color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # x-axis
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # y-axis
plt.scatter(roots, [0, 0], color='red', label='Roots')  # Mark roots
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

