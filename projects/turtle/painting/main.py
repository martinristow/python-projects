# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('Hirstspotpainting.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

from turtle import Screen
import turtle as t
from random import choice
my_turtle = t.Turtle()
t.colormode(255)


color_list = [
    (253, 253, 252), (242, 244, 247), (241, 247, 243), (144, 76, 50), (188, 165, 117),
    (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81),
    (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169),
    (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172),
    (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63),
    (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45)
]
my_turtle.penup()
my_turtle.speed("fastest")
my_turtle.hideturtle()
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    my_turtle.dot(20, choice(color_list))
    my_turtle.forward(50)

    if dot_count % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)

screen = Screen()
screen.exitonclick()


