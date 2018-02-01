import turtle
import random

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        angle = random.randint(20, 40)
        t.right(angle)
        leng = random.randint(8, 15)
        tree(branchLen-leng,t)
        t.left(angle*2)
        leng = random.randint(8, 15)
        tree(branchLen-leng,t)
        t.right(angle)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()