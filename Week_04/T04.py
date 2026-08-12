from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def build_full_adder(a_bit: int, b_bit: int, cin_bit: int):
    # 4 Qubits: q0 = A, q1 = B, q2 = Cin, q3 = Ancilla/Carry Out
    # Outputs: q1 will hold Sum, q3 will hold Carry Out
    qc = QuantumCircuit(4, 2)

    # Initialize input values
    if a_bit:
        qc.x(0)
    if b_bit:
        qc.x(1)
    if cin_bit:
        qc.x(2)

    # Compute Carry Out bits using Toffoli (CCX) and CNOT (CX)
    qc.ccx(0, 1, 3)  # Carry from A AND B
    qc.cx(0, 1)  # A XOR B
    qc.ccx(1, 2, 3)  # Carry from (A XOR B) AND Cin
    qc.cx(2, 1)  # Sum = A XOR B XOR Cin

    # Uncompute A XOR B to restore clean state on q0, q1
    qc.cx(0, 1)

    # Measure Sum (q1) and Carry Out (q3)
    qc.measure([1, 3], [0, 1])
    return qc


print("=== REAL-WORLD: FULL-ADDER EMULATION ===")
# Test inputs: A = 1, B = 1, Cin = 1 (Sum = 1, Carry Out = 1)
test_a, test_b, test_cin = 1, 1, 1
qc_adder = build_full_adder(test_a, test_b, test_cin)

print(f"Testing Inputs: A={test_a}, B={test_b}, Cin={test_cin}")
print("Circuit Diagram:")
print(qc_adder.draw(output="text"))

simulator = AerSimulator()
counts_adder = simulator.run(qc_adder, shots=100).result().get_counts()

print("\nSimulation Result (Outcome string 'Cout Sum'):", counts_adder)