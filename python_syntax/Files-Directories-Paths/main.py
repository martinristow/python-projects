file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()  # Osloboduvanje na resursite
print(contents)

with open("my_file.txt") as file: # drug nacin na otvaranje na datoteka
    contents = file.read()
    print(contents)
    # file.close() # koga ja otvarame datotekata na ovoj nacin
    # nema potreba da ja zatvarame bidejki toa samo se pravi

with open("new_file.txt", mode="a") as file: # mode="w" -> stariot text ke bide zamenet
    # so nov text, mode="a" -> na stariot text ke se dodade i noviot text
    # mode="r" -> samo citame od datotekata i ne moze da vrsime nikakva modifikacija
    file.write("\nNew text.")


