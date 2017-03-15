#!/bin/sh
#
#SBATCH --job-name=15DubinABT
#SBATCH --array=0-99
#SBATCH --time=00:20:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=4096
#SBATCH --mail-type=ALL
#SBATCH --mail-user=hoergems@gmail.com

source /home/hoe01h/.bash_profile
cd /data/hoe01h/Downloads/frapu/abt/problems/robot_problem
./abt_dubin --cfg /data/hoe01h/Downloads/frapu/ConfigFiles/WAFRJournal/randomScene/Dubin/collisionsNotAllowed/30_obstacles/cfg/10/dubin$SLURM_ARRAY_TASK_ID.cfg
