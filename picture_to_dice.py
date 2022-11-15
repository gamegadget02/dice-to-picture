from PIL import Image
from the_dice import *
from turtle import *
import config

turtle1 = turtle.Turtle(visible=False)
turtle1.speed(0)
turtle1.penup()

screen = turtle.Screen()
screen.setup(config.width, config.height)

image = Image.open("IMG_20221115_120137.png")
imagebwlow = image.convert("RGB")
size = config.width/12, config.height/12
imagebwlow.thumbnail(size, None)
imagebwlow.show()
print(size)

'''
f = open("output.txt", "w")
x,y = 0,0
while y < (config.height/config.detail)*12-12:
    rgb = imagebwlow.getpixel((x/12,y/12))
    r,g,b = rgb
    a = sum([r,g,b])/3
    if x >= (config.width/config.detail)*12-12:
        y+=12
        x=0
        f.write("\n")
        f.write(str(a)+",")
    else:
        f.write(str(a)+",")
        x+=12
f.close()
'''
x,y = 0,0
while y< size[1]:
    rgb = imagebwlow.getpixel((x,y))
    r,g,b = rgb
    a = sum([r,g,b])/3
    #rgb= (0,0,0)
    if x >= size[0]-1: 
        y+=12
        x=0
    if a <= 2:
        x+=1
    elif a <=42:
        sixSide(x*12,y,rgb)
        x+=1
    elif a <=42*2:
        fiveSide(x*12,y,rgb)
        x+=1
    elif a <=42*3:
        fourSide(x*12,y,rgb)
        x+=1
    elif a <= 42*4:
        threeSide(x*12,y,rgb)
        x+=1
    elif a <= 42*5:
        twoSide(x*12,y,rgb)
        x+=1
    elif a <= 42*6:
        oneSide(x*12,y,rgb)
        x+=1

screen.exitonclick()
    