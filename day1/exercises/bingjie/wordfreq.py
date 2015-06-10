
# coding: utf-8

import numpy as np
import string
import collections


# In[2]:

f = open('../ihaveadream.txt','r')
words = [word.strip(string.punctuation) for word in f.read().split()]


# In[6]:

three = []
for word in words:
    wd = word.lower()
    if len(wd) > 3:
        three.append(wd)


# In[7]:

counts = collections.Counter(three)


# In[8]:

print counts


