#!/usr/bin/env python


"""
 Write a program that prints out all words longer than three letters and 
 their frequencies in a given file, ordered by frequency. 
 """
wordminlength = 3
text = ""
files = []

for file in files:
    f = open(file)
    for line in f:
        text += line


wordfreq = {} 
for word in text:
    if word > wordminlength:
        if word in wordfreq:
            wordfreq[word] += 1
        else:
            wordfreq[word] = 1



  