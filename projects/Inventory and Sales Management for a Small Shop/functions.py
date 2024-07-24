product_list = []
initial_amount = 0

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
    for product in product_list:
        print(f"Name: {product["Name"]}, Quantity: {product["Quantity"]}, Price: {product["Price"]}")

# def home_page(text):
#     go_back = False
#     while not go_back:
#         if text == "yes":
#             go_back = True
#         elif text == "no":
#             continue

def update_quantity():
    print("List of all products in inventory with their quantities: ")
    for product in product_list:
        print(f"Name: {product["Name"]}, Quantity: {product["Quantity"]}")
        name = input("Product Name:")
        if product_exists(name):
            quantity = int(input("Write a new quantity:"))
            if quantity < 0:
                print("You entered a negative number!")
                continue
            product["Quantity"] = quantity
        print("Product not exists in the inventory.")


def update_price():
    print("List of all products in inventory with their prices:")
    for product in product_list:
        print(f"Name: {product["Name"]}, Price: {product["Price"]}")
        name = input("Product Name:")
        if product_exists(name):
            new_price = int(input(f"Enter a new price for {product["Name"]}"))
            if new_price <=0 or new_price >= 100:
                print("Product prices cannot be $0 or less than $0 and greater than $100.")
                continue
            product["Price"] = new_price
        print("Product not exists in the inventory.")