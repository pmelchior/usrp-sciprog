#!/usr/bin/env python
import sys

def sum_digits(num):
	snum = str(num)
	accumulator = 0
	for i in xrange(0,len(snum)):
		accumulator+=int(snum[i])
	return accumulator

start=int(sys.argv[1])
if len(sys.argv)==2:
	end=int(sys.argv[1]) * int(sys.argv[1])
	

if len(sys.argv)>=3: #ignores later arguments
	end=int(sys.argv[2])

for i in xrange(start,end+1):
		if i%start == 0:
			print sum_digits(i)