#!/bin/bash
#Submit this script with: sbatch thefilename
#SBATCH --time=01:00:00   # walltime
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --nodes=1
#SBATCH --constraint=AVX
#SBATCH --mem-per-cpu=1G
#SBATCH -J "neuralnet_example"
#SBATCH --output=grid_examples/neuralnet_example/slurm_out/%x_%A_%a.out
#SBATCH --error=grid_examples/neuralnet_example/slurm_err/%x_%A_%a.err
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL

source ~/myproject_env/bin/activate
cd grid_examples/neuralnet_example

python neuralnet_example_main.py