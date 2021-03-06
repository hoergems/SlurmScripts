#!/bin/sh
#
#SBATCH --job-name=Dub
#SBATCH --array=0-30:10
#SBATCH --time=03:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16000

#SBATCH --mail-type=ALL
#SBATCH --mail-user=hoergems@gmail.com

source /home/hoe01h/.bash_profile
cd /data/hoe01h/WAFRExtension/abt/problems/robot_problem
./measureCompareObst_dubin --cfg /data/hoe01h/WAFRExtension/ConfigFiles/WAFRExtension/measureCompare/dubin3/dubin$SLURM_ARRAY_TASK_ID.cfg
