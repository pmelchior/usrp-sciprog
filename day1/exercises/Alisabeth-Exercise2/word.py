#!/usr/bin/env python

s = ""
character = raw_input("Enter a word: ")
while character != "!" or character != "?" or character != ".":   
    print(s + " " + character)
    s = s + " " + character
    character = raw_input("Enter a word: ")
    if character == "!" or character == "?" or character == ".":
        print(s + character)
        break