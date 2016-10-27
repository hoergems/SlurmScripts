#!/bin/sh
#
#SBATCH --job-name=25rHFR
#SBATCH --array=5-30:5
#SBATCH --time=25:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=8000

#SBATCH --mail-type=ALL
#SBATCH --mail-user=hoergems@gmail.com

source /home/hoe25h/.bash_profile
cd /data/hoe25h/WAFRExtension/abt/problems/robot_problem
./hfr_dubin --cfg /data/hoe25h/WAFRExtension/ConfigFiles/WAFRExtension/ABTHFRDubinRandomObstacles/2.5/dubin$SLURM_ARRAY_TASK_ID.cfg
