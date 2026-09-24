import matplotlib.pyplot as plt
import numpy as np

# Bit sizes from n = 2 to 10
n_values = np.arange(2, 11)

# Classical worst-case queries: 2^(n-1) + 1
classical_worst_case = 2 ** (n_values - 1) + 1

# Quantum queries: always exactly 1 query
quantum_queries = np.ones_like(n_values)

print("=== REAL-WORLD: QUERY COMPLEXITY COMPARISON ===")
print("n (Input Bits) | Classical Worst-Case (2^(n-1)+1) | Quantum Queries")
print("-" * 65)
for n_val, c_val, q_val in zip(
    n_values, classical_worst_case, quantum_queries
):
    print(f"{n_val:<14} | {c_val:<33} | {q_val:<15}")

# Plotting the exponential gap
plt.figure(figsize=(9, 5))
plt.plot(
    n_values,
    classical_worst_case,
    "ro-",
    linewidth=2,
    label="Classical Worst-Case (2^(n-1) + 1)",
)
plt.plot(
    n_values,
    quantum_queries,
    "bs--",
    linewidth=2,
    label="Quantum Deutsch-Jozsa (1 Query)",
)

plt.yscale("log")
plt.xlabel("Number of Input Bits (n)", fontsize=11)
plt.ylabel("Number of Oracle Queries (Log Scale)", fontsize=11)
plt.title(
    "Query Complexity: Classical Worst-Case vs Deutsch-Jozsa Algorithm",
    fontsize=12,
)
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig("dj_exponential_speedup.png")
print("\nPlot saved successfully as 'dj_exponential_speedup.png'.")