
# coding: utf-8

# In[2]:

for j in range(100):
        i = j + 1
        if (i%3 == 0) and (i%5 == 0):
            print('FizzBuzz')
        elif (i%3 == 0):
            print('Fizz')
        elif (i%5 == 0):
            print('Buzz')
        else:
            print(i)


# In[ ]:



