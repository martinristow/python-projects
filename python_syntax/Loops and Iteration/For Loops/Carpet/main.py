number = int(input("Enter a number: "))
char = ""
for i in range(number):
    char += "*"
    print(char)

for i in range(number-1, 0, -1):
    print("*" * i)
