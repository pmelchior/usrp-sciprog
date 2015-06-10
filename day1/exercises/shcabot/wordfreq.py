#!/usr/bin/env python
import sys
import numpy as np
freq = np.array([])
f = open(sys.argv[1], 'r')
for line in f:
	for word in line.split():
		if len(freq) > 0:
			if word.lower() in freq[:,0]: 
				freq[freq[:,0].index(word.lower())][1] += 1
		else:
			if len(word) > 3:
				freq = np.append(freq, [[word.lower(), 1]])


freqsorted = freq[freq[:,1].argsort()]
for i in xrange(0, freqsorted.length()):
	print (freqsorted[i][0] + ": " + str(freqsorted[i][1]))