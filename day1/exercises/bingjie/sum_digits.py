
# coding: utf-8

from __future__ import division

def sum_digits(n):
   i = 0
   while n:
       i, n = i + n % 10, n // 10
   return i

def sum_dig_func(fir, *args):
    fir = float(fir)
    if not args:
        #print 'no second argument... doing till the square of the first.'
        sqr = fir**2
        #print sqr
        #print int(sqr)
        for x in xrange(1, int(sqr)+1):
            #just need to do a loop here, sqr+1 is probably the greatest loop # I need.
            #better way to do this?
            multi = fir * x
            #print multi
            if multi <= sqr:
                print sum_digits(multi)
    else:
        #print 'has second argument... doing till the value of it.'
        sqr = fir**2
        for x in xrange(1, int(sqr)+1):
            #just need to do a loop here, sqr+1 is probably the greatest loop # I need.
            #better way to do this?
            multi = fir * x
            #print args
            if multi <= args[0]:
                print sum_digits(multi)
    return


# In[36]:

sum_dig_func(4)


# In[37]:

sum_dig_func(4, 20)