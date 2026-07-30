import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

# 1. Create a 1-qubit quantum circuit
qc = QuantumCircuit(1)

# 2. Apply Hadamard (H) gate, followed by Phase (S) gate
qc.h(0)
qc.s(0)

# 3. Print the circuit diagram
print("--- Circuit Diagram ---")
print(qc.draw(output="text"))

# 4. Get and display the resulting statevector
state = Statevector(qc)
print("\nResulting Statevector:", state.data)
# Output will be: [0.7071+0.j, 0.+0.7071j] which corresponds to 1/√2 |0⟩ + i/√2 |1⟩

# 5. Visualize the state on the Bloch Sphere
plot_bloch_multivector(state)
plt.show()