
#name: Gael Diab
#email:gael.diab07@myhunter.cuny.edu

import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("khaki")


tess = turtle.Turtle()           # create tess and set some attributes
tess.color("darkblue")
tess.pensize(5)

alex = turtle.Turtle()           # create alex
alex.color("violet")
alex.pensize(5)

for i in range(4):
    tess.forward(100)
    tess.left(90)
    
alex.left(90)
alex.forward(100)
alex.right(30)
alex.forward(100)
alex.right(120)
alex.forward(100)
alex.right(120)
alex.forward(100)