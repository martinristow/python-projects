# print(len(1234)) # an error will be returned here, because the length of an integer cannot be measured

num_char = len(input("What is your name?"))
print(type(num_char)) # type() -> return variable data type
# print("Your name has " + num_char + " characters.") # num_char is error

new_num_char = str(num_char)
# print(type(new_num_char))
print("Your name has " + new_num_char + " characters.") # this is correct version of Type Conversion


# Small Exercise
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input()

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two integers together
two_digit_number = first_digit + second_digit

print(two_digit_number)
