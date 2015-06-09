
# coding: utf-8

# In[29]:

import sys
#f = open(sys.argv[1])
f = open('ihaveadream.txt')
word = f.read()
word = word.split(' ')
char_set = {x for x in word}
char_freq = {x :word.count(x) for x in char_set}
a = char_freq
for k, v in reversed(sorted(a.items(), key = lambda x:x[1])):
    if (int(v) >= 4):
        print('%s: %d' %(k, v))
    
# In[ ]:



