from turtle import Turtle
import random
BALL_COLORS = ["red", "blue", "green", ""]
CIRCLE_SIZE = (10, 10)
BALL_SPEED = 10

class Ball(Turtle):
    def __init__(self, start_position):
        super().__init__()
        self.create_ball(start_position)

    def create_ball(self, start_position):
        self.shape("circle")
        self.setheading(90)
        self.color(random.choice(BALL_COLORS))
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.goto(start_position)

    def move_up(self):
        new_y = self.ycor() + BALL_SPEED
        self.sety(new_y)


