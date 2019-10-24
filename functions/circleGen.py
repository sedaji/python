#python 3.5.2
import math
import random
length = 70
height = 70
thickness = .325

randString = "!$%^&*_+{}|():,./;'[]\-=_<>?"
randString2 = "__"
listLen = len(randString)
listLen2 = len(randString2)


centerX = length/2
centerY = height/2


def DistanceForm(x1,y1):
    x2 = centerX
    y2 = centerY
    return (math.sqrt( (x2-x1)**2 + (y2-y1)**2) )


for i in range(height+1):
    for j in range(length+1):
        circleChar = randString[random.randint(0,(listLen-1))] + randString[random.randint(0,(listLen-1))]
        circleChar2 = randString2[random.randint(0,(listLen2-1))] + randString2[random.randint(0,(listLen2-1))]
        radius = (DistanceForm(i,j))
        if radius < (height/2+thickness):
            print(circleChar,end='')
        else:
            print(circleChar2,end='')
    print()
