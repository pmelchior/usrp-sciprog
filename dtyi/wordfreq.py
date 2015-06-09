#!/usr/bin/env python
import sys

def main(filename):
	f = open(filename,'r')
	line = f.readline()
	dict = {}
	while line != "":
		words = line.split(" ")
		for word in words:
			if len(word) <= 3:
				continue
			if word in dict.keys():
				dict[word]+=1
			else:
				dict[word] = 0

	for entry in dict.keys():
		print entry + ": " + dict[entry]


	f.close()

if __name__ == "__main__":
    main(sys.argv[1])