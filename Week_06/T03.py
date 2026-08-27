import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def build_simon_circuit_4bit(secret_str):
    n = len(secret_str)
    qc = QuantumCircuit(2 * n, n)
    for i in range(n):
        qc.h(i)
    qc.barrier()

    # Oracle implementation
    for i in range(n):
        qc.cx(i, i + n)

    # Find first non-zero bit as anchor
    first_one = secret_str.find("1")
    if first_one != -1:
        for i in range(n):
            if secret_str[i] == "1":
                qc.cx(first_one, i + n)

    qc.barrier()
    for i in range(n):
        qc.h(i)
    qc.measure(range(n), range(n))
    return qc


def solve_gf2(equations, n):
    # Convert equations to binary matrix
    matrix = [list(map(int, list(eq))) for eq in equations]
    matrix = np.array(matrix, dtype=int)

    # Gaussian elimination over GF(2)
    rows, cols = matrix.shape
    pivot_row = 0
    for col in range(cols):
        # Find pivot
        sel = -1
        for r in range(pivot_row, rows):
            if matrix[r, col] == 1:
                sel = r
                break
        if sel == -1:
            continue
        # Swap rows
        matrix[[pivot_row, sel]] = matrix[[sel, pivot_row]]
        # Eliminate below and above
        for r in range(rows):
            if r != pivot_row and matrix[r, col] == 1:
                matrix[r] = (matrix[r] ^ matrix[pivot_row]) % 2
        pivot_row += 1
        if pivot_row == rows:
            break

    # Find non-trivial nullspace vector s != 0^n
    for candidate in range(1, 2**n):
        cand_bits = np.array(
            [int(b) for b in format(candidate, f"0{n}b")], dtype=int
        )
        if np.all((matrix @ cand_bits) % 2 == 0):
            return format(candidate, f"0{n}b")
    return "0" * n


print("=== HARD: 4-BIT SIMON'S ALGORITHM WITH GF(2) SOLVER ===")
true_secret_4bit = "1011"
qc_4bit = build_simon_circuit_4bit(true_secret_4bit)

simulator = AerSimulator()
counts_4bit = simulator.run(qc_4bit, shots=1024).result().get_counts()
unique_measurements = list(counts_4bit.keys())

print(f"True Secret String: {true_secret_4bit}")
print(f"Measured Unique Strings ({len(unique_measurements)}):", unique_measurements)

recovered_secret = solve_gf2(unique_measurements, 4)
print(f"\nRecovered Secret String via GF(2) Elimination: {recovered_secret}")
print(f"Validation: {'SUCCESS' if recovered_secret == true_secret_4bit else 'FAILED'}")