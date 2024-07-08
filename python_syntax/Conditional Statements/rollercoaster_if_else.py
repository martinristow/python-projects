print("Welcome to the rollercoaster")

bill = 0
height = int(input("What is your height in cm ?"))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age ?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 10
        print("Adult tickets are $10.")

wants_photo = input("Would you like a photo? Y or N!")
if wants_photo == "Y":
    bill +=3
    print("Thank you!")
    print(f"Your bill is: ${bill}!")
else:
    print("Sorry, you have to grow taller before you can ride!")