from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=1000, height=600)
user_input = screen.textinput("Enter your Choice","Enter your choice from blue,purple,red,green")

x_position = [-430,-410,-420,-420]
y_position = [-240, -120,0,120]
cars = []
names = ['blue','purple','red','green']
for i in range(4):
    image_path= (f"images/car{i+1}.gif")
    screen.addshape(image_path)
    new_car = Turtle()
    new_car.name = names[i]
    new_car.shape(image_path)
    new_car.penup()
    new_car.goto(x_position[i],y_position[i])
    cars.append(new_car)



while True:
    car = random.choice(cars)
    if car.xcor()>=430:
        
        print("Winner: ",car.name)
        if user_input == car.name:
            print("You Won!!")
        else:
            print("You Lost")
        break
    car.forward(10)
screen.exitonclick()