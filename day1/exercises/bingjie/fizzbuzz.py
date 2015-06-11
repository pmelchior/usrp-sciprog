#!/usr/bin/env python
# coding: utf-8

from __future__ import division

for x in xrange(1, 101):
    #print x
    if x%3 == 0 and x%5 == 0:
        print 'FizzBuzz'
    elif x%3 == 0:
        print 'Fizz'
    elif x%5 == 0:
        print 'Buzz'
    else:
        print x