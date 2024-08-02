import random

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock = '''
 _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''                     
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)     
'''

computer = [0,1,2]
computer_image = [paper, rock, scissors]


print("What do you choose? Type 1 for Rock, 0 or Paper or 2 for Scissors.")
user_choice = int(input())


if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:

    computer_choice = random.randint(0,2)
    print(computer_image[user_choice])

    print("Computer chose:\n")
    print(computer_image[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You Lose!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Win!")
    elif computer_choice > user_choice:
        print("You Win!")
    elif computer_choice < user_choice:
        print("You Lose!")
    elif user_choice == computer_choice:
        print("It's a tie!")