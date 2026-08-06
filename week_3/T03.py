import random
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# 1. Define 2x2 matrix representations for single-qubit gates
gate_matrices = {
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
    "H": (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex),
    "S": np.array([[1, 0], [0, 1j]], dtype=complex),
}

# 2. Randomly select 5 single-qubit gates
random.seed(42)  # Fixed seed for consistent testing
gate_pool = ["X", "Y", "Z", "H", "S"]
chosen_gates = [random.choice(gate_pool) for _ in range(5)]

print("--- Chosen Gate Sequence ---")
print(" -> ".join(chosen_gates))

# 3. Analytical Calculation (Multiply matrices from right to left starting on state |0>)
initial_state = np.array([1, 0], dtype=complex)  # Basis state |0>
net_matrix = np.eye(2, dtype=complex)

for gate_name in chosen_gates:
    net_matrix = np.dot(gate_matrices[gate_name], net_matrix)

analytical_state = np.dot(net_matrix, initial_state)

# 4. Qiskit Circuit Simulation
qc_hard = QuantumCircuit(1)
for gate_name in chosen_gates:
    if gate_name == "X":
        qc_hard.x(0)
    elif gate_name == "Y":
        qc_hard.y(0)
    elif gate_name == "Z":
        qc_hard.z(0)
    elif gate_name == "H":
        qc_hard.h(0)
    elif gate_name == "S":
        qc_hard.s(0)

print("\n--- Circuit Diagram ---")
print(qc_hard.draw(output="text"))

simulated_state = Statevector(qc_hard).data

# 5. Output Verification
print("\n--- Results ---")
print("Analytical Statevector:", analytical_state)
print("Simulated Statevector: ", simulated_state)
print(
    "Verification Verdict:  ",
    "MATCH SUCCESSFUL"
    if np.allclose(analytical_state, simulated_state)
    else "MISMATCH",
)