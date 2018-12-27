#!/bin/sh 
# 
#SBATCH --job-name=MovoTableABT 
#SBATCH --array=0-9 
#SBATCH --time=00:10:00 
#SBATCH --nodes=1 
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=1 
#SBATCH --cpu-freq=high 
#SBATCH --mem=8192 
#SBATCH --mail-type=NONE 
#SBATCH --mail-user=hoergems@gmail.com 
source /home/hoe01h/.bash_profile 
source /data/hoe01h/usr/share/oppt/setup.sh 
gzMasterUriPort=`expr 11345 + $SLURM_ARRAY_TASK_ID` 
echo $gzMasterUriPort 
echo 'SLURM ID:'
echo $SLURM_ARRAY_JOB_ID 
export GAZEBO_MASTER_URI=http://localhost:$gzMasterUriPort 
cd /data/hoe01h/oppt_devel/bin 
./abtLite --cfg /home/marcus/PhD/scripts/ConfigFiles/MLMC/MovoTable/cfg/MovoTable_correction_$SLURM_ARRAY_TASK_ID.cfg 
