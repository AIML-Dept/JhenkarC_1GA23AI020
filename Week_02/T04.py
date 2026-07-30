import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

# 1. Create ideal (clean) circuit and prepare state |+>
clean_qc = QuantumCircuit(1)
clean_qc.h(0)

clean_state = Statevector(clean_qc)

# 2. Model noisy channel: apply a random phase error delta around the Z-axis
delta_phase = np.random.uniform(0.1, 0.5)  # Random error between ~5.7° and 28.6°

noisy_qc = QuantumCircuit(1)
noisy_qc.h(0)
noisy_qc.rz(delta_phase, 0)  # Inject random phase rotation (phase noise)

noisy_state = Statevector(noisy_qc)

# 3. Print circuits and state outputs
print("--- Clean Circuit ---")
print(clean_qc.draw(output="text"))
print("Clean Statevector:", clean_state.data)

print("\n--- Noisy Channel Circuit ---")
print(noisy_qc.draw(output="text"))
print(f"Applied Random Phase Error (δ): {delta_phase:.4f} radians")
print("Noisy Statevector:", noisy_state.data)

# 4. Visualizations on Bloch sphere
fig_clean = plot_bloch_multivector(clean_state, title="Ideal State (|-+⟩)")
fig_noisy = plot_bloch_multivector(
    noisy_state, title=f"Noisy Channel State (Phase Shift = {delta_phase:.3f} rad)"
)

plt.show()