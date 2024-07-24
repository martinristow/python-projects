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