#!/bin/sh
#
#SBATCH --job-name=Manip
#SBATCH --array=0-30:10
#SBATCH --time=05:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16000

#SBATCH --mail-type=ALL
#SBATCH --mail-user=hoergems@gmail.com

source /home/hoe01h/.bash_profile
cd /data/hoe01h/WAFRExtension/abt/problems/robot_problem
./measureCompareObst_manipulator --cfg /data/hoe01h/WAFRExtension/ConfigFiles/WAFRExtension/measureCompare/manipulator2/manipulator4DOF$SLURM_ARRAY_TASK_ID.cfg
