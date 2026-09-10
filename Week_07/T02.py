from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc_medium = QuantumCircuit(2, 1)

# Step 1: State preparation
qc_medium.x(1)
qc_medium.h(0)
qc_medium.h(1)

qc_medium.barrier()

# Step 2: Oracle for balanced f(x) = x
# y_out = y XOR x -> CNOT with control q0, target q1
qc_medium.cx(0, 1)

qc_medium.barrier()

# Step 3: Interference on input qubit
qc_medium.h(0)

# Step 4: Measure input qubit
qc_medium.measure(0, 0)

print("=== MEDIUM: DEUTSCH'S ALGORITHM (BALANCED f(x)=x) ===")
print("Circuit Diagram:")
print(qc_medium.draw(output="text"))
print()

simulator = AerSimulator()
counts_med = simulator.run(qc_medium, shots=1024).result().get_counts()
print(f"Measurement Counts (1024 shots): {counts_med}")
print(
    f"Function Type: {'Balanced' if '1' in counts_med and len(counts_med) == 1 else 'Constant'}"
)