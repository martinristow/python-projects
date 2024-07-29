############DEBUGGING#####################

# # Describe Problem
# def my_function():
#    for i in range(1, 20):
#      if i == 20:
#        print("You got it")
# my_function()

def my_function(): # This bug is fixed
   for i in range(1, 21): # The range should be from 1 to 21 if we want this function to be error free
    # print(i) # Result will be from 1 to 20
    if i == 20:
        print("You got it")
my_function()

# --------------------------------------------------------------------------------------------------------- #

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # The bug is number 6 because we do not have an element at index 6 in our list
# print(dice_imgs[dice_num])

from random import randint # This bug is fixed
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) # The exact randint is from index 0 to index 5
print(dice_imgs[dice_num])

# --------------------------------------------------------------------------------------------------------- #

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

year = int(input("What's your year of birth?")) # This bug is fixed
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994: # The bug was year > 1994 and was fixed with add year >= 1994
  print("You are a Gen Z.")

# --------------------------------------------------------------------------------------------------------- #

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# This bug is fixed
age = int(input("How old are you?")) # Added int() function to convert string into int digit
if age >= 18:
  print(f"You can drive at age {age}.") # Added miss f string

# --------------------------------------------------------------------------------------------------------- #

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# The bug is fixed
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) # The bug was double equal (==)
total_words = pages * word_per_page
print(total_words)

# --------------------------------------------------------------------------------------------------------- #

# #Use a Debugger
# def mutate(a_list):
#    b_list = []
#    for item in a_list:
#      new_item = item * 2
#     b_list.append(new_item) # The bug was in one missed space
#    print(b_list)
#
# mutate([1,2,3,5,8,13])

# The bug is fixed
def mutate(a_list):
   b_list = []
   for item in a_list:
     new_item = item * 2
     b_list.append(new_item) # After added one missed space, this function worked perfectly without any bugs
   print(b_list)
#
mutate([1,2,3,5,8,13])