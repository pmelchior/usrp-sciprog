#!/usr/bin/env python

def askword():

	s = raw_input('Enter a word (. ! or ? to end): ')
	print s
	if s in [',', 'i', '?']:
		break

if __name__ == '__main__':
	askword()