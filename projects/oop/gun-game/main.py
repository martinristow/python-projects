from turtle import Screen
from turtle_player import TurtlePlayer
screen = Screen()
screen.title("Gun Game")
screen.bgcolor("black")
# screen.tracer(0)

turtle_player = TurtlePlayer()
screen.listen()
screen.onkey(turtle_player.move_left, "a")
screen.onkey(turtle_player.move_right, "d")


is_game_on = True
# while is_game_on:
#     pass

screen.exitonclick()
