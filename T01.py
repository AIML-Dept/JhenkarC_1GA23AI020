import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

# 1. Create a circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# 2. Apply a Hadamard gate to qubit 0
qc.h(0)

# 3. Measure qubit 0 into classical bit 0
qc.measure(0, 0)

# 4. Instantiate the Aer Simulator
simulator = AerSimulator()

# 5. Execute the circuit for 1024 shots
job = simulator.run(qc, shots=1024)
result = job.result()

# 6. Retrieve measurement outcomes (counts)
counts = result.get_counts()
print("Measurement Counts:", counts)

# 7. Plot and display the histogram
fig = plot_histogram(counts)
plt.show()

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# Draws using Matplotlib once pylatexenc is present
qc.draw(output="mpl")
plt.show()