import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Goal: Prepare an entangled state |psi> = cos(theta)|00> + sin(theta)|11>
# Example: theta = pi/6 (30 degrees) => sqrt(3)/2 |00> + 1/2 |11>
theta = np.pi / 6

qc_custom = QuantumCircuit(2)

# Step 1: Rotate qubit 0 around Y-axis by 2*theta
qc_custom.ry(2 * theta, 0)

# Step 2: Entangle qubit 0 with qubit 1
qc_custom.cx(0, 1)

# Extract and inspect statevector directly (State Tomography/Inspection)
state_custom = Statevector.from_instruction(qc_custom)

print("=== CHALLENGE: ARBITRARY 2-QUBIT ENTANGLED STATE ===")
print("Circuit Diagram:")
print(qc_custom.draw(output="text"))

print("\nTarget State Amplitudes:")
print(f"|00> expected: {np.cos(theta):.4f}")
print(f"|11> expected: {np.sin(theta):.4f}")

print("\nConstructed Statevector Data:")
print(np.round(state_custom.data, 4))

print("\nState Label Representation:")
print(state_custom.draw(output="repr"))