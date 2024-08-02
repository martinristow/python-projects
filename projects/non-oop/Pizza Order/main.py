print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ?") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N ?") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N ?") # Do you want extra cheese? Y or N

bill = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25
cheese = 1

# Conditional checking for size of pizza
if size == "S":
  bill += small_pizza

elif size == "M":
  bill += medium_pizza

else:
  bill += large_pizza

# Conditional checking for pepperoni
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

# Conditional checking for extra cheese
if extra_cheese == "Y":
  bill += cheese

print(f"Your final bill is: ${bill}.")