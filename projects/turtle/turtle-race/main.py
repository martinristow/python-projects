from turtle import Screen, Turtle
import random
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
# First argument in textinput is title and second argument is prompt
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
number_of_turtles = len(colors)
# y = -100
# x = -230
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, number_of_turtles):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("fastest")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    # X-axis is along the horizontal , Y-axis is along the vertical
    # (Х-оската е по хоризонталата, Y-оската е долж вертикалата)
    # my_turtle.goto(x=x, y=y)
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    # y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
