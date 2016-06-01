import string
import numpy as np
f = open('ihaveadream.txt')
words = np.array([])
for word in f.read().split():
	word = word.translate(None,string.punctuation)
	word = word.translate(None,'2')
	word = word.translate(None,'3')
	word = word.translate(None,'1')
	word = word.lower()
	words = np.append(words,word)
freqs = np.array([])
for i in range(0,len(words)):
	if len(words[i]) > 3:
		if words[i] in freqs[:,0]:
			freqs[freqs[:,0].index(words[i]),1] += 1
		else: 
			freqs = np.append(freqs,([words[i],1]))
for i in range(0,len(freqs)):
	print freqs[:,0] + ' ' + str(freqs[:,1]) 
