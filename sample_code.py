from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 1. Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# 2. Apply a Hadamard gate to qubit 0 to put it in superposition
qc.h(0)

# 3. Apply a CNOT gate with qubit 0 as control and qubit 1 as target
qc.cx(0, 1)

# 4. Measure both qubits into the classical bits
qc.measure([0, 1], [0, 1])

# 5. Initialize the Aer simulator backend
simulator = AerSimulator()

# 6. Run the circuit on the simulator
job = simulator.run(qc, shots=1000)

# 7. Get and print the counts (results)
result = job.result()
counts = result.get_counts(qc)
print("\nSimulation successful!")
print("Measurement Results (approx. 50% '00' and 50% '11'):")
print(counts)
