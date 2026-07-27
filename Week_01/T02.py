import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

# 1. Instantiate a 3-qubit, 3-classical-bit circuit
qc = QuantumCircuit(3, 3)

# 2. Apply Hadamard gates across all 3 qubits to form equal superposition
qc.h([0, 1, 2])

# 3. Measure all 3 qubits into classical register
qc.measure([0, 1, 2], [0, 1, 2])

# Optional: Print ASCII circuit diagram in terminal
print("--- Circuit Diagram ---")
print(qc.draw(output="text"))

# 4. Run simulation using AerSimulator
simulator = AerSimulator()
shots = 8192  # High shot count minimizes statistical variance
job = simulator.run(qc, shots=shots)
result = job.result()

# 5. Extract measurement counts and display calculated probabilities
counts = result.get_counts()
print("\n--- Empirical Probabilities ---")
for state in sorted(counts.keys()):
    prob = counts[state] / shots
    print(f"State |{state}>: {prob:.4f}  (Theoretical: 0.1250)")

# 6. Plot visual histogram and display circuit diagram plot
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
qc.draw(output="mpl", ax=ax[0])
ax[0].set_title("3-Qubit Circuit")

plot_histogram(counts, ax=ax[1])
ax[1].set_title("Probability Distribution")

plt.tight_layout()
plt.show()