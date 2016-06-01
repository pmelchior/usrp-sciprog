#!/usr/bin/env python
import sys
from collections import Counter
filename=sys.argv[1]
f=open(filename, 'r')
f_contents = f.read()
words = f_contents.split()
words = set(words)
print words
