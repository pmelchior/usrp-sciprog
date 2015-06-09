
# coding: utf-8

# In[10]:

#!/usr/bin/env python
import sys

def sum_digits(number):
    a = list(str(number))
    count = 0
    for i in range(len(a)):
        count += float(a[i])
    print(int(count))

if __name__=='__main__':
    length = len(sys.argv)
    if (length == 1):
        a = int(sys.argv[0])
        square = a * a
        for k in range(square - a):
            k2 = a + k
            if (k2%a == 0):
                print( sum_digits( int(k2) ) )
            else:
                pass
        
    elif (length == 2):
        a = int(sys.argv[0])
        b = int(sys.argv[1])
        for k in range(b - a):
            k2 = a + k
            if (k2%a == 0):
                print( sum_digits( int(k2) ) )
            else:
                pass
    else:
        print('ERROR')


# 1
# 

# In[ ]:



