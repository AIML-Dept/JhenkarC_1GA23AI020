import random
import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from scipy.stats import chisquare

# Parameters
NUM_SAMPLES = 2048  # Number of random 8-bit integers to generate
NUM_QUBITS = 8      # 8 qubits generate numbers between 0 and 255 (2^8 = 256)
NUM_BINS = 2**NUM_QUBITS

# -------------------------------------------------------------
# 1. Classical PRNG (Python's Mersenne Twister)
# -------------------------------------------------------------
random.seed(42)  # Seeded for reproducibility demonstration
prng_samples = [random.getrandbits(NUM_QUBITS) for _ in range(NUM_SAMPLES)]

# -------------------------------------------------------------
# 2. Quantum RNG (8-Qubit Superposition)
# -------------------------------------------------------------
qc = QuantumCircuit(NUM_QUBITS, NUM_QUBITS)
qc.h(range(NUM_QUBITS))  # Put all 8 qubits in equal superposition
qc.measure(range(NUM_QUBITS), range(NUM_QUBITS))

simulator = AerSimulator()
# Run simulator for NUM_SAMPLES shots
job = simulator.run(qc, shots=NUM_SAMPLES, memory=True)
result = job.result()
# Extract each individual bitstring and convert to integer
bitstrings = result.get_memory()
qrng_samples = [int(bits, 2) for bits in bitstrings]

# -------------------------------------------------------------
# 3. Statistical Analysis & Testing
# -------------------------------------------------------------
def analyze_randomness(name, samples):
    # Bin counts for each integer 0-255
    counts, _ = np.histogram(samples, bins=NUM_BINS, range=(0, NUM_BINS))
    
    # Expected frequency per bin under uniform distribution
    expected_freq = NUM_SAMPLES / NUM_BINS
    
    # Chi-Square Test (Null hypothesis: sample follows uniform distribution)
    chi2_stat, p_val = chisquare(counts)
    
    # Shannon Entropy Calculation (Max entropy for 8 bits = 8.0)
    probabilities = counts / NUM_SAMPLES
    probabilities = probabilities[probabilities > 0]
    shannon_entropy = -np.sum(probabilities * np.log2(probabilities))
    
    print(f"=== {name} Analysis ===")
    print(f"  Mean Value      : {np.mean(samples):.2f} (Theoretical: 127.5)")
    print(f"  Std Deviation   : {np.std(samples):.2f} (Theoretical: ~73.9)")
    print(f"  Shannon Entropy : {shannon_entropy:.4f} / 8.0000 bits")
    print(f"  Chi-Square Stat : {chi2_stat:.2f}")
    print(f"  p-value         : {p_val:.4f} (p > 0.05 indicates uniform distribution)\n")
    return counts

counts_prng = analyze_randomness("Python PRNG (Mersenne Twister)", prng_samples)
counts_qrng = analyze_randomness("Quantum RNG (Simulated)", qrng_samples)

# -------------------------------------------------------------
# 4. Visualization
# -------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 4), sharey=True)

axes[0].bar(range(NUM_BINS), counts_prng, color='crimson', alpha=0.7, width=1.0)
axes[0].set_title("Python PRNG Distribution")
axes[0].set_xlabel("8-bit Integer (0-255)")
axes[0].set_ylabel("Frequency")
axes[0].axhline(NUM_SAMPLES/NUM_BINS, color='black', linestyle='--', label='Expected Uniform')
axes[0].legend()

axes[1].bar(range(NUM_BINS), counts_qrng, color='mediumpurple', alpha=0.7, width=1.0)
axes[1].set_title("Simulated QRNG Distribution")
axes[1].set_xlabel("8-bit Integer (0-255)")
axes[1].axhline(NUM_SAMPLES/NUM_BINS, color='black', linestyle='--', label='Expected Uniform')
axes[1].legend()

plt.tight_layout()
plt.show()