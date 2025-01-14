import ctypes
import math
import matplotlib.pyplot as plt
import numpy as np

# Load the shared library
# Replace './code.so' with the correct location of the shared library
c_library = ctypes.CDLL('./code.so')

# Define the structure to hold the roots
class Roots(ctypes.Structure):
    _fields_ = [("root1", ctypes.c_double), ("root2", ctypes.c_double)]

# Set the argument and return types for the C function
c_library.eigen_values.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
c_library.eigen_values.restype = Roots

def f(x):
    return np.sqrt(2) * x**2 + 7 * x + 5 * np.sqrt(2)

# Python function to call the C function
def find_roots(a, b, c):
    roots = c_library.eigen_values(a, b, c)
    return roots.root1, roots.root2

# Example usage for the equation sqrt(2)x^2 + 7x + 5sqrt(2) = 0
a = math.sqrt(2)
b = 7
c = 5 * math.sqrt(2)

root1, root2 = find_roots(a, b, c)
print(f"Root 1: {root1:.3f}, Root 2: {root2:.3f}")

# Plot the graph of f(x)
x = np.linspace(-10, 5, 500)
y = f(x)
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$f(x) = \sqrt{2}x^2 + 7x + 5\sqrt{2}$')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.scatter([root1, root2], [0, 0], color='red', label='Roots')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()

