# Input area
# Input of the parameters

#input_points = input("Give input points - x and y from 0 to 100, in bracets separated by commas and semi-colon(e.g. (0,20);(10,30)) : ")

# Debug mode

input_points="(0,0);(90,100)"

# Convert parameters
def withoutBracets(string):
	return string[1:len(string)-1]

points_string = input_points.split(";")
setPoints = []

for i in range(0,2):
	points_string[i] = withoutBracets(points_string[i])
	setPoints.append(points_string[i].split(","))
	setPoints[i] = [int(x) for x in setPoints[i]]
# Line equation (y = grad*x + b)
# Gradient
grad = (setPoints[1][1] - setPoints[0][1])/(setPoints[1][0] - setPoints[0][0])
# Absolute
b = setPoints[1][1] - grad*setPoints[1][0]
line = [grad, b]
# Inverse line equation (x = y/grad - b/grad)
inverseLine = [1/grad, b/grad]

# Distance squared
def distanceFromLineSq(x,y):
	distanceXSq = (x-(inverseLine[0]*y+inverseLine[1]))**2
	distanceYSq = (y-(line[0]*x+line[1]))**2
	return distanceXSq + distanceYSq

# Start point
# Getting the points around certain point ( sharing a side )
def getNeighbours(point):
	arr = []
	darr = [-1,1]
	for dx in darr:
		arr.append([point[0]+dx,point[1]])
	
	for dy in darr:
		arr.append([point[0],point[1]+dy])
	return arr
# Get distance of two points
def distanceBetween(p1,p2):
	dxSq = (p1[0]-p2[0])**2
	dySq = (p1[1]-p2[1])**2
	return dxSq+dySq
# Selecting the appropriate pixel - when two pixels get the same score, y direction goes first
def selectPoint(points, final):
	topDist = -1
	topPoint = -1
	topDistToFin = -1
	for point in points:
		candidate = distanceFromLineSq(point[0],point[1])
		candidateToFin = distanceBetween(point,final)
		if (candidate <= topDist) or point == points[0]:
			if candidateToFin > topDistToFin and not (point == points[0]):
				continue
			topDist = candidate
			topPoint = point
			topDistToFin = candidateToFin
	return topPoint
# Here, the code begins
linepoints = [setPoints[0]]
finalPoint = setPoints[1]
# Unfortunatelly, recursion depth is reached for common cases :(
def getNextPoint(linepoints):
	if len(linepoints) > 1:
		lastpoint = linepoints[-2]
	else:
		lastpoint = linepoints[0]
	neighbours = getNeighbours(linepoints[-1])
	# Get rid of the previous one
	for i in range(0,len(neighbours)):
		point = neighbours[i]
		if point == lastpoint:
			del neighbours[i]
			break
	# Find the proper point
	new_point = selectPoint(neighbours, finalPoint)
	return new_point
# Visualisation
from tkinter import *
canvas = False
canvas_width = 800
canvas_height = 400

master = Tk()
	
canvas = Canvas(master, 
	width=canvas_width,
	height=canvas_height)
canvas.pack()

def addPointAt(x,y, canvas):
	scale = 2
	y0 = int(canvas_height * 3 / 4)
	x0 = int(canvas_width / 4 )
	canvas.create_rectangle(x+x0,-y+y0,x+x0+scale,-y+y0-scale, fill="black")

# Make Way
while not (linepoints[-1] == finalPoint):
	new_point = getNextPoint(linepoints)
	linepoints.append(new_point)
	addPointAt(new_point[0],new_point[1], canvas)
	
mainloop()