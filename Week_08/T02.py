from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

n = 3
qc_medium = QuantumCircuit(n + 1, n)

# Step 1: Initialize states
qc_medium.x(n)
for i in range(n + 1):
    qc_medium.h(i)

qc_medium.barrier()

# Step 2: Balanced Parity Oracle f(x) = x0 XOR x1 XOR x2
# Implemented by CNOT gates from each input qubit to the ancilla
for i in range(n):
    qc_medium.cx(i, n)

qc_medium.barrier()

# Step 3: Interference
for i in range(n):
    qc_medium.h(i)

# Step 4: Measure input qubits
qc_medium.measure(range(n), range(n))

print("=== MEDIUM: 3-BIT BALANCED PARITY ORACLE ===")
print("Circuit Diagram:")
print(qc_medium.draw(output="text"))
print()

simulator = AerSimulator()
counts_med = simulator.run(qc_medium, shots=1024).result().get_counts()
print("Measurement Results (1024 shots):", counts_med)

all_zeros = "0" * n
print(
    f"Inferred Classification: {'Constant' if all_zeros in counts_med else 'Balanced (Non-zero result)'}"
)