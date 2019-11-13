#KoshyFunctions
import turtle
bob = turtle.Turtle()

def polygon(sides,distance,color):
    bob.color(color)
    angle = 360/sides
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
def star(distance,color):
    bob.color(color)
    for times in range(5):
        bob.forward(distance)
        bob.right(144)
def explosion(d,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(8):
        bob.forward(d)
        bob.right(135)
    bob.end_fill()
def fiveCircle(d,c):
    a = 360/5
    for times in range(5):
        bob.color(c)
        bob.circle(25)
        bob.left(a)
        bob.forward(d)
