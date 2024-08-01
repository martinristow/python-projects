from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")


timmy.forward(100)
timmy.left(50)
timmy.forward(100)

my_screen = Screen()
my_screen.exitonclick()

print(timmy)
print(type(timmy))

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electic", "Water", "Fire"])

table.align = "l"
print(table)

table.align = "c"
print(table)

table.align["Type"] = "r"
print(table)



