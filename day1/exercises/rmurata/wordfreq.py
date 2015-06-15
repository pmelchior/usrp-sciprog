
# coding: utf-8

# In[29]:
f = open('ihaveadream.txt')
word = f.read()
word = word.split()

pre = []
count = 0
check = []
for i in range(len(word)):
    if (len(word[i]) <= 1):
        check.append(1)
    elif (word[i][-2] == '\n'):
        check.append(2)
    else:
        a = word[i][-1]
        check.append(a)

table = [chr(i) for i in xrange(97, 123)]

for i in range(len(check)):
    if check[i] in table:
        pre.append(word[i].lower())
    elif check[i] in ['1', '2']:
        pass
    else:
        c = word[i][:-1]
        pre.append(c.lower())
        if (c.lower() == 'children'):
            print(word[i])
        
word = pre
char_set = {x for x in word}
char_freq = {x :word.count(x) for x in char_set}
a = char_freq
for k, v in reversed(sorted(a.items(), key = lambda x:x[1])):
    if (len(list(k)) >= 4) and (v >= 4):
        print('%s: %d' %(k, v))

    
# In[ ]:



