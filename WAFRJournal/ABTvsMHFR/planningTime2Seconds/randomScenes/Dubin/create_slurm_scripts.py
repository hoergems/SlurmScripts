import sys
import os
import subprocess
import glob
import argparse
import fileinput
import shutil

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-nO', '--numObstacles', type=int, default=5,
                    help='Number of obstacles')
parser.add_argument('-nP', '--numParallelJobs', type=int, default=10,
                    help='Number of obstacles')
parser.add_argument('-nc', '--numCovarianceSteps', type=int, default=10,
                    help='Number of covariance steps')
parser.add_argument('-nr', '--numRuns', type=int, default=100,
                    help='Number of runs')
parser.add_argument('-r', '--robotProblem', type=str, default="Dubin", help="The robot problem")
parser.add_argument('-m', '--memory', type=str, default="4096", help="The amout of memory requested per job")
parser.add_argument('-cf', '--configFolder', type=str, required=True, help="Path where the config files are stored in")

args = parser.parse_args()

numObstacles = args.numObstacles
numParallelJobs = args.numParallelJobs
numConvarianceSteps = args.numCovarianceSteps
numRuns = args.numRuns
memory = args.memory
configFolder = args.configFolder
if (configFolder.strip()[-1] != "/"):
    configFolder += "/"

robot = args.robotProblem
robotExec = "robot"

shared_path = os.path.dirname(os.path.abspath(__file__))

folder = str(numObstacles) + "_obstacles"
if os.path.isdir(folder):
    shutil.rmtree(folder)
os.makedirs(folder)

# Create the scripts for ABT
for k in xrange(0, numRuns/numParallelJobs):	    
    string = "#!/bin/sh \n"
    string += "# \n"
    string += "#SBATCH --job-name=" + str(numObstacles)
    string += robot + "ABT \n"
    string += "#SBATCH --array="
    string += str(k * numParallelJobs) + "-" + str(k * numParallelJobs + numParallelJobs-1) + " \n"
    string += "#SBATCH --time=00:20:00 \n"
    string += "#SBATCH --nodes=1 \n"
    string += "#SBATCH --ntasks=1 \n"
    string += "#SBATCH --mem=" + memory + " \n"
    string += "#SBATCH --mail-type=NONE \n"
    string += "#SBATCH --mail-user=hoergems@gmail.com \n"
    string += "source /home/hoe01h/.bash_profile \n"
    string += "source /data/hoe01h/gazebo_models/setup.sh \n"
    string += "gzMasterUriPort=`expr 11345 + $SLURM_ARRAY_TASK_ID` \n"
    string += "echo $gzMasterUriPort \n"
    string += "export GAZEBO_MASTER_URI=http://localhost:$gzMasterUriPort \n"
    string += "export OPPT_RESOURCE_PATH=${OPPT_RESOURCE_PATH}:/data/hoe01h/gazebo_models/models/randomScenes/Dubin \n"
    string += "export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:/data/hoe01h/gazebo_models/models/randomScenes/Dubin \n"
    string += "cd /data/hoe01h/oppt_devel/bin \n"
    ff = configFolder + robot + "/cfg/" + str(numObstacles) + "_obstacles/" + robot + "_$SLURM_ARRAY_TASK_ID.cfg"
    string += "./abt --cfg " + ff + " \n"    
    print folder
    if not os.path.exists(folder):
	os.makedirs(folder)
    with open(folder + "/jobs_abt_" + robot + "_" + str(k) + ".sh", 'a+') as f:
	f.write(string)
		
# Create the scripts for MHFR
for k in xrange(0, numRuns/numParallelJobs):	    
    string = "#!/bin/sh \n"
    string += "# \n"
    string += "#SBATCH --job-name=" + str(numObstacles)
    string += robot + "MHFR \n"
    string += "#SBATCH --array="
    string += str(k * numParallelJobs) + "-" + str(k * numParallelJobs + numParallelJobs-1) + " \n"
    string += "#SBATCH --time=00:20:00 \n"
    string += "#SBATCH --nodes=1 \n"
    string += "#SBATCH --ntasks=1 \n"
    string += "#SBATCH --cpus-per-task=8 \n"
    string += "#SBATCH --mem=" + memory + " \n"
    string += "#SBATCH --mail-type=NONE \n"
    string += "#SBATCH --mail-user=hoergems@gmail.com \n"
    string += "source /home/hoe01h/.bash_profile \n"
    string += "source /data/hoe01h/gazebo_models/setup.sh \n"
    string += "gzMasterUriPort=`expr 11345 + $SLURM_ARRAY_TASK_ID` \n"
    string += "echo $gzMasterUriPort \n"
    string += "export GAZEBO_MASTER_URI=http://localhost:$gzMasterUriPort \n"
    string += "export OPPT_RESOURCE_PATH=${OPPT_RESOURCE_PATH}:/data/hoe01h/gazebo_models/models/randomScenes/Dubin \n"
    string += "export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:/data/hoe01h/gazebo_models/models/randomScenes/Dubin \n"
    string += "cd /data/hoe01h/oppt_devel/bin \n"
    ff = configFolder + robot + "/cfg/" + str(numObstacles) + "_obstacles/" + robot + "_$SLURM_ARRAY_TASK_ID.cfg"
    string += "./mhfr --cfg " + ff + " \n"    
    print folder
    if not os.path.exists(folder):
	os.makedirs(folder)
    with open(folder + "/jobs_mhfr_" + robot + "_" + str(k) + ".sh", 'a+') as f:
	f.write(string)
		
shutil.copyfile("run.sh", folder + "/run.sh")
os.system("chmod +x " + folder + "/run.sh")
for line in fileinput.input(folder + "/run.sh", inplace=1):
    if "endIndex=11" in line:
	line = "endIndex=" + str(numConvarianceSteps + 1) + "\n"	
    elif "for ((a=0;" in line:
	line = "  for ((a=0; a < " + str(numRuns/numParallelJobs) + "; a++))\n"
    sys.stdout.write(line)
