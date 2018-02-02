#!/bin/sh 
# 
#SBATCH --job-name=calcHeuristicSamples
#SBATCH --array=0-9 
#SBATCH --time=07:25:00 
#SBATCH --nodes=1 
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=7 
#SBATCH --mem=12000 
#SBATCH --mail-type=NONE 
#SBATCH --mail-user=hoergems@gmail.com 
source /home/hoe01h/.bash_profile 
gzMasterUriPort=`expr 11345 + $SLURM_ARRAY_TASK_ID` 
echo $gzMasterUriPort 
export GAZEBO_MASTER_URI=http://localhost:$gzMasterUriPort 
export OPPT_RESOURCE_PATH=$OPPT_RESOURCE_PATH:/data/hoe01h/oppt_devel/files/ 
export OPPT_RESOURCE_PATH=$OPPT_RESOURCE_PATH:/data/hoe01h/gazebo_models/models/randomScenes/Dubin 
cd /data/hoe01h/oppt_devel/bin 
./calcHeuristicSamples --cfg /flush1/hoe01h/ConfigFiles/approximateDynamics/4DOFFactory1ApproxMax$SLURM_ARRAY_TASK_ID.cfg
