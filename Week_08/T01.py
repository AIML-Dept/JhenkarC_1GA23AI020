from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

n = 3
# Circuit with n input qubits, 1 ancilla qubit, and n classical bits
qc_easy = QuantumCircuit(n + 1, n)

# Step 1: Initialize states
qc_easy.x(n)  # Ancilla to |1>
for i in range(n + 1):
    qc_easy.h(i)  # Inputs to |+>, Ancilla to |->

qc_easy.barrier()

# Step 2: Constant Oracle f(x) = 1 (Applies X to ancilla, flipping target unconditionally)
# Note: For f(x) = 0, oracle can simply be identity (no gates)
qc_easy.x(n)

qc_easy.barrier()

# Step 3: Interference on input qubits
for i in range(n):
    qc_easy.h(i)

# Step 4: Measure only the input qubits
qc_easy.measure(range(n), range(n))

print("=== EASY: 3-BIT CONSTANT ORACLE (f(x) = 1) ===")
print("Circuit Diagram:")
print(qc_easy.draw(output="text"))
print()

simulator = AerSimulator()
counts = simulator.run(qc_easy, shots=1024).result().get_counts()
print("Measurement Results (1024 shots):", counts)

result_bitstring = list(counts.keys())[0]
print(
    f"Inferred Classification: {'Constant (All Zeros)' if result_bitstring == '0'*n else 'Balanced'}"
)