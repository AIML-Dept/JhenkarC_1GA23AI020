from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc_x_basis = QuantumCircuit(2, 2)
qc_x_basis.h(0)
qc_x_basis.cx(0, 1)

qc_x_basis.barrier()
qc_x_basis.h(0)
qc_x_basis.h(1)

qc_x_basis.measure([0, 1], [0, 1])

print("=== HARD: MEASURING BELL PAIR IN HADAMARD BASIS ===")
print("Circuit Diagram:")
print(qc_x_basis.draw(output="text"))
print()

simulator = AerSimulator()
counts_x = simulator.run(qc_x_basis, shots=1024).result().get_counts()
print("Measurement Results in X-Basis (1024 shots):", counts_x)