#!/bin/sh
#
#SBATCH --job-name=abtDubin1
#SBATCH --array=1-4
#SBATCH --time=08:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=4096
#SBATCH --mail-type=ALL
#SBATCH --mail-user=hoergems@gmail.com

source /home/hoe01h/.bash_profile
cd /data/hoe01h/WAFRExtension/abt2/problems/robot_problem
./abt_dubin --cfg /data/hoe01h/WAFRExtension/ConfigFiles/WAFRExtension/emptyEnvironmentABTHFR/dubin/distanceHeuristic/dubin$SLURM_ARRAY_TASK_ID.cfg
