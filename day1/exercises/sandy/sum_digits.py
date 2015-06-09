import numpy as np
import sys

def sum_digits(in_int):
	in_str = str(in_int)
	sum = 0
	for chr in in_str:
		sum = sum + int(chr)
	return sum

base = int(sys.argv[1])
bound = base**2
if len(sys.argv) > 2:
	bound = int(sys.argv[2])

it = base
while it <= bound:
	print sum_digits(it)
	it = it + base

