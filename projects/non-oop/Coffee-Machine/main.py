from functions import (print_report, process_coins, make_coffee,
                       is_transaction_successful, is_resource_sufficient)
from data import MENU
stop_machine = True


# TODO: Turn off the Coffee Machine by entering “off” to the prompt
def turn_off_machine():
    """For maintainers of the coffee machine, they can use “off” as the secret
     word to turn off the machine. Your code should end execution when this happens."""
    global stop_machine
    print("Turn Off!")
    stop_machine = False


while stop_machine:
    # TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    ask_user = input("What would you like? (espresso/latte/cappuccino):")

    if ask_user == "off":
        turn_off_machine()
    elif ask_user == "report":
        print_report()
    else:
        drink = MENU[ask_user]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(ask_user, drink["ingredients"])
