import turtle
import math as m


def drawCircle(point,radius,color,myTurtle):
    myTurtle.up()
    print(point)
    myTurtle.goto(point)
    myTurtle.down()
    myTurtle.fillcolor(color)
    myTurtle.begin_fill()
    print("radius =", radius)
    myTurtle.circle(radius)
    myTurtle.end_fill()


def getNextRadius(radius):
    return radius / (1 + m.sqrt(2))
    
    
def sierpinski(point,radius,degree,skip,myTurtle):
    colormap = ['blue','red','green','cyan','yellow','violet','orange']
    drawCircle(point,radius,colormap[degree],myTurtle)
    nextRadius = getNextRadius(radius)
    print(skip)

    if degree > 0:
        nextSkip = skip + 1

        if nextSkip > 4:
            nextSkip = 1

        # 1st circle (top left circle) NOT skipped
        if skip != 1:
            # Starting point
            sierpinski([point[0]-nextRadius, point[1]+radius-2*nextRadius], nextRadius, degree-1, nextSkip, myTurtle)
            # sierpinski([point[0]+nextRadius, point[1]+radius-2*nextRadius], nextRadius, degree-1, nextSkip, myTurtle)

        # 2nd circle (bottom left circle) NOT skipped
        if skip != 2:
            # pass
            sierpinski([point[0]-nextRadius, point[1]+radius], nextRadius, degree-1, nextSkip, myTurtle)
        
        # 3rd circle (top right circle) NOT skipped
        if skip != 3:
            # pass
            sierpinski([point[0]+nextRadius, point[1]+radius], nextRadius, degree-1, nextSkip, myTurtle)
        
        # 4th circle (bottom right circle) NOT skipped
        if skip != 4:
            # pass
            sierpinski([point[0]+nextRadius, point[1]+radius-2*nextRadius], nextRadius, degree-1, nextSkip, myTurtle)

def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(2000)
    win = turtle.Screen()
    degree = 5
    point = [0,-100]
    radius = 200
    skip = 1

    sierpinski(point, radius, degree, skip, myTurtle)

    myTurtle.hideturtle()
    win.exitonclick()

main()
