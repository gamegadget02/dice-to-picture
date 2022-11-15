from PIL import Image
from the_dice import *
from turtle import *

turtle1 = turtle.Turtle(visible=False)
turtle1.speed(0)
turtle1.penup()

screen = turtle.Screen()
screen.setup(50*12, 75*12)

image = Image.open("IMG_20221115_120137.png")
imagebw = image.convert("RGB")
imagebw.save("temp.jpg", quality=1)
imagebwlow = Image.open("temp.jpg", "r")
imagebwlow = imagebwlow.convert("RGB")
#imagebwlow.show()
width,hight = imagebwlow.size
size = width/20, hight/20
imagebwlow.thumbnail(size, Image.Resampling.LANCZOS)
#imagebwlow.show()
width,hight = imagebwlow.size
print(hight)
print(width)
f = open("output.txt", "w")
x,y = 0,0
while y<900:
    rgb = imagebwlow.getpixel((x/12,y/12))
    r,g,b = rgb
    a = sum([r,g,b])/3
    if x >= 600-12:
        y+=12
        x=0
        f.write("\n")
        f.write(str(a)+",")
    else:
        f.write(str(a)+",")
        x+=12
f.close()
x,y = 0,0
while y<900:
    rgb = imagebwlow.getpixel((x/12,y/12))
    r,g,b = rgb
    a = sum([r,g,b])/3
    if x >= 600-12:
        y+=12
        x=0
    if a <= 3:
        x+=12
    elif a <=42:
        sixSide(x,y,rgb)
        x+=12
    elif a <=42*2:
        fiveSide(x,y,rgb)
        x+=12
    elif a <=42*3:
        fourSide(x,y,rgb)
        x+=12
    elif a <= 42*4:
        threeSide(x,y,rgb)
        x+=12
    elif a <= 42*5:
        twoSide(x,y,rgb)
        x+=12
    elif a <= 42*6:
        oneSide(x,y,rgb)
        x+=12

screen.exitonclick()
    