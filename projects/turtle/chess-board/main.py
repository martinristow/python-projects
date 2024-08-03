import turtle as t
# Turtle setup
my_turtle = t.Turtle()
t.colormode(255)


# Function to draw a square
def draw_square(color):
    my_turtle.begin_fill()
    my_turtle.color(color)
    for _ in range(4):
        my_turtle.forward(50)
        my_turtle.right(90)
    my_turtle.end_fill()


my_turtle.penup()

# Hide turtle after completion
my_turtle.hideturtle()
# Total square of table
total_square = 64

# Setting the initial position of the turtle
my_turtle.speed("fastest")
my_turtle.setheading(225)
my_turtle.forward(260)
my_turtle.setheading(0)


# Function to draw a chessboard
def draw_chest():
    colors = ["black", "white"]  # 0 for black, 1 for white
    start_color = 0
    for row in range(8):
        for col in range(8):
            draw_square(colors[(start_color + col) % 2])
            my_turtle.forward(50)
        start_color = (start_color + 1) % 2
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(400)
        my_turtle.setheading(0)


# Drawing the chessboard
draw_chest()
# Close the screen with a click
screen = t.Screen()
screen.title("chess board")
screen.exitonclick()
