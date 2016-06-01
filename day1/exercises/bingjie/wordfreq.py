#!/usr/bin/env python
# coding: utf-8

import numpy as np
import string
import collections


f = open('../ihaveadream.txt','r')
words = [word.strip(string.punctuation) for word in f.read().split()]

three = []
for word in words:
    wd = word.lower()
    if len(wd) > 3:
        three.append(wd)

counts = collections.Counter(three)

print counts


