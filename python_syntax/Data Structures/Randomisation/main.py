import random
import my_module # a reference to another module created by me
random_number = random.randint(1, 10)
print(random_number)

random_float = random.random()
print(random_float)

# 0.0000000.... - 4.9999999....
random_float_v1 = random.random() * 5
print(random_float_v1)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

print(my_module.pi) # printing a result from my_module