import turtle
import math as m


# Function to draw square
def drawCarpet(point, colour, tur):
    tur.fillcolor(colour)
    tur.up()
    tur.begin_fill()
    tur.goto(point[0][0], point[0][1])
    tur.down()
    tur.goto(point[1][0], point[1][1])
    tur.goto(point[2][0], point[2][1])
    tur.goto(point[3][0], point[3][1])
    tur.goto(point[0][0], point[0][1])
    tur.end_fill()


def thirds(p1, p2, n):
    # Find each smaller square total length
    length = m.sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))
    # Find nth third length e.g. 1/3 of 300
    newlen = (n / 3) * length
    # Return coordinate of square
    return ((p1[0] + newlen), (p1[1] + newlen))


def sierpinski(point, degree, tur):
    colours = ['blue', 'red', 'green', 'aqua', 'yellow']
    drawCarpet(point, colours[degree], tur)

    if degree > 0:
        # All start from bottom left of drawn square
        # Bottom Left Square
        sierpinski([point[0], (point[0][0], thirds(point[0], point[1], 1)[1]), thirds(point[0], point[1], 1),
                    (thirds(point[0], point[3], 1)[0], point[0][1])], degree - 1, tur)

        # Middle Left Square starting from the top bottom square coordinates
        sierpinski([(point[0][0], thirds(point[0], point[1], 1)[1]), (point[0][0], thirds(point[0], point[1], 2)[1]),
                    (thirds(point[0], point[3], 1)[0], thirds(point[0], point[1], 2)[1]),
                    (thirds(point[0], point[3], 1)[0], thirds(point[0], point[1], 1)[1])], degree - 1, tur)

        # Top Left Square starting from top middle square coordinates
        sierpinski(
            [(point[0][0], thirds(point[0], point[1], 2)[1]), point[1], (thirds(point[1], point[2], 1)[0], point[1][1]),
             (thirds(point[0], point[3], 1)[0], thirds(point[0], point[1], 2)[1])],
            degree - 1, tur)

        # Top Middle Square starting from top left square bottom right coordinates
        sierpinski([(thirds(point[0], point[3], 1)[0], thirds(point[0], point[1], 2)[1]),
                    (thirds(point[1], point[2], 1)[0], point[1][1]), (thirds(point[1], point[2], 2)[0], point[1][1]),
                    (thirds(point[1], point[2], 2)[0], thirds(point[0], point[1], 2)[1])], degree - 1, tur)

        # Top Right Square starting from top middle square bottom right coordinates
        sierpinski([(thirds(point[1], point[2], 2)[0], thirds(point[0], point[1], 2)[1]),
                    (thirds(point[1], point[2], 2)[0], point[1][1]), point[2],
                    (point[2][0], thirds(point[3], point[2], 2)[1])], degree - 1, tur)

        # Middle Right Square starting from Top Right Square bottom left coordinates
        sierpinski([(thirds(point[0], point[3], 2)[0], thirds(point[3], point[2], 1)[1]),
                    (thirds(point[0], point[3], 2)[0], thirds(point[0], point[1], 2)[1]),
                    (point[2][0], thirds(point[3], point[2], 2)[1]), (point[2][0], thirds(point[3], point[2], 1)[1])],
                   degree - 1, tur)

        # Bottom Right Square starting from Middle Right Square bottom left coordinates
        sierpinski([(thirds(point[0], point[3], 2)[0], point[3][1]),
                    (thirds(point[0], point[3], 2)[0], thirds(point[3], point[2], 1)[1]),
                    (point[2][0], thirds(point[3], point[2], 1)[1]),
                    point[3]], degree - 1, tur)

        # Bottom Middle Square starting from Bottom Right square left coordinates
        sierpinski([(thirds(point[0], point[3], 1)[0], point[3][1]), thirds(point[0], point[1], 1),
                    (thirds(point[0], point[3], 2)[0], thirds(point[0], point[1], 1)[1]),
                    (thirds(point[0], point[3], 2)[0], point[3][1])], degree - 1, tur)


# Main functions
def main():
    # create turtle object
    myTur = turtle.Turtle()
    myTur.speed(2000)  # adjust the drawing speed here
    windows = turtle.Screen()

    # 4 points of the first square based on [x,y] coordinates
    points = [[-300, -300], [-300, 300], [300, 300], [300, -300]]
    degree = 4  # Vary the degree of complexity here

    sierpinski(points, degree, myTur)

    myTur.hideturtle()  # hide the turtle cursor after drawing is
    # completed

    windows.exitonclick()  # Exit program when user click on window


main()
