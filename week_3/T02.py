from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

# 1. Create a 1-qubit circuit to build the |-> state
qc_medium = QuantumCircuit(1)
qc_medium.h(0)  # Creates |+> state: 1/sqrt(2)(|0> + |1>)
qc_medium.z(0)  # Applies Z gate to flip phase: 1/sqrt(2)(|0> - |1>)

# 2. Compute statevector
state_medium = Statevector(qc_medium)

print("--- Circuit Diagram ---")
print(qc_medium.draw(output="text"))

print("\n--- Resulting Statevector ---")
print("Statevector of |-> State:", state_medium.data)
# Output: [0.7071+0.j, -0.7071+0.j]

# 3. Measurement Verification
# (Applying H before measuring changes X-basis |-> into Z-basis |1>)
qc_verify = QuantumCircuit(1, 1)
qc_verify.h(0)
qc_verify.z(0)
qc_verify.h(0)
qc_verify.measure(0, 0)

simulator = AerSimulator()
counts = simulator.run(qc_verify, shots=1024).result().get_counts()

print("\n--- Verification Measurement ---")
print("Counts (Should yield '1' 100% of the time):", counts)