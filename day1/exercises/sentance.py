#! /Users/cstahl/anaconda3/bin/python

sentance = ""

while True:
    mydata = input('Enter a word (. ! or ? to end): ')

    if not (mydata is '.' or mydata is '?' or mydata is '!'):
        if sentance is '': sentance = mydata
        else: sentance = sentance + ' ' + mydata
    else:
        sentance += mydata
        print(sentance)
        break
