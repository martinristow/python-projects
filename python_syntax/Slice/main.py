piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[2:5]) # Number 5 is not include in print list
print(piano_keys[1:])
print(piano_keys[:2])
print(piano_keys[::2])  # Last digit is increment
print(piano_keys[::-1])  # Reverse list

for item in piano_keys[::-1]:
    print(item)

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_tuple[1:4])
print(piano_tuple[::2])
print(piano_tuple[0:6:5])
