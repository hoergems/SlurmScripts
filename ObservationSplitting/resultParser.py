import os

for i in xrange(1, 11):
	succRuns = 0
	rewards = []
	for j in xrange(25):
		with open(str(i) + "_dist/log_ABT_4DOFManipulator_" + str(j) + ".log", 'r') as f:
			for line in f.readlines():
				if "Num successful runs" in line:
					if "Num successful runs: 1":
						succRuns = succRuns + 1
				elif "Mean rewards:" in line:
					rewards.append(float(line.split(": ")[1].rstrip()))
	std = sqrt(2.0)
	print "succRuns: " + str(succRuns)