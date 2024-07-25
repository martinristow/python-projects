import functions

add = True

while add:
    print("\n")
    print("Add a new product press 1")
    print("Show all products in inventory press 2")
    print("Do you wanna update currently quantity of some product? Press 3")
    print("Price update? Press 4")
    print("Product remove? Press 5")
    print("Product Sell? Press 6")
    digit = int(input())
    if digit == 1:
        functions.add_new_product()
        # text = input("Do you want to go back? 'yes' or 'no'").lower()
        # functions.home_page(text)
    elif digit == 2:
        functions.show_inventory()
    elif digit == 3:
        functions.update_quantity()
    elif digit == 4:
        functions.update_price()
    elif digit == 5:
        functions.remove_product()
    elif digit == 6:
        functions.sell_product()
    else:
        break