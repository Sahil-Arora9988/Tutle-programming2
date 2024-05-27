from turtle import Turtle, Screen

t = Turtle()
s = Screen()
t.color('red')
t.shape("turtle")

def move_forward():
    t.forward(10)
def move_left():
    t.left(90)

def move_right():
    t.right(90)

def move_backward():
    t.backward(10)

s.listen()
s.onkey(key = 'w', fun = move_forward)
s.onkey(key = 'a', fun = move_left)
s.onkey(key = 's', fun = move_right)
s.onkey(key = 'd', fun = move_backward)

s.exitonclick()