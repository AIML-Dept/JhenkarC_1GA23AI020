from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

n = 3
qc_simon = QuantumCircuit(2 * n, n)

# Step 1: Apply Hadamard gates to input register
for i in range(n):
    qc_simon.h(i)

qc_simon.barrier()

# Step 2: Query Oracle for s = '110'
for i in range(n):
    qc_simon.cx(i, i + n)
qc_simon.cx(2, 3)
qc_simon.cx(2, 4)

qc_simon.barrier()

# Step 3: Apply Hadamard gates to input register again
for i in range(n):
    qc_simon.h(i)

# Step 4: Measure input register
qc_simon.measure(range(n), range(n))

print("=== MEDIUM: FULL SIMON'S ALGORITHM CIRCUIT ===")
print("Circuit Diagram:")
print(qc_simon.draw(output="text"))
print()

simulator = AerSimulator()
counts = simulator.run(qc_simon, shots=1024).result().get_counts()
print("Measured Output Bitstrings (1024 shots):", counts)

print("\nVerifying Orthogonality (s . y mod 2 = 0 where s = 110):")
secret = "110"
for y in counts.keys():
    # Calculate dot product
    dot_product = sum(int(secret[i]) * int(y[i]) for i in range(n)) % 2
    print(f"Measured string y = {y} -> (110 . {y}) mod 2 = {dot_product}")