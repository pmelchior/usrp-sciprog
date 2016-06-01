#!/usr/bin/env python

def main():
	for i in range(1,101):
		l = ""
		if i%3 == 0:
			l = l + 'Fizz'
		if i%5 == 0:
			l = l + 'Buzz'
		if l=="":
			l = i
		print l;

if __name__ == "__main__":
    main()
