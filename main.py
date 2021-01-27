import turtle

# variables for assigning to user input for the dimensions of our Tessellation
rows = input("Enter the number of rows: ")
columns = input("Enter the number of columns: ")

# variables for our turtles coordinates to be used in our drawing functions with their starting point values
diTurtleX = -280
diTurtleY = 225
circTurtleX = -245
circTurtleY = 200

colsDrawn = 0
circleRows = 0

# creating our turtle objects for our 2 different shapes

# circle turtle
circTurtle = turtle.Turtle(shape="turtle")
circTurtle.color('blue', 'green')

# diamond turtle
diTurtle = turtle.Turtle(shape="turtle")
diTurtle.color('yellow', 'red')
sc = diTurtle.getscreen()

# use at beginning of loop before function call
diTurtle.penup()
diTurtle.setx(diTurtleX)
diTurtle.sety(diTurtleY)

circTurtle.penup()
circTurtle.setx(circTurtleX)
circTurtle.sety(circTurtleY)

# defining our turtle drawing functions for diamond and circle rows

def drawDiamonds():
    diTurtle.speed(8)
    diTurtle.pendown()
    diTurtle.begin_fill()
    diTurtle.left(45)

    diTurtle.forward(50)
    diTurtle.left(90)
    diTurtle.forward(50)
    diTurtle.left(90)
    diTurtle.forward(50)
    diTurtle.left(90)
    diTurtle.forward(50)
    diTurtle.left(90)
    diTurtle.end_fill()
    # prepare for next in row
    diTurtle.penup()
    diTurtle.right(45)
    diTurtle.forward(70.72)


def drawCircles():
    circTurtle.speed(8)
    circTurtle.pendown()
    circTurtle.begin_fill()
    circTurtle.circle(25)
    circTurtle.end_fill()
    # prepare for next in row
    circTurtle.penup()
    circTurtle.forward(70.72)

for line in range(int(rows)):
    circlesDrawn = 0
    colsDrawn = 0
    while colsDrawn <= (int(columns) - 1):
        drawDiamonds()
        while circlesDrawn < (int(columns) - 1) and circleRows < (int(rows) - 1):
            drawCircles()
            circlesDrawn += 1
        colsDrawn += 1
    circleRows += 1
    diTurtleY -= 70
    circTurtleY -= 70

    diTurtle.penup()
    diTurtle.setx(diTurtleX)
    diTurtle.sety(diTurtleY)

    circTurtle.penup()
    circTurtle.setx(circTurtleX)
    circTurtle.sety(circTurtleY)

sc.exitonclick()