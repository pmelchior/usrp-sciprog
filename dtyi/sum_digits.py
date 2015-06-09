#!/usr/bin/env python
import sys


def sum_digits(n):
	sum = 0;
	while(n != 0):
		sum += n%10
		n/=10
	print sum

if __name__ == "__main__":
	if len(sys.argv)==3:
		mult = int(sys.argv[2])
	else:
		mult = int(sys.argv[1])

	for i in range(1,mult+1):
	    sum_digits(i*int(sys.argv[1]))