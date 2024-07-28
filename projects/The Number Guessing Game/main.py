from art import logo
import random
print(logo)
easy_level = 10
hard_level = 5
got_it = False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,101)
print(f"Pssst, the correct answer is {number}")

choose = input("Choose a difficulty. Type 'easy' or 'hard':")

if choose == "easy":
    print("You have 10 attempts remaining to guess the number.")
    user_choose = int(input("Make a guess: "))
    while not got_it:
        if easy_level == 0:
            print("You've run out of guesses, you lose.")
        else:
            if user_choose == number:
                print(f"You got it! The answer was {number}.")
                got_it = True
            elif user_choose > number:
                print("Too high.")
                print("Guess again.")
                easy_level -= 1
                print(f"You have {easy_level} attempts remaining to guess the number.")
                user_choose = int(input("Make a guess:"))
            elif user_choose < number:
                print("Too low.")
                print("Guess again.")
                easy_level -= 1
                print(f"You have {easy_level} attempts remaining to guess the number.")
                user_choose = int(input("Make a guess:"))
elif choose == "hard":
    print("You have 5 attempts remaining to guess the number.")
    user_choose = int(input("Make a guess: "))
    while not got_it:
        if easy_level == 0:
            print("You've run out of guesses, you lose.")
        else:
            if user_choose == number:
                print(f"You got it! The answer was {number}.")
                got_it = True
            elif user_choose > number:
                print("Too high.")
                print("Guess again.")
                hard_level -= 1
                print(f"You have {hard_level} attempts remaining to guess the number.")
                user_choose = int(input("Make a guess: "))
            elif user_choose < number:
                print("Too low.")
                print("Guess again.")
                hard_level -= 1
                print(f"You have {hard_level} attempts remaining to guess the number.")
                user_choose = int(input("Make a guess: "))