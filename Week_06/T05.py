import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def generalized_simon_solver(secret_bitstring: str):
    n = len(secret_bitstring)
    simulator = AerSimulator()

    # Edge Case: Check if secret string is all zeros
    is_all_zeros = all(b == "0" for b in secret_bitstring)

    # Build Circuit
    qc = QuantumCircuit(2 * n, n)
    for i in range(n):
        qc.h(i)
    qc.barrier()

    # Standard Copy
    for i in range(n):
        qc.cx(i, i + n)

    # Apply secret mapping if non-zero
    if not is_all_zeros:
        first_one = secret_bitstring.find("1")
        for i in range(n):
            if secret_bitstring[i] == "1":
                qc.cx(first_one, i + n)

    qc.barrier()
    for i in range(n):
        qc.h(i)
    qc.measure(range(n), range(n))

    # Run Simulation
    shots = 1000 + 500 * n
    counts = simulator.run(qc, shots=shots).result().get_counts()
    unique_measurements = list(counts.keys())

    # If all-zero secret (1-to-1 function), output contains all 2^n strings
    if len(unique_measurements) == 2**n:
        return "0" * n, counts

    # Solve over GF(2)
    matrix = np.array(
        [list(map(int, list(eq))) for eq in unique_measurements], dtype=int
    )
    for candidate in range(1, 2**n):
        cand_bits = np.array(
            [int(b) for b in format(candidate, f"0{n}b")], dtype=int
        )
        if np.all((matrix @ cand_bits) % 2 == 0):
            return format(candidate, f"0{n}b"), counts

    return "0" * n, counts


print("=== CHALLENGE: GENERALIZED SIMON'S ALGORITHM SOLVER ===")
test_secrets = ["000", "101", "0110", "11001"]

for sec in test_secrets:
    found_sec, raw_counts = generalized_simon_solver(sec)
    print(f"Target Secret: {sec:<6} | Found Secret: {found_sec:<6} | Unique Samples: {len(raw_counts)}")
    print(f"Status: {'PASS' if found_sec == sec else 'FAIL'}")
    print("-" * 50)