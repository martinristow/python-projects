fruits = ["Apple","Orange","Lemon"]

for fruit in fruits:
    print(fruit)
    print(fruit + " is very good fruit.")
print(fruits)


print("\n")
# for loops with range
for number in range(1,10): # Only numbers 1 to 9 are printed. Increase by 1
    print(number)

print("\n\n")

# Increase by other number
for number in range(1, 11, 3): # Increase by 3
    print(number) # output will be 1, 4, 7 and 10.
   # Explanation 1, 1 + 3 = 4, 4 + 3 = 7, 7 + 3 = 10

print("\n\n")

# Gauss
total = 0
for number in range(1, 101):
    total += number
print(total) # Output will be 5050. Matches Gauss's value!
