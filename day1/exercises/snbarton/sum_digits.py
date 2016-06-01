import sys

def sum_digits(number):
	numarray = list(number)
	sum = 0
	for i in range(0,len(number)):
		sum += int(numarray[i])
	return sum

if len(sys.argv) == 3:
	stop = int(sys.argv[2])
else: stop = int(sys.argv[1])**2

number = sys.argv[1]
i = int(number)
counter = 1
while i < stop:
	i = int(sys.argv[1])*counter
	number = str(i)
	print sum_digits(number)
	counter += 1
