from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def build_dj_circuit(n: int, oracle_type: str):
    qc = QuantumCircuit(n + 1, n)

    # State preparation
    qc.x(n)
    for i in range(n + 1):
        qc.h(i)
    qc.barrier()

    # Oracle construction
    if oracle_type == "constant":
        # Constant f(x) = 0 (identity) or f(x) = 1 (flip ancilla)
        qc.x(n)
    elif oracle_type == "balanced":
        # Balanced function using alternating CNOTs and X flips
        for i in range(n):
            qc.cx(i, n)
    else:
        raise ValueError("Invalid oracle type")

    qc.barrier()

    # Interference
    for i in range(n):
        qc.h(i)

    # Measurement
    qc.measure(range(n), range(n))
    return qc


print("=== HARD: GENERALIZED DEUTSCH-JOZSA (n = 2 to 5) ===")
simulator = AerSimulator()

for n_bits in range(2, 6):
    for o_type in ["constant", "balanced"]:
        qc = build_dj_circuit(n_bits, o_type)
        counts = simulator.run(qc, shots=500).result().get_counts()
        measured_string = list(counts.keys())[0]

        is_constant = measured_string == "0" * n_bits
        classification = "Constant" if is_constant else "Balanced"

        print(
            f"n = {n_bits} | Case: {o_type:<8} | Measured: {measured_string:<6} | Result: {classification}"
        )
    print("-" * 55)