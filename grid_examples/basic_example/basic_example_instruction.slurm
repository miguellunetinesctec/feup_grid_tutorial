#!/bin/bash
#Submit this script with: sbatch thefilename
#SBATCH --time=01:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH -p batch   # partition(s)
#SBATCH --mem-per-cpu=1G   # memory per CPU core
#SBATCH -J "basic_example"   # job name
#SBATCH --output=grid_examples/basic_example/slurm_out/%x_%A_%a.out
#SBATCH --error=grid_examples/basic_example/slurm_err/%x_%A_%a.err
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL
# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE
cd grid_examples/basic_example
python3 basic_example_main.py