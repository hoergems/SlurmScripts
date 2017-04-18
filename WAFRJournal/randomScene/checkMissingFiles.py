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
	for file in files:
	    print file
	'''for count in xrange(1, 101):
	    
	for file in glob.glob("*.log"):
	    print file'''