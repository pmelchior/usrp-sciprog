#!/usr/bin/env python
def sum_digits(n):
    number = str(n)
    return sum(int(c) for c in number) #use return not print
"""This function sums the digits in a string """

def sumrepeated(n, y=None): # n not defined until def () closes, so need to pass y until later
    total = 0
    n = int(n)
    if y is None:
        y = n**2     
    while total < y:
        total = int(total) + int(n)
        if total < 10:
            print total
        else:
            print sum_digits(total)
    if n is y: 
        sum_digits(y)
    else:
        pass
"""This function repeatedly sums a number given up until the argument squared
(if no other argument provided) or until the second argument. """

import sys
sys.argv
x = sys.argv[1]
y = int(sys.argv[2])
sumrepeated(x,y)
print "\n"
