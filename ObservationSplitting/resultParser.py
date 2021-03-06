import os.path
import math

distMin = 0.00001
distMax = 1.0

increment = (distMax - distMin) / 49.0
dist = distMin

for i in xrange(1, 51):
	succRuns = 0
	rewards = []
	for j in xrange(50):
		logFile = str(i) + "_dist/log_ABT_4DOFManipulator_" + str(j) + ".log"
		if os.path.isfile(logFile):
			with open(logFile, 'r') as f:
				for line in f.readlines():
					if "Num successful runs" in line:
						if "Num successful runs: 1" in line:
							succRuns = succRuns + 1
					elif "Mean rewards:" in line:
						rewards.append(float(line.split(": ")[1].rstrip()))
	summ = 0.0
	for k in xrange(len(rewards)):
		summ = summ + rewards[k]
	if len(rewards) > 0:
		mean = summ / float(len(rewards))
		innerSum = 0.0
		for k in xrange(len(rewards)):
			innerSum += math.pow(rewards[k] - mean, 2)
		stdd = 1.0 / (float(len(rewards))) * innerSum
		stdd = math.sqrt(stdd)
		print "i, " + str(i) + ", dist, " + str(dist) + ", succRuns, " + str(succRuns) + ", r, " + str(mean) + ", " + str(stdd)
	dist = dist + increment