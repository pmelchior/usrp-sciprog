#!/usr/bin/env python
import sys


def sum_digits(n):
	sum = 0;
	while(n != 0):
		sum += n%10
		n//=10
	print sum

if __name__ == "__main__":
	mult = int(sys.argv[1])
	if len(sys.argv)==3:
		limit = int(sys.argv[2])
	else:
		limit = mult**2

	for i in range(mult, limit+1, mult):
	    sum_digits(i)