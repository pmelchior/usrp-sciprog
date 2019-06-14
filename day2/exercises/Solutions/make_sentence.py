import sys

word = ''
sentence = ''
<<<<<<< HEAD
while word not in ['.' , '!' , '?']:
    word = input('Enter a word (. ! or ? to end): ')
    sentence += word + ' '

print(sentence)
=======
while word not in ['.', '?', '!']:

    word = input('Enter a word (. ! or ? to end): ')
    sentence+= word+' '
print(sentence)
>>>>>>> 316f3ce47e547b176ce30522b28b4666f2a1e0bd
