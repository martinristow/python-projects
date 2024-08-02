from art import logo,vs
from game_data import data
from random import choice

if_true = True
SCORE = 0

# Generate a random account from the game data.
def random_choose(data):
    choose_data = choice(data)
    data.remove(choose_data)
    return choose_data

 # Format the account data into printable format
def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

def check(user_guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    global SCORE
    # Use if statement to check if user is correct
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

# Display art
print(logo)

account_b = random_choose(data)

# Make the game repeatable
while if_true:
    # Making account at position B became the next account at position A.
    account_a = account_b
    account_b = random_choose(data)

    print(f"Compare A: {format_data(account_a)} .")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower count of each account
    account_a_followers = account_a["follower_count"]
    account_b_followers = account_b["follower_count"]

    is_correct = check(user_guess, account_a_followers,account_b_followers)

    # Check if user is correct
    if is_correct == True:
        # Score keeping
        SCORE+= 1
        # Give user feedback on their guess
        print(f"You're right! Current score: {SCORE}.")
    else:
        if_true = False
        print(f"Sorry, that's wrong. Final score: {SCORE}")

