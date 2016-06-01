
# coding: utf-8

# In[10]:

#!/usr/bin/python
import sys

def sum_digits(string):
    a = list(str(string))
    count = 0
    for i in range(len(a)):
        count += float(a[i])
    print(int(count))

if __name__=='__main__':
    length = len(sys.argv) - 1
    a = int(sys.argv[1])
    if (length == 1): 
        square = a * a
    elif (length == 2):
        square = int(sys.argv[2])
    for k in range(square - a + 1):
        k2 = a + k
        if (k2%a == 0):
            sum_digits( str(k2) ) 
        else:
            pass


# 1
# 

# In[ ]:



