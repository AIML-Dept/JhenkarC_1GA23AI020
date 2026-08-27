from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def simon_oracle_110():
    # 3 input qubits (0, 1, 2) and 3 auxiliary output qubits (3, 4, 5)
    oracle = QuantumCircuit(6, name="Oracle_110")

    # Step 1: Copy input qubits to target qubits
    for i in range(3):
        oracle.cx(i, i + 3)

    # Step 2: Implement XOR logic for s = '110' (MSB to LSB: q0=0, q1=1, q2=1 or bit 0, 1)
    # Using secret string s = '110' with rightmost bit at index 0 (s_0=0, s_1=1, s_2=1):
    # Condition: if MSB q2=1, flip q3 and q4
    oracle.cx(2, 3)
    oracle.cx(2, 4)

    return oracle


# Verify truth table across all 8 possible 3-bit inputs
oracle_circuit = simon_oracle_110()
print("=== EASY: SIMON'S ORACLE ('110') ===")
print("Oracle Circuit Diagram:")
print(oracle_circuit.draw(output="text"))
print()

simulator = AerSimulator()
print("Input x  | Output f(x) | Matching Collision x XOR s")
print("-" * 55)

for x_int in range(8):
    x_str = format(x_int, "03b")  # e.g., '000', '001', ...
    qc = QuantumCircuit(6, 3)

    # Initialize input qubits according to x_str
    for i in range(3):
        if x_str[2 - i] == "1":
            qc.x(i)

    # Append oracle
    qc.compose(oracle_circuit, inplace=True)

    # Measure output qubits (3, 4, 5)
    qc.measure([3, 4, 5], [0, 1, 2])

    result = simulator.run(qc, shots=1).result().get_counts()
    fx_str = list(result.keys())[0]

    # Calculate x XOR s ('110')
    x_xor_s = format(x_int ^ 0b110, "03b")
    print(f"{x_str:<8} | {fx_str:<11} | x XOR 110 = {x_xor_s}")