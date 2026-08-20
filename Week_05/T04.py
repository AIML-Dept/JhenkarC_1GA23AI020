import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

true_theta = 1.15
qc_tomo = QuantumCircuit(1, 1)
qc_tomo.ry(true_theta, 0)
qc_tomo.measure(0, 0)

print("=== REAL-WORLD: QUANTUM STATE TOMOGRAPHY ===")
print("Circuit Diagram:")
print(qc_tomo.draw(output="text"))
print()

total_shots = 10000
simulator = AerSimulator()
counts = simulator.run(qc_tomo, shots=total_shots).result().get_counts()

count_0 = counts.get("0", 0)
p_0_measured = count_0 / total_shots
estimated_theta = 2 * np.arccos(np.sqrt(p_0_measured))

print(f"Measurement Counts: {counts}")
print(f"Estimated Theta: {estimated_theta:.4f} rad")
print(f"True Theta:      {true_theta:.4f} rad")