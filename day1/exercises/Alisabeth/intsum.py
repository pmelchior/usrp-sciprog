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
limit = int(x) * int(x)
print(len(sys.argv))

if len(sys.argv) ==2:
    while x <= limit:
        print(int_sum(x))
        x += x

else:
    y = sys.argv[2]
    while x <= y:
        print(int_sum(x))
        x += x
   