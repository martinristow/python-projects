from art import logo
import random

print(logo)

easy_level = 10
hard_level = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,101)
print(f"Pssst, the correct answer is {number}")

choose = input("Choose a difficulty. Type 'easy' or 'hard':")

def check_guess(guess, number, attempts):
    """Checks the guess against the number and returns the remaining attempts."""
    if guess > number:
        print("Too high")
        return attempts - 1
    elif guess < number:
        print("Too low")
        return attempts - 1
    else:
        print(f"You got it. The answer is {number}")
        return 0

if choose == "easy":
    attempts = easy_level
else:
    attempts = hard_level

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    attempts = check_guess(user_guess,number,attempts)

    if attempts == 0 and user_guess != number:
        print("You've run out of guesses, you lose.")
        break
    elif user_guess == number:
        break
    else:
        print("Guess again.")
