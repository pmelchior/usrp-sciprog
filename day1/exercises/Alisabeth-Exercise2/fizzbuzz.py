#!/usr/bin/env python

x = 0;
while x <= 100:
    if x%3 == 0 and x%5 != 0:
        print("Fizz")
    elif x%5 == 0 and x%3 != 0:
        print("Buzz")
    elif x%5 == 0 and x%3 == 0:
        print("FizzBuzz")
    else: 
        print(x)
    x += 1