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
size = config.widthsm/config.detail, config.heightsm/config.detail
imagebwlow.thumbnail(size, Image.Resampling.LANCZOS)
imagebwlow.show()
print(config.height)
print(config.width)
print(config.heightsm/config.detail)
print(config.widthsm/config.detail)
f = open("output.txt", "w")
x,y = 0,0
while y < config.height:
    rgb = imagebwlow.getpixel((x/12,y/12))
    r,g,b = rgb
    a = sum([r,g,b])/3
    if x >= config.width-12:
        y+=12
        x=0
        f.write("\n")
        f.write(str(a)+",")
    else:
        f.write(str(a)+",")
        x+=12
f.close()
x,y = 0,0
while y<config.height:
    rgb = imagebwlow.getpixel((x/12,y/12))
    r,g,b = rgb
    a = sum([r,g,b])/3
    #rgb= (0,0,0)
    if x >= config.width-12: 
        y+=12
        x=0
    if a <= 2:
        x+=12
    elif a <=42:
        sixSide(x-300,y,rgb)
        x+=12
    elif a <=42*2:
        fiveSide(x-300,y,rgb)
        x+=12
    elif a <=42*3:
        fourSide(x-300,y,rgb)
        x+=12
    elif a <= 42*4:
        threeSide(x-300,y,rgb)
        x+=12
    elif a <= 42*5:
        twoSide(x-300,y,rgb)
        x+=12
    elif a <= 42*6:
        oneSide(x-300,y,rgb)
        x+=12

screen.exitonclick()
    