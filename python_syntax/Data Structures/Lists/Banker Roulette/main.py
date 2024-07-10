import random

names_string = "Martin, Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
numbers_of_elements = len(names)
random_choise = random.randint(0, numbers_of_elements - 1)
print(names[random_choise] + " is going to buy the meal today!")