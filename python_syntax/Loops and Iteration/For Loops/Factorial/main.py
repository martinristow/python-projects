# Factorial
number = int(input("Enter a number:\n"))
if number < 0:
    print("You must enter a positive number!")
else:

    if number == 1 or number == 0:
        number = 1
        print(number)
    else:
        sum = 1
        for i in range(1,number+1):
            sum *= i
        print(sum)
