import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Inject small rotation errors (delta) into the final Hadamard reconstruction
# Ideal H = RY(pi/2) followed by Z; Imperfect H modeled as RY(pi/2 + delta)
error_deltas = [0.0, 0.1, 0.25, 0.5, 0.8, 1.2]
reliabilities = []
shots = 2000
simulator = AerSimulator()

print("=== CHALLENGE: IMPERFECT HADAMARD RELIABILITY ANALYSIS ===")
print("Delta (rad) | Success P(1) | Error Rate")
print("-" * 40)

for delta in error_deltas:
    # Test on balanced oracle f(x) = x (ideal outcome is bit '1')
    qc_err = QuantumCircuit(2, 1)
    qc_err.x(1)
    qc_err.h(0)
    qc_err.h(1)
    qc_err.barrier()

    # Balanced Oracle
    qc_err.cx(0, 1)
    qc_err.barrier()

    # Imperfect Hadamard transformation: Ry(pi/2 + delta) followed by Phase Z
    # When delta = 0, this approximates standard Hadamard behavior
    qc_err.ry(np.pi / 2 + delta, 0)
    qc_err.z(0)
    qc_err.measure(0, 0)

    counts = simulator.run(qc_err, shots=shots).result().get_counts()
    p_success = counts.get("1", 0) / shots
    reliabilities.append(p_success)
    print(f"{delta:<11.2f} | {p_success:<14.4f} | {1.0 - p_success:.4f}")

# Plotting Reliability Degradation
plt.figure(figsize=(8, 4.5))
bars = plt.bar(
    [str(d) for d in error_deltas],
    reliabilities,
    color="steelblue",
    edgecolor="black",
)
plt.axhline(
    y=0.5,
    color="red",
    linestyle="--",
    label="Random Guess Threshold (P=0.5)",
)
plt.title(
    "Algorithm Reliability Degradation vs. Gate Rotation Error", fontsize=11
)
plt.xlabel("Injected Gate Error Delta (radians)", fontsize=10)
plt.ylabel("Measurement Success Probability P(1)", fontsize=10)
plt.ylim(0, 1.1)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig("deutsch_gate_error.png")
print("\nPlot saved successfully as 'deutsch_gate_error.png'.")