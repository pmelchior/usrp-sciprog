#! /Users/cstahl/anaconda3/bin/python

for i in range(1, 101):
    if (i%3 == 0):
        if (i%5 == 0): 
            print("FizzBuzz")
        else:
            print("Buzz")
    else: 
        print(i)
