# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# Simple Function
def greet():
    print("This is a first statement.")
    print("This is a second statement.")
    print("This is a third statement.")

greet()

print("\n")

# Function that allows for input
# name is a Parameter
# "Martin" is Argument
def greet_with_input(name):
    print(f"Hello {name}")
    print(f"How are you {name}")

greet_with_input("Martin")

# Functions with more than 1 input
def greet_with(name, age, sex, number):
    print(f"Welcome {name}, you are {age} old and your sex is {sex}. For more information call on my number {number}. ")

greet_with("Martin",22,"Male","000-999-999") # positional argument
greet_with("000-999-999","Male","22","Martin") # positional argument
print("\n")
greet_with(name = "Martin",age = 22,sex = "Male",number = "000-999-999") # Keywords argument
print("\n")
greet_with(age = 22, sex = "Male", number = "999-999-999", name = "Martin") # Keywords argument