import qiskit
from qiskit_aer import Aer

# 1. Print Qiskit Version
print(f"Qiskit Version: {qiskit.__version__}")

# 2. List Available Local Aer Backends
print("\nAvailable Aer Backends:")
backends = Aer.backends()
for backend in backends:
    print(f" - {backend.name}")