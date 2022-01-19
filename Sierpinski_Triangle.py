import turtle


def drawTriangle(points, colour, myTurtle):
    myTurtle.fillcolor(colour)
    myTurtle.up()  # Pen up
    myTurtle.begin_fill()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()  # Pen down
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, myTurtle):
    # Draw a triangle based on the 3 points given
    colours = ['blue', 'red', 'green', 'aqua', 'yellow', 'violet']
    drawTriangle(points, colours[degree], myTurtle)

    if degree > 0:
        # Recursion
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree - 1, myTurtle)
        sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree - 1, myTurtle)
        sierpinski([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree - 1, myTurtle)


def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(4)  # adjust the drawing speed here
    myWin = turtle.Screen()
    # 3 points of the first triangle based on [x,y] coordinates
    myPoints = [[-200, -50], [0, 200], [200, -50]]
    degree = 1  # Vary the degree of complexity here

    # first call of the recursive function
    sierpinski(myPoints, degree, myTurtle)

    myTurtle.hideturtle()  # hide the turtle cursor after drawing is
    # completed

    myWin.exitonclick()  # Exit program when user click on window


main()
