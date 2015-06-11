#!/usr/bin/env python

def askword():

    sentence = []
    end = True
    while end:
        word = raw_input('Enter a Word (. ! or ? to end): ')
        sentence.append(word)
        if word in ['.', '!', '?']: 
            end = False
    excl = sentence.pop()
    last_word = sentence.pop()
    sentence_string = ''
    for x in sentence:
        sentence_string += x + ' '
    print (sentence_string + last_word + excl)      

if __name__ == '__main__':
    askword()