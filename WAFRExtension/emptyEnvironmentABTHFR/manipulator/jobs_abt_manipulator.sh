#!/bin/sh
#
#SBATCH --job-name=abtMan
#SBATCH --array=1-4
#SBATCH --time=10:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=4096
#SBATCH --mail-type=ALL
#SBATCH --mail-user=hoergems@gmail.com

source /home/hoe01h/.bash_profile
cd /data/hoe01h/WAFRExtension/abt/problems/robot_problem
./abt_manipulator --cfg /data/hoe01h/WAFRExtension/ConfigFiles/WAFRExtension/emptyEnvironmentABTHFR/manipulator/manipulator4DOFEmpty$SLURM_ARRAY_TASK_ID.cfg
