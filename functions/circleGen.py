#python 3.5.2
import math
length = 60
height = 60
thickness = .4
circleChar = "++"

centerX = length/2
centerY = height/2


def DistanceForm(x1,y1):
    x2 = centerX
    y2 = centerY
    return (math.sqrt( (x2-x1)**2 + (y2-y1)**2) )


for i in range(height+1):
    for j in range(length+1):
        
        radius = (DistanceForm(i,j))
        if radius > (length/2-thickness) and radius < (height/2+thickness):
            print(circleChar,end='')
        else:
            print("  ",end='')
    print()
