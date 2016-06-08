# convert degrees to radians
# print column titles
# right align degree values
# limit radians to 7 characters
# use math module for cosine and pi
# align cosine value to decimal point
# do the radian formatting as a function call


def fixformat(s):		# functions must be defined before being called
	while len(s) < 7:
		s = s + " "

	return s


import math

degree = 0
degreeMax = 180
degreeIncr = 10

print "Degrees   Radians    Cosine"

while degree <= degreeMax:
	radian = degree * math.pi / 180

	degreeS = str(degree)

	if len(degreeS) == 1:
		degreeS = "  " + degreeS
	elif len(degreeS) == 2:
		degreeS = " " + degreeS

	radianS = str(radian)
	radianS = fixformat(radianS)		# our function call

	cosine = math.cos(radian)
	cosineS = str(cosine)[:7]

	if cosine >= 0.:
		cosineS = " " + cosineS

	print degreeS + "       " + radianS[:7] + "   " + cosineS

	degree += degreeIncr
