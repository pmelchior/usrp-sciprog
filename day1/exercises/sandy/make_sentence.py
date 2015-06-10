import numpy as np
output = ""
user_input = ""
while True:
	user_input = raw_input("enter a word (. ! ? to end): ")
	if user_input == "." or user_input == "?" or user_input == "!":
		break
	output = output +  " " + user_input
final = output + user_input
print final[1:]