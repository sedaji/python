import math
import random
from PIL import Image, ImageDraw
length = 700
height = 700

gradient = 255/ height
thickness = .125

im = Image.new('RGB', (length,height), (255,255,255))
draw = ImageDraw.Draw(im)

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
            color = int(255-j*gradient)
            draw.point(([i,j]), (120, color, color-random.randint(10,70)))

im.save('output.png', 'PNG')
