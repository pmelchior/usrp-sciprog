import sys

sentence = ''

while True:
    word = input('Enter a word (. ! or ? to end): ')
    if word in ['.' , '!' , '?']:
        sentence = sentence.strip() + word
        break
    sentence += word + ' '

print(sentence)
