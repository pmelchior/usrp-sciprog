#!/usr/bin/env python
def numberlist():
	for num in range(100):
		if (num % 5 == 0) and (num % 3 == 0):
			print "FizzBuzz"
		elif (num % 3 == 0):
			print "Fizz"
		elif (num % 5 == 0):
			print "Buzz"
		else: 
			print num
numberlist()
	