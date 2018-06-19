import os

for i in xrange(1, 11):
	for j in xrange(25):
		with open(str(i) + "_dist/log_ABT_4DOFManipulator_" + str(j) + ".log", 'r') as f:
			for line in f.readlines():
				print line