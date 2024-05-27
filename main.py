from turtle import Turtle, Screen

t = Turtle()
t.shape('turtle')
t.color('blue')
# i=100
# for square in range(5):
#     t.forward(i)
#     t.left(90)

# for i in range(10):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()
#     t.left(90)

for i in range(20):
    for square in range(4):
        t.left(90)
        t.forward(100)
    t.right(45)
    t.penup()
    t.forward(10)
    t.pendown()
    t.left(45)

   





screen = Screen()
screen.exitonclick()