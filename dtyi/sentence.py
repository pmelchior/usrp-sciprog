#!/usr/bin/env python


def main():
    escape_chars = {'!', '?', '.'}
    sentence = ""
    word = raw_input('Enter a word (. ! or ? to end) ')
    while(not word in escape_chars):
        sentence = sentence + word + " "
        word = raw_input('Enter a word (. ! or ? to end) ')
    sentence = sentence[:-1]
    print sentence + word

if __name__ == "__main__":
    main()
