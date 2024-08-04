# W = Forward
# S = Backward
# A = Counter-Clockwise
# D = Clockwise
# C = Clear drawing

from turtle import Screen, Turtle
my_turtle = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    my_turtle.forward(10)


def move_backward():
    my_turtle.forward(-10)


def move_left():
    my_turtle.left(10)


def move_right():
    my_turtle.left(-10)


def clear_screen():
    my_turtle.penup()
    my_turtle.clear()
    # my_turtle.setposition(0, 0)
    # my_turtle.setheading(0)
    my_turtle.home()
    my_turtle.pendown()


screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
