import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Part A: GHZ State
qc_ghz = QuantumCircuit(3)
qc_ghz.h(0)
qc_ghz.cx(0, 1)
qc_ghz.cx(1, 2)
state_ghz = Statevector.from_instruction(qc_ghz)

print("=== CHALLENGE: GHZ VS W-STATE ENTANGLEMENT PERSISTENCE ===")
print("1. GHZ Circuit Diagram:")
print(qc_ghz.draw(output="text"))
outcome_ghz, post_ghz = state_ghz.measure([0])
print("GHZ Qubit 0 Measurement Outcome:", outcome_ghz)
print("GHZ Post-Measurement Statevector:", np.round(post_ghz.data, 3))

# Part B: W-State (|001> + |010> + |100>)/sqrt(3)
qc_w = QuantumCircuit(3)
qc_w.ry(2 * np.arccos(1 / np.sqrt(3)), 0)
qc_w.ch(0, 1)
qc_w.cx(1, 2)
qc_w.cx(0, 1)
qc_w.x(0)
state_w = Statevector.from_instruction(qc_w)

print("\n2. W-State Circuit Diagram:")
print(qc_w.draw(output="text"))
outcome_w, post_w = state_w.measure([0])
print("W-State Qubit 0 Measurement Outcome:", outcome_w)
print("W-State Post-Measurement Statevector:", np.round(post_w.data, 3))