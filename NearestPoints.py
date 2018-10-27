from operator import itemgetter, attrgetter
import math
import random
class Point:
    def __init__(self,X,Y):
        self.x = X
        self.y = Y
    def getPoint(self):
        return [self.x,self.y]
class shortestLenPoints:
    def __init__(self):
        self.point1 = Point(0,0)
        self.point2 = Point(0,0)
        self.distance = 0
def calDistance(point1,point2):
    return math.sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2)
def proPoints(point1,point2):
    shortest = shortestLenPoints()
    shortest.distance = calDistance(point1,point2)
    shortest.point1  = point1.getPoint()
    shortest.point2 = point2.getPoint()
    return shortest
def divideAndConquer(pointX,pointY):
    pointNum = len(pointX)
    YL = []
    YR = []
    YBorder = []
    shortestInBorder = float("inf") #infinite number
    shortestInBorderPoints = shortestLenPoints()
    shortestPoints = shortestLenPoints()
    dividePoints = int((pointNum-1)/2)
#    print '___________'
#    print dividePoints,pointNum
    #####################################
    if pointNum == 3:# while it's only two or three points
            shortest1 = calDistance(pointX[0],pointX[1])
            shortest2 = calDistance(pointX[1],pointX[2])
            shortest3 = calDistance(pointX[0],pointX[2])
        #    print 'num==3:'
        #    print shortest1,shortest2,shortest3
            if shortest1 < shortest2:
                if shortest1 >= shortest3:
                    shortestPoints = proPoints(pointX[0],pointX[2])
                else:
                    shortestPoints = proPoints(pointX[0],pointX[1])
            else:
                if shortest2 >= shortest3:
                    shortestPoints = proPoints(pointX[0],pointX[2])
                else:
                    shortestPoints = proPoints(pointX[1],pointX[2])
            return shortestPoints
    if pointNum == 2:
            shortestPoints = proPoints(pointX[0],pointX[1])
        #    print 'num==2'
        #    print shortestPoints.distance
            return shortestPoints
    if pointNum == 1:
            shortestPoints.distance = float("inf")
            shortestPoints.point1 = pointX[0].getPoint()
            shortestPoints.point1 = pointX[0].getPoint()
            return shortestPoints
    if pointNum == 0:
        print 'fucking wrong'
        exit(0)

    #####################################
#    print 'dividePoints:'
#    print dividePoints
    sameX = 0
    for point in pointY:
        if point.x < pointX[dividePoints].x:
            sameX = sameX + 1
            YL.append(point)
        elif point.x == pointX[dividePoints].x:
            if sameX <= dividePoints:
                sameX = sameX + 1
                YL.append(point)
            else:
                YR.append(point)
        else:
            YR.append(point)
    XL = pointX[0:dividePoints]
    XR = pointX[dividePoints+1:pointNum-1]
    #Now that's begin divide and conquer
    shortestPointsL = divideAndConquer(XL,YL)
    shortestPointsR = divideAndConquer(XR,YR)
    # compare left with right
    if shortestPointsL.distance > shortestPointsR.distance:
        shortest = shortestPointsR.distance
        shortestPoints = shortestPointsR
    else:
        shortest = shortestPointsL.distance
        shortestPoints = shortestPointsL
    # find the shortest between two borders
    for point in pointY:# find the points between the borders
        if point.x >= pointX[dividePoints].x - shortest and point.x <= pointX[dividePoints].x + shortest:
            YBorder.append(point)
    for i in range(0,len(YBorder)):# find the nearest points between two borders
        for j in range(i+1,len(YBorder)):
            if j-i > 7:
                break
            length = calDistance(YBorder[i],YBorder[j])
            if  length < shortestInBorder:
                shortestInBorder = length
                shortestInBorderPoints = proPoints(YBorder[i],YBorder[j])
    # compare left and right with shortest between two borders
    if shortest > shortestInBorder:
        shortestPoints = shortestInBorderPoints
    return shortestPoints

num = int(input('Please enter the number of points you want to run:'))
ceil = int(input('Please enter ceil of x and y:'))
floor = int(input('Please enter floor of x and y:'))
RawPoints = []
for i in range(0,num):
    tempX,tempY = random.randint(floor,ceil),random.randint(floor,ceil)
    tempPoint = Point(int(tempX),int(tempY))
    RawPoints.append(tempPoint)
print 'The points are:'
for point in RawPoints:
    print (point.x,point.y)
PointsX = sorted(RawPoints,key=attrgetter('x'))#sort according to x
PointsY = sorted(RawPoints,key=attrgetter('y'))#sort according to y
nearestPoints = shortestLenPoints()
nearestPoints = divideAndConquer(PointsX,PointsY)
print 'Nearest points are '
print nearestPoints.point1[0],nearestPoints.point1[1]
print 'and'
print nearestPoints.point2[0],nearestPoints.point2[1]
print 'Shortest distance: '
print nearestPoints.distance
