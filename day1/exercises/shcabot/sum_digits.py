#!/usr/bin/env python
import sys
def sum_digits(val):
	sval = str(val)
	sum = 0
	for i in xrange(0, len(sval)):
		sum = sum + int(sval[i])

	return sum

start = int(sys.argv[1])
if len(sys.argv) == 2:
	end = int(sys.argv[1]) * int(sys.argv[1])

if len(sys.argv) == 3:
	end = int(sys.argv[2])

for i in xrange(start, end + 1):
	if (i % start) == 0:
		print sum_digits(i)
