# import turtle
# tim = turtle.Turtle()
import random
from turtle import Screen
# This is not good for us
# from turtle import *
# from random import *

# Aliasing Modules
# keyword, Module name, keyword, alias name
# import turtle as t
# new_object = t.Turtle()
# new_object.left(100)

# Installing Modules
import heroes

print(heroes.gen())

# keyword, Module name, keyword, Thing in Module
import turtle as t

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red", "green")
#
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)


# Challenge 1 - Draw a Square
my_turtle = t.Turtle()
t.colormode(255)
# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)

# Challenge 2 - Draw a Dashed Line
# for _ in range(4):
# my_turtle.color("black")
# my_turtle.forward(10)
# my_turtle.color("white")
# my_turtle.forward(10)
# my_turtle.color("black")

# this way is better
# my_turtle.forward(10)
# my_turtle.penup()
# my_turtle.forward(10)
# my_turtle.pendown()


# Drawing Different Shapes
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

from random import choice
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         my_turtle.forward(100)
#         my_turtle.left(angle)
#
#
# for shape_side_n in range(3, 11):
#     my_turtle.color(choice(colours))
#     my_turtle.width(5)
#     my_turtle.speed(0.3)
#     draw_shape(shape_side_n)


# Generate Random RGB Colours
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

random_walk = [0, 90, 180, 270]

for _ in range(350):
    my_turtle.color(random_color())
    # my_turtle.width(10)
    # width or pensize
    my_turtle.pensize(15)

    # my_turtle.speed(0)
    my_turtle.speed("fastest")
    my_turtle.forward(30)
    my_turtle.setheading(choice(random_walk))


screen = Screen()
screen.exitonclick()
