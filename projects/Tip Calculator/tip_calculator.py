# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

bill = 0
percent = 0
people = 0

print("Welcome to Tip Calculator!")

bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

tip_percent = tip / 100 # we have a calculated percent
bill_with_tip_percent = tip_percent * bill
total_bill = bill + bill_with_tip_percent
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

final_amount = "{0:.2f}".format(bill_per_person) # rounding to two decimal places

print(f"Each person should pay: ${final_amount}")