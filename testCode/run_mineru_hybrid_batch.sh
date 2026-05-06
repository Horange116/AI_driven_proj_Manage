#!/bin/bash
#SBATCH -J mineru_hybrid_full
#SBATCH -p A800Z
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --qos=qmultiple9
#SBATCH -o /home/s2025244189/s2025244265/AI_driven_proj_Manage/logs/mineru_hybrid_%j.out
#SBATCH -e /home/s2025244189/s2025244265/AI_driven_proj_Manage/logs/mineru_hybrid_%j.err

set -euo pipefail

cd /home/s2025244189/s2025244265/AI_driven_proj_Manage

echo "Started at: $(date)"
echo "Host: $(hostname)"
echo "CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-}"

export PYTHONUNBUFFERED=1

python -u testCode/run_mineru_hybrid_batch.py --model-source local

echo "Finished at: $(date)"
