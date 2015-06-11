#!/usr/bin/env python


#then call that function in the second part of the program
#where the program will count by the first number given (ex. 4, 8, 12, 16)
#and then add the integers of each of those (4, 8, 3, 7)
#and it stops when the square of the first number is reached (16)
#or at the second number provided, if there is one provided (4, 20 goes to 20)




def sum_digits(n):
        """
        sums integers in a number
        """
	if n < 10:
		return n
	else:
             all_but_last= n // 10    # // is integer division
             """ I think this part is breaking when n > 99 because when it
             integer divides by 10, it returns n > 10"""
             if all_but_last >= 10:
                 all_but_last= all_but_last // 10
             else:
                    pass
             last = n % 10   # % means divide left by right, returns remainder
             print sum_digits(all_but_last) + last
             
sum_digits(555) #incorrect
sum_digits(123) #incorrect
sum_digits(200) #correct
sum_digits(111) #incorrect
sum_digits(105) #correct
sum_digits(110) #incorrect


"""
 555 // 10 = 55
 55 // 10 = 5
 remainder = 5
 5 + 5 = 10 - >incorrect

 I want the program to divide by 100 if >99, divide by 1000 if >999, et cetera 
 then divide by all smaller powers of 10 (1000, 100, 10)
 then add those numbers (only the value in that spot)

So if n = 555
555 // 100 = 5
555 // 10 = 55, 55 // 10 = 5
remainder = 5
5 + 5 + 5 = 15 -> correct
 
 
will len(n) work, then divide by 10^len(n)-1, then 10^(len(n)-2) 


 """
 
"""
 METHOD: convert given number n to a string ex. n = 555, str(n) = 'n'
 Then loop it. ex. for c in s: print c.
 This will print the string(n) as a list. Then add the parts of that list.
"""
 