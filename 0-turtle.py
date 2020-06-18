# -*- codign: utf-8 -*-

# Libraries
import turtle

def run():
    # Set Window
    window = turtle.Screen() # Set Object Graphic - Turtle in the actual window
    window.bgcolor("#0791e6") # Background color
    # Set Object
    turtleTemp = turtle.Turtle() # Start Object Turtle
    turtleTemp.color("white") # Set color
    # Speed Flag
    turtleTemp.speed(100)
    # Move Object
    steps = 106
    for i in range(steps):
        turtleTemp.forward(i * 2) # Steps
        turtleTemp.right(i * 10) # Angle of line

    # Complement
    for i in range(steps):
        count = (steps - i)
        turtleTemp.forward(count * 2) # Steps
        turtleTemp.right(count * 10) # Angle of line

    window.mainloop() # Make Loop to last functions


if __name__ == "__main__":
    run()
