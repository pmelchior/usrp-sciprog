#! /usr/bin/env python                                                                                                       \
                                                                                                                              
''' sum_digits.py                                                                                                            \
                                                                                                                              
takes user input and returns the sum of hte digits of the integer input                                                      \
                                                                                                                              
'''

import sys

def sum_digits(k):
   s = 0
   for i in range(0, len(str(k))):
      s += int(str(k)[i]);
   return s;

max_mul = 999;
if len(sys.argv) == 2:
   max_mul = int(sys.argv[1]) *int(sys.argv[1]);
if len(sys.argv) > 2:
   max_mul = int(sys.argv[2]);

curr_mul = int(sys.argv[1]);
while curr_mul <= max_mul :
   print sum_digits(curr_mul)
   curr_mul += int(sys.argv[1]);
