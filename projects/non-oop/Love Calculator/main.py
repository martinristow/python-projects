print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")

combined_names = name1 + name2
lower_names = combined_names.lower()

# true
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = t + r + u + e

# love
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_digit = l + o + v + e

digit = str(first_digit) + str(second_digit)
digit_converted = int(digit)

if digit_converted < 10 or digit_converted > 90:
  print(f"Your score is {digit_converted}, you go together like coke and mentos.")
elif digit_converted >= 40 and digit_converted <= 50:
  print(f"Your score is {digit_converted}, you are alright together.")
else:
  print(f"Your score is {digit_converted}.")

