"""
Tim's solution to deg.py with the following formatting:

column titles
right align degree values
limit radians to 7 characters.
"""

from math import pi

print('degrees radians')
for deg in range(0,181,10):
    rad = deg*pi / 180.
    print('{:-7.0f} {:7.5f}'.format(deg, rad))

