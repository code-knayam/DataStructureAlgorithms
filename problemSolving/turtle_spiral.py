import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(40)
        drawSpiral(myTurtle,lineLen-1)

drawSpiral(myTurtle,100)
myWin.exitonclick()