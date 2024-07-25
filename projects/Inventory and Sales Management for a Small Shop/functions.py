product_list = []
sell_product_list = []
income = 0
profit = 0

def product_exists(name):
    """
        Checks if a product with the given name exists in the product list.

        Args:
        name (str): The name of the product to check.

        Returns:
        bool: True if the product exists, False otherwise.
    """
    for product in product_list:
        if product["Name"] == name:
            return True
    return False
def add_new_product():
    """
       Adds a new product to the inventory if it does not already exist.

       Prompts the user for the product's name, quantity, and price.
    """
    name = input("What is the name of product: ")
    if not product_exists(name):
        quantity = int(input("What is the quantity that you will enter: "))
        price = float(input("What is the price of this product: "))
        product = {"Name": name, "Quantity": quantity, "Price": price}
        product_list.append(product)
    else:
        print("Product already exists in the inventory.")


def show_inventory():
    """
        Displays all products in the inventory along with their quantity and price.

        Also shows the total number of products in the inventory.
    """
    print("List of all products in inventory:")
    product_elem = 0
    for product in product_list:
        product_elem += 1
        print(f"Name: {product["Name"]}, Quantity: {product["Quantity"]}, Price: ${product["Price"]:.2f}")
    if product_elem == 0:
        print("Inventory is Empty!")
    else:
        print(f"Total number of products in inventory: {product_elem}")


def update_quantity():
    """
        Updates the quantity of a specific product in the inventory.

        Prompts the user for the product name and the new quantity.
    """
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
    """
       Updates the price of a specific product in the inventory.

       Prompts the user for the product name and the new price.
    """
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
                    print(f"Updated price for {name} to ${new_price:.2f}.")
                    break
    else:
        print("Product does not exist in the inventory.")


def remove_product():
    """
        Removes a specific product from the inventory.

        Prompts the user for the product name and confirms before removing it.
    """
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

def sell_product():
    """
        Sells a specified quantity of a product, updating the inventory and income.

        Prompts the user for the product name and quantity to sell.
    """
    global sell_product_list
    global income
    name = input("Product Name:")
    if product_exists(name):
        quantity = int(input("Enter the product quantity:"))
        if quantity < 0:
            print("You entered a negative number!")
        else:
            for product in product_list:
                if product["Name"] == name:
                    remaining_quantities = product["Quantity"] - quantity
                    if not remaining_quantities <= 0:
                        product1 = {"Name":name,"Quantity":quantity}
                        sell_product_list.append(product1)
                        product["Quantity"] -= quantity
                        income += product["Price"] * quantity
                        print(f"Product Sold: {name}. Remaining quantities :{remaining_quantities}.")
                        break
                    else:
                        print(f"The quantity you want to sell is not possible, because there are still products {product["Quantity"]} left")
    else:
        print("Product does not exist in the inventory.")


def warning_message():
    """
        Displays a warning message for products with low stock (less than 20 units).
    """
    print("List of low stock products:")
    for product in product_list:
        if product["Quantity"] < 20:
            print(f"Product {product["Name"]} has only {product["Quantity"]}  in stock.")


quantity = 0
def show_report():
    """
        Displays a report of the store's income, profit, and best-selling products.

        Best-selling products are those sold in quantities greater than 50.
    """
    global quantity
    global profit
    profit = income * 0.23
    print(f"The store's income amounts to: ${income}. Profit made: ${profit}")
    print("Best Selling Products:")
    for product in sell_product_list:
        quantity += product["Quantity"]
        if quantity > 50:
            print(f"{product["Name"]} : {product["Quantity"]}")

def add_promotions_or_discounts():
    """
        Adds a discount or promotion to a specific product.

        Prompts the user for the product name and discount percentage.
    """
    ask = input("Do you wanna add some discount of a product? Type 'yes' or 'no'!")
    if ask == "yes":
        name = input("What is the name of product you want to add a discount to?")
        if product_exists(name):
            discount = int(input("How much discount do you want to make on the product? Only Percentages(example '15')"))
            if discount < 0:
                print("Discount must be greater 0 percentages.")
            else:
                for product in product_list:
                    amount = product["Price"] * (discount / 100)
                    product["Price"] = product["Price"] - amount
        else:
            print("Product not exists in the inventory.")
def show_promotions_or_discounts():
    """
        Displays all products with their current discounted prices.
    """
    for product in product_list:
        print(f"{product["Name"]}: Discounted Price: ${product["Price"]:.2f}")
        print("End of discounted products list.")

def display_menu():
    """
        Displays the main menu with options for managing the inventory and sales system.
    """
    print("\n--- Inventory and Sales Management System ---\n")
    print("1. Add a new product")
    print("2. Show all products in inventory")
    print("3. Update the quantity of a product")
    print("4. Update the price of a product")
    print("5. Remove a product")
    print("6. Sell a product")
    print("7. Show warning messages (low stock)")
    print("8. Show sales report")
    print("9. Add a discount or promotion to a product")
    print("10. Show discounted products")
    print("0. Exit")
    print("--------------------------------------------")
