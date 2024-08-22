#!/bin/bash
#SBATCH --partition=GPUQ
#SBATCH --account=ie-idi
#SBATCH --time=01:05:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --gres=gpu:a100:4
#SBATCH --constraint="gpu40g|gpu80g|gpu32g"
#SBATCH --mem=12000 # Default units are megabytes.
#SBATCH --job-name="train_vortex_model_1"
#SBATCH --output=train_model_logs.out
module load foss/2022a
module load PyTorch/1.12.0-foss-2022a-CUDA-11.7.0
module load torchvision/0.13.1-foss-2022a-CUDA-11.7.0
module load CUDA/12.0.0
pip install -r requirements.txt
python3 .
