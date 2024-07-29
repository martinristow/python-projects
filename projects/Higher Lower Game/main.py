from art import logo
from art import vs
from game_data import data
from random import choice
SCORE = 0
if_true = False

print(logo)
def random_choose(data):
    choose_data = choice(data)
    data.remove(choose_data)
    return choose_data
    # print(choose_data).

def proverka(proveri,proveri1,odgovor):
    global SCORE
    if odgovor =="A" and proveri["follower_count"] > proveri_1["follower_count"]:
        SCORE += 1
        print(f"You're right! Current score: {SCORE}.")
    elif odgovor == "B" and proveri["follower_count"] < proveri_1["follower_count"] :
        SCORE += 1
        print(f"You're right! Current score: {SCORE}.")
    else:
        print(f"Sorry, that's wrong. Final score: {SCORE}")


while not if_true:
    print(logo)
    proveri = random_choose(data)
    proveri_1 = random_choose(data)
    print(f"Compare A: {proveri["name"]}, a {proveri["description"]}, from {proveri["country"]}.")
    print(vs)
    print(f"Compare B: {proveri_1["name"]}, a {proveri_1["description"]}, from {proveri_1["country"]}.")
    ask = input("Who has more followers? Type 'A' or 'B': ")
    proverka(proveri, proveri_1, ask)
    if_true = True