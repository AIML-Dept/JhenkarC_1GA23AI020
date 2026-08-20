import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from scipy import stats

qc_qrbg = QuantumCircuit(1, 1)
qc_qrbg.h(0)
qc_qrbg.measure(0, 0)

print("=== CHALLENGE: STATISTICAL HYPOTHESIS TESTING ===")
print("Circuit Diagram (QRBG):")
print(qc_qrbg.draw(output="text"))
print()

total_samples = 1000
simulator = AerSimulator()
q_result = (
    simulator.run(qc_qrbg, shots=total_samples, memory=True)
    .result()
    .get_memory()
)
quantum_bits = [int(b) for b in q_result]

np.random.seed(42)
biased_classical_bits = np.random.choice(
    [0, 1], size=total_samples, p=[0.46, 0.54]
)
expected_freq = [total_samples / 2, total_samples / 2]


def evaluate_generator(name, bits):
    observed_0 = bits.count(0) if isinstance(bits, list) else np.sum(bits == 0)
    observed_1 = bits.count(1) if isinstance(bits, list) else np.sum(bits == 1)
    chi2_stat, p_value = stats.chisquare(
        f_obs=[observed_0, observed_1], f_exp=expected_freq
    )
    print(
        f"--- {name} ---\nCounts 0: {observed_0}, 1: {observed_1} | P-Value: {p_value:.4f}"
    )


evaluate_generator("Quantum Random Generator", quantum_bits)
evaluate_generator("Biased Classical PRNG", biased_classical_bits)