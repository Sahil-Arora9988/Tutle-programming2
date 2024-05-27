from turtle import Turtle, Screen

t = Turtle()
t.shape('turtle')
t.color('blue')
t.speed('fastest')

def draw_spirogragh(gap_size):
    angle = 0
    for circle in range(int(360/gap_size)):
        t.circle(100)
        t.setheading(angle)
        angle +=gap_size

draw_spirogragh(2)

s = Screen()
s.exitonclick()