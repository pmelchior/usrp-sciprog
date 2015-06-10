#write a function called sum_digits that returns the sum of the digits
#then call that function in the second part of the program
#where the program will count by the first number given (ex. 4, 8, 12, 16)
#and then add the integers of each of those (4, 8, 3, 7)
#and it stops when the square of the first number is reached (16)
#or at the second number provided, if there is one provided (4, 20 goes to 20)

def sum_digits(n):
	if n < 10:
		return n
	else:
             all_but_last= n // 10
             last = n % 10
             print sum_digits(all_but_last) + last



# strange error. Lines 8 and 13, unexpected '('