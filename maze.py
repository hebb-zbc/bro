from turtle import *
# Help here https://docs.python.org/3/library/turtle.html
setup(1024,642) # set the window size to 480x360 pixels
bgcolor('yellow') # set BG to yellow
bgpic("maze.png") # BG pic only works with PNG and GIF
title("Mr. Stratton's Maze Tutorial") # Title of window

t = Turtle()


t.color("blue") # Colour line
# shape("arrow") # Shape of the turtle (“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”)
t.turtlesize(3) # size of turtle (easier for some kids to see)
t.pensize(3) # Set the size of the pen

t.penup()
t.goto(-412,260)
t.right(90)

t.pendown()
# vvvvvv Enter your code below here vvvvvv
