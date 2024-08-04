from turtle import Screen, Turtle


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

for turtle_index in range(0, number_of_turtles):
    my_turtle = Turtle(shape="turtle")
    my_turtle.penup()
    my_turtle.color(colors[turtle_index])
    # X-axis is along the horizontal , Y-axis is along the vertical
    # (Х-оската е по хоризонталата, Y-оската е долж вертикалата)
    # my_turtle.goto(x=x, y=y)
    my_turtle.goto(x=-230, y=y_position[turtle_index])
    # y += 40


screen.exitonclick()
