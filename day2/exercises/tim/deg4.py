"""
Tim's solution

store a list of radians and a list of cosines

print the lists

use a range() loop instead of while
"""

from math import pi
import math

degrees = range(0,181,10)
radians = [deg*pi / 180. for deg in degrees]
cosines = [math.cos(rad) for rad in radians]

print(radians)
print(cosines)

print('degrees radians cosines')
for deg, rad, cos in zip(degrees, radians, cosines):
    print('{:-7.0f} {:7.5f} {:-9f}'.format(deg, rad, cos))

