import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

# 1. Build circuit
qc = QuantumCircuit(1)
qc.x(0)

# 2. Draw circuit in terminal
print("--- Circuit Diagram ---")
print(qc.draw())

# 3. Compute Statevector
state = Statevector(qc)
print("\nResulting Statevector:", state.data)

# 4. Plot visual state
plot_bloch_multivector(state)
plt.show()