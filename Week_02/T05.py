import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector


def build_and_validate_qubit(theta: float, phi: float):
    print(
        f"--- Parametric State Construction (θ = {theta:.4f}, φ = {phi:.4f}) ---"
    )

    # 1. Manual / Theoretical Calculation:
    # |ψ⟩ = cos(θ/2)|0⟩ + e^(i*φ) * sin(θ/2)|1⟩
    c0 = np.cos(theta / 2.0)
    c1 = np.exp(1j * phi) * np.sin(theta / 2.0)
    manual_statevector = np.array([c0, c1])

    # 2. Qiskit Construction using Universal Rotation Gate U(theta, phi, lambda=0)
    qc = QuantumCircuit(1)
    qc.u(theta, phi, 0, 0)
    qiskit_statevector = Statevector(qc).data

    # 3. Print Circuit Diagram
    print("\nCircuit Diagram:")
    print(qc.draw(output="text"))

    # 4. Display both Statevectors
    print(f"\nTheoretical Statevector: {manual_statevector}")
    print(f"Qiskit Statevector:      {qiskit_statevector}")

    # 5. Programmatic Validation
    is_matching = np.allclose(manual_statevector, qiskit_statevector)
    print(f"\nValidation Verdict: {'MATCH SUCCESSFUL' if is_matching else 'MISMATCH'}")

    # 6. Plot Bloch Sphere
    plot_bloch_multivector(qiskit_statevector)
    plt.show()


# Example Execution: θ = π/3 (~60°), φ = π/4 (45°)
build_and_validate_qubit(theta=np.pi / 3, phi=np.pi / 4)