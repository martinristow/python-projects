#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


f = open("invited_names.txt", "r")
length = len(f.readlines())

for _ in range(length):
    with open("starting_letter.txt", mode="r") as text:
        contents = text.read()


with open("invited_names.txt", mode="r") as names:
    name_text = names.read()

name_list = []
name_list += name_text.split("\n")


for name in range(length):
    x = contents.replace("[name]", f"{name_list[name]}")
    with open(f"{name_list[name]}.txt", mode="w") as write_in_file:
        write_in_file.write(x)





