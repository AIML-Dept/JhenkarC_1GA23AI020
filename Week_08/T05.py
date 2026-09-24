import random
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def build_random_balanced_circuit(n: int):
    qc = QuantumCircuit(n + 1, n)

    # State preparation
    qc.x(n)
    for i in range(n + 1):
        qc.h(i)
    qc.barrier()

    # Generate a random binary mask to wrap CNOTs with X gates
    # This randomizes which half of the inputs map to 1 and 0
    mask = [random.choice([0, 1]) for _ in range(n)]

    # Wrap with X gates based on the random mask
    for i in range(n):
        if mask[i] == 1:
            qc.x(i)

    # Apply CNOT gates to ancilla
    for i in range(n):
        qc.cx(i, n)

    # Uncompute X gates
    for i in range(n):
        if mask[i] == 1:
            qc.x(i)

    qc.barrier()

    # Interference
    for i in range(n):
        qc.h(i)

    # Measure input register
    qc.measure(range(n), range(n))
    return qc, mask


print("=== CHALLENGE: RANDOMIZED BALANCED ORACLE VALIDATION ===")
n = 4
simulator = AerSimulator()

for trial in range(1, 6):
    qc_rand, generated_mask = build_random_balanced_circuit(n)
    counts = simulator.run(qc_rand, shots=500).result().get_counts()
    measured_keys = list(counts.keys())

    # Check if '0000' is in measurement
    contains_all_zeros = "0" * n in counts
    classification = "Constant" if contains_all_zeros else "Balanced"

    print(f"Trial {trial}:")
    print(f"  Applied Random Mask: {generated_mask}")
    print(f"  Measured Bitstring(s): {measured_keys}")
    print(
        f"  Correctly Classified as Balanced? {'YES (Pass)' if not contains_all_zeros else 'NO (Fail)'}"
    )
    print("-" * 55)