def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    result = round(celsius_to_fahrenheit(celsius), 3)
    print(f"{celsius} °C is equivalent to {result} °F")
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    result = round(fahrenheit_to_celsius(fahrenheit), 3)
    print(f"{fahrenheit} °F is equivalent to {result} °C")
else:
    print("This number is not valid. Only allowed numbers are 1 and 2!")
