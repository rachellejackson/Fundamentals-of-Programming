"""
Problem prompt:

A random walk is a particular kind of probabilistic (pseudo-random) simulation that models certain
statistical systems, such as Brownian motion of particles or molecules.  Coin flipping is an example
of a one-dimensional random walk--one dimensional because you only can go forward (when you flip heads)
or backward (when you flip tails) along a straight line.  Suppose you take a random walk of n steps.  
How many steps away from your starting point would you expect to end up on average, if you repeated 
the experiment many times?

Now suppose we make it two-dimensional. Suppose you can go forward, backward, left and right. 
How many steps away from your starting point would you expect to end up on average, if you repeated 
this experiment many times?

And finally, suppose instead of just four choices, we could go any direction? We can generate a random
direction using an angle from the x axis using equation 1.  Then we can use equations 2 and 3 to 
generate new positions for each time step.

(1) angle = random() * 2 * math.pi
(2) x = x + cos(angle)
(3) y = y + sin(angle)

Your program should take the number of steps as input. Assume the walker always starts at (0, 0) in
a 100 x 100 unit grid. Create a graphical program that will draw a line to trace the path of the walk
as it progresses. At the end, print out the straight-line distance and actual distance traveled to the
console or GUI, rounded to the nearest whole unit.  
"""

import math
import turtle
import random

def randwalk (turtlename, numberofsteps):
    """
    Sketches the random walk and calculates the Euclidean distance between the initial (0, 0) 
    and final points of the random walk.

    Parameters:
        turtleName (string): the name of the turtle object.
        numberofsteps (int): the number of steps to be taken to generate the random walk.

    Returns: 
        straightDistance (int): the Euclidean distance between the initial (0, 0) and final
        points of the random walk.
    """
    
    angle = 0
    x = 0
    y = 0
    totaldistancefromcenter = 0
    
    for i in range(numberofsteps):
        angle = random.random() * 2 * math.pi
        x = x + math.cos(angle)
        y = y + math.sin(angle)
        turtlename.setposition(x, y)
        straightDistance = math.sqrt(x**2 + y**2)
        
    return straightDistance
    
def main ():
    """
    Gets value from the user for the number of steps to be taken on the random walk, draws a 
    100 x 100 coordinate grid for the walk to take place on, and prints the distance traveled and 
    the Euclidean distance between the initial (0, 0) and final points of the random walk. 
    """

    #Gets and validates steps from user
    steps = int(input("Please input the number of steps: "))
    while (steps < 0):
        steps = int(input("Input must be positive. Please input the number of steps: "))
    Bev = turtle.Turtle()

    #Draw coordinate grid
    Bev.setposition(-50, 0)
    Bev.forward(100)
    Bev.penup()
    Bev.setposition(0, -50)
    Bev.pendown()
    Bev.left(90)
    Bev.forward(100)
    Bev.penup()
    Bev.setposition(0,0)
    Bev.pendown()

    #Sketches the random walk
    randwalk(Bev, steps)

    #calculates the distance between the initial and final points
    euclideanDistance= randwalk(Bev, steps)

    #Prints the distances
    print("The actual distance travelled was: %.f" %steps, "units.")
    print("The straight-line distance travelled was: %.f" %euclideanDistance, "units.")
    
