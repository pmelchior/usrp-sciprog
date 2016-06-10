# convert degrees to radians

degree = 0
degreeMax = 180
degreeIncr = 10
pi = 3.14159

while degree <= degreeMax:
	radian = degree * pi / 180
	print degree, radian
	degree += degreeIncr
