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

for i in range(60):
    print(i)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(95)

turtle.done()