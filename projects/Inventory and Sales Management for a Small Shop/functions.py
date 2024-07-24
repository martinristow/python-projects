product_list = []
initial_amount = 0

stop_function = False
def product_exists(name):
    for product in product_list:
        if product["Name"] == name:
            return True
    return False
def add_new_product():
    name = input("What is the name of product: ")
    if not product_exists(name):
        quantity = int(input("What is the quantity that you will enter: "))
        price = float(input("What is the price of this product: "))
        product = {"Name": name, "Quantity": quantity, "Price": price}
        product_list.append(product)
    else:
        print("Product already exists in the inventory.")

    # print(product_list)


def show_inventory():
    print("List of all products in inventory:")
    product_elem = 0
    for product in product_list:
        product_elem += 1
        print(f"Name: {product["Name"]}, Quantity: {product["Quantity"]}, Price: {product["Price"]}")
    if product_elem == 0:
        print("Inventory is Empty!")
    else:
        print(f"Total number of products in inventory: {product_elem}")


# def home_page(text):
#     go_back = False
#     while not go_back:
#         if text == "yes":
#             go_back = True
#         elif text == "no":
#             continue

def update_quantity():
    show_inventory()
    name = input("Product Name:")
    if product_exists(name):
        quantity = int(input("Write a new quantity: "))
        if quantity < 0:
            print("You entered a negative number!")
        else:
            for product in product_list:
                if product["Name"] == name:
                    product["Quantity"] = quantity
                    print(f"Updated quantity for {name} to {quantity}.")
                    break
    else:
        print("Product does not exist in the inventory.")



def update_price():
    show_inventory()
    name = input("Product Name:")
    if product_exists(name):
        new_price = float(input(f"Enter a new price for {name}: "))
        if new_price <= 0 or new_price >= 100:
            print("Product prices cannot be $0 or less than $0 and greater than $100.")
        else:
            for product in product_list:
                if product["Name"] == name:
                    product["Price"] = new_price
                    print(f"Updated price for {name} to {new_price}.")
                    break
    else:
        print("Product does not exist in the inventory.")


def remove_product():
    show_inventory()
    name = input("Product Name:")
    for product in product_list:
        if product_exists(name):
            confirmation = input("Are you sure want to delete this product? Type 'yes' or 'no'")
            if confirmation == "yes":
                product_list.remove(product)
        else:
            print("Product not exists in the inventory.")
    show_inventory()