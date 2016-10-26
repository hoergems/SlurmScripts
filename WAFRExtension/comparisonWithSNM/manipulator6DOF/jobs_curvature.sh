#!/bin/sh
#
#SBATCH --job-name=nnlC6
#SBATCH --time=15:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16000
#SBATCH --mail-type=ALL
#SBATCH --mail-user=hoergems@gmail.com

source /home/hoe01h/.bash_profile
cd /data/hoe01h/WAFRExtension/abt2/problems/robot_problem
./nnl_manipulator --cfg /data/hoe01h/WAFRExtension/ConfigFiles/WAFRExtension/comparisonWithSNM/manipulator6DOF/Curvature/manipulator6DOF.cfg
