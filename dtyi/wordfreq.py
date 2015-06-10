#!/usr/bin/env python
import sys
import re

def main(filename):
	f = open(filename,'r')
	line = f.readline()
	dict = {}
	while line != "":
		words = re.sub("[^A-Za-z]", " ", line).split()
		for word in words:
			word = word.lower()
			if len(word) <= 3:
				continue
			if word in dict.keys():
				dict[word]+=1
			else:
				dict[word] = 1
		line = f.readline()

	f.close()
	
	sortedkeys = sorted(dict, key=dict.get, reverse=True)
	for entry in sortedkeys:
		print entry + ": " + str(dict[entry])

if __name__ == "__main__":
    main(sys.argv[1])