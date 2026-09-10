from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def build_deutsch_circuit(oracle_type: str):
    qc = QuantumCircuit(2, 1)

    # Initial state setup: |01> -> |+->
    qc.x(1)
    qc.h(0)
    qc.h(1)
    qc.barrier()

    # Dynamic Oracle Selection:
    # 1. constant_0: f(x) = 0
    # 2. constant_1: f(x) = 1
    # 3. balanced_identity: f(x) = x
    # 4. balanced_not: f(x) = NOT x
    if oracle_type == "constant_0":
        qc.id(1)  # No action
    elif oracle_type == "constant_1":
        qc.x(1)  # Flips target unconditionally: y XOR 1
    elif oracle_type == "balanced_identity":
        qc.cx(0, 1)  # y XOR x
    elif oracle_type == "balanced_not":
        qc.x(0)
        qc.cx(0, 1)
        qc.x(0)  # y XOR (NOT x)
    else:
        raise ValueError(f"Unknown oracle type: {oracle_type}")

    qc.barrier()
    qc.h(0)
    qc.measure(0, 0)
    return qc


print("=== HARD: TESTING ALL FOUR SINGLE-BIT ORACLES ===")
simulator = AerSimulator()
oracle_names = [
    "constant_0",
    "constant_1",
    "balanced_identity",
    "balanced_not",
]

for name in oracle_names:
    test_qc = build_deutsch_circuit(name)
    counts = simulator.run(test_qc, shots=500).result().get_counts()
    measured_bit = list(counts.keys())[0]
    classification = "Constant" if measured_bit == "0" else "Balanced"
    print(
        f"Oracle: {name:<18} | Measurement: {measured_bit} | Inferred: {classification}"
    )