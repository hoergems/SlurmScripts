#!/bin/sh
#
#SBATCH --job-name=EnnlManip
#SBATCH --array=1-4
#SBATCH --time=20:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16000
#SBATCH --mail-type=ALL
#SBATCH --mail-user=hoergems@gmail.com

source /home/hoe01h/.bash_profile
cd /data/hoe01h/WAFRExtension/abt/problems/robot_problem
./nnl_manipulator --cfg /data/hoe01h/WAFRExtension/ConfigFiles/WAFRExtension/SNMExtra/manipulator4DOFFactory$SLURM_ARRAY_TASK_ID.cfg
./serializer -p /datastore/hoe01h/WAFRExtension/SNMExtra/manipulator
