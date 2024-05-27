from turtle import Turtle, Screen
import random

t = Turtle()
s = Turtle()
a= Turtle()
screen = Screen()

t.color("blue")
t.pensize(10)
t.shape("turtle")
s.color('red')
s.pensize(10)
s.shape("circle")
a.color("orange")
a.pensize(10)
a.shape("triangle")

def t_walk():
    t.setheading(random.choice([0,90,180,270]))
    t.forward(50)

def s_walk():
    s.setheading(random.choice([0,90,180,270]))
    s.forward(50)

def a_walk():
    a.setheading(random.choice([0,90,180,270]))
    a.forward(50)

for turtle in range(30):
    t_walk()
    s_walk()
    a_walk()


screen.exitonclick()

