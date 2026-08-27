import matplotlib.pyplot as plt
import numpy as np

# String lengths from 2 to 30 bits
bit_lengths = np.arange(2, 31, 2)

# Quantum queries: Simon's algorithm requires O(n) queries (approx 2 * n)
quantum_queries = 2 * bit_lengths

# Classical queries: Requires finding collision via Birthday Paradox O(2^(n/2))
classical_queries = 2 ** (bit_lengths / 2)

print("=== REAL-WORLD: QUERY COMPLEXITY COMPARISON ===")
print("Bit Length (n) | Quantum Queries (2n) | Classical Queries (2^(n/2))")
print("-" * 65)
for n, q, c in zip(
    bit_lengths[:8], quantum_queries[:8], classical_queries[:8]
):
    print(f"{n:<14} | {q:<20} | {int(c):<25}")

plt.figure(figsize=(9, 5))
plt.plot(bit_lengths, classical_queries, "r-o", label="Classical (2^(n/2))")
plt.plot(bit_lengths, quantum_queries, "b-s", label="Quantum (Simon's: 2n)")
plt.yscale("log")
plt.xlabel("Secret Bitstring Length (n)", fontsize=11)
plt.ylabel("Number of Oracle Queries (Log Scale)", fontsize=11)
plt.title("Query Complexity: Classical vs Simon's Algorithm", fontsize=12)
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.savefig("simon_speedup.png")
print("\nPlot saved successfully as 'simon_speedup.png'.")