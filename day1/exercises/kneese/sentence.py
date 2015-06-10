#!/usr/bin/env python

prompt = "Enter a word (. ! or ? to end): "
mysentence = raw_input(prompt)
word = ""
while word not in (".", "!", "?"):
	word = raw_input(prompt) 
	
	if word not in (".", "!", "?"):
		mysentence = mysentence + " " + word
	else:
		mysentence = mysentence + word

	

print mysentence
	
	