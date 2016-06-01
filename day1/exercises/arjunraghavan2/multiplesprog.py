import numpy as np # Importing numpy library
for x in range (1, 101): # For loop
	if (np.round(x/3))-((x*1.0)/3)==0 and (np.round(x/5))-((x*1.0)/5)!=0:
		print 'Fizz' # Checking for multiples of 3
	elif (np.round(x/5))-((x*1.0)/5)==0 and (np.round(x/3))-((x*1.0)/3)!=0:
		print 'Buzz' # Checking for multiples of 5
	elif (np.round(x/3))-((x*1.0)/3)==0 and (np.round(x/5))-((x*1.0)/5)==0:
		print 'FizzBuzz' # Checking for multiples of 3 and 5
	else: """ If the number is neither only a multiple of 3 nor only a multiple of 
	5 nor a multiple of both 3 and 5, the number itself is printed """
		print x