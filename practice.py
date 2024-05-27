from turtle import Turtle, Screen

t = Turtle()
t.shape('turtle')
t.color('blue')

def draw_square():
    for square in range(4):
        t.forward(100)
        t.left(90)


for i in range(20):
    draw_square()
    t.right(45)
    t.penup()
    t.forward(10)
    t.pendown()
    t.left(45)

   





screen = Screen()
screen.exitonclick()