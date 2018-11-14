import sys
import os
import subprocess
import glob
import argparse
import fileinput
import shutil

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-np', '--numParallelJobs', type=int, default=10,
                    help='Number of obstacles')
parser.add_argument('-nr', '--numRuns', type=int, default=100,
                    help='Number of runs')
parser.add_argument('-r', '--robotProblem', type=str, default="Dubin", help="The robot problem")
parser.add_argument('-m', '--memory', type=str, default="4096", help="The amout of memory requested per job")
parser.add_argument('-cf', '--configFolder', type=str, required=True, help="Path where the config files are stored in")

args = parser.parse_args()

numParallelJobs = args.numParallelJobs
numRuns = args.numRuns
memory = args.memory
configFolder = args.configFolder
if (configFolder.strip()[-1] != "/"):
    configFolder += "/"

robot = args.robotProblem
robotExec = "robot"

shared_path = os.path.dirname(os.path.abspath(__file__))

folder = "mlmc"
if os.path.isdir(folder):
    shutil.rmtree(folder)
os.makedirs(folder)

# Create the scripts for ABT
for k in xrange(0, numRuns/numParallelJobs):
	string = "#!/bin/sh \n"
	string += "# \n"
	string += "#SBATCH --job-name="
	string += robot + "ABT \n"
	string += "#SBATCH --array="
	string += str(k * numParallelJobs) + "-" + str(k * numParallelJobs + numParallelJobs-1) + " \n"
	string += "#SBATCH --time=00:10:00 \n"
	string += "#SBATCH --nodes=1 \n"
	string += "#SBATCH --ntasks=1 \n"
    string += "#SBATCH --cpus-per-task=4 \n"
    string += "#SBATCH --mem=" + memory + " \n"
    string += "#SBATCH --mail-type=NONE \n"
    string += "#SBATCH --mail-user=hoergems@gmail.com \n"
    string += "source /home/hoe01h/.bash_profile \n"
    string += "source /data/hoe01h/usr/share/oppt/setup.sh \n"
    string += "gzMasterUriPort=`expr 11345 + $SLURM_ARRAY_TASK_ID` \n"
    string += "echo $gzMasterUriPort \n"
    string += "export GAZEBO_MASTER_URI=http://localhost:$gzMasterUriPort \n"
    string += "cd /data/hoe01h/oppt_devel/bin \n"
    string += "./abt --cfg " + configFolder + robot + "/cfg"
    string += "/" + robot + "_$SLURM_ARRAY_TASK_ID.cfg \n"
    if (os.path.exists(folder + "/jobs_abt_" + robot + "_" + str(k) + ".sh")):
        os.remove(folder + "/jobs_abt_" + robot + "_" + str(k) + ".sh")
    with open(folder + "/jobs_abt_" + robot + "_" + str(k) + ".sh", 'a+') as f:
        f.write(string)
print "HELLO"

print str(numRuns/numParallelJobs)
		
shutil.copyfile("run.sh", folder + "/run.sh")
os.system("chmod +x " + folder + "/run.sh")
for line in fileinput.input(folder + "/run.sh", inplace=1):
    if "endIndex=11" in line:
        line = "endIndex=" + str(1 + 1) + "\n"
    elif "for ((a=0;" in line:
        line = "  for ((a=0; a < " + str(numRuns/numParallelJobs) + "; a++))\n"
    elif "folder=0" in line:
        line = "folder=mlmc\n"
    sys.stdout.write(line)