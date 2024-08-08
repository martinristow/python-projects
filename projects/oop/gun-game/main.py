from turtle import Screen
from turtle_player import TurtlePlayer
from ball import Ball
screen = Screen()
screen.title("Gun Game")
screen.bgcolor("black")
# screen.tracer(0)

turtle_player = TurtlePlayer()
balls = []


def shoot_ball():
    start_position = turtle_player.position()
    new_ball = Ball(start_position)
    balls.append(new_ball)


screen.listen()
screen.onkey(turtle_player.move_left, "a")
screen.onkey(turtle_player.move_right, "d")
screen.onkey(shoot_ball, "Up")


is_game_on = True
while is_game_on:
    for ball in balls:
        ball.move_up()
    screen.update()


screen.exitonclick()
