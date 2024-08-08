from turtle import Turtle

START_POSITION = (0, -250)
MOVE_DISTANCE = 12

class TurtlePlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.move_to_start_position()

    def move_to_start_position(self):
        self.goto(START_POSITION)

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.setx(new_x)

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.setx(new_x)
