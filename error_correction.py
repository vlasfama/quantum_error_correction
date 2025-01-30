# Importing required modules
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Function to encode the bit-flip code
def encode_bit_flip(qc, qubit):
    # Encoding the qubit using two ancilla qubits
    qc.cx(qubit, qubit + 1)
    qc.cx(qubit, qubit + 2)

# Function to induce a bit-flip error on a qubit
def induce_bit_flip_error(qc, qubit):
    qc.x(qubit)  # Apply X (bit-flip) gate to induce an error

# Function to correct bit-flip errors using majority voting
def correct_bit_flip(qc, qubit):
    # Measure majority vote using ancilla qubits
    qc.cx(qubit, qubit + 1)
    qc.cx(qubit, qubit + 2)
    qc.ccx(qubit + 1, qubit + 2, qubit)

# Function to encode the phase-flip code
def encode_phase_flip(qc, qubit):
    # Encoding for phase flip
    qc.h(qubit)  # Hadamard transform
    encode_bit_flip(qc, qubit)  # Use same bit-flip encoding trick
    qc.h(qubit)

# Function to induce a phase-flip error on a qubit
def induce_phase_flip_error(qc, qubit):
    qc.z(qubit)  # Apply Z (phase-flip) gate to induce an error

# Function to correct phase-flip errors using the bit-flip technique in the Hadamard basis
def correct_phase_flip(qc, qubit):
    qc.h(qubit)
    correct_bit_flip(qc, qubit)
    qc.h(qubit)

# Main simulation function
def simulate_error_correction(error_type="bit-flip"):
    # Initialize quantum circuit with 3 qubits (1 data + 2 ancillas)
    qc = QuantumCircuit(3, 1)  # 1 classical bit for final measurement

    # Initialize the qubit to |1>
    qc.x(0)

    if error_type == "bit-flip":
        encode_bit_flip(qc, 0)
        induce_bit_flip_error(qc, 0)  # Introduce an error
        correct_bit_flip(qc, 0)  # Correct the error
    elif error_type == "phase-flip":
        encode_phase_flip(qc, 0)
        induce_phase_flip_error(qc, 0)  # Introduce an error
        correct_phase_flip(qc, 0)  # Correct the error

    # Measure the first qubit to verify correction
    qc.measure(0, 0)

    # Visualize the circuit
    print("Quantum Circuit:")
    print(qc.draw())

    # Simulate the circuit using Aer's qasm simulator
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1024).result()
    counts = result.get_counts()

    # Display results
    print("Measurement outcomes:", counts)
    plot_histogram(counts)
    plt.show()

# Run both simulations
print("\nBit-Flip Error Correction:")
simulate_error_correction("bit-flip")

print("\nPhase-Flip Error Correction:")
simulate_error_correction("phase-flip")
