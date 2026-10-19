import time

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

start_time = time.perf_counter()

n = 20  # Number of qubits

qc = QuantumCircuit(n)

#GHZ state
qc.h(0)

for i in range(0, n - 1):
    qc.cx(i, i + 1)

qc.measure_all()

simulator = AerSimulator()
job = simulator.run(qc, shots=1024)

result = job.result()
counts = result.get_counts(qc)
print("\nSimulation successful!")
print("Measurement Results")
print(counts)
elapsed_time = time.perf_counter() - start_time
print(f"Runtime: {elapsed_time:.6f} seconds")
