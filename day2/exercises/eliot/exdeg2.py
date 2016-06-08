# convert degrees to radians
# print column titles
# right align degree values
# limit radians to 7 characters

degree = 0
degreeMax = 180
degreeIncr = 10
pi = 3.14159

print "Degrees   Radians"

while degree <= degreeMax:
	radian = degree * pi / 180

	degreeS = str(degree)	# articulate string variable with trailing S

	if len(degreeS) == 1:
		degreeS = "  " + degreeS
	elif len(degreeS) == 2:
		degreeS = " " + degreeS

	radianS = str(radian)
	print degreeS + "       " + radianS[:7]

	degree += degreeIncr
