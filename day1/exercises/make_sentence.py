#!/usr/bin/env python

sentence = ""
while True:	
	word =  input("Enter somethin: ")
	if (word=="!" or word=="?" or word=="."):
		print(sentence)
		sentence = sentence + word
		exit()
	else:
		sentence = sentence + word + " "
