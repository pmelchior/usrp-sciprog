print('Hello minions \n how are you today?')
print('this is a script, which, when called, will execute all the line in it:')

def add_numbers(x, y):
	'''
	Function that adds two input numbers
	Inputs
		x: a number
		y: a number
	Outputs
		result: the sum of x and y  
	'''
	return x+y

a = 3
b = -10
print('for instance, I can declare functions and execute them. \n Here I add {0} and {1} to make {2}'.format(a,b,add_numbers(a,b)))
