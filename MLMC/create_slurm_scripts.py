import sys
import os
import subprocess
import glob
import argparse
import fileinput
import shutil

def getTimeString(minutes, planningTime):
    print "minutes1: " + str(minutes)
    minutes = int((minutes/1000.0)*planningTime)  
    print "minutes2: " + str(minutes)
    hours = 0
    while minutes > 59:    
        hours = hours + 1
        minutes = minutes - 60

    timeString = ""
    if (hours < 10):
        timeString += "0" + str(hours)
    else:
        timeString += str(hours)
    timeString += ":"
    if (minutes < 10):
        timeString += "0" + str(minutes)
    else:
        timeString += str(minutes)
    timeString += ":00"
    return timeString


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-np', '--numParallelJobs', type=int, default=10,
                    help='Number of obstacles')
parser.add_argument('-nr', '--numRuns', type=int, default=100,
                    help='Number of runs')
parser.add_argument('-r', '--robotProblem', type=str, default="Dubin", help="The robot problem")
parser.add_argument('-m', '--memory', type=str, default="4096", help="The amout of memory requested per job")
parser.add_argument('-cf', '--configFolder', type=str, required=True, help="Path where the config files are stored in")
parser.add_argument('-t', '--time', type=int, default=5, help="Allocated time for each run")
parser.add_argument('-cp', '--cpus', type=int, default=1, help="Number of cpu cores")
parser.add_argument('-var', '--variant', type=str, help="variant")

args = parser.parse_args()
variant = args.variant

numParallelJobs = args.numParallelJobs
numRuns = args.numRuns
memory = args.memory
cpus = args.cpus
configFolder = args.configFolder
if (configFolder.strip()[-1] != "/"):
    configFolder += "/"

robot = args.robotProblem
robotExec = "robot"

shared_path = os.path.dirname(os.path.abspath(__file__))

folder = "mlmc"
'''if os.path.isdir(folder):
    shutil.rmtree(folder)
os.makedirs(folder)'''

# Convert time string
minutes= args.time


algs = ["correction"]
times = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]

for time in times:
    timeString = getTimeString(minutes, time)
    print "timeString: " + timeString

    # Create the scripts for ABT
    for k in xrange(0, numRuns/numParallelJobs):    
        string = "#!/bin/sh \n"
        string += "# \n"
        string += "#SBATCH --job-name="
        string += robot + "ABT \n"
        string += "#SBATCH --array="
        string += str(k * numParallelJobs) + "-" + str(k * numParallelJobs + numParallelJobs-1) + " \n"
        string += "#SBATCH --time=" + timeString + " \n"
        string += "#SBATCH --nodes=1 \n"
        string += "#SBATCH --ntasks=1 \n"
        string += "#SBATCH --cpus-per-task=" + str(cpus) + " \n"
        string += "#SBATCH --cpu-freq=high \n"    
        string += "#SBATCH --mem=" + memory + " \n"
        string += "#SBATCH --mail-type=NONE \n"
        string += "#SBATCH --mail-user=hoergems@gmail.com \n"
        string += "source /home/hoe01h/.bash_profile \n"
        string += "source /data/hoe01h/usr/share/oppt/setup.sh \n"
        string += "gzMasterUriPort=`expr 11345 + $SLURM_ARRAY_TASK_ID` \n"
        string += "echo $gzMasterUriPort \n"
        string += "echo 'SLURM ID:'\n"
        string += "echo $SLURM_ARRAY_JOB_ID \n"
        string += "export GAZEBO_MASTER_URI=http://localhost:$gzMasterUriPort \n"
        if "pomcp" in variant:
            string += "cd /data/hoe01h/despot/bin \n"            
        else:
            string += "cd /data/hoe01h/oppt_devel/bin \n"        
        if "pomcp" in variant:
            configFilePath = configFolder + robot + "/cfg/" + robot + "_pomcp_" + str(time) + "_$SLURM_ARRAY_TASK_ID.cfg"
            string += "./despotSolver --cfg " + configFilePath + " \n"
        else:
            configFilePath = configFolder + robot + "/cfg/" + robot + "_" + variant + "_" + str(time) + "_$SLURM_ARRAY_TASK_ID.cfg"
            string += "./abtLite --cfg " + configFilePath + " \n"
        #string += "rm /flush1/hoe01h/SlurmScripts/MLMC/mlmc/slurm-${SLURM_ARRAY_JOB_ID}_${SLURM_ARRAY_TASK_ID}.out \n"                    
        if (os.path.exists(folder + "/jobs_abt_" + variant + "_" + robot + "_" + str(time) + "_" + str(k) + ".sh")):
            os.remove(folder + "/jobs_abt_" + variant + "_" + robot + "_" + str(time) + "_" + str(k) + ".sh")
        with open(folder + "/jobs_abt_" + variant + "_" + robot + "_" + str(time) + "_" + str(k) + ".sh", 'a+') as f:
            f.write(string)
    print "HELLO"

    print str(numRuns/numParallelJobs)

runFile = "run.sh"     		
shutil.copyfile("run.sh", folder + "/" + runFile)
os.system("chmod +x " + folder + "/" + runFile)
for line in fileinput.input(folder + "/" + runFile, inplace=1):
    if "endIndex=11" in line:
        line = "endIndex=" + str(1 + 1) + "\n"
    elif "for ((a=0;" in line:
        line = "  for ((a=0; a < " + str(numRuns/numParallelJobs) + "; a++))\n"
    elif "folder=0" in line:
        line = "folder=mlmc\n"
    sys.stdout.write(line)