import turtle

X_OFFSET = 298#248
Y_OFFSET = 350-5#447
DOT_SIZE = 4

turtle1 = turtle.Turtle(visible=False)
turtle1.speed('fastest')
turtle1.penup()
turtle.colormode(255)

def sixSide(startx, starty,rgb):
    turtle1.setposition((0+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
    turtle1.setposition((8+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
    turtle1.setposition((0+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
    turtle1.setposition((8+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
    turtle1.setposition((0+startx)-X_OFFSET,(-4-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
    turtle1.setposition((8+startx)-X_OFFSET,(-4-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
def fiveSide(startx, starty,rgb):
    turtle1.setposition((0+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
    turtle1.setposition((8+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
    turtle1.setposition((0+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
    turtle1.setposition((8+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
    turtle1.setposition((4+startx)-X_OFFSET,(-4-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
def fourSide(startx, starty,rgb):
    turtle1.setposition((0+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
    turtle1.setposition((8+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
    turtle1.setposition((0+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
    turtle1.setposition((8+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
def threeSide(startx, starty,rgb):
    turtle1.setposition((0+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
    turtle1.setposition((8+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
    turtle1.setposition((4+startx)-X_OFFSET,(-4-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
def twoSide(startx, starty,rgb):
    turtle1.setposition((0+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
    turtle1.setposition((8+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)
def oneSide(startx, starty,rgb):
    turtle1.setposition((4+startx)-X_OFFSET,(-4-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,rgb)