import turtle
import math as m


# Function to draw square
def drawCarpet(point, tur):
    tur.up()
    print("\n1st Point:" ,point[0][0], point[0][1])
    tur.goto(point[0][0], point[0][1])
    tur.down()
    print("2nd Point:" ,point[1][0], point[1][1])
    tur.goto(point[1][0], point[1][1])
    print("3rd Point:" ,point[2][0], point[2][1])
    tur.goto(point[2][0], point[2][1])
    print("4th Point:" ,point[3][0], point[3][1])
    tur.goto(point[3][0], point[3][1])
    print("5th Point:" ,point[0][0], point[0][1])
    tur.goto(point[0][0], point[0][1])


def thirds(p1, p2,n):
    # Find each smaller square total length
    length = m.sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))
    # Find next smaller square coordinates
    diff = (n/3 * length)
    return ((p1[0] + diff), (p2[0] + diff))

def sierpinski(point, degree, tur):
    drawCarpet(point, tur)

    if degree > 0:
        # Bottom Left Square
        sierpinski([point[0], (point[0][0],thirds(point[0], point[1],1)[1]), thirds(point[0], point[1],1), (thirds(point[0], point[3],1)[0],point[0][1])],degree - 1, tur)
        
        # Middle Left Sqaure starting from the top bottom sqaure coordinates
        sierpinski([(point[0][0],thirds(point[0], point[1],1)[1]), (point[0][0],thirds(point[0], point[1],2)[1]), (thirds(point[0], point[3],1)[0],thirds(point[0], point[1],2)[1]), 
        (thirds(point[0], point[3],1)[0],thirds(point[0], point[1],1)[1])], degree-1, tur)
        
        # # Top Left Sqaure starting from it's orginial coordinates
        # sierpinski([point[1],(thirds(point[1], point[2], 1)[0],point[1][1]),(thirds(point[0], point[3],1)[0],thirds(point[0], point[1],2)[1]),(point[0][0],thirds(point[0], point[1],2)[1])], 
        # degree-1, tur)

        # # Top Middle Sqaure starting from top left sqaure right coordinates
        # sierpinski([(thirds(point[1], point[2], 1)[0],point[1][1]),(thirds(point[1], point[2],2)[0],point[1][1]), (thirds(point[1], point[2],2)[0],thirds(point[0], point[1],2)[1]),
        # (thirds(point[0], point[3],1)[0],thirds(point[0], point[1],2)[1])], degree-1, tur)


# Main functions
def main():
    # create turtle object
    myTur = turtle.Turtle()
    myTur.speed(4)
    windows = turtle.Screen()

    points = [[-300, -300], [-300, 300], [300, 300], [300, -300]]
    degree = 2

    sierpinski(points, degree, myTur)

    myTur.hideturtle()  # hide the turtle cursor after drawing is
    # completed

    windows.exitonclick()  # Exit program when user click on window


main()
