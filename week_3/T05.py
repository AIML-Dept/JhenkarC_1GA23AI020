import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import DensityMatrix, Operator, Statevector
from qiskit.visualization import plot_state_city

print("--- Challenge Exercise: HZH = X Gate Equivalence ---")

# 1. Analytical Proof via Matrix Multiplication
H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
X_expected = np.array([[0, 1], [1, 0]], dtype=complex)

# Matrix Multiplication: H * Z * H
HZH_analytical = np.dot(H, np.dot(Z, H))

print("Matrix H * Z * H:")
print(np.round(HZH_analytical, 4))

print("\nMatrix X:")
print(X_expected)

analytical_match = np.allclose(HZH_analytical, X_expected)
print("\nAnalytical Equivalence Verified:", analytical_match)

# 2. Qiskit Circuit Operator Verification
qc_hzh = QuantumCircuit(1)
qc_hzh.h(0)
qc_hzh.z(0)
qc_hzh.h(0)

op_hzh = Operator(qc_hzh)

qc_x = QuantumCircuit(1)
qc_x.x(0)

op_x = Operator(qc_x)

circuit_match = op_hzh.equiv(op_x)
print("Qiskit Circuit Operator Equivalence Verified:", circuit_match)

# 3. State Output Verification on |0>
state_hzh = Statevector(qc_hzh)
state_x = Statevector(qc_x)

print("\nStatevector from HZH circuit:", state_hzh.data)
print("Statevector from X circuit:  ", state_x.data)

# -------------------------------------------------------------
# Visualization: Plotting Density Matrices cleanly
# -------------------------------------------------------------
# Convert statevectors to density matrices for state city plotting
dm_hzh = DensityMatrix(state_hzh)
dm_x = DensityMatrix(state_x)

# Render state city plots (Qiskit generates figures directly)
fig1 = plot_state_city(dm_hzh, title="HZH Circuit Final State Density Matrix")
fig2 = plot_state_city(dm_x, title="X Gate Circuit Final State Density Matrix")

plt.show()