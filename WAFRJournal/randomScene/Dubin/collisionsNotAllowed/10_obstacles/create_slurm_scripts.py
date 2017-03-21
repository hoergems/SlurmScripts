import sys
import os
import subprocess
import glob
import argparse
import fileinput

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-nO', '--numObstacles', type=int, default=5,
                    help='Number of obstacles')
parser.add_argument('-nP', '--numParallelJobs', type=int, default=10,
                    help='Number of obstacles')
args = parser.parse_args()

numObstacles = args.numObstacles
numParallelJobs = args.numParallelJobs

shared_path = os.path.dirname(os.path.abspath(__file__))

for i in xrange(1, 11):
    for j in xrange(0, 100/numParallelJobs):
        string = "#!/bin/sh \n"
        string += "# \n"
        string += "#SBATCH --job-name=" + str(numObstacles)
        string += "DubinABT \n"
        string += "#SBATCH --array="
        string += str(j * numParallelJobs) + "-" + str(j * numParallelJobs + numParallelJobs-1) + " \n"
        string += "#SBATCH --time=00:20:00 \n"
        string += "#SBATCH --nodes=1 \n"
        string += "#SBATCH --ntasks=1 \n"
        string += "#SBATCH --mem=4096 \n"
        string += "#SBATCH --mail-type=ALL \n"
        string += "#SBATCH --mail-user=hoergems@gmail.com \n"
        string += "source /home/hoe01h/.bash_profile \n"
        string += "cd /data/hoe01h/Downloads/frapu/abt/bin \n"
        string += "./abt_dubin --cfg /data/hoe01h/Downloads/frapu/ConfigFiles/WAFRJournal/randomScene/Dubin/collisionsNotAllowed/"
        string += str(numObstacles)
        string += "_obstacles/cfg/"
        string += str(i)
        string += "/dubin$SLURM_ARRAY_TASK_ID.cfg \n"
        print string
        if not os.path.exists(str(i)):
	    os.makedirs(str(i))
	with open(str(i) + "/jobs_abt_dubin_" + str(j) + ".sh", 'a+') as f:
	    f.write(string)
	
with open("run.sh", 'a+') as f:
    for line in f.readlines():
	print line
	    
for line in fileinput.input("run.sh", inplace=1):
    if "for ((a=0;" in line:
	line = "  for ((a=0; a < " + str(100/numParallelJobs) + "; a++))\n"
    sys.stdout.write(line)
print "launched \n"
