import sys
import os
import subprocess
import glob
import argparse
import fileinput

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-r', '--robot', type=str, default="Dubin", help="The robot")
args = parser.parse_args()

robot = args.robot
robotExec = "Dubin"
if (robot == "4DOF"):
    robotExec = "robot"

shared_path = os.path.dirname(os.path.abspath(__file__))

for numObstacles in [5, 10, 15, 20, 25]:    
    for folder in xrange(1, 11):
	path = "/datastore/hoe01h/WAFRJournal/randomScene/" + robot + "/collisionsNotAllowed/" + str(numObstacles) + "_obstacles/" + str(folder)
	files = glob.glob(path + "/*.log")
	algs = {}
	algs["abt"] = []
	algs["mhfr"] = []
	for file in files:
	    if "abt" in file:
		algs["abt"].append(file)
	    elif "mhfr" in file:
		algs["mhfr"].append(file)	    
	for count in xrange(1, 101):
	    foundABT = False
	    foundMHFR = False
	    for file in algs["abt"]:		
		fileComps = file.split("_")[-2]		
		if str(count) in fileComps:
		    foundABT = True		
            for file in algs["mhfr"]:
		fileComps = file.split("_")[-2]
		if str(count) in fileComps:
		    foundMHFR = True
            if not foundABT:
		print "missing ABT: " + str(count)
	    if not foundMHFR:
		print "missing MHFR: " + str(count)