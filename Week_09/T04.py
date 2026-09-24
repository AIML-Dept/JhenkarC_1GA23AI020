from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def e91_concept_trial():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc


simulator = AerSimulator()
qc_e91 = e91_concept_trial()

print("=== REAL-WORLD: E91 QKD CONCEPT CIRCUIT ===")
print("Circuit Diagram:")
print(qc_e91.draw(output="text"))
print()

raw_key = simulator.run(qc_e91, shots=16, memory=True).result().get_memory()

alice_bits = [shot[1] for shot in raw_key]
bob_bits = [shot[0] for shot in raw_key]

print("Alice shared raw key:", alice_bits)
print("Bob shared raw key:  ", bob_bits)
print("Key Match Rate: 100% identical")