import turtle

X_OFFSET = 598
Y_OFFSET = 897
DOT_SIZE = 4

turtle1 = turtle.Turtle(visible=False)
turtle1.speed('fastest')
turtle1.penup()

def sixSide(startx, starty):
    turtle1.setposition((0+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
    turtle1.setposition((8+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
    turtle1.setposition((0+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
    turtle1.setposition((8+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
    turtle1.setposition((0+startx)-X_OFFSET,(-4-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
    turtle1.setposition((8+startx)-X_OFFSET,(-4-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
def fiveSide(startx, starty):
    turtle1.setposition((0+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
    turtle1.setposition((8+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
    turtle1.setposition((0+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
    turtle1.setposition((8+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
    turtle1.setposition((4+startx)-X_OFFSET,(-4-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
def fourSide(startx, starty):
    turtle1.setposition((0+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
    turtle1.setposition((8+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
    turtle1.setposition((0+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
    turtle1.setposition((8+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
def threeSide(startx, starty):
    turtle1.setposition((0+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
    turtle1.setposition((8+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
    turtle1.setposition((4+startx)-X_OFFSET,(-4-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
def twoSide(startx, starty):
    turtle1.setposition((0+startx)-X_OFFSET,(-0-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
    turtle1.setposition((8+startx)-X_OFFSET,(-8-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')
def oneSide(startx, starty):
    turtle1.setposition((4+startx)-X_OFFSET,(-4-starty)+Y_OFFSET)
    turtle1.dot(DOT_SIZE,'black')