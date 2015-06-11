'''
(From @jakevdp): Create a program (a .py file) which repeatedly asks the user for a word. The program should append all the words together. When the user types a "!", "?", or a ".", the program should print the resulting sentence and exit.

For example, a session might look like this:

    $ ./make_sentence.py
    Enter a word (. ! or ? to end): My
    Enter a word (. ! or ? to end): name
    Enter a word (. ! or ? to end): is
    Enter a word (. ! or ? to end): Walter
    Enter a word (. ! or ? to end): White
    Enter a word (. ! or ? to end): !

    My name is Walter White!
'''
'''str = ""
#word = input('Enter a word (. ! or ? to end): ')
word =""
while (word !='.','!','?'):
    str+=word
    word = input()
print (str)
'''
str=""
word  = raw_input('Enter a word (. ! or ? to end): ')
str+=word
while word!= '!' and  word!= '.' and word!= '?':
        word = raw_input('Enter a word (. ! or ? to end): ')
        str+=word
print str
