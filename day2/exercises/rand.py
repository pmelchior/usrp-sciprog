#! /Users/cnstahl/anaconda3/bin/python

import numpy

uni = numpy.random.uniform(2,17,17)
uni = numpy.floor(uni)
mask = (uni %2 == 0) & (5 < uni) & (uni < 10)
print(uni[mask])
