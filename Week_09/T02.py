from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def generate_bell_circuit(bell_type):
    qc = QuantumCircuit(2, 2)
    if bell_type == "Phi+":
        pass
    elif bell_type == "Phi-":
        qc.z(0)
    elif bell_type == "Psi+":
        qc.x(1)
    elif bell_type == "Psi-":
        qc.x(1)
        qc.z(0)

    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc


simulator = AerSimulator()
bell_states = ["Phi+", "Phi-", "Psi+", "Psi-"]

print("=== MEDIUM: ALL FOUR BELL STATES ===")
for name in bell_states:
    circuit = generate_bell_circuit(name)
    counts = simulator.run(circuit, shots=1024).result().get_counts()
    print(f"State: {name:<5} | Measured Counts: {counts}")