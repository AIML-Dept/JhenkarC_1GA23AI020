from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc_phi_plus = QuantumCircuit(2, 2)
qc_phi_plus.h(0)
qc_phi_plus.cx(0, 1)
qc_phi_plus.measure([0, 1], [0, 1])

print("=== EASY: PHI+ BELL STATE ===")
print("Circuit Diagram:")
print(qc_phi_plus.draw(output="text"))
print()

simulator = AerSimulator()
counts = simulator.run(qc_phi_plus, shots=1024).result().get_counts()
print("Measurement Results (1024 shots):", counts)