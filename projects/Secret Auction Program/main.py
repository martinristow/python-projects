from replit import clear
from art import logo

print(logo)

adding_New_Person = True
binder_person = []
while adding_New_Person:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))

    new_person = {
        "name" : name,
        "bid" : bid
    }
    binder_person.append(new_person)

    ask_for_new_person = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if ask_for_new_person == "yes":
        # clear()
        continue
    elif ask_for_new_person == "no":
        adding_New_Person = False
        value = 0
        max_value = 0
        for i in binder_person:

            value = i["bid"]
            if max_value < value:
                name = i["name"]
                max_value = value

            print(f"The winner is {name} with a bid of ${max_value}.")
            break
    else:
        print("You should enter a 'yes' or 'no'!")