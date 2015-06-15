#!/usr/bin/env python

def askword():

	sentence = ''
	end = True
	while end:
		word = raw_input('Enter a Word (. ! or ? to end): ')
		sentence += word + ' '
		if word in ['.', '!', '?']: 
			end = False
	print sentence

if __name__ == '__main__':
	askword()