from qiskit import QuantumCircuit


def conceptual_classification_circuit():
    # Demonstration of phase kickback tagging a boundary separation:
    # Feature register q0, Label marker q1
    qc = QuantumCircuit(2, 1)

    # Encode feature state into superposition
    qc.h(0)

    # Encode decision boundary condition into ancilla
    qc.x(1)
    qc.h(1)
    qc.barrier()

    # Kernel/Oracle decision boundary:
    # If feature satisfies boundary criterion (x=1), phase kickback occurs
    qc.cx(0, 1)
    qc.barrier()

    # Readout feature state
    qc.h(0)
    qc.measure(0, 0)
    return qc


qc_classifier = conceptual_classification_circuit()
print("=== REAL-WORLD: PHASE KICKBACK BINARY CLASSIFICATION ===")
print("Conceptual Decision Circuit Diagram:")
print(qc_classifier.draw(output="text"))
print()
print(
    "Conceptual Mapping:\n"
    "1. Feature Encoding: Qubit q0 represents the superposition of feature states.\n"
    "2. Boundary Oracle: The controlled operation queries whether an input falls\n"
    "   above or below a separation hyperplane.\n"
    "3. Phase Kickback: The target ancilla |-> imparts a -1 phase tag to\n"
    "   samples satisfying the classification criterion without measuring them.\n"
    "4. Interference Readout: The final Hadamard maps this phase tag directly\n"
    "   to an observable computational basis outcome (0 for Class A, 1 for Class B)."
)