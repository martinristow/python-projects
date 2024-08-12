def add(*args):
    print(args[2])
    sum = 0
    for number in args:
        sum += number
    return sum


total = add(3, 5, 10, 50, 40)
print(total)
