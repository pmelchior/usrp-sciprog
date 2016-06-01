#!/usr/bin/env python

import sys

def int_sum(x):
    """
    Returns the sum of the digits of multiples of an integer
    """
    z = 0
    sum1 = 0
    while z < len(x):
        number = x[z]
        sum1 += int(number)
        z += 1    
    return sum1

#initialize limit
limit = 0

#define the bound for each circumstance
if len(sys.argv) == 3:
    limit = int(sys.argv[2])
else:
    limit = int(sys.argv[1]) ** 2

#compute sums by calling function
multiplier = 1
current = int(sys.argv[1])

while(True):
    product = current * multiplier
    if product <= limit:
        print(int_sum(str(product)))
    else:
        break
    multiplier += 1

    
   