from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Build individual 1-qubit circuits to inspect each gate's statevector cleanly
qc_x = QuantumCircuit(1)
qc_x.x(0)

qc_y = QuantumCircuit(1)
qc_y.y(0)

qc_z = QuantumCircuit(1)
qc_z.z(0)

# Extract individual statevectors
state_q0 = Statevector(qc_x)
state_q1 = Statevector(qc_y)
state_q2 = Statevector(qc_z)

# Combined circuit for diagram display
qc_easy = QuantumCircuit(3)
qc_easy.x(0)
qc_easy.y(1)
qc_easy.z(2)

print("--- Circuit Diagram ---")
print(qc_easy.draw(output="text"))

print("\n--- Resulting Statevectors ---")
print("Qubit 0 (X Gate):", state_q0.data)
print("Qubit 1 (Y Gate):", state_q1.data)
print("Qubit 2 (Z Gate):", state_q2.data)