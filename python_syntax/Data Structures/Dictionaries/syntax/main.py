# syntax for define a dictionary is : {Key: Value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    123: "Hello numbers"
}

# print(programming_dictionary["Loop"])

# Adding a new items to dictionary
programming_dictionary["Variable"] = "A variable is a place where certain data is stored."

print(type(programming_dictionary))

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key) # That will return as a key
    print(programming_dictionary[key]) # That will return as a key value

