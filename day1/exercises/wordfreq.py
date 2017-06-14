#! /Users/cstahl/anaconda3/bin/python

import re
import operator

with open('ihaveadream.txt') as f: 
    read_data = f.read()

words = read_data.split()
freqs = {}
for word in words:
    m = re.search('\w+', word)
    if m is not None: newword = m.group(0)
    else: continue
    newword = newword.lower()
    if len(newword) > 3:
        if newword not in freqs:
            freqs[newword] = 1
        else: freqs[newword] += 1

for item in sorted(freqs.items(), key=operator.itemgetter(1), reverse=True):
    print(item[0] + ' :' + str(item[1]))
