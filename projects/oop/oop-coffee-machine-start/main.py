from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

stop_machine = False

while not stop_machine:
    option = menu.get_items()
    ask_user = input(f"What would you like? {option}: ")
    if ask_user == "off":
        stop_machine = True
    elif ask_user == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(ask_user)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


