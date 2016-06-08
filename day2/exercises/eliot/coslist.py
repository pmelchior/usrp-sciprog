# convert degrees to radians
# print column titles
# right align degree values
# limit radians to 7 characters
# use math module for cosine and pi
# align cosine value to decimal point
# store the values in 2 lists


import math

degree = 0
degreeMax = 180
degreeIncr = 10

print "Degrees   Radians    Cosine"

radianL = []
cosineL = []

while degree <= degreeMax:
	radian = degree * math.pi / 180
	radianL.append(radian)

	degreeS = str(degree)

	if len(degreeS) == 1:
		degreeS = "  " + degreeS
	elif len(degreeS) == 2:
		degreeS = " " + degreeS

	radianS = str(radian)

	while len(radianS) < 7:
		radianS = radianS + " "

	cosine = math.cos(radian)
	cosineL.append(cosine)
	cosineS = str(cosine)

	if cosine >= 0.:
		cosineS = " " + cosineS

	print degreeS + "       " + radianS[:7] + "   " + cosineS

	degree += degreeIncr

print " "
print radianL
print " "
print cosineL
