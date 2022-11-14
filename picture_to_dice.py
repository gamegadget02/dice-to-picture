from PIL import Image
from the_dice import *
from turtle import *

turtle1 = turtle.Turtle(visible=False)
turtle1.speed(0)
turtle1.penup()

screen = turtle.Screen()
screen.setup(100*12, 150*12)

image = Image.open("photo-1506794778202-cad84cf45f1d.jpg")
imagebw = image.convert("RGB")
imagebw.save("temp.jpg", quality=1)
imagebwlow = Image.open("temp.jpg", "r")
imagebwlow = imagebwlow.convert("RGB")
#imagebwlow.show()
width,hight = imagebwlow.size
size = width/10, hight/10
imagebwlow.thumbnail(size, Image.Resampling.LANCZOS)
imagebwlow.show()
width,hight = imagebwlow.size
print(hight)
print(width)
f = open("output.txt", "w")
x,y = 0,0
while y<1800:
    rgb = imagebwlow.getpixel((x/12,y/12))
    r,g,b = rgb
    a = sum([r,g,b])/3
    if x >= 1200-12:
        y+=12
        x=0
        f.write("\n")
        f.write(str(a)+",")
    else:
        f.write(str(a)+",")
        x+=12
f.close()
x,y = 0,0
while y<1800:
    rgb = imagebwlow.getpixel((x/12,y/12))
    r,g,b = rgb
    a = sum([r,g,b])/3
    if x >= 1200-12:
        y+=12
        x=0
    if a <= 3:
        pass
        x+=12
    elif a <=42:
        sixSide(x,y)
        x+=12
    elif a <=42*2:
        fiveSide(x,y)
        x+=12
    elif a <=42*3:
        fourSide(x,y)
        x+=12
    elif a <= 42*4:
        threeSide(x,y)
        x+=12
    elif a <= 42*5:
        twoSide(x,y)
        x+=12
    elif a <= 42*6:
        oneSide(x,y)
        x+=12

screen.exitonclick()
    