#!/usr/bin/env python
import sys
import re

def main(filename):
	"""
	Tokenizes the file, extracting words by throwing out non-alpha chars,
	and counts how many times each word greater than 3 chars appears
	using a dictionary.
	"""
	f = open(filename,'r')
	line = f.readline()
	word_table = {}
	while line != "":
		words = re.sub("[^A-Za-z]", " ", line).split()
		for word in words:
			word = word.lower()
			if len(word) <= 3:
				continue
			if word in word_table.keys():
				word_table[word] += 1
			else:
				word_table[word] = 1
		line = f.readline()

	f.close()
	
	sortedkeys = sorted(word_table, key=word_table.get, reverse=True)
	for entry in sortedkeys:
		print entry + ": " + str(word_table[entry])

if __name__ == "__main__":
    main(sys.argv[1])