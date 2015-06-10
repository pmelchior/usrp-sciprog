import numpy as np
import string
from collections import Counter

txt = open("../ihaveadream.txt", "r")

fulltxt = txt.readlines()

collect = []
for line in fulltxt:
	rawwords = line.split()
	for rword in rawwords:
		word = rword.translate(string.maketrans("",""), string.punctuation)
		word = ''.join([i for i in word if not i.isdigit()])
		word = word.lower()
		if len(word) > 3:
			collect.append(word)

freqs = Counter(collect)

for w, c in freqs.most_common():
	print w, c