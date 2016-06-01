#!/usr/bin/env python
import re
import numpy as np

def wordfreq():
    #identifies words longer than three characters
    #and print them out with their frequencies
    textfile = open('ihaveadream.txt')

    #cleaning the textfile
    dream = textfile.read()
    dream = dream.lower()
    dream = re.sub('[^a-z]',' ', dream)

    wordlist = dream.split()

    wordcount = {}
    for word in wordlist:
        if (len(word) > 3) and (word not in wordcount):
            wordcount[word] = 1
        elif (len(word) > 3) and (word in wordcount):
            wordcount[word] += 1
        else: pass

    words = wordcount.keys()
    freqs = wordcount.values()

    freqs_indices = np.argsort(freqs)

    for index in reversed(freqs_indices):
        print (words[index] + ': ' + str(freqs[index]))

if __name__ == '__main__':
    wordfreq()   