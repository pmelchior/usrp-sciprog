import numpy as np
def sum_digits(string1): 
	strval=str(string1) # Original function definition
	avals=np.zeros(len(strval))
	for val in strval:
		avals=np.append(avals,int(val)) # Appending each digit via breaking up from string
	global sum 
	sum=np.sum(avals) # Summing the values; note the global definition of the 'sum' variable

a=input('Pick a number:') # User input requested
b=input('Pick another number, if you wish or input 0 if not:')

if b==0:
	count=1 #Two cases possible
	v=a
	while (v*count)<=(a**2): 
		sum_digits(v*count)
		global sum
		print int(sum) # Printing of outputs
		count=count+1 # To get next multiple
elif b!=0:
	count=1
	v=a
	while (v*count)<=(b):
		sum_digits(v*count) # The other case
		print int(sum) # Same procedure as (a**2) limit case used here except for differing condition on 'while' loop
		count=count+1
