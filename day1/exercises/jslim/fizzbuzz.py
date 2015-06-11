#!/usr/bin/env python

def fizzbuzz():

    x = 1
    y = 0
	while y < 100:
		if x % 15 == 0 print 'FizzBuzz'
		elif x % 3 == 0 print 'Fizz'
		elif x % 5 == 0 print 'Buzz'
		else print x
		x += 1
		y += 1

if __name__ = '__main__':
	fizzbuzz()