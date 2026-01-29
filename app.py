import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
def rectangle(y, z):
    t.forward(y)
    t.left(90)
    t.forward(z)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.forward(z)
    t.left(90)
rectangle(125, 100)

t.right(180)

def equal(x):
    t.forward(x)
    t.right(120)
    t.forward(x)
    t.right(120)
    t.forward(x)
    t.right(120)
equal(90)

t.left(90)
rectangle(50, 50)
rectangle(100, 100)
rectangle(150, 150)
rectangle(200, 200)
turtle.done()