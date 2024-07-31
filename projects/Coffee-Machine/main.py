MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# def check_price():
#     for i in MENU:
#         print(MENU[i]["cost"])
# check_price()



money = 0
stop_machine = True


# TODO: Print report.
def print_report():
    """When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g. """
    for resource in resources:
        if resource == "coffee":
            print(f"{resource}: {resources[resource]}g ")
        else:
            print(f"{resource}: {resources[resource]}ml ")
    print(f"Money: ${money}")


# TODO: Turn off the Coffee Machine by entering “off” to the prompt
def turn_off_machine():
    """For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens."""
    global stop_machine
    print("Turn Off!")
    stop_machine = False


# TODO: Process coins.
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


while stop_machine:
    # TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    ask_user = input("What would you like? (espresso/latte/cappuccino):")

    if ask_user == "off":
        turn_off_machine()

    elif ask_user == "report":
        print_report()
