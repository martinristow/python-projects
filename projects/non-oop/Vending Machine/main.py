import time
from datas import MENU, resources

is_on = True
income = 0


# TODO: Turn off the Vending Machine by entering “off”
def turn_off_machine():
    """For maintainers of the coffee machine, they can use “off” as the secret
     word to turn off the machine. Your code should end execution when this happens."""
    global is_on
    print("Turning off the machine...")
    for i in range(3, 0, -1):
        print(f"The machine will turn off in the next {i} seconds!")
        time.sleep(1)
        if i == 1:
            print("The machine is now off.")
            is_on = False


# TODO: Generate and print a report of the current resource values and money when the user enters “report”.
def print_report():
    """Prints a report of resources and current income."""
    for item in resources:
        print(f"{item.title()}: {resources[item]}")
    print(f"Money: ${income}")


# TODO: Check if there are sufficient resources for the ordered product and notify if there are not enough.
def stock_sufficient(order_ingredients):
    """Check if there are sufficient resources for the ordered product."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"“Sorry, {item.title()} is out of stock.")
            return False
        return True


# TODO: Process coins.
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


# TODO: Check if the transaction is successful, handle money and provide change, or refund if insufficient.
def successfully_transaction(new_product, new_payment):
    """Check if the transaction is successful and handle money accordingly."""
    if new_payment >= new_product:
        global income
        income += new_product
        change = round(new_payment - new_product, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print(f"Sorry, that's not enough money. Money refunded.")
        return False


# TODO: Check for sufficient resources before giving a product, notify
#  if resources are insufficient, deduct the product from resources, and print a success message.
def give_product(product_name, order_ingredients):
    """Deduct the product from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {product_name}. Enjoy!")


while is_on:
    # TODO: Ask user what would you like to buy
    choose = input("What would you like to buy? (chips/candy/soda):")
    if choose == "off":
        turn_off_machine()
    elif choose == "report":
        print_report()
    else:
        product = MENU[choose]
        if stock_sufficient(product["ingredients"]):
            payment = process_coins()
            if successfully_transaction(product["cost"], payment):
                give_product(choose, product["ingredients"])
