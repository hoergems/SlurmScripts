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
parser.add_argument('-r', '--robot', type=str, default="Dubin", help="The robot")
parser.add_argument('-m', '--memory', type=str, default="4096", help="The amout of memory requested per job")
parser.add_argument('-f', '--folder', type=str, default="collisionsNotAllowed", help="Folder prefix")

args = parser.parse_args()

numObstacles = args.numObstacles
numParallelJobs = args.numParallelJobs
numConvarianceSteps = args.numCovarianceSteps
numRuns = args.numRuns
memory = args.memory
folderPrefix = args.folder

robot = args.robot
robotExec = "dubin"
if (robot == "4DOF"):
    robotExec = "robot"

shared_path = os.path.dirname(os.path.abspath(__file__))

folder = str(numObstacles) + "_obstacles"
if os.path.isdir(folder):
    shutil.rmtree(folder)
os.makedirs(folder)

# Create the scripts for ABT
for i in xrange(1, numConvarianceSteps + 1):
    for j in xrange(0, numRuns/numParallelJobs):
        string = "#!/bin/sh \n"
        string += "# \n"
        string += "#SBATCH --job-name=" + str(numObstacles)
        string += robot + "ABT \n"
        string += "#SBATCH --array="
        string += str(j * numParallelJobs) + "-" + str(j * numParallelJobs + numParallelJobs-1) + " \n"
        string += "#SBATCH --time=00:20:00 \n"
        string += "#SBATCH --nodes=1 \n"
        string += "#SBATCH --ntasks=1 \n"
        string += "#SBATCH --mem=" + memory + " \n"
        string += "#SBATCH --mail-type=ALL \n"
        string += "#SBATCH --mail-user=hoergems@gmail.com \n"
        string += "source /home/hoe01h/.bash_profile \n"
        string += "cd /data/hoe01h/Downloads/frapu/abt2/abt/bin \n"
        string += "./abt_" + robotExec + " --cfg /data/hoe01h/Downloads/frapu/ConfigFiles/WAFRJournal/randomScene/" + robot + "/" + folderPrefix + "/"
        string += str(numObstacles)
        string += "_obstacles/cfg/"
        string += str(i)
        string += "/" + robot + "$SLURM_ARRAY_TASK_ID.cfg \n"        
        if not os.path.exists(folder + "/" + str(i)):
	    os.makedirs(folder + "/" + str(i))
	if (os.path.exists(folder + "/" + str(i) + "/jobs_abt_" + robot + "_" + str(j) + ".sh")):
	    os.remove(folder + "/" + str(i) + "/jobs_abt_" + robot + "_" + str(j) + ".sh")
	with open(folder + "/" + str(i) + "/jobs_abt_" + robot + "_" + str(j) + ".sh", 'a+') as f:
	    f.write(string)
	  
#Create the scripts for MHFR
for i in xrange(1, numConvarianceSteps + 1):
    for j in xrange(0, numRuns/numParallelJobs):
	string = "#!/bin/sh \n"
        string += "# \n"
        string += "#SBATCH --job-name=" + str(numObstacles)
        string += robot + "MHFR \n"
        string += "#SBATCH --array="
        string += str(j * numParallelJobs) + "-" + str(j * numParallelJobs + numParallelJobs-1) + " \n"        
        string += "#SBATCH --time=00:20:00 \n"
        string += "#SBATCH --nodes=1 \n"
        string += "#SBATCH --ntasks=1 \n"
        string += "#SBATCH --cpus-per-task=8 \n"
        string += "#SBATCH --mem=" + memory + " \n"
        string += "#SBATCH --mail-type=ALL \n"
        string += "#SBATCH --mail-user=hoergems@gmail.com \n"
        string += "source /home/hoe01h/.bash_profile \n"
        string += "cd /data/hoe01h/Downloads/frapu/abt2/abt/bin \n"
        string += "./hfr_" + robotExec + " --cfg /data/hoe01h/Downloads/frapu/ConfigFiles/WAFRJournal/randomScene/" + robot + "/" + folderPrefix + "/"
        string += str(numObstacles)
        string += "_obstacles/cfg/"
        string += str(i)
        string += "/" + robot + "$SLURM_ARRAY_TASK_ID.cfg \n"
        if not os.path.exists(folder + "/" + str(i)):
	    os.makedirs(folder + "/" + str(i))
	if (os.path.exists(folder + "/" + str(i) + "/jobs_mhfr_" + robot + "_" + str(j) + ".sh")):
	    os.remove(folder + "/" + str(i) + "/jobs_mhfr_" + robot + "_" + str(j) + ".sh")
	with open(folder + "/" + str(i) + "/jobs_mhfr_" + robot + "_" + str(j) + ".sh", 'a+') as f:
	    f.write(string)
        
shutil.copyfile("run.sh", folder + "/run.sh")
os.system("chmod +x " + folder + "/run.sh")
for line in fileinput.input(folder + "/run.sh", inplace=1):
    if "endIndex=11" in line:
	line = "endIndex=" + str(numConvarianceSteps + 1) + "\n"	
    elif "for ((a=0;" in line:
	line = "  for ((a=0; a < " + str(numRuns/numParallelJobs) + "; a++))\n"
    sys.stdout.write(line)
print "launched \n"
