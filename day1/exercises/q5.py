import numpy as np
larger_than_3= []
with open('ihaveadream.txt','r') as f:
    for line in f:
        for i in line.split():
            if len(i)>3:
                larger_than_3.append(i)
wordlst = []
countlst = []
for i in np.unique(larger_than_3):
    word =  i.strip('"')
    count =  larger_than_3.count(word)
#     print "{}:{}".format(word,count)
    wordlst.append(word)
    countlst.append(count)
countlst= np.array(countlst)
wordlst=np.array(wordlst)
# countlst[np.argsort(countlst)[::,-1]]
np.argsort(countlst)[::-1]
# print "{}:{}".format(wordlst[np.argsort(countlst)[::-1]],countlst[np.argsort(countlst)[::-1]])
wordlst=wordlst[np.argsort(countlst)[::-1]]
countlst=countlst[np.argsort(countlst)[::-1]]
for i in np.arange(len(wordlst)):
    print "{}:{}".format(wordlst[i],countlst[i])