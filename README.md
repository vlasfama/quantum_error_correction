# Quantum Error Correction Simulation

This project demonstrates the implementation of basic quantum error correction using the **bit-flip** and **phase-flip** codes. The simulation encodes a single qubit, introduces errors, and corrects them using quantum circuits, showcasing how quantum error correction can mitigate noise.

## Features

- **Bit-Flip Code:** Detects and corrects bit-flip errors (X-gate).
- **Phase-Flip Code:** Detects and corrects phase-flip errors (Z-gate).
- **Simulation using Qiskit's local simulator** to visualize the effects of error correction.

## Prerequisites

- **Python 3.8 or later**
- **Qiskit**
- **Matplotlib**

## Installation

1. Create and activate a virtual environment using Miniconda:

   ```bash
   conda create -n quantum_env python=3.9
   conda activate quantum_env
   ```

2. Install the required libraries:

   ```bash
   pip install qiskit matplotlib
   ```

## Running the Simulation

1. Clone this repository or copy the code into a Python file, e.g., `quantum_error_correction.py`.

2. Run the script using:

   ```bash
   python error_correction.py
   ```

3. The simulation will display:
   - The quantum circuit used for each error correction.
   - The measurement outcomes.
   - A histogram showing the results of the error correction.

## Project Structure

```plaintext
quantum_error_correction.py  # Main Python script
```

## How It Works

1. **Bit-Flip Code:**
    - The original qubit is encoded using two ancilla qubits.
    - A bit-flip error is induced.
    - The error is corrected using majority voting.

2. **Phase-Flip Code:**
    - The original qubit is encoded using Hadamard gates and the bit-flip procedure.
    - A phase-flip error is induced.
    - The error is corrected using a combination of Hadamard gates and bit-flip error correction.

## Quantum Circuit Overview

The circuit involves the following key components:

- **Encoding:** Redundant encoding to detect and correct errors.
- **Error Induction:** Inducing either a bit-flip or phase-flip error.
- **Correction:** Detecting and fixing errors through gates and measurement.

## Example Output

The simulation will output:

- A quantum circuit diagram.
- Measurement results.
- A histogram showing the corrected states.

## Dependencies

- `qiskit`
- `matplotlib`

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues or pull requests to enhance the project!

## Acknowledgments

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [IBM Quantum](https://quantum-computing.ibm.com/)
