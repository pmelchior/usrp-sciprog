import numpy as np

mylist = np.arange(1,101)

for num in mylist:
	if num % 15 == 0:
		print "FizzBuzz "
	elif num & 5 == 0:
		print "Buzz "
	elif num & 3 == 0:
		print "Fizz "
	else:
		print str(num) + " "

