#!/bin/sh
#
#SBATCH --job-name=hfrOMan
#SBATCH --array=1-2
#SBATCH --time=30:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16000
#SBATCH --mail-type=ALL
#SBATCH --mail-user=hoergems@gmail.com

source /home/hoe01h/.bash_profile
cd /data/hoe01h/WAFRExtension/abt/problems/robot_problem
./hfr_manipulator --cfg /data/hoe01h/WAFRExtension/ConfigFiles/WAFRExtension/experiments1/manipulatorOld/manipulator4DOFFactory$SLURM_ARRAY_TASK_ID.cfg
