#!/usr/bin/env python
sentence= raw_input('Enter a word (. ! or ? to end):')

def make_sentence():
	global sentence
	word = raw_input('Enter a word (. ! or ? to end):')
	if (word=='.') or (word=='!') or (word=='?'):
		sentence += word
		print sentence
	else:
		sentence += ' ' + word
		make_sentence()
if __name__ == '__main__':
	if (sentence=='.') or (sentence=='!') or (sentence=='?'):
		print sentence
	else:
		make_sentence()