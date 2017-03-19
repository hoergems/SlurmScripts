import sys
import os
import subprocess
import glob

shared_path = os.path.dirname(os.path.abspath(__file__))
numObstacles = 20



for i in xrange(1, 11):
    for j in xrange(0, 10):
        string = "#!/bin/sh \n"
        string += "# \n"
        string += "#SBATCH --job-name=" + str(numObstacles)
        string += "DubinABT \n"
        string += "#SBATCH --array="
        string += str(j * 10) + "-" + str(j * 10 + 9) + " \n"
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
	    
        
    
    
    
    
    '''numObstacles += 5
    for j in xrange(1, 11):
	cmd = "sbatch jobs_abt_dubin_" + str(j) + ".sh"
	exec_path = str(numObstacles) + "_obstacles/" + str(j) + "/"
	
	print exec_path
	print cmd
	popen = subprocess.Popen(cmd, cwd=exec_path, shell=True)
	popen.wait()'''
print "launched \n"
