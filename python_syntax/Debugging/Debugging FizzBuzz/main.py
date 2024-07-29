# # Target is the number up to which we count
# target = int(input())
# for number in range(1, target + 1):
#   if number % 3 == 0 or number % 5 == 0: # or is bug
#     print("FizzBuzz")
#   if number % 3 == 0: # should be elif
#     print("Fizz")
#   if number % 5 == 0: # should be elif
#     print("Buzz")
#   else:
#     print([number]) # [] is bug

target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0: # Change 'or' into 'add'
    print("FizzBuzz")
  elif number % 3 == 0: # Change 'if' into 'elif'
    print("Fizz")
  elif number % 5 == 0:# Change 'if' into 'elif'
    print("Buzz")
  else:
    print(number) # Removed '[]'