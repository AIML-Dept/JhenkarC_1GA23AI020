import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram

# 1. Create a 2-qubit circuit
qc = QuantumCircuit(2)

# 2. Apply Hadamard (H) gate to both qubits to create equal superposition
qc.h(0)
qc.h(1)

# 3. Print the circuit diagram
print("--- Circuit Diagram ---")
print(qc.draw(output="text"))

# 4. Extract statevector amplitudes
state = Statevector(qc)
amplitudes = state.data

print("\n--- Amplitudes & Probabilities ---")
for i, amp in enumerate(amplitudes):
    # Binary representation corresponding to basis states |00>, |01>, |10>, |11>
    basis_state = format(i, "02b")
    prob = np.abs(amp) ** 2
    print(f"State |{basis_state}⟩: Amplitude = {amp:.4f} | Prob = {prob:.4f}")

# 5. Verify that amplitudes sum to unity
prob_sum = np.sum(np.abs(amplitudes) ** 2)
print(f"\nSum of squared amplitudes: {prob_sum:.4f}")
print("Normalization Verified:", np.isclose(prob_sum, 1.0))

# 6. Visualizations
# Plot probability distribution histogram
plot_histogram(state.probabilities_dict())
plt.suptitle("Probability Distribution across Basis States")
plt.show()

# Plot Bloch spheres for both qubits
plot_bloch_multivector(state)
plt.show()