import turtle
import math as m


def drawCircle(point,radius,color,myTurtle):
    myTurtle.up()
    myTurtle.goto(point)
    myTurtle.down()
    myTurtle.fillcolor(color)
    myTurtle.begin_fill()
    myTurtle.circle(radius)
    myTurtle.end_fill()


def getNextRadius(radius):
    return radius / (1 + m.sqrt(2))
    
    
def sierpinski(point,radius,degree,skip,myTurtle):
    colormap = ['blue','red','green','cyan','yellow','violet','orange']
    drawCircle(point,radius,colormap[degree],myTurtle)
    nextRadius = getNextRadius(radius)

    if degree > 0:
        nextSkip = skip + 1

        if nextSkip > 4:
            nextSkip = 1

        # If skip is 1, it will move to the bottom after drawing the above code, however if skip changes, the pointer change
        # Therefore, sometimes when drawn the shape does not go in sequence and jump around

        # 1st circle (top left circle) is skipped
        # If skip = 2 / 3 / 4, start from bottom left
        if skip != 1:
            # Start from bottom left
            sierpinski([point[0]-nextRadius, point[1]+radius-2*nextRadius], nextRadius, degree-1, nextSkip, myTurtle)

        # 2nd circle (bottom left circle) is skipped
        # If skip = 1 / 3 / 4, start from top left
        if skip != 2:
            # Start from top left
            sierpinski([point[0]-nextRadius, point[1]+radius], nextRadius, degree-1, nextSkip, myTurtle)
        
        # 3rd circle (top right circle) is skipped
        # If skip = 1 / 2 / 4
        if skip != 3:
            # Go to the right of the circle drawn during if skip != 2
            sierpinski([point[0]+nextRadius, point[1]+radius], nextRadius, degree-1, nextSkip, myTurtle)
        
        # 4th circle (bottom right circle) is skipped
        # If skip = 1 / 2 / 3
        if skip != 4:
            # Go to the bottom of the circle drawn during if skip != 3
            sierpinski([point[0]+nextRadius, point[1]+radius-2*nextRadius], nextRadius, degree-1, nextSkip, myTurtle)


def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(2000)
    win = turtle.Screen()
    degree = 5
    point = [0,-250]
    radius = 250
    skip = 1

    sierpinski(point, radius, degree, skip, myTurtle)

    myTurtle.hideturtle()
    win.exitonclick()

main()
