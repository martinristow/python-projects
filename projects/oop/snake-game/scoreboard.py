from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
MOVE = False
X_POSITION = 0
Y_POSITION = 270


# def read_high_score():
#     with open("data.txt", "r") as file:
#         score = int(file.read())
#     return score


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = read_high_score()
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=X_POSITION, y=Y_POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=MOVE, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", move=MOVE, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def write_high_score(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))
            # data.write(f"{self.high_score}")
