#!/usr/bin/env python
import sys

def sum_digits(number):
	# adds individual digits in the input
	sum = 0
	numstr = str(number)
	for num in numstr:
		sum += int(num)
	return sum

if len(sys.argv) > 2:
	stop = int(sys.argv[2])
else:
	stop = int(sys.argv[1])**2

i = 0
counter = 1
while i < stop:
	i = int(sys.argv[1])*counter
	print sum_digits(i)
	counter += 1