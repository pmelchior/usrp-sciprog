"""
Tim's solution to deg.py with the following formatting:

column titles
right align degree values
limit radians to 7 characters.

use math.cos(radian) to compute cosine

print cosine in 3rd column (align cos to decimal point)
"""

from math import pi
import math

print('degrees radians cosine')
for deg in range(0,181,10):
    rad = deg*pi / 180.
    cos = math.cos(rad)
    print('{:-7.0f} {:7.5f} {:-9f}'.format(deg, rad, cos))

