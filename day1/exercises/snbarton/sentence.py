sentence = ''

def build():
	global sentence
	print 'inside'
	word = raw_input('Enter a word (. ! or ? to end): ')
	if (word == '.') or (word == '!') or (word == '?'):
		sentence = sentence + word
		print(sentence)
	else:
		sentence = sentence + word + ' '
		build()

if __name__ == '__main__':
	build()