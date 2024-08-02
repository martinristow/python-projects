class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name, price, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    # def calculate_total_price(self, price, quantity): # nema potreba pak kako parametri da gi zimame argumentite price i quantity
    # mozeme samo da gi izbriseme i da si gi povikuvame kako dolu vo istata funkcija
    #     return price * quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    # So __repr__ pravime ubav prikaz na nasite objekti. Namesto da imame object12131323 nekoj brojki tamu
    # mozeme so ovaa funkcija i nasite elementi da si gi prikazeme mnogu dobro objektite koj sto gi imame kreirano
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

# item1 = Item("Phone", 100, 3)
# # item2 = Item("Laptop", 1500, 6)
# #
# # print(item2.calculate_total_price())
# # print(item1.calculate_total_price())
# # print(Item.__dict__)  # All the attributes for Class level
# # print(item1.__dict__)  # All the attributes for instance level
#
# item1.apply_discount()
# # print(item1.price)
#
# item2 = Item("Laptop", 1500, 6)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
print(Item.all)