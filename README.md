# Grid Computing Examples

This repository provides five complementary examples demonstrating how to use grid computing with SLURM. Each example illustrates different aspects and capabilities of the grid environment.

## Repository Structure

### Example Folders

All examples follow a consistent structure within the `grid_examples` folder:

```
grid_examples/
├── X_example/
│   ├── X_example_instruction.slurm    # SLURM job submission script
│   ├── X_example_main.py              # Python code to be executed
│   ├── output/                        # Output files from the code
│   ├── slurm_out/                     # Standard output from SLURM
│   └── slurm_err/                     # Error messages from SLURM
```

### Gurobi License Configuration

The repository includes Gurobi license management files in the main directory:
- `gurobi_licenses_assignment.py` - Script for license assignment
- `gurobi_lic/` - Folder containing subfolders for each grid node with its unique Gurobi license

**Note:** Each grid node must have a unique Gurobi license.

## Examples

### 1. Basic Example (`basic_example`)
A simple example that creates a CSV file to verify basic operations are working correctly.

**Command:**
```bash
sbatch grid_examples/basic_example/basic_example_instruction.slurm
```

### 2. Parser Example (`parser_example`)
Demonstrates how to create an array of jobs that can run in parallel for faster computation.

**Command:**
```bash
sbatch grid_examples/parser_example/parser_example_instruction.slurm
```

**Requirements:** Activate the virtual environment
```bash
source ~/myproject_env/bin/activate
```

### 3. Neural Network Example (`neuralnet_example`)
Shows how to run deep learning or deep reinforcement learning code that requires specific node constraints.

**Special Requirements:**
- Uses AVX-enabled nodes via `#SBATCH --constraint=AVX`
- Virtual environment activation required

**Command:**
```bash
sbatch grid_examples/neuralnet_example/neuralnet_example_instruction.slurm
```

### 4. Jupyter Example (`jupyter_example`)
Creates both an unexecuted Jupyter notebook and a version with pre-executed code.

**Command:**
```bash
sbatch grid_examples/jupyter_example/jupyter_example_instruction.slurm
```

**Requirements:** Activate the virtual environment

### 5. Gurobi Example (`gurobi_example`)
Demonstrates Gurobi license assignment and running optimization code with Gurobi.

**Command:**
```bash
sbatch grid_examples/gurobi_example/gurobi_example_instruction.slurm
```

**Requirements:** Activate the virtual environment

## Environment Setup

Most examples (all except `basic_example`) require activating a Python virtual environment with the necessary packages:

```bash
source ~/myproject_env/bin/activate
```

The `myproject_env` folder should be visible in the grid main page.

## Expected Output

The `grid_examples_executed` folder contains the expected output after running all examples successfully. Use this to verify your results.

## Quick Start

1. Ensure your virtual environment is set up at `~/myproject_env/`
2. If using Gurobi, ensure licenses are properly configured in `gurobi_lic/`
3. Submit jobs using the commands listed above
4. Check output in the respective `output/`, `slurm_out/`, and `slurm_err/` folders
5. Compare your results with `grid_examples_executed/`
