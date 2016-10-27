#!/bin/sh
#
#SBATCH --job-name=50rHFR
#SBATCH --array=5-30:5
#SBATCH --time=25:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=8000

#SBATCH --mail-type=ALL
#SBATCH --mail-user=hoergems@gmail.com

source /home/hoe50h/.bash_profile
cd /data/hoe50h/WAFRExtension/abt/problems/robot_problem
./hfr_dubin --cfg /data/hoe50h/WAFRExtension/ConfigFiles/WAFRExtension/ABTHFRDubinRandomObstacles/5.0/dubin$SLURM_ARRAY_TASK_ID.cfg
