#!/bin/bash
#Submit this script with: sbatch thefilename
#SBATCH --time=01:00:00   # walltime
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --nodes=1
#SBATCH --array=0-19
#SBATCH --mem-per-cpu=1G
#SBATCH -J "parser_example"
#SBATCH --output=grid_examples/parser_example/slurm_out/%x_%A_%a.out
#SBATCH --error=grid_examples/parser_example/slurm_err/%x_%A_%a.err
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL

source ~/myproject_env/bin/activate
cd grid_examples/parser_example

LETTERS=("A" "B" "C" "D")
NUMBERS=(1 2 3 4 5)

N_LETTERS=${#LETTERS[@]}
N_NUMBERS=${#NUMBERS[@]}
N_TASKS=$((N_LETTERS * N_NUMBERS))

IDX=${SLURM_ARRAY_TASK_ID}

NUMBER=${NUMBERS[$((IDX % N_NUMBERS))]}
LETTER=${LETTERS[$((IDX / N_NUMBERS))]}

echo "Running LETTER=${LETTER}, NUMBER=${NUMBER}"

python parser_example_main.py \
  --letter "${LETTER}" \
  --number "${NUMBER}"



