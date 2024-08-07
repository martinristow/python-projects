from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
MOVE = False
X_POSITION = 0
Y_POSITION = 270


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=X_POSITION, y=Y_POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=MOVE, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=MOVE, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
