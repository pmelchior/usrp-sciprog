#!/usr/bin/env python
sentence = raw_input('Enter a word (. ! or ? to end):')
def ask():
	global sentence
	word = raw_input('Enter a word (. ! or ? to end):')
	if (word == '.') or (word == '!') or (word == '?'):
		sentence = sentence + word	
		print(sentence)
	else:
		sentence = sentence + ' ' + word
		ask()

if __name__ == '__main__':
	if (sentence == '.') or (sentence == '!') or (sentence == '?'):
		print(sentence)
	else:
		ask()