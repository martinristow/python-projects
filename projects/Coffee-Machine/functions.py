from data import resources
money = 0


# TODO: Generate and print a report of the current resource values and money when the user enters “report”.
def print_report():
    """When the user enters “report” to the prompt, a report should be generated
    that shows the current resource values. e.g. """
    for resource in resources:
        if resource == "coffee":
            print(f"{resource}: {resources[resource]}g ")
        else:
            print(f"{resource}: {resources[resource]}ml ")
    print(f"Money: ${money}")


# TODO: Process coins.
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


# TODO: Check if there are sufficient resources for the ordered drink and notify if there are not enough.
def is_resource_sufficient(order_ingredients):
    """Check if there are sufficient resources for the ordered drink."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: Check if the transaction is successful, handle money and provide change, or refund if insufficient.
def is_transaction_successful(money_received, drink_cost):
    """Check if the transaction is successful and handle money accordingly."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: Check for sufficient resources before making coffee, notify
#  if resources are insufficient, deduct ingredients if sufficient, and print a success message.
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name} ☕. Enjoy! ")
