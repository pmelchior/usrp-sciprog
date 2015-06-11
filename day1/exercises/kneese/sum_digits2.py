#!/usr/bin/env python

"""
 METHOD: convert given number n to a string ex. n = 555, str(n) = 'n'
 Then loop it. ex. for c in s: print c.
 This will print the string(n) as a list. Then add the parts of that list.
"""
 
def sum_digits(n):
    number = str(n)
    print sum(int(c) for c in number) #sum the digits in the string


def sumrepeated(n, y=None): # n not defined until def () closes, so need to pass y until later
    total = 0       
    if y is None:
        y=n**2     
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

sumrepeated(4)

#Everything seems to work except when I run sumrepeated(4, 20) I get 3 "None"s.
#Sumrepeated(4) prints 2 "None"s. 
