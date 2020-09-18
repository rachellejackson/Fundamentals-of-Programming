"""
Problem prompt:

Farmer John has four fields of soybeans planted. There are three months left until
harvest time, and the almanac has forecast a very dry summer. Farmer John has 
decided to put in a new, more efficient irrigation system to water his soybean crops. 
His estimate is that the new system will cost about $10,000. Soybeans are going 
for about $9.86 a bushel, so Farmer John wants to harvest as many bushels of soybeans
as he possibly can. As he ponders on this problem, he sketches a map of his soybean 
fields that shows how the irrigation system will cover the crops.

The square ABCD has it's vertices located at the centers of four identical circles, 
which are the regions covered by the new circular irrigation system. Farmer John is intrigued by 
the pattern shown in the shaded region of the map, and wonders what the area of this shaded region is.

You have to solve two problems for this project:

1. Draw an image. 

2. Compute the area of this shaded region, given the the length of one of the sides of the 
square--which can be a real number--as user input. Your answer should be accurate to two 
decimal places.

User input may be console input, or may come from a text entry box in the GUI, or may come from 
mouse clicks in the window.

"""

def leftoverArea(sideLength):
    """
    Calculates the area leftover after four, quarter-circles are removed
    from a square given the side length of a square.

    Parameters:
        sideLength (float): the side length of a square

    Returns:
        leftover (float): the remaing area of thesquare after 
        quarter-circles are removed
    """
    squareArea = sideLength * sideLength
    radius = sideLength/2
    circleArea = radius * radius * math.pi
    leftover = squareArea - circleArea
    return leftover


def drawcircle(turtleName, radius, xcoordinate, ycoordinate):
    """
    Sends the turtle object (turtleName) to a coordinate point (x, y), draws a circle with a 
    given radius that the user inputs, and fills the circle with white. 

    Parameters:
        turtleName (string): name of turtle object drawing circle
        radius (float): radius of the circle
        xcoordinate (int): x-coordinate of center of circle
        ycoordinate (int): y-coordinate of center of circle        
    """
    turtleName.penup()
    turtleName.setposition(xcoordinate, ycoordinate)
    turtleName.pendown()
    turtleName.begin_fill()
    turtleName.fillcolor("white")
    turtleName.circle(radius)
    turtleName.end_fill()


def label(turtlename, xcoord, ycoord, letter):
    """
    Labels a coordinate point with an alphabetic character.

    Parameters:
        turtleName (string): name of turtle object labeling square
        xcoordinate (int): x-coordinate of the label
        ycoordinate (int): y-coordinate of the label  
        letter: the alphabetic character assigned to the coordinate
    """
    turtlename.penup()
    turtlename.setposition(xcoord, ycoord)
    turtlename.write(letter)



import turtle
import math


def main():
    """
    Uses Tkinter's turtles to sketch a map of Farmer John's fields. 
    """
    Bev = turtle.Turtle()
    Bev.pensize(2)

    #Calculates the area of the shaded region and returns errors/quits for invalid inputs.
    try:
        squaresidelength = float(input("Please enter the side length of square: "))
    except:
        print("Input must be a number. Exiting.")
        return None

    if squaresidelength <=0:
        print("Input must be greater than 0. Exiting.")
        return None

    Area = leftoverArea(squaresidelength)
    print("The area of the shaded region is %.2f" %Area)

    #Draws the square and fills it in with gray. 
    Bev.penup()
    Bev.setposition(50, 0)
    Bev.pendown()
    Bev.begin_fill()
    Bev.fillcolor("grey")
    for i in range(4):
        Bev.left(90)
        Bev.forward(100)
    Bev.end_fill()

    #Draws the four circles using a previously defined function.
    drawcircle(Bev, 50, 50, 50)
    drawcircle(Bev, 50, -50, 50)
    drawcircle(Bev, 50, -50, -50)
    drawcircle(Bev, 50, 50, -50)

    #Labels the corners of the square using a previously defined function.
    label(Bev, 50, 100, "A")
    label(Bev, -60, 100, "B")
    label(Bev, -60, -15, "C")
    label(Bev, 50, -15, "D")

    #Redraws the square after it is covered by the circles.
    Bev.penup()
    Bev.setposition(50, 0)
    Bev.pendown()
    for i in range(4):
        Bev.left(90)
        Bev.forward(100)
    
