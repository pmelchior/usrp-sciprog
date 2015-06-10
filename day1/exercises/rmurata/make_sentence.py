
# coding: utf-8

# In[3]:
import string

while 1:
    s = raw_input('')
    s = s.split(' ')
    count = 0
    for i in range(len(s)):
        if s[i][-1] in ['.', '!', '?']:
            print('Enter a word(. ! or ? to end):%s' % s[i])
            count = 1
        else:
            print('Enter a word(. ! or ? to end):%s' % s[i])
    if (count == 1):
        break

print(string.join(s))

    
# In[ ]:



