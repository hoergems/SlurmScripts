import sys
import os
import subprocess
import glob

shared_path = os.path.dirname(os.path.abspath(__file__))
numObstacles = 0

for i in xrange(6):
    numObstacles += 5
    for j in xrange(1, 11):
	cmd = "sbatch jobs_abt_dubin_" + str(j) + ".sh"
	path = "/datastore/hoe01h/WAFRJournal/SlurmScripts/WAFRJournal/randomScene/Dubin/collisionsNotAllowed/" + str(numObstacles) + "_obstacles/" + str(j) + "/"
	
	print path
	print cmd
	popen = subprocess.Popen(cmd, cwd=path)
	popen.wait()
print "launched \n"