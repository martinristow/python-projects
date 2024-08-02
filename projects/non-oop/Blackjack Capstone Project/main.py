import random
from art import logo


want_play = False

def card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_card_sum = 0
    card_sum_computer = 0
    first_card = random.choice(cards)
    second_card = random.choice(cards)
    computer_first_card = random.choice(cards)
    computer_card_list = [computer_first_card]

    card_lists = [first_card, second_card]
    user_card_sum = sum(card_lists)

    print(f"Your cards: {card_lists}, current score: {user_card_sum}")
    print(f"Computer's first card: {computer_first_card}")
    ask_for_another_card = input("Type 'y' to get another card, type 'n' to pass:")

    if ask_for_another_card == "y":
        card_lists.append(random.choice(cards))
        card_sum = sum(card_lists)
        print(f"Your cards: {card_lists}, current score: {card_sum}")
        print(f"Computer's first card: {computer_card_list}")
    elif ask_for_another_card == "n":
        computer_card_list.append(random.choice(cards))
        card_sum_computer = sum(computer_card_list)
        print(f"Your final hand: {card_lists}, final score: {user_card_sum}")
        print(f"Computer's final hand: {computer_card_list}, final score: {card_sum_computer}")

    if user_card_sum > card_sum_computer:
        print("Opponent went over. You win 😁")
    elif user_card_sum < card_sum_computer:
        print("You went over. You lose 😭")
    else:
        print("Draw")
def play(answer):
    formated_answer = answer.lower()
    if formated_answer == "y":
        want_play = True
        while want_play:
            print(logo)
            card()
            break

play(answer =input("Do you want to play a game of Blackjack? Type 'y' or 'n':"))