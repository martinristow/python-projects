import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.screensize(canvwidth=725, canvheight=491)
screen.addshape(image)
turtle.shape(image)

text_turtle = turtle.Turtle()
text_turtle.hideturtle()
data = pandas.read_csv("50_states.csv")
states_len = len(data)
all_states = data["state"].to_list()
correct_states = 0

is_game_on = True
list_of_states = []
dialog_title = "Guess the State"
winning_text = turtle.Turtle()
winning_text.hideturtle()

while is_game_on:
    if len(list_of_states) == 50:
        winning_text.write("Congrats you guessed all states in US!", align="center", font=("Arial", 20, "normal"))
        is_game_on = False
        break

    answer_state = screen.textinput(title=dialog_title, prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missed_states = []
        for state in all_states:
            if state not in list_of_states:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in list_of_states:
        # If the state has already been guessed, don't increase the score or display it again.
        continue

    check = data[data["state"] == answer_state]

    if not check.empty:
        # state = check.state.iloc[0]
        # x_cor = float(check.x.iloc[0])
        # y_cor = float(check.y.iloc[0])
        state = check.state.item()
        x_cor = float(check.x.item())
        y_cor = float(check.y.item())

        text_turtle.penup()
        text_turtle.color("red")
        text_turtle.goto(x_cor, y_cor)

        text_turtle.write(state, align="center", font=("Arial", 10, "normal"))

        correct_states += 1
        list_of_states.append(answer_state)  # Add the correctly guessed state to the list

        dialog_title = f"{correct_states} / {states_len} States Correct"
    else:
        continue

# screen.exitonclick()
