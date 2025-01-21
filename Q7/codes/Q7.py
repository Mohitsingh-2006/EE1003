import random
from collections import Counter
import ctypes

# Load the compiled C library
coin_toss_lib = ctypes.CDLL('./coin_toss.so')

# Define the C function argument and return types
coin_toss_lib.calculate_net_money.argtypes = [ctypes.c_char_p]
coin_toss_lib.calculate_net_money.restype = ctypes.c_double

# Simulation Parameters
num_tosses = 4  # Number of coin tosses
num_simulations = 100000  # Number of trials for accurate probabilities

# Function to calculate net money using the C function
def calculate_net_money(outcome):
    outcome_c = ctypes.c_char_p(outcome.encode('utf-8'))  # Convert Python string to C string
    return coin_toss_lib.calculate_net_money(outcome_c)

# Generate random outcomes and calculate net money
outcomes = []
for _ in range(num_simulations):
    outcome = ''.join(random.choice(['H', 'T']) for _ in range(num_tosses))  # Generate random outcome
    net_money = calculate_net_money(outcome)  # Call the C function
    outcomes.append(net_money)

# Count occurrences of each net money
counts = Counter(outcomes)

# Calculate probabilities
probabilities = {money: count / num_simulations for money, count in counts.items()}

# Display the results
print("Net Money and Their Probabilities:")
for money, prob in sorted(probabilities.items()):
    print(f"Net Money: ₹{money:.1f}, Probability: {prob:.4f}")

# Optionally, plot the results
import matplotlib.pyplot as plt

plt.bar(probabilities.keys(), probabilities.values(), color='skyblue', edgecolor='black')
plt.xlabel("Net Money (₹)")
plt.ylabel("Probability")
plt.title("Probability Distribution of Net Money After 4 Tosses")
plt.xticks(sorted(probabilities.keys()))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

