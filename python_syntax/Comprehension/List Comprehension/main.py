numbers = [1, 2, 3, 4]
new_numbers = [number * 2 for number in numbers]
print(new_numbers)

new_list = [number * 3 for number in range(1, 5)]
print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)
