#!/bin/bash
#Submit this script with: sbatch thefilename
#SBATCH --time=00:01:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH -p batch   # partition(s)
#SBATCH --nodelist=ava20
#SBATCH --mem-per-cpu=1G   # memory per CPU core
#SBATCH -J "gurobi_example"   # job name
#SBATCH --output=grid_examples/gurobi_example/slurm_out/%x_%A_%a.out
#SBATCH --error=grid_examples/gurobi_example/slurm_err/%x_%A_%a.err
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL

source ~/myproject_env/bin/activate
# Set the Gurobi license path dynamically
export GRB_LICENSE_FILE="/homes/up202005556/gurobi_lic/${HOSTNAME}/gurobi.lic"

# Call the Python script to assign the Gurobi license
python gurobi_licenses_assignment.py

cd grid_examples/gurobi_example
python gurobi_example_main.py
