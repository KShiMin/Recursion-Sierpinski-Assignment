import turtle
import math as m


def drawCircle(sqaureCor, mid, angle, myTurtle):
    # make line / shape not visible
    # myTurtle.penup()
    myTurtle.goto(sqaureCor[0][0], sqaureCor[0][1])
    myTurtle.goto(sqaureCor[1][0], sqaureCor[1][1])
    myTurtle.goto(sqaureCor[2][0], sqaureCor[2][1])
    myTurtle.goto(sqaureCor[3][0], sqaureCor[3][1])
    myTurtle.goto(sqaureCor[0][0], sqaureCor[0][1])
    myTurtle.goto(mid[1][0], mid[1][1])
    # make line / shape visible
    myTurtle.pendown()
    # draw circle
    myTurtle.circle(mid[0])
    # make line / shape not visible
    # myTurtle.penup()
    # myTurtle.forward(100)


def radiusLen(r):
    return r / 2


def midPointer(p1, p2):
    l = m.sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))
    diff = l / 2
    print((p1[0] + diff), (p1[1] + diff))
    return diff, ((p1[0] + diff), (p1[1]))


def sirepinski(sqaureCor, angle, degree, myTurtle):
    colour = ["blue", "red", "green", "cyan", "yellow", "violet"]
    drawCircle(sqaureCor, midPointer(sqaureCor[0], sqaureCor[1]), angle, myTurtle)

    # if degree > 0:
    # sirepinski(mid(r), myTurtle.left(90), degree - 1, myTurtle)
    # sirepinski(mid(r), myTurtle.left(180), degree - 1, myTurtle)


def main():
    myTurtle = turtle.Turtle()
    win = turtle.Screen()
    degree = 1
    square = [[-200, -200], [-200, 200], [200, 200], [200, -200]]
    radius = 100
    # set angle to draw circle
    angle = 90

    sirepinski(square, angle, degree, myTurtle)

    myTurtle.hideturtle()
    win.exitonclick()


main()
