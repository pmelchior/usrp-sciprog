#! /usr/bin/env python                                                                                                        

''' fizzbuzz.py                                                                                                               
prints numbers between 1 and 100, replacing multiples of 3 with 'fizz', multiples of 5 with 'buzz'                            
and multiples of both with 'fizzbuzz'                                                                                         
'''

def check(n):
   if n%15 == 0:
      print 'fizzbuzz'
   elseif n%5 == 0:
      print 'buzz'
   elseif n%3 == 0:
      print 'fizz'
   else:
      print n

for i in range(0, 31):
   check(i);
