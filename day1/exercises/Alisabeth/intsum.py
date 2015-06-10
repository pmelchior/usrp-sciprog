#!/usr/bin/env python

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

import sys
x = sys.argv[1]
limit = int(x)**2

if len(sys.argv) < 3:
    while x <= limit:
        sum2 = int_sum(x)
        print(sum2)
        x += x
        break
else:
    y = sys.argv[2]
    while x <= y:
        sum2 = int_sum(x)
        print(sum2)
        x += x
        break