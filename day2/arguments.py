import sys

if len(sys.argv) > 1:

	print('The following arguments were provided: {}'.format(*sys.argv[1:]))

	for c, arg in enumerate(sys.argv[1:]):

		description = input('Please give the description of input {0} with value {1}: '.format(c, arg))
		print('input number {0}, with value {1} is a {2} '.format(str(c), arg, description))
else:
	print('No argument was given to me, byebye now.')

