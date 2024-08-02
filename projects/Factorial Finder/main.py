number = int(input("Enter a number for Factorial Finder: "))
num = 1

for i in range(number, 0, -1):
    num *= i

print(f"Factorial of number {number} is {num}.")