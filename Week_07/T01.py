from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Initialize circuit: 2 qubits (q0: input, q1: ancilla) and 1 classical bit
qc_easy = QuantumCircuit(2, 1)

# Step 1: State preparation
qc_easy.x(1)  # Set ancilla to |1>
qc_easy.h(0)  # Superposition on input
qc_easy.h(1)  # Ancilla into |->

qc_easy.barrier()

# Step 2: Oracle for constant f(x) = 0 (Identity / no-op)
# y_out = y XOR 0 = y -> identity operation
qc_easy.id(1)

qc_easy.barrier()

# Step 3: Interference on input qubit
qc_easy.h(0)

# Step 4: Measure input qubit
qc_easy.measure(0, 0)

print("=== EASY: DEUTSCH'S ALGORITHM (CONSTANT f(x)=0) ===")
print("Circuit Diagram:")
print(qc_easy.draw(output="text"))
print()

simulator = AerSimulator()
counts = simulator.run(qc_easy, shots=1024).result().get_counts()
print(f"Measurement Counts (1024 shots): {counts}")
print(
    f"Function Type: {'Constant' if '0' in counts and len(counts) == 1 else 'Balanced'}"
)