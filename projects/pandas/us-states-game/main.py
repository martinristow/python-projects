import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
for i in range(20):
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    proverka = data[data["state"] == answer_state]
    state = proverka.state.iloc[0]
    x_cor = float(proverka.x.iloc[0])
    y_cor = float(proverka.y.iloc[0])

    turtle.penup()
    turtle.color("red")
    turtle.goto(x_cor, y_cor)
    turtle.write(state, align="center", font=("Arial", 10, "normal"))

screen.exitonclick()
