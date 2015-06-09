'''Write a function called sum_digits that returns the sum of the digits of an integer argument; that is, sum_digits(123) should return 6. Use this function in a program called sum_digits.py that prints out the sum of the digits of every integer multiple of the first argument, up to either the second argument (if included) or the first argument's square. That is:'''
import numpy as np
def sum_digits(num):
    val=0
    num = str(num)
    for i in np.arange(len(num)):
        val+=int(num[i])
    print val

sum_digits(153)
